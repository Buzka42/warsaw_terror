### 1. ClockEvidence — OSNMA Incident Notary for Critical Infrastructure

1. **One-Line Pitch & Challenge Track:** **Challenge 1 —** A receiver-independent gateway that converts Galileo OSNMA status, receiver observables and independent clock telemetry into signed incident evidence and an immediate holdover recommendation for GNSS-dependent infrastructure.

2. **Exact EU Space Data/Signal Pipeline:** Consume Galileo **E1-B I/NAV OSNMA authentication results** from an OSNMA-capable receiver over serial/MQTT, alongside receiver-reported Galileo System Time, clock bias/drift, per-satellite C/N₀ and AGC. Fuse these with local PTP/NTP or oscillator-holdover telemetry and, optionally, a second receiver. Detect persistent clock divergence, abrupt clock steps and inter-receiver disagreement; OSNMA failure alone never constitutes an attack verdict. Emit an ES256-signed evidence bundle containing raw observations, thresholds and timestamps, invoke a SIEM/OT webhook recommending holdover, and prefill the 24-hour incident-reporting workflow where NIS2 applies.

3. **Why It's NOT a Duplicate:** This is not a geographic jamming/spoofing heatmap or border-monitoring product. It protects a specific substation, telecom site or data centre and delivers a machine-actionable incident, forensic evidence and recovery recommendation. Antenna disconnections and ordinary receiver faults are explicit negative controls rather than being labelled “spoofing.”

4. **Target Buyer & Business Model:** Electricity TSOs/DSOs, mobile-network operators, rail infrastructure managers and financial data centres pay an annual **per-monitored-site subscription**, with hardware integration sold as a paid deployment. Existing receivers may detect anomalies, but operators still lack cross-vendor evidence preservation and integration with incident-response systems. Operational OSNMA and NIS2/CER resilience programmes create a 2026 procurement hook.

5. **48-Hour Prototype Scope:** Build fresh Python adapters, a transparent rule engine, signed JSON evidence, a mock SIEM webhook and an incident-report generator. Replay clean, jammed, spoofed/replayed and oscillator-fault receiver traces; use a live OSNMA receiver if available, otherwise clearly labelled public/sample receiver logs. Demonstrate that the clean trace passes, an antenna fault remains “unknown/fault,” and a synthetic spoofing sequence produces a signed alert and holdover ticket. FastAPI, MQTT and standard cryptography libraries are sufficient.

6. **Biggest Risk & Likely Jury Pushback:** “OSNMA authenticates navigation data, not the ranging signals or receiver position, so this cannot prove spoofing.” Agree explicitly: it does not stop jamming, replay/meaconing or every spoofing attack. The product is a multi-observable incident-evidence and response layer, not an “unspoofable receiver”; ambiguous cases remain unknown, and production validation requires hardware-in-the-loop RF testing and independent holdover.

---

### 2. ReCell — Mobile-Network Restoration Dispatch

1. **One-Line Pitch & Challenge Track:** **Challenge 2 —** ReCell converts Sentinel-1 flood evidence and mobile-operator outage telemetry into optimised Cell-on-Wheels, generator and crew work orders that maximise restored population and critical-service coverage.

2. **Exact EU Space Data/Signal Pipeline:** Access **Sentinel-1 GRD IW VV/VH** pre-event and event acquisitions through **CDSE/openEO**, applying calibration, speckle handling and terrain correction; use **Copernicus DEM GLO-30** for access and pre-approved-site constraints. Fuse SAR water likelihood with operator cell-outage telemetry, OSM roads, GHSL population and hospital/shelter locations. OR-Tools assigns limited COW units, generators and crews to maximise weighted coverage restored per travel hour. Field closure messages contain device-signed **Galileo OS positions and OSNMA status**, treated as supporting evidence rather than spoof-proof location proof. The output is a dispatch/reroute API, not an EO layer.

3. **Why It's NOT a Duplicate:** It does not merely display flooded roads or damaged infrastructure. The core computation is resource-constrained restoration optimisation, and every result is a specific crew assignment with destination, expected restored coverage and access rationale. There is no vague “AI crisis brain”: SAR estimates environmental constraints, operator data identifies outages, and the optimiser makes the decision.

4. **Target Buyer & Business Model:** Mobile-network operators, tower companies and their managed field-service contractors buy an **annual network-readiness licence plus per-activation usage**; voivodeship crisis centres can purchase access through joint resilience contracts. The economic buyer is the network-operations continuity team, which already pays for emergency COW deployment and faces NIS2/CER service-continuity pressure.

