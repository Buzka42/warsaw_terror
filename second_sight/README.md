# Second Sight: code

Design doc: [`../power_plant.md`](../power_plant.md)

```bash
pip install entsoe-py cdsapi pvlib xarray netCDF4 pandas numpy
python engine.py --selftest          # offline, no keys needed

export ENTSOE_TOKEN=...              # transparency.entsoe.eu, account settings
export SODA_EMAIL=...                # soda-pro.com account (CAMS)
# ~/.cdsapirc with your CDS key      # cds.climate.copernicus.eu
python fetch_dec29.py entsoe
python fetch_dec29.py era5
python fetch_dec29.py cams
python fetch_dec29.py rogowiec
python engine.py --backtest          # national wind: ERA5 physics vs ENTSO-E, 28 to 30 Dec 2025
```

Status: `--selftest` passes; `--backtest` verified end to end on synthetic files only. Not yet run on real data (needs the keys above).

Next steps: weight the wind capacity factor by real farm locations; per-farm bands; plug OSNMAlib into `time_source()`; console and KSC PDF.
