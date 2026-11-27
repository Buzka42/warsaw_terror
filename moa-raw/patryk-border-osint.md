# ŚLAD: Persistent Disturbance Leads for Border Patrol Tasking

*Expanded from Patryk's seed idea (2026-11-27). Working name: "ślad" is Polish for "trace" or "track".*

---

## 1. One-Line Pitch & Challenge Track

**ŚLAD gives border analysts a ranked weekly queue of patrol leads. It flags grid cells along a chosen border segment where Sentinel-1 shows repeated ground disturbance on plausible crossing corridors, after removing the farming, forestry, weather and construction effects that drown out raw change detection. Each lead goes out as a TAK/KML/JSON tasking packet, and Galileo OSNMA-authenticated field confirmation closes the evidence loop.**

**Track: Challenge 3, Countering transnational crime and terrorism with space data.** Targets are organised migrant smuggling, cigarette and excise smuggling, and hybrid-threat logistics on the EU's eastern land border.

The key reframe from the seed: **we don't detect footpaths.** At C-band and 10 m pixels nobody can, and the Warsaw jury will know that. ŚLAD detects **persistent use**: the same cells disturbed again and again across consecutive 6-day pairs, on terrain that a least-cost-path model says links the border line to an inland pickup road. A one-off change is noise. A repeated change on a corridor is a lead.

---

## 2. Exact EU Space Data/Signal Pipeline

### 2.1 Core: Sentinel-1 (the all-weather backbone)

| Stream | Access | What we compute |
|---|---|---|
| **Sentinel-1 IW GRD**, VV+VH, ascending and descending | **CDSE openEO** (`load_collection("SENTINEL1_GRD")` → `sar_backscatter(coefficient="sigma0-ellipsoid")`, terrain-corrected) | Per-acquisition σ⁰ stacks over the segment AOI. With S-1A plus S-1C (and S-1D as it enters service), each relative orbit repeats every 6 days. Combining ascending and descending gives roughly 2–3 looks a week over Podlasie. |
| **Sentinel-1 IW SLC**, burst-limited to the AOI | CDSE S3 / OData download → **ESA SNAP `gpt`** (open source) or `pyroSAR` wrapper | **Interferometric coherence (γ)** for consecutive 6/12-day pairs, about 40–60 m effective cells. Coherence loss on open terrain (meadows, field margins, the cleared strip along the barrier, riverbanks) is the most sensitive available indicator of physical disturbance such as trampling, vehicle passage or digging. |

**Per-cell computation** (H3 resolution 10 cells, about 15,000 m² each, or a 50 m grid):

1. **Log-ratio change** `Δσ⁰ = 10·log10(σ⁰_t / σ⁰_t−1)` for VV and VH, plus the change in the VH/VV ratio, which is sensitive to vegetation structure.
2. **Coherence drop** `Δγ = γ_ref − γ_pair`, where γ_ref is the cell's median coherence over the previous 60 days. This applies only to cells where γ_ref > 0.3. Forest is always decorrelated at C-band and is excluded from the coherence term by design.
3. **Contextual anomaly score.** Each change is z-scored against cells of the **same land-cover class within the same segment and acquisition pair**. This cancels segment-wide effects that would otherwise flood the output: rain, wet snow, and above all **freeze–thaw in late November**, which shifts σ⁰ by several dB across whole regions.
4. **Persistence score.** We count how many of the last *N* pairs (default N = 6, about 5 weeks) put the cell above threshold, weighted toward recent pairs with a CUSUM-style accumulator. This one step separates "used corridor" from "ploughed once".

### 2.2 Confirmation: Sentinel-2 L2A (when the sky allows)

- **Access:** CDSE openEO, `SENTINEL2_L2A`, with the SCL band used as a cloud and shadow mask.
- **Compute:** ΔNDVI and ΔBSI (Bare Soil Index) per cell, and 10 m before/after RGB chips for the lead report.
- **Honest role:** in November in eastern Poland, cloud-free S-2 scenes are rare. S-2 is an **opportunistic confidence booster** and a source of human-readable imagery. Nothing in the pipeline depends on it.

### 2.3 Context layers (false-positive suppression, where most of the value lies)

