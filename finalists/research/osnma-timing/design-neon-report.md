# 12th CASSINI Hackathon (Warsaw, Poland): Detailed Idea Research & Evaluation Report

* **Event:** 12th CASSINI Hackathon — *EU Space for Peace and Resilience*
* **Dates & Location:** November 27–29, 2026 | Warsaw, Poland (Local Organizer: Blue Dot Solutions)
* **Hard Submission Deadline:** Sunday, November 29, 2026 at 15:00 CET (Local Pitches start 15:05 CET; European Demo Day on December 2, 2026)

---

## 1. 2026 Strategic Context: What Actually Moves the Needle in Warsaw

To win both the **Local Warsaw Finals** (PLN 7,500 + European Demo Day slot) and the **European Demo Day** (€5,000 + 100 hours of CASSINI mentoring), an idea must simultaneously satisfy three realities unique to **November 2026**:

### A. Fresh 2026 Polish & EU Regulatory Catalysts (Budget Unlockers)
Judges penalize "nice-to-have" civic tools with no buyer urgency. In late 2026, four concrete legal and financial pressures are actively forcing Polish and EU institutions to spend money:
1. **Poland's NIS2 Implementation (KSC Act Amendment — Dz. U. 2026 poz. 252):** Entered into force on **April 3, 2026**, expanding cybersecurity mandates to roughly **38,000 essential and important entities** in Poland. Self-registration in the **S46 System** (`wykaz-ksc.gov.pl`) closed on October 3, 2026, and entities face a hard **April 3, 2027** compliance cliff. Crucially, entities must submit an **Early Warning within 24 hours** and a **Significant Incident Report within 72 hours** to their sectoral CSIRT.
2. **Poland's CER Directive Implementation (UZK Amendment):** Signed June 19, 2026 and in force since **July 4, 2026**, requiring designated critical entities (*podmioty krytyczne*) to conduct biennial all-hazards risk assessments covering **antagonistic threats (sabotage)**, extreme weather, and operational continuity.
3. **EU Smart Tachograph v2 OSNMA Mandate:** Since **December 2025**, every newly registered heavy truck and bus in the EU is legally required to carry a second-generation smart tachograph supporting **Galileo OSNMA**—meaning authenticated PNT hardware is already rolling out across European logistics fleets at zero hardware cost to software startups.
4. **Poland's Illegal Hazardous Waste Crisis (Nov 23, 2026 Announcement):** Just days before the hackathon, Poland's Climate Ministry (MKiŚ) confirmed a **PLN 1.1 billion** budget (2025–2027) to clear illegal hazardous waste dumps (29,000 tonnes cleared across 17 sites so far), alongside long-term financing plans for the **BDO** waste registry.

### B. 2026 EU Space Infrastructure Milestones
* **Galileo OSNMA (Operational since July 2025; Public Key ID 2 active since Dec 10, 2025):** First operational civilian GNSS authentication service globally. Supported by mature open-source Python tooling (`OSNMAlib`, with live **Galmon** P2P stream integration—enabling a live 48-hour demo without physical RF hardware), with **Galileo Signal Authentication Service (SAS)** entering live L3 signal testing in 2026 (`SASlib`).
* **Copernicus Sentinel-1C & Sentinel-2C (Operational on CDSE/openEO):** Following the May 2026 Sentinel-1 orbital reconfiguration, Europe has restored its **6-day SAR revisit cadence** (all-weather, day/night), paired with rapid optical revisit via Sentinel-2A/2B/2C and streamlined serverless processing via **CDSE / openEO**.
* **Local GNSS Interference Baseline:** Since May 2026, Blue Dot Solutions' own Gdańsk monitoring station has documented GNSS jamming across Pomerania and the southern Baltic on roughly **two-thirds of days**—making generic "jamming detection maps" redundant, while making *downstream digital mitigation and compliance* urgently relevant.

### C. Webinar Saturation & Anti-Cliché Filter
Based on Poland's Nov 5 webinar (GNSS jamming/spoofing for borders & critical infrastructure) and central European webinars (openEO, APEx, AI for Resilience, and Ukraine's *"Nobody Is Waiting for Your Map"* session), ideas were strictly filtered out if they resembled:
* Generic GNSS jamming/spoofing heatmaps.
* Static Sentinel-2 change-detection or post-disaster damage dashboards with no downstream API/workflow.
* Standard AIS + SAR "dark vessel" maritime trackers.
* Vague "AI crisis management platforms" lacking a clear buyer.

---

## 2. Weighted Scoring Matrix (Evaluated Against Official Rubric)

Each candidate is scored out of 10 across the three official equally weighted criteria (**Relevance 33%**, **Innovativeness & Business Viability 33%**, **Execution & 48h Prototype Feasibility 33%**) plus an **Anti-Saturation / Warsaw Jury Fit** modifier.

| Rank | Idea Name | Official Track | Relevance (33%) | Innovation & Biz (33%) | 48h Execution (33%) | Saturation Risk | Composite Score | Best Jury Appeal |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **ChronoShield** | Challenge 1 (Cybersecurity) | 9.8 | 9.4 | 9.2 | **Low** | **9.47 / 10** | ChipCraft, Cyber Defense Forces, WAT, Blue Dot Solutions |
| **2** | **ProofOfRoute** | Challenge 3 (Transnational Crime) | 9.4 | 9.7 | 9.0 | **Very Low** | **9.37 / 10** | European Demo Day Jury, ABGi, InsurTech/Logistics VCs |
| **3** | **EcoForensic** | Challenge 3 (Transnational Crime) | 9.3 | 9.2 | 9.5 | **Very Low** | **9.33 / 10** | Polish Public-Sector Judges, IGiK, CDSE/EO Mentors |
| **4** | **CorridorGuard** | Challenge 2 (Civil Resilience) | 9.5 | 8.9 | 9.1 | **Low–Med** | **9.17 / 10** | Scanway, IGiK, Energy/Rail Defense Mentors |
| **5** | **BlackoutBridge** | Challenge 2 (Civil Resilience) | 9.2 | 8.6 | 8.5 | **Medium** | **8.77 / 10** | Civil Defense, Product/UX Judges, Crisis Responders |

---

## 3. Ultra-Detailed Candidate Deep Dives

---

### Candidate #1: ChronoShield — PNT Firewall & Automated KSC/NIS2 24-Hour Incident Reporter

