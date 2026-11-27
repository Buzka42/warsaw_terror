## 1. ChronoSeal — attested time for critical infrastructure

**1. One-Line Pitch & Challenge Track**
A drop-in timing-integrity layer that turns Galileo OSNMA into a signed *"this second is authentic"* verdict for substations, telcos and trading systems — and fails over to holdover **before** spoofed time can mis-operate a protection relay. **Challenge 1.**

**2. Exact EU Space Data/Signal Pipeline**
- Galileo E1-B I/NAV decoded by a multi-band receiver (Septentrio mosaic / u-blox F9-class with OSNMA firmware) or an E1 (1575.42 MHz) + E5b SDR capture; OSNMA TESLA key chain verified against the GSC-published DSM-PKR root key and Merkle tree, per-satellite MACSEQ/MACLT status extracted.
- Cross-checks that OSNMA alone cannot give: GNSS time vs. local OCXO/CSAC holdover drift model (Allan deviation), vs. PTP grandmaster peers over fibre (IEEE 1588), and vs. a second constellation. This is what catches **meaconing** — replay of an *authentic* recording passes OSNMA but drifts against holdover.
- Galileo HAS (E6-B) corrections for stable, high-accuracy time/position transfer where needed.
- Every second is signed (Ed25519 over COSE/JWS: time, uncertainty, authenticated SV count, cross-check residuals, receiver ID) and streamed over gRPC to SCADA/PMU/OSS as a **trust bit** plus token.
- On failure: trust bit → 0, trigger PTP holdover or backup source, and emit a signed incident bundle pre-formatted for NIS2 Art. 23 (24 h early warning / 72 h notification / 1-month report).

**3. Why It's NOT a Duplicate**
Not a jamming heatmap, not a map at all. The deliverable is an **actuation path**: a machine-readable trust bit, an automatic failover, and a cryptographic audit artifact. It also attacks the exact gap most "GNSS security" pitches hand-wave: OSNMA authenticates message content, not signal freshness — we cover replay via holdover forensics.

**4. Target Buyer & Business Model**
DSOs/TSOs (PSE, Tauron, Enea, PGE Dystrybucja), telecom timing chains, exchange matching engines, data centres, rail signalling. Pricing: €3–8k/site/yr appliance + cloud attestation; €150k+ OT integration for a DSO; per-endpoint API for data centres. 2026 drivers: NIS2 in force, CER critical-entity identification deadline (17 July 2026) forcing documented resilience, GNSS interference in Poland/Baltic now a board-level risk, and OSNMA finally being a verifiable signal rather than a paper feature.

**5. 48-Hour Prototype Scope**
linuxptp grandmaster on a NUC/RPi with GNSS HAT (or recorded IQ replayed through an open OSNMA parser); token service; a mock PMU/Modbus endpoint consuming the trust bit; live attack demo injecting a time offset/replay, showing attestation flip → holdover → auto-generated NIS2 report. No custom hardware.

**6. Biggest Risk & Likely Jury Pushback**
*"OSNMA is a receiver firmware feature — chip vendors bundle it, and a weekend demo can't prove metrology."* Defence: we are not the receiver; we are the cross-source attestation and OT-integration layer the asset owner buys, and the moat is the holdover/peer-forensics logic plus compliance evidence. Partner rather than compete with ChipCraft-type vendors; present measured residuals, never certification claims.

---

## 2. VeriTerra — physics-based verification of satellite imagery

**1. One-Line Pitch & Challenge Track**
An ingestion firewall that scores every satellite image for tampering and synthetic content by checking it against physics and against the *other* Sentinel — so insurers, newsrooms and analysts can trust a picture before they pay or publish on it. **Challenge 1** (integrity of space-based strategic enablers).

**2. Exact EU Space Data/Signal Pipeline**
- Ingest Sentinel-1 GRD/coherence and Sentinel-2 L2A via CDSE (STAC/OData/openEO) by product ID; SHA-256 each asset and wrap it in a signed "product birth certificate" (COSE) chained to the CDSE catalogue record plus an RFC 3161 timestamp → tamper-evidence from acquisition.
- Physics check: solar azimuth/elevation from S2 metadata + Copernicus GLO-30 DEM + OSM/WSF building footprints → predict shadow direction and length per structure; a spliced building casts the wrong shadow.
- Cross-modal check: any new structure in S2 must have a matching SAR signature (double-bounce, coherence change) in S1; "appeared in optical, absent in SAR history" is a red flag.
- Forensic check: seam/clone detection, resampling and JPEG-ghost artefacts, region-wise noise-residual variance (spliced regions carry different sensor noise), spectral plausibility (NDVI/NDBI ranges), acquisition-time plausibility.
- Time-series check against the full S2 archive: physically impossible one-scene-only change.
- Output: signed trust score + localized tamper map + verdict API (accept / quarantine / escalate).