| Layer | Source | Use |
|---|---|---|
| Land cover / forest | Copernicus HRL Tree Cover Density, CLC+ Backbone, ESA WorldCover | Land-cover stratification for z-scoring; coherence eligibility mask |
| Planned and executed logging | **Bank Danych o Lasach** (State Forests open data, compartment-level) | Suppress changes inside compartments with scheduled cuts |
| Agricultural parcels | Polish LPIS via Geoportal WMS/WFS (if accessible), fallback OSM `landuse=farmland` | Suppress parcel-wide uniform changes (ploughing, harvest) by checking whether the change fills the parcel or forms a linear or point pattern inside it |
| Barrier line, roads, tracks | OSM (`barrier=fence` along the PL–BY border, `highway=*`) | Corridor model; masking of **East Shield (Tarcza Wschód) construction zones**, which generate large, legitimate change |
| Weather | ERA5-Land (Copernicus Climate Data Store): soil temperature, snow depth, precipitation | Flags pairs affected by freeze–thaw or snow and down-weights them |
| Weak validation | Border Guard (Straż Graniczna) public daily counts of attempted illegal crossings, published per regional unit | Correlates the weekly lead volume per sector with reported attempts (a sanity check, not ground truth) |

### 2.4 Corridor model (the geospatial reasoning layer)

- We build a **cost surface** from land cover (dense forest is cheap to move through unseen, open field is expensive and exposed, wetland and river are very expensive except at known fords) and the barrier geometry.
- We compute **least-cost corridors** from the border line to every inland road node within 15 km. The inland road nodes stand in for vehicle pickup points, which is the documented smuggling model of a walking leg followed by a pickup.
- Each cell gets a **corridor centrality** (how many low-cost paths pass through it) and a **forest-edge exit flag**. C-band cannot see under the canopy, but people leaving the forest onto open ground near a road leave a coherence signature.

### 2.5 Lead score

```
lead_score = persistence × anomaly_magnitude × corridor_centrality × (1 − suppression_penalty)
```

The output is the top-K cells, merged into lead polygons. For each lead we record its type (forest-edge exit, barrier-strip disturbance, hinterland staging area, or far-side activity) and a confidence value.

### 2.6 Field-loop: Galileo OSNMA (evidence integrity)

- A patrol confirms or rejects the lead with a geotagged observation.
- The position comes from a **Galileo OSNMA-authenticated fix**. On the prototype this uses a u-blox ZED-F9P / X20-class receiver streaming raw navigation subframes into the open-source **OSNMAlib**, or replayed OSNMA test vectors if no hardware is available.
- The observation record is hashed together with the OSNMA authentication status and the lead ID. This gives a **tamper-evident chain of custody**, and it matters in a region where **GNSS spoofing originating from Belarus and Kaliningrad is documented**. OSNMA detects spoofing but does not help against jamming. The record logs "OSNMA: authenticated / not authenticated / no signal" and never claims more than that.
- Confirmed and rejected leads flow back as **labels**, so the threshold for each segment improves every week.

---

## 3. Why It's NOT a Duplicate

**It is not a "Sentinel-2 + AI change-detection dashboard."**
- The primary output is a **lead queue with a tasking packet**: Cursor-on-Target XML for TAK, KML for existing GIS, and a JSON webhook for an incident system. A heatmap is never the main screen.
- The core logic is not "what changed" but **"what keeps changing, on a plausible route, after removing every legitimate cause of change."** Persistence plus a corridor prior plus context suppression is a different analytic product from bi-temporal change detection.
- It is **SAR-first and coherence-based**, which most hackathon teams avoid because SLC processing is harder than pulling S-2 RGB.

**It is not a GNSS jamming heatmap.** Galileo appears only as **OSNMA evidence authentication** in the field loop, a narrow and defensible use, not as interference mapping.

**It is not a dark-vessel tracker.** This is a land border, with no AIS and no maritime domain.

**It is not a vague "AI crisis platform."** There is one user (a Border Guard sector analyst), one cadence (each new S-1 pair, rolled up into a weekly patrol-planning cycle), and one decision (where to send the next patrol, and where to put a mobile sensor).

**Overlap with sibling ideas (TorGuard, CorridorGuard, balonowy-radar):** all four share the **S-1 change-and-persistence engine**. What separates them is the target prior:

| Idea | Prior / target | Corridor model |
|---|---|---|
| **ŚLAD** | Foot and vehicle crossing usage | Border → road least-cost paths |
| TorGuard | Rail sabotage / tampering | Rail line buffer |
| CorridorGuard | Linear critical infrastructure | Pipeline / power-line buffer |
| balonowy-radar | Balloon landing sites | Wind-trajectory landing ellipses |

