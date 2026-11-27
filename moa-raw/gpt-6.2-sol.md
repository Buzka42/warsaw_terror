**My Warsaw pick: ClockWitness—if you can verify a public Galileo OSNMA recording or reference vector with an existing decoder. If you can’t, build ClearIntake.** ClockWitness has the strongest technical distinction: it shows what authenticated navigation data *doesn’t* prove about a critical clock, then turns that distinction into an operator decision. ClearIntake has the simplest buyer story and the most reliable live demo: a water utility gets a sampling work order, not another satellite map.

I’m treating the event dates, tracks and Fresh Code Rule as supplied. I haven’t independently verified the November 2026 webinar content or final handbook. Prices below are pilot hypotheses, not evidence of willingness to pay. For each idea, the Sunday demo should have one live or auditable ESA/EU data path and one offline fallback using the **same real input**, with any simulated telemetry clearly labelled.

## 1. ClockWitness — An evidence recorder for critical clocks

### 1. One-Line Pitch & Challenge Track
**Challenge 1 — Cybersecurity for space-based strategic enablers.** Give telecom timing operators a signed incident record that answers two separate questions: *Was the Galileo navigation message authenticated?* and *Did the site clock remain within tolerance against an independent reference?*

### 2. Exact EU Space Data/Signal Pipeline
Feed recorded **Galileo E1-B I/NAV** messages carrying **OSNMA** into an existing public decoder such as [OSNMAlib](https://github.com/Algafix/OSNMA). Use European GNSS Service Centre trust material appropriate to the recording or official test vector. Preserve `verified`, `pending`, and `unavailable/failed` states rather than reducing them to a binary alarm. Separately ingest receiver clock-offset telemetry and a reference from a different timing failure domain; simulate those two streams for the hackathon if hardware is unavailable. A policy engine evaluates offset, duration and reference health, then signs an evidence bundle containing the authentication state, offset history, source health and event timestamps.

### 3. Why It's NOT a Duplicate
No RF heatmap and no claim to locate an interferer. The product is the **incident evidence and escalation decision** for one timing site. The live reveal: authenticated navigation data and an out-of-tolerance site clock can coexist, and the tool explains why both statements can be true.

### 4. Target Buyer & Business Model
Start with the **synchronization engineering lead at a telecom operator or timing-service provider** already collecting GNSS-disciplined clock telemetry. Test a **€10k–€25k fleet pilot**, then a per-site subscription. The value hypothesis is faster triage and fewer unnecessary site visits. For in-scope operators, NIS2’s 24-hour early-warning requirement for *significant* incidents adds value to a usable timeline; a clock alarm alone does not establish reportability.

### 5. 48-Hour Prototype Scope
Build one decoder adapter, one telemetry replay, one policy engine and one webhook. By Sunday 15:00 CET, run a genuine OSNMA input and two labelled telemetry scenarios: normal operation and a clock fault despite verified navigation data. Show the resulting ticket and independently verify the evidence bundle’s signature. No live RF setup or autonomous clock switching is needed. **Go/no-go:** if you cannot get a genuine decoder result, don’t present a simulated authentication flag as the space component.

### 6. Biggest Risk & Likely Jury Pushback
**“OSNMA doesn’t authenticate the ranging signal or prove the clock is correct. Is your reference actually independent?”** Correct. Show the failure-domain diagram, the decoder’s trusted-time assumptions and the reference-health gate. If both clocks rely on the same vulnerable upstream source—or the reference is unavailable—the product reports *insufficient independent evidence*, not reassurance.

## 2. SceneGate — A release gate for operational Copernicus products

### 1. One-Line Pitch & Challenge Track
**Challenge 1 — Cybersecurity for space-based strategic enablers.** Stop an untraceable or stale Copernicus-derived artifact from triggering a utility or emergency-management workflow, even when its map looks plausible.

### 2. Exact EU Space Data/Signal Pipeline
Query **Sentinel-2 Level-2A surface reflectance** through [CDSE STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html) and retrieve the selected product assets. Use **B08 and B12**, aligned to a documented 20 m grid, plus the **Scene Classification Layer** to compute a small pre/post Normalized Burn Ratio change artifact. At ingestion, record scene IDs, sensing times, processing baseline where available, area of interest and hashes of the assets actually consumed. Bind those inputs, the recipe version and the output hash in a signed manifest. A separate verifier checks the manifest, freshness policy and approved geospatial configuration before issuing a downstream release receipt.

### 3. Why It's NOT a Duplicate
The fire-change raster is a test artifact, not the product. The product is the **enforcement point between Earth observation and an operational webhook**. The demo compares two visually plausible artifacts: one is traceable and current; the other is quarantined because its source date falls outside policy. That is a different sale from analytics or visualization.

### 4. Target Buyer & Business Model
Sell first to an **EO integration provider delivering automated feeds to utilities or civil-protection agencies**. It controls the publication path and can reuse the same gate across customers. Test a **€12k–€25k integration pilot**, followed by an annual fee per protected workflow. The willingness-to-pay test is concrete: will the integrator put this on a production publication path because it reduces audit effort or contractual exposure?

### 5. 48-Hour Prototype Scope
Implement one small-area CDSE pull, one deterministic processing recipe, one signing service and one consumer webhook. Demo a valid release, a stale-scene rejection and a hold when the approved output grid does not match. Export one signed release or quarantine receipt for review. Use public libraries and test fixtures; skip multi-tenant access control and production key infrastructure.

### 6. Biggest Risk & Likely Jury Pushback
**“You signed your own manifest. Does that prove ESA supplied the bytes or that the analysis is correct?”** No. The signature binds what this system retrieved and processed; it is **not** an ESA signature or a scientific guarantee. Keep the trust boundary explicit: official retrieval endpoint, restricted signer and separate verifier. A compromised trusted signer is out of scope. The defensible win is showing what the downstream consumer actually refuses to accept.

## 3. ReEntry Queue — The first flood inspection shift for grid operators

### 1. One-Line Pitch & Challenge Track
**Challenge 2 — Space-enabled crisis response and civil resilience.** After a flood, turn satellite evidence and grid alarms into a ranked, supervisor-approved queue of **which substations to inspect next and which access roads still need verification**.

### 2. Exact EU Space Data/Signal Pipeline
Pull a **Copernicus Emergency Management Service Rapid Mapping** flood delineation vector for a documented event, such as a suitable September 2024 activation in southern Poland. Preserve the product’s observation time and footprint. Overlay that extent with **OpenStreetMap** road segments, synthetic distribution-substation locations and simulated read-only SCADA alarms. Classify the asset perimeter and candidate approach segments as `observed inundation`, `not mapped as inundated within coverage`, or `unknown/stale`. Rank inspection jobs by service criticality, alarm state and access evidence. Export them as work orders with observation age and explicit verification requirements.

### 3. Why It's NOT a Duplicate
The shift supervisor doesn’t need another flood polygon. They need to allocate scarce crews. The demo shows a **new observation changing the order of two jobs** and recommends what a crew should verify first. It does not certify that an electrical asset or a road is safe.

### 4. Target Buyer & Business Model
Target a **regional electricity distribution operator’s emergency operations or field-service team**, with a southern Polish territory as the pilot. Test a **€15k–€35k storm-season pilot**, then an annual integration and readiness contract. Measure time to produce the first approved inspection queue, dispatcher rework and avoidable journeys. This supports critical-entity resilience planning without claiming to deliver compliance by itself.

### 5. 48-Hour Prototype Scope
Use one real EMS activation, a small road graph, 15–30 fictional assets and two alarm snapshots. Build a ranking service, an approval screen and a CSV or mock field-service API export. Replay two observation states to show a priority change and a route sent for manual verification. No production SCADA connection, live road-safety promise or automated switching.

### 6. Biggest Risk & Likely Jury Pushback
**“A flood extent is not a road-closure feed, especially in towns and behind levees.”** Agree. Outside coverage is `unknown`, and absence from a mapped flood polygon is not proof of safe access. Give dispatcher or road-authority confirmation precedence. Score the prototype on **inspection planning under uncertainty**, not navigation or clearance.

## 4. ClearIntake — Satellite-triggered sampling for drinking-water utilities

### 1. One-Line Pitch & Challenge Track
**Challenge 2 — Space-enabled crisis response and civil resilience.** Give a water utility a defensible **sample-here-next work order** when a reservoir patch warrants investigation beyond the fixed intake sensor.

### 2. Exact EU Space Data/Signal Pipeline
Use **Sentinel-2 MSI Level-1C** products via CDSE for a reservoir reach with enough open water for shoreline exclusion. Apply an aquatic atmospheric-correction processor such as **ACOLITE** to a small subset. Align **B04 (~665 nm)** and **B05 (~705 nm)** to 20 m, then compute the normalized difference chlorophyll index, `(B05 − B04)/(B05 + B04)`, from valid water reflectance. Reject cloud, glint-contaminated, shoreline-adjacent and otherwise invalid pixels; suppress the output if valid coverage is too low. Combine a coherent candidate patch with a utility-defined sampling zone, intake turbidity or fluorescence telemetry, and a weather feed. Emit a proposed station, sampling window, quality flags and a lab-order payload.

### 3. Why It's NOT a Duplicate
The innovation is not bloom detection. It is moving from a fixed intake reading to a **specific, reviewable sampling task** when there is satellite evidence elsewhere in the reservoir. The satellite changes the proposed sampling station; it does not diagnose toxicity, predict plume arrival or order an intake shutdown.

### 4. Target Buyer & Business Model
Target the **raw-water quality lead at a utility with a surface-water intake and an existing sampling crew**. A Warsaw-area use case could use the Zegrze reservoir if suitable scenes and open-water pixels exist. Test a **€10k–€20k seasonal pilot** per reservoir, then an annual monitoring and lab-integration fee. Compare time to collect an informative sample and the number of low-value sampling trips against the existing protocol.

### 5. 48-Hour Prototype Scope
Process one usable historical scene and one poor-coverage scene. Use labelled simulated intake telemetry unless a public feed is available. Have an operator accept a recommendation and generate a mock laboratory information management system work order. Then run the poor-coverage case and show the system **abstaining** rather than filling the map or inventing a sample location.

### 6. Biggest Risk & Likely Jury Pushback
**“Sediment, adjacency and atmospheric correction can all produce misleading index values. Where is your validation?”** Show raw band values, masks and the shoreline buffer. Don’t claim a chlorophyll concentration, a species identification or a toxin measurement without field validation. The paid pilot should compare recommendations against paired field samples and the utility’s normal sampling plan. Until then, it’s a way to prioritize samples, not a water-quality verdict.

## 5. TimberTrace Review — A harvest-date evidence check for timber compliance

### 1. One-Line Pitch & Challenge Track
**Challenge 3 — Countering transnational crime and terrorism with space data.** Help timber importers and compliance teams identify **shipment origin declarations that warrant documentary review**, without treating satellite imagery as proof of origin or a sanctions violation.

### 2. Exact EU Space Data/