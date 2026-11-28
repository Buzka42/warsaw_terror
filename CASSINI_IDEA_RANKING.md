I couldn't save the ranking: writing `/tmp/warsaw_terror/moa_ranking.md` was blocked, because nobody can approve file writes in this non-interactive session. The full document is below; save it as `moa_ranking.md`.

Reading `/home/arawn/Projects/cassini-moa/` was also blocked, so I couldn't read `AGGREGATION_RULES.md` at all. I worked from the identically named copies in this repo instead. The expanded border-OSINT doc is committed here as `moa-raw/patryk-border-osint.md`. I applied rule 4 as your brief describes it. I had to guess at rule 5 (the truncation note); how I handled it is set out at the top of the document. Web search was also blocked, so facts I couldn't confirm are marked *(verify)*.

---

# CASSINI Warsaw 2026: MoA idea aggregation and ranking

*12th CASSINI Hackathon, EU Space for Peace and Resilience, Warsaw, 27–29 November 2026. Aggregated 28 November 2026.*

## Read this first

**Inputs.** Every file in the brief was read in full, using the copies in this repository:

| File in the brief | Copy used |
|---|---|
| `raw/glm-5.3.md` … `raw/muse-wonder.md` (6 legs) | `moa-raw/` (same names) |
| `neon-report.md`, `system-one-threat-triage.md`, `cassini_power_plant_hackathon_strategy.md` | `moa-raw/` |
| `border-osint-expanded.md` | `moa-raw/patryk-border-osint.md` (expanded version, commit ab7e637) |
| `balloon-radar-en.md` | `balloon_radar.md` |
| `last_signal.md`, `proof_of_place.md`, `gaps_and_needs.md` | repository root |

**Not counted as separate ideas:**
- `balonowy_radar.md` (the Polish original of Balloon Radar);
- the original border-OSINT seed;
- `how_it_works.md` (team explainer);
- `gaps_and_needs.md`, which was used only to check past winners.

**Rule 5 (truncation), as interpreted here:**
- The System One doc is damaged. Its formulas and several cost figures are cut off mid-sentence (for example "drops from 3/M input, $15/M output … to 432.00"). Lines ~177–528 are bare reference titles with no links. None of that was used as evidence.
- The GPT and Muse legs were re-committed as "full" versions, and the full versions were used.
- No idea lost points because a section looked thin from truncation.
- If the real rule says otherwise, re-check the entries that draw on the System One doc: #5, #6, #13, #16, #19, #26 and #29.

**Unverified facts.** Claims in the Neon and System One docs dated after mid-2026 are treated as those sources' claims, not as checked facts. That covers the KSC dates, the PLN 1.1 bn waste programme, the SENT fines, and the "System One" models (Jev, Clef) with their benchmarks. Items marked *(verify)* are my own recollection.

## How the scores work

- **Base score (0–10).** The official rubric (Relevance, Innovation & business, Execution, weighted equally), applied the way the Warsaw jury and a Demo Day panel would apply it. The Warsaw jury here means ChipCraft, IGiK, Scanway, Blue Dot and Cyber Defence Forces/WAT. Technical holes, data-access problems and buyer problems count against an idea.
- **Convergence penalty (rule 4).** An idea that many models produced is presumed to be what rival teams using AI will pitch too.
  - **By source count:** 1 source → 0; 2 → −0.5; 3–4 → −1.0; 5 or more → −2.0. The System One doc counts as half a source wherever it re-skins a Neon idea ("ChronoShield S1", "ProofOfRoute S1", "EcoForensic EO-Jev").
  - **Template penalty, −0.3 to −0.5,** when the core mechanism is one of four over-used templates:
    - (a) Sentinel-1 flood mask → dispatch, routing or payout ticket (7 ideas from 6 sources);
    - (b) Sentinel change detection along a corridor (about 5 ideas);
    - (c) Polish illegal waste (6 sources);
    - (d) an OSNMA-stamped field photo used as the "Galileo part" (a bolt-on in about a dozen ideas).
  - **Hard differentiator.** Something a rival can't copy in 48 hours would halve the penalty. None of the converged ideas has one.
- **Past-winner adjacency, −0.5.** Applied where a recent CASSINI winner did the same thing: GNSS spoofing detection, GNSS-denied navigation, satellite subsidence monitoring, flood triggers, dark vessels.
- **Final score** = base − penalties. Ties go to the idea whose core claim better survives the jury's first hard question.

**On fairness.** The four team-written ideas (Balloon Radar, Last Signal, Proof of Place, ŚLAD) were designed *after* the AI pool existed, and away from it, so they escape the convergence penalty almost by construction. That's a real advantage: rivals won't have them. But they've also been stress-tested less, so their problem lists are longer, not shorter. The penalty has a mirror-image risk too: if no model proposed an idea, the models may have had good reason to avoid it.

## Plain-language glossary

- **OSNMA:** Galileo's free signature on its navigation messages.
  - It proves the message *content* came from Galileo.
  - It does **not** prove the signal wasn't recorded and replayed or delayed.
  - It does nothing against jamming.
- **Meaconing:** recording real satellite signals and re-broadcasting them later or somewhere else. It passes OSNMA.
- **Sentinel-1:** EU radar satellite. It sees through cloud and at night, with about 20 m detail. A spot in Poland gets a few looks a week, but the same viewing angle only every 6 days.
- **Coherence and InSAR:** ways of comparing two radar passes.
  - Coherence drops when the ground changes, for example from digging or traffic. It also drops with rain, snow, frost and vegetation.
  - InSAR measures millimetre movement, but only on hard, stable surfaces (concrete, rock, buildings). It fails on grass, fields and forest.
- **Sentinel-2:** optical imagery, 10 m detail, every few days. It is blind under cloud, which in Poland means most of November.
- **Sentinel-3:** 300 m water colour and 1 km heat and fire pixels.
- **Sentinel-5P:** air pollution, with pixels of about 5.5 × 3.5 km.
- **EGMS:** ready-made Copernicus ground-movement maps for all of Europe, updated about once a year.
- **CEMS / EFAS / GFM:** Copernicus emergency products: rapid flood maps after an activation, flood forecasts, and automatic flood extent.
- **EWSS / CAMF:** Galileo's Emergency Warning Satellite Service and its 122-bit alert format, which targets one ellipse.
- **C2PA:** the industry standard for tamper-evident "content credentials" in photos.
- **NIS2 / KSC, CER:** the EU cyber-incident law and its Polish version (24-hour early warning), and the EU critical-entity resilience law.

## Convergence map

Source tags: **GLM, DeepSeek, Kimi, Qwen, GPT, Muse** are the six raw legs. **Neon** is the neon report, **S1** is the System One doc, **Plant** is the power-plant guide, and **Team** means the team's own design docs.

