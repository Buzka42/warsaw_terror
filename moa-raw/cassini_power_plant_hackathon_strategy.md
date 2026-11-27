# 12th CASSINI Hackathon (Warsaw) Strategy Guide
## Project: Integrated Space-Based Cyber-Physical Threat Detection for Power Plants

---

## 1. Executive Summary & Winning Positioning

Your core concept—fusing **Galileo**, **Copernicus**, **ICS/SCADA telemetry**, and **Cyber Threat Intelligence (CTI)** to protect power plants—is directly aligned with **Challenge 1: Cybersecurity for space-based strategic enablers**. 

However, to win both the **Warsaw finals** and **European Demo Day**, the concept must pivot away from a generic *"AI + satellite monitoring dashboard"* (which violates the hackathon's anti-saturation rule: *"Nobody is waiting for your map"*) and instead become an **out-of-band cyber-physical verification and NIS2/KSC compliance engine**.

### The Sharpened Pitch
> **One-Line Pitch:** An out-of-band cyber-physical verification engine for European power utilities that pairs real-time **Galileo OSNMA** timing-integrity checks with **Copernicus** physical state verification to detect falsified SCADA telemetry and auto-generate **24-hour NIS2/KSC incident reports**.

### Why This Positioning Wins All Three Rubric Pillars
* **Relevance (33%):** Directly uses operational **Galileo OSNMA** (Initial Service live since July 2025) and **Copernicus Sentinel-1/2/3** via **CDSE/openEO** to defend critical energy infrastructure.
* **Innovativeness & Business Viability (33%):** Solves a specific, high-stakes workflow bottleneck—detecting *"Stuxnet-style"* spoofed OT telemetry and meeting Poland's **amended KSC Act (NIS2)** reporting deadlines ahead of the **April 3, 2027** full enforcement date.
* **Execution Feasibility (33%):** Achievable in 48 hours using real historical Sentinel-2/3 imagery of a Polish power plant (e.g., Kozienice or Bełchatów) fused with a realistic Python-based PMU/SCADA + OSNMA attack replay simulator.

---

## 2. Technical Architecture: Surviving Warsaw's Technical Jury

Warsaw's mentors and judges include GNSS hardware engineers (**ChipCraft**), remote sensing academics (**IGiK**), space optics specialists (**Scanway**), EO experts (**Blue Dot Solutions**), and military cyber-defense experts (**Cyber Defense Forces / MUT**). 

To survive their scrutiny, **never claim that Copernicus satellites detect cyberattacks in real time.** Instead, split your architecture strictly by **timescale**:

### Layer 1: Real-Time Timing & Synchronization Tripwire (Sub-Second)
* **The Threat:** Modern power grids rely on Phasor Measurement Units (PMUs) synchronized via GNSS to measure voltage/current phase angles across substations. Under **IEEE C37.118.1**, Total Vector Error ($\text{TVE}$) must stay below $1\%$. On Europe's $50\ \text{Hz}$ grid, a $1\%$ $\text{TVE}$ phase-angle limit corresponds to a maximum timing error of approximately **$\pm 31.8\ \mu\text{s}$**. A covert GNSS timing spoofing attack can shift substation clocks without moving the receiver's reported position, tripping protection relays or masking a cyber intrusion.
* **EU Space Signal:** **Galileo OSNMA** (Open Service Navigation Message Authentication).
* **Pipeline Logic:**
  1. Continuously validates cryptographic **OSNMA** status flags on substation GNSS-disciplined clocks (PTP / IEEE 1588 / NTP).
  2. **Crucial Technical Nuance (for ChipCraft):** OSNMA authenticates navigation *data* (preventing forged ephemeris/time messages), but does **not** prevent jamming or *meaconing* (delay-and-replay attacks). Therefore, your engine pairs OSNMA verification with **Carrier-to-Noise density ratio ($C/N_0$) anomaly checks** and **local oscillator holdover drift monitoring** (flagging clock slew rates that exceed physical crystal drift).

### Layer 2: Out-of-Band Physical Truth Verification (Hours to Days)
* **The Threat:** Advanced Persistent Threats (APTs) in Operational Technology (OT)—such as Stuxnet or Industroyer2—compromise SCADA/HMI systems to display *"all normal"* readings to operators while physically degrading equipment or manipulating load.
* **EU Space Data (via CDSE / openEO API):**
  * **Copernicus Sentinel-2 (L2A, 10m–20m, Sentinel-2A/B/C):** Extracts physical operational proxies over the plant Area of Interest (AOI), specifically **cooling tower vapor plumes** (optical Bands 2/3/4/8 + cloud/shadow masking) and **localized high-heat anomalies** using Short-Wave Infrared (**SWIR Bands 11 & 12**).
  * **Copernicus Sentinel-3 (SLSTR, 1 km Thermal IR):** Monitors macro-scale **cooling-water thermal discharge plumes** in adjacent rivers or cooling reservoirs (e.g., the Vistula River at Kozienice or cooling lakes at Bełchatów) to verify whether thermal output matches reported MW generation.
  * **Copernicus Sentinel-1 (SAR C-Band, Sentinel-1A/C):** Provides all-weather, day/night structural change detection (coherence loss / backscatter anomalies) over adjacent high-voltage switchyards and perimeter zones when cloud cover blocks Sentinel-2.
* **Pipeline Output:** Converts satellite passes into a binary/probabilistic **Physical Operational State** (e.g., *Active Full Load*, *Reduced/Idle*, *Anomalous Thermal Signature*).

### Layer 3: Deterministic Fusion & Automated Workflow Output
Avoid black-box "AI fusion" buzzwords. Use a transparent, auditable **Physical-Digital Discrepancy Engine**:
1. **Inputs:**
   * Layer 1: Galileo OSNMA + clock-drift telemetry.
   * Layer 2: Copernicus openEO physical state vector.
   * Layer 3a (OT Telemetry): Read-only export via a **unidirectional hardware data diode** (IEC 60870-5-104 / Modbus / IEEE C37.118 logs) containing reported MW output and timestamps.
   * Layer 3b (CTI): Public/sector Threat Intelligence feeds (e.g., **MISP**, **CERT Polska**, **CSIRT MON**, **MITRE ATT&CK for ICS**).
2. **Correlation Rule Example:**
   * `IF` (OSNMA fails OR clock drift $> 20\ \mu\text{s}$) `AND` (SCADA reports nominal $100\%$ load while Sentinel-2/3 shows absent cooling plume / thermal drop) `AND` (active OT CTI indicator) $\rightarrow$ **CRITICAL: Coordinated Cyber-Physical Manipulation Suspected**.
3. **Actionable Workflow Outputs (NOT Just a Map):**
   * **SIEM/SOAR Webhook:** Pushes a structured JSON alert (STIX 2.1 / ECS format) directly into Splunk, QRadar, or TheHive.
   * **Automated NIS2 / KSC S46 Incident Draft:** Pre-populates a **24-hour Early Warning** compliance report (timeline, affected asset, cryptographic OSNMA evidence, satellite verification timestamp) ready for one-click submission to **CSIRT NASK / CSIRT GOV / CSIRT MON**.

---

## 3. 2026 Regulatory & Business Viability (Go-To-Market)

### Regulatory Tailwinds in Poland & the EU (Late 2026 Context)
* **Poland's Amended KSC Act (NIS2 Transposition):** Entered into force on **April 3, 2026** (*Dz. U. 2026 poz. 252*). Essential/key energy entities had to self-register by **October 3, 2026**, and face full technical compliance obligations by **April 3, 2027** (just 4 months away).
* **Stakes for Buyers:**
  * Corporate fines up to **€10,000,000 or 2% of global annual turnover** for Key Entities.
  * **Personal management liability:** Fines up to **300% of a manager's salary** (100% in public entities) for failing to maintain cybersecurity governance.
  * Strict **24-hour Early Warning** and **72-hour Incident Notification** mandates via Poland's **S46** system.
* **EU CER Directive (Critical Entities Resilience):** Mandates integrated *physical* and *cyber* resilience monitoring for energy infrastructure—directly justifying space-based out-of-band physical verification.

### Target Customers & Pricing Model
* **Primary Buyers:**
  * **Transmission System Operators (TSOs):** e.g., **PSE** (Polskie Sieci Elektroenergetyczne) in Poland, 50Hertz, TenneT.
  * **Major Power Utilities:** **PGE GiEK**, **Enea Wytwarzanie**, **Tauron**, **Orlen**.
  * **OT Managed Security Service Providers (MSSPs) & Insurers:** Offering cyber-physical risk validation.
* **Business Model (B2B SaaS / API):**
  * **Per-Facility Annual License:** €15,000–€35,000 per critical power plant or high-voltage substation per year.
  * **Zero-Touch Deployment:** Connects strictly outside the OT security perimeter via read-only data diode exports—eliminating the #1 procurement blocker for air-gapped utilities.

---

## 4. 48-Hour Prototype Execution Plan (Nov 27–29, 2026)

### Recommended Target Site for Live Demo
Choose a real Polish power plant with unmistakable visual/thermal signatures in Copernicus data:
* **Option A (Best for Thermal Plume + Cooling Towers):** **Elektrownia Bełchatów** ($51.266^\circ\text{N}, 19.327^\circ\text{E}$) — Europe's largest lignite power plant; massive cooling towers produce clear Sentinel-2 steam plumes and thermal signatures.
* **Option B (Best for River Thermal Discharge + Proximity to Warsaw):** **Elektrownia Kozienice** ($51.664^\circ\text{N}, 21.462^\circ\text{E}$) — Located on the Vistula River near Warsaw; strong cooling tower plumes and river thermal discharge detectable in Sentinel-3 SLSTR.

### The Live Sunday Demo Scenario: *"Operation Silent Drift"*
Show a 2-minute live end-to-end replay instead of static slides:
1. **Baseline State (Normal):** Dashboard/API shows Kozienice/Bełchatów running at nominal load. Galileo OSNMA status is `AUTHENTICATED`, PMU timing offset is $< 1\ \mu\text{s}$, and the latest Sentinel-2 openEO pass confirms active cooling tower plumes.
2. **Attack Injection (Live Trigger):** Click **"Simulate Cyber-Physical Attack"**. Your Python backend injects:
   * A **Galileo timing spoofing/meaconing event** (OSNMA flag drops + clock slew exceeds $31.8\ \mu\text{s}$ IEEE C37.118 threshold).
   * A **compromised SCADA feed** still reporting `100% Nominal Output` (masking a forced turbine/cooling trip).
   * A **real historical Sentinel-2/3 openEO pass** (from a known outage/maintenance date) showing missing thermal/steam signature.
   * A matching **OT CTI alert** (e.g., ICS Modbus/IEC-104 anomalous command signature).
3. **Automated Response (The "Wow" Moment):**
   * The Discrepancy Engine raises a **CRITICAL Cyber-Physical Divergence Alert** with an explainable breakdown (no black-box AI).
   * The system **automatically generates and downloads a structured NIS2/KSC S46 24-Hour Early Warning Report (JSON + PDF)** and fires a live webhook into a mock SOC queue (e.g., Slack/Discord/TheHive webhook).

### Recommended Tech Stack (Fresh Code Rule Compliant)
* **EO Pipeline:** Python + `openeo` client connected to **CDSE openEO Federation** (`openeofed.dataspace.copernicus.eu`). Pre-cache 2–3 real GeoTIFF/JSON stats from CDSE as a fallback in case venue Wi-Fi drops, while running live API queries when online.
* **Backend & Simulator:** Python (**FastAPI**) hosting the SCADA/PMU simulator, OSNMA/clock-drift anomaly detector, Discrepancy Scoring Engine, and PDF/JSON NIS2 report generator (`ReportLab` or `WeasyPrint`).
* **Frontend:** Lightweight **React / Next.js** or **Streamlit** SOC analyst console (focus 80% on the alert timeline, telemetry charts, OSNMA status, and S46 report preview; keep the map secondary).

### Team Task Split (4–6 People)
| Role | Friday Night – Saturday Morning | Saturday Afternoon – Sunday Morning |
| :--- | :--- | :--- |
| **EO / Space Engineer** | Pull real Sentinel-2 L2A (RGB + SWIR B11/B12) & Sentinel-3 SLSTR passes over Bełchatów/Kozienice via CDSE openEO. | Compute automated plume/thermal index (normal vs. outage dates); expose clean JSON API endpoint + cached fallback. |
| **GNSS / OT Cyber Engineer** | Build Python IEEE C37.118 PMU + SCADA simulator with realistic 50 Hz timing drift & OSNMA flag states. | Implement deterministic correlation logic + CTI rule matching + NIS2/KSC S46 JSON/PDF generator. |
| **Full-Stack / UI Dev** | Scaffold SOC Operator Console + live attack-trigger controls. | Integrate live charts (clock drift vs. $31.8\ \mu\text{s}$ threshold, SCADA vs. EO state) + webhook demo. |
| **Business / Pitch Lead** | Validate KSC/NIS2 S46 reporting fields, Polish utility pricing, and competitor gap analysis. | Build 3–5 min pitch deck, rehearse Q&A defense matrix, record backup video of live demo. |

---

## 5. Warsaw Jury Q&A Defense Matrix

| Likely Jury Question | Who Will Ask | Winning Defense |
| :--- | :--- | :--- |
| **"Sentinel-2 revisits every few days and clouds block optical imagery. How does this stop a real-time cyberattack?"** | IGiK / Blue Dot Solutions / Scanway | *"It doesn't—and we explicitly separate timescales. **Galileo OSNMA** handles sub-second real-time detection of timing/synchronization attacks. **Copernicus** acts as an independent, out-of-band physical verification layer to catch stealthy, long-dwell OT manipulation (like Stuxnet) and verify physical plant state during comms blackouts. When clouds block Sentinel-2, **Sentinel-1 SAR** provides all-weather structural monitoring."* |
| **"OSNMA only authenticates navigation data—it doesn't stop jamming or replay (meaconing) attacks."** | ChipCraft | *"Exactly right. That's why our Layer 1 fuses OSNMA authentication flags with **$C/N_0$ signal-strength monitoring** and **local oscillator holdover drift checks** against Europe's $\pm 31.8\ \mu\text{s}$ IEEE C37.118 threshold. If a meaconer delays a valid OSNMA signal, the clock slew rate vs. local crystal holdover catches it."* |
| **"Utilities will never let a startup plug software into an air-gapped SCADA network."** | Cyber Defense Forces / MUT | *"We never touch the OT control plane. Our engine sits strictly **out-of-band**, ingesting read-only telemetry exported through the plant's existing **unidirectional hardware data diodes** (or historian mirrors). Zero inbound commands, zero added attack surface."* |
| **"Sentinel-3 SLSTR thermal resolution is 1 km—you can't see a single transformer."** | IGiK / Blue Dot Solutions | *"Correct. We don't use Sentinel-3 to inspect individual transformers. We use Sentinel-3 SLSTR specifically for **macro-scale cooling water discharge plumes** in adjacent rivers/lakes (e.g., Vistula at Kozienice), and **Sentinel-2 (10m–20m optical/SWIR)** for cooling tower vapor plumes and localized high-heat anomalies."* |
| **"Why wouldn't PGE or PSE just use their existing SIEM (Splunk/QRadar)?"** | Business / VC Judges | *"SIEMs only see what the plant's own IT/OT network tells them. If an attacker compromises the SCADA historian or spoofs GNSS clocks, the SIEM is blind. We don't replace Splunk—we feed an **independent, space-verified ground-truth signal** directly into their existing SIEM and automate their **KSC/NIS2 24-hour S46 report**."* |

---

## 6. Winning Pitch Deck Blueprint (3–5 Minutes)

1. **Slide 1 — The Hook (20s):** *"In April 2026, Poland's amended KSC Act made 24-hour cyber incident reporting mandatory—with fines up to €10M and 300% personal manager liability. Yet if an attacker spoofs a power plant's SCADA telemetry or GNSS clocks, operators are flying blind."*
2. **Slide 2 — The Gap (30s):** Show the blind spot: OT networks are self-referential. Existing space data (Galileo, Copernicus) and SOC tools live in silos.
3. **Slide 3 — The Architecture (45s):** Clean two-timescale diagram: **Sub-second Galileo OSNMA + Holdover** (Timing Truth) + **Out-of-Band Copernicus S1/S2/S3 via openEO** (Physical Truth) $\rightarrow$ **Automated SIEM + NIS2 S46 Report**.
4. **Slide 4 — Live Prototype Demo (90s):** Run *"Operation Silent Drift"* live on a real Polish power plant (Kozienice/Bełchatów). Show real openEO data + live generated NIS2 24-hour report.
5. **Slide 5 — Business Model & Roadmap (30s):** B2B SaaS (€15k–€35k/plant/yr), zero-touch data-diode integration, targeting Polish TSO/utilities ahead of the **April 3, 2027** KSC compliance deadline.
6. **Slide 6 — Team & Ask (15s):** Why your team can build it, plus next steps (pilot with a Polish energy operator / ESA BIC Poland).