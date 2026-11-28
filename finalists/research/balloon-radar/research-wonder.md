Verdict incoming — verifying every load-bearing claim (CAMS winds, OSNMA keys, EGNOS-on-phone, SondeHub timing) before scoring this.CAMS pressure-level winds look doubtful from the catalogue — now checking OSNMA timing, EGNOS protection levels, and the legal wall for ATC.Live-wind fallback and radiosonde physics check out — now probing phone GNSS chipsets, closure economics, and Polish incidents.# Balloon Radar — Hard Review (Sat 28 Nov, ~36h to submission)

**Overall:** Memorable problem, real numbers, falsifiable demo — and three subsystems (forecast, OSNMA, EGNOS-RTKLIB) where each alone can eat a weekend. The forecast core is buildable. The GNSS stack as written is not, on unknown phones, in the time left. Cut scope now or the demo dies in integration.

---

## 1. Technical implementation, component-by-component

### 1.1 Live wind: CAMS — doc's `[VERIFY]` resolves YES, but it's the wrong tool for this job

- **Severity: MAJOR**
- **Evidence:** CAMS global forecasts do expose `u_component_of_wind`/`v_component_of_wind` on pressure levels — a worked ECMWF notebook retrieves exactly that at 850 hPa via `cdsapi` from `cams-global-atmospheric-composition-forecasts`. So Path "CAMS live" is not a fantasy. **But:** CAMS horizontal resolution is 0.4°×0.4° (~40 km) and multi-level data is only **3-hourly**, vs ERA5 0.25° hourly. A balloon at 10 m/s wind moves 108 km in one 3h CAMS step — your "linear in time" interpolation is smoothing over the entire Vilnius–border corridor.
- **Fix (Sat morning, 1h):** Use CAMS only as the *labelled Copernicus live source* for the slide, but run the actual demo trajectory on **ECMWF IFS open data via Open-Meteo** (`ecmwf_ifs025`, no API key, pressure-level JSON) or `ecmwf-opendata`. Open-Meteo serves pressure-level forecasts as JSON with no key for non-commercial use. Say on-slide: *"Live winds: ECMWF IFS (model behind Copernicus CAMS); replay & land cover: Copernicus ERA5/CLMS."* Honest, and jurors from IGiK will respect the disclosure more than a 40 km wind field dressed as precision. Do **not** claim CAMS = Sentinel — the doc is right that Copernicus ≠ Sentinels only, but see §2.

### 1.2 ERA5 replay

- **Severity: MINOR (doc is right)**
- **Evidence:** ERA5 is history-only, ~5 days behind real time, free account + licence accepted once per dataset in browser. New CDS (post-Sep 2024) requires re-accepting licences; old keys are dead.
- **Fix:** Create CDS + ADS accounts **this morning**, accept ERA5 + CAMS licences in the web form *before* touching `cdsapi` (API fails silently otherwise), request one Vilnius incident bbox (53–57°N, 22–28°E, 1000–200 hPa, hourly) and **cache the NetCDF offline**. CDS queue times on tape-backed pressure-level ERA5 can be hours — never request live on stage.

### 1.3 Drift engine + Monte Carlo (500 members, midpoint, log-p interpolation)

- **Severity: MINOR — sound, buildable in a day.** This is standard advection; `numpy`+`xarray` trilinear/log-p interpolation at 30–60s steps for 500 members × ~3h flight is trivial compute (<1 min). Chi-square ellipse scaling in doc (1.386 / 4.605 for 2 dof) is correct.
- **Real bug risk:** converting geopotential (ERA5 `z`, m²/s²) to geometric altitude — divide by 9.80665, and balloons float on *pressure* surfaces more than geometric altitude; interpolate wind in log-p directly against the balloon's pressure altitude, don't round-trip through geometric height. Also: sampled "wind perturbation" as white noise per-member is wrong — it under-disperses. Perturb per-member with a constant wind bias (e.g. ±1–2 m/s rotated) so trajectories actually separate.

### 1.4 Smuggling-balloon flight profile — priors are findable, doc hasn't found them

