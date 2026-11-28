# Second Sight: gaps closed and Saturday plan

Companion to [`power_plant.md`](power_plant.md). Written Saturday 28 November, 01:30.

---

## Part 1. Gaps we closed, from the first idea to now

The first version was the team's proposal *Integrated Space-Based Cyber-Physical Threat Detection for Power Plants*, then the strategy guide in `moa-raw/cassini_power_plant_hackathon_strategy.md`.

| # | Gap in the earlier version | How we closed it | Evidence |
|---|---|---|---|
| 1 | **Read as an "AI platform".** The brief warns against vague AI + satellite claims, and we had no attack data to train on | No trained model. Physics (power curves, irradiance) plus transparent verdict rules printed on screen | Section 7.2 |
| 2 | **Thermal example didn't hold up.** Sentinel-2 has no thermal band; Sentinel-3 is ~1 km and daily, too coarse for a SCADA attack lasting minutes | Dropped plant thermal as the headline. Wind and PV output from ERA5 and CAMS, which is the right physics for the assets that were attacked | Section 2 |
| 3 | **Fully simulated demo.** No real SCADA, network or CTI data | Replay of a real, documented attack: 29 December 2025 in Poland (CERT Polska), on real Copernicus and ENTSO-E data | Sections 1, 10 |
| 4 | **Scope too wide** for 48 hours: four data sources plus AI | One question: is the asset physically running, and is the evidence safe? Two space inputs that matter, one engine | Section 5 |
| 5 | **NO2 vs ENTSO-E already published** (2026 paper on 18 plants, Climate TRACE on Bełchatów) | Kept as background only; not our innovation claim | Section 3 |
| 6 | **Galileo spoofing detection already placed** (3rd, 2024) and the CERT reports never mention GNSS | Galileo's job is now authenticated time on an evidence log outside the plant. The CERT supplement shows why: PLC and firewall logs were wiped | Sections 2, 7.3 |
| 7 | **OSNMA overclaim.** Earlier I suggested OSNMA could authenticate published ENTSO-E or PGE data. It can't | Removed. OSNMA only stamps what our own receiver logs | Section 2 |
| 8 | **No answer to "why not Dragos or Nozomi?"** | Structural blind spot: they share the attacker's network path. In December the RTUs, routers and logs were the target. We have no network path into the plant | Section 1 table |
| 9 | **Unverified legal facts** (KSC dates and fines) | Verified: in force 3 April 2026, implementation deadline 3 April 2027, personal fines up to 300% of monthly pay, penalties generally not before two years after entry into force | Section 4 |
| 10 | **No EU vision** | NCCS roadmap (2027 controls, 2028 reports, ACER indicators from 2027), Cybersecurity Act revision on PV remote access, inverter phase-out, Grids Package, European Space Shield | Section 4 |
| 11 | **No asset register** | JRC-PPDB-OPEN for large units (official resource); ESA APEx PV farm mapping and wind turbine detection on Sentinel-2 for small farms (official resource) | Sections 2, 5 |
| 12 | **No resilience angle** | Resilience assessment mode with five metrics: register gap, observability under blackout, verification error, evidence survival, classification delay | Section 8 |
| 13 | **Risk of crying wolf** | Second real replay: Rogowiec 2021, ten Bełchatów units tripped from human error. Engine must say "non-weather trip, investigate", not "cyber" | Section 8 |
| 14 | **Operator misdiagnosis not addressed** | New verdict `NON_WEATHER_TRIP`, so a stopped turbine isn't filed as a contractor error by default | Section 7.2 |
| 15 | **No code** | `second_sight/`: data fetcher (ENTSO-E, ERA5, CAMS, JRC) and engine (physics band, verdicts, hash chained evidence log). Self-test passes | `second_sight/README.md` |

