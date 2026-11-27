# CASSINI Warsaw 2026: 5 High-Conviction Ideas

Winning pattern for Warsaw: **Do not sell a map. Sell a legally, operationally, or financially consequential output** — a signed attestation, a work order, a customs dossier, a shutdown decision — that a named Polish/EU buyer already has a 2026 regulatory deadline to produce.

---

### 1. One-Line Pitch & Challenge Track
**Galileo Time-Trust: OSNMA-verified timestamping appliance for OT/SCADA logs that auto-generates NIS2-proof evidence when GNSS timing is spoofed.**
**Challenge 1: Cybersecurity for space-based strategic enablers**

**2. Exact EU Space Data/Signal Pipeline**
Galileo E1B I/NAV OSNMA data — DSM-HKROOT, DSM-KROOT, TESLA chain verification via EUSPA's `osnmalib` / OSNMA test vectors and live/recorded streams from the Galileo Service Centre — is decoded to verify that the navigation message, and therefore Galileo System Time, is authentic and not replayed/spoofed. Verified time anchors a hash-chain (SHA-256 Merkle tree) over simulated SCADA/PMU event logs. Galileo HAS (E6B) is used as secondary correction source for receiver position sanity-check. Pipeline computes: OSNMA tag verification status per satellite, TESLA key disclosure delay check, clock-offset vs. NTP/terrestrial reference divergence, and outputs a signed JSON attestation + NIS2 Article 23 early-warning PDF (24h deadline format).

**3. Why It's NOT a Duplicate**
This is not a jamming/spoofing heatmap — no map is the product. The product is a *cryptographic non-repudiation artifact* a CISO can hand to UKE/CSIRT NASK during a NIS2 incident. Heatmaps tell you something bad happened somewhere; this proves whether *your specific substation log* can be trusted in court and in an incident report — the exact question NIS2 and the CER Directive force operators to answer.

**4. Target Buyer & Business Model**
Polish essential entities under NIS2: PSE (transmission grid), PKP Energetyka, Orange Polska/Exatel (telecom timing for 5G TDD depends on GNSS phase sync), Gaz-System. Buyer persona: OT Security Lead / NIS2 Compliance Officer. Pricing: €18–35k per site appliance + €6k/yr attestation SaaS, or API pricing per 10k signed log batches. Willingness to pay in 2026 is regulatory, not discretionary — NIS2 fines reach €10M or 2% of global turnover.

**5. 48-Hour Prototype Scope**
Team streams pre-recorded + live Galileo I/NAV data through `osnmalib`, verifies OSNMA TESLA chain, and shows a live demo: (a) clean log stream gets green signed attestation, (b) injected spoofed/replayed timestamp triggers failed tag verification, attestation is refused, and a NIS2 incident ticket + PDF evidence pack is auto-generated in a mock ticketing UI. Backend in Python, one dashboard *only as demo surface* — the deliverables shown on screen are the signed JSON and the PDF. Fully Fresh-Code compliant using public EUSPA libraries.

**6. Biggest Risk & Likely Jury Pushback**
ChipCraft/WAT jury: *"You don't have an OSNMA-capable receiver here, and OSNMA verification has latency from TESLA key disclosure — this isn't real-time."* Defense: Be upfront — prototype uses EUSPA test vectors + recorded live sky data, which is exactly how OSNMA integrators validate; state the ~30s TESLA delayed-disclosure design openly and position product as *forensic attestation* (proof after the fact for regulators), not real-time blocking. That honesty converts the weakness into the use case.

---

### 1. One-Line Pitch & Challenge Track
**SAR-Truth: Cross-modal API that verifies whether a claimed satellite/damage image is real by physically cross-checking it against Sentinel-1 SAR backscatter — exposing forged EO imagery used in insurance fraud and wartime disinformation.**
**Challenge 1: Cybersecurity for space-based strategic enablers**

