Blunt review underway — verifying every Galileo, EGNOS, Copernicus and C2PA claim against primary sources before the Sunday deadline.Core signal claims check out with major caveats — now probing RTKLIB/Galileo support, GFM API specifics, and rival saturation.# Proof of Place — Hard Review (Sat 28 Nov 2026, ~30h to deadline)

## Verdict up front: **CONDITIONAL GO** — see final section. The spine is jury-legible and all-three-systems, but the demo as designed will break in at least three places (phone nav-messages, "authenticated fix", live Copernicus verdict) unless you cut scope today.

---

## 0. What is right (brief, keep these)

- **OSNMA is real and operational.** Initial Service declared 24 Jul 2025; receivers must register on GSC to download public key + Merkle tree root.
- **The Poland 2024 hook is real.** Reuters: disinformation attributable to Russian/Belarusian services spiked ~300% in first flood days. Full Fact traced 4 of 5 clips in a "Spain" compilation back to pre-Spain posts linked to Poland.
- **Article 50 timing is right.** Transparency rules apply from 2 Aug 2026; deployers must disclose deepfakes.
- **GFM exists and is free/anonymous via API, WMS and STAC** — `https://api.gfm.eodc.eu/v2/`, `https://geoserver.gfm.eodc.eu/geoserver/gfm/wms`, STAC at `stac.eodc.eu` with layer `ensemble_flood_extent`.
- **Pixel 10 C2PA is real** — first phone line with Content Credentials on every Pixel Camera photo — but see §2.5: Google's record deliberately excludes location, which is actually your best pitch line.
- **Three-way verdict (CONSISTENT/INCONSISTENT/NO OBSERVATION) and "we never fake a verdict"** — this honesty is your main defence with IGiK/Blue Dot. Keep it verbatim.

---

## 1. Technical implementation, component by component

### 1.1 Galileo nav-message capture on phones
- **BLOCKER — Qualcomm phones likely give you nothing.** EUSPA material states Qualcomm-based smartphones do not provide navigation messages (nor carrier phase). Most Pixels/Samsungs in a 3–6 person team are Qualcomm (Tensor is the exception path). Android does expose 228-bit Galileo I/NAV pages via `GnssNavigationMessage.getData()` / `TYPE_GAL_I`, but only if the chipset HAL delivers them.
  - **Fix (Sat 09:00, 30 min):** On *every* team phone install GnssLogger + GPSTest, log 5 min outdoors, grep the `.txt` for `Nav,` rows with Galileo SVIDs. Google's log format is `Nav,Svid,Type,Status,MessageId,Sub-messageId,Data(Bytes)`. If zero Galileo Nav rows on all phones → Path B immediately, no more debugging. Borrow a known-good device (older Broadcom/Mediatek, e.g. Xiaomi Mi 8-class) via mentors today, not Sunday.

- **BLOCKER — OSNMAlib does not eat GnssLogger files.** OSNMAlib "is not a GNSS receiver… it needs the navigation bits, satellite ID and GNSS time" encapsulated in its own `DataFormat`; its input modules read decoded SBF/hex formats, and it requires Merkle root + public key + KROOT in `exec_path`. The GnssLogger→OSNMAlib bit-packing converter (228 bits, sync/tail excluded, OSNMA 40-bit Reserved-1 field) is **the** hidden work item — budget 3–5h for one person, including TOW/GST reconstruction. Doc treats this as ingest plumbing. It is not.
  - **Fix:** Start from OSNMAlib's shipped test vectors / a Septentrio SBF recording for the "working OSNMA" claim, and write the Android converter as stretch. That is still Fresh-Code-legit pipeline work (see §6).

- **MAJOR — TTFAF kills "seal at capture".** Hot-start OSNMA time-to-first-authenticated-fix averages ~100s in ideal conditions in current implementations, ~61–69s optimised, best case 44s. In flood/urban conditions it will be worse. A citizen pressing shutter once gets `NOT AUTHENTICATED` through no fault.
  - **Fix:** Reframe UX in pitch and code: app logs GNSS continuously, seal status is "authenticated window ±2 min around capture", not instant-at-shutter. Say "the app must be running before the shot" before the jury says it.