**Recommendation:** don't submit four change-detection projects. Pick ŚLAD as the submission. Mention in the business slide that the engine generalises to rail and linear infrastructure, and present that as TAM expansion, not as separate products.

**Against existing services:** the Copernicus Security Service border surveillance component (through Frontex and EUROSUR) delivers **on-request VHR imagery and analyst reports**. It is high quality but expensive, tasked, and episodic. ŚLAD is **continuous, automated, free-data, and priced per kilometre**, and it **cues** VHR tasking rather than competing with it. A ŚLAD lead becomes the justification for a Frontex/SatCen VHR request.

---

## 4. Target Buyer & Business Model

### Primary buyers (B2G)

1. **Straż Graniczna (Polish Border Guard)**, specifically the Podlaski regional unit (PL–BY border) and the Nadbużański unit (Bug river, PL–BY/PL–UA), with procurement funded through:
   - **Tarcza Wschód / East Shield** (about PLN 10 bn, 2024–2028), which explicitly covers surveillance and situational awareness.
   - The **EU Border Management and Visa Instrument (BMVI)**, which co-finances member-state border surveillance capability.
2. **Other EU eastern-frontier border guards** facing the same pattern: Lithuania (VSAT, ~680 km LT–BY), Latvia (VRS), Estonia (PPA), and Finland (Rajavartiolaitos, ~1,340 km with Russia, border closed since 2023).
3. **Frontex / EUROSUR Fusion Services** as an aggregator or reseller of leads across member states.
4. **Secondary:** National Revenue Administration / Customs (KAS) for cigarette and excise smuggling corridors.

### Why they need it in 2026

- **The barrier displaced the problem rather than ending it.** The steel barrier with its electronic perimeter covers the line itself. Crossings move into the hinterland (staging and pickup), to sections without the electronic layer (the Bug river and wetlands), and to neighbouring states. Cameras watch the line. Nothing watches 15 km deep at scale.
- **Satellites see the far side.** Sentinel-1 sees activity on the far side of the border (new clearings, vehicle concentrations, staging areas) with no overflight and no sovereignty problem.
- **Patrol hours are the scarce resource.** A weekly prioritised queue that cuts wasted patrols is an operations-budget argument, not a "nice map" argument.

### Revenue model

| Tier | Price (indicative) | Content |
|---|---|---|
| **Pilot** | €60–90k fixed, 6 months, one sector (~50–80 km) | Calibration with Border Guard feedback, precision measured against patrol outcomes |
| **Operational SaaS** | **€500–900 per border-km per year** | Continuous leads, TAK/KML/API integration, OSNMA field app |
| **Premium** | +€150–250k/year | On-premise / air-gapped deployment, classified-network integration, VHR cueing workflow |

**Sizing:** Poland's eastern land border (BY + UA + RU, about 1,160 km) comes to roughly **€0.6–1.0M ARR** at full rollout. Adding the Baltic states and Finland (about 3,000 km more) brings the EU eastern frontier to roughly **€2.5–4M ARR**. That is modest but real, and the same engine extends to rail, pipelines and power lines (the TorGuard/CorridorGuard markets).

**Go-to-market reality:** direct Polish public procurement is slow. The credible path is to **partner with an incumbent integrator** that already holds Border Guard surveillance contracts, plus non-dilutive bridges: ESA BASS / InCubed, the EUSPA and CASSINI acceleration track, and defence-innovation calls such as NATO DIANA.

**Cost base:** data is free (CDSE). Compute is CDSE openEO credits plus a small cloud VM for SNAP coherence. Marginal cost per border-km is low, so gross margin is above 80% once calibration per sector is done.

---

## 5. 48-Hour Prototype Scope

**Demo AOI:** one 30–40 km PL–BY segment covering a forest-edge zone and a stretch of the barrier, for example the Białowieża / Dubicze Cerkiewne area, which gives you forest, barrier strip, open fields and roads all in one AOI. Date range: the last ~8 weeks, which is about 8–10 pairs per orbit direction.

### Team split (5–6 people)

