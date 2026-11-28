Blunt 48-hour review incoming — verifying EWSS, CAMF, Android I/NAV, EFAS/GHSL access and every load-bearing claim against primary sources before the verdict.Found a key clash — the official ground segment already converts CAP polygons to ellipses. Now checking phone reception, fire data and the remaining datasets.# Last Signal — Hard Review (as of Saturday 28 Nov, 09:00)

## 0. What is right

- **The CAMF core is real and buildable.** CAMF v1.2 (March 2026) is genuinely in force, 122 bits, 105 mandatory + 17 additional, and explicitly licensed for "standardisation, research and development and commercial purposes". A pure-Python bit-packing codec in a day is realistic.
- **The ellipse constraint is real.** Target area is 49 bits: centre lat 16, lon 17, semi-major 5, semi-minor 5, azimuth 6, azimuth resolution 2.8125°, semi-axes log-spaced 0.216–2500 km. The doc's numbers check out.
- **The timing is genuinely exceptional.** Galileo Service Notice #28 confirms sporadic real EWM test transmissions **23 Jul – 30 Nov 2026**, authenticated with a new OSNMA ADKD=2. You are pitching on the last weekend of that window. EWSS Initial Service in 2027 is also confirmed.
- **Alert RCB really is SMS, not cell broadcast**, so the "towers down = no alert" premise holds: RCB is described as an SMS system forwarded by mobile operators, and Poland's cell-broadcast replacement is only planned, with launch around September 2027.

Everything below is the bad news.

---

## 1. Technical implementation, component by component

### 1.1 CAMF codec — mostly fine, four traps

**Trap 1 — Azimuth convention (MAJOR).** Your optimiser will get rotation wrong if anyone assumes compass bearing. CAMF azimuth λ is "measured from East to the ellipse major axis line, with positive values counted from East toward North", over −90°…+87.1875°. *Fix:* single conversion function `azimuth_camf = 90° − bearing_north_clockwise (mod 180°)`, unit-tested both ways, and plot decoded-from-bits ellipses (not pre-quantisation ellipses) on the console. If the map shows the quantised ellipse, this bug becomes visible to the IGiK jurors immediately.

**Trap 2 — Ellipse membership test (MAJOR).** The spec defines the centre grid "on a grid defined by fixed latitude and longitude intervals in the Mercator projection" and all positions in WGS84. A `shapely` ellipse test in raw degrees, or in Web-Mercator metres without geodesic correction, will misclassify edge cases by hundreds of metres at Polish latitudes and will be torn apart by the GNSS jurors. *Fix:* do membership in a local azimuthal-equidistant projection centred on the ellipse (`pyproj.Proj(proj="aeqd", lat_0=…, lon_0=…)`) or via geodesic inverse; state the method on a slide. Do the optimiser's population sums in the GHSL native grid (World Mollweide, EPSG:54009) — reprojecting the ellipse polygon, not the raster.

**Trap 3 — No official test vectors (MAJOR).** The doc assumes "decode the spec's own examples **[VERIFY examples exist]**". CAMF v1.2's Annex C is field tables, not worked bit-strings; the document itself says receiver guidelines "should be provided separately by satellite navigation providers" — i.e. they are not in this document. *Fix:* (a) hand-build 3 golden vectors and cross-check against the QZSS DCX interface specification, which carries the identical 122-bit CAMF; (b) get a mentor or another team to independently decode one of your vectors on Sunday morning — an "independent decode" is a stronger demo claim than self-round-trip anyway.

**Trap 4 — Provider ID and library tables are not fully public (MAJOR).** A3 allows "up to 32 individual alert providers per Country/Region" but the actual per-country lists "shall be provided for each Country/Region" — there is no published Polish provider list assigning RCB a code. You cannot legitimately encode "RCB" today. *Fix:* encode with `A1 = Test`, provider code 00000, and say so on screen: "Test message type, placeholder provider — production codes are assigned nationally." That converts a bluff into evidence you read the spec. Same for the instruction library: List A/B have 32 entries each; you must transcribe Annex C tables by hand — budget 2 hours, double-key the flood-relevant entries, and checksum by having two people transcribe independently.