- **MAJOR — GSC key access is a registration, not a download.** Users must register/log in to GSC to get OSNMA public key and Merkle files. Do this **today** with two team accounts; a weekend support delay is unrecoverable. Also note loose time-sync requirement (default 30s) for OSNMA init — your "authenticated time vs photo time" check must tolerate that, not flag 10s gaps.

### 1.2 "Authenticated fix" — the core correctness bug
- **BLOCKER — OSNMA authenticates data, not pseudoranges, so "position computed using only OSNMA-authenticated satellites" is not an authenticated position.** Literature is explicit: OSNMA "can only authenticate the navigation data, and the PVT is still computed using unauthenticated ranging data". Your §7.2 `AUTHENTICATED` definition over-claims and ChipCraft will say exactly this sentence.
  - **Fix (wording + logic, 1h):** Rename outputs: `NAV-DATA AUTHENTICATED (n sats)`, position = "position consistent with authenticated ephemeris/clock, computed from unauthenticated pseudoranges". Add the anti-replay checks you already list (GST vs receiver clock jump, C/N0/AGC, GPS/Galileo agreement) and present Copernicus as the independent channel — "defeating meaconing needs an independent reference that does not come from the sky" is quotable. Mention SAS correctly: SAS authenticates ranging itself, was first demonstrated in real-world positioning Sep 2026, still upcoming/not operational. Do **not** imply SAS is usable this weekend.

### 1.3 EGNOS via RTKLIB server-side
- **MAJOR — RTKLIB/Galileo/EGNOS chain is fragile.** Upstream RTKLIB states Galileo "is not yet formally supported"; EGNOS corrections in RTKLIB are fundamentally GPS-centric SBAS. It does accept EMS 2.0 files (`rnx2rtkp` reads RINEX OBS/NAV + SBAS log), but you first need GnssLogger→RINEX conversion (Google gps-measurement-tools / `android_rinex`), which drops/keeps constellations unevenly per device.
- **MAJOR — ±4 m claim is indefensible.** EGNOS Open Service commits 3m horizontal (95%) for proper SBAS receivers; EUSPA itself notes no smartphone provides position based on EGNOS corrections, and in urban/harsh environments SBAS adds little because multipath dominates. On phone code measurements your honest number is 5–15m open-sky, worse in Kłodzko streets.
  - **Fix:** (a) Use **RTKLIB-demo5 fork**, not vanilla 2.4.3, and pin the binary in Docker today. (b) Drop "EGNOS error bound ±4.1m" from seal example; report `accuracy_estimate_m` from solution covariance and label HPL as stretch only — a real HPL needs SBAS integrity params (UDRE/GIVE) correctly decoded, not a scaled sigma. (c) EDAS is "controlled access… to authorised users" — registration today, fallback = EMS archive file for the replay date. If neither lands by Sat 18:00, cut EGNOS to "SBAS-corrected vs uncorrected delta on recorded data" slide, keep Galileo+Copernicus as the live spine. Jury scores EU-space *use*, not three-for-three at any cost.

### 1.4 Copernicus flood check
- **MAJOR — "Verdict in seconds" is false for live captures.** GFM products are delivered with an **8-hour lag** from Sentinel-1 acquisition, on top of revisit gaps. Your §1 promise "verdict in seconds" and the replay example (Sentinel-1 5h earlier) will be read as typical. It is best-case.
  - **Fix:** Split latency claims: seal (OSNMA/EGNOS) in seconds; Copernicus verdict asynchronous, minutes-to-hours, `PENDING → NO OBSERVATION` until a pass exists. This actually strengthens the "we never pretend" story.
- **MAJOR — Constellation facts in doc are stale.** Since 24 Jun 2026 the 6-day repeat is Sentinel-**1C+1D**; Sentinel-1A terminated 29 Jun 2026. Your 2024 replay correctly uses 1A-era data (a Sentinel-1A image of the Polish floods on 15 Sep 2024 is documented), but any slide saying "1A+1C" today is an IGiK own-goal.
  - **Fix:** Global search-replace; phrase revisit honestly: "6-day same-orbit repeat; more frequent imaging over Poland from overlapping swaths, still not daily-guaranteed."
