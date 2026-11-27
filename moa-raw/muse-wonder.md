# 5 High-Conviction Ideas for CASSINI Warsaw 2026

Winning strategy for Warsaw: **don't sell a map. Sell a signed decision, a work order, a customs hold, a routing instruction, or a NIS2 evidence file** that a named Polish/EU institution must produce anyway in 2026.

---

## 1. TimeSeal — Galileo-Authenticated Timing Forensics for Power & Telecom

### 1. One-Line Pitch & Challenge Track
**Challenge 1: Cybersecurity for space-based strategic enablers** — An OSNMA timing-integrity agent for substations and 5G sites that detects GNSS time spoofing and automatically generates a signed, NIS2-ready incident evidence pack and SCADA/SOC ticket.

### 2. Exact EU Space Data/Signal Pipeline
- **Galileo Open Service + OSNMA:** Receiver / simulated receiver feed provides Galileo E1-B I/NAV, OSNMA TESLA keys, MACK messages, navigation data. Pipeline verifies DSM-KROOT chain and TESLA key authentication using open Python OSNMA libraries and EUSPA test vectors.
- **Galileo HAS / multi-GNSS cross-check:** Compare Galileo-authenticated time/position against GPS/GLONASS observables, receiver clock bias jumps, C/N0, AGC and pseudorange residuals. A time step that is cryptographically unauthenticated, or authenticated Galileo diverging from other constellations, raises severity.
- **EGNOS:** Used as independent integrity/time reference where available via EDAS-style data.
- **Access/compute:** Live demo can use recorded Septentrio/Android raw GNSS logs + EUSPA OSNMA test vectors, plus a software spoof injector that shifts clock +2 microseconds / replays old nav data. Output is hash-chained, Ed25519-signed JSON + PDF evidence bundle: raw observables hash, OSNMA verification status, clock drift plot, affected asset ID, and recommended action — `SWITCH_TO_HOLDOVER`, `OPEN_NIS2_INCIDENT`, timestamped for the NIS2 24h early-warning clock.
- **Integration output:** Webhook to a mock ServiceNow / TheHive / SCADA ticket system, not a heatmap.

### 3. Why It's NOT a Duplicate
It is not a jamming/spoofing heatmap for aviation or borders. It solves the **post-detection legal and operational bottleneck**: Polish TSOs, DSOs and telcos must prove *when* timing integrity was lost, *what* data proves it, and *when* they reacted. TimeSeal turns OSNMA from a receiver feature into an auditable incident workflow and an automatic holdover-oscillator trigger.

### 4. Target Buyer & Business Model
- **Buyers:** PSE / Tauron Dystrybucja / Enea Operator substation automation teams; Orange Polska / Polkomtel 5G timing teams; PKP PLK signalling-time operators; their SOC providers.
- **Why 2026:** NIS2 24h incident reporting + Critical Entities Resilience Directive audits make “our GPS glitched” indefensible. Phasor Measurement Units and 5G TDD both collapse on bad time.
- **Model:** €8–25k per critical site/year for software agent + evidence vault, or €40–80k per SOC deployment. Hardware-agnostic overlay on existing receivers is the wedge.

### 5. 48-Hour Prototype Scope
Team builds: (1) log parser for Galileo raw/OSNMA test data, (2) spoof injector UI — replay attack, time jump, constellation divergence, (3) OSNMA verification status + clock-bias anomaly detector, (4) one-click signed NIS2 evidence PDF/JSON generator, (5) mock SOC ticket webhook firing live.
**Sunday demo:** Run clean log → green “Authenticated Time”. Inject +5µs spoof → OSNMA/auth mismatch, ticket auto-created, evidence bundle hash verified live in front of jury.

### 6. Biggest Risk & Likely Jury Pushback
**Pushback from ChipCraft / Cyber Defense Forces:** “OSNMA authenticates navigation data origin, it does not stop jamming, meaconing delay, or a compromised receiver. And you have no real receiver.”
**Defence:** Concede precisely. TimeSeal never claims anti-jam. It claims **non-repudiation**: authenticated vs unauthenticated time, cross-constellation residual checks, and a tamper-evident log generated outside the receiver. Prototype uses EUSPA vectors because OSNMA live-chip access in 48h is unrealistic — the product roadmap is Septentrio/u-blox OSNMA receiver integration. That honesty wins technical juries.