**2. Exact EU Space Data/Signal Pipeline**
Via CDSE/openEO: Sentinel-1C GRD (IW, VV+VH backscatter, accessed via openEO `load_collection` on Copernicus Data Space) and Sentinel-2C L2A (B04/B08/B11) for the same AOI/date claimed by a suspect image. Pipeline computes SAR-optical physical consistency: e.g., claimed "flooded/destroyed" optical scene must show corresponding VH backscatter drop (water) or coherence/backscatter change (structural destruction); a claimed clear-sky optical image dated during Sentinel-2 cloud cover or inconsistent with S1 acquisition geometry fails. Uses SNAP-derived backscatter statistics + a lightweight consistency classifier. Output: verification verdict (AUTHENTIC / INCONSISTENT / FABRICATED), confidence, and the physics evidence, via REST API.

**3. Why It's NOT a Duplicate**
Inverse of the banned cliché: instead of *producing* another change-detection dashboard, it *audits other people's imagery*. As generative-AI fake satellite images enter insurance claims and Telegram disinformation channels, nobody in the hackathon field is building the verification layer. Output is an API verdict integrated into a claims workflow or a fact-check desk — not a visualization.

**4. Target Buyer & Business Model**
PZU and European reinsurers (Munich Re, Hannover Re) processing war/weather damage claims with user-submitted imagery; EUvsDisinfo / EEAS StratCom and defense OSINT cells verifying claimed strike damage; EO data marketplaces needing provenance checks. Pricing: per-verification API (€0.40–2.00/call at volume) or €3–8k/month enterprise licence for insurers. Clear ROI: one rejected fraudulent claim pays for a year.

**5. 48-Hour Prototype Scope**
Pre-select 6–8 test cases: 3 real Sentinel-2 scenes (e.g., 2024 Silesia flood, verified), 3 forged versions (edited/AI-generated — remove a building, fake flooding, wrong date). Live demo: judge submits/selects an image + claimed date/location, API pulls the matching Sentinel-1 scene from CDSE in real time, runs consistency checks, returns verdict with backscatter evidence panels. Achievable with openEO + rasterio + FastAPI.

**6. Biggest Risk & Likely Jury Pushback**
IGiK/Scanway jury: *"SAR and optical acquisitions aren't simultaneous, clouds and revisit gaps make this unreliable, and 10–20m resolution can't verify building-level claims."* Defense: Concede scope explicitly — v1 verifies *scene-level* claims (flooding extent, large-structure destruction, date/location authenticity) at Sentinel resolution, which covers the highest-value fraud/disinfo cases; use Sentinel-1's cloud independence as the core advantage, and present confidence + acquisition-time delta transparently rather than a binary fake/real claim.

---

### 1. One-Line Pitch & Challenge Track
**LeveeWork: Sentinel-1 InSAR millimetre-deformation monitoring of Polish flood levees that automatically issues ranked maintenance work orders into asset-management systems before failure.**
**Challenge 2: Space-enabled crisis response and civil resilience**

**2. Exact EU Space Data/Signal Pipeline**
Sentinel-1A/1C SLC (IW mode) via CDSE, processed with SNAP GPT / openEO InSAR workflows: Persistent Scatterer / SBAS interferometry over multi-temporal stacks computes line-of-sight deformation velocity (mm/yr) along levee crests on the Vistula and Odra. Sentinel-2 L2A NDWI/NDVI adds vegetation/erosion and soil-moisture context; Copernicus EMS risk-mapping products provide baseline flood exposure. Pipeline thresholds deformation velocity + acceleration against levee asset registry (open data from Wody Polskie / geoportal.gov.pl); exceedance auto-generates a structured work order (asset ID, chainage, deformation rate, urgency class) in a format importable to IBM Maximo / GIS asset systems.

**3. Why It's NOT a Duplicate**
Explicitly answers the webinar warning *"nobody is waiting for your map"* — the deliverable is a *prioritized, budget-ready maintenance ticket list*, not flood extent polygons. It also shifts from reactive crisis