- **BLOCKER (for own-mask fallback) — Simple VV thresholding is a known false-positive machine.** Sentinel-1 cannot reliably detect inundation in dense urban areas or under vegetation; smooth dry surfaces/moist soil mimic water, single-date thresholds fail, pre-event reference + terrain constraints are required.
  - **Fix:** Make **GFM ensemble + EMSR756 the primary**, own mask only as visual context with pre/post change (Δbackscatter vs a pre-flood scene), HAND/slope exclusion if time. Never let own-mask alone produce `INCONSISTENT`.
- **MAJOR — `INCONSISTENT` logic is scientifically unsafe.** "Satellite looked, saw nothing within wider radius" ignores GFM exclusion/advisory flags, urban SAR blindness, wind-roughened water. One `INCONSISTENT` on a genuinely flooded street photo, demoed or discovered by IGiK, destroys credibility.
  - **Fix:** `INCONSISTENT` only when: valid GFM observation (not advisory-flagged/excluded), within window, *and* point is in GFM-observable land cover. Otherwise downgrade to `NO OBSERVATION / NOT OBSERVABLE`. Also fix internal inconsistency: search radius formula gives ~60m for S1, yet seal example claims CONSISTENT at 118m — jury will spot this in §7.4.
- **MINOR — EMSR756 is your safest asset.** Activation facts check out (Polish activation 13 Sep 2024, first delineations 15 Sep, ~60% of mapped flooding in Poland). Download vector delineations for **one** AoI (Kłodzko/Nysa area) today; don't build a multi-AoI browser.

### 1.5 Fire check (Sentinel-3 FRP)
- **MAJOR — Doc's "NRT in 3-minute frames" is wrong; product mechanics understated.** SLSTR FRP detects hotspots on a 1 km grid, NRT means <3h from sensing, product `SL_2_FRP___` in NetCDF via CDSE OData/STAC — parsing this is a half-day job for a point query, not a REST call.
  - **Fix:** Cut fire to **one pre-downloaded, pre-parsed case** (CSV of detections for a known 2024/2025 European fire) queried locally. No live CDSE FRP in demo path. LSTM 50m is 2028-planned (some sources now say ≥2029) — say "from ~2028–29", not a roadmap promise.

### 1.6 Sentinel-2 context, openEO/CDSE
- **MINOR — Workable but quota/ops risk.** CDSE openEO free tier = 10,000 credits/month, ~12 requests/min; registration + OAuth client credentials required. Sentinel-2 revisit 2–5 days and cloud during Storm Boris means "before/after visual" will often be grey — first cloud-free S2 over Wrocław was 18 Sep.
  - **Fix:** Pre-download all replay tiles Sat morning to local disk/`data/`; live openEO only as non-demo-path. Cache = your offline fallback (§3).

### 1.7 C2PA seal
- **MAJOR — Package and label problems.** `c2pa-python` exists (`pip install c2pa-python`, Python ≥3.10, Builder API) but is explicitly **prerelease, API subject to change**, and changed completely vs 0.4.0. Pin exact version in `requirements.txt` today and freeze. Your label `eu.space.proof-of-place.v1` violates spec: entity labels shall begin with the entity's Internet domain in reverse-domain notation, e.g. `eu.cassini.proofofplace` style under a domain you can claim. Also: self-signed test cert → every public verifier shows "unknown/untrusted signer". Jury will open verify.contentauthenticity.org live.
  - **Fix:** (a) Pin `c2pa-python`, test sign+read round-trip on a JPEG **tonight** (your own checklist item — treat as gate). (b) Rename label. (c) In pitch say "test certificate; production needs C2PA trust-list CA" before asked. (d) **JPEG only** for demo — HEIC/video C2PA support is patchy; do not promise video sealing live. (e) Note platforms strip metadata on upload — seal survives as original-file verification, not social-media repost. Say it first.