5. **48-Hour Prototype Scope:** Use real archived Sentinel-1 acquisitions from a Polish flood, a county-scale OSM road graph, 30–50 synthetic or anonymised cell records and three simulated COW units. Build the fresh-code openEO pipeline, road-cost calculation and OR-Tools optimiser. Live-demo three dispatch tickets, then close one road and regenerate the plan. Report population/critical-site coverage restored per crew-hour against a nearest-outage baseline; use a minimal work-order interface only to expose the API results.

6. **Biggest Risk & Likely Jury Pushback:** “Ten-metre SAR cannot certify road passability, and COW placement is a radio/backhaul problem.” Correct: ReCell produces conservative, human-approved dispatch recommendations, not safety certification. Production deployment is restricted to operator-approved COW sites with known power, spectrum and backhaul options, while uncertain road segments remain excluded or require field confirmation. The prototype’s claimed value is better prioritisation under constraints, not autonomous network restoration.

---

### 3. DIWASS Crosscheck — Transnational Waste-Shipment Inspection Broker

1. **One-Line Pitch & Challenge Track:** **Challenge 3 —** DIWASS Crosscheck correlates digital waste-shipment records with independent Copernicus site evidence and carrier arrival events to generate inspection-ready cases for suspected diversion, fictitious recovery and illegal dumping.

2. **Exact EU Space Data/Signal Pipeline:** In production, ingest DIWASS notification, consent, movement and destination-confirmation records through an interoperability adapter aligned with **Implementing Regulation (EU) 2025/1290**, plus national BDO permits and facility data. For declared destinations and related facilities, retrieve **Sentinel-2 L2A** multispectral bands/SCL and **Sentinel-1 GRD VV/VH** through CDSE/openEO. Compute transparent site-level features—yard spectral change, disturbed extent, SAR backscatter change and observation gaps—without claiming to identify waste or weigh it. Add consented carrier **Galileo OS position plus OSNMA status** in device-signed arrival events. Rules correlate missing destination confirmation, arrival mismatch, repeated capacity inconsistencies and corroborating activity at undeclared sites; the output is a ranked inspection case tied to shipment and facility IDs.

3. **Why It's NOT a Duplicate:** This is not a Sentinel-2 change-detection dashboard searching for suspicious brown patches. EO is only corroborating evidence inside a shipment-specific enforcement workflow. Each alert states which legal record is inconsistent, what independent evidence supports review and which authority should inspect; there is no AIS, dark-vessel or generic crime map.

4. **Target Buyer & Business Model:** Environmental inspectorates and customs authorities pay an **annual jurisdiction licence plus notification volume**; large exporters and recyclers form a faster private-entry market, paying per shipment for independent audit evidence. DIWASS went live on **21 May 2026**, and the EU prohibition on plastic-waste exports to non-OECD countries applies from **21 November 2026**, creating immediate enforcement and compliance workloads.

5. **48-Hour Prototype Scope:** Generate 20–30 transparent synthetic DIWASS fixtures from published document fields—explicitly not claiming production-system access—and geocode several real facilities from public permits. Process genuine Sentinel-1/Sentinel-2 time series for two facilities, implement five explainable correlation rules, and expose a FastAPI endpoint that returns clean/review/inspection decisions with signed JSON and a compact evidence PDF. Demo a clean shipment, a missing-destination confirmation and a diversion scenario containing real EO change.

6. **Biggest Risk & Likely Jury Pushback:** “DIWASS/BDO access will be difficult, and satellites cannot prove illegal waste or measure tonnage.” Both are true. The prototype separates the tested adapter contract from restricted production access, and the product only prioritises human inspection—it never declares illegality or derives tonnage from pixels. OSNMA validates navigation-message origin, not the carrier’s physical delivery; legal chain of custody still requires inspection, weighbridge and laboratory evidence.

---

### 4. SentinelGate — Zero-Trust Firewall for Copernicus-Driven Decisions

1. **One-Line Pitch & Challenge Track:** **Challenge 1 —** SentinelGate quarantines substituted, stale or incorrectly processed Copernicus inputs before they reach automated utility or civil-protection workflows, while issuing signed, reproducible provenance for every accepted result.

2. **Exact EU Space Data/Signal Pipeline:** Resolve **Sentinel-1 GRD IW VV/VH** product UUIDs, acquisition metadata and checksums through **CDSE OData/STAC**, retrieve source products through CDSE, and execute a pinned **openEO process graph** for a concrete flood-exposure decision. Independently verify product identity, AOI, acquisition freshness and approved processing policy; hash the openEO graph, local reference code and output. Recompute a small critical tile using a deterministic local implementation and compare within stated numerical tolerance. Return `ACCEPT` or `QUARANTINE`, sign the complete provenance record and open a security ticket on failure.