- **Severity: BLOCKER for credibility (not for code)**
- **Evidence:** Public reporting gives usable priors the doc calls `[ASSUMPTION]`: balloons fly "up to 11 km altitude", other reporting says "cheap helium balloons at 3–4 km altitude — aircraft height — carry crates of cigarettes with GPS trackers", loads of 500–1,500 packs, each with a GPS transmitter. Polish cases: up to 1,500 packs per balloon.
- **Why blocker:** 3 km vs 11 km float altitude in sheared winds = landing points tens of km apart. Your 90% ellipse will be enormous or wrong. A ChipCraft/IGiK juror asking "where did 3–11 km come from?" gets `[ASSUMPTION]` today.
- **Fix (2h research, Sat):** One "Assumptions" slide: float 2–8 km (bracket the 3–4 km and 11 km reports), ascent 3–6 m/s (weather-balloon class), descent = balloon leak/burst + payload parachute-less drop reported from recovered debris. Cite VSAT/LRT reports. State calibration loop. This converts a blocker into a shown-known-unknown.

### 1.5 Threat layer / corridors (OurAirports)

- **Severity: MINOR (data fine, concept naive)**
- **Evidence:** OurAirports is public domain, nightly CSVs with runway end coordinates.
- **Problem:** A 10 NM × ±1 NM centreline box surface-to-ceiling is **not** how ATC protects approaches (it's a funnel by glidepath altitude, plus radar vectoring areas). With a surface-to-X ceiling box you'll over-alert: any balloon drifting at 5 km over the centreline 9 NM out is not a conflict for an aircraft at 900 m on final.
- **Fix:** Intersect in 3D: corridor altitude = glidepath (3° from threshold) ± tolerance, capped ~1,200 m. Only count members whose *altitude at crossing* is in-band. This also fixes the "P(conflict)=1.0 all night" problem partially (§6).

### 1.6 SondeHub validation

- **Severity: MAJOR — timing in the build plan is wrong**
- **Evidence:** Legionowo RS41 flights in Nov 2026 data: first frame ~11:18 UTC, last ~13:14 UTC, ~1h55 flight, consistent with ~5 m/s ascent to 30–35 km. Launches are 00/12 UTC nominal. SondeHub live API exists: `https://api.v2.sondehub.org/sondes/live` returns lat/lon/alt/time JSON, plus a `sondehub` PyPI streaming SDK.
- **Consequences:** (a) Sat "13:00 CET dress rehearsal on the 12 UTC launch" — 13:00 CET = 12:00 UTC, the sonde launches ~12:18 CET and lands ~14:15 CET; your rehearsal *starts* at launch, fine, but landing error isn't known until ~14:30 CET. (b) Sun: launch ~12:18 CET, **landed by ~14:20 CET — at 15:05 pitch it is not "live", it's finished.** That's actually *better* (you can show final landing error live-computed), but the script's "real radiosonde on screen live" claim will be visibly false — a grey landed marker.
- **Fix:** Rewrite demo beat: *"Launched 12:18 today, landed 14:1x near X. Our 12:20 forecast landing ellipse vs actual: error Y km — computed an hour ago, not cherry-picked."* Pre-register the forecast (screenshot/timestamp/hash posted before landing) so jury believes no refit. Fallback: Saturday's recorded flight, as doc says. Also note SondeHub's own Tawhiri predictor already runs predictions ~every 60s for flights in progress using GFS winds — your "baseline: SondeHub prediction" comparison is available via `https://api.v2.sondehub.org/tawhiri`; use it as *baseline only*, never as your engine (Fresh Code + it's the competitor).

### 1.7 Galileo OSNMA via GnssLogger + OSNMAlib — highest-risk component

- **Severity: BLOCKER as scoped (Path A on arbitrary team phones)**
- **Evidence:**
  - OSNMAlib is real, open Python, GitHub `Algafix/OSNMA`, maintained, with GnssLogger among its input sources — but a 2025 paper notes GnssLogger format can't distinguish E1B vs E5b I/NAV, and OSNMA bits exist **only on E1B**.
  - Android gives 228-bit I/NAV pages via `GnssNavigationMessage.getData()`, only E1 pages carry OSNMA; whether a given phone emits nav messages at all is chipset-dependent — "smartphones based on Broadcom GNSS chipsets provide navigation messages" (implying others may not). Raw measurements are mandatory on Android 10+, but nav-message emission is not guaranteed.
  - OSNMA keys: GSC registration + login, download `.crt` public key and Merkle-tree XML under GSC Products; current key rotated Dec 2025 (PKID 2) — old sample keys in repos will fail.
  - Time-to-first-authenticated-fix: ~100 s typical hot-start, 44–69 s optimised, *in ideal/open-sky conditions*; cold start only at 6-hourly key broadcasts. Indoors at a Warsaw venue: assume **no fix at all**.
- **Fix (decision by Sat 12:00, as doc's own gap list says):** This morning, outside, run GnssLogger 10 min on *every team phone*; grep log for Galileo nav messages (type 1537). If none: Path B immediately — OSNMAlib's official test vectors / a recorded SBF/UBX log — and demo it as *"verification pipeline on recorded border-zone data"*. Budget max 3h total on Path A. Also pre-download current PKID-2 `.crt` + Merkle XML after GSC registration today; registration is manual-ish, don't leave to Sunday.

### 1.8 EGNOS server-side via RTKLIB SBAS — demo-able, claim is overcooked

- **Severity: MAJOR**
- **Evidence:**
  - RTKLIB does support SBAS correction input as RTKLIB-format or **EMS (EGNOS Message Server) 2.0** files, and EMS+RTKLIB post-processing is published practice. EDAS is registration-controlled, near-real-time + FTP historical archive with EMS messages — registration via EGNOS Helpdesk is not instant self-serve.
  - Phone side: "as far as we know, there is no smartphone providing its position based on EGNOS corrections" (EGNOS programme Q&A); SBAS helps ~50% only in open-sky/rural, not multipath-dominated environments. Phone RINEX conversion needs a converter (e.g. `raw_Android_to_rinex` → RINEX 3.05, then RTKLIB) — that's a third tool in the chain the doc omits.
  - HPL: DO-229 protection levels assume a certified airborne receiver model; a mid-range/non-DO-229 receiver's PLs demonstrably failed to bound errors (413 epochs exceeded) in testing. Your phone HPL is a number, not an integrity guarantee.
- **Fix:** Drop "holds up in court" / "seizure location holds up in evidence" everywhere (see §5). Demo claim becomes: *"EGNOS-corrected vs standalone position differed by X m on our log; we attach the correction provenance to the seizure record."* Use archived EMS file downloaded Sat, RTKLIB `rnx2rtkp -p 0` (single) with SBAS option offline. If RTKLIB build fights you (it will — old C code, use the `RTKLIB` Explorer fork / prebuilt binaries), cut EGNOS to a precomputed before/after screenshot. It is the most cuttable component with least Relevance loss.

### 1.9 Land cover (CORINE / HRL Tree Cover Density)

- **Severity: MINOR**
- **Evidence:** CORINE 2018 is 100 m raster GeoTIFF, downloadable pre-packaged or via CLMS API; Tree Cover Density now 10 m via CDSE. Multi-GB Europe mosaics — clip a small bbox for PL/LT *today*, cache GeoTIFF, `rasterio` zonal stats inside ellipse. Do not download on venue Wi-Fi. Note CLC 2018 vintage: a 2018 forest map for a 2026 seizure is fine for dispatch triage, say "indicative".

### 1.10 Frontend / webhooks / FastAPI

- **Severity: MINOR.** MapLibre + Telegram bot webhook is a half-day build. Only risk: venue network. Everything (§1.2, 1.6 replay, 1.8) must run from localhost with cached tiles (pre-render static map images or cache vector tiles for the two demo bboxes). Live SondeHub pull is the *only* allowed network dependency on stage, with Saturday recording behind it.

---

## 2. EU-space signal/data correctness

| Claim in doc | Verdict |
|---|---|
| ERA5 replay-only, days delay | ✅ Correct |
| CAMS live winds on pressure levels | ✅ Exists but 0.4°, 3-hourly multi-level — coarser than the approach-corridor geometry you're intersecting with |
| Radiosonde validates wind model, not smuggling profile | ✅ Honest and correct; RS41 ~5 m/s, burst 30–35 km vs smuggler float 3–11 km |
| "OSNMA tells patrol GPS isn't lying" | ⚠️ Overclaim. OSNMA authenticates *navigation data*, increases spoof detection, "does not prevent their occurrence. Nor does it protect against jamming" — EUSPA's own words. It does not authenticate pseudoranges/PVT; replay/meaconing still works. Pitch line must become *"tells the patrol whether Galileo nav data is authentic — one spoofing class detected, jamming still blind"* or ChipCraft jurors will correct you publicly. Note also OSNMA only covers Galileo E1B — a phone navigating mostly on GPS L1 gets no protection for those satellites. |
| "EGNOS makes seizure location hold up in court" | ❌ Overclaim. SBAS HPL integrity (DO-229) presumes certified equipment; a post-processed phone fix has no chain-of-custody, no certified receiver, metre-level multipath noise. A cyber-defence juror + any lawyer-adjacent mentor will kill this. Replace with "documented, reproducible correction provenance". |
| GNSS threat near border is real | ✅ Strongly supported: interference "particularly pronounced in north-eastern Poland, near the border with Lithuania… Suwałki Gap"; spoofing reach ~450 km covering Baltics/most of Poland reported 2026. This is your best Galileo justification — use these specifics. |
| No Sentinel anywhere | ⚠️ Relevance risk (doc's own ranking flags it). Mitigation is legitimate: Copernicus services = C3S/CAMS/CLMS, not only Sentinels. But add one Sentinel-flavoured layer only if free: e.g. Sentinel-2 true-colour backdrop via CDSE static tile for the landing ellipse. Do not build change detection. |

**Signal-geometry nitpick jurors may catch:** balloons at 3–4 km are *at aircraft height on approach* only within ~40 km of an airport on a 3° path… actually at 10 NM (~18.5 km) aircraft are ~1 km up. Balloons drifting *through* 0–1.2 km during ascent/descent near the airport are the conflict; a balloon floating at 8 km over EYVI is an en-route (FIR) problem, not a runway-closure problem. Your threat layer must say which regime it's alerting on — currently it conflates them (§1.5 fix handles this).

---

## 3. Demo risk

| Risk | Sev | Mitigation executable by Sun 12:00 |
|---|---|---|
| Sunday sonde already landed by pitch (see §1.6) — "live" claim false on screen | **MAJOR** | Reframe as completed, timestamped forecast-vs-actual; keep live map as backdrop |
| Venue indoors: no GNSS fix, no OSNMA, no EGNOS demo | **BLOCKER if attempted live** | Never do live GNSS on stage. Pre-record outside Sat; screen-record OSNMAlib output |
| CDS/ADS queue or licence not accepted → no ERA5 replay data | **MAJOR** | Download + cache Sat morning; replay must run 100% offline |
| SondeHub lag / no Legionowo flight Sunday (weather/ops scrub) | **MAJOR** | Saturday flight recording + replay are the primary demo; Sunday is bonus. Pitch must work with zero live elements |
| Phone exposes no Galileo nav messages | **BLOCKER for Path A** | Sat 12:00 Path A/B gate (§1.7) |
| EDAS registration pending | **MAJOR** | Use EMS archive file; if unavailable, precomputed RTKLIB result screenshot; cut if needed |
| Telegram webhook on venue Wi-Fi fails | MINOR | Send alert to a phone on mobile data; also show it in UI. Record one arriving |
| Team size: doc plans "two people", prompt says team is 3–6 | **MAJOR (execution score)** | Assign explicit owners today: forecast / GNSS / frontend+pitch / practitioner+business. The 7-component scope (§5 of doc) for 2 people in 48h is not credible; for 4 with cuts (§8) it is |

---

## 4. Jury pushback — first hard question per archetype

- **ChipCraft (GNSS chip engineers):** *"Your phone's chipset — does it even output E1B I/NAV pages, and how do you handle OSNMA's ~100s TTFAF and 30s time-sync requirement in a jammed environment where you may have no trusted time?"* Have the phone model + chipset + a real log line ready, or Path B honesty.
- **IGiK (remote sensing academics):** *"CAMS at 0.4°/3-hourly — what's your trajectory error growth vs ERA5, and did you validate ellipse calibration (coverage), not just one landing error?"* Show: actual-in-90%-ellipse yes/no across *all* Nov Legionowo flights you can replay (SondeHub archive gives you ~daily flights — run 5–10 replays Sat night, report coverage + median error vs Tawhiri baseline). One flight is an anecdote; ten is validation.
- **Scanway (space optics):** *"Why no optical/EO confirmation layer — how do you know it's a balloon and not a drone/bird?"* Answer prepared: detection is out of scope/operator radar; you're the forecast layer. Don't improvise a Sentinel balloon-spotting claim (a 10 m Sentinel-2 pixel will not see a balloon — saying otherwise loses all credibility with this juror).
- **Blue Dot Solutions (EO experts):** *"Tawhiri and HYSPLIT exist, SondeHub already predicts every sonde. What's your 10×?"* Answer: threat layer + dispatch + authenticated patrol, with the replay lead-time number. Without that number (§6) you have no answer.
- **Cyber Defence Forces / WAT:** *"OSNMA doesn't stop jamming or meaconing, EGNOS position from a phone isn't evidentiary, and you're building targeting-adjacent prediction for objects from a hostile state — dual-use/export and operational-security implications?"* Concede OSNMA limits precisely (§2), drop court claim, frame defensive civil-protection use.
- **ESA BIC Poland:** *"Who signs the first cheque, how much, and why won't they build this in-house in a month?"* See §5 — currently unanswerable.

---

## 5. Buyer, business, legal/procurement

- **Severity: BLOCKER for business-viability third of score — "SaaS per airport" as written.**
- **Safety-case wall (real):** An ANSP cannot operationally shorten closures on your say-so. EU 2017/373 requires a safety (support) assessment for changes to the functional system. Procurement + safety case + integration with ATM systems = multi-year, classified-adjacent radar feeds you don't have. **Reframe (Sat, zero code):** sell *decision-support / situational awareness for the supervisor and airport duty manager*, explicitly "human decides, we quantify". Sell first to **border guards and airport operations** (lower certification bar) and to ANSP as analytics, not ATM equipment.
- **Money numbers are wrong in the doc:** "passenger compensation claims" — balloon/security closures are textbook *extraordinary circumstances*; EU261 €250–600 is owed only when cause is within airline control. Airlines' real cost is diversion/handling/rebooking care, not EU261 cash. Use verified scale instead: ~60h closures, 300+ flights, ~47,000 passengers in 2025; one night ~11h closure, 50 flights, 7,400 passengers. Price hypothesis: if you save even 2 closure-hours/year at one airport you cover a €30–60k/yr licence — state it as hypothesis with those inputs, not "subscription TBD".
- **Poland angle is real and should lead locally:** balloons crossed into Poland multiple nights, civil-aviation restrictions over Podlaskie, dozens recovered in Podlaskie/Białystok, ~120 Podlaskie Border Guard incidents reported. For a Warsaw jury, PAŻP + Podlaski Oddział SG are your named first customers, Vilnius is the proof case.
- **Market honesty:** ~5 ANSPs + ~10 airports + 2 border guards in the affected corridor is a *wedge*, not a market. The generalisation (plumes, drifting debris, HAB/UAS drift) must be one credible sentence, not the pitch. ESA BIC juror will accept "Baltic pilot → NATO eastern-flank civil protection" if the pilot path is grant-funded (EDF/EUDIS, ESA BIC) — name the instrument.
- **Legal/IP:** OSNMAlib (check its licence before commercial claims), Tawhiri API is non-commercial — do not ship a product on it. CORINE/ERA5 attribution (CC BY) must be on slides.

---

## 6. Rule compliance & saturation

- **Fresh Code: CONDITIONAL PASS.** Writing your own drift/Monte Carlo/threat layer over libraries (`xarray`, `cdsapi`, OSNMAlib, RTKLIB) is exactly the allowed pattern stated in the doc. **Violation traps:** (1) calling SondeHub Tawhiri API as your predictor — that's using an existing trajectory predictor as the product; use only as baseline. (2) Any pre-weekend code in the repo — keep git history clean from Friday, commit early/often as proof. (3) OSNMAlib/RTKLIB are libraries — allowed explicitly ("open/public libraries and APIs allowed"), say so in submission README with versions pinned.
- **EU Space requirement: PASS but thin.** Active use: ERA5/CAMS (Copernicus C3S/CAMS), CLMS land cover, Galileo OSNMA (real verification, even Path B recorded data counts if *you* run the verification), EGNOS EMS messages in RTKLIB. That's genuinely all three pillars — stronger than most Sentinel-dashboard rivals. Risk is perception (no satellite imagery) — mitigate with the data-flow slide naming dataset IDs (`reanalysis-era5-pressure-levels`, `cams-global-atmospheric-composition-forecasts`, CLC2018 100m).
- **Saturation: LOW — genuine differentiator.** As doc says, it's not a jamming heatmap / Sentinel-2 dashboard / dark-vessel clone. Balloon smuggling is, however, a *known* 2025–26 news topic; another Warsaw team may pick it. Your moat in-room is the live Sunday validation + practitioner quote, neither of which a copycat gets by Sunday. The doc's ranking (7.0, most memorable demo) is fair.
- **The saving-may-vanish problem (doc's ranking is right):** On a 60-balloon night, P(≥1 corridor hit over the night) → ~1 for hours; your honest product then recommends… closing, like today. **Fix:** Replay one *sparse* night and one *dense* night; pitch metric changes by regime: sparse → shorter closures; dense → earlier *first* closure decision + diversion planning lead time + border-guard interceptions. Never put "40 min instead of 11h" on a slide until the replay prints it.

---

## 7. What's right (briefly)

Problem selection and verified scale; decision-not-map outputs; Monte Carlo over fake precision; ERA5-replay/live-forecast separation; explicit out-of-scope list; Path A/B GNSS fallback thinking; practitioner-gap self-awareness. The skeleton is jury-grade. The GNSS scope and business framing are not.

---

## (a) Prioritized fix list — top 10

1. **Sat 09:00–10:00: GNSS phone test outside** — GnssLogger on all phones; Galileo nav-message yes/no → Path A/B decision by 12:00. Register GSC, download PKID-2 key + Merkle XML today.
2. **Adopt Open-Meteo/ECMWF IFS as live wind** (no key, pressure levels), CAMS as labelled Copernicus source; cache everything offline.
3. **Create CDS/ADS accounts, accept licences, download & cache ERA5 Vilnius replay + CLMS clips** — offline-first everything.
4. **Rewrite pitch claims:** OSNMA = "authenticates Galileo nav data; doesn't stop jamming/meaconing"; delete "holds up in court" → "documented correction provenance".
5. **Run multi-flight validation:** replay ≥5 Legionowo flights from SondeHub archive; report median landing error + ellipse coverage vs Tawhiri baseline. One flight = anecdote.
6. **3D threat layer:** glidepath-altitude-banded corridors (fix over-alerting + P(conflict)=1 problem).
7. **Smuggling-profile assumptions slide** with cited priors (3–11 km float, 500–1,500 packs, GPS trackers).
8. **Vilnius replay numbers before any slide number:** sparse vs dense night; lead time + closure-window delta, or change metric to decision lead time.
9. **Practitioner hunt at Sat mentoring (11:30/16:30):** one PAŻP/Border Guard/airport quote; fallback = cited VSAT/LRT statements. Reframe buyer: decision-support, border-guard/airport-ops first, Reg. 2017/373 acknowledged.
10. **Demo hardening Sun 12:00:** full offline run, Saturday-flight screen recording, static map fallbacks, backup slides that tell the whole story with zero live elements. Pin library versions + Fresh-Code README (git log from Friday).

## (b) Three things to verify first on Saturday morning

1. **Do our phones log Galileo E1B nav messages?** (Outside, 10-min GnssLogger log, grep type 1537 — decides OSNMA Path A/B and 30% of the pitch.)
2. **Can we pull one live wind cube and one ERA5 cube end-to-end?** (Open-Meteo IFS JSON + ERA5 NetCDF downloaded, licences accepted, `xarray` opens them, one trajectory integrates — decides the entire forecast demo.)
3. **Is Sunday's Legionowo sonde actually scheduled and visible on SondeHub, and what are its real launch/landing times (~12:18–14:15 CET)?** (Decides whether the pitch is "landed, error computed" vs Saturday recording.)

## (c) Verdict: **CONDITIONAL GO**

The problem is real, current, Polish-relevant, and unmatched in the likely field, and the forecast core (cached ERA5/IFS winds + own Monte Carlo + corridor logic + SondeHub validation) is honestly buildable by Sunday with a falsifiable, timestamped prediction no rival can fake. It becomes a NO-GO only if the team insists on the full seven-component scope — live phone OSNMA, RTKLIB-EGNOS protection levels, and "court-grade" claims — on untested chipsets, because that path burns Saturday on GNSS plumbing, invites lethal ChipCraft/cyber-juror corrections, and still demos nothing on stage indoors. Cut EGNOS to precomputed, gate OSNMA at noon, reframe ATC as decision-support, and ship the replay numbers: then this is a credible podium contender.