### 1.8 Spoof demo (§5 item 7)
- **BLOCKER as designed — Editing a photo's claimed position is not a GNSS spoof and OSNMA won't "fail" on it.** If you only move EXIF/reported coords, your *comparison* catches it only if you independently recomputed position from pseudoranges — the pipeline section never clearly builds that (RTKLIB step is EGNOS, not authenticated-PVT). A ChipCraft juror will ask "show me the pseudorange processing".
  - **Fix:** Build two honest demos: (1) **Tamper demo:** edited claimed location vs seal → signature/hash mismatch (C2PA layer). (2) **Replay-limit demo:** recorded-data OSNMA verification on genuine log vs fabricated nav bits (corrupt I/NAV pages) → OSNMA rejects. Label meaconing as *not* defeated. This converts your weakest claim into your most credible slide.

---

## 2. Correctness of EU-space usage — what each system actually proves

| Claim in doc | Reality | Severity |
|---|---|---|
| "Galileo signs where the photo was taken" | Galileo/OSNMA authenticates nav *data* origin; position derives from unauthenticated ranging. It proves "this ephemeris/time data is Galileo-genuine", not "camera was here" (phone could be elsewhere with relayed signals). Tagline is fine as poetry, fatal as a technical claim. Rephrase on slide 2. | **MAJOR** |
| "EGNOS says how sure we are" | Only if you compute a real SBAS solution + integrity; a phone-derived sigma is an estimate, not an EGNOS protection level. EGNOS commits 3m/95% to proper receivers — don't inherit that number. | **MAJOR** |
| "Copernicus checks the scene really happened there" | Copernicus checks *observable surface state near a point within a time window*, with urban/vegetation blindness and 8h GFM lag. Flood yes/no at ±4m precision is overreach; at neighbourhood scale it's defensible. Sell neighbourhood scale. | **MAJOR** |
| Claim-check on viral "Valencia" clip | **Your strongest demo — but note limit:** Copernicus can show flood in Poland in Sep and (separately) flood *also existed* in Valencia 29–30 Oct. `INCONSISTENT at Valencia` only works if you check the *specific claimed street/time*; region-level check may return CONSISTENT for Valencia too (Valencia really flooded). Pick the clip/claim where location-level check discriminates, verify Sat. Full Fact traced clips via captions/Google Lens, not precise geolocation — don't claim coordinates Full Fact didn't publish. | **MAJOR** |
| Fire at 1km | Adequate for large wildfires only; a house fire/container fire photo will be `NOT OBSERVABLE`. Doc concedes this — keep concession, drop fire from live demo. | MINOR |

---

## 3. Demo risk & offline fallbacks

- **BLOCKER — Live outdoor capture at 13:00 Sunday.** Indoor/no-fix, TTFAF ~1–2 min, OSNMA window, venue Wi-Fi, plus 15:00 submission collide. Pre-record the *entire* demo as video by Sun 12:00 (past-winner notes in your own files demand this), run live capture only as bonus. Cache: GFM COGs, EMSR756 vectors, S1 chips, sealed sample files, OSNMA logs — all on laptop, server on `localhost`. CDSE/GFM/GSC must not be in the live path.
- **MAJOR — "Drop a file" verifier** must handle: unsigned file, stripped file, wrong format, >10MB video. Each needs a graceful verdict, rehearsed. A stack trace on stage = Execution score gone.
- **MAJOR — MapLibre/Leaflet tiles need internet.** Use pre-rendered S1/GFM overlay images on a static basemap screenshot, or vector-only display, offline.
- **MINOR — Time zones:** GST→UTC leap-second handling (Galileo GST offset) is a classic off-by-seconds bug; assert test with known log.

---

## 4. Jury pushback — first hard question per archetype