| Concept | Sources | Count |
|---|---|---|
| OSNMA timing integrity + NIS2 evidence | GLM ChronoMesh, DeepSeek ChronoSeal, Kimi ClockEvidence, Qwen CERTUS, GPT ClockWitness, Muse TimeSeal, Neon ChronoShield, S1 PNT-Triage, Plant (timing layer) | 9, including all six raw legs |
| Illegal-waste triage | Neon EcoForensic, S1 WasteTriage, Kimi DIWASS Crosscheck, GPT WasteDocket (same core in Qwen Veritrace and Muse WasteAlibi) | 6 |
| Flood mask → dispatch / routing / trigger | DeepSeek GridWade, Kimi ReCell, Kimi AccessSure, GPT PumpSlot, Muse BridgePass, Neon BlackoutBridge, GLM Parametra (IntakeGuard partly) | 7 ideas, 6 sources |
| Rail manifest vs radar | Qwen TorGuard, Muse RailManifest | 2 |
| Levee InSAR | GLM WałWatch, Qwen GruntWatch (Neon partly) | 2–3 |
| Parametric flood triggers | GLM Parametra, Kimi AccessSure | 2 |
| Drinking-water intake | DeepSeek IntakeGuard, Muse IntakeGuard (same name, arrived at independently) | 2 |
| EO provenance gate | Kimi SentinelGate, GPT OrbitReceipt | 2 |
| Corridor sabotage triage | Neon CorridorGuard, S1 CER-Triage | 1.5 |
| Overland sanctions / tachograph | Neon ProofOfRoute, S1 SanctionGate | 1.5 |
| Subsea cable watch | Qwen Baltic Corridor, S1 BalticCable-Triage (which S1 itself rejects) | 1.5 |
| Everything else | one source each | 1 |

The Kłodzko 2024 flood is the demo case in about a dozen ideas, two of them the team's. Expect the jury to see it several times on Sunday.

## Ranked table

| Rank | Idea | Track | Sources | Score /10 | One-line verdict |
|---|---|---|---|---|---|
| 1 | **Last Signal**: Galileo EWSS alert targeting + reference receiver | C2 (C1 link) | Team | **7.4** | Most original and very buildable; the risk is who pays, not the tech |
| 2 | **Balloon Radar**: smuggling-balloon drift forecast for ATC and border guards | C3 | Team | **7.0** | Most memorable live demo; thin EU-space content and an ATC safety-case wall |
| 3 | **Proof of Place**: Galileo/EGNOS/Copernicus seal for crisis media | C2 (C1 link) | Team (spine from Qwen) | **6.5** | Best all-three-systems story; OSNMA can't stop replay, and the satellite check often says "no data" |
| 4 | **ŚLAD**: border patrol leads from repeated ground disturbance | C3 | Team (Patryk) | **5.5** | Best of the change-detection family; Polish security forces' own traffic is the strongest signal |
| 5 | **ProofOfRoute / SanctionGate**: tachograph OSNMA + radar vs sanctions evasion | C3 | Neon, S1 | **5.2** | Great business, broken core claim; pivot to SENT jamming-gap evidence |
| 6 | **OSNMA timing integrity + NIS2 evidence** (ChronoShield and 8 twins) | C1 | All 6 legs + Neon, S1, Plant | **4.9** | The idea every AI-assisted rival brings; no hard differentiator anywhere |
| 7 | **BridgePass**: bridge GO/NO-GO for heavy convoys | C2 | Muse | **4.7** | Strong demo, but the satellite can only ever say "check" |
| 8 | **GhostStack**: Sentinel-5P emitters vs registries | C3 | GLM | **4.5** | Original science; what it can see, commercial players already see |
| 9 | **GhostWorks**: satellite audit of EU-funded works | C3 | DeepSeek | **4.4** | Tidy EO product in the wrong challenge; most fraud is indoors |
| 10 | **Rail manifest reconciliation** (TorGuard / RailManifest) | C3 | Qwen, Muse | **4.3** | Great border story; the terminal already knows more than the satellite |
| 11 | **VeriTerra**: physics checks for faked satellite images | C1 | DeepSeek | **4.2** | Right question, wrong resolution |
| 12 | **Levee InSAR → work orders** (WałWatch / GruntWatch) | C2 | GLM, Qwen | **4.1** | Radar can't see into grass levees; EGMS and a past winner cover the rest |
| 13 | **Illegal-waste inspection triage** (EcoForensic and co.) | C3 | Neon, S1, Kimi, GPT (+Qwen, Muse) | **4.0** | Hot news hook, six sources, and the waste sits inside warehouses |
| 14 | **IntakeGuard**: drinking-water intake closure | C2 | DeepSeek, Muse | **3.9** | The utility's own river sensors beat the satellite |
| 15 | **Parametric flood triggers** (Parametra / AccessSure) | C2 | GLM, Kimi | **3.8** | Right output, saturated market; the revisit misses flash floods |
| 16 | **CorridorGuard (+ CER-Triage)** | C2 | Neon, S1 | **3.7** | Too slow for sabotage; incumbents own pipeline monitoring |
| 17 | **EO provenance gate** (SentinelGate / OrbitReceipt) | C1 | Kimi, GPT | **3.6** | Correct and boring: nobody has been attacked this way |
| 18 | **GridWade**: flood-to-grid switching playbook | C2 | DeepSeek | **3.6** | Utilities won't share the network data it needs |
| 19 | **CrisisVerif**: AI triage of crisis posts vs Copernicus | C2 | S1 | **3.5** | A Proof of Place feature built on unverifiable AI models |
| 20 | **Veritrace**: court-ready evidence chain for waste crime | C3 | Qwen | **3.5** | Good evidence spine inside the most crowded domain |
| 21 | **ReCell**: mobile-network restoration dispatch | C2 | Kimi | **3.5** | An operator's internal planning problem |
| 22 | **PumpSlot**: flood-pump mutual-aid dispatch | C2 | GPT | **3.4** | Safe to build, nothing to win; flood maps arrive too late |
| 23 | **PlotProof**: EUDR deforestation audit API | C3 | GLM | **3.3** | A real business in the wrong room, in a crowded market |
| 24 | **AirShift**: crew rescheduling during smoke episodes | C2 | GPT | **3.0** | A productivity feature, not resilience |
| 25 | **Power-plant cyber-physical check** | C1 | Plant | **2.9** | The grid operator knows within seconds that a plant tripped; satellites add nothing |
| 26 | **SatSOC-Triage**: satellite telemetry triage | C1 | S1 | **2.9** | Tiny Polish market, research data only |
| 27 | **WasteAlibi**: OSNMA vs truck alibis | C3 | Muse | **2.8** | An unauthenticated log doesn't put the truck at the dump |
| 28 | **BlackoutBridge**: GNSS-denied offline crisis routing | C2 | Neon | **2.6** | Two crises glued together; offline maps already exist |
| 29 | **Baltic Corridor (+ BalticCable-Triage)** | C2 | Qwen, S1 | **2.5** | The banned dark-vessel category with a new label |

---

## Idea sections

### 1. Last Signal: Galileo EWSS alert targeting + reference receiver
**Challenge 2 (C1 link) · Team doc only; no AI leg touched EWSS · 7.4 (base 7.4, no penalty)**

**What it is.** Galileo's new Emergency Warning Satellite Service can push a short alert straight to phones when mobile towers are down. But each alert is only 122 bits, and it can target only one coarse ellipse. Last Signal turns Copernicus flood or fire data plus population data into the best ellipse(s), meaning exactly who to warn. It encodes the alert in the official format and adds an open decoder that reads it from Galileo navigation data on an Android phone.