3. **Why It's NOT a Duplicate:** The flood calculation is merely the test workload; the product is cybersecurity middleware for the EO supply chain. It protects downstream caches, third-party APIs and derived decision layers rather than producing another map. Its live demo centres on defeating stale-product substitution, output-raster tampering and unauthorised process-graph changes.

4. **Target Buyer & Business Model:** EO analytics companies serving regulated utilities, national civil-protection platforms and insurers buy **annual protection per connected pipeline plus processing volume**, with an initial paid integration audit. The willingness to pay comes from preventing automated decisions on corrupted supplier data and producing investigation-ready provenance; the product supports NIS2 supplier-risk controls without claiming that NIS2 explicitly mandates it.

5. **48-Hour Prototype Scope:** Build one county-scale openEO workflow and a local reference implementation using public Python libraries. Add four fresh-code attack fixtures: a clean run, an older scene substituted under a plausible filename, a modified derived GeoTIFF and an unapproved threshold in the process graph. Demonstrate clean acceptance, three quarantines, an ES256-signed in-toto-style provenance JSON and automatic ticket creation. Pin the backend and processing versions so the demo remains reproducible.

6. **Biggest Risk & Likely Jury Pushback:** “TLS and provider checksums already solve this, and openEO jobs are not necessarily bit-for-bit reproducible.” TLS does not protect a downstream cache, contractor or derived output after delivery. SentinelGate’s added layer is independent source verification, approved-process policy and decision-output replay. The prototype guarantees reproducibility only for its pinned local reference path, uses tolerances where necessary and never claims to prove physical truth or defend against a fully compromised CDSE itself.

---

### 5. AccessSure — Parametric Flood-Access Claims API

1. **One-Line Pitch & Challenge Track:** **Challenge 2 —** AccessSure provides insurers and infrastructure operators with an auditable parametric trigger that releases emergency liquidity when a pre-agreed critical access route becomes flood-obstructed, rather than waiting for a physical damage assessment.

2. **Exact EU Space Data/Signal Pipeline:** For each insured route, retrieve baseline and event **Sentinel-1 GRD IW VV/VH** acquisitions through CDSE/openEO and compute calibrated backscatter change and persistent water likelihood only on pre-qualified, exposed road segments. Combine that result with a policy-specific river-gauge threshold and consecutive-observation rule; use Copernicus EMS delineations as validation where an activation exists. A device-signed field report containing **Galileo OS position and OSNMA status** provides an appeal or secondary-confirmation channel. The engine emits a signed claims certificate containing acquisition IDs, thresholds, segment evidence and confidence directly to the insurer’s claims API.

3. **Why It's NOT a Duplicate:** The insured event is **loss of access**, not visible flood extent or building damage, and the product’s output is a reproducible payout decision. It is not a road-flood map, real-time navigation service or black-box catastrophe model. Its differentiation from broad parametric flood products is the customer-defined route trigger, transparent evidence bundle and field-appeal mechanism.

4. **Target Buyer & Business Model:** Insurers and reinsurers buy an **annual monitored-corridor subscription plus per-policy API fee**, initially targeting utilities, municipal mutuals and humanitarian logistics buyers that need rapid cash for generators, alternative transport and emergency suppliers. The insurer owns the policy and regulatory relationship; AccessSure sells independent trigger computation and auditability rather than becoming an insurer.

5. **48-Hour Prototype Scope:** Select three real routes from an archived Polish flood, including one non-trigger control, and process genuine pre-event, event and post-event Sentinel-1 acquisitions. Encode one sample policy, calculate its segment-level trigger, validate the result against available gauge or EMS evidence, and issue signed certificates to a mock claims endpoint. Live-demo trigger, no-trigger and field-appeal paths; no blockchain or real payment rail is required.

6. **Biggest Risk & Likely Jury Pushback:** “Sentinel revisit latency and SAR observability create unacceptable basis risk.” AccessSure therefore sells delayed emergency-liquidity settlement, not minute-by-minute passability or life-safety routing. Policies are restricted to suitable exposed segments, include observation-gap rules, dual triggers and human appeal, and require multi-event backtesting before launch. Narrow or vegetation-covered routes are explicitly uninsurable by this trigger rather than silently misclassified.