### Gaps still open
1. **No practitioner.** The one stated reason a past winner won. Highest priority Saturday.
2. **No real numbers yet.** The backtest has only run on synthetic files.
3. **Latency.** ERA5 and CAMS are days behind. We present a replay and say live use needs forecasts and nowcasts.
4. **The 30 attacked farms aren't public.** We use detected or public farms and say so.
5. **Attribution differs** (CERT: Berserk Bear cluster; Dragos: ELECTRUM). Pitch says "Russia-linked".
6. **Still marked [VERIFY]:** CER Directive article and dates, ACER indicator definitions, JRC Polish coverage, PV MW per hectare, APEx wind algorithm ID and run time.

---

## Part 2. Saturday task list

Schedule anchors: mentoring at **11:30** and **16:30**; go/no-go at **12:00**; submission **Sunday 15:00**, pitches from 15:05.

### Early morning (before 10:00)
- [ ] **Everyone:** read `power_plant.md` sections 1, 7.2 and 10 (15 min)
- [ ] **Data:** register ENTSO-E (Transparency Platform, then email for API token), Copernicus CDS, SoDa (CAMS), CDSE (APEx). ENTSO-E is slowest, do it first
- [ ] **Data:** `python second_sight/fetch_dec29.py jrc` (no key). Check how many Polish units, and whether Bełchatów and the CHP plants are there
- [ ] **Engine:** `python second_sight/engine.py --selftest`, then plug OSNMAlib into `time_source()` or load recorded OSNMA data
- [ ] **GNSS:** if not done Friday, test GnssLogger Galileo navigation messages by a window
- [ ] **Pitch:** read the CERT Polska PDFs (January and August) for any detail on how long telemetry was lost

### Morning (10:00 to 12:00)
- [ ] **Data:** `fetch_dec29.py entsoe` and `era5` as soon as keys arrive; check Polish wind and solar for 28 to 30 December has no gaps
- [ ] **Data:** run APEx PV farm mapping and wind turbine detection on one Polish region on CDSE
- [ ] **Engine:** `engine.py --backtest` on real data; write down MAE and band coverage
- [ ] **Front end:** console skeleton: timeline and verdicts first, map second
- [ ] **Pitch:** prepare three questions for mentors (below)

### 11:30 mentoring
- [ ] Ask every mentor: *"Do you know anyone at a DSO, PSE, PGE or CERT Polska we could talk to today?"*
- [ ] Ask: *"Would an operator trust a physics estimate of farm output during a telemetry outage? What error would be acceptable?"*
- [ ] Ask: *"Is the external evidence log with Galileo time useful to an incident responder?"*
- [ ] Get one quotable sentence, with permission to cite name and role or anonymised

### 12:00 go/no-go
- [ ] If the national wind backtest tracks ENTSO-E within a usable band: wind + PV headline
- [ ] If not: PV only, plus the CHP evidence story
- [ ] If ENTSO-E keys haven't arrived: use a manual CSV export from the Transparency Platform website

### Afternoon (12:00 to 18:00)
- [ ] **Data:** Rogowiec 2021 per-unit data (`fetch_dec29.py rogowiec`); confirm the drop shows
- [ ] **Engine:** per-farm bands for the APEx-detected assets; run the 29 December replay through the verdict rules; evidence log entries with OSNMA time
- [ ] **Engine:** resilience metrics for the demo region
- [ ] **Front end:** KSC early warning draft (JSON + PDF); evidence log viewer showing tamper detection
- [ ] **Pitch:** verify CER and ACER facts; first full deck draft

### 16:30 mentoring
- [ ] Show the replay. Ask: *"What would make you mark this down?"* Fix the top answer tonight

### Evening
- [ ] Full rehearsal with timer (5 min)
- [ ] Record a backup video of the demo
- [ ] Pre-cache all data so the demo runs offline

### Sunday morning
- [ ] Final numbers on slides (only numbers the code produced)
- [ ] Fill the submission: 2 page summary, roles, video, challenge link, space data used, APIs and libraries, hardware, GitHub link
- [ ] Submit before 15:00

### Hard rules
- No number on a slide until the code produces it.
- Say "replay on real data", never "real time".
- Say "Russia-linked", not a specific group.
- Never claim satellites saw the CHP turbine stop.
