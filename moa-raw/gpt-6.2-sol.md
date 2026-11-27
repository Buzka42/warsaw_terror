**Build ClockWitness if you can verify a usable Galileo OSNMA capture before the event. Otherwise, build PumpSlot.** ClockWitness has the strongest Warsaw technical pitch: it shows exactly what Galileo authenticates, what it does not, and how a critical-infrastructure operator uses that distinction. PumpSlot is the safer all-round entry: it turns a Copernicus flood product into a dispatch decision a jury can test in 90 seconds.

I’m using the event details and webinar guidance you supplied; I haven’t independently verified the 2026 event materials. Pricing below is a proposed pilot price, not evidence of willingness to pay. For all five ideas, verify documentation, account access and public sample availability before the weekend, but write the competition code during the event. Use archived *real* space data for a deterministic live demo, and label any simulated operational inputs.

## 1. ClockWitness — Galileo timing incident evidence

### 1. One-Line Pitch & Challenge Track
**Challenge 1 — Cybersecurity for space-based strategic enablers.** Give a grid timing operator a signed incident record showing whether Galileo navigation-message authentication changed, whether the delivered clock drifted, and what evidence supports each finding.

### 2. Exact EU Space Data/Signal Pipeline
Replay recorded **Galileo E1-B I/NAV pages carrying OSNMA** through a public OSNMA library such as **OSNMAlib**, using a supported capture format and the applicable trust material from the [European GNSS Service Centre](https://www.gsc-europa.eu/). Associate the verifier’s authentication events with receiver timestamps, retaining the delay between message receipt and authentication. In a separate stream, ingest a 1 PPS offset log measured against an independent reference in production, or a clearly labeled reference trace in the demo. A rules engine emits separate states for **message authentication**, **clock agreement**, and **reference health**, then signs a JSON evidence package with the input hashes, thresholds and event timeline.

### 3. Why It's NOT a Duplicate
This is not a jamming detector or a map. Its differentiating demo is **“the navigation message authenticated, but the clock is still outside tolerance.”** A receiver alarm and a timing monitor can each see part of that incident. ClockWitness joins the evidence into a record a timing engineer and a security team can review together, without claiming it has attributed an attack.

### 4. Target Buyer & Business Model
Sell first to a **Polish power-grid timing or substation integrator**, with the utility’s timing engineer and SOC as end users. Propose a **€12k–€25k integration pilot**, then an annual per-site monitoring and evidence-export license. The value is fewer manual investigations across receiver, clock and SOC logs. For incidents that actually meet the NIS2 significance threshold, the export can support preparation of the **24-hour early warning**; it does not decide reportability or send a regulatory filing.

### 5. 48-Hour Prototype Scope
A four-person team builds one replay adapter, one verifier integration, one correlation service and a signed incident export. Show three cases by Sunday: authenticated messages with a healthy clock; authenticated messages with a simulated clock deviation; and insufficient authentication evidence with a healthy clock. Let the judge inspect the underlying events and independently verify the export signature. **Go/no-go:** confirm that a compatible recording and trust material are accessible before choosing this idea. Don’t make hardware procurement part of the critical path.

### 6. Biggest Risk & Likely Jury Pushback
**“OSNMA does not authenticate the received RF time of arrival or prove UTC accuracy.”** Correct. Keep the navigation and timing verdicts separate, show delayed authentication and initialization explicitly, and fail to **unknown** when either evidence stream is insufficient. A second receiver sharing the same GNSS dependency is not an independent clock reference. In production, the quality of that independent reference is part of the product’s acceptance test.

## 2. PumpSlot — Flood pump mutual-aid dispatch

### 1. One-Line Pitch & Challenge Track
**Challenge 2 — Space-enabled crisis response and civil resilience.** Convert a Copernicus flood delineation and live field reports into a reviewable work order assigning a scarce mobile pump, crew and verified access route.

### 2. Exact EU Space Data/Signal Pipeline
Download an observed flood delineation from a [Copernicus EMS Rapid Mapping](https://mapping.emergency.copernicus.eu/) activation. Preserve the acquisition time, product version and source sensor; pick a Sentinel-1-derived product if the activation metadata confirms it. Intersect flood geometry with candidate staging areas and access-road segments. Join it to road-closure reports, timestamped water-level readings, operator-entered site priorities and a pump inventory. A small constraint solver assigns assets based on pump capacity requirements, crew availability and travel time, while ruling out confirmed closures and requiring verification for uncertain access.

### 3. Why It's NOT a Duplicate
A flood map can’t tell a dispatcher **which pump to send where and what to do when the approach is uncertain**. PumpSlot issues a proposed work order, reserves the asset on approval and explains infeasible assignments. The hero demo is a road closure invalidating the first assignment and producing a different dispatch decision—not another layer appearing on a map.

### 4. Target Buyer & Business Model
Start with a **regional water utility or municipal flood-response consortium** that already shares mobile pumps across depots. Sell a **PLN 40k–80k tabletop-exercise and integration pilot**, then annual software and connector fees. The operational sponsor is the dispatch lead; the budget case is faster mutual-aid coordination and fewer wasted deployments. Exercises make the value testable without waiting for a flood and can support resilience planning where CER obligations apply.

### 5. 48-Hour Prototype Scope
Use one real EMS activation, a small OpenStreetMap road graph, five simulated pump requests and three simulated assets. Build the ingest, solver, approval queue and a webhook to a mock dispatch system. In the demo, first generate a feasible dispatch order; then close the final approach road and show the solver reassign the pump or return **no verified route**. Compare the result against a nearest-pump baseline and show the precise constraint it misses.

### 6. Biggest Risk & Likely Jury Pushback
**“A satellite-derived flood polygon cannot tell you whether a truck can drive down a road now.”** Exactly. The polygon flags segments for review; current ground reports determine operational clearance. Water extent is not water depth, and neither gives you pump sizing. Use field-entered pumping requirements, show acquisition age, and default to dispatcher approval. If the EMS product is stale or absent, the tool falls back to ground-only dispatch and says so.

## 3. OrbitReceipt — A release gate for operational Earth observation

### 1. One-Line Pitch & Challenge Track
**Challenge 1 — Cybersecurity for space-based strategic enablers.** Stop a stale, mis-scoped or unverified Copernicus-derived product from silently entering a utility’s operational workflow, and show the operator exactly why it was held.

### 2. Exact EU Space Data/Signal Pipeline
Query **Sentinel-2 Level-2A** products via the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) catalogue. Retrieve a small area’s B04, B08 and Scene Classification Layer through a supported CDSE access path. Compute a reproducible, cloud-masked NDVI raster; the index is just a test artifact. A controlled worker records source product IDs, sensing time, footprint, input digests, processing parameters and output digest in a signed manifest. On delivery, a separate verifier checks the signer, output digest, required area coverage, validity window and approval policy. It admits the artifact or holds it and opens a ticket with the failed checks.

### 3. Why It's NOT a Duplicate
There’s no change-detection dashboard here. The product protects the **handoff between an EO processor and the system that acts on its output**. A valid signature can tell you who attested to a file; it cannot by itself tell a buyer whether yesterday’s tile is acceptable, whether the area is complete, or whether the workflow version is approved. OrbitReceipt makes those buyer-specific checks enforceable at ingest.

### 4. Target Buyer & Business Model
Sell to **EO service integrators delivering into critical-infrastructure workflows**. Their delivery or security lead pays for a reusable acceptance gate rather than writing bespoke checks for every utility contract. Propose a **€10k–€20k onboarding pilot** covering one producer, one buyer and one data product, then an annual fee per governed feed or environment. The commercial test: can the gate replace a manual acceptance checklist the buyer already uses?

### 5. 48-Hour Prototype Scope
Fetch two real Sentinel-2 acquisitions for one area, process small crops and stand up a producer and an independently configured consumer. Demo acceptance of the correct product, rejection of a **correctly signed but expired** product, and rejection of an output whose digest does not match its receipt. Send a structured failure ticket and show the consumer retaining the last approved artifact with a visible age label. Use a standard signature library, not custom cryptography.

### 6. Biggest Risk & Likely Jury Pushback
**“You’re signing your own output. That doesn’t establish satellite-source authenticity or prove the processing was correct.”** Correct. The receipt is an attestation from an approved worker, not a Copernicus signature. A compromised worker or signing key is outside the prototype’s guarantee. Narrow the promise to delivery integrity and consumer-side acceptance policy, and show the authorization boundary in one diagram. If the jury asks why this needs EU Space, point to the tests that depend on actual sensing time, product footprint and scene-quality metadata—not merely the file hash.

## 4. AirShift — Outdoor work-order rescheduling during smoke episodes

### 1. One-Line Pitch & Challenge Track
**Challenge 2 — Space-enabled crisis response and civil resilience.** Give a municipal field-operations supervisor a revised crew schedule during a particulate episode, with each outdoor task marked **keep, move, or review** under the employer’s own policy.

### 2. Exact EU Space Data/Signal Pipeline
Retrieve hourly surface **PM₂.₅** from **CAMS European air-quality forecasts** via the [Atmosphere Data Store](https://ads.atmosphere.copernicus.eu/), retaining forecast issue time and lead time. Join grid-cell forecasts to quality-flagged Polish **GIOŚ** station observations where available. Use stations as a recent local check, not as ground truth for every job site. For a documented smoke event, add valid **Sentinel-3 SLSTR Level-2 Fire Radiative Power** detections from the EUMETSAT Data Store as regional fire context. **CAMS and station observations drive the schedule; a Sentinel-3 detection neither proves smoke reached a job site nor triggers a move.** Overlay work-order locations, time windows and dependencies, then move flexible tasks into lower-exposure windows allowed by policy.

### 3. Why It's NOT a Duplicate
Air-quality alerts tell a supervisor conditions may deteriorate. AirShift tells them **which jobs can move without missing service deadlines, and which need a human decision**. The output is a work-order change set and a supervisor approval record, not a plume map. The same workflow is useful on non-wildfire particulate days, which improves the buying case in Poland.

### 4. Target Buyer & Business Model
Start with a **municipal services contractor** employing outdoor crews across multiple sites. The operations director pays for fewer last-minute cancellations; occupational health and safety staff own the policy. Propose a **PLN 25k–50k seasonal pilot** for one depot and one work-order integration, followed by a per-depot subscription. Sell it as planning support, not personal exposure measurement, medical guidance or proof of compliance.

### 5. 48-Hour Prototype Scope
Replay one archived Polish particulate episode with a real CAMS forecast and station observations, and load 12 synthetic jobs with different locations, deadlines and flexibility. Run the scheduler live and export the approved changes as CSV or a webhook. Compare it with a blanket cancellation policy: report how many jobs move, how many remain on schedule, and how many require review. Use Sentinel-3 fire context only if the selected episode supports it; don’t force a fire attribution into the demo.

### 6. Biggest Risk & Likely Jury Pushback
**“A regional forecast grid cannot resolve exposure at a particular work site.”** It can’t. Make decisions at the grid-cell and time-window scale, surface disagreement with ground stations, and send high-consequence or poorly supported decisions to review. Use an archived forecast issued **before** the work window, not a retrospective analysis presented as what the supervisor would have known. The pilot should test schedule usefulness and false holds before anyone claims a health benefit.

## 5. WasteDocket — Cross-border waste inspection triage

### 1. One-Line Pitch & Challenge Track
**Challenge 3 — Countering transnational crime and terrorism with space data.** Give environmental inspectors an auditable queue of cross-border waste shipment cases where declared receiving-site activity warrants a desk review.

### 2. Exact EU Space Data/Signal Pipeline
Retrieve **Sentinel-2 Level-2A** B04, B08 and B11 plus the Scene Classification Layer through **CDSE/openEO** or a CDSE processing interface. For one permitted yard and its immediate surroundings, mask clouds, shadows and snow; align bands at **20 m**, respecting B11’s native resolution; and measure persistent changes in broad surface characteristics against a seasonal baseline. Join only predefined receiving-site polygons to permit records and authorized shipment metadata. Compare anomaly timing with declared receipt windows and record valid-pixel coverage. The output is **review suggested**, **no material anomaly observed**, or **insufficient imagery**—never “illegal shipment detected.”

### 3. Why It's NOT a Duplicate
The unit of work is **a shipment-to-permit case assigned to an inspector**, not a change pixel. A site change by itself does not create a case. The demo shows a persistent observation that matters in the shipment context, an ordinary yard change that does not escalate, and a clouded site that remains unknown. Each case packet includes the observations, dates, data-quality limits and an alternative explanation to check.

### 4. Target Buyer & Business Model
Pitch **GIOŚ or a cross-border waste inspection authority** as the design partner, with a public-sector systems integrator as the likely procurement channel. Propose a **€20k–€40k regional pilot** for a bounded set of facilities, then an annual workflow and data-integration license. The 2026 tailwind is the revised EU Waste Shipment Regulation and the move to digital waste-shipment exchanges, including DIWASS. **Do not assume those records are public or that an API is available to your team.** The buyer’s measurable benefit is fewer low-value desk reviews per useful inspection referral.

### 5. 48-Hour Prototype Scope
Use real Sentinel-2 time series over three public industrial footprints, with clearly synthetic permit boundaries, shipment records and case labels. Build the quality mask, interpretable change features, case rules and a downloadable inspection packet. Show the inspector dismissing a case for a plausible non-criminal reason and saving that decision to the audit log. Do not name real facilities as suspicious in the pitch.

### 6. Biggest Risk & Likely Jury Pushback
**“You cannot identify waste type, quantity, legality or intent from Sentinel-2.”** Correct. Only evaluate sites large enough to yield multiple usable 20 m pixels, and treat small or indoor facilities as out of scope. Construction, aggregate storage and seasonal changes can look similar. If you secure a pilot, evaluate on authorized historical cases against a **records-only baseline**. If imagery does not improve the review queue at a fixed workload, drop that feature rather than claim detection.

**Competition call:** Choose **ClockWitness** for technical differentiation, **PumpSlot** for the strongest execution odds, or **WasteDocket** if you can get an inspector to validate the workflow before the event. In Warsaw, lead with the hardest technical objection and show how the prototype handles it. At European Demo Day, lead with the buyer’s decision before and after your tool. In both rooms, show the actual artifact—a signed incident record, a dispatch order, a release rejection, a work-order change set, or an inspection packet—before showing a map.