**3. Why It's NOT a Duplicate**
This is not change detection and produces no "damage map". It verifies the *data itself* — provenance plus physical and cross-modal consistency — and returns an accept/reject decision at ingest. It is the missing integrity layer under every EO dashboard.

**4. Target Buyer & Business Model**
Insurers/reinsurers and loss adjusters (before/after claim imagery), media and OSINT verification desks, litigation/e-discovery, defence analysts, and EO analytics vendors needing a data-quality gate. Pricing: €100–600 per verification; €50–250k/yr enterprise API; OEM licensing into platforms. 2026 drivers: generative imagery is now convincing at a glance, AI Act transparency pressure, NIS2 supply-chain integrity expectations.

**5. 48-Hour Prototype Scope**
Six to ten real Warsaw/Poland scenes; four hand-made forgeries (inserted airstrip, deleted building, inpainted flood extent, edited metadata); detectors implemented in Python (rasterio, GeoPandas, OpenCV, numpy) with a single "verify this product" endpoint and a live demo on an unseen tile; show hash + signature + per-check verdicts.

**6. Biggest Risk & Likely Jury Pushback**
*"Deepfake detection is an unwinnable arms race; you'll be bypassed — and who actually pays?"* Defence: we sell **provenance + physics consistency**, not omniscient detection. The strongest guarantee is the acquisition-time hash chain (tamper-evidence); physics checks are defence-in-depth and are cheap to update. The buyer pain is contractual and financial — a fraudulent claim or a retracted publication — not academic perfection.

---

## 3. GridWade — flood-to-grid switching playbook

**1. One-Line Pitch & Challenge Track**
Converts a Sentinel-1 flood mask into a substation-level **switching playbook and outage forecast 24–72 h before the water arrives**, delivered as tickets into the DSO's operations systems. **Challenge 2.**

**2. Exact EU Space Data/Signal Pipeline**
- Sentinel-1A/1C GRD VV/VH via openEO/CDSE → speckle-filtered flood mask by threshold + change against a dry reference mosaic; refined with **HAND** (Height Above Nearest Drainage from Copernicus GLO-30 DEM + HydroSHEDS rivers) to kill false positives on wet fields and steep terrain, and to classify depth bands.
- Validation with Sentinel-2 NDWI where cloud-free and with Copernicus EMS Rapid Mapping products when activated.
- Trigger and extrapolation: EFAS/GloFAS 5-day discharge forecasts plus a simple travel-time/rating-curve model to project the SAR-observed front forward.
- Network layer: operator CIM/CIMXML or OSM substations/lines/transformers, plus GHSL/OSM buildings for customers-at-risk; graph simulation of sectionalising, tie-switching and generator placement; road-access loss from the same flood layer.
- Output: ranked action list → ADMS/OMS via REST or CIM; field crews carry Galileo OSNMA-authenticated positions so actions are auditable.

**3. Why It's NOT a Duplicate**
No map. The output is a **specific switching order, generator pre-positioning list and mutual-aid request**, tied to the asset register, plus a regulator-ready resilience record. Competitors produce flood extents; we produce the operator's Monday-morning decision.

**4. Target Buyer & Business Model**
DSOs (Tauron, Enea, PGE Dystrybucja, Energa), water/wastewater utilities, industrial parks. Pricing: €40–150k/yr per DSO by critical-asset tier, event-surge add-on. 2026 drivers: CER identification deadline and resilience plans, NIS2, Floods Directive risk-cycle reporting, and the 2024 Polish flood as a live reference case.

**5. 48-Hour Prototype Scope**
Replay September 2024 S1 scenes over Kłodzko/Nysa with OSM grid data and Copernicus DEM; generate a playbook for ~10 substations; run the whole pipeline live on a fresh S1 scene in under 15 minutes; export ticket JSON into a mock operator console.

**6. Biggest Risk & Likely Jury Pushback**
*"SAR flood mapping is unreliable in towns (double-bounce, shadow), and DSOs won't trust OSM topology."* Defence: HAND + S2 + EMS cross-validation, per-pixel confidence, and human confirmation in the loop; we ingest CIM where available and the first product (asset-at-risk + access loss + switching options) does not require full topology. We sell decision speed and evidence, not survey-grade hydraulics.

---

## 4. IntakeGuard — drinking-water intake protection

**1. One-Line Pitch & Challenge Track**
Gives water utilities a 24–72 h **"shut the intake" decision** when a flood, spill or bloom is heading downstream — with the regulatory dossier attached. **Challenge 2.**

