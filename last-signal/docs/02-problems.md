# Last Signal — problems register (from the project dossier, unchanged)

## 4. Problems and solutions

### 4.1 Consolidated problem register

Severity definitions:

- **BLOCKER** — the original claim or deliverable must be removed, replaced, or gated before submission.
- **MAJOR** — can invalidate the result, business case, or demo if not fixed.
- **MINOR** — should be fixed if time allows, but must not displace the blockers.

Attribution note: the supplied project packet contains complete reviews from research-sol and research-wonder, the project ranking, fact-check, design document, guidelines, and past-winner notes. A separate complete research-kimi review was not present in the material available for this dossier; no finding below is attributed to Kimi.

| ID | Problem | Severity | Raised by | Solution | Residual risk |
|---|---|---:|---|---|---|
| P-01 | The design implies Galileo EWSS can now deliver an alert to a phone. In reality, test transmissions run 23 Jul–30 Nov 2026 and Initial Service is planned for 2027. There is no public uplink for the team. | BLOCKER | Sol, Wonder, Ranking, Fact-check | Rename “Send” to “Export exercise draft.” Remove live-delivery claims. Say “preparing for the 2027 service.” | Judges may still consider the impact future-dated. Mitigate with preparation/test use case. |
| P-02 | “Reference receiver on an Android phone” is unproven. Device support for Galileo I/NAV `Nav` records varies; a fix does not prove navigation-page access; indoor reception is unlikely. | BLOCKER | Sol, Wonder, Ranking | Run one 20–30 minute outdoor phone gate. If it fails, ship payload decoder only and label phone UI as preview. | Even if pages exist, EWSS payload identification may remain impossible. |
| P-03 | The 2026 EWSS radio encapsulation is not established from public material. CAMF 122 bits, long RLM 160 bits, SAR field 22 bits/page, and Android's 228-bit I/NAV representation are different layers. | BLOCKER | Sol, Wonder | Ask ChipCraft/mentors for a shareable capture plus expected decoded fields. Otherwise start demo at CAMF payload boundary. Never splice synthetic bits into a log and call it reception. | A GNSS judge may still see Galileo as under-used if only payload decoding is shown. Show real EMS geometry and, if available, unrelated real I/NAV inspection separately. |
| P-04 | Original integrity claim overstates OSNMA. Authenticating navigation data on a satellite does not authenticate the return-link alert. | BLOCKER | Ranking, Sol, Wonder | Remove green badge and broad Challenge 1 claim. Use provenance states and fail-closed handling. | Cyber judges may ask why integrity remains in the pitch at all. Answer with ADKD=2 roadmap and audit states. |
| P-05 | Updated fact: Service Notice #28 does assign OSNMA ADKD=2 to EWSS authentication, but ADKD=2 is reserved in the current SIS ICD material and public tooling may discard it. | MAJOR | Sol, Wonder, Fact-check | State both halves: “EWSS authentication is specified for the tests through ADKD=2; our public toolchain cannot yet verify it.” Display tag-slot readiness only if actually implemented. | Jurors may challenge whether MACLT 34 details have been checked in v-current documents. Mark exact implementation status honestly. |
| P-06 | CAMF v1.2 is in force, but the team designed from v1.1 and has not verified the v1.2 body, field changes, language tables, or worked examples. | BLOCKER | Sol, Wonder, Design | Download v1.2 Saturday morning, hash it, compare relevant sections and Annex C. Implement one verified flood profile. If not verified by midday, label codec experimental. | Transcription errors remain possible; independent decode required. |
| P-07 | A self-round-trip encoder/decoder can share the same bug and falsely appear conformant. Annex C field tables are not a complete conformance suite. | MAJOR | Sol, Wonder | Build hand-checked golden vectors, independent field breakdown, malformed-field tests, and an independent decode by another person. | Cross-checking against QZSS material helps only if the relevant CAMF tables are identical in the implemented subset. **[UNVERIFIED]** |
| P-08 | The official/CAMF system behaviour described in the reviews computes a smallest ellipse containing the target polygon. The design instead celebrates partial coverage such as “96% covered.” | BLOCKER | Wonder; supported by Sol's matched-coverage warning | Ship Spec Mode as baseline/default and Population Mode as explicit operator-approved trade-off. Show missed residents in red. | Civil-protection users may reject any partial-coverage mode. That reaction is itself useful validation. |
| P-09 | Multi-ellipse corridor alerts can collide on Alert ID when provider, hazard, and onset are the same. The second alert may replace the first. | BLOCKER | Wonder; Sol also warns messages may conflict | Demo one ellipse per alert. Show two-ellipse union only as offline sensitivity analysis. Flag operational rule as an EUSPA question. | Corridor advantage becomes less dramatic. Honest constraint is preferable to a non-working alert model. |
| P-10 | The B1–B4 17-bit settings are mutually exclusive. B3 secondary ellipse is not a second freely fitted corridor ellipse. | MAJOR | Sol, Wonder | Implement only one verified setting or none. Describe B3 accurately as constrained secondary geometry/guidance, subject to v1.2 confirmation. | Reduced feature list; no material demo loss. |
| P-11 | No verified Polish provider code exists in the material. Encoding “RCB” would be a bluff. | MAJOR | Wonder | Use Test message type and placeholder provider, clearly displayed. | Judge may ask who will assign codes; answer: national implementation, not the team. **[UNVERIFIED: assignment process]** |
| P-12 | The scripted Polish-then-Ukrainian alert is not supported by the reviewed CAMF international library: Ukrainian is not listed among the 25 languages. | BLOCKER | Wonder, Sol | Remove Ukrainian as a decoded-library claim. Use verified Polish plus Czech/German, or label Ukrainian as a future national-library/UI translation. | Polish/Ukrainian local relevance is reduced, but factual credibility is preserved. |
| P-13 | CAMF azimuth is measured from East toward North. GIS code often assumes bearing from North clockwise. A sign/convention error rotates the ellipse incorrectly. | MAJOR | Wonder, Sol | Single conversion function, inverse unit tests, north–south/east–west golden cases, and render only decoded ellipses. | If v1.2 changes the convention, tests must be updated after document check. |
| P-14 | Ellipse membership in degrees or Web Mercator can misclassify locations by hundreds of metres. Population scoring in the wrong CRS compounds the error. | MAJOR | Wonder, Sol | Use local azimuthal-equidistant/geodesic membership and GHSL native-grid population scoring. Document methods. | Edge sensitivity remains; show the sensitivity result. |
| P-15 | EMSR756 is retrospective. AOI products were released at different times and some were still in progress days later. It cannot support “we could have warned before the dam broke.” | BLOCKER | Sol, Wonder | Label as retrospective targeting. Show acquisition/release dates. Remove lead-time claims. | Story becomes less dramatic but technically defensible. |
| P-16 | The wrong EMSR756 layer could be used: AOI rectangle, permanent water, damage points, or map image instead of observed flood geometry. AOI03 and AOI16 Nysa must not be confused. | MAJOR | Sol | Inspect ZIP contents and layer metadata. Record product, layer, sensor, acquisition, and release. Switch from Stronie to Nysa if geometry/exposure is inadequate. | Public API/ZIP behaviour may differ at download time; verify Saturday. |
| P-17 | EFAS real-time forecasts are restricted to partners. Archived access needs EWDS/ECMWF processes and EFAS outputs are discharge forecasts, not street-level inundation polygons. | BLOCKER for live claim | Sol, Wonder, Ranking | Remove EFAS from executable path. Optional slide context only. Future production input would be an authority/partner-supplied reviewed polygon. | Some judges may ask what triggers the first warning; answer honestly: partner forecast/national hydrology outside prototype. |
| P-18 | GFM is observed surface flooding with a target of roughly eight hours after Sentinel-1 acquisition, not real-time onset detection. It has radar shadow, vegetation, urban, and no-observation limitations. | MAJOR | Sol, Wonder | Use only as backup or update context. Cache one scene and advisory masks. Never render no-observation as dry. | A suitable scene may not exist for the chosen case. EMSR756 remains primary. |
| P-19 | GHSL measures modelled residential population, not people present, phone owners, evacuees, tourists, or people who lost mobile service. Its 100 m cells are sensitive in narrow valleys. | MAJOR | Sol, Wonder, Ranking | Call counts “estimated residents.” Use 2020 epoch, native grid, transparent cell rule, and one sensitivity check. If denominator is tiny, switch AOI. | Results remain estimates; relative comparison is more defensible than absolute impact. |
| P-20 | The design's 96% coverage, 18% over-warning, and 11,400 outage population figures are not computed results. | BLOCKER | Sol, Wonder, Design | Delete until produced by the final pipeline. Lead with missed residents and show raw counts. | Real numbers may be less impressive. Use the honest trade-off as the story. |
| P-21 | An optimiser can improve its over-warning ratio by sacrificing a small settlement. “Outside mapped flood” also does not mean safe. | MAJOR | Sol, Wonder | Put missed mapped-exposed residents first; show missed-area map; compare at matched coverage or display the full trade-off. | Population mode may look unattractive once misses are visible; that is the point of decision support. |
| P-22 | The official ground segment/service concept already includes CAP submission and conversion to a target ellipse/EWM. STELLAR and ERAS-related work weaken the claim that “the missing piece” does not exist. | BLOCKER commercially | Sol, Wonder | Reposition as operator-side comparison, QA, audit, and what-if module for vendors/authorities. Ask whether the gateway exposes/retains an operator-reviewed ellipse. | If the gateway already does population-aware optimisation with audit and override, the standalone product thesis may fail. |
| P-23 | Direct sale to RCB or a voivodeship is unproven. EWSS is free to authorities; public procurement is slow; F24/Everbridge-type vendors may be partners or substitutes. | MAJOR | Sol, Wonder, Ranking | Make the first offer a fixed-scope paid tabletop benchmark for a warning-platform integrator, reviewed by an operator. Treat direct authority licence and device SDK as later hypotheses. | No buyer commitment exists. Practitioner and vendor discovery are essential. |
| P-24 | A second fire hazard is not a quick clone. Sentinel-3 FRP detects active fire at coarse scale; it is not a perimeter or evacuation model. EFFIS active-fire detections are not all Sentinel-3 measurements. | MAJOR | Sol, Wonder | Cut fire from the prototype. Mention polygon-input generalisation only as roadmap. | Some judges may see flood-only scope as narrow; narrowness is preferable to false breadth. |
| P-25 | There is no geospatial tower-outage dataset in the evidence. Press reports do not locate towers, establish all-operator coverage holes, or identify affected residents. | MAJOR | Sol, Wonder, Ranking | Delete outage layer and population weighting. Use the dated Orange/PAP report as narrative context only. | The “only channel” claim becomes weaker and must be removed. |
| P-26 | Alert RCB should be described accurately as SMS-based, not assumed to be cell broadcast in 2026. | MINOR | Sol, Wonder, Fact-check context | Say “Alert RCB is described as an SMS system forwarded through mobile operators.” Do not claim it is Poland's only warning channel. | Future Polish cell-broadcast plans do not change the 2024 premise but should not be overstated. **[UNVERIFIED: exact current implementation timetable]** |
| P-27 | CAP does not natively preserve a CAMF ellipse, and a locally generated CAP file does not prove RCB/gateway acceptance. The gateway may regenerate geometry. | MAJOR | Sol, Wonder | Generate CAP only as a validated Test fixture, or cut it. Label original hazard and proposed target separately. | CAP may be dropped for time; JSON report is sufficient. |
| P-28 | Venue Wi-Fi, CDSE, tile servers, CDN assets, or a phone loading a web UI after enabling airplane mode can break the demo. | MAJOR | Sol, Wonder | Pre-download all data and basemap. Test with networking off. Cache/preload phone view. Record a 60–90 second fallback. | Local laptop failure remains; duplicate bundle on two machines. |
| P-29 | Python/GIS installation can fail because of version and binary-wheel issues, especially Rasterio/Python compatibility. | MAJOR | Sol | Pin versions, install Saturday morning, smoke-test GeoTIFF/CRS on both laptops, freeze environment and cache wheels. | A second laptop may still differ; use precomputed demo bundle as fallback. |
| P-30 | Fresh Code risk if Balloon Radar ingestion, OSNMA, receiver, or UI code is copied. Related-team pre-existing captures may also raise provenance questions. | BLOCKER | Wonder, Sol | Create a clean weekend repository, rewrite project code, use only public libraries/data, document dependencies, and ask organisers about pre-existing team captures. | Organiser interpretation may still restrict some reuse; obtain the ruling early. |
| P-31 | Kłodzko 2024 may be used by other flood teams, even though EWSS itself is unsaturated. “No AI idea used EWSS” is not evidence about the actual Warsaw field. | MAJOR | Sol, Wonder, Ranking | Differentiate through encoded-target benchmark and operator trade-off, not another generic Kłodzko map. Do not add an artificial second hazard unless it is genuinely cheap. | Another team could still choose EWSS; **[UNVERIFIED: rival census]**. Execution and practitioner input become differentiators. |
| P-32 | No civil-protection practitioner has validated the workflow. Past-winner analysis identifies practitioner involvement as especially valuable. | MAJOR | Wonder, Guidelines/past-winner notes | Use Saturday mentor slots to obtain one operator/vendor conversation and one quotable sentence. Label it feedback, not partnership. | A single quote does not prove demand. Do not inflate it into an LOI. |
| P-33 | Safety, liability, privacy, and accessibility requirements are absent from a production version. A tool that trades coverage against over-warning could create serious accountability questions. | MAJOR | Sol, Wonder | Explicit human approval, audit log, exercise mode, fail-closed unknown states, local-only mock location, no publication of raw logs with identifiers. Production requires authority acceptance testing. | Prototype remains unsuitable for operational use; state this plainly. |
| P-34 | QZSS sharing the CAMF payload does not mean the same radio interface, authority process, procurement, or receiver firmware. Dam/Seveso sales hooks are also unverified. | MINOR | Sol | Say only that parts of the payload codec may be reusable. Remove Japan/dam/Seveso from near-term revenue. | International expansion remains speculative. |
| P-35 | CAMF country filtering needs an actual country polygon. A country code alone does not let the demo test “inside ellipse but wrong country.” | MINOR | Sol, Wonder | Load a local Poland boundary from GUGiK PRG or a simplified fallback. Test inside/outside/wrong-country cases. | Boundary simplification can create border edge errors; keep test points away from the border unless testing that explicitly. |
| P-36 | Duration and library behaviours can be mishandled: unknown duration may require an all-clear; unknown library version must not produce invented instructions. | MINOR | Wonder, Sol | Implement expiry and unknown-library states exactly after checking v1.2. Do not claim full update/all-clear behaviour unless implemented. | Operational update semantics remain outside prototype scope. |
| P-37 | Exact submission artefacts and local rule interpretation are not established by the supplied general material. | BLOCKER operationally | Sol | Ask Blue Dot Solutions/organisers at kick-off for controlling checklist, Fresh Code interpretation, project visibility, location tag, and deadline mechanics. Publish and verify by 14:15 Sunday. | Late discovery can force reformatting; prepare repo, slides, video, and description regardless. |
| P-38 | Sentinel constellation statements can become outdated. Fact-check confirms Sentinel-1C+1D restored nominal six-day same-track repeat on 24 Jun 2026 and Sentinel-1A was retired 29 Jun 2026. | MINOR | Sol, Fact-check | Do not describe the 2024 case using the 2026 constellation. If GFM is mentioned, separate historical acquisition from current repeat capability. | Repeat time is not a valley-specific delivery guarantee. |

### 4.2 Discussion of the blockers

#### Blocker cluster A — The original product promises delivery it cannot demonstrate

The original design moves too easily between four different propositions:

1. Galileo is testing EWSS.
2. EWSS will become an operational service.
3. A phone can receive the alert.
4. The team's phone demonstrates that reception.

Only the first is established for the hackathon weekend, and even that is sporadic. The second is a plan for 2027. The third requires future device support. The fourth depends on undocumented encapsulation, handset behaviour, outdoor reception, and broadcast timing.

The corrected demo therefore starts with something the team controls completely: a real Copernicus polygon and a CAMF payload. That is not a retreat into simulation for its own sake. The payload's geometry changes because the real Copernicus input changes. The judge can inspect the encoded and decoded ellipse. That satisfies the need for a working system without pretending that a public warning was transmitted.

#### Blocker cluster B — “Optimal” originally meant the wrong thing

The design initially treats “96% coverage with lower over-warning” as obviously better. The specification behaviour identified by research-wonder points the other way: compute an ellipse that contains the target polygon. A civil-protection operator may legitimately ask who authorised a system to leave 4% of the mapped at-risk population outside.

The solution is not to delete population optimisation. It is to make the conflict visible:

- Spec Mode answers: “What is the smallest encodable ellipse that covers the whole mapped area?”
- Population Mode answers: “What would change if population distribution were prioritised, and exactly who would be missed?”

That turns a spec violation into the product's intellectual contribution. The human approval action is essential. It is both an accountability feature and a legal-risk reduction measure.

#### Blocker cluster C — CAMF conformance is not yet proven

CAMF v1.2 is the controlling document, but the team has not yet verified its full text against the implementation. A codec written from v1.1 and tested only against itself could be internally consistent and externally wrong.

The minimum credible standard by Sunday is:

- v1.2 document obtained and hashed;
- relevant field tables checked by two people;
- one payload broken down independently by hand;
- one independent decode by someone who did not write the encoder;
- test message type and placeholder provider;
- no claim of certification or full conformance.

If those conditions fail, the honest label is “experimental CAMF geometry codec,” not “official encoder.”

#### Blocker cluster D — The gateway may already solve the wrong version of the problem

The commercial design assumed that authorities receive EWSS but no tool to choose the ellipse. The reviews show that the service concept already includes ground-side CAP conversion and ellipse computation, and that STELLAR/ERAS-related work exists.

This does not automatically kill the business. It changes what must be sold:

- not “we invent ellipse conversion”;
- but “we let an operator or vendor inspect, compare, audit, and improve the conversion before it is committed.”

The critical unknown is whether the production gateway:

1. exposes the final ellipse;
2. permits operator override;
3. uses population-aware criteria;
4. retains an approved target through CAP conversion;
5. provides an audit trail;
6. can be benchmarked against an alternative.

If the answer is that it already does all six, the standalone product thesis fails. If it does only mechanical smallest-area conversion, Last Signal has a credible component opportunity.

#### Blocker cluster E — Retrospective data cannot be turned into a false warning timeline

EMSR756 is valuable precisely because it is a real observed Copernicus product. It becomes a liability if the team claims it was available before it was produced.

The honest claim is:

> “Using a later Copernicus observation of the 2024 flood, we test how that footprint would fit Galileo's future warning format.”

The dishonest claim is:

> “We would have warned Stronie Śląskie before the dam broke.”

The first survives an IGiK or Blue Dot judge. The second may collapse the whole presentation.

### 4.3 Reviewer disagreements and adjudication

#### Disagreement 1 — Does OSNMA authenticate EWSS?

- **Ranking position:** ordinary OSNMA authenticates navigation words, not the return-link field, so “OSNMA OK” does not authenticate the alert.
- **Research-sol position:** Service Notice #28 explicitly assigns ADKD=2 to EWSS authentication during the tests, but public tooling and the reserved-ADKD treatment prevent the team from claiming verification.
- **Research-wonder position:** essentially the same as Sol, with additional detail about MACLT 34 and delayed TESLA authentication.

**Adjudication: Sol and Wonder are right on the current service fact; the ranking is right on what ordinary navigation authentication proves.**

The reconciled statement is:

> EWSS test messages are intended to be authenticated through OSNMA ADKD=2, but ADKD=2 is reserved in the current public SIS ICD material and public tooling cannot be assumed to verify it. Authenticating ordinary navigation data is not the same as verifying the alert.

This is also consistent with fact-check.md, which confirms ADKD=2 test transmissions.

#### Disagreement 2 — Should the Android receiver be dropped or retained as a recorded-data decoder?

- **Research-sol:** Do not make the Android reference receiver a deliverable.
- **Research-wonder:** Cut it to an honest recorded-data reference decoder and phone display if the phone gate fails.

**Adjudication: Sol is right about the deliverable; Wonder is right about the optional stretch.**

The team should promise only the payload decoder. A recorded-data receiver may be demonstrated only if the capture and EWSS payload boundary are genuinely identified. The phone screen remains a preview, not evidence of reception. This preserves scope control without forbidding a lucky capture from becoming appendix evidence.

#### Disagreement 3 — Outage layer: delete it or keep a labelled regional shading?

- **Research-sol:** Delete the outage layer and weighting.
- **Research-wonder:** A gmina/powiat-level press-reported shading could be used to weight population if clearly labelled.

**Adjudication: Sol is right for the 48-hour prototype.**

The evidence supports a dated operator statement about major base-station problems, not a geospatial outage surface. Using it to alter population weights would manufacture analytical precision. Keep the story in the opening, but keep outage data out of the computation.