---

## 2. BridgePass — GO / NO-GO Bridge Routing for Heavy Rescue Convoys

### 1. One-Line Pitch & Challenge Track
**Challenge 2: Space-enabled crisis response and civil resilience** — A routing API that tells State Fire Service and military logistics whether a 30–44 tonne rescue convoy can cross a specific bridge after flood/impact, and reroutes it if not.

### 2. Exact EU Space Data/Signal Pipeline
- **Copernicus EGMS (European Ground Motion Service, Sentinel-1 InSAR):** Pre-event millimetre deformation velocity/line-of-sight displacement for bridge AOIs in Poland — the baseline structural trend.
- **Sentinel-1C SAR via CDSE/openEO:** Sentinel-1 IW GRD + SLC coherence. Pipeline computes pre/post-event coherence loss and backscatter change over bridge deck/abutment polygons; coherence collapse = possible scour, deck displacement or debris.
- **Sentinel-2C L2A via CDSE/openEO:** When cloud-free, water extent / road inundation at approaches, NDWI.
- **Ground layers:** GDDKiA / BDOT10k bridge registry, weight limits, road network. Fusion produces per-bridge score: `GREEN cross at normal load / AMBER single-vehicle, engineer check / RED do not cross`.
- **Output:** Modified GraphHopper/OSRM routing graph where RED bridges are removed and AMBER bridges get heavy penalty. API returns route + machine-readable justification per bridge.

### 3. Why It's NOT a Duplicate
Not a “damaged buildings on a map.” The user never wanted flood extent — a PSP/KW PSP duty officer wants to know: *“Can this 40t pumper / military transporter get to Kutno in the next 2 hours, yes or no, and by which road?”* The deliverable is a legally defensible routing decision with an audit trail for sending — or not sending — a heavy vehicle over a suspect structure.

### 4. Target Buyer & Business Model
- **Buyers:** Komenda Główna PSP, wojewódzkie crisis-management centres, Territorial Defence Forces logistics, GDDKiA, road-freight insurers / heavy-haul operators (post-flood rerouting).
- **Model:** B2G platform licence €60–150k/voivodeship/year + per-incident API pricing for insurers/logistics. Peacetime value: prioritize bridge inspection budgets using EGMS deformation trends — pays outside disasters.
- **Why 2026:** Sentinel-1C restores 6-day dual-satellite revisit; EGMS makes InSAR buyable without building an InSAR company.

### 5. 48-Hour Prototype Scope
Pre-select 15–25 bridges on one Polish river corridor (e.g., Wisła / Bzura). Pre-download EGMS + one Sentinel-1 pre/post pair for a historical flood or use coherence-loss simulation seeded from real GRD scenes. Build: openEO CDSE query live for latest Sentinel-1/2 over AOI, bridge scoring function, GraphHopper route with/without RED bridge.
**Sunday demo:** Enter “Warsaw → flooded municipality, 40t vehicle”. System returns Route A rejected — Bridge X coherence loss + approach inundation — Route B approved, with per-bridge evidence card. Change one bridge to RED live, route recalculates.

### 6. Biggest Risk & Likely Jury Pushback
**Pushback from IGiK / Scanway:** “EGMS updates are slow, Sentinel-1 is 6–12 days, InSAR cannot certify a bridge safe, coherence loss has many causes.”
**Defence:** Agree — BridgePass never certifies safety. It is a **triage and exclusion** tool: it only has authority to say NO-GO / CHECK, never structural approval. Baseline EGMS is pre-computed in peacetime; in crisis, even one post-event coherence scene + approach flooding eliminates the worst bridges, which is exactly the decision bottleneck. Field engineer confirms AMBER. Framing it as “satellite structural certification” would be killed; framing it as convoy risk triage survives.

---

## 3. RailManifest — SAR-vs-Customs Reconciliation at the Eastern Border

### 1. One-Line Pitch & Challenge Track
**Challenge 3: Countering transnational crime and terrorism with space data** — Reconciles Sentinel-1-observed rail transshipment activity at Poland–Belarus/Ukraine gauge-change terminals against declared customs manifests, and auto-generates an inspection-hold ticket when physical activity and paperwork disagree.