### 1.2 Ellipse optimiser — the core idea has a spec conflict and an ID collision

**BLOCKER — your objective contradicts the specified system behaviour.** CAMF §3.6 states: "the system shall compute the ellipse parameters such that the resulting ellipse fits best the polygon. This best fit ellipse is the ellipse that contains the entire polygon area and that has the smallest area". STELLAR (the CNES/Telespazio EWSS demonstrator) implemented exactly that: "the ellipse must encompass all the target area… the smallest surface as possible". Your headline — "96% coverage, 18% over-warning" — means deliberately *not* alerting 4% of the at-risk population. A civil-protection juror will ask who authorised leaving 4% unwarned.

*Fix (executable by Sunday):* ship **two modes** and make the contrast the demo's intellectual core:
1. **Spec mode:** smallest quantised ellipse containing 100% of the hazard polygon (the STELLAR/ERAS baseline — this is also your "naive vs ours" baseline, except it's not naive, it's the mandated one).
2. **Population mode:** maximise at-risk population covered per over-warned person, with **missed at-risk population shown in red as an explicit number**, never hidden. Frame it as "a decision-support trade-off the duty officer must sign off", not as the system silently optimising.

That framing survives the pushback; the current framing does not.

**BLOCKER — multi-ellipse alerts collide on Alert ID.** The Alert ID is built from A2+A3+A4+A6+A7 (country, provider, hazard, onset), and the spec warns the operational concept must prevent creating "2 different alerts with the same hazard category & type and onset" from one provider. Your "2 EWSS messages for one valley, same hazard, same onset" therefore produces **two messages with the same Alert ID** — a receiver may treat the second as an update of the first and replace it. *Fix:* either (a) present multi-ellipse as separate alerts with explicitly different onset minutes and admit this is a hack the operational concept must resolve, or (b) drop to one ellipse per alert in the demo and present corridor-splitting as "requires EUSPA operational rules — open question we flag". Option (b) plus the B3 note below is more honest. Note also B3 "secondary ellipse" is **not** a second corridor segment: it is a homothetic/rotated transform of the main ellipse for vigilance or evacuation-point instructions, and B1/B2/B3/B4 are mutually exclusive within the 17 additional bits.

**MINOR — search speed.** Quantised space is small (centre grid × 32 × 32 × 64); the expensive part is raster population sums. Precompute GHSL cumulative sums per candidate via raster zonal stats once per hazard polygon, cache with `rasterio` masks at 100 m; a coarse-to-fine search will run in seconds. This is fine. Do **not** reproject the raster per candidate.

### 1.3 Receiver / I-NAV extraction — the weakest component

**BLOCKER — you do not know, and probably cannot know by Sunday, how the 2026 test EWMs are encapsulated.** CAMF is deliberately implementation-independent: it "does not describe the implementation of the format on the side of national civil protection systems" and is "described independently of any specific implementation". The historical path was the SAR field: the RLM "is transmitted in the SAR field of the E1 signal I/NAV message, which allocates 20 bits every 2 s page", 22 bits per odd page including start/short-long flags, and EUSPA's earlier grant call confirmed EWSS messages "will be encoded in the I/NAV, in particular in the bits used for the return link service (i.e. SAR bits)". But the 2026 test campaign's exact encapsulation, repetition, and which long-RLM code carries CAMF are not in any public document you have cited. *Fix:* on Saturday morning, email/ask mentors (ChipCraft first) one question: "Is there a published Galileo EWSS SIS ICD or receiver guideline for the 2026 tests?" If no: **the receiver demo becomes "decoder fed by (i) our own encoder output injected into a real recorded I/NAV SAR-field stream, replacing spare RLM payload, and (ii) any genuine long-RLM code-0010/0101 traffic we record"** — note the GalileoSARlib study found long RLMs with codes "0010" and "0101" are already on air and undefined/spare in current documentation, which is a genuinely interesting hook: "5.3% of RLM traffic is long-format with spare codes — that is the EWSS carrier being exercised." Reuse **GalileoSARlib** (open-source, parses SAR field from SBF) rather than writing SAR parsing from scratch.

