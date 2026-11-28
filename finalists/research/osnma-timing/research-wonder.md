Verdict incoming — verifying every load-bearing OSNMA, timing and NIS2 claim against primary sources before I tear the design apart.Core OSNMA facts check out — OSNMA is real but only authenticates messages, not timing. Now probing holdover, EGNOS and incumbent receivers that already ship this.# OSNMA Timing Integrity + NIS2 Incident Evidence — Hard Review

**Review time: Saturday 28 Nov 2026, early morning. Submission: Sunday 29 Nov 15:00 CET.**
**Merged concept reviewed:** vendor-neutral timing-trust evidence layer (ChronoShield / ClockWitness / ClockEvidence / CERTUS) — beside an existing receiver, cross-check Galileo OSNMA authentication against an independent local clock reference and receiver observables, classify the event, emit a signed incident-evidence bundle + pre-filled (not auto-filed) KSC/NIS2 24 h early-warning draft, plus an EN 16605-style scorecard.

This is the strongest version. Everything below is written against it. Where the four source designs contradict it (auto-filing, "PNT Trust Score", live spoofing, EGNOS cross-checks, internet NTP references), those claims are treated as defects to delete, not features to defend.

---

## 0. What Is Right (brief, so you stop re-litigating it)

- **OSNMA is real and operational.** It was declared operational on 24 July 2025, and lets users verify navigation information comes from Galileo and has not been tampered with. This is not vapourware; the jury cannot kill you on "does it exist".
- **The killer line is correct:** "authenticated — but still wrong." OSNMA authenticates the navigation *message*, not the ranging signal; a record-and-rebroadcast (meaconing) attacker passes it, so the OSNMA verdict and the clock verdict *must* be separate states. ClockWitness's three-state design (auth / clock agreement / reference health, fail to `unknown`) is the technically honest core. Keep it verbatim.
- **The threat context is real and current.** Poland's National Institute of Telecommunications reports a "systematic and drastic increase" in intentional GNSS interference since the start of 2026, with full-band disruption on 63% of days in 1–19 August around Gdańsk. Relevance is not your problem.
- **EN 16605 framing is real.** EN 16605:2024 specifies Galileo timing-receiver requirements including OSNMA processing and AGC-based anti-jamming/anti-spoofing. A conformance scorecard is a legitimate, citable output format.
- **OSNMAlib exists and is the right tool** (details below). The demo is buildable in 48 h *if* scoped as replay-only.

Everything else in the four source documents ranges from sloppy to demo-killing. Details:

---

## 1. Technical Implementation, Component by Component

### 1.1 OSNMAlib (`github.com/Algafix/OSNMA`) — REAL, but with three traps

The library is a real open Python implementation of the OSNMA protocol, EUPL-1.2 licensed. It verifies the DSM-PKR public key, the TESLA root key, MACK structure and ADKD 0/4/12 tags. Supported inputs: Septentrio SBF (file and live IP), u-blox UBX (file and live serial), live Galmon aggregated data, GNSS-SDR via UDP, and Android GNSSLogger files. Python 3.10–3.12, Linux and Windows.

**Trap 1 — Public Key ID 2 rotation (MAJOR, becomes BLOCKER on stage).** OSNMA updated its Public Key from ID 1 to ID 2 on 2025-12-10 10:00 UTC, confirmed by GSC performance reports: PKID 2 applicable as of 2025-12-10T10:00:00Z. Any capture recorded before that date needs PKID 1; anything after needs PKID 2; OSNMAlib ships both keys in the run folders. If your replay file and your configured key mismatch, you get authentication failures in a clean scenario — the worst possible live-demo failure, because it looks exactly like your product crying wolf.
**Fix (30 min, Saturday):** pin capture date ↔ PKID in the replay adapter config, assert it at startup, and print `PKID=2, capture=YYYY-MM-DD` on the demo screen. Do not let anyone "just try another file" on Sunday.

**Trap 2 — GSC trust material is registration-gated.** The public key and Merkle tree root must be downloaded from the European GNSS Service Centre under GSC Products > OSNMA_PUBLICKEY / OSNMA_MERKLETREE, and registration is required. GSC confirms crypto material is available to registered users via the website and an OSNMA SFTP server. One third-party tutorial warns key-access confirmation "may take around a week" — that figure is from the old test-phase flow and may be stale, but you cannot verify that from the venue.
**Fix:** OSNMAlib's `custom_run/` folder already contains the current Merkle Tree and Public Key downloaded from GSC, plus a runnable `current_config.sbf`. Use the bundled material for the demo; treat a fresh GSC download as a nice-to-have, never as critical path. If a team member has a GSC account, download PKID 2 `.crt` + Merkle XML Saturday morning as provenance dressing — screenshot it for the pitch — but the demo must run on bundled files.

**Trap 3 — Galmon live feed is a P2P side-show, not a backbone.** The Galmon feed streams from a hardcoded IP (86.82.68.237, TCP 10000), aggregates receivers worldwide, and packets occasionally arrive out of order. OSNMAlib's own README warns "there may be some problems with the data received from galmon due to the P2P nature of this service" and output arrives roughly every 30 s.
**Fix:** Galmon = optional "live" tab if venue Wi-Fi cooperates. The scored demo is a local replay file. Also note OSNMAlib.eu publishes a live OSNMA status JSON from a KU Leuven receiver — usable as a sanity cross-check screenshot, not as an input.

**Alternative worth knowing:** `galileo-osnma` (Rust, docs.rs, v0.11.6) reads the same Galmon transport and u-blox sources. Do **not** switch — Python OSNMAlib is the fastest path for a Python team — but cite it if a juror asks whether OSNMAlib is a one-student toy. It's not; there's an ecosystem.

**Fresh-code note:** cloning OSNMAlib pre-weekend for *verification* is fine (see §6), but your replay adapter, correlation engine and export code must be written during the event. Using the library as a library is explicitly the allowed pattern.

### 1.2 Galileo HAS, SAS, EGNOS — three claims to delete

- **Galileo HAS (CERTUS claims "cm-level authenticated position where needed") — MAJOR / false.** HAS is a PPP correction service; it is not an authentication service and does nothing for a *timing* incident record. It adds a dependency, a second data path, and a ChipCraft question you cannot answer. **Fix: delete HAS entirely.** It is not in the merged design.
- **Galileo SAS / "SASlib" (ChronoShield roadmap slide) — MAJOR if presented as near-term, MINOR as roadmap.** SAS internal testing began 3 Dec 2025 with E6-C encryption on L3 satellites; the first real-world authenticated position fix happened 16 Sep 2026 at Jammertest with five satellites for two hours, and Initial Service is targeted for 2027. There is no public "SASlib" you can integrate this weekend. **Fix:** one roadmap sentence — "SAS adds ranging authentication from 2027; our evidence schema has a field reserved for it" — and nothing more. Any slide implying SAS is usable now will be destroyed by ChipCraft.
- **EGNOS as cross-check (ChronoShield: "Galileo vs. EGNOS/GPS inter-system residuals") — BLOCKER if left in.** EGNOS augments **GPS L1 C/A** — it provides corrections and integrity for GPS space vehicles. It is not an independent Galileo timing reference, and "EGNOS residuals catch meaconing" is not a defensible mechanism. **Fix: delete EGNOS from the detection logic.** EGNOS may appear once, honestly, as "future multi-source input". If you keep it in the pipeline diagram, the GNSS engineers will spend your whole Q&A on it.

### 1.3 Receivers — CERTUS names a part that doesn't exist as described

