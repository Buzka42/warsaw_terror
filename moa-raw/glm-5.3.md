## Idea 1 — **ChronoMesh**: Galileo-authenticated time integrity for critical infrastructure

**1. One-Line Pitch & Challenge Track**
A software-only "time trust layer" that uses **Galileo OSNMA** cryptographic authentication plus cross-site consensus to detect GNSS *spoofing of timing infrastructure* (power grids, telecom, finance) and auto-generates the NIS2 24-hour early-warning report — turning an invisible attack into a detected, reported, failed-over event. Track: **Challenge 1** (cybersecurity of space-based strategic enablers — Galileo is the enabler being defended).

**2. Exact EU Space Data/Signal Pipeline**
- **Galileo E1-B I/NAV navigation bits + OSNMA**: live capture via RTL-SDR + GNSS-SDR, or (venue-safe) pre-recorded IF datasets; OSNMA verification (TESLA key chain, Kroot, MAC over ephemeris/TOW) using the open-source `galileo-osnma` Python reference library per the EUSPA OSNMA ICD.
- **Consensus layer**: lightweight agents on existing GNSS-disciplined NTP/PTP grandmasters exchange signed pairwise time-offset vectors; one site diverging while claiming "satellite lock" = spoofing.
- **Outputs (no map involved)**: (a) integrity flag consumed by synchrophasor/SCADA quality words (IEEE C37.118 / IEC 61850 style), (b) auto-drafted **NIS2 Art. 23 early-warning ticket pushed via webhook to the SOC/SIEM**, (c) failover command to holdover oscillator.

**3. Why It's NOT a Duplicate**
It is the explicit counter to the saturated jamming-heatmap webinar: a heatmap tells you where interference is, not whether *your* clock is lying. Jamming is denial (loud, obvious); spoofing is forgery (silent, fatal) — and only cryptographic authentication defeats forgery. We output SOC tickets, compliance reports, and failover commands, not a heat layer. No one at the venue will be doing crypto-level signal verification.

**4. Target Buyer & Business Model**
NIS2-covered operators running GNSS-disciplined clocks: DSOs/TSOs (PMU sync), telcos (5G TDD needs ±1.5 µs; a spoofed TDD frame timing breaks the radio network), banks/exchanges (MiFID II RTS-25: 100 µs HFT timestamps traceable to UTC), data centers. SaaS per protected site: €4–8k/site/year, agent license + SIEM integration fee. The NIS2 24-hour duty creates the compliance pull; Poland's KSC turbulence makes an EU-wide, regulator-format-agnostic reporter extra valuable.

**5. 48-Hour Prototype Scope**
- Agent v0: verify OSNMA on an authentic Galileo capture (passes), then on a forged/altered I/NAV replay (NMA fails → alarm). This is the live demo: real Galileo signal, real key-chain verification, real detection.
- 3-laptop consensus mesh; one fed a TOW-jumped replay → divergence alarm while "locked".
- Auto-generated NIS2-style incident report (PDF/STIX) + webhook to a mock SOC dashboard; failover action shown on a simulated PTP grandmaster.
- Optional stretch: Septentrio mosaic-X5 native OSNMA output if a dev kit is secured before Friday.

**6. Biggest Risk & Likely Jury Pushback**
The ChipCraft-class judge: *"Hardware timing firewalls already exist (Safran/Orolia, Adtran), and most commercial receivers don't expose raw I/NAV — can a software agent even see OSNMA?"* Defense: (1) hardware boxes are €5–10k+/site capex with slow procurement; we're a retrofit layer on existing fleets, and receivers that export raw nav data (u-blox, Septentrio) already enable it; (2) consensus detection covers legacy-receiver fleets — OSNMA coverage grows as OSNMA-capable chipsets (mosaic-class) commoditize, so our crypto layer is the roadmap, not vaporware; (3) we detect *protocol-level forgery of time*, a class jamming detectors and RF heatmaps structurally cannot address.

---

## Idea 2 — **WałWatch**: Sentinel-1 levee integrity triage that dispatches inspectors, not maps

**1. One-Line Pitch & Challenge Track**
A millimetre-precision **Sentinel-1 InSAR + coherence** monitoring service for linear flood-defence assets (embankments, canal walls, rail earthworks) that ranks thousands of kilometres by structural risk and **auto-dispatches inspection work orders into asset-management/CMMS systems** when deformation accelerates — predictive triage for the CER Directive era. Track: **Challenge 2** (civil resilience).

