"""Fetch the real data for the 29 December 2025 replay.

Needs free accounts, read from environment variables:
  ENTSOE_TOKEN   ENTSO-E Transparency Platform security token
  ~/.cdsapirc    Copernicus CDS API key (for ERA5)
  SODA_EMAIL     email registered at soda-pro.com (for CAMS irradiance)

Usage:
  python fetch_dec29.py entsoe   # Polish wind + solar actual generation, Nov-Dec 2025
  python fetch_dec29.py rogowiec # Belchatow per unit, 16-18 May 2021
  python fetch_dec29.py era5     # 100 m wind over Poland, Nov-Dec 2025
  python fetch_dec29.py cams     # irradiance at sample PV sites, Dec 2025
  python fetch_dec29.py jrc      # JRC-PPDB-OPEN power plant register (no key needed)
"""
import os
import sys
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)
TZ = "Europe/Warsaw"
START = pd.Timestamp("2025-11-01", tz=TZ)
END = pd.Timestamp("2026-01-01", tz=TZ)

# Sample PV sites (lat, lon). Replace with farms from a citable register (URE / OSM).
PV_SITES = {
    "pv_west": (52.40, 16.90),
    "pv_south": (50.30, 19.00),
    "pv_east": (51.25, 22.57),
}


def entsoe():
    from entsoe import EntsoePandasClient
    c = EntsoePandasClient(api_key=os.environ["ENTSOE_TOKEN"])
    for psr, name in [("B19", "wind_onshore"), ("B16", "solar")]:
        df = c.query_generation("PL", start=START, end=END, psr_type=psr)
        # entsoe-py may return several columns (e.g. Actual Aggregated / Consumption): keep the first one
        s = df.iloc[:, 0] if isinstance(df, pd.DataFrame) else df
        s.rename(name).to_csv(DATA / f"entsoe_pl_{name}.csv")
        print(name, s.shape, "missing hours:", int(s.isna().sum()))


def rogowiec():
    from entsoe import EntsoePandasClient
    c = EntsoePandasClient(api_key=os.environ["ENTSOE_TOKEN"])
    df = c.query_generation_per_plant(
        "PL",
        start=pd.Timestamp("2021-05-16", tz=TZ),
        end=pd.Timestamp("2021-05-19", tz=TZ),
        psr_type="B02",  # fossil brown coal / lignite
    )
    df.to_csv(DATA / "entsoe_pl_lignite_units_2021-05.csv")
    print("lignite units", df.shape)


def era5():
    import cdsapi
    days = [f"{d:02d}" for d in range(1, 32)]
    req = {
        "product_type": ["reanalysis"],
        "variable": ["100m_u_component_of_wind", "100m_v_component_of_wind"],
        "year": ["2025"],
        "month": ["11", "12"],
        "day": days,
        "time": [f"{h:02d}:00" for h in range(24)],
        "area": [55.0, 14.0, 49.0, 24.2],  # N, W, S, E: Poland
        "data_format": "netcdf",
    }
    cdsapi.Client().retrieve("reanalysis-era5-single-levels", req, str(DATA / "era5_pl_100m.nc"))


def cams():
    from pvlib.iotools import get_cams
    for name, (lat, lon) in PV_SITES.items():
        df, meta = get_cams(lat, lon, pd.Timestamp("2025-12-01"), pd.Timestamp("2025-12-31"),
                            email=os.environ["SODA_EMAIL"], identifier="cams_radiation", time_step="15min")
        df.to_csv(DATA / f"cams_{name}.csv")
        print(name, df.shape)


def jrc():
    """JRC Open Power Plants Database v1.0 (Zenodo 3574566). Prints the Polish units."""
    import io, urllib.request, zipfile
    url = "https://zenodo.org/records/3574566/files/JRC-PPDB-OPEN.ver1.0.zip?download=1"
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
    z.extractall(DATA / "jrc_ppdb_open")
    for name in z.namelist():
        if name.lower().endswith(".csv") and "unit" in name.lower():
            df = pd.read_csv(DATA / "jrc_ppdb_open" / name, low_memory=False)
            cc = next((c for c in df.columns if c.lower() in ("country", "country_code")), None)
            pl = df[df[cc].astype(str).str.upper().isin(["PL", "POLAND"])] if cc else df
            pl.to_csv(DATA / "jrc_ppdb_pl_units.csv", index=False)
            print(name, "Polish units:", len(pl))
            print(pl.head(20).to_string())


if __name__ == "__main__":
    {"jrc": jrc, "entsoe": entsoe, "rogowiec": rogowiec, "era5": era5, "cams": cams}[sys.argv[1]]()