| Role | Deliverable by Sunday 15:00 CET |
|---|---|
| **SAR engineer** | openEO S-1 GRD σ⁰ stacks (asc + desc), log-ratio, land-cover-stratified z-scores, persistence accumulator. **Stretch:** SNAP coherence for 3–4 SLC pairs on the AOI. |
| **Geo-analyst** | Cost surface and least-cost corridors (`scikit-image` `MCP` or `networkx` on the grid), corridor centrality per cell, suppression masks (BDL, OSM, HRL, ERA5 freeze flags) |
| **Backend** | FastAPI: `POST /segment` (polygon + dates) → job → `GET /leads` (GeoJSON) + `GET /leads/{id}/report` (PDF) + webhook + **CoT XML export** |
| **Frontend** | **Lead queue first** (ranked table, type, confidence, before/after chips, σ⁰/γ time series per lead). The map is secondary, opened only from a lead. |
| **Field-loop dev** | Minimal mobile/web form: confirm or reject a lead → OSNMAlib status (live with an F9P if available, otherwise replayed test vectors) → hashed evidence record → label stored |
| **Pitch/business** (can be shared) | Deck, the buyer story, a mock Border Guard weekly briefing built from the output |

### Timeline

- **Fri evening:** define the AOI, submit openEO batch jobs early (queues get congested at hackathons), start SLC downloads, fetch the BDL, OSM and ERA5 layers. **All code is written from scratch this weekend.** Only public libraries and data are used.
- **Sat:** scoring pipeline end-to-end on cached stacks. Corridor model. API. Lead-queue UI. First lead list by Saturday 18:00. Saturday night goes to false-positive triage: look at the top 30 leads by hand and tune the suppression rules.
- **Sun morning:** reports, CoT export, OSNMA loop, freeze-time features, rehearsal.

### Live demo script (4 minutes)

1. Draw a new segment, or select one of three prepared ones, and pick a date range. A small-AOI openEO job runs live, with a cached fallback for the full segment.
2. Show the **funnel** with numbers: "8,400 cells changed → 1,100 after weather normalisation → 310 after farm/forest/construction suppression → 42 persistent → **9 on corridors**." This one slide answers "isn't this just change detection?"
3. Open lead #1 (forest-edge exit near a road): σ⁰/γ time series showing repeated drops, the corridor overlay, and the S-2 chip if a clear scene exists.
4. Export to TAK (CoT shows up in an ATAK or WinTAK client if a team member has one) and send the webhook.
5. Field confirmation with the OSNMA-authenticated stamp. The label feeds back and the score recalibrates.

### Validation you can honestly show

- **Sanity:** the pipeline must flag the 2022 barrier construction strip as massive change when run on 2022 dates, and must **suppress** it in 2026 runs through the construction mask.
- **Suppression ablation:** the count of leads with and without each context layer, which shows how much each one removes.
- **Weak correlation:** weekly lead count per Border Guard sector against the publicly reported attempt counts. Present it as exploratory, never as accuracy.

---

## 6. Biggest Risk & Likely Jury Pushback

**1. "C-band at 10–20 m can't see a footpath. This is physically impossible." (IGiK, Blue Dot)**
→ *Defence:* agree immediately, then reframe. "Correct. We don't detect paths. We detect **repeated coherence loss on eligible open-terrain cells** (γ_ref > 0.3) that lie on modelled corridors. We exclude forest from the coherence term because volume decorrelation makes C-band coherence meaningless under canopy. Our lead types are forest-edge exits, barrier-strip disturbance and hinterland staging, all at the 50 m cell scale." Showing that you know the physical limits wins more points than overclaiming.

**2. "Your false-positive rate will be enormous: ploughing, logging, freeze–thaw, wild boar, East Shield construction."**
→ *Defence:* this is the strongest part of the design, so lead with the funnel slide. Same-class z-scoring removes regional weather effects. ERA5 soil-temperature flags remove freeze–thaw pairs. BDL and OSM masks remove logging and construction. The persistence requirement removes one-off agricultural events. Be honest about wildlife and legitimate local traffic: those survive the filters, and that is why the output is a **lead for a human**, not an alert. The field feedback loop measures precision per sector over time.

**3. "6-day revisit. Crossings happen in hours. Operationally useless." (Cyber Defense Forces / military jury)**
→ *Defence:* ŚLAD is **pattern intelligence for patrol planning and sensor placement** on a weekly cycle, not real-time interdiction. Persistent corridors last weeks, because smuggling networks reuse routes. Its job is to tell commanders where to put the mobile thermal camera next week.