### 2. Exact EU Space Data/Signal Pipeline
- **Sentinel-1C IW GRD via CDSE/openEO:** SAR backscatter time series over fixed terminal polygons (Małaszewicze-type AOI, anonymized in demo). Rail yards are strong, stable radar reflectors; pipeline computes change in yard occupancy proxy — total high-backscatter train-length along known track lines, dwell time of consists between passes.
- **Sentinel-2C L2A:** Cloud-free corroboration: train consists, bulk piles (grain, timber, fertilizer), truck queues.
- **Copernicus EMS / EGMS infrastructure masks:** Track geometry from OpenStreetMap + BDOT-type layers constrains detection to track polylines — reduces false positives.
- **Ground/customs layer (mock in prototype):** Declared manifest CSV/API — wagon count, commodity code, declared dwell. Fusion engine flags: observed consist present with no manifest; dwell 3× declared (possible relabelling); bulk pile volume change inconsistent with declared tonnage.
- **Output:** KAS/OLAF-style inspection ticket: terminal, time window, SAR scene IDs, observed-vs-declared delta, confidence, recommended action `HOLD_FOR_INSPECTION`, with scene provenance hashes.

### 3. Why It's NOT a Duplicate
This is the deliberate land-based inversion of the banned “dark vessel” cliché — and it is not a tracker. There is no AIS to switch off on rail; the crime is **paper fraud**: sanctions relabelling, commodity-code switching and undeclared transshipment at the standard/broad-gauge break. The product is manifest reconciliation and a customs workflow trigger, aimed at a fixed, finite set of high-value terminals — not global ship dots.

### 4. Target Buyer & Business Model
- **Buyers:** Krajowa Administracja Skarbowa (KAS), EU OLAF / EU sanctions-enforcement units, PKP Cargo / terminal operators (self-audit proof), trade-compliance and cargo insurers, sanctions-screening firms.
- **Model:** €15–40k per terminal/year monitoring + per-alert evidence fee; enterprise compliance version for freight forwarders who must prove they did *not* handle sanctioned cargo.
- **Why 2026:** EU Russian/Belarusian timber, fertilizer, steel and dual-use sanctions enforcement is shifting from declarations to physical verification. Małaszewicze is one of Europe’s most strategic rail chokepoints — Polish jury relevance is immediate.

### 5. 48-Hour Prototype Scope
One terminal AOI. Use real Sentinel-1 GRD time series from CDSE (6–10 scenes) via openEO; detect high-backscatter linear features on track masks; compute yard-occupancy index per date. Build manifest-upload page, discrepancy rules, ticket generator.
**Sunday demo:** Upload manifest declaring “12 wagons, 24h dwell”. System shows SAR series indicating consist present across 3 passes / 6 days → auto-generates HOLD ticket with scene IDs. Upload matching manifest → ticket closes. Jury sees paperwork-vs-physics, live.

### 6. Biggest Risk & Likely Jury Pushback
**Pushback from Blue Dot / IGiK:** “Sentinel-1 is ~10–20m — you cannot count individual 3m-wide wagons or read commodity type.”
**Defence:** Never claim wagon counting or commodity ID. Claim **consist presence, aggregate train-length along a known track, and dwell time** — detectable as a persistent high-backscatter linear anomaly on a fixed track mask, validated against Sentinel-2 on clear days. Commodity comes from the manifest; space data only proves the *physical inconsistency*. Product sells discrepancy triage for inspectors who currently inspect <5% of consists — a 3× better inspection hit-rate is the KPI, not perfect counting.

---

## 4. IntakeGuard — Drinking-Water Intake Closure Decisions After Floods

### 1. One-Line Pitch & Challenge Track
**Challenge 2: Space-enabled crisis response and civil resilience** — Predicts when a flood-driven turbidity/contamination plume will reach a drinking-water intake and automatically issues the signed closure / boil-water decision pack for the water utility and Sanepid.