#### 1. Strategic Overview & Pitch
* **Challenge Track:** Challenge 1 — Cybersecurity for space-based strategic enablers.
* **One-Line Pitch:** A software-defined PNT (Positioning, Navigation, and Timing) security agent that uses **Galileo OSNMA** and cross-clock anomaly detection to shield critical infrastructure from GNSS timing spoofing, trigger automated oscillator holdover, and auto-file legally compliant **24-hour KSC/NIS2 Early Warning reports** to Polish/EU sectoral CSIRTs.
* **The Core Insight:** Critical infrastructure doesn't just use satellites for location—**5G TDD base stations** ($\pm 1.5\ \mu\text{s}$ phase sync), **power grid synchrophasors/PMUs** ($\pm 1\ \mu\text{s}$), and **MiFID II financial trading clocks** ($\pm 100\ \mu\text{s}$) rely on GNSS for *precision time*. A subtle spoofing attack that drifts a substation's or telecom tower's clock by milliseconds can cascade into blackouts or dropped cellular networks—while simultaneously creating a severe legal violation under Poland's 2026 NIS2 law if unreported within 24 hours.

#### 2. 2026 Market & Regulatory Catalyst
* **The Compliance Cliff:** Poland's KSC Act amendment (**Dz. U. 2026 poz. 252**, effective April 3, 2026) brings **~38,000 Polish entities** under mandatory cybersecurity supervision, with a **April 3, 2027** deadline to operationalize ISMS and **S46 System** reporting workflows.
* **Why CISOs Care Now:** Telecom, energy, and banking CISOs have dozens of IT firewalls (SIEM/SOAR), but **zero visibility into their RF/GNSS timing layer**—and no automated bridge from a GNSS receiver anomaly to a sectoral CSIRT 24-hour Early Warning dossier.
* **Direct Alignment with Blue Dot Solutions:** In 2026, Blue Dot Solutions highlighted that simply plotting RF jamming in Pomerania is only step one—the real operational challenge is connecting GNSS interference events to failures inside digital systems.

#### 3. Exact EU Space Data Pipeline & Technical Architecture
```text
[Galileo E1-B I/NAV Stream / Galmon P2P / Local u-blox Receiver]
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│ 1. Cryptographic Layer (OSNMAlib - Python)               │
│    - Validates DSM-PKR (Public Key ID 2) & Merkle Root   │
│    - Verifies TESLA KROOT & MACSEQ/MACLT tags            │
│    - Flags forged ephemeris / nav-message spoofing       │
└─────────────────────────┬────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│ 2. Anti-Meaconing & Clock Residual Engine                │
│    - Computes offset Δt = |t_Galileo - t_PTP/NTP_ref|    │
│    - Monitors C/N0 jumps, clock bias rate (dΔt/dt),      │
│      and Galileo vs. EGNOS/GPS inter-system residuals    │
│    - Outputs real-time PNT Trust Score S_PNT ∈ [0, 100]  │
└─────────────────────────┬────────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌─────────────────────────┐     ┌──────────────────────────┐
│ 3A. Automated Mitigation│     │ 3B. NIS2 / S46 Compliance│
│ - Fires REST/SNMP hook  │     │ - Packages signed IoCs,  │
│ - Locks node into local │     │   drift plots, OSNMA fail│
│   OCXO/Rubidium holdover│     │   logs into S46 JSON/PDF │
│ - Alerts NOC / SIEM     │     │   24h Early Warning Pack │
└─────────────────────────┘     └──────────────────────────┘
```
* **EU Space Signals Used:**
  * **Galileo E1-B I/NAV with OSNMA:** Cryptographically verifies the authenticity of Galileo navigation messages and satellite clock correction parameters using the TESLA protocol.
  * **EGNOS / Multi-Constellation Residuals:** Cross-checks Galileo time solutions against EGNOS integrity messages and local network PTP (IEEE 1588) / authenticated NTS-NTP servers to detect **meaconing** (record-and-replay attacks that preserve valid OSNMA bits but introduce propagation delay $\Delta t$).
* **Decision Logic:**
  * Computes a weighted **PNT Trust Score** $S_{\text{PNT}} \in [0, 100]$ based on:
    1. OSNMA cryptographic authentication status (binary gate: `VERIFIED` vs `FAILED`).
    2. Clock drift magnitude $|\Delta t|$ against sector SLA threshold $\tau_{\text{sector}}$ ($1.5\ \mu\text{s}$ Telecom 5G, $1.0\ \mu\text{s}$ Power PMU, $100\ \mu\text{s}$ Finance MiFID II).
    3. Rate-of-change spike $|\frac{d\Delta t}{dt}|$ and sudden $C/N_0$ carrier-to-noise anomalies.
  * When $S_{\text{PNT}} < 60$ for $> 5\text{ s}$, ChronoShield automatically fires a webhook/SNMP trap placing the timing server into **Local Holdover Mode** and initiates the **24-hour NIS2 countdown timer**, pre-filling all technical Indicators of Compromise (IoCs) required by Poland's S46 reporting schema.