**BLOCKER — Android nav-message support.** "Very few devices support logging navigation messages". Android does define `TYPE_GAL_I` and the I/NAV page format (2×114 = 228 bits per page), but chipset exposure is device-specific, and GnssLogger `Nav` records are the first thing to silently be absent. *Fix:* the Friday-night phone test is not a checklist item, it is a **gate**. Test every team phone + borrow 2–3 mentor phones Saturday 09:00. You need one device that logs Galileo I/NAV `Nav` lines for ≥10 minutes outdoors. If none: pivot the receiver to a **laptop + recorded SBF/log replay** (GalileoSARlib's published datasets) and put the phone UI on top as a display of the decoded result with an honest "reference receiver on recorded Galileo data" label. Do not fake a live phone decode.

**MAJOR — indoor demo.** The pitch venue will attenuate E1 badly. Even with a working phone, "live only if test alerts are being broadcast" plus "sporadic transmissions" plus indoors = near-certain live failure. *Fix:* live capture attempt happens **Saturday outdoors**, recorded; Sunday demo plays the recording. See §3.

### 1.4 Integrity / OSNMA — your ranking section is now out of date, in your favour — but the code won't do it

**MAJOR (opportunity + trap).** The ranking file says OSNMA doesn't authenticate the alert. Service Notice #28 supersedes that: "EWSS messages broadcast by the Galileo Programme will be authenticated using OSNMA… authenticated through a new OSNMA ADKD with value 2 (ADKD=2)". So EWSS *is* OSNMA-authenticated — say this loudly; it's a strong Challenge 1 link. **But:** ADKD=2 is "'Reserved' in the OSNMA Signal-in-Space Interface Control Document" and existing users are "expected to… discard the tags associated to an ADKD defined as 'Reserved'", authentication uses MACLT ID=34 with at most one FLX tag per subframe, and OSNMAlib (github `Algafix/OSNMA`) implements the pre-2026 OSNMA for ADKD 0/4/12 navigation data. It will **not** verify ADKD=2 EWM tags out of the box, and may not even parse MACLT 34. *Fix:* scope the integrity feature to: (1) OSNMA status for ADKD0 (nav data) via OSNMAlib as a *consistency* signal; (2) display "EWM authentication = OSNMA ADKD=2 per Service Notice #28; verification requires updated MACLT 34 — not yet in public OSNMAlib; our receiver exposes the FLX tag slot for it." Cyber-defence jurors will reward precisely this sentence and punish any slide implying "OSNMA OK ⇒ alert authentic" today. Also add the TESLA timing point: OSNMA gives *delayed* authentication (key disclosed after the tag), so a receiver cannot authenticate an alert at first reception — only retrospectively. For a "evacuate now" message that tension is a real design issue; naming it unprompted is the best Challenge 1 move available to you.

### 1.5 Copernicus inputs

**EFAS — BLOCKER for real-time claims, fine for replay.** "All real-time EFAS forecasts and products are restricted and only accessible to EFAS partners… restricted EFAS real-time forecasts are released publicly after an embargo of 30 days". You will not get a hackathon account by Sunday, and in production you'd need to be an EFAS partner authority — which actually supports the buyer story (sell *to* partners) but kills any "live EFAS feed in the demo" line. *Fix:* replay uses archived (>30-day) September 2024 EFAS via EWDS, or drop EFAS from the demo path entirely and drive the replay from EMSR756 + GFM. Also note EFAS output is river-discharge forecast points, **not flood-extent polygons**: turning discharge exceedance into a hazard polygon needs flood-hazard maps and a Manning/routing assumption. In 48 h, do not pretend otherwise — for the replay, the hazard polygon *is* the EMSR756 delineation; EFAS supplies only onset timing narrative.

**GFM — MAJOR latency honesty.** GFM: 20 m resolution, "latency from satellite acquisition to product availability is under 8 hours", updated every 1–3 days over Europe depending on Sentinel-1 overpass. Fine for *Update* messages; useless for the dam-break first warning. Your pipeline already assigns GFM to updates — keep that discipline in the script, never say "real-time flood extent".

**EMSR756 — MINOR, but watch the timeline claim.** Activation 13/09/2024 12:50, 20 products/35 maps; first delineations delivered 15 September for Świdnica and Jelenia Góra AOIs. So EMSR756 cannot support a "we would have warned Stronie before the dam broke on the 15th" claim. Your replay's honest claim is: warning from forecast (EFAS/national hydrology) → updates from EMSR756/GFM. If your replay timeline shows an alert *before* 15 Sep based on EMSR756 polygons, that is fabrication — a remote-sensing juror (IGiK) may know these dates.

**GHSL — MINOR, mostly fine.** GHS-POP R2023A: 100 m, World Mollweide, persons per pixel, CC BY 4.0, epochs in 5-year steps to 2030. It's *residential* (night-time) modelled population, not people-present-at-14:00, and 2025 is a projection. One sentence in the pitch: "residential population; daytime/tourist load is a production refinement." Download the single tile covering Lower Silesia Saturday morning; do not stream it during the demo.

**Fire (Sentinel-3 SLSTR FRP) — MAJOR if demoed, MINOR if dropped.** SLSTR FRP is 1 km pixels with hotspots characterised "within three hours from SLSTR observation sensing time" and ~daily-scale revisit. That is a poor trigger for an urgent wildfire ellipse and will invite "why not VIIRS/Meteosat?" — to which you have no EU-space answer you'd like. *Fix:* cut fire from the live demo; keep one line "second hazard class: fire, via EFFIS/SLSTR FRP" in the roadmap slide only.

**Outage layer — MAJOR.** There is no API; the doc already labels it approximate. Drawing tower-level outage polygons from press quotes would be fabrication. *Fix:* powiat/gmina-level shading labelled "reported outage area (press, Sept 2024), not tower data", used only to weight population — and be ready to say production data comes from operator reporting under the national crisis framework, not from you.

### 1.6 Stack choices

- `FastAPI + numpy/shapely/pyproj/rasterio` (Python 3.11): fine, `pip install` and go. Pin nothing exotic.
- **MapLibre GL JS with online tiles will fail on venue Wi-Fi.** *Fix:* pre-download vector tiles for Lower Silesia into a local PMTiles file, or render the console against static raster basemap images. Test the full demo with Wi-Fi off on Saturday night.
- **OSNMAlib**: clone `github.com/Algafix/OSNMA`, run its sample I/NAV **Saturday morning**; if install/import fights you for >45 min, drop to "OSNMA status displayed from pre-computed sample output" and spend the time on the codec.
- **Frontend phone view**: a responsive web page on the same laptop-as-server, phone on local hotspot/USB tethering — but remember the phone in "flight mode" then can't load your web app. Preload/cache it as a PWA or serve it before enabling flight mode. This detail will bite at 14:55 Sunday if untested.

---

## 2. Correctness of EU-space usage — summary of what each input actually proves

| Claim in doc | Reality | Severity |
|---|---|---|
| EWSS alerts broadcast to phones now | Test transmissions only, ending 30 Nov 2026; Initial Service 2027; external chipset testing only *after* this internal phase | MAJOR — pitch must say "preparing for 2027" |
| OSNMA check authenticates the alert | ADKD=2 does authenticate EWMs, but is Reserved in current SIS ICD and public tooling discards it | MAJOR — reframe per §1.4 |
| Show alert "in the user's language… Polish, then Ukrainian" | International library exists in 25 languages — the list is Bulgarian…Norwegian and **does not include Ukrainian**; fallback if language unavailable is English | **BLOCKER for the scripted demo beat** — replace Ukrainian with e.g. Czech/German, or explain a Ukrainian *national* library would be needed. Do not show Ukrainian UI text as if decoded from CAMF |
| Library-version mismatch handling | Receiver "shall notify the user that an alert is on-going nearby, but the warning message cannot be notified" and user must install the latest library | MINOR — implement exactly this behaviour; it's a spec-compliance point in your favour |
| Country ∩ ellipse geofence | Correct per spec: notify iff position ∈ Country ∩ Ellipse | MINOR — but you need an offline Poland boundary dataset; the CAMF gives a country *code*, not a polygon. Budget 30 min: Natural Earth / GADM Poland polygon, simplified, shipped in repo |
| Duration-based clearing | Duration has only 4 values: Unknown, <6 h, 6–12 h, 12–24 h; "Unknown" *requires* a mandatory All-Clear later | MINOR — encode floods as 12–24 h or Unknown+All-Clear in replay |
| "No mobile network needed" | True for the GNSS downlink; but the phone needs a GNSS fix (works in flight mode — GPS/GNSS receivers remain active as receive-only) **and** a chipset/firmware that extracts EWSS — which per EUSPA requires chipset-industry readiness work still in progress | MAJOR — "phones" in pitch = "EWSS-capable devices from 2027+", never "your phone today" |

---

## 3. Demo risk and fallbacks

| Risk | P(fail) | Fallback (build by Sat 22:00) |
|---|---|---|
| No live EWM during pitch (sporadic tests) | ~Certain | Recorded outdoor capture Saturday; pitch language: "recorded yesterday from the live test broadcast" — only if you actually capture one; otherwise "injected into real recorded I/NAV" |
| Team phones don't log Galileo `Nav` | High | Laptop replay of recorded logs + GalileoSARlib datasets; phone as display only |
| Venue Wi-Fi / CDSE / tile servers down | High | Everything local: EMSR756 + GHSL pre-downloaded, PMTiles basemap, no live API calls in demo path. Full offline run-through Sat 22:00 with Wi-Fi off |
| CAMF transcription bug found live | Medium | Golden vectors + independent decode (mentor/other team) Sunday 10:00; freeze codec after |
| Numbers on slides (96%/18%) not yet computed | Certain as of now | **No number goes on a slide until the replay produces it.** The ranking file itself flags these as [VERIFY]. Compute Sat afternoon; if optimiser underperforms, the honest number *is* the story ("even optimal ellipse over-warns X% — that's why B-mode matters") |
| Phone flight-mode can't load web UI | Medium | PWA cache / load-then-flight-mode rehearsed sequence |

Record a 90-second screen-capture of the full demo Saturday night. If the live demo dies, play it without apology and move on.

---

## 4. Jury pushback — first hard question per archetype

| Juror | First question | Your only survivable answer |
|---|---|---|
| **GNSS chip engineer (ChipCraft)** | "Which word/page carries your 122 bits in the 2026 test signal, and what's the repetition period?" | "CAMF is signal-independent; the Galileo encapsulation via the SAR/RLM field (20 bits per odd page) is the documented path, but the 2026 test ICD isn't public — so our receiver decodes CAMF from the SAR field of recorded I/NAV and we flag the production ICD as the gating item. That's exactly why a reference decoder + test vectors is the product." |
| **Remote-sensing academic (IGiK)** | "Your hazard polygon is a post-event delineation. What exactly did you know, and when, on 14 September?" | Show the timeline honestly: forecast-based first alert (EFAS partner data / national hydrology), GFM update <8 h after a Sentinel-1 pass, EMSR756 from 15 Sep. Never claim EMSR756 gave lead time. |
| **Space optics (Scanway)** | "Why is a 100 m residential grid the right denominator for 'people at risk' in a valley at midday?" | "It isn't — it's the best open EU-wide proxy (GHS-POP R2023A, 100 m); production adds daytime mobility data. Our metric is *relative* — same denominator for baseline and optimised ellipse." |
| **EO expert (Blue Dot)** | "EFAS real-time is partner-restricted. Who runs this in production?" | "An EFAS-partner authority — which is why the buyer is the authority/PWS vendor, not us as data broker." Restricted access with 30-day embargo is documented — agreeing with the premise disarms it. |
| **Cyber-defence (WAT / Cyber Defence Forces)** | "I spoof an EWM with a £300 SDR on day one. What stops me?" | "OSNMA ADKD=2 authenticates EWMs, but verification is TESLA-delayed and public tooling currently discards ADKD=2 tags — so today: anomaly flags (time/onset consistency, nav-data OSNMA status), audit logging, and never acting on unauthenticated alerts alone. We do not claim real-time alert authentication." |
| **ESA BIC Poland** | "EUSPA is procuring ERAS as a turnkey system and STELLAR already computes the ellipse in a Python script. What is left to sell?" | See §5 — this is the existential question. |

---

## 5. Buyer, business, legal, procurement

**BLOCKER (commercial) — the "missing piece" may already be procured.** CAMF itself assigns ellipse computation to "the system": "The ellipse parameters shall be computed by the system based on the information contained in the CAP message". STELLAR built the EWS-PP-Server that verifies CAP, computes the ellipse and the EWM bit chain. ERAS is being procured by EUSPA as the operational Galileo infrastructure for EWSS delivery. If ERAS includes a competent CAP→ellipse converter, a standalone "optimiser licence for RCB" is a feature inside someone else's contract, with public-procurement cycles measured in years.

*Executable pivot (no extra build, just repositioning):*
1. **Primary buyer = public-warning-system (PWS) vendors and national integrators** (the F24/Telespazio/AWARE class of companies) who must add EWSS targeting to existing CAP chains across 27 different national setups — sell the optimiser as a *component/SDK with conformance tests*, not as a system for RCB. AWARE already exists to push EWSS into "widespread PWS solutions" in the B2B/B2G market — your customers/partners are named by that sentence.
2. **Your defensible differentiator vs STELLAR's converter:** STELLAR optimises *area ratio* (polygon/ellipse closest to 1, containing whole polygon). Yours optimises *population-weighted* outcome with GHSL and shows the duty officer the missed-population cost. That is a real, articulable delta — lead with it.
3. **Chipset SDK:** reference decoder + test vectors is the most credible revenue line (ChipCraft is in the room), but temper it: EUSPA will run "ad hoc testing campaigns" for chipset manufacturers after the internal test phase — you sell *preparation* for those campaigns, starting now.
4. **Legal/liability:** any tool that trades coverage for over-warning creates liability for the *authority*, not you, only if the human sign-off is explicit in UX (see §1.2 Mode 2 with red missed-population and a named "approve" action). Build that button; it's both a legal shield and a demo beat. Also note CAMF terms prohibit altering the *document* and require source attribution — put the attribution line in your README.
5. **SUNSHINE competition/co-option:** SUNSHINE (Jan 2025–2027) is already funded to promote EWSS + Copernicus EMS use by civil-protection authorities and "can support integration of EWSS into your national warning systems". Position as "the tool SUNSHINE-trained authorities will need", and try to get a SUNSHINE-adjacent mentor quote Saturday.

**Practitioner gap (from your own past-winners analysis): CRITICAL and still open.** Past CASSINI winners' pattern — practitioner involvement was Viadrus's stated differentiator. You have no civil-protection practitioner. Saturday: use mentor hours to get *one* conversation (State Fire Service / RCB / voivodeship crisis centre duty officer, even by phone) and one quotable sentence on ellipse trade-offs. This is worth more points than any feature after the codec+optimiser core.

---

## 6. Rules, saturation, differentiation

- **Fresh Code (MAJOR risk):** the doc says the receiver uses "the same stack the team already uses for OSNMA in Balloon Radar". If any code is copied from the pre-weekend Balloon Radar repo — OSNMA parsing, GnssLogger ingestion — that's a Fresh Code violation and discoverable via git history. *Fix:* fresh repo created Friday, rewrite ingestion (it's ~100 lines), use only public libraries (OSNMAlib, GalileoSARlib) as dependencies, and keep commit timestamps clean. State this proactively in the submission ("libraries: OSNMAlib, GalileoSARlib, shapely…; all project code written 27–29 Nov").
- **EU-space requirement:** comfortably satisfied — Galileo EWSS/OSNMA + Copernicus EMS/GFM/GHSL. But if the receiver ends up decoding only self-injected bits, a strict juror could argue Galileo is decorative. Mitigation: even in fallback, decode **real recorded Galileo I/NAV pages** (real SAR field, real OSNMA fields) with the CAMF payload injected at the bit level, and show one slide of genuine on-air RLM statistics from your own Saturday recording. That keeps Galileo load-bearing.
- **Saturation:** EWSS itself is unsaturated (your strongest asset). **Kłodzko-2024 replay is not** — your ranking file already warns it's everyone's demo. Add the second scenario cheaply: a Seveso/dam-break point-source hazard is actually the *easy* case for your optimiser (compact polygon → tight ellipse, B2 hazard-centre setting exists precisely for point hazards) and differentiates the replay. Two hours of work, high return.
- **Track fit:** Challenge 2 primary is right; the Challenge 1 link only survives with the §1.4 honest framing.