### 2. Exact EU Space Data/Signal Pipeline
- **Sentinel-1C GRD via CDSE/openEO:** Flood extent and duration upstream of intake, day/night, through cloud — defines contaminated surface-water source area.
- **Sentinel-2C L2A via CDSE/openEO:** Water-quality retrieval on river reaches: turbidity proxy (red/red-edge reflectance, NDTI), chlorophyll/NDCI where relevant. Processed with openEO UDP / standard aquatic reflectance algorithms — no black-box “AI”.
- **Sentinel-3 SLSTR/OLCI:** Daily wider-swath turbidity/thermal corroboration between Sentinel-2 passes.
- **Copernicus EMS:** Activation products as validation layer when available.
- **Ground fusion:** Intake locations and river network (BDOT / Wody Polskie), upstream industrial/agricultural risk sites (wastewater plants, fuel depots from public registries), river flow velocity (IMGW public data). Simple advection model: plume travel time = distance / flow, widened by uncertainty band.
- **Output:** Decision pack with countdown: `INTAKE X — predicted plume arrival 14:00–19:00 tomorrow — recommended CLOSE at 12:00`, draft public notice, SMS/alert text, and signed evidence log for EU Drinking Water Directive compliance.

### 3. Why It's NOT a Duplicate
Not a flood map. Flood maps already exist and water utilities still close intakes too late or too early because nobody converts upstream imagery into **“close this intake at this hour, here is your legal evidence.”** The bottleneck is the accountable decision and public notice under time pressure — IntakeGuard outputs the notice, the timing, and the audit trail. Map is an internal intermediate, never the product shown first.

### 4. Target Buyer & Business Model
- **Buyers:** MPWiK Warszawa and regional water utilities (wodociągi), Wody Polskie, voivodeship Sanepid stations, municipalities legally responsible for boil-water notices.
- **Model:** €30–90k per utility catchment/year; per-incident decision-pack pricing for small utilities that cannot staff remote-sensing teams. Insurers of business-interruption from water shutdowns are secondary buyers.
- **Why 2026:** Drinking Water Directive risk-based catchment obligations + CER resilience duties for water operators. One late closure is a public-health and liability event; one unnecessary closure costs hundreds of thousands in tanker water.

### 5. 48-Hour Prototype Scope
One river reach with a real intake (Wisła near Warsaw / Gruba Kaśka context, or Odra). Pull real Sentinel-2 L2A via CDSE openEO live, compute NDTI turbidity on river mask, pull one Sentinel-1 flood scene, implement travel-time model with IMGW flow input, generate decision PDF + alert text.
**Sunday demo:** Select upstream flood/turbidity event from a historical scene → system computes arrival window at intake → generates closure recommendation and ready-to-send public notice in Polish, with scene IDs and uncertainty stated.

### 6. Biggest Risk & Likely Jury Pushback
**Pushback from IGiK:** “Sentinel-2 is 5-day and cloud-blocked exactly during floods; turbidity retrieval in narrow rivers is mixed-pixel and uncalibrated.”
**Defence:** Correct — therefore Sentinel-2 turbidity is corroboration, Sentinel-1 flood extent + upstream risk-site registry + flow model is the primary trigger, and output is an **arrival window with explicit confidence**, not a concentration measurement. Turbidity algorithm is presented as relative anomaly vs that reach’s own baseline, never as mg/L without in-situ calibration. Roadmap: calibrate with utility’s own intake turbidity sensors — which also creates the data moat.

---

## 5. WasteAlibi — Breaking Spoofed-Geofence Alibis in Illegal Waste Crime

### 1. One-Line Pitch & Challenge Track
**Challenge 3: Countering transnational crime and terrorism with space data** — Destroys the “our trucks were never there” defence in illegal waste dumping by fusing Galileo OSNMA-authenticated vehicle positions with Sentinel evidence of dump growth, into a court-ready inspection pack for GIOŚ.