#### 4. Anti-Saturation & Competitive Differentiation
* **Why It Beats Webinar Clones:** Competing teams will build map-based RF jamming trackers (duplicating Blue Dot Solutions' Gdańsk station and GPSJam.org). ChronoShield operates **inside the enterprise security stack (SIEM/SOAR + NTP/PTP timing daemons)** as a middleware firewall and compliance automation engine.
* **Commercial Differentiation:** Hardware anti-jamming antennas (CRPA) cost €20,000–€100,000+ per site and require physical tower climbs. ChronoShield deploys as a lightweight software daemon alongside existing OSNMA-capable timing receivers or edge gateways at $< 5\%$ of hardware retrofit costs.

#### 5. Target Buyer, GTM Strategy & Business Model
* **Primary Buyers (Poland & EU):**
  * **Energy Grid Operators (DSOs/TSOs):** PSE, Tauron, Energa, Enea (especially substations in northern/eastern Poland experiencing frequent Baltic jamming).
  * **Telecom Operators:** Orange Polska, Play, Plus (Polkomtel), T-Mobile (5G RAN synchronization).
  * **Financial Infrastructure:** Warsaw Stock Exchange (GPW), clearing houses, and Polish banks subject to MiFID II + DORA + NIS2.
* **Pricing Model (B2B SaaS / Edge License):**
  * **Site Agent Tier:** €400 / critical timing node / month (volume discounts for $> 50$ substations or base stations).
  * **Enterprise Compliance Module (S46 / NIS2 / DORA SIEM Connector):** €2,500 / month flat platform fee.
  * **Estimated Polish SAM:** Even capturing $1\%$ of Poland's 38,000 KSC-regulated entities (focusing on top ~350 energy/telecom/finance operators) represents a €4M–€8M ARR beachhead before EU-wide expansion.

#### 6. 48-Hour Prototype Scope & Live Stage Demo Script
* **Tech Stack:** Python (`OSNMAlib` connected to live **Galmon** Galileo feed + pre-recorded official OSNMA test vectors for deterministic demo safety), FastAPI backend, React/Tailwind SOC dashboard, WeasyPrint/ReportLab for signed PDF + S46 JSON export.
* **Build Schedule:**
  * *Friday Night:* Clone `github.com/Algafix/OSNMA`, verify live Galmon feed + offline official test vector playback, design PNT Trust Score state machine and mock PTP/NTP telemetry stream.
  * *Saturday:* Build FastAPI engine with 3 sector profiles (5G Telecom, Power Grid Substation, MiFID II Bank), integrate simulated **Spoofing** (invalid OSNMA MAC) and **Meaconing** (valid OSNMA + $45\ \mu\text{s}$ replay delay) attack injectors, build SIEM/Holdover webhook simulator.
  * *Sunday (by 13:00 CET):* Build the S46 / NIS2 24-hour Early Warning PDF + JSON auto-generator, polish dashboard, rehearse 3-minute demo + Q&A.
* **The Live "Wow Moment" on Stage (90 Seconds):**
  1. Show live Galileo satellites being cryptographically authenticated via `OSNMAlib` (green Trust Score: 99/100) feeding a mock Energa substation in Gdańsk.
  2. Click **"Inject Clock Spoofing / Meaconing Attack"**.
  3. In real time, the Trust Score plunges to 18/100, OSNMA/clock-residual flags turn crimson, the API automatically switches the substation to **"SAFE OCXO HOLDOVER"** (preventing grid desync), and a **pre-filled Polish KSC/NIS2 24-Hour Early Warning Dossier** downloads instantaneously with cryptographic hashes and IoCs.

#### 7. Adversarial Jury Q&A Stress Test
* **Q (ChipCraft / GNSS Hardware Mentor):** *"OSNMA only authenticates the navigation message bits, not the physical ranging code. A sophisticated attacker can record and replay a valid Galileo signal (meaconing) and pass OSNMA checks. How do you stop that?"*
  * **Winning Rebuttal:** *"Exactly right—that's why ChronoShield never relies on OSNMA alone. OSNMA kills forged-message spoofing, while our second layer monitors inter-clock residuals against authenticated network time (NTS/PTP), $C/N_0$ power anomalies, and cross-constellation EGNOS/GPS offsets to catch replay latency. On our 2027 roadmap, we are already architecting support for Galileo's upcoming Signal Authentication Service (SAS)—whose live L3 signals are being validated this year—to add true ranging-level authentication."*
* **Q (Cyber Defense Forces / WAT):** *"What if the attacker jams all GNSS bands completely so there is no signal to authenticate?"*
  * **Winning Rebuttal:** *"Jamming drops $C/N_0$ and locks out navigation frames, which immediately drops our Trust Score below threshold, triggers safe local oscillator holdover, and logs the outage duration and RF degradation telemetry into the NIS2 incident report—giving operators verifiable proof of external interference rather than silent equipment failure."*

---

### Candidate #2: ProofOfRoute — Space-Verified Chain of Custody Against Sanctions Evasion & Cargo Fraud

#### 1. Strategic Overview & Pitch
* **Challenge Track:** Challenge 3 — Countering transnational crime and terrorism with space data.
* **One-Line Pitch:** A B2B compliance and anti-fraud API that fuses **Galileo OSNMA** telemetry (from EU-mandated Smart Tachograph v2 units) with **Copernicus Sentinel-1 SAR** physical verification to detect GPS-spoofed smuggling, EU sanctions evasion ("ghost transit"), and fraudulent cargo insurance claims.
* **The Core Insight:** Since 2022, one of Europe's largest transnational crime vectors is **sanctions evasion via land transit**: EU-manufactured dual-use electronics, machinery, or luxury vehicles are legally declared for export through Poland/Baltics to Central Asia (e.g., Kazakhstan/Kyrgyzstan), but are secretly offloaded in Belarus or Russia while a spoofed GPS tracker fakes normal transit coordinates. Meanwhile, cargo insurers lose billions to staged theft and "phantom route" claims.

#### 2. 2026 Market & Regulatory Catalyst
* **Zero-Hardware Rollout Advantage:** As of **December 2025**, EU Mobility Package regulations mandate **Smart Tachograph v2 with Galileo OSNMA** in all newly registered commercial trucks and buses across the EU. Millions of heavy vehicles are already generating cryptographically signed location records—yet almost nobody is ingesting that proof into customs, export-control, or insurance workflows.
* **Strict Corporate Liability Under EU Sanctions:** European exporters and freight forwarders now face severe criminal and financial liability (under the EU "No-Russia Clause" and harmonized sanctions-violation criminalization) if their dual-use goods divert into sanctioned territories without due diligence.

#### 3. Exact EU Space Data Pipeline & Technical Architecture
```text
[Truck Smart Tachograph v2 / IoT Tracker]    [Bill of Lading / Customs Route Plan]
   (Galileo OSNMA Signed Route Logs)           (Expected Corridor & Border Gates)
                  │                                           │
                  └────────────────────┬──────────────────────┘
                                       ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 1. Cryptographic Route Integrity Engine (Galileo OSNMA Verification)       │
│    - Verifies OSNMA signatures along every waypoint & border crossing      │
│    - Flags "unsigned gaps", impossible velocity jumps, or spoofed GPS      │
│      coordinates where standard GPS ≠ Galileo OSNMA position               │
└──────────────────────────────────────┬─────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 2. Physical Presence Cross-Check (CDSE / openEO — Sentinel-1A/1C SAR)      │
│    - Triggered automatically for high-risk stops, bonded warehouses,       │
│      or suspicious "dark gaps" near eastern EU border crossings            │
│    - Queries Sentinel-1 GRD (VV/VH backscatter σ⁰) over claimed trans-     │
│      shipment yard / parking lot to verify physical convoy presence or     │
│      detect anomalous off-route staging activity in restricted zones       │
└──────────────────────────────────────┬─────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 3. Tamper-Evident Space-Verified Compliance Certificate (REST API + PDF)   │
│    - Outputs PASS / REVIEW / HIGH-RISK FLAG + Fraud Risk Score (0–100)     │
│    - Generates cryptographically hashed Audit PDF for Customs / Insurers   │
└────────────────────────────────────────────────────────────────────────────┘
```
* **EU Space Data & Signals Used:**
  * **Galileo OSNMA:** Cryptographically authenticates vehicle position and timestamp logs from Smart Tachograph v2 / OSNMA IoT seals, preventing driver-installed $50 USB GPS spoofers from fabricating transit histories.
  * **Copernicus Sentinel-1A/1C (SAR GRD via CDSE/openEO):** Provides all-weather, cloud-penetrating backscatter change analysis ($\Delta \sigma^0$ in VV/VH polarization) over key border queues, transshipment hubs, and unauthorized forest/industrial offload zones along EU external borders.
  * **Copernicus Sentinel-2C (Optical RGB/SWIR via CDSE):** Secondary visual corroboration of large logistics yards and border checkpoints when cloud cover is $< 20\%$.

#### 4. Anti-Saturation & Competitive Differentiation
* **Why It Beats Webinar Clones:** 90% of Challenge 3 teams build *"AIS + SAR dark vessel trackers at sea."* ProofOfRoute dominates the vastly underserved **overland & multimodal cross-border smuggling/sanctions-evasion market**—which is far more relevant to Warsaw, Poland's eastern border (Terespol, Koroszczyn, Kuźnica), and EU industrial exporters.
* **Workflow, Not a Map:** The customer does not want to stare at a GIS dashboard. An export compliance officer or insurance claims adjuster wants an API response (`status: FLAGGED_SPOOFING_DETECTED`) and a legally defensible audit certificate attached to a Bill of Lading.

#### 5. Target Buyer, GTM Strategy & Business Model
* **Primary Buyers:**
  * **Dual-Use & High-Tech EU Exporters:** German, Polish, and Dutch industrial manufacturers shipping machinery/electronics to Eastern Europe & Central Asia who need auditable "No-Russia" due diligence.
  * **Marine & Cargo Insurance Underwriters:** Allianz Commercial, PZU, Warta, Lloyd's syndicates (preventing staged-theft fraud and verifying transit clauses).
  * **Customs & Border Authorities (Phase 2 B2G):** Poland's Krajowa Administracja Skarbowa (KAS), Frontex, and EU OLAF (Anti-Fraud Office).
* **Pricing Model:**
  * **Transactional Verification API:** €3–€12 per verified high-risk Bill of Lading / shipment dossier.
  * **Enterprise Compliance SaaS:** €1,500–€5,000 / month for freight forwarders and insurers integrating directly into TMS/ERP systems (SAP, CargoWise).

#### 6. 48-Hour Prototype Scope & Live Stage Demo Script
* **Tech Stack:** Python FastAPI, `OSNMAlib` verification module, `openeo` Python client querying real CDSE Sentinel-1/2 imagery over a real Polish-Belarusian border logistics hub (e.g., Małaszewicze / Koroszczyn), React frontend with interactive shipment verifier & PDF generator.
* **Build Schedule:**
  * *Friday Night:* Create two realistic shipment JSON telemetry traces from Warsaw toward Central Asia via eastern Poland: **Shipment A** (legitimate OSNMA-signed route) and **Shipment B** ("Ghost Transit" where the truck detours to an unauthorized offload depot while feeding spoofed non-OSNMA GPS coordinates).
  * *Saturday:* Connect `OSNMAlib` verification check + real CDSE/openEO Sentinel-1 SAR backscatter lookup for the border transshipment zone; compute unified Fraud Risk Score.
  * *Sunday (by 13:00 CET):* Build the 1-click **"Space-Verified Chain of Custody Certificate"** PDF export and clean API playground showing JSON webhook payloads.
* **The Live "Wow Moment" on Stage:**
  * Upload Shipment B's manifest. Standard GPS tracking shows a clean green line crossing the border on schedule. ProofOfRoute instantly flags **RED (Risk 94/100)**: OSNMA authentication broke for 6 hours 18 km before the border, velocity residuals prove synthetic GPS injection, and Sentinel-1 SAR confirms abnormal heavy-vehicle clustering at an unpermitted staging site—auto-freezing the insurance payout / export clearance.

#### 7. Adversarial Jury Q&A Stress Test
* **Q (Logistics / Business Judge):** *"Smart Tachograph v2 already uses OSNMA, and truckers can just remove the SIM card or turn off the tracker. Why does ProofOfRoute matter?"*
  * **Winning Rebuttal:** *"Removing or jamming a tracker creates a verifiable 'dark gap'—and under ProofOfRoute, a dark gap inside a high-risk border geofence automatically fails compliance verification and triggers Sentinel-1 SAR yard checks. Smart Tachograph v2 solves hardware generation of signed coordinates, but right now that data sits trapped in roadside police readers. We unlock it as a real-time B2B API for exporters and insurers."*
* **Q (IGiK / Remote Sensing Judge):** *"Sentinel-1 has a 6-day revisit and 10-meter resolution—you can't track a single truck moving down a highway with SAR!"*
  * **Winning Rebuttal:** *"Correct—we never claim to track individual moving trucks from SAR. Galileo OSNMA handles continuous per-second truck tracking; Sentinel-1 SAR is used specifically to monitor stationary transshipment hotspots, border queues, and illegal offload yards over time to identify systematic smuggling hubs and corroborate multi-hour stops."*

---

### Candidate #3: EcoForensic — Prosecution-Ready Space Evidence Against Transnational Waste Crime

#### 1. Strategic Overview & Pitch
* **Challenge Track:** Challenge 3 — Countering transnational crime and terrorism with space data.
* **One-Line Pitch:** An automated environmental forensics platform that fuses **Sentinel-1 (SAR)**, **Sentinel-2 (Optical)**, and **Sentinel-3 (Thermal)** time-series data with Poland's **BDO waste registry** to detect illegal cross-border hazardous waste dumps, predict deliberate landfill arson, and generate court-admissible **Prosecution Evidence Dossiers**.
* **The Core Insight:** Europol classifies **transnational illegal waste trafficking** as one of Europe's fastest-growing organized crime sectors. Criminal syndicates truck toxic chemical waste illegally across borders (often from Western Europe into Poland), lease abandoned quarries or industrial yards under shell companies, dump thousands of tonnes of barrels in weeks, and then **set the dumps on fire** to destroy forensic evidence—leaving Polish municipalities stuck with tens of millions of PLN in cleanup bills.

#### 2. 2026 Market & Regulatory Catalyst
* **Breaking Polish News Hook (Literally 4 Days Before the Hackathon!):** On **November 23, 2026**, Poland's Climate Minister announced a **PLN 1.1 billion** national program (2025–2027) to clear illegal hazardous waste sites (29,000 tonnes already removed across 17 sites), alongside long-term funding for the **BDO (Baza danych o produktach i opakowaniach oraz o gospodarce odpadami)** registry.
* **The Legal Bottleneck:** Under Polish law, to force the criminal syndicate (or site lessee/landowner) to pay cleanup costs—rather than taxpayers—prosecutors and **GIOŚ/WIOŚ** (Environmental Inspectorates) must establish **exact dumping timelines** (proving *when* the waste arrived so shell companies cannot blame a previous tenant). Continuous Copernicus archives provide an immutable, timestamped orbital witness going back years.

#### 3. Exact EU Space Data Pipeline & Technical Architecture
```text
[AOI: Abandoned Industrial Parks, Quarries, Border Logistics Zones]
                                 │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ Sentinel-1A/1C SAR│  │ Sentinel-2A/2B/2C │  │ Sentinel-3 SLSTR  │
│ (CDSE / openEO)   │  │ (CDSE / openEO)   │  │ (Thermal IR)      │
│ - Coherence loss  │  │ - Bare soil /     │  │ - Land Surface    │
│   & backscatter   │  │   plastic / scrap │  │   Temperature     │
│   change (Δσ⁰)    │  │   spectral index  │  │   (LST) anomaly   │
│ - Detects dumping │  │ - New truck tire  │  │ - Early arson /   │
│   under clouds    │  │   tracks & mounds │  │   heating alert   │
└─────────┬─────────┘  └─────────┬─────────┘  └─────────┬─────────┘
          └──────────────────────┼──────────────────────┘
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. Automated BDO Permit & Land Registry Cross-Check Engine      │
│    - Intersects detected anomaly polygons with official BDO     │
│      permitted waste-storage parcels & active construction zones│
│    - Filters out legal landfills & licensed quarries            │
│    - Estimates dumped area (m²), growth rate, & cleanup cost    │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. Court-Admissible Forensic Evidence Pack (PDF + GeoPackage)   │
│    - Chronological before/during/after Sentinel strip + timestamps│
│    - SHA-256 hash of raw CDSE scene IDs (chain of custody)      │
│    - Arson Risk Score & 1-click dispatch to WIOŚ / Police       │
└─────────────────────────────────────────────────────────────────┘
```
* **EU Space Data & Signals Used:**
  * **Copernicus Sentinel-1A/1C (SAR GRD/SLC via openEO):** Detects rapid surface roughness increases, mound formation, and coherence drops ($\Delta \gamma$) inside peri-urban industrial plots—even at night or under winter cloud cover.
  * **Copernicus Sentinel-2A/2B/2C (Multispectral 10 m–20 m via openEO):** Computes Hydrocarbon/Plastic/Disturbed-Ground spectral ratios (SWIR bands B11/B12 vs. NIR/Red) and flags sudden disappearance of vegetation or emergence of unsorted waste piles and heavy-truck access tracks.
  * **Copernicus Sentinel-3 SLSTR (Thermal Infrared):** Monitors Land Surface Temperature (LST) anomalies over flagged unpermitted sites to catch exothermic chemical decomposition or pre-arson hotspots *before* toxic smoke plumes engulf nearby towns.
  * **Galileo OSNMA (Mobile Inspector Companion — Bonus Integration):** When a WIOŚ inspector visits the flagged site to collect soil samples, our lightweight mobile capture tool stamps their ground photos with Galileo-authenticated coordinates so defense lawyers cannot challenge photo authenticity in court.

#### 4. Anti-Saturation & Competitive Differentiation
* **Zero Duplication Risk:** At a "Peace & Resilience" hackathon, almost no other team will think of transnational environmental organized crime—yet it is a **core Europol priority**, fits Challenge 3 seamlessly, uses **three Sentinel constellations**, and hits an active **PLN 1.1 billion Polish government headline** from this exact week.
* **Why Judges Love It:** Unlike static maps, EcoForensic outputs a **financial and legal weapon**: an immutable timeline with SHA-256 scene provenance that shifts millions of PLN in remediation liability off municipal taxpayers and onto perpetrators.

#### 5. Target Buyer, GTM Strategy & Business Model
* **Primary Buyers:**
  * **Polish Environmental Inspectorates & Ministries:** GIOŚ, 16 regional WIOŚ offices, Ministry of Climate and Environment (MKiŚ).
  * **Municipalities (*Gminy*) & Regional Authorities:** Currently bearing massive cleanup liabilities when dumps go undetected until abandoned.
  * **Environmental Liability Insurers & Industrial Landlords:** Real-estate owners leasing warehouses/yards who face bankruptcy if a shell-company tenant secretly fills their lot with toxic barrels.
* **Pricing Model:**
  * **Municipal / Voivodeship Monitoring SaaS:** €1,500–€3,500 / month per region (scanning thousands of high-risk parcels automatically every 6 days).
  * **Industrial Landlord Shield (B2B):** €150 / site / month for real-estate funds and logistics park owners to monitor leased yards for unauthorized dumping.
  * **Forensic Dossier Fee:** €500 per certified historical timeline report for prosecutors/insurers.

#### 6. 48-Hour Prototype Scope & Live Stage Demo Script
* **Tech Stack:** Python + `openeo` (CDSE free tier), real Sentinel-1 & Sentinel-2 historical archive over 1–2 real documented Polish illegal waste dump / landfill fire locations (e.g., Zielona Góra / Zgierz / Mazowieckie historical sites), GeoPandas parcel cross-check against a mock BDO permitted-sites GeoJSON layer, Streamlit or React dashboard + automated Forensic PDF generator.
* **Build Schedule:**
  * *Friday Night:* Select 2 real historical Polish illegal dump sites with clear before/after Sentinel-2 + Sentinel-1 signatures on CDSE; verify openEO script pulls real imagery cleanly.
  * *Saturday:* Build automated change-detection pipeline (SAR backscatter + SWIR/NDVI anomaly score) + BDO permit exclusion filter + thermal risk indicator + estimated cleanup cost calculator (based on Polish average hazardous waste remediation cost of ~PLN 5,000–10,000/tonne).
  * *Sunday (by 13:00 CET):* Build the 1-click **"Prosecution-Ready Forensic Dossier (PDF)"** containing dated CDSE Sentinel thumbnails, SHA-256 product ID hashes, timeline chart showing exact start week of illegal dumping, and estimated taxpayer liability saved.
* **The Live "Wow Moment" on Stage:**
  * Open with: *"Four days ago, Poland confirmed we are spending PLN 1.1 billion cleaning up illegal hazardous waste dumps—because we only find them after criminals vanish or burn them down."*
  * Run a live CDSE/openEO query over a real Polish site: show the exact month illegal dumping started, show the BDO registry returning `NO ACTIVE PERMIT`, flag the thermal anomaly, and generate a court-ready Forensic PDF with SHA-256 CDSE scene hashes in 3 seconds.

#### 7. Adversarial Jury Q&A Stress Test
* **Q (IGiK / Remote Sensing Judge):** *"At 10-meter Sentinel-2 resolution, how do you distinguish illegal toxic barrels from a completely legal pile of construction gravel or timber?"*
  * **Winning Rebuttal:** *"We explicitly do not claim to perform chemical spectroscopy from orbit. EcoForensic detects **unpermitted, rapid-onset industrial dumping and land-use violation** by fusing Sentinel-1/2 change signatures with the BDO permit registry and construction-permit layers. Our job is to shrink 10,000 abandoned parcels down to the top 15 high-probability illegal sites so understaffed WIOŚ inspectors know exactly where to send a field team or drone before the dump grows from 20 tonnes to 5,000 tonnes—and to lock in the exact timeline for prosecution."*
* **Q (Challenge Fit Judge):** *"Is waste dumping really 'transnational crime and terrorism'?"*
  * **Winning Rebuttal:** *"Yes—Europol's SOCTA explicitly lists transnational waste trafficking as a tier-1 organized crime threat in the EU, generating billions in illicit proceeds that cross intra-EU borders directly into Poland, and deliberate toxic-dump arson poses an acute civil-resilience and CBRN-adjacent public health threat."*

---

### Candidate #4: CorridorGuard — Automated Hybrid-Sabotage & Pre-Failure Triage for Linear Infrastructure

#### 1. Strategic Overview & Pitch
* **Challenge Track:** Challenge 2 — Space-enabled crisis response and civil resilience.
* **One-Line Pitch:** An API-first preventive monitoring platform that fuses **Sentinel-1A/1C SAR interferometric coherence** and **Sentinel-2C** multispectral indices to detect unauthorized excavation, heavy machinery intrusion, soil moisture leaks, or embankment subsidence along thousands of kilometers of pipelines, railways, and flood levees—automatically pushing prioritized inspection work orders into operator SCADA/ERP systems.
* **The Core Insight:** Poland and Central Europe maintain tens of thousands of kilometers of exposed linear infrastructure—oil/gas pipelines (PERN, GAZ-SYSTEM), strategic NATO-corridor rail lines (PKP PLK), and river flood levees (Wody Polskie). Physical guarding or daily helicopter/drone patrols across the entire network are financially impossible, leaving networks exposed to both **hybrid sabotage** (unauthorized digging/tampering) and **pre-disaster structural failure** (levee piping/seepage before floods).

#### 2. 2026 Market & Regulatory Catalyst
* **Poland CER Directive Law (UZK Amendment — Effective July 4, 2026):** Legally compels designated critical entities in Poland to conduct continuous all-hazards risk assessments covering **antagonistic sabotage**, natural hazards, and preventive operational resilience.
* **Restored 6-Day SAR Cadence (May 2026):** With Sentinel-1C fully operational alongside Sentinel-1A, all-weather SAR monitoring of linear corridors across Poland is twice as fast as during the 2022–2025 Sentinel-1B gap.

#### 3. Exact EU Space Data Pipeline & Technical Architecture
```text
[Operator Corridor GeoJSON (200m Buffer around Pipeline / Rail / Levee)]
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│ 1. Serverless CDSE / openEO Continuous Triage Pipeline                │
│    - Sentinel-1A/1C (6-day): Computes SAR backscatter ratio (Δσ⁰)     │
│      & coherence drop (Δγ) to catch trenching, heavy vehicles,        │
│      and ground deformation through clouds/darkness                   │
│    - Sentinel-2C (5-day): Computes NDWI (water/leak seepage along     │
│      levees/pipelines) & BSI (Bare Soil Index for fresh excavation)   │
└─────────────────────────────────┬─────────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│ 2. False-Positive Suppression Filter (The Secret Sauce)               │
│    - Masks out active agricultural fields (ESA WorldCereal / LPIS)    │
│      so routine autumn plowing / tractors don't trigger alerts        │
│    - Cross-checks operator's "Permitted Maintenance Schedule" API     │
└─────────────────────────────────┬─────────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│ 3. Automated SCADA / ERP / Drone-Tasking Dispatch                     │
│    - Fires webhook to SAP PM / Jira / Slack with Severity Score       │
│    - Auto-generates KML/MAVLink drone-inspection flight box OR        │
│      high-res commercial satellite tasking request (e.g., Scanway!)   │
└───────────────────────────────────────────────────────────────────────┘
```
* **EU Space Data & Signals Used:**
  * **Sentinel-1A/1C (SAR via CDSE/openEO):** Detects mechanical ground disturbance, unauthorized trenching, and embankment subsidence regardless of weather.
  * **Sentinel-2C (Optical via CDSE/openEO):** Computes Normalized Difference Water Index ($\text{NDWI} = \frac{\text{B03} - \text{B08}}{\text{B03} + \text{B08}}$) to spot underground pipeline leaks or levee water seepage, and Bare Soil Index (BSI) for excavation verification.
  * **ESA WorldCereal / Copernicus Land Monitoring Service (CLMS):** Provides automated crop/agricultural land masks to suppress seasonal farming false positives.

#### 4. Anti-Saturation & Competitive Differentiation
* **Why It Beats Webinar Clones:** Directly obeys the Ukraine webinar rule (*"Nobody is waiting for your map"*). Instead of another post-flood damage map, CorridorGuard focuses on **pre-incident triage** and outputs **ERP work orders + automated drone/high-res optical tasking bounding boxes**.
* **Strategic Warsaw Jury Synergy:** Framing free Copernicus Sentinel data as the **wide-area tipping-and-cueing layer** that tells operators *where* to task high-resolution optical satellites or drones directly complements Polish space hardware companies in the room (like **Scanway** and **Creotech**).

#### 5. Target Buyer, GTM Strategy & Business Model
* **Primary Buyers:** GAZ-SYSTEM, PERN, PKP PLK, PSE, Orlen, Wody Polskie (Poland), plus European TSOs/rail operators (ENTSO-G, Deutsche Bahn, etc.).
* **Pricing Model:** Annual B2B/B2G SaaS priced per kilometer monitored:
  * **Tier 1 (Copernicus Continuous Triage):** €15–€35 / km / year (e.g., monitoring 2,500 km of high-pressure pipeline = €50k–€85k ARR per enterprise contract).
  * **Tier 2 (Tip-and-Cue Commercial Optical / Drone Dispatch API):** Revenue share / markup on high-resolution optical tasking triggered by critical alerts.

#### 6. 48-Hour Prototype Scope & Live Stage Demo Script
* **Tech Stack:** Python + `openeo` (CDSE), GeoPandas corridor buffer generator, real Sentinel-1 & Sentinel-2 scenes over a real 50 km stretch of Polish Vistula/Oder flood levee or energy pipeline corridor, FastAPI webhook dispatcher + interactive triage UI.
* **Build Schedule:**
  * *Friday Night:* Pull real OpenStreetMap geometry for a 50 km Polish pipeline/rail/levee corridor; test openEO script computing SAR backscatter change + Sentinel-2 NDWI/BSI.
  * *Saturday:* Implement ESA WorldCereal / land-cover false-positive mask + mock "Permitted Maintenance Works" whitelist; build live webhook integration firing structured incident tickets to a mock SCADA/Jira queue with auto-generated drone mission bounding box (GeoJSON/KML).
  * *Sunday (by 13:00 CET):* Polish UI showing side-by-side "Raw Alerts (142)" vs. "After Agricultural & Permit Suppression (3 Critical Tickets)"—proving operational usability.
* **The Live "Wow Moment" on Stage:**
  * Show 142 noisy raw satellite changes along a 50 km Polish corridor—then toggle CorridorGuard's **Agricultural + Permit Suppression Engine**. 139 tractor/maintenance alerts vanish instantly, leaving **2 high-severity unpermitted excavations** that auto-fire inspection tickets with 1-click drone flight paths.

#### 7. Adversarial Jury Q&A Stress Test
* **Q (Scanway / IGiK Mentor):** *"Sentinel-1/2 has 10-meter pixels and a 5–6 day revisit. A saboteur can dig a hole and plant an explosive in 2 hours. Isn't Sentinel too slow and coarse?"*
  * **Winning Rebuttal:** *"For a lone individual on foot, yes—and we never claim Copernicus catches a 2-hour foot intrusion. CorridorGuard catches **heavy-machinery earthworks, systematic site prep, illegal nearby construction, slow pipeline leaks, and gradual levee weakening**—the exact threats that cause 90% of third-party pipeline ruptures and flood breaches—at 1/100th the cost of daily commercial tasking. Even better, our tipping-and-cueing engine tells operators the exact $500\text{ m} \times 500\text{ m}$ box where they should task a sub-meter commercial payload like Scanway's."*

---

### Candidate #5: BlackoutBridge — GNSS-Denied, Offline-First Crisis Routing Engine

#### 1. Strategic Overview & Pitch
* **Challenge Track:** Challenge 2 — Space-enabled crisis response and civil resilience.
* **One-Line Pitch:** An offline-first navigation and convoy routing engine for emergency responders and critical supply fleets that dynamically routes around flooded or damaged infrastructure (using **Sentinel-1 / Copernicus EMS**) and seamlessly switches to **GNSS-denied dead-reckoning & landmark routing** the instant **Galileo OSNMA/EGNOS** integrity checks detect jamming or spoofing.
* **The Core Insight:** During major disasters (such as the September 2024 Lower Silesia floods) or hybrid-warfare crises (as seen daily in Ukraine and increasingly across northern/eastern Poland), three navigation failures happen simultaneously: (1) cellular towers go dark, killing Google Maps/Waze; (2) bridges and roads become impassable; and (3) GNSS jamming/spoofing sends ambulance and logistics drivers miles off course.

#### 2. 2026 Market & Regulatory Catalyst
* **Civil Defense Modernization in Poland:** Following Poland's new Civil Protection and Civil Defense legislation and 2026 CER implementation, municipalities, the State Fire Service (PSP), and critical logistics operators (fuel, hospital supplies, telecom repair crews) are actively procuring resilient, offline-capable crisis mobility tools.
* **Everyday Polish GNSS Jamming:** Pomeranian and eastern Polish emergency/logistics fleets already experience recurring GPS disruptions on commercial devices.

#### 3. Exact EU Space Data Pipeline & Technical Architecture
```text
[CDSE / openEO: Sentinel-1 Flood Mask]   [Copernicus EMS: Damage Vectors]
                 │                                       │
                 └───────────────────┬───────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Hazard-Aware Offline Routing Graph (OpenStreetMap + Valhalla/OSRM)   │
│    - Intersects Sentinel-1 water/flood polygons & EMS bridge damage     │
│      vectors with OSM road edges; dynamically marks edges IMPASSABLE    │
│    - Exports compact, pre-packaged regional offline routing tiles       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │ (Synced over low-bandwidth / Wi-Fi)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. Edge Client (Offline PWA / Mobile) + GNSS Integrity Guard            │
│    - Continuously checks Galileo OSNMA status, EGNOS integrity flags,   │
│      C/N0 ratios, and IMU accelerometer/gyroscope consistency           │
│    - NORMAL MODE: Standard Galileo/EGNOS turn-by-turn hazard routing    │
│    - JAMMED/SPOOFED MODE: Locks out poisoned GPS, activates IMU dead-   │
│      reckoning + visual landmark prompts ("Turn right after red bridge  │
│      at 450m") derived from cached Sentinel-2 + OSM landmark tags       │
└─────────────────────────────────────────────────────────────────────────┘
```
* **EU Space Data & Signals Used:**
  * **Copernicus Sentinel-1 (SAR Flood Masks via CDSE/openEO):** Rapid, cloud-penetrating detection of inundated roads during storms/floods.
  * **Copernicus Emergency Management Service (EMS):** Structured GeoJSON road/bridge damage grading vectors.
  * **Galileo OSNMA & EGNOS:** Real-time navigation integrity monitoring to distinguish genuine satellite fixes from spoofed/jammed signals before they corrupt the driver's route.

#### 4. Anti-Saturation & Competitive Differentiation
* **Why It Beats Webinar Clones:** Turns Copernicus flood/damage layers into **actionable turn-by-turn crisis mobility** rather than a commander's wall map, while uniting Earth Observation (Copernicus) and Navigation Resilience (Galileo/EGNOS) in a single compelling product.
* **Commercial Gap:** Google Maps/Waze fail offline and break catastrophically under GPS spoofing; military tactical suites (like ATAK) are far too complex and restricted for civilian municipal water crews, hospital supply trucks, or volunteer rescue drivers.

#### 5. Target Buyer, GTM Strategy & Business Model
* **Primary Buyers:** Municipal Crisis Management Centers (CZK), Polish State Fire Service (PSP), Volunteer Fire Departments (OSP), Government Centre for Security (RCB), humanitarian NGOs (Red Cross / PAH), and critical utility/medical repair fleets.
* **Pricing Model:** B2G/B2B SaaS: €15–€30 / vehicle / month for the offline resilient client + €1,000 / month municipal dispatch hub API.

#### 6. 48-Hour Prototype Scope & Live Stage Demo Script
* **Tech Stack:** Python (`openeo` + GeoPandas to ingest a real Sentinel-1 flood mask from Lower Silesia 2024 into a local `NetworkX` / `OSRM` / `Valhalla` road graph), React Progressive Web App (PWA) with MapLibre GL offline vector tiles, simulated GNSS Jamming/Spoofing toggle + landmark-anchored driver view.
* **Build Schedule:**
  * *Friday Night:* Download OSM road graph for a Polish city/county (e.g., Kłodzko or Gdańsk/Pomerania) and verify dynamic edge blocking via GeoJSON flood/hazard polygon.
  * *Saturday:* Connect real CDSE Sentinel-1 flood mask ingestion; build PWA driver UI with dual-mode state machine (`GALILEO VERIFIED` vs. `GNSS-DENIED LANDMARK MODE`).
  * *Sunday (by 13:00 CET):* Add live spoofing-injection toggle (showing fake GPS jumping 30 km into the Baltic Sea while BlackoutBridge rejects the spoofed coordinate and keeps the ambulance safely routed via dead-reckoning + OSM landmark cues).
* **The Live "Wow Moment" on Stage:**
  * Show an ambulance routing across Kłodzko. Toggle **"Apply Live Sentinel-1 Flood Mask"**—two bridges turn red and the route instantly reroutes across dry high ground. Then toggle **"Inject Baltic GPS Spoofing"**—the raw GPS dot teleports wildly into a field, while BlackoutBridge flashes `OSNMA INTEGRITY LOSS — GNSS LOCKED OUT`, smoothly preserving the true route using landmark-anchored navigation.

#### 7. Adversarial Jury Q&A Stress Test
* **Q (Hardware / GNSS Judge):** *"Smartphone IMUs drift by tens of meters within 30 seconds. How does dead-reckoning stay accurate during a 20-minute jammed drive?"*
  * **Winning Rebuttal:** *"Pure smartphone IMU dead-reckoning drifts rapidly—which is why BlackoutBridge pairs **map-matching** (constraining heading/turn rates to the offline OSM road topology) with **human-in-the-loop landmark confirmation** (the driver taps one large button or uses voice to confirm major intersections/roundabouts, re-anchoring position error back to $0\text{ m}$ at every junction). For fleet vehicles, it also ingests OBD-II wheel-speed odometry for $< 2\%$ distance drift."*

---

## 4. Final Decision Framework: Picking Your #1 Winner Tonight

Do **not** pick an idea in a vacuum—remember that **Quality of the Team (33%)** and **48-Hour Prototype Execution** decide winners on Sunday at 15:00 CET. Use this team-fit matrix to lock in your choice within 30 minutes tonight:

| If Your Team's Strongest Skills Are... | Pick This Idea | Why You Will Win With It |
| :--- | :--- | :--- |
| **Backend, Cybersecurity, Networking, Embedded/Linux, Compliance** | **#1 ChronoShield** | Highest local Warsaw jury synergy (ChipCraft, Cyber Defense Forces, WAT, Blue Dot Solutions) + razor-sharp April 2027 Polish KSC/NIS2 compliance urgency + real `OSNMAlib` live execution. |
| **Full-Stack Dev + Killer Business/B2B Pitcher (Fintech / Supply Chain)** | **#2 ProofOfRoute** | Strongest European Demo Day commercial story. Zero hardware rollout thanks to Dec 2025 EU Smart Tachograph v2 mandate + combines **both** Galileo OSNMA and Copernicus SAR. |
| **Python, Data Science, GIS / Earth Observation (`openeo` / GeoPandas)** | **#3 EcoForensic** | Lowest duplication risk in the entire room, easiest to deliver a 100% real CDSE Sentinel-1/2/3 demo, and an unforgettable PLN 1.1B Polish news hook from Nov 23, 2026. |
| **Remote Sensing / EO + Industrial / Defense B2B Engineering** | **#4 CorridorGuard** | Directly answers *"Nobody is waiting for your map"*, aligns with Poland's July 2026 CER law, and creates direct partnership appeal with Scanway / energy / rail mentors. |
| **Frontend / Mobile PWA / UX Design + Mapping (`MapLibre` / `OSRM`)** | **#5 BlackoutBridge** | Most visually dramatic live stage demo if your team can nail the offline map + live flood-reroute + spoof-lockout UI smoothly. |

### Immediate Friday Night Action Plan (Next 2 Hours)
1. **Lock the Idea & Challenge Track** on TAIKAI (make sure every teammate agrees on the single core user workflow—cut all extra features).
2. **Verify Data Access Immediately:**
   * If choosing **ChronoShield** or **ProofOfRoute**: Clone `OSNMAlib` (`github.com/Algafix/OSNMA`), verify Python 3.11/3.12 environment, and confirm offline official test vectors + live Galmon stream work tonight.
   * If choosing **EcoForensic**, **CorridorGuard**, or **BlackoutBridge**: Verify your free **CDSE (Copernicus Data Space Ecosystem)** account, run one `openeo` Python query over your Polish Area of Interest (AOI), and **cache the resulting GeoTIFF/JSON locally** so slow Wi-Fi on Sunday cannot break your live demo.
3. **Book Your First Saturday Morning Mentor Slot:**
   * Pitching **ChronoShield**? Go straight to **ChipCraft**, **Cyber Defense Forces / WAT**, and **Blue Dot Solutions** mentors to stress-test your anti-meaconing logic.
   * Pitching **EcoForensic** or **CorridorGuard**? Go straight to **IGiK** and **Scanway** mentors to validate your SAR/optical false-positive suppression.
   * Pitching **ProofOfRoute**? Go straight to **ABGi Poland** and past CASSINI winners to sharpen your B2B unit economics for European Demo Day.