#### Disagreement 4 — Should the optimiser maximise population coverage or obey full containment?

- **Design position:** Optimise coverage versus over-warning.
- **Research-wonder:** The specified system behaviour is the smallest ellipse containing the whole polygon.
- **Research-sol:** Compare fairly, score decoded candidates, and lead with missed residents.

**Adjudication: Wonder is right about the baseline; the design's population idea remains valuable as an explicitly governed alternative.**

The product should not present partial coverage as automatically “optimal.” It should show both modes and force a human to accept any missed-population trade-off.

#### Disagreement 5 — Who is the buyer?

- **Design position:** Civil-protection authorities buy the authoring tool; chipset firms buy the receiver SDK.
- **Research-sol:** The plausible first customer is a warning-platform integrator's product organisation; an authority operator is the pilot user. Device SDK revenue should be removed from the base case.
- **Research-wonder:** Public-warning-system vendors and national integrators are primary; chipset test-vector work is a credible secondary revenue line.

**Adjudication: Sol and Wonder converge more than they disagree. The corrected buyer is the vendor/integrator; the authority is the user and validation partner.**

Research-sol is more conservative on SDK revenue and should prevail for the base-case forecast. Chipset work can be a later upside, especially with ChipCraft-type companies preparing for EUSPA testing, but it is not yet a proven first revenue line.

#### Disagreement 6 — Is the existing gateway an inconvenience or an existential threat?

- **Research-wonder:** ERAS/STELLAR create the existential jury question.
- **Research-sol:** The gateway owns conversion; pivot to comparison/QA unless the gateway already exposes equivalent optimisation and audit.

**Adjudication: Both are right. This is the project's largest commercial unknown.**

The design's “missing piece” language must be abandoned. The surviving thesis is narrower: population-aware preflight comparison, audit, training, and vendor integration. The Saturday mentor question—“Can an operator inspect or override the final ellipse, and can we benchmark against your converter?”—is a genuine go/no-go business test.

#### Disagreement 7 — Should a second hazard be added to escape Kłodzko saturation?

- **Research-wonder:** A dam-break or Seveso point-source case could differentiate the replay cheaply.
- **Research-sol:** Cut the second hazard; use a second flood AOI only as a robustness check after the main case works. Differentiate through the encoded-target benchmark.
- **Ranking:** Suggested a second hazard because Kłodzko is likely to be reused.

**Adjudication: Sol is right for build scope; the ranking is right about the presentation risk.**

Do not build a second hazard pipeline. If, and only if, the main case is complete, a static point-source polygon can be used as a five-minute input-swap robustness check. The primary differentiator should be the measurable encoded-ellipse comparison, not another dataset.

#### Disagreement 8 — How strong is the “zero convergence” advantage?

- **Ranking/design position:** No AI-generated team idea used EWSS, so rivals are unlikely to land there.
- **Research-sol:** The internal idea pool is not evidence about the Warsaw field.
- **Research-wonder:** EWSS itself is unsaturated, but Kłodzko replay is not.

**Adjudication: Sol and Wonder are right.**

EWSS is a genuine differentiator, but “no convergence” must not be presented as a researched market fact. The defensible claim is: “EWSS is a newly published service with a live test window; we are not aware of a comparable Warsaw entry.” Even that should be softened unless the team checks the public project list Saturday.

---