### 2. Exact EU Space Data/Signal Pipeline
- **Galileo OSNMA + HAS:** Fleet tracker positions are only accepted as alibi evidence if the underlying Galileo nav data passes OSNMA authentication. Spoofed/replayed positions fail authentication or show HAS-corrected position diverging from claimed position → alibi flagged as unreliable. This is the cryptographic core.
- **Sentinel-2C L2A via CDSE/openEO:** SWIR/NIR change at registered and suspected warehouse/plot polygons: new waste piles, bare-soil disturbance, burned areas (SWIR burn signal). Relative change vs site baseline.
- **Sentinel-3 SLSTR thermal / FIRMS-type active-fire data:** Thermal anomaly corroboration for waste-fire risk sites.
- **Ground registries:** BDO waste-transport registry (mock/API-shaped in prototype), warehouse/plot registry, prior GIOŚ inspection addresses. Sites scored: BDO-declared activity vs observed physical change vs authenticated truck presence near site.
- **Output:** Ranked inspection warrant pack: site, dates, Sentinel scene IDs, OSNMA-authentication failures for vehicles claiming absence, before/after chips, chain-of-custody hash. Delivered as inspector task list in QField/GeoPackage format for field teams.

### 3. Why It's NOT a Duplicate
Not generic change detection and not vehicle tracking. Poland’s illegal-waste model — imported waste, rented warehouse, arson, vanished operator — survives because every party produces *paper and GPS logs that can be fabricated*. WasteAlibi attacks the **evidentiary** bottleneck: OSNMA makes the location alibi cryptographically testable, Sentinel independently proves physical change at the site, and the output is an inspection/court pack for Główny Inspektorat Ochrony Środowiska, not a dashboard for the public.

### 4. Target Buyer & Business Model
- **Buyers:** GIOŚ / voivodeship inspectorates (WIOŚ), municipalities liable for cleaning abandoned waste (cleanup costs run to millions of PLN per site), warehouse landlords and their property insurers who unknowingly rent to waste criminals, legitimate waste firms undercut by illegal operators.
- **Model:** B2G inspection-intelligence licence €50–120k/year per voivodeship; private wedge: €500–2k per site due-diligence report for warehouse insurers/landlords before signing a lease — this pays before any ministry procurement closes.
- **Why 2026:** EU Waste Shipment Regulation tightening + Polish waste-fire politics. Municipalities are financially desperate to catch sites *before* abandonment, when the polluter can still pay.

### 5. 48-Hour Prototype Scope
Pick 2–3 known-style warehouse AOIs (anonymized). Pull real Sentinel-2 time series via CDSE, compute SWIR change chips. Build mock BDO manifest + truck-log upload; run one log through OSNMA test-vector verification showing “authenticated” vs one replayed log showing failure; fuse into ranked site list and generate inspection pack PDF + GeoPackage.
**Sunday demo:** Suspect’s truck log claims “never within 20km”. System shows OSNMA authentication failure on that log segment + Sentinel-2 pile growth at the warehouse that week → inspection pack generated, ranked #1 for Monday morning.

### 6. Biggest Risk & Likely Jury Pushback
**Pushback from Cyber Defense Forces / lawyers on team:** “OSNMA failure proves the log is unreliable, not that the truck was at the dump. Sentinel-2 can’t see inside a closed warehouse. Courts won’t accept this.”
**Defence:** Exactly the intended standard: WasteAlibi produces **inspection grounds, not convictions**. OSNMA failure legally destroys the alibi’s credibility; Sentinel proves external change at open plots and burn/fire risk at warehouses; inside-warehouse proof remains the inspector’s job — now sent to the right address first. Evidence pack preserves scene IDs and hashes so an expert witness can reproduce every step. Sell prioritization (“inspect these 5 of 400 sites Monday”) and no judge-credible team should claim more.

---

## Recommended Pick If You Must Choose One

| Rank | Idea | Why it can win Warsaw |
|---|---|---|
| **1** | **TimeSeal** | Most differentiated, pure Challenge 1, OSNMA is 2026-operational, Polish GNSS-hardware jury can validate it, NIS2 gives a paying buyer. Hardest to copy. |
| **2** | **BridgePass** | Best live demo and clearest life-safety decision. EGMS shortcut makes InSAR credible in 48h. |
| **3** | **RailManifest** | Highest geopolitical relevance at the Polish eastern border; strong European Demo Day story. |

**Build rule for any of the five:** first screen of the demo is the *output artefact* — ticket, evidence PDF, route, closure notice, inspection pack. Show the satellite map only when a juror asks “prove it.” That single inversion separates you from every “nobody is waiting for your map” team in the room.