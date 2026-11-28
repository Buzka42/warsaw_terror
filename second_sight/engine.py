"""Second Sight core: physics band, verdict rules, hash-chained evidence log.

Run the offline self-test (synthetic data, no network):
  python engine.py --selftest

Run the national wind backtest on real data (after fetch_dec29.py entsoe + era5):
  python engine.py --backtest
"""
import hashlib
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data"

# ---------------------------------------------------------------- physics

CUT_IN, RATED, CUT_OUT = 3.0, 12.0, 25.0  # m/s, generic onshore turbine at hub height ~100 m


def wind_capacity_factor(ws):
    """Generic power curve: cubic between cut-in and rated, flat to cut-out, zero beyond."""
    ws = np.asarray(ws, dtype=float)
    cf = np.clip((ws**3 - CUT_IN**3) / (RATED**3 - CUT_IN**3), 0.0, 1.0)
    cf[(ws < CUT_IN) | (ws >= CUT_OUT)] = 0.0
    return cf


def pv_capacity_factor(ghi_w_m2, performance_ratio=0.8):
    return np.clip(np.asarray(ghi_w_m2, dtype=float) / 1000.0 * performance_ratio, 0.0, 1.0)


@dataclass
class Band:
    """Expected output band, calibrated as scale * physics_cf plus residual quantiles."""
    scale: float = 1.0
    lo_q: float = 0.0
    hi_q: float = 0.0

    @classmethod
    def fit(cls, physics_cf, actual, q=(0.05, 0.95)):
        x, y = np.asarray(physics_cf), np.asarray(actual)
        ok = np.isfinite(x) & np.isfinite(y)
        x, y = x[ok], y[ok]
        scale = float((x @ y) / (x @ x))  # least squares through origin
        resid = y - scale * x
        return cls(scale, float(np.quantile(resid, q[0])), float(np.quantile(resid, q[1])))

    def predict(self, physics_cf):
        mid = self.scale * np.asarray(physics_cf)
        return np.maximum(mid + self.lo_q, 0), mid, mid + self.hi_q


# ---------------------------------------------------------------- verdicts

def verdict(telemetry_mw, lo, hi, prev_telemetry_mw=None, physics_dropped=False):
    """Rules from power_plant.md section 7.2. telemetry_mw=None means telemetry lost."""
    if telemetry_mw is None:
        # Physics says it should be producing (lower bound above zero): the operator is blind, not the plant.
        return "BLIND" if lo > 0 else "BLIND_LOW_CONFIDENCE"
    if lo <= telemetry_mw <= hi:
        return "NORMAL"
    dropped = prev_telemetry_mw is not None and telemetry_mw < 0.5 * prev_telemetry_mw
    if dropped and physics_dropped:
        return "WEATHER"
    if dropped:
        return "NON_WEATHER_TRIP"
    return "SUSPECT_TELEMETRY"


def regional_escalation(verdicts, threshold=3):
    bad = [v for v in verdicts if v in ("BLIND", "NON_WEATHER_TRIP", "SUSPECT_TELEMETRY")]
    return "COORDINATED_EVENT" if len(bad) >= threshold else None


# ---------------------------------------------------------------- evidence log

def time_source():
    """Placeholder. Replace with OSNMAlib output: (GST time, 'AUTHENTICATED')."""
    return datetime.now(timezone.utc).isoformat(), "UNAUTHENTICATED_SYSTEM_CLOCK"