**4. "The Border Guard already has towers, cameras and the electronic barrier."**
→ *Defence:* those cover the **line**. ŚLAD covers **depth** (15 km hinterland), **gaps** (Bug river, wetlands, sections without the electronic layer), the **far side**, and **other countries' borders** that lack Poland's barrier investment. It also cues expensive VHR tasking.

**5. Ethics: "Pushbacks, humanitarian deaths in the forest. Are you building a tool for human-rights violations?"**
→ *Defence:* take this head-on, because a "Space for Peace" jury may raise it.
- At 10 m resolution the system **cannot identify individuals**, and it processes no personal data.
- Every lead and action is written to an audit log.
- The same lead workflow supports **search-and-rescue**. People stranded on forest-edge corridors in winter face hypothermia risk, and a persistent-use corridor is exactly where a rescue patrol should go.
- The governance slide states: lawful-use clauses in the licence, audit logging, and no integration with automated enforcement.

**6. "Coherence from SLC in 48 hours? Show me." (technical judges)**
→ *Mitigation:* GRD backscatter through openEO is the **guaranteed** path. SNAP coherence is the stretch goal, scoped to 3–4 pairs on one AOI. If coherence fails, the pipeline still runs on σ⁰ persistence, and the deck says so honestly.

**7. ChipCraft-style GNSS scrutiny: "What exactly does OSNMA prove?"**
→ *Defence:* precise wording. OSNMA authenticates the **navigation message** of Galileo satellites. It detects spoofed navigation data but does not prevent jamming, and it does not by itself prove position against every attack (relay/meaconing remains a residual risk). We log authentication status as **evidence metadata**, not as proof of location. If you have no receiver, say the demo uses replayed vectors.

---

## 7. Hackathon Fit Verdict

| Criterion (33% each) | Score | Rationale |
|---|---|---|
| **Relevance** | **8.5 / 10** | Clean fit for Challenge 3 (smuggling and hybrid threats on the EU external border). Uses Copernicus heavily (S-1 GRD + SLC, S-2, HRL, ERA5 from C3S) and Galileo OSNMA in a meaningful but secondary role. Strong local resonance in Warsaw given East Shield and the PL–BY situation. |
| **Innovation & Business Viability** | **7 / 10** | The persistence + corridor prior + suppression funnel, the TAK tasking output, and the OSNMA evidence loop clearly lift it above "change map." The buyer is real and funded (Border Guard, BMVI, East Shield), but government procurement is slow and the market is niche (about €2.5–4M ARR across the EU eastern frontier). The extension to rail and linear infrastructure lifts it. Points are lost because it still belongs to the most crowded family of concepts. |
| **Execution / Feasibility** | **7.5 / 10** | The GRD path through openEO plus the corridor model plus the lead queue is very achievable in 48 h. Coherence and live OSNMA are stretch goals. Main execution risks are openEO queue congestion (mitigation: submit jobs Friday night, cache the full segment, keep the live AOI small) and November cloud cover (S-2 is already optional). |
| **Weighted total** | **≈ 7.7 / 10** | |

### Fresh Code Rule risk: **Low, with one caveat**
- All pipeline, scoring, corridor, API and UI code must be written Friday through Sunday. Open libraries (openEO client, SNAP, pyroSAR, OSNMAlib, scikit-image, FastAPI, H3) and public data are fine.
- **Caveat:** if any code from TorGuard, CorridorGuard or balonowy-radar already exists from earlier work, **do not reuse it**. Rebuild the shared change engine from scratch this weekend and keep git history that shows it.
- Pre-downloading data before Friday is a grey area. Do downloads after the official start.

### Anti-saturation risk: **Medium. Manage it actively.**
- ŚLAD sits in the same family as the most saturated cliché, change detection on Sentinel imagery. One map-first slide and the jury will file it under "Nobody is waiting for your map."
- **Rules for the pitch:**
  - Open with the **Border Guard analyst's weekly patrol-planning problem**.
  - Show the **suppression funnel numbers** before any imagery.
  - Make the **lead queue and TAK export** the hero screen.
  - Say "we don't detect footpaths" before a judge can.
- Submit **one** change-detection project from the idea pool, not four.

### Verdict: **GO**

Conditions:
1. SAR-first, with GRD persistence as the guaranteed core.
2. Corridor model plus context suppression as the differentiators.
3. Lead-queue and tasking output as the hero of the demo.
4. OSNMA field loop as a credible bonus, with precise wording.
5. Ethics and search-and-rescue framing prepared before the first jury question.