---

## (a) Prioritized fix list (top 10)

1. **Saturday 09:00 phone gate:** test GnssLogger Galileo `Nav` logging on all available phones outdoors; pick the demo device or trigger laptop-replay fallback.
2. **Fix the pitch's Ukrainian beat** — CAMF's 25 languages exclude Ukrainian; use Polish + Czech/German, mention national-library path for Ukrainian.
3. **Implement spec-mode vs population-mode optimiser** with missed-at-risk population in red and an explicit human "approve" action (spec mandates full containment).
4. **Resolve multi-ellipse Alert-ID collision** — one ellipse per alert in demo; corridor-splitting flagged as open operational question (Alert ID = A2+A3+A4+A6+A7).
5. **Azimuth conversion + geodesic ellipse test** with unit tests; console always renders the *quantised, decoded* ellipse.
6. **Golden CAMF vectors:** independent decode by a mentor/another team; encode as `A1=Test` with placeholder provider (no published Polish provider codes).
7. **Rewrite OSNMA claims** to ADKD=2 reality (authenticates EWMs, Reserved in ICD, MACLT 34, public tooling discards it); scope code to consistency flags only; 45-min OSNMAlib timebox.
8. **Offline-proof the demo:** EMSR756 + GHSL tile + PMTiles basemap local; Wi-Fi-off rehearsal Saturday 22:00; 90-s backup recording.
9. **Get one practitioner quote** (fire service / crisis centre / PWS vendor) via Saturday mentoring; reposition buyer story to PWS vendors + chipset test-vector SDK vs ERAS/STELLAR (ERAS is EUSPA-procured turnkey).
10. **Fresh repo, no Balloon Radar code reuse;** README with CAMF attribution and library list; add second point-source (dam/Seveso) scenario to escape Kłodzko saturation.