@dataclass
class EvidenceLog:
    path: Path
    entries: list = field(default_factory=list)

    def append(self, record):
        t, status = time_source()
        prev = self.entries[-1]["hash"] if self.entries else "0" * 64
        body = {"seq": len(self.entries), **record, "time": t, "time_status": status, "prev_hash": prev}
        body["hash"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
        self.entries.append(body)
        with open(self.path, "a") as f:
            f.write(json.dumps(body) + "\n")
        return body

    @staticmethod
    def verify(path):
        prev = "0" * 64
        for line in open(path):
            e = json.loads(line)
            h = e.pop("hash")
            if e["prev_hash"] != prev or hashlib.sha256(json.dumps(e, sort_keys=True).encode()).hexdigest() != h:
                return False, e["seq"]
            prev = h
        return True, None


# ---------------------------------------------------------------- real backtest

def backtest():
    import xarray as xr
    ds = xr.open_dataset(DATA / "era5_pl_100m.nc")
    tdim = "valid_time" if "valid_time" in ds.dims else "time"
    ws = np.hypot(ds["u100"], ds["v100"])
    # Spatial mean of capacity factor over the box. Next step: weight by real farm locations.
    cf = xr.apply_ufunc(wind_capacity_factor, ws).mean(dim=["latitude", "longitude"])
    cf = cf.to_series().tz_localize("UTC")
    cf.index.name = "time"

    act = pd.read_csv(DATA / "entsoe_pl_wind_onshore.csv", index_col=0, parse_dates=True)
    act.index = pd.to_datetime(act.index, utc=True)
    act = act.iloc[:, 0].resample("1h").mean()

    df = pd.concat({"cf": cf, "actual": act}, axis=1).dropna()
    train = df[df.index < "2025-12-27"]
    test = df[(df.index >= "2025-12-28") & (df.index < "2025-12-31")]
    band = Band.fit(train.cf, train.actual)
    lo, mid, hi = band.predict(test.cf)
    out = test.assign(lo=lo, mid=mid, hi=hi)
    inside = ((out.actual >= out.lo) & (out.actual <= out.hi)).mean()
    mae = (out.actual - out.mid).abs().mean()
    out.to_csv(DATA / "backtest_dec28_30.csv")
    print(f"scale={band.scale:.0f} MW, band=[{band.lo_q:.0f}, +{band.hi_q:.0f}] MW")
    print(f"28-30 Dec: MAE={mae:.0f} MW, actual inside band {inside:.0%} of hours")


# ---------------------------------------------------------------- self-test

def selftest():
    rng = np.random.default_rng(0)
    ws = rng.gamma(4, 2, 2000)
    cf = wind_capacity_factor(ws)
    assert cf.min() >= 0 and cf.max() <= 1 and wind_capacity_factor([30])[0] == 0
    actual = np.maximum(9000 * cf + rng.normal(0, 300, cf.size), 0)  # real output is never negative
    band = Band.fit(cf, actual)
    assert abs(band.scale - 9000) < 200, band.scale
    lo, mid, hi = band.predict(cf)
    cover = ((actual >= lo) & (actual <= hi)).mean()
    assert 0.85 < cover < 0.95, cover

    assert verdict(None, 10, 16) == "BLIND"
    assert verdict(12, 10, 16) == "NORMAL"
    assert verdict(2, 10, 16, prev_telemetry_mw=12, physics_dropped=True) == "WEATHER"
    assert verdict(0, 10, 16, prev_telemetry_mw=12) == "NON_WEATHER_TRIP"
    assert verdict(30, 10, 16, prev_telemetry_mw=29) == "SUSPECT_TELEMETRY"
    assert regional_escalation(["BLIND"] * 3) == "COORDINATED_EVENT"

    p = Path("/tmp/second_sight_selftest.jsonl")
    p.unlink(missing_ok=True)
    log = EvidenceLog(p)
    for i in range(5):
        log.append({"asset": f"PL-WF-{i:04d}", "verdict": "BLIND"})
    assert EvidenceLog.verify(p) == (True, None)
    lines = p.read_text().splitlines()
    tampered = json.loads(lines[2]); tampered["verdict"] = "NORMAL"; lines[2] = json.dumps(tampered)
    p.write_text("\n".join(lines) + "\n")
    assert EvidenceLog.verify(p) == (False, 2)
    print(f"selftest ok: band coverage {cover:.0%}, tampering detected at entry 2")


if __name__ == "__main__":
    {"--selftest": selftest, "--backtest": backtest}[sys.argv[1]]()