- **ChipCraft (GNSS chips):** "Show me the pseudorange processing and explain why OSNMA-authenticated ephemeris + unauthenticated ranging equals an authenticated position. Also, which chipset in your phone gave you I/NAV pages?" → Answer per §1.2/§1.1; have GPSTest screenshot + phone model/chipset slide ready.
- **IGiK (remote sensing):** "Your `INCONSISTENT` — how do you handle GFM exclusion areas, urban double-bounce and reference-water masking? What's your validation against EMSR756, n=?" → Answer: §7.7 metrics actually computed (even n=200 sampled points, confusion table) or delete the metrics section. Uncomputed promised metrics are worse than none.
- **Scanway (optics):** "Why Sentinel-3 FRP at 1km rather than Sentinel-2 SWIR active-fire, and what's your detection limit in MW?" → Have one sentence + the pre-parsed case; don't improvise radiometry.
- **Blue Dot (EO business):** "GFM and EMS are free public services — what exactly do you sell that isn't a wrapper?" → Answer: the *join* + seal + API SLA + intake ranking, priced per verification; concede data is free, workflow is the product.
- **Cyber Defence Forces / WAT:** "A state actor meacons genuine Galileo at the target site, stages the photo, your seal says AUTHENTICATED. What did you actually stop?" → Answer honestly: casual forgery, back-dating, relocation of genuine footage (the actual 2024 tactic), and you raise cost; you do not stop an on-site state operation. This honesty is the only survivable answer — they ran the 2024 response.
- **ESA BIC Poland:** "Name the first paying customer, the procurement route, and month-12 revenue." → See §5; "newsrooms under AI Act pressure" is not an answer.

---

## 5. Buyer, business, legal/procurement

- **MAJOR — AI Act does not create your buyer.** Article 50 obliges AI *providers/deployers* to label synthetic content; it creates no duty for newsrooms to buy positive-authentication of real footage. Pitch it as reputational/workflow tailwind, not compliance mandate — a juror with the regulation open will correct you.
- **MAJOR — DSA claim needs exact articles or deletion.** Crisis obligations sit in Art. 36 (crisis response mechanism) and Art. 48 (voluntary crisis protocols); neither obliges platforms to purchase verification APIs. Your own doc flags "[VERIFY exact DSA articles]" — either cite 36/48 correctly as "cooperation pressure" or cut DSA from revenue table.
- **MAJOR — Competitor is not hypothetical.** Truepic already sells capture-time verified time/date/device/location to insurers, C2PA-compliant, alongside ProofMode/Numbers Protocol. Your differentiation is exactly two things: OSNMA-grade nav-data authentication and independent Copernicus cross-check. Put that comparison table on a slide; pretending greenfield loses Innovation points (past CASSINI winners already include GNSS-spoofing detection — SignalHawk 3rd, 8th ed. — jury has seen "GNSS trust" pitches).
- **MAJOR — Procurement reality:** RCB/State Fire Service/voivodeship centres buy via public procurement with security requirements; cycle ≫ hackathon pilot. Realistic beachhead: **one fact-checker (Demagog/Konkret24) free pilot + insurer innovation unit (claims triage) paid PoC**, ESA BIC/non-dilutive first — as your GTM says, but pitch must demote crisis centres to phase 2. Insurers: seal helps only for *their* requested captures (adjuster/claimant app flow), not viral media — separate the two products' claims.
- **MAJOR — Legal overclaims to delete:** "holds up in court" (Balloon Radar inheritance) — a self-signed C2PA test cert + phone GNSS is evidence support, not qualified electronic seal/timestamp under eIDAS; Polish court admissibility is judge-assessed. Also GDPR: precise location in a *public* verification page is personal data when linked to a person — your "coarser public location" mitigation must be implemented (round to ~100m–1km publicly), not just asserted. Crisis photos may identify victims — intake map needs access control in the story.
- **MINOR — Pricing absent.** Add one defensible line: e.g. per-verification API €X vs fact-checker hourly cost of manual geolocation (30–120 min). Even a hypothesis with arithmetic beats "usage-based".

---

## 6. Rules compliance & saturation