## (b) Three things to verify first on Saturday morning

1. **Do any of our phones log Galileo I/NAV `Nav` records with GnssLogger?** (30 min, outdoors, every phone.) This decides whether "reference receiver" is a phone demo or a recorded-data demo.
2. **Is there any public Galileo-side EWSS encapsulation spec / are test EWMs capturable today?** Ask ChipCraft/GNSS mentors directly; simultaneously run a 1-hour outdoor recording and inspect SAR-field long RLMs (GalileoSARlib) for non-spare payloads.
3. **Does the optimiser on real EMSR756 + GHSL data beat the spec-mode baseline by a number worth printing?** Run Biała Lądecka end-to-end before 13:00; if the population-mode gain is small, the pitch pivots to spec-mode + trade-off visualisation, and slide numbers change accordingly.

## (c) Verdict: **CONDITIONAL GO**

The concept is the strongest originality-to-buildability bet in the pool: CAMF v1.2 is public and commercially usable, the codec and quantised optimiser are genuinely weekend-sized, and pitching during the final 48 hours of Galileo's live EWM test window (Service Notice #28, ending 30 Nov) is a once-only narrative gift. But the project as written over-claims in four places that this specific jury is professionally equipped to puncture — a coverage-trading objective that contradicts the spec's mandated full-containment ellipse, a multi-ellipse scheme that collides on Alert ID, a Ukrainian-language demo beat the CAMF library cannot produce, and a phone receiver whose Galileo encapsulation and Android nav-message support are both unverified and likely unavailable indoors. Cut the receiver to an honest recorded-data reference decoder, ship the two-mode optimiser with explicit human sign-off on missed population, fix the language and OSNMA (ADKD=2) stories, and land one practitioner quote — with those conditions met by Saturday night, this is a credible podium contender; without conditions 2–4, it is one hard ChipCraft question away from collapsing on stage.