**2. Exact EU Space Data/Signal Pipeline**
- **Sentinel-1 IW SLC** (S1A + S1C), 15–30 scenes per AOI from **CDSE (S3 / OData)**; SBAS/PS-InSAR processing in SNAP/ISCE2 (or COMET LiCSAR velocity priors for speed) → segment-wise LOS deformation time series in mm.
- Pairwise **coherence loss** on embankment segments post-flood-wave as a soil-saturation/settlement soft signal.
- Fusion: embankment registry geometry (Wody Polskie GIS / OSM), national LiDAR DTM, river gauges.
- Compute: per-segment velocity vs. multi-year baseline; anomaly = kσ excursion with sustained trend → ranked GeoJSON work order (not a dashboard) pushed by webhook to mock SAP-PM/CMMS, each ticket carrying its SAR evidence chip (unwrapped interferogram crop).

**3. Why It's NOT a Duplicate**
The banned pattern is *post-event optical damage maps*. WałWatch is *pre-event structural health*: millimetric deformation with weeks-to-months lead time, applied to assets nobody instruments (Poland's embankment network is monitored by driving past it). We sell the **ranking decision** — which 2 km of 3,000 gets the scarce inspection crew and the pre-flood reinforcement budget — and we name it in Polish (*wał*), because the 2024 Lower Silesian floods are the local jury's raw memory.

**4. Target Buyer & Business Model**
**Wody Polskie** (State Water Holding — owns/maintains the embankment network), PKP PLK (rail earthworks), German/Dutch water boards. The **CER Directive (EU) 2022/2557** obliges resilience assessment of critical entities — a live budget line for 2026–27. Pricing: €30–80 per km per year, tiered, plus a per-inspection-ticket fee; positioned as maintenance opex, not a €100k enterprise InSAR portal (which is how SkyGeo/Altamira-class incumbents sell, leaving water boards unserved).

**5. 48-Hour Prototype Scope**
- One AOI: a Vistula reach near Warsaw or the Nysa Kłodzka corridor hit by Storm Boris (Sept 2024).
- SNAP SBAS over ~15 SLCs → velocity points per embankment segment; segment scoring + threshold engine.
- Live demo: new interferometric pair ingested and re-scored on stage; webhook fires a work order into a mock CMMS; the "map" is deliberately shown only as an evidence attachment to the ticket.
- Honest-validation slide: stable urban control segment vs. embankment segment behavior.

**6. Biggest Risk & Likely Jury Pushback**
The IGiK-class judge: *"InSAR on vegetated earthen levees decorrelates; you'll have no persistent scatterers."* Defense, pre-registered: we don't claim geodetic verdicts — we claim triage ranking from a hybrid signal (PS/DS points on culverts, revetments, and road crossings + segment-level coherence statistics as a soft indicator), thresholds calibrated against inspection outcomes over time; and we flag honest limitations on the slide — which itself differentiates us from every hand-wavy "SAR + AI" pitch they'll see that weekend. Business pushback (*"water boards are slow and poor"*) is answered by CER-driven budget timing and the commercial rail buyer as the wedge.

---

## Idea 3 — **Parametra**: the parametric payout trigger oracle

**1. One-Line Pitch & Challenge Track**
We convert Copernicus flood and fire products into **signed, machine-readable parametric payout triggers** delivered by webhook to insurers, humanitarian anticipatory-action funds, and municipal treasuries. We don't show anyone a map — **we are the layer that decides when the money moves**. Track: **Challenge 2**.

**2. Exact EU Space Data/Signal Pipeline**
- **Sentinel-1 GRD IW (VV/VH)** via **CDSE openEO** process graph (`openeo.dataspace.copernicus.eu`): speckle filter → adaptive VV threshold (~−17 to −20 dB, Otsu-calibrated per tile) → zonal statistics over contract polygons → flooded-area percentage **within ~6 hours of each pass**.
- **Sentinel-3 SLSTR FRP** + EFFIS/CAMS for wildfire triggers; **CEMS Rapid Mapping** vectors ingested as an authoritative complementary layer where an activation exists.
- **Trigger engine**: each contract specifies peril, polygon, threshold, waiting period, and a data-source hierarchy → deterministic verdict → **attestation**: hash of all inputs + code version, RFC-3161-timestamped and signed, appended to an immutable log → payout webhook (demo into a mock insurer core + mobile-money sandbox).

**3. Why It's NOT a Duplicate**
"Nobody is waiting for your map" is literally our design doc. Flood extent is *input*; the product is a contract-grade legal/financial decision with replayable provenance. Speed (verdict in hours, machine-readable) and dispute-proof auditability are what EMS PDFs and shapefiles-for-humans don't provide — and what parametric products, anticipatory-action grants, and pre-authorized municipal procurement legally require.

**4. Target Buyer & Business Model**
(1) Insurers/reinsurers writing parametric flood cover in CEE (demand spiked after the 2024 floods; the Commission is actively pushing wider nat-cat cover in Europe); (2) humanitarian anticipatory action (Red Cross forecast-based financing, START Network, WFP — established trigger-finance precedents, not hypothetical buyers); (3) municipalities that need an objective trigger event to release pre-approved emergency procurement *before* the flood peak. Pricing: per-policy per-season transaction fee (€0.50–2) at insurer volume + platform SaaS; grant-funded humanitarian deployments.

**5. 48-Hour Prototype Scope**
- Author 3 real contract specs (e.g., Kłodzko Valley household cover; Odra-basin anticipatory grant; municipal pre-authorization).
- Run the openEO job on the actual Sept 2024 flood scenes from CDSE — the demo shows the trigger firing at T+5h after the relevant pass, with today's data pulled live on stage.
- Signed attestation + payout webhook into a mock core; **"dispute mode"**: replay the exact input hash and code version to show the verdict regenerates identically — the provenance party trick for the judges.

**6. Biggest Risk & Likely Jury Pushback**
*"EMS and JRC already publish flood extent; Floodbase already does parametric triggers — why pay you?"* Defense: EMS publishes human-readable products during activations, not a contract-grade machine API with SLAs, verdicts, and provenance; Floodbase is multi-source and US-market leaning — no EU-native S1/S3/CEMS fusion, no CEE distribution. The second attack is **basis risk** (trigger ≠ actual loss) — answered head-on: the pre-agreed trigger methodology *is* the product, published to the reinsurer, with hybrid triggers (S1 + gauges + GLOFAS) and waiting-period logic demonstrated live. That transparency, not pixels, is what a parametric buyer pays for.

---

## Idea 4 — **GhostStack**: orbital enforcement of emitters that officially don't exist

**1. One-Line Pitch & Challenge Track**
We cross-reconcile **Sentinel-5P (TROPOMI)** industrial emission plumes — NO₂, SO₂, CO — against the European pollutant release register, permits, and sanctions lists, surfacing **"ghost emitters"**: refineries, factories, and waste-burning sites that legally don't exist but breathe like industry. Output: **ranked enforcement dossiers** for authorities and counterparty-utilization intel for commodity desks. Track: **Challenge 3**.

**2. Exact EU Space Data/Signal Pipeline**
- **Sentinel-5P L2 NO₂/SO₂/CO** from **CDSE (`s3://eodata`)**: 30–90-day oversampling (pixel-averaging + wind-rotated aggregation, Beirle-class methodology) at 100–500 m grid over a chosen AOI; Gaussian plume fit with local wind reanalysis → source location + emission flux time series.
- **Reconciliation join**: E-PRTR / European industrial emissions portal facility coordinates, IED permit registries, OSM industrial polygons, the EU consolidated sanctions list, and open business registries (KRS/BRIS).
- Mismatch classes: (a) strong plume, no permit/registry entry → illegal operation; (b) sanctioned site with sustained activity → sanctions-breach evidence; (c) registered site with flux ≫ declared → under-reporting (the signature of theft-tapped pipelines and off-book production); plus **S3/SLSTR hotspot** co-detections of illegal waste-dump fires — a nationally infamous crime category in Poland since 2023.

**3. Why It's NOT a Duplicate**
Zero vessels, zero AIS, zero SAR dark-ship tropes — and TROPOMI is the Copernicus stream *no hackathon team touches* (everyone camps on S1/S2). The workflow isn't detection-on-a-map, it's **registry forensics**: registries are annual, stale, and self-reported; the orbit is daily and doesn't fill in forms. The product is a prosecutorial lead with a legal basis attached (Environmental Crime Directive (EU) 2024/2103, transposed by May 2026; EU sanctions regimes).

**4. Target Buyer & Business Model**
Government: OLAF, national environmental-crime units and sanctions authorities with fresh ECD-transposition budgets. B2B: commodity trading desks needing **independent throughput verification** of counterparties (e.g., is that "product" actually re-refined sanctioned crude?) — a hard, today-problem in European trading houses. Model: government dossier-credit subscription + per-desk intel feed (€k/month).

**5. 48-Hour Prototype Scope**
- One AOI, oversampled NO₂ composite computed for real; plume-fit for 2–3 sources.
- E-PRTR join (public dataset, downloaded in advance) + sanctions/registry cross-match.
- **Validation-by-contrast demo**: (1) positive control — a registered EU plant matches its plume; (2) the flagged mismatch case; (3) the credibility slide — TROPOMI demonstrably sees known refinery shutdowns (post-strike outages 2024–25 are visible in the archive), proving the sensor distinguishes operational from idle.
- Auto-generated dossier (PDF + JSON) delivered to a mock case-management intake; live pull of the current day's S5P granule on stage.

**6. Biggest Risk & Likely Jury Pushback**
*"TROPOMI's ~3.5 × 5.5 km pixels can't see a hidden factory, and you'll defame a pig farm."* Defense: we publish an honest detectability floor (mid-size combustion emitters), never emit accusations — only **confidence-tiered inspection leads** where the ground inspection is the adjudicator; fusion with S2 stack/infrastructure change and S3 thermal narrows localization. Second pushback — *E-PRTR is 1–2 years stale* — is our thesis, not our weakness: the whole product exists because self-reported registries lag reality and enforcement needs a fresh, independent prior. Handled properly on the slide, both pushbacks become selling points.

---

## Idea 5 — **PlotProof**: the EUDR declarative audit API

**1. One-Line Pitch & Challenge Track**
An audit service for the **EU Deforestation Regulation**: importers upload their suppliers' plot geolocations and deforestation-free declarations; we verify every plot's land-cover history against the **Sentinel-2 archive** and return a **signed, DDS-ready due-diligence verdict per plot** in hours — the independent verifier layer for the compliance regime that has bound every EU operator of the seven covered commodities since 30 Dec 2025 (and small ones since 30 June 2026). Track: **Challenge 3** (illegal logging is transnational organized crime; we monetize the choke point where it launders into EU supply chains).

**2. Exact EU Space Data/Signal Pipeline**
- Input: supplier GeoJSON plots + declared post-cutoff-clearing status (EUDR cutoff: **31 Dec 2020**).
- **CDSE openEO** process graph over **Sentinel-2 L2A**: SCL cloud-mask → monthly composites 2018→2026 → canopy-proxy index time series per plot, cross-checked against the open JRC Tropical Moist Forest layer.
- Compute per plot: forest presence at the FAO/EUDR canopy threshold on the cutoff date; first-clearing date; then a **legal-state verdict**: *Cleared-before-cutoff* (compliant) / *Cleared-after-cutoff* (violation) / *No-forest-history* (compliant, low risk) / *Insufficient-observability* — which triggers a **Sentinel-1 VV/VH** cloud-independent fallback pass.
- Output: signed certificate + evidence bundle (timelapse chip, index series, confidence) + the JSON payload for the EU Information System due-diligence statement (mock submission in the demo). Reverse mode for authorities: scan a producing region for new clearings, diff against DDS-submitted plots → unregistered-clearing leads.

**3. Why It's NOT a Duplicate**
This is the anti-pattern executed in reverse: not "S2 + AI change-detection on a map," but **declarative audit** — verify what the supplier *claims*, per plot, mapped onto EUDR legal states, with a signed verdict and a DDS submission payload as the deliverable. The map never appears; the certificate does. Emerging EUDR vendors sell monitoring dashboards to the *same party* being audited — none sells the arm's-length auditor role with submission integration, which is exactly what authorities and financing banks require.

**4. Target Buyer & Business Model**
EU importers of coffee, cocoa, palm, soy, rubber, cattle, wood — each DDS requires geolocated plots, penalties start at **4% of total annual EU turnover**, so the buyer's pain is live *right now*. Second buyers: banks/insurers behind those shipments needing third-party pre-clearance, and member-state competent authorities (reverse mode). Pricing: per-plot verification micro-fees at import volume (thousands of plots/importer/year) + supplier-monitoring subscription — a per-transaction toll on a legally mandated pipeline.

**5. 48-Hour Prototype Scope**
- openEO pipeline over ~1,000 real plots (cocoa in Côte d'Ivoire or coffee in Vietnam — Copernicus is global, so this stays EU-space-native).
- Verdict classifier validated against JRC TMF labels; **S1 fallback** shown for a cloudy-gap plot.
- Live demo arc: audience CSV of plots dropped in → verdicts stream back in minutes → one deliberately false declaration (plot cleared in 2023, declared as pre-2020) gets caught with its evidence bundle → signed certificate + mock DDS submission. Replay of the verdict from logged input hashes closes the audit-trail loop.

**6. Biggest Risk & Likely Jury Pushback**
*"The Commission/JRC runs its own geolocation checks; smallholder plots are sub-hectare and S2 has 10 m pixels and cloud gaps — your verdicts will be shaky."* Defense, in order: the Commission's checking is the *forcing function* that makes importers pay for pre-clearance — we ride it, we don't compete with it; accuracy is handled by publishing per-plot confidence with every verdict, the S1 SAR fallback for persistent cloud, and explicit *field-check* flags for sub-resolution plots — the honesty is the product, because a verifier that overclaims is worthless in an enforcement context. And the defensible wedge: as independent verifier we have no conflict of interest — the dashboard vendors structurally cannot offer that.