- **MAJOR — Fresh Code exposure:** Design reuses Veritrace "sealing spine" and Balloon Radar GNSS backend per your own §11/ranking notes. Rule (as briefed): code written during weekend; libraries/APIs allowed. Pre-existing *design docs* are fine; pre-existing *code, downloaded OSNMA logs, pre-built C2PA certs/scripts* are the grey zone. Mitigate: fresh repo Fri evening, commit history visible, declare in submission "open libraries + recorded public test data", rewrite pipeline code in-repo. Don't demo code you can't show a weekend commit for.
- **MINOR — EU-space requirement: comfortably met** *if* OSNMA path works on at least recorded data + GFM live query works. If GNSS collapses to EXIF-GPS + Copernicus, you become a generic fact-check tool and Relevance (33%) craters — hence §1.1 gate matters. Judging is Relevance/Innovation/Team-quality thirds in standard CASSINI rules (your brief says Execution — either way, working demo is a third).
- **MAJOR — Saturation:** Challenge 2 will be flooded (pun intended) with Sentinel-1/2 flood dashboards. Your anti-saturation asset is claim-check + seal, not the flood map — lead demo with claim-check (viral clip), not with "genuine sealed photo" map view. Ranking doc's own bottom line says the same. Obey it.

---

## (a) Prioritized fix list — Top 10

1. **Sat 09:00 phone gate:** test Galileo Nav rows on all phones; Path A/B decision by 10:00 (§1.1).
2. **Register GSC (OSNMA keys), EDAS, CDSE today** — two accounts each; download keys/Merkle/EMS archive (§1.1, §1.3).
3. **Rename/redefine authentication outputs** — kill "authenticated position/fix" language everywhere (§1.2).
4. **Freeze GNSS demo as recorded-data OSNMA** (genuine vs corrupted I/NAV) + tamper demo via C2PA; drop live-spoof pretence (§1.8).
5. **Pre-download replay pack:** EMSR756 one AoI + GFM COGs + S1 chips for Kłodzko, Sep 2024; make demo fully offline (§3).
6. **Fix verdict logic:** NOT OBSERVABLE downgrade, advisory-flag handling, radius/example inconsistency, async Copernicus latency wording (§1.4).
7. **C2PA gate tonight:** pinned `c2pa-python`, JPEG sign/verify round-trip, spec-compliant reverse-domain label, test-cert disclosure line (§1.7).
8. **Update stale facts:** Sentinel-1C+1D (1A retired 29 Jun 2026), FRP <3h/1km, LSTM 2028–29, DSA Art. 36/48 or cut (§1.4–1.5, §5).
9. **EGNOS descoping decision Sat 18:00:** demo5 RTKLIB SBAS delta on recorded data or cut to slide; remove ±4m (§1.3).
10. **Business/legal slide rewrite:** Truepic comparison, fact-checker beachhead, insurer PoC, remove court/compliance mandates, price hypothesis (§5). Plus: practitioner quote — your own past-winner analysis calls this CRITICAL and it's still missing; use Sat mentoring to get one fact-checker/mentor sentence.

## (b) Three things to verify first Saturday morning

1. **Do any team phones log Galileo I/NAV `Nav` rows in GnssLogger outdoors?** (decides Path A/B, §1.1)
2. **Can OSNMAlib verify one genuine recorded log end-to-end with GSC keys, and does `c2pa-python` sign+verify one JPEG with the custom assertion?** (your two load-bearing libraries, §1.1/§1.7)
3. **Does a GFM STAC/API query return `ensemble_flood_extent` for Kłodzko 15 Sep 2024, and does it agree with EMSR756 at your test points?** (decides demo claim + metrics, §1.4)

## (c) Verdict

**CONDITIONAL GO.** The problem is real, Polish, mentor-resonant, and the Galileo-authenticates-data + Copernicus-independently-observes join is genuinely differentiated against both flood dashboards and Truepic — provided you stop over-claiming what OSNMA and EGNOS prove, gate the phone/OSNMA feasibility by Saturday 10:00 with a recorded-data fallback, and lead with claim-check instead of live sealing. If gates (b)1–(b)2 fail and you cannot show OSNMA verification on *any* real data by Saturday evening, switch the pitch to claim-check-first with GNSS as recorded proof-of-concept — or fold Proof of Place back into Balloon Radar as its evidence module per your §11; do not spend Sunday morning debugging chipsets while the submission clock runs.