**2. Exact EU Space Data/Signal Pipeline**
- Sentinel-1 flood extent; Sentinel-2 NDWI and turbidity proxies; **Sentinel-3 OLCI** (300 m, near-daily) total suspended matter and chlorophyll — the layer that keeps working when S2 is clouded out.
- River graph from HydroSHEDS/HYDRORIVERS + EFAS discharge forecasts + open gauge telemetry (IMGW, GRDC) → 1-D advection–dispersion travel time and dilution, propagating an observed plume downstream.
- Utility asset overlay: intake coordinates, plant capacity, raw-water reservoir hours of buffering, alternative sources.
- Computes time-to-arrival per intake, predicted turbidity proxy exceedance, hours of storage left, and a recommended action (switch source, increase coagulation, close intake, pre-flush) with confidence bands.
- Output: a timestamped action order, read-only SCADA tag integration, and an annex formatted for the utility's water-safety plan.

**3. Why It's NOT a Duplicate**
It is predictive and prescriptive: a shutdown/restart order and a compliance annex, not a turbidity map. The core computation is travel time to a named asset, not a raster.

**4. Target Buyer & Business Model**
Municipal water utilities and regional suppliers (Aquanet, Saur, Wody Polskie), plus food & beverage plants with river abstraction and utility insurers. Pricing: €25–80k/yr per utility by intake count; industrial-abstractor module. 2026 drivers: revised Drinking Water Directive risk-based water-safety planning phasing in through 2027–2029, climate-driven turbidity events, and the Odra 2022 / 2024 flood precedents.

**5. 48-Hour Prototype Scope**
Replay the Odra 2022 or September 2024 event with S3 OLCI + S1; show plume arrival at a chosen intake with a 36-hour-ahead alert; write to a mock PLC tag; generate the PDF dossier; run the same pipeline on the latest S3 scene live.

**6. Biggest Risk & Likely Jury Pushback**
*"Turbidity is not toxicity — you're not detecting chemicals; and S3 is 300 m with cloud gaps."* Defence: we are an explicit screening and trigger layer that buys time for sampling and source-switching, not a contaminant detector; we fuse gauge and utility sensor data, publish uncertainty, and bias to conservative triggers. Dispersion assumptions are stated and validated against observed gauge timing in the demo.

---

## 5. GhostWorks — satellite audit of publicly funded works

**1. One-Line Pitch & Challenge Track**
Cross-checks EU-funded construction claims against what was physically built, and hands auditors a ranked, evidence-backed **case file**. **Challenge 3** (fraud against the EU budget as transnational organised crime).

**2. Exact EU Space Data/Signal Pipeline**
- Money side: TED tenders, national e-procurement, cohesion/RRF project lists and payment datasets (open data) → project coordinates, contract value, declared start/end and milestones.
- Physical side: Sentinel-2 time series (bare soil → impervious → roof progression), Sentinel-1 backscatter and coherence (earthworks and structures even under cloud), Copernicus Urban Atlas / EMS layers for context — all via CDSE/openEO.
- Anomaly scores per project: declared completion vs. observed progress, built footprint vs. contracted area, work claimed on a site with no disturbance, duplicate or overlapping sites, implausible one-scene progress jumps.
- Output: ranked case files with timelines, before/after chips, hashes and a defensible methodology note, routed to an audit referral queue.

**3. Why It's NOT a Duplicate**
It starts from the **money**, not the image: EO is used as a control on a financial claim. No dashboard — a prioritised investigation queue with admissible evidence packaging.

**4. Target Buyer & Business Model**
EPPO, OLAF, national audit offices (NIK), managing authorities, surety/performance-bond insurers, forensic audit firms. Pricing: €500–2k per case file, or €150–400k/yr national licence; insurers pay by bond exposure. 2026 drivers: peak RRF/cohesion disbursement and audit pressure, growing EPPO caseload, insurers absorbing completion fraud.

**5. 48-Hour Prototype Scope**
Thirty to fifty real, publicly listed EU-funded projects in Poland with coordinates; full pipeline run; three to five flagged cases with imagery timelines; case-file PDF export; live "add a project and get a verdict" demo. Findings labelled **anomalies requiring verification**, never accusations.

**6. Biggest Risk & Likely Jury Pushback**
*"You will flag innocent projects — defamation and legal exposure — and procurement data is messy."* Defence: outputs are risk indicators with confidence and mandatory human review, sold only to investigating bodies and never published by us; we test physical existence and progress, not construction quality; data-quality handling (missing coordinates, aggregated contracts) is shown explicitly in the demo rather than hidden.