- **"u-blox ZED-F10T" (CERTUS) — MAJOR factual error.** The shipping OSNMA timing part is the **NEO-F10T**: a dual-band timing module with built-in Galileo OSNMA, secure boot and T-RAIM, aimed at 5G timing, mass production with TIM 3.02 firmware as of the Apr 2026 datasheet. If you say "ZED-F10T" to ChipCraft, you lose credibility in one word. **Fix:** cite NEO-F10T (and Septentrio mosaic-T) as *production integration targets*, not demo hardware.
- **Septentrio mosaic-T** is real, OSNMA-capable, and retail-visible: ~€390–470 for a timing dongle variant, ~€1,195 module list price. Still: **do not put hardware procurement on the critical path** (ClockWitness's own go/no-go says this, correctly). A €400–1,200 receiver bought Saturday, with Warsaw indoor sky view, learning OSNMA cold-start live, is how demos die. Replay only. If a mentor lends you a receiver, it's a prop on the table with a pre-recorded SBF file from *that* receiver — which OSNMAlib reads natively.
- **"u-blox publishes reference OSNMA code / verification API" (CERTUS) — MINOR exaggeration.** u-blox exposes OSNMA configuration/status via UBX (e.g. UBX-MGA-GAL-OSNMA_PUBKEY / MERKLE assistance messages on gen-9 parts); the receiver verifies internally, you don't get a raw-tag verification API to build a product on. Your product correctly sits *beside* the receiver consuming its status + observables — say exactly that.

### 1.4 Independent reference: the single most attacked component

This is where the ranking's "known problems" are right, and where ChronoShield/CERTUS are weakest.

- **Internet NTP / e-CzasPL as reference — BLOCKER.** GUM itself states NTP synchronisation uncertainty ranges "from tenths of a second to single milliseconds, and in some cases even up to several microseconds" depending on link quality. NTP over the internet typically holds a few ms. Your sector thresholds are 1–1.5 µs (see §2). An internet-NTP reference is **three orders of magnitude too coarse** to detect a 45 µs meaconing delay claim, let alone a 2 µs drift. Any slide showing NTP/e-CzasPL-over-internet as the µs reference ends the technical discussion.
  **Fix (the only honest one):** the reference in the demo is a **clearly labelled recorded/simulated local 1PPS offset trace** (ClockWitness already concedes this), and the production claim is "local holdover oscillator or PTP grandmaster *at the site*, whose quality is part of acceptance testing". PTP with hardware timestamping genuinely reaches sub-µs — but only on a PTP-aware local network, and only if the PTP grandmaster isn't itself GNSS-disciplined by the same compromised receiver. Say that sentence before the jury does.
- **Holdover switching (ChronoShield "fires SNMP trap, locks node into OCXO holdover in 5 s") — MAJOR overclaim.** A good OCXO drifts roughly 1–10 µs per 24 h of free-run; rubidium ~100–500 ns over the same period. Holdover is a *bridge of hours*, and real timing appliances (which the buyer already owns) do the actual switchover. Your software does not "lock" a substation clock; it *recommends* holdover and *records* that it did. **Fix:** rename to "holdover recommendation webhook (mock in demo)". The moment you claim actuation of grid timing kit, the cyber-defence jurors will ask about your safety case, and you don't have one.
- **"Second receiver as independent reference" — MAJOR conceptual flaw** (ClockWitness already flags it; enforce it). Two receivers under the same sky share the same jamming/meaconing exposure. In the classifier, receiver #2 is *corroboration*, never *reference*.

### 1.5 "PNT Trust Score ∈ [0,100]" — delete it (MAJOR)

A weighted composite score is the one artefact in ChronoShield that a technical jury will actively punish: the weights are invented, the score hides exactly the OSNMA-vs-clock distinction that is your differentiator, and "99 → 18" is theatre, not evidence. **Fix:** three independent verdicts with explicit thresholds and `unknown` states (ClockWitness design), plus an EN 16605-style checklist. This is also your anti-saturation move (§6).

### 1.6 Evidence signing, SIEM, report generation — feasible, two cuts

- **ES256-signed JSON bundle — fine.** Standard `cryptography` (pyca) ES256 over a canonicalised JSON payload + input hashes + threshold config + event timeline is a Saturday-afternoon build. Include an independent verify script the jury can run — ClockWitness promises this; it's cheap and it's your best Execution-criterion artefact. **MINOR risk:** canonicalisation bugs (key ordering/float formatting) making your own verifier fail on stage. Fix: sign the *exact bytes* of the exported file, hash with SHA-256, verify offline in rehearsal.
- **Wazuh live integration (CERTUS) — MAJOR scope risk.** Wazuh is a real open-source SIEM, but standing up a manager + agent + custom rules in the remaining hours buys you a fragile demo and zero jury points that a mock webhook doesn't. **Fix:** cut Wazuh. Emit a CEF/JSON event to a local mock SIEM endpoint (a 30-line FastAPI receiver that displays the alert). Say "Wazuh/Splunk via webhook in production" in one sentence.
- **PDF generation (WeasyPrint/ReportLab) — MINOR.** Fine, but build the JSON first; PDF is a rendering. Generate the PDF from the signed JSON so the hash story is consistent.
- **MQTT/serial receiver adapters (ClockEvidence) — MINOR.** Plausible in production; in the demo, replay files only. Don't write a serial adapter Saturday unless replay already works.
- **Merkle log of per-second verdicts (CERTUS) — MINOR over-engineering.** A hash-chained JSONL is 20 lines and gives you "tamper-evident" honestly; a Merkle tree is a Sunday-morning time sink. Hash chain, not Merkle.

---

## 2. Correctness of the EU-Space Signal Usage

What OSNMA actually proves, stated precisely (put this on slide 2, verbatim logic):

| Claim in designs | Verdict | Evidence |
|---|---|---|
| OSNMA authenticates Galileo nav messages (ephemeris, clock corrections) on E1-B I/NAV | **True** | OSNMA authenticates Open Service data through the I/NAV on E1-B |
| OSNMA proves received time-of-arrival / UTC accuracy at µs level | **False — BLOCKER if claimed** | TESLA delayed disclosure: data is authenticated only after key disclosure, retrievable in one 30 s subframe; receivers need loose sync of 30–300 s depending on mode. A protocol that *assumes* you already know time to ±30 s cannot *certify* µs. OSNMAlib defaults TS=30 s |
| OSNMA defeats forged-message spoofing | **True** | It defeats an attacker fabricating orbits/clock data |
| OSNMA defeats meaconing/replay | **False** | "It does not stop an attacker who records and rebroadcasts genuine Galileo signals with a delay"; tests show OSNMA receivers reporting meaconed signals as authentic |
| OSNMA defeats jamming | **False (by design)** | Jamming = no signal = no authentication. Your product's jamming verdict is "signal lost + reference holds", i.e. an *availability* record, not a crypto verdict. State it that way |
| Time-to-first-authenticated-fix is instant | **False** | OSNMAlib reports TTFAF as a metric and achieves as low as 44 s in hot start with optimisations. Your UI must show a `WARMING_UP / NOT_YET_AUTHENTICATED` state — which is, conveniently, a third demo case |
| 5G needs ±1.5 µs; PMU ±1 µs; MiFID II 100 µs | **Substantially true, fix the 5G nuance** | TDD ±1.5 µs vs common reference and PMU 1 µs are documented; MiFID II RTS 25: 100 µs / 1 µs granularity for HFT. **But** advanced 5G features push to ±130 ns / ±65 ns — don't let a telecom juror catch you presenting 1.5 µs as "the 5G requirement" full stop. Say "±1.5 µs baseline TDD; tighter for CoMP/CA — which is why the reference must be local PTP/oscillator, not NTP" |
| ChronoShield's "45 µs meaconing delay" demo | **Plausible as simulation, mislabelled as detection** | A 45 µs offset is detectable *only* against a local reference with ≪45 µs error — i.e. your labelled simulated trace. Fine. But the demo injection is a *trace edit*, not a signal attack; label it "simulated clock deviation on recorded reference trace" or ChipCraft will (correctly) call it a spreadsheet attack |

**Net correctness position:** the merged design's epistemics are sound *iff* the three verdicts stay separate, authentication delay (≥30 s subframe cadence) is shown in the UI, and every timing number is tied to the reference's stated error budget. The single most important sentence in your pitch: **"OSNMA tells us the message is Galileo's; only the independent local clock tells us whether to believe the time; when either is missing, we say `unknown`."**

---

## 3. Demo Risk (Sunday 15:05, venue Wi-Fi, jury watching)

| # | Failure mode | Severity | Mitigation executable before Sunday 15:00 |
|---|---|---|---|
| D1 | PKID 1/2 mismatch → clean trace shows AUTH FAIL | **BLOCKER** | Pin capture↔key (§1.1); startup assertion; rehearse with the *exact* files in the *exact* repo that will be submitted |
| D2 | Live Galmon feed stalls / venue network blocks raw TCP 10000 / out-of-order packets corrupt a subframe | **MAJOR** | Demo is 100% local replay. Galmon only as an unprompted bonus tab. Pre-download everything Saturday |
| D3 | GSC website login/registration needed mid-demo | **MAJOR** | Never. Bundled OSNMAlib keys on disk (§1.1); screenshot of GSC product page for provenance |
| D4 | Team attempts live RF spoofing/jamming demo (CERTUS "SDR replay attack on stage") | **BLOCKER — legal** | Deliberate GNSS interference is banned under ITU rules and national law in most jurisdictions; GPS spoofing/jamming is "illegal in most jurisdictions and is not permitted under any product configuration". Transmitting on Galileo E1 in a Warsaw conference venue is a non-starter regardless of shielding claims. **All attacks are file/trace replays. Say so proudly: "we never transmit."** |
| D5 | OSNMAlib cold-start on replay takes ~a minute before first authenticated verdict; dead air on stage | **MAJOR** | Pre-warm: start the replay before the pitch segment, or use a warm-start config (saved PK + KROOT) and show the state machine honestly. Turn the delay into content: "authentication is retrospective by design — TESLA keys arrive ≥30 s late" |
| D6 | Reference trace and OSNMA timeline misaligned (timestamps from different clocks in your own demo data) | **MAJOR** | Single demo-data generator script writing both streams from one synthetic clock; unit-test the three cases (clean / auth-OK+clock-bad / auth-insufficient) Saturday night; freeze the fixtures |
| D7 | ES256 verifier fails on stage due to canonicalisation | **MINOR→MAJOR live** | Sign raw bytes; run the jury-verify script in rehearsal on the *submitted* artefact |
| D8 | Wazuh/PTP "live" services not up | **MAJOR if attempted** | Cut (§1.6). Mock webhook receiver only. No PTP grandmaster theatre without hardware timestamping NICs you don't have |
| D9 | Dashboard shows a map / red-green "attack!" screen identical to rivals | **MAJOR (score, not function)** | Hero artefact on screen = the signed evidence bundle + timeline, inspectable. No map at all. (See §6) |

**Offline fallback (non-negotiable):** entire demo — replay file, keys, fixtures, built frontend, generated sample bundle — runs from one laptop with Wi-Fi off. Record a 90-second screen capture Sunday ~12:00 as the last-resort pitch track.

---

## 4. Jury Pushback — First Hard Question per Archetype

**ChipCraft (GNSS chip engineers):** *"OSNMA authenticates data, not the ranging code. Your 'meaconing detection' is just clock comparison that a Meinberg box already does. What, precisely, did Galileo give you?"*
Prepared answer: OSNMA gives the *forged-message* verdict and, crucially, authenticates the satellite clock-correction/ephemeris data the clock comparison is judging — without it, a drift verdict can't distinguish "attacker forged the corrections" from "attacker delayed the signal". Your product is the *evidence join* of the two verdicts, not either sensor. Concede the receiver vendors verify OSNMA internally (Oscilloquartz integrated OSNMA into its timing platforms in July 2026 using u-blox technology); your layer is vendor-neutral *across* a mixed fleet. If you instead pitch "we verify OSNMA ourselves in software" as the product, they'll ask why a buyer wouldn't buy the receiver that already does it — have the fleet-evidence answer ready.

**Cyber Defence Forces / WAT:** *"Your agent auto-switches critical timing infrastructure and auto-files to S46. Show me the authorisation model, the fail-safe, and what happens when* your *agent is the compromised component."*
Prepared answer: we neither switch nor file. We *recommend* holdover via webhook (site's own appliance acts) and *pre-fill* a draft a human submits. The agent is read-only against the timing chain; the signed bundle includes our own software/config hash so a compromised agent is itself detectable. If any team member says "auto-file" or "auto-switch" on stage, this question ends you — ChronoShield's and CERTUS's wording must be purged from slides, README and TAIKAI text.

**IGiK (remote sensing academics):** — your weakest-fit juror; they will test whether the EU-space usage is load-bearing or decorative. *"Remove Galileo. Your clock-comparison still works against GPS. Why is this a Galileo product?"*
Prepared answer: because only Galileo gives you *cryptographic* nav-data authentication as an open service — the auth verdict (and its absence/`unknown` state) exists only because of OSNMA on E1-B I/NAV. The clock comparison alone can say "disagreement"; it cannot say "the message itself was forged". Offer the ablation demo: same trace with OSNMA processing disabled → classifier degrades to `unknown` on the forged case. (Build this toggle Saturday; it's ~1 hour and it's your best science-juror artefact.)

**Scanway (space optics):** — likely your business-realism proxy. *"Who signs the first cheque, for what line item, replacing which existing spend?"* See §5. If your answer is "38,000 KSC entities", you fail. One named beachhead (Baltic energy/telecom timing fleets), per-site evidence/audit pricing, integrator channel.

**Blue Dot Solutions (EO/GNSS-interference locals):** *"We monitor GNSS interference from Gdańsk. The Institute's station already documents this. What do you add beyond another event log?"*
Prepared answer: they document the *RF environment*; you produce the *per-site, signed, regulator-shaped incident record* inside the operator's SOC workflow, joining OSNMA state to *that site's* clock behaviour. Different artefact, different buyer. Do not claim interference measurement novelty — claim evidence/workflow novelty.

**ESA BIC Poland:** *"Incumbents ship this. What's defensible in 24 months?"*
Honest answer: nothing in the crypto; the defensible asset is (a) vendor-neutral fleet evidence format + EN 16605 scorecard mappings, (b) KSC/S46-shaped reporting workflow for Polish/EU operators, (c) an evaluation corpus of labelled incident traces. Say you'll pursue an integrator/LOI before Demo Day. "We built OSNMA verification" as a moat claim is dead on arrival — Meinberg already supports Galileo OSNMA with automated key renewal and Microchip sells a BlueSky GNSS Firewall as an overlay protecting deployed timing systems.

---

## 5. Buyer, Business Model, Legal/Regulatory, Procurement

**Regulatory reality check (several load-bearing claims in the designs are wrong or stale):**

- **"April 2027 fines cliff" — overstated (MAJOR).** The KSC amendment (Dz.U. 2026 poz. 252) entered into force 3 Apr 2026; ISMS/S46 obligations bite 3 Apr 2027; **first audit and financial penalties only from 3 Apr 2028**, with penalties expressly not imposable until two years after entry into force. The compliance-work window is real (that's when budgets for tooling open), but any slide saying "fines from April 2027" is factually wrong and a Polish juror may know it. Fix wording: "obligations live Apr 2027; enforcement from Apr 2028 — operators are buying evidence capability *now* to be auditable then."
- **"~38,000 entities / ~100k entities" (ChronoShield vs CERTUS) — the two designs disagree with each other; neither is sourced on your slides.** Don't quote either number without the biznes.gov.pl/ISAP citation in the fact-check file. Safer: "essential + important entities under the amended KSC" and name sectors, not counts.
- **NIS2 24 h early warning — real, but conditional (BLOCKER for "auto-file").** Article 23 requires early warning within 24 h *of becoming aware of a significant incident*, then notification within 72 h and final report within one month. "Significant" means caused/capable of severe operational disruption or financial loss, or affecting others — a *human legal judgement* about impact, not a threshold crossing in your rules engine. A GNSS anomaly that holdover absorbed with no service impact may not be reportable at all. **Your product pre-fills; a named human decides and submits.** Every "auto-file / auto-generate legally compliant report" phrase (ChronoShield, CERTUS) must become "pre-filled draft + evidence annex, human-approved".
- **S46 has no public API/schema you can target (MAJOR).** In Poland, significant incidents are reported through S46 to the competent sectoral CSIRT, with CSIRT NASK/GOV/MON as interim recipients. No public S46 JSON schema or submission API is documented. ChronoShield's "S46 JSON export" and "packages IoCs into S46 format" are invented formats. **Fix:** label your export "S46-*ready* draft (fields aligned to Art. 23 early-warning content: malicious-act suspicion, cross-border impact) — final submission via S46 portal by the operator". One slide, honest label.
- **Personal executive liability (CERTUS) — tone down.** Polish KSC does include head-of-entity liability with fines up to 300% of remuneration, but penalties apply from 2028 (§above). "Manufactured by law" urgency is a 2027–28 story, not a Nov-2026 cheque.
- **Pricing sanity:** ChronoShield's €400/node/month + €2,500/month platform vs CERTUS's €150–400/site/month are both invented (the GPT leg at least admits pricing is "a proposed pilot price, not evidence of willingness to pay"). The merged, defensible offer: **€12–25k integration pilot → per-site annual evidence/monitoring licence** (ClockWitness's proposal — the most honest in the set). €4–8M "SAM from 1% of 38,000 entities" — delete; it's arithmetic, not a market.
- **Procurement reality:** TSOs/DSOs and MNOs buy timing resilience from Meinberg/Safran/Microchip/Oscilloquartz and integrators, on multi-year cycles. A startup sells (a) to the *integrator* as an evidence module, or (b) a paid pilot to one operator's timing/SOC team. Your pitch must name the channel (SIEM/timing integrator) as primary — CERTUS's B2B2B defence is correct; make it the headline model, not a Q&A fallback.
- **Demo-data legality:** replaying recorded I/NAV and editing clock traces is lawful; transmitting anything on E1 is not (§3, D4). Also do not name real operators (Energa/PSE/Orange) as demo sites — "a mock substation profile" only; implying a real operator's live timing feed on stage is a fabrication a local juror can falsify.

---

## 6. Rule Compliance & Saturation

**Fresh Code:** the rules state all code must be created by the team during the hackathon weekend, while publicly available/openly licensed APIs, SDKs, frameworks and libraries are permitted. Implications: OSNMAlib, `cryptography`, FastAPI as *libraries* = compliant. Pre-written adapters/engines = not. Pre-downloaded *data* (test vectors, keys, captures) is the standard grey zone — mitigate by (a) timestamps in git showing project code written Sat–Sun, (b) README stating what is library, what is data, what is fresh code. ChronoShield's "Friday night: clone and verify" plan is fine *as verification*; don't commit pre-written pipeline code.

**EU-space requirement:** satisfied *actively* only if real Galileo I/NAV data flows through real OSNMA verification in the demo (OSNMAlib on a real capture/test vector with correct PKID). If the "OSNMA status" in your demo is a hand-authored flag in a synthetic JSON, you are a timing-dashboard team wearing a Galileo badge, and IGiK/ChipCraft will say so. The recorded-capture replay is what makes Galileo load-bearing. Label simulated *clock* traces as simulated; never label the *navigation data* as simulated if it's a real capture — that distinction is your credibility.

**Saturation (treat as context per instructions, but plan for the room as it is):** the ranking records this as the pool's most convergent idea — top pick of multiple independent generators, present in every leg — with past-podium adjacency (GNSS spoofing detection placed at a recent defence edition). Assume ≥3 rival teams pitch "OSNMA + NIS2 + red screen". Your only separations, all executable: (1) no map, no composite score — three verdicts + `unknown`; (2) the "authenticated but clock wrong" case as the *hero*, with delayed-authentication state visible; (3) a jury-runnable signature verifier; (4) the OSNMA-off ablation toggle; (5) EN 16605 scorecard language. If your demo looks like a SOC dashboard going red, you are tied with every rival and Execution decides it on polish you may not win.

---

## 7. Consolidated Problem Register (severity · evidence · fix)

1. **BLOCKER — "Auto-file NIS2/S46" + "auto-switch to holdover" claims.** NIS2 reporting attaches to a human-judged *significant* incident; no public S46 API exists. *Fix (1 h):* global find-replace to "pre-filled draft, human submits" / "holdover recommendation webhook"; update slides, README, TAIKAI.
2. **BLOCKER — Internet NTP/e-CzasPL as µs reference.** GUM's own NTP uncertainty is ms-class vs 1–1.5 µs thresholds. *Fix:* reference = labelled recorded local 1PPS trace in demo; production = on-site oscillator/PTP with stated error budget; PTP sub-µs only with HW timestamping.
3. **BLOCKER — Any live RF spoof/jam element.** Illegal transmission risk. *Fix:* replay-only; "we never transmit" as a stated design principle.
4. **BLOCKER — PKID mismatch risk on replay.** PKID 2 from 2025-12-10; OSNMAlib ships both keys. *Fix:* pinned config + startup assertion + rehearsal on final artefacts.
5. **BLOCKER — EGNOS as Galileo cross-check.** EGNOS augments GPS L1, not Galileo timing. *Fix:* remove from detection path.
6. **MAJOR — Composite "PNT Trust Score".** Invented weights hide the core distinction. *Fix:* three verdicts + `unknown` + thresholds shown.
7. **MAJOR — OSNMA ⇒ timing-truth implication anywhere in copy.** TESLA needs ±30 s loose sync; meaconing passes OSNMA. *Fix:* §2 wording; show auth latency (≥30 s subframe, TTFAF ~44 s hot) in UI.
8. **MAJOR — "ZED-F10T" + HAS + SAS-now claims.** Real part is NEO-F10T with OSNMA; SAS is a 2026 test, 2027 service. *Fix:* correct part number; HAS deleted; SAS one roadmap sentence.
9. **MAJOR — Wazuh + live PTP + serial/MQTT adapters in scope.** *Fix:* mock webhook; replay adapters only; Wazuh named as production integration.
10. **MAJOR — "Fines cliff April 2027" + entity-count numbers.** Penalties from 3 Apr 2028. *Fix:* corrected timeline slide.
11. **MAJOR — Galmon as demo backbone.** P2P feed, out-of-order packets, hardcoded endpoint; author's own caveat. *Fix:* offline replay; Galmon optional.
12. **MINOR — Merkle tree, HAS, GNSS-SDR, Android inputs, PDF-first build.** All cut or deferred; hash-chained JSONL + JSON-first export instead.
13. **MINOR — GSC registration latency uncertainty.** Third-party flows warn of slow confirmation; GSC material is registration-gated. *Fix:* bundled OSNMAlib keys; fresh download optional.

**Where designs were right (credit on the record):** ClockWitness's three-case demo, fail-to-unknown, "don't make hardware procurement critical path" go/no-go, and pilot pricing; Kimi ClockEvidence's "OSNMA failure alone never constitutes an attack verdict" and antenna-fault negative control; CERTUS's B2B2B integrator channel; the wildcard pick's vendor-neutral fleet-evidence + EN 16605 scorecard framing. The merged build is those four, minus everything listed above.

---

## (a) Prioritized Fix List — Top 10

1. Purge "auto-file / auto-switch / legally compliant report" everywhere → "pre-filled draft, human submits; holdover *recommendation*". (§7.1)
2. Freeze demo data: one real I/NAV capture, correct PKID (assert at startup), three rehearsed cases incl. `unknown`. (§7.4)
3. Replace Trust Score with three separate verdicts + explicit thresholds + auth-latency state. (§7.6/7.7)
4. Reference = labelled recorded local 1PPS trace; delete internet-NTP/e-CzasPL as µs reference from all diagrams. (§7.2)
5. Delete EGNOS cross-check, HAS, SAS-now, "ZED-F10T"; correct to NEO-F10T/mosaic-T as production targets. (§7.5/7.8)
6. Replay-only demo, fully offline; "we never transmit" slide line; 90 s screen-recording fallback. (§7.3)
7. Cut Wazuh/PTP/serial scope → mock SIEM webhook; hash-chained JSONL; ES256 bundle + standalone jury verifier (test it). (§1.6)
8. Build the OSNMA-off ablation toggle (degrades forged case to `unknown`). (§4, IGiK)
9. Fix regulatory slide: obligations Apr 2027, penalties Apr 2028; drop entity counts and SAM arithmetic; pilot pricing €12–25k → per-site licence via integrators. (§5)
10. Fresh-code hygiene: git history from Saturday, README separating library/data/fresh code; TAIKAI text matching the honest claims. (§6)

## (b) Three Things to Verify First on Saturday Morning

1. **OSNMAlib end-to-end on your exact capture:** `pip install -r requirements.txt` on Python 3.10–3.12, run `custom_run/run.py` and one replay with the *date-correct* PKID (PKID 2 for post-2025-12-10 data), and confirm a clean AUTHENTICATED verdict + TTFAF number. If this isn't green by Saturday noon, nothing else matters — fix this before writing any UI.
2. **The three demo fixtures from one generator:** clean / auth-OK+clock-drift / auth-insufficient traces, time-aligned, with the classifier emitting the intended verdicts and `unknown` where designed. Freeze the files; no Sunday-morning regeneration.
3. **The signed bundle round-trip:** export ES256-signed JSON for the drift case and verify it with the *standalone* verifier script on a second laptop (or clean venv), Wi-Fi off. If the jury can't verify, your Execution artefact is a screenshot.

## (c) Verdict: **CONDITIONAL GO**

The concept survives hard review because its physics and its regulation are both real: OSNMA is operational and genuinely proves nav-message authenticity — and genuinely *cannot* prove µs timing, which is exactly the gap a vendor-neutral, three-verdict evidence layer with a local reference and an EN 16605-shaped, human-submitted KSC draft can honestly fill, against a documented 2026 Baltic interference surge and a 2027–28 Polish compliance build-out. It is a GO only on the merged, de-hyped specification above: replay-only with correct PKID, no auto-filing, no auto-switching, no Trust Score, no EGNOS/HAS/SAS dressing, no live RF. If Saturday-morning check #1 fails and cannot be fixed by noon, or if the team insists on the ChronoShield/CERTUS "auto-report + trust score + live attack" version, this becomes a **NO-GO** — that version is factually wrong on its reference clock, its regulator interface and its legal claims, and ChipCraft plus the cyber-defence jurors will dismantle it in the first two questions.