**Pluses**
- **Zero convergence.** None of the ~45 AI-generated ideas uses EWSS, so rivals working from the same models won't land here.
- **EUSPA wants it.** EWSS is the newest Galileo service and EUSPA wants it adopted, which suits the EUSPA and EC judges at European Demo Day.
- **A Polish story that tells itself:** Kłodzko Valley, September 2024, towers down, and a Sejm interpellation saying telecom failures crippled crisis management.
- **A real, measurable problem at the core.** Squeezing a long, thin river-valley hazard into a coarse ellipse forces a trade between coverage and needless warnings. That produces hard slide numbers: "96% of at-risk people covered, X fewer warned needlessly."
- **The output is an action:** a send-ready alert plus a CAP message, not a map. ChipCraft-type chip designers have a direct business interest in a reference decoder and test vectors.
- **Very buildable in 48 h:** a bit-packing codec, a grid-search optimiser, a public population grid and archived EMS flood outlines.

**Minuses and limitations**
- **EWSS may not broadcast alerts yet** (it's in testing or approaching initial service, *verify*). The demo injects alerts into recorded logs, and a sceptic will call it "simulated".
- **No phone shows EWSS alerts today.** It needs chipset firmware, operating-system support, and a GNSS receiver that is actually running. Mass-market reception is years away, so the citizen-impact claim is a 2028-plus claim.
- **Weak buyer.** EWSS is free to authorities, and Polish civil protection (RCB) buys slowly. The better buyers are public-warning-system vendors and chipset makers, selling through them to government.
- **Biggest unknown.** If the EWSS ground segment or the national alert gateway already converts CAP polygons into CAMF ellipses, the optimiser becomes a feature rather than a product. Check this first.
- **Copernicus inputs are a bottleneck:**
  - EFAS real-time forecasts are restricted to partner authorities.
  - EMS rapid maps arrive hours to a day after the event, too late for the first warning.
  - The population grid (100 m) is coarse for small valley towns.

**Known problems**
- **The integrity section over-promises.** As specified, OSNMA signs navigation words (orbits, clocks, time), not the return-link field the alert travels in. "OSNMA OK" therefore does not authenticate the alert. Say that authentication is EUSPA's mechanism and that you only run consistency checks.
- **Kłodzko 2024 is everyone's demo.** Open with the towers-down moment, and add a second hazard (a dam break or a Seveso chemical plant) so the demo doesn't blur into five other Kłodzko replays.
- **The receiver depends on the phone.** Whether GnssLogger logs Galileo navigation pages varies by phone. Test tonight, or the receiver half becomes "decoder on synthetic bits".

**Bottom line:** the best ratio of originality to feasibility in the pool. Its risk is commercial, not technical.

---

### 2. Balloon Radar: smuggling-balloon drift forecast
**Challenge 3 · Team doc (Polish original not double-counted) · 7.0 (base 7.0, no penalty)**

**What it is.** Balloon Radar forecasts where cigarette-smuggling balloons launched from Belarus will drift. It runs 500 simulated flights through Copernicus wind data to cover their unknown altitude and lift. Air traffic control gets a conflict probability and a targeted closure window for the approach corridor. Border guards get a landing area and a patrol app that checks Galileo OSNMA status.

**Pluses**
- **No AI leg proposed it**, and the hook is unforgettable: Vilnius airport closed for about 11 hours by balloons, and the Border Guard confirmed balloons reaching Podlasie.
- **A live, falsifiable demo.** Predict the Legionowo radiosonde (12 UTC launch) and show the real landing during the pitch. Few teams will risk a live prediction, and it reads as confidence.
- **Decision outputs** (closure window, dispatch ticket) that match the "early warning" pattern of past winners.
- **Hybrid-threat framing** that suits the Warsaw security jury.

**Minuses and limitations**
- **The detection input isn't yours.** Radar tracks belong to the air navigation provider or the military, and the demo uses incident reports. Expect: "your product starts after the hard part."
- **Safety-case wall.** An air navigation provider can't operationally use a new tool to shorten closures without a safety assessment under EU air-traffic rules (Reg. 2017/373). Frame it as decision support for the supervisor.
- **Thin EU-space content.** The engine runs on wind fields: ERA5 for replay, and possibly ECMWF open data for the live forecast, which is not formally Copernicus. Land cover comes from CLMS. There is no Sentinel anywhere, and Galileo/EGNOS is a patrol bolt-on. A jury that equates Copernicus with satellites will mark Relevance down.
- **A tiny market:** a handful of air navigation providers, airports and border-guard units, and the problem depends on Belarus's behaviour.
- **The flight profile is unknown.** Smuggling-balloon altitude, lift and release behaviour are guesses until recovered balloons calibrate them.

**Known problems**
- **The saving may vanish on the worst nights.** With dozens of balloons in the air, the chance that at least one hits the corridor is close to 100% for hours. Honest uncertainty can erase the closure saving on exactly the nights that made headlines. Run the replay before putting any number on a slide.
- **A radiosonde validates only the winds.** It bursts at ~30 km, so it tests the wind model, not the smuggling profile. Say so before a juror does.
- **EGNOS on a phone adds little.** Phone measurements are noisy at the metre level, and a phone "protection level" isn't certified, so "holds up in court" is an overclaim.
- **Two dependencies are still unconfirmed:** whether CAMS publishes winds on pressure levels, and whether your phones log Galileo navigation messages. OSNMA also needs minutes from a cold start before the first authentication.

**Bottom line:** the most memorable demo in the pool. Lead with the replay numbers and be first to say what you don't know.

---

### 3. Proof of Place: Galileo/EGNOS/Copernicus seal for crisis media
**Challenge 2 (C1 link) · Team doc. Sealing spine from Qwen Veritrace; claim-check overlaps S1 CrisisVerif and DeepSeek VeriTerra · 6.5 (base 6.8, −0.3 for the OSNMA-photo template)**

**What it is.** A capture app and verifier that seals disaster photos and videos with three things:
- a Galileo OSNMA-authenticated place and time;
- an EGNOS error estimate;
- an automatic Copernicus check that the claimed flood or fire was actually observed nearby.

A "claim-check" mode lets fact-checkers test viral footage that was never sealed.

**Pluses**
- **Uses all three EU systems, each for a real job.** The Cyber Defence Forces, who are in the room, publicly called the 2024 flood disinformation an information operation.
- **A verdict plus a cryptographic seal, not a map.** The honest three-way verdict (consistent / inconsistent / no observation) will impress IGiK.
- **Tailwinds:** AI Act Article 50 labelling since August 2026, and C2PA in mainstream phones.
- **Value from day one:** claim-check mode works without anyone installing the app.
- **Shared GNSS backend with Balloon Radar,** so phone work tonight counts twice.

**Minuses and limitations**
- **OSNMA doesn't stop replay.** Anyone who records real Galileo signals at the claimed place with a cheap software radio can replay them, and only timeliness checks limit this. It works against casual fakers, not against a state operation.
- **Patchy phone support.** Many phones don't expose Galileo navigation messages. From a cold start, the first authenticated fix takes minutes, so the app must be running before the shot. That's a real UX problem in a flood.
- **The Copernicus check will mostly say "no observation".** Sentinel-1 sees a spot only a few times a week, flood maps lag, and Sentinel-3 fire pixels are 1 km. "Copernicus confirms" will be rare.
- **Adoption chicken-and-egg.** Disinformation producers never seal, and citizens won't install a new app mid-crisis. The real users are professional capturers: newsroom photographers, insurance adjusters, responders.
- **An established competitor.** Truepic-style "controlled capture" already sells verified place-and-time photos to insurers, and newsrooms have little money.

**Known problems**
- **The 2024 disinformation was mostly real footage re-captioned.** A seal helps only if honest content is sealed at the source, so the claim-check mode has to carry the pitch.
- **±4 m from EGNOS on phone data is optimistic.** Server-side EGNOS on phone measurements is weak.
- **GFM API access is unverified.** The fallback is your own Sentinel-1 water mask.

**Bottom line:** the strongest all-three-systems story. Win with a live claim-check on the real Poland-footage-sold-as-Valencia clip, and state the replay limit before ChipCraft does.

---

### 4. ŚLAD: border patrol leads from repeated ground disturbance
**Challenge 3 · `border-osint-expanded` (Patryk's seed, expanded) · 5.5 (base 6.0, −0.5 change-detection template)**

**What it is.** ŚLAD finds spots near the Poland–Belarus border where Sentinel-1 radar shows ground disturbance repeating week after week. It keeps only spots on routes that a terrain model says link the border to an inland pickup road, after filtering out farming, logging, weather and construction. The output is a ranked weekly patrol-lead queue for Border Guard tools (TAK/KML). Field confirmations stamped with OSNMA feed back as training labels.

**Pluses**
- **Honest physics:** "we don't detect footpaths." Persistence plus a route model plus suppression is a genuine analytic idea, not before/after change spotting.
- **A great answer to "isn't this just change detection?"** The funnel slide: 8,400 changed cells → 9 leads on corridors.
- **A funded buyer** (Border Guard, East Shield at ~PLN 10 bn, EU border funds) and strong local resonance.
- **The radar-backscatter path through openEO is very doable in 48 h.**

**Minuses and limitations**
- **Too slow to interdict.** A few looks a week makes this weekly pattern intelligence, not real time, and military jurors will push on it.
- **Forest and winter defeat the radar.** Białowieża forest is opaque to this radar. Late-November snow, freeze-thaw and wet ground scramble coherence across whole regions.
- **Can't be validated in 48 hours.** When the jury asks "how many of your 9 leads are real?", the honest answer is "unknown".
- **Slow, small market.** Procurement goes through integrators, and the doc's own estimate is ~€2.5–4 M ARR across the EU's eastern frontier.
- **Ethics at Demo Day.** Pushbacks and deaths in the forest are a live EU controversy. An EC/EUSPA panel may balk at a tool that sends patrols toward migrant routes, even framed as smuggling and rescue.

**Known problems**
- **The security forces' own traffic is the strongest signal.** The most persistent disturbance on border corridors is the security apparatus itself: patrol tracks along the barrier, military operations, East Shield works and service roads. These pass the "persistent and on a corridor" filter by construction. Removing them needs a map of security-force routes, which no hackathon team will get.
- **Wild boar and local traffic survive the filters.**
- **Coherence processing is only a stretch goal.** Backscatter alone is much less sensitive.
- **It's the same engine as CorridorGuard and TorGuard.** Submit only one change-detection project.

**Bottom line:** the best of the change-detection family, but still in it. Treat it as the fallback if the team has a radar specialist.

---

### 5. ProofOfRoute / SanctionGate: tachograph OSNMA + radar vs sanctions evasion
**Challenge 3 · Neon (ProofOfRoute), S1 (SanctionGate, a derivative) · 5.2 (base 5.5, −0.3)**

**What it is.** A compliance API for exporters, forwarders and cargo insurers that checks whether a truck really drove the declared route. It uses Galileo-authenticated positions from mandatory EU smart tachographs, plus Sentinel-1 checks of transshipment yards near the eastern border. The output is pass / review / high-risk with an audit certificate. The S1 version adds AI triage and Polish SENT appeal packs.

**Pluses**
- **A non-obvious data source.** OSNMA is already built into mandatory tachographs, so no new hardware is needed.
- **Pure business-to-business, EU-wide.** Sanctions liability (the No-Russia clause, re-export via Central Asia) makes this the strongest European Demo Day business story in the pool.
- **Low convergence.** None of the six raw legs found it.
- **A hidden gem: Polish SENT-GEO.** Carriers face PLN 10,000 fines for GPS data gaps, often caused by jamming (per S1, *unverified*). A "this gap was jamming" evidence pack for carriers is a concrete, local, cash pain.

**Minuses and limitations**
- **Tachographs don't record a continuous signed track.** They store authenticated positions only at events: start and end of the working day, roughly every 3 hours of driving, border crossings, and loading or unloading *(verify)*. Neon's "per-second OSNMA truck tracking" is wrong, and a GNSS juror will know it.
- **Wrong data owner.** Tachograph files belong to the carrier and to roadside control. An exporter or insurer gets them only if the carrier cooperates, and the carrier is the party being audited.
- **The radar part is decorative.** 20 m radar every few days can't tie a truck cluster in a Belarusian yard to a specific shipment.
- **The fraud mostly doesn't look like this.** Re-export via Central Asia usually means the goods really arrive and then move on paper. "Spoofed GPS detour into Belarus" is a minority case.
- **The demo will be synthetic.** Real tachograph files carrying OSNMA flags are unlikely to be obtained in 48 hours.

**Known problems**
- **"OSNMA broke for 6 hours" is also what ordinary jamming in Podlasie looks like.** The signal alone can't separate crime from the environment.
- **The S1 variant puts an AI classifier inside a sanctions decision.** Its own cited studies report 46–92% decision flips under text injection. A cyber jury will use that.

**Bottom line:** good business, broken core claim. If chosen, pivot to SENT-gap evidence packs, where tachograph and jamming evidence actually fit.

---

### 6. OSNMA timing integrity + NIS2 incident evidence
**Challenge 1 · GLM ChronoMesh, DeepSeek ChronoSeal, Kimi ClockEvidence, Qwen CERTUS, GPT ClockWitness, Muse TimeSeal, Neon ChronoShield, S1 PNT-Triage, Plant (layer 1): 9 sources · 4.9 (base 7.4, −2.0 convergence, −0.5 past-winner adjacency)**

**What it is.** Software that watches the GNSS-driven clocks used by substations, 5G sites and trading systems. It checks Galileo OSNMA signatures and compares GNSS time against an independent clock (holdover oscillator, PTP peers, e-CzasPL). When they disagree it switches to holdover and writes a signed incident record pre-filled for the 24-hour NIS2/KSC early warning.

**Pluses**
- **The cleanest Challenge 1 fit in the pool,** with real pain (Baltic jamming, microsecond timing budgets in 5G and grid sensors) and real regulatory pull.
- **Demoable without hardware:** OSNMAlib, public Jammertest recordings and simulated clocks. GPT's honest version is technically excellent: "the message authenticated, but the clock is still wrong."
- **The Warsaw jury (ChipCraft, Cyber Defence Forces) can validate it.**

**Minuses and limitations**
- **Maximum convergence.** It's the #1 pick of GPT, Muse, Neon and S1, and it appears in every raw leg. Any team that asked an AI for Challenge 1 ideas has this exact pitch: the same buyers, the same NIS2 slide, the same "inject spoof → screen goes red" demo.
- **OSNMA doesn't stop meaconing or delay attacks** (every leg admits it). All the real detection comes from the independent-clock comparison, which timing appliances already do.
- **Vendors already ship it:** OSNMA-capable timing receivers (Septentrio, u-blox) and "GNSS firewall" and multi-source timing products (Microchip BlueSky, Safran/Orolia, Meinberg).
- **The auto-NIS2 report is a PDF template.** A GNSS anomaly isn't automatically a reportable significant incident; a human decides that.
- **Past-podium adjacency.** GNSS spoofing detection placed 3rd at a recent defence edition, and the Polish 5 November webinar was about GNSS interference, so this track will be crowded.

**Known problems**
- **Internet NTP is far too coarse.** Several legs use e-CzasPL or NTP over the internet as the independent reference. That is accurate to milliseconds and useless against microsecond attacks, and a GNSS juror will catch it. The reference has to be a local oscillator or PTP over fibre.
- **OSNMA assumes loose time already.** Its security assumes the receiver knows the time to within a loose bound (seconds), so it can't certify the microseconds that grids and 5G need.
- **The demo will look like everyone's.** Live spoofing at the venue would be illegal radio transmission, so the demo is recorded data, the same as every rival's.
- **No leg offers a hard differentiator.** A real OSNMA timing receiver plus a real oscillator on the table would be one, but that isn't realistic in 48 hours.

**Bottom line:** the idea every rival brings. Only pick it with real timing hardware on the table.

---

### 7. BridgePass: bridge GO/NO-GO for heavy convoys
**Challenge 2 · Muse · 4.7 (base 5.2, −0.5 flood-routing template)**

**What it is.** A routing service that tells fire-service and military logistics whether a 30–44 t convoy can cross specific bridges after a flood. It uses Copernicus EGMS ground-movement history plus fresh Sentinel-1 change on bridge decks and approaches. Red bridges are removed and the route recalculates.

**Pluses**
- **Clear yes/no output** and a strong live demo: close a bridge and the route changes.
- **Military mobility and heavy-vehicle bridge capacity** are hot NATO and Polish topics.
- **EGMS gives movement history without running InSAR yourself.** Single source.

**Minuses and limitations**
- **EGMS is a peacetime baseline,** updated about once a year, not crisis information.
- **The post-flood radar check is slow and vague.** There are a few looks a week, and coherence over moving water is poor. Scour at the piers, the real flood failure mode, is underwater and invisible.
- **It can only ever say "check".** Road authorities inspect key bridges after every major flood anyway, and the system has no authority to say "safe".
- **Slow buyers** (fire service, Territorial Defence, the national roads authority GDDKiA). Closures come from road authorities and police, not satellites.

**Known problems**
- **Old data for a 2-hour decision.** "Can this pumper get there in 2 hours?" is answered with data that is days old.
- **Routing around floods is a standard hackathon pattern.** The bridge-InSAR angle is the only differentiator, and it's also the weakest part technically.

**Bottom line:** a great demo with thin satellite value. Engineers on site make the real decision.

---

### 8. GhostStack: Sentinel-5P emitters vs registries
**Challenge 3 · GLM · 4.5 (base 4.5, no penalty)**

**What it is.** GhostStack averages months of Sentinel-5P air-pollution data to locate industrial emission sources. It then compares them with emission registers, permits and sanctions lists. It flags sites that emit like industry but don't officially exist, and sanctioned sites that keep running, and outputs enforcement dossiers.

**Pluses**
- **Uses the Copernicus mission almost no team touches,** with real science that IGiK will respect.
- **A credible visual:** refinery shutdowns after drone strikes are visible in the archive.
- **A legal hook** in the new Environmental Crime Directive. Single source.

**Minuses and limitations**
- **The detection floor kills the main thesis.** Pixels are ~5.5 × 3.5 km, and even after months of averaging only big emitters stand out. A hidden illegal factory or a waste fire sits far below that floor.
- **Prior art.** Published TROPOMI point-source catalogues already find sources missing from inventories, and commercial firms (Kayrros and others) sell refinery-activity intelligence to trading desks.
- **Too slow to enforce:** it needs 30–90 days of data per answer.
- **Weak Polish relevance and buyer.**

**Known problems**
- **Cities swamp industry.** Traffic and city NO₂ dominate in Poland, so the risk of wrongly accusing a site is real.
- **Validation isn't feasible in 48 hours.**

**Bottom line:** smart and original, but whatever it can see, others already see better.

---

### 9. GhostWorks: satellite audit of EU-funded works
**Challenge 3 · DeepSeek · 4.4 (base 4.4, no penalty)**

**What it is.** GhostWorks takes public lists of EU-funded construction projects (cohesion funds, recovery funds/KPO) with declared locations and milestones. It checks Sentinel-1/2 time series to see whether anything was actually built, and ranks anomalies into case files for EPPO, OLAF and NIK.

**Pluses**
- **Starts from the money** and uses satellites as an independent check, a clear workflow.
- **Politically hot:** KPO money is under scrutiny (for example the 2025 HoReCa grant scandal), and EPPO's caseload is growing.
- **The EO part is feasible:** bare soil turning into a building over months is visible.

**Minuses and limitations**
- **Off-theme.** "Fraud against the EU budget" stretches "transnational crime and terrorism", so expect a lower Relevance score.
- **Most fraud is invisible from orbit:** invoices, equipment, renovations, interiors. The HoReCa yachts and saunas are exactly the kind of thing satellites can't see.
- **Location data is poor.** Project coordinates are often missing, or point to an office address.
- **Existing tools.** The Commission's ARACHNE tool and national auditors already do risk scoring, and these buyers procure slowly.

**Known problems**
- **Defamation risk** if a real project is flagged on stage.

**Bottom line:** a tidy EO product in the wrong hackathon.

---

### 10. Rail manifest reconciliation (TorGuard / RailManifest)
**Challenge 3 · Qwen, Muse · 4.3 (base 4.8, −0.5)**

**What it is.** It watches the rail yards at the Belarus/Ukraine gauge-change terminals (for example Małaszewicze) with Sentinel-1, estimating how many trains are present and for how long. It compares that with customs manifests, and mismatches become inspection-hold tickets for customs (KAS/OLAF).

**Pluses**
- **Turns the banned dark-vessel cliché into a land version,** with immediate Polish geopolitical relevance.
- **Customs inspect only a small share of trains,** so better prioritisation is a real need.
- **Rail yards are bright radar targets,** so detecting whether a train is present, and for how long, is roughly feasible.

**Minuses and limitations**
- **It can't link what it sees to a manifest.** 20 m pixels every few days over a yard full of wagons show total occupancy, not which train is which.
- **The fraud is in the contents** (relabelled goods, dual-use items), and radar can't see contents.
- **The ground already knows more.** The terminal operator and the railway know exactly which wagons are where, and customs can get that data by law. The satellite delivers a worse copy of information that already exists on the ground.
- **Manifests are confidential,** so they'll be mocked. Qwen's wagon-counting detector contradicts the legs' own later "we never count wagons".

**Known problems**
- **Congestion looks like fraud.** A congested yard, as during the 2025 border closures, produces "present for 6 days against 24 h declared" with no fraud at all.
- **Two models converged,** so expect a rival with the same Małaszewicze pitch.

**Bottom line:** a great story, but the ground knows more than the satellite.

---

### 11. VeriTerra: physics checks for faked satellite images
**Challenge 1 · DeepSeek · 4.2 (base 4.2, no penalty)**

**What it is.** VeriTerra is an intake filter that scores satellite images for tampering or AI fabrication. It checks:
- shadows against the sun angle and terrain;
- optical "new structures" against Sentinel-1 radar history;
- editing artefacts.

It also hashes and signs genuine Copernicus products at download.

**Pluses**
- **A real, rising problem:** fake satellite images circulated in recent conflicts.
- **Not change detection,** and a fit for C1's "integrity of space data".
- **A genuinely good cross-sensor check:** an optical claim tested against radar history.

**Minuses and limitations**
- **Wrong resolution for the fakes that matter.** Those are high-resolution commercial images of a hangar or a ship. At Sentinel's 10–20 m, a building's shadow is 1–3 pixels, so the physics checks only work for large claims.
- **An arms race.** "Deepfake detection is an arms race" is a fair pushback, and artefact detectors go stale.
- **Poor buyers:** OSINT desks and newsrooms have little money, and insurers rarely receive satellite images as evidence.

**Known problems**
- **Hashing at download proves very little.** It shows only that you got what CDSE served, which overlaps with #17.

**Bottom line:** the right question at the wrong resolution.

---

### 12. Levee InSAR → work orders (WałWatch / GruntWatch)
**Challenge 2 · GLM, Qwen (Neon partly) · 4.1 (base 5.1, −0.5 convergence, −0.5 past-winner adjacency)**

**What it is.** It uses Sentinel-1 interferometry (millimetre ground movement) and coherence along flood embankments and dams to rank segments by risk. It pushes inspection work orders into the operator's maintenance system (Wody Polskie) before the next flood.

**Pluses**
- **Prevention, not post-disaster mapping,** with a ticket as the output and the 2024 flood in recent memory.
- **IGiK respects rigorous InSAR.**
- **A buyer with budget:** post-2024 reconstruction money and the CER law.

**Minuses and limitations**
- **The radar can't see into grass levees.** Earthen levees are grass-covered, and this radar loses coherence on vegetation. It measures concrete structures and roads crossing the levee, not the earth fill that actually fails.
- **Largely already done.** EGMS publishes free movement maps for all of Europe, and incumbents (TRE Altamira, SkyGeo, Detektia) plus Dutch dike-monitoring services exist.
- **Heavy processing.** Running 15+ radar scenes through SNAP in 48 hours is risky, and atmospheric noise swamps millimetre signals on short stacks.
- **Slow procurement and a past-winner neighbour.** Wody Polskie buys slowly, and Viadrus (satellite subsidence and leak prediction) won recently and is in the room.

**Known problems**
- **Qwen's Stronie Śląskie claim is unsupported.** The dam failed during an extreme overtopping event. Keep "measurable precursors" off the slides.
- **It watches for the wrong failure.** Levees fail through overtopping, seepage and piping during high water. Those are fast processes that slow deformation monitoring mostly misses.

**Bottom line:** credible science aimed at a failure mode that isn't the one that breaks levees.

---

### 13. Illegal-waste inspection triage (EcoForensic, WasteTriage, DIWASS Crosscheck, WasteDocket)
**Challenge 3 · Neon, S1, Kimi, GPT, with the same core in Qwen and Muse (6 sources) · 4.0 (base 6.0, −2.0)**

**What it is.** It combines Sentinel-1/2 time series over industrial plots, quarries and permitted waste sites with Poland's waste registry (BDO) or the EU's waste-shipment records (DIWASS). It flags sites where physical activity doesn't match the paperwork and produces inspection packets for the environmental inspectorates (GIOŚ/WIOŚ).

**Pluses**
- **A very current hook:** the PLN 1.1 bn clean-up programme announced days before the event (per Neon).
- **A Europol priority** with a clear buyer.
- **A real-data EO demo is doable,** and the triage framing is honest.

**Minuses and limitations**
- **Six sources, plus a headline any team will read.** Expect several rivals pitching this.
- **The waste is indoors.** The Polish "waste bomb" model is rented warehouses and halls. Satellites only see open-air dumps.
- **10–20 m pixels can't tell waste from gravel, timber, compost or aggregate,** and ploughing, quarrying and construction cause most of the change.
- **The registries aren't open.** BDO isn't openly queryable and DIWASS isn't public (GPT and Kimi say so), so the registry side will be mocked.
- **The buyer may already have it.** GIOŚ already partnered with the Polish Space Agency on Sentinel imagery (per S1).

**Known problems**
- **Neon's "pre-arson heating" claim is physically implausible.** Sentinel-3's 1 km pixels can't see it at a few-hectare dump.
- **Neon overreaches on precision.** "Exact start week" and "court-admissible" claims ignore cloud gaps.

**Bottom line:** a good problem, crowded and half invisible.

---

### 14. IntakeGuard: drinking-water intake closure
**Challenge 2 · DeepSeek, Muse (same name, independently) · 3.9 (base 4.4, −0.5)**

**What it is.** It predicts when a flood-driven turbidity or pollution plume will reach a drinking-water intake. It combines Sentinel-1 flood extent, Sentinel-2/3 water-colour proxies and a simple river travel-time model, then issues a "close the intake at hour X" decision pack with a draft public notice.

**Pluses**
- **A clear, accountable decision** backed by real liability and the Drinking Water Directive's risk-planning duty.

**Minuses and limitations**
- **The satellites can't see the river properly.** Sentinel-3's 300 m water-colour pixels are wider than most Polish rivers. Sentinel-2 is clouded out during floods and gives only relative turbidity on narrow rivers.
- **The utility's own sensors do this better.** Utilities already have turbidity sensors at and upstream of their intakes, plus national gauge data, and those are faster and more accurate.
- **Turbidity is not toxicity.** The dangerous events aren't turbidity plumes, for example a chemical spill or the 2022 Odra golden-algae disaster driven by salinity.

**Known problems**
- **Muse's Warsaw example fits badly.** Gruba Kaśka is a riverbed infiltration intake that filters through sand, so "close the intake at noon" doesn't suit it.
- **A rival may literally pitch "IntakeGuard".** Two models produced the same name.

**Bottom line:** the utility's own sensors beat the satellite at this job.

---

### 15. Parametric flood triggers (Parametra / AccessSure)
**Challenge 2 · GLM, Kimi · 3.8 (base 4.8, −0.5 convergence, −0.5 past-winner adjacency)**

**What it is.** It turns Sentinel-1 flood detection (and Sentinel-3 fire data) into signed, replayable payout triggers for insurers, anticipatory-aid funds and municipalities. Kimi's variant pays out when a specific access road goes under water.

**Pluses**
- **A decision that moves money,** with a smart "replay the verdict" provenance demo and real buyers.

**Minuses and limitations**
- **Commercially crowded:** Floodbase, ICEYE flood products, Descartes, and the big reinsurers' parametric desks.
- **Past-winner adjacency:** a flood-trigger team won the 11th edition (per S1).
- **The revisit misses flash floods.** Sentinel-1 can miss a peak (Kłodzko peaked within about a day), so a trigger that depends on pass timing creates basis risk, the gap between what triggers and what was actually lost.
- **Radar flood detection fails in towns,** where the insured losses are.
- **Kimi's route trigger is mostly unobservable.** Roads are about one pixel wide and often tree-lined.
- **Insurers need years of backtests** before buying.

**Bottom line:** the right output in a saturated market, with a revisit problem.

---

### 16. CorridorGuard (+ CER-Triage): linear-infrastructure sabotage triage
**Challenge 2 · Neon, S1 (CER variant; S1 rejects the unpivoted version) · 3.7 (base 4.5, −0.3 convergence, −0.5 change-detection template)**

**What it is.** It watches buffers along pipelines, railways, power lines and levees with Sentinel-1/2 for unauthorised digging, heavy machinery, leaks or subsidence. It suppresses farming and permitted works, then pushes tickets plus drone or high-resolution tasking boxes. CER-Triage applies the same idea to wind and solar sites whose SCADA was knocked out.

**Pluses**
- **A strong demo:** "142 raw alerts → 3 tickets" after suppression.
- **Tip-and-cue appeal for Scanway,** and a CER-law tailwind.

**Minuses and limitations**
- **Too slow for sabotage.** A saboteur digs and plants in hours, and the satellite comes every few days.
- **Water indices can't see buried pipeline leaks.**
- **Incumbents own this:** LiveEO (heavily funded), Orbital Eye and Viadrus already sell it, and S1 scores it lowest on saturation.
- **It's the same engine as ŚLAD.** Don't submit both.

**Bottom line:** incumbents own it.

---

### 17. EO provenance gate (SentinelGate / OrbitReceipt)
**Challenge 1 · Kimi, GPT · 3.6 (base 4.1, −0.5)**

**What it is.** Middleware that checks Copernicus-derived products before they enter an operator's automated workflow: right scene, right area, not stale, approved processing, signed provenance. Anything that fails is quarantined and ticketed.

**Pluses**
- **A genuine C1 angle** (supply-chain integrity) with honest scoping, and cheap to build.

**Minuses and limitations**
- **No demonstrated threat.** Nobody can name an incident of a substituted Sentinel scene, and buyers don't pay to stop attacks that haven't happened.
- **Generic tooling.** It's ordinary software supply-chain tooling (signatures, provenance records) applied to images, and CDSE already publishes checksums.
- **Low wow:** jurors see a green tick and a red cross.

**Bottom line:** correct and boring.

---

### 18. GridWade: flood-to-grid switching playbook
**Challenge 2 · DeepSeek · 3.6 (base 4.1, −0.5 flood template)**

**What it is.** It converts a Sentinel-1 flood map plus flood forecasts into a substation-level switching playbook and outage forecast for electricity distributors, delivered as tickets.

**Pluses**
- **Operator-facing output,** and the 2024 flood is a real reference case.

**Minuses and limitations**
- **No network data.** Distributors won't share network topology, and OpenStreetMap's medium-voltage data is incomplete.
- **Distributors already have plans.** They use the national flood-hazard maps (ISOK) and pre-planned flood procedures, and switching orders from a startup are a liability.
- **The forecast does the real work.** The flood forecast (EFAS) covers the 24–72 h horizon, while the Sentinel-1 snapshot may arrive after the water.

**Bottom line:** the forecast does the work; the satellite is a passenger.

---

### 19. CrisisVerif: AI triage of crisis posts against Copernicus
**Challenge 2 · S1 · 3.5 (base 3.5, no penalty)**

**What it is.** It triages social-media posts and citizen reports during a crisis. A new type of AI "decision model" classifies each post (dam breach, rumour, psyop). Hard checks against Copernicus EMS flood outlines, Sentinel-1 and OSNMA-stamped responder reports override the AI when the space data contradicts the post.

**Pluses**
- **A real 2024 problem,** and "space data has veto power over the AI" is a good security design.
- **Honest about satellite latency:** posts wait in a "pending pass" queue instead of being called false.

**Minuses and limitations**
- **Built on unverifiable AI models.** It depends on brand-new "System One" models (Jev, Clef) whose capabilities can't be verified here. Its own cited research reports 46–92% decision flips under text injection, and in a disinformation product the attacker writes the text.
- **Workflow mismatch.** County crisis centres handle emergency calls and official reports, not thousands of posts; social-media monitoring sits with RCB and NASK.
- **Mostly "pending" in the first day.** EMS flood maps arrive about a day after the event.
- **It duplicates Proof of Place's claim-check mode.**

**Bottom line:** a feature of #3, not a product.

---

### 20. Veritrace: court-ready evidence chain for waste crime
**Challenge 3 · Qwen · 3.5 (base 4.3, −0.5 waste-domain convergence, −0.3 OSNMA-photo template)**

**What it is.** It reconciles waste-transport registries (SENT/BDO) with Copernicus observations of disposal sites. It then packages the findings with C2PA credentials, an eIDAS qualified timestamp, a blockchain anchor and OSNMA-stamped inspector photos into a "court-admissible" bundle.

**Pluses**
- **Attacks a real bottleneck:** evidence dies in court.
- **eIDAS timestamps are legally recognised,** and the evidence spine is reusable (Proof of Place reuses it).

**Minuses and limitations**
- **Three products in one weekend:** detection, registry fusion, an evidence spine and a verification portal.
- **No added legal weight.** Courts rely on expert witnesses and standard procedure, so C2PA and blockchain add nothing there, and "EBSI anchor" reads as a buzzword.
- **Permissioned registries, crowded domain.**

**Bottom line:** the spine is good; Proof of Place is the better home for it.

---

### 21. ReCell: mobile-network restoration dispatch
**Challenge 2 · Kimi · 3.5 (base 4.0, −0.5 flood template)**

**What it is.** It optimises where mobile operators send portable cell towers, generators and crews after a flood, using Sentinel-1 flood evidence, outage data, roads and population.

**Pluses**
- **Concrete optimisation** that ties neatly to the towers-down story.

**Minuses and limitations**
- **A trivial optimisation problem.** Operators own few portable cells, so optimising a handful of units is easy. Placement is really limited by backhaul and power, which a satellite can't see.
- **The operator's own data matters more.** Operators' network-centre data and crew reports outweigh a flood map, and 10 m radar can't tell whether a road is passable (Kimi admits this).

**Bottom line:** an operator's internal spreadsheet problem.

---

### 22. PumpSlot: flood-pump mutual-aid dispatch
**Challenge 2 · GPT · 3.4 (base 3.9, −0.5 flood template)**

**What it is.** It assigns scarce mobile flood pumps, crews and routes using a Copernicus EMS flood outline, field reports and a small constraint solver. In the demo, a road closure changes the dispatch.

**Pluses**
- **The safest build in the pool,** with a testable decision.

**Minuses and limitations**
- **The flood maps arrive too late.** EMS rapid maps come hours to a day after the event, after pumps have been dispatched.
- **The wrong dispatcher and a weak buyer.** The fire service dispatches pumps through its own command system, and a water-utility consortium is a weak buyer.
- **The satellite barely contributes.** GPT itself says field reports decide.

**Bottom line:** safe to build, nothing to win.

---

### 23. PlotProof: EUDR deforestation audit API
**Challenge 3 · GLM · 3.3 (base 3.3, no penalty)**

**What it is.** Importers upload supplier plot coordinates. The service checks each plot's Sentinel-2 history against the regulation's 2020 cutoff and returns a signed verdict plus the payload for the EU due-diligence statement.

**Pluses**
- **Real legal pull,** per-plot pricing and a clean pipeline.

**Minuses and limitations**
- **Off-theme** for a security hackathon, with little Polish relevance (the plots are in Côte d'Ivoire).
- **A crowded market.** Dozens of EUDR vendors exist, and the EU provides free forest baseline maps.
- **Shaky verdicts on small plots.** Smallholder plots are under a hectare, and 10 m pixels plus clouds make verdicts unreliable.

**Known problems**
- **The timing claim is likely wrong.** EUDR was postponed again in late 2025, as I recall to end-2026 for large operators and mid-2027 for small ones *(verify)*. GLM says it has applied since December 2025.

**Bottom line:** a real business in the wrong room.

---

### 24. AirShift: crew rescheduling during smoke episodes
**Challenge 2 · GPT · 3.0 (base 3.0, no penalty)**

**What it is.** It reschedules outdoor municipal crews' tasks during smoke or smog episodes using CAMS air-quality forecasts and station data, and outputs a set of work-order changes.

**Pluses**
- **Honest and buildable.**

**Minuses and limitations**
- **Off-theme with low willingness to pay.**
- **Coarse forecasts:** the CAMS grid is about 10 km.
- **Sentinel-3 is decorative.** GPT admits it doesn't drive any decision.
- **Routine, not crisis.** Polish smog is mostly winter home heating.

**Bottom line:** a productivity feature, not resilience.

---

### 25. Power-plant cyber-physical check
**Challenge 1 · Plant strategy (its timing half duplicates #6) · 2.9 (base 3.4, −0.5)**

**What it is.** It pairs OSNMA timing checks with Copernicus observation of a power plant's physical state (cooling-tower plumes, river heat discharge) to catch falsified SCADA readings, and auto-drafts NIS2/KSC reports.

**Pluses**
- **The two-timescale framing is honest:** timing checks in real time, satellites over days. The data-diode deployment answer is good.

**Minuses and limitations**
- **The premise fails.** If a 1 GW unit trips, the grid operator (PSE) sees it within seconds through independent metering, grid frequency and market settlement, and the shift crew can see the cooling towers. Satellites passing every few days through November cloud add nothing.
- **Stuxnet-style attacks are invisible from orbit.** They damage equipment while output looks normal.
- **Too coarse for river heat.** Sentinel-3's 1 km heat pixels can't reliably resolve a discharge plume on the Vistula.
- **The timing half is the most converged idea in the pool.**

**Bottom line:** slower and coarser than phoning the shift supervisor.

---

### 26. SatSOC-Triage: satellite telemetry triage
**Challenge 1 · S1 (a secondary idea) · 2.9 (base 2.9, no penalty)**

**What it is.** AI-assisted triage of satellite telemetry and collision alerts that tries to separate malicious telecommands from radiation faults.

**Minuses and limitations**
- **Few customers.** Poland has few satellite operators, and the EU Space Act is years away.
- **Research data only** (ESA OPS-SAT).
- **Crowded field:** anomaly detection is heavily researched, and it sits close to past winners' orbital tools. Its own source ranks it near the bottom.

**Bottom line:** no buyer in the room.

---

### 27. WasteAlibi: OSNMA vs truck alibis
**Challenge 3 · Muse · 2.8 (base 3.3, −0.5 waste domain)**

**What it is.** It tests waste-truck GPS alibis with Galileo OSNMA (an unauthenticated position counts as an unreliable alibi) and adds Sentinel-2 evidence of dump growth to make inspection packs.

**Minuses and limitations**
- **A logic flaw.** An OSNMA failure shows only that a log is unauthenticated, not that the truck was at the dump. Most fleet trackers don't support OSNMA at all, so every innocent log "fails" too.
- **The suspect controls the evidence.** They own their logs and can switch the tracker off, so the evidence has to come from someone else's data.
- **Still the crowded waste domain,** and warehouses are opaque.

**Bottom line:** the core inference doesn't hold.

---

### 28. BlackoutBridge: GNSS-denied offline crisis routing
**Challenge 2 · Neon · 2.6 (base 3.6, −0.5 flood template, −0.5 past-winner adjacency)**

**What it is.** Offline navigation for responders that routes around Sentinel-1/EMS flood areas. When Galileo/EGNOS integrity checks flag jamming or spoofing, it switches to dead reckoning and landmark prompts.

**Minuses and limitations**
- **A contrived double crisis.** There was no GNSS jamming in the Kłodzko flood, and no flood in the Baltic jamming zones.
- **The technical claims don't hold up:**
  - OSNMA doesn't detect jamming (you just lose the signal);
  - phone dead reckoning drifts within a minute;
  - "landmark prompts from Sentinel-2" make no sense at 10 m.
- **Offline maps already exist** (OsmAnd, Organic Maps), and GNSS-denied navigation already placed at a past edition.

**Bottom line:** two problems glued together, neither solved.

---

### 29. Baltic Corridor (+ BalticCable-Triage): subsea cable watch
**Challenge 2 · Qwen, S1 (which rejects it) · 2.5 (base 3.3, −0.3 convergence, −0.5 banned category and past winner)**

**What it is.** It watches registered subsea cable and pipeline corridors with Sentinel-1 ship detection fused with AIS. It scores vessel behaviour (loitering, anchor drag) and auto-drafts incident records for asset owners and insurers.

**Minuses and limitations**
- **It's the banned "AIS + radar dark vessel" category with a new customer label.** A recent winner (SheerSea) did dark vessels, and Windward, ICEYE and NATO's Baltic Sentry occupy the space.
- **Wrong timescale.** The radar comes every few hours to days, while an anchor drag takes minutes.
- **Noisy detection.** Radar ship detection throws many false targets (wind farms, sea clutter), and AIS can't tell an accidental anchor drop from a deliberate drag.

**Bottom line:** the one idea the brief explicitly said not to build.

---

## Cross-cutting notes

- **The OSNMA-stamped photo is the most common bolt-on in the pool**, appearing in about a dozen ideas. The jury will be numb to it, and it invites "what exactly does OSNMA prove?" Use Galileo only where it does real work: EWSS in #1, place/time sealing in #3.
- **"System One" decision models are a technique, not an idea.** They aren't ranked separately. Adding a brand-new classifier to a security product hands the Cyber Defence Forces jurors an easy attack, especially given the injection-flip rates the S1 doc itself cites.
- **Kłodzko 2024 saturation.** If you pitch a flood case, open with something only you have (towers down and EWSS for #1; Poland footage passed off as Valencia for #3), not the flood map.
- **Shared GNSS groundwork.** #1, #2 and #3 all depend on the same Friday-night test: whether your phones log Galileo navigation messages. Its result decides more than any ranking here.
