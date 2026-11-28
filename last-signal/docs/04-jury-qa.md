# Last Signal — jury Q&A (from the project dossier, unchanged)

## 7. Jury Q&A

### 7.1 GNSS chip engineers — ChipCraft archetype

#### Q1. “Show me the unmodified E1-B pages containing your emergency warning. What exactly did Android give you?”

**Honest answer**

> “We are not claiming that this prototype received an EWSS message. Our mandatory demo starts at the CAMF payload boundary. Android can expose Galileo I/NAV messages on some devices as 228-bit records, but navigation-page availability is device-specific, and ordinary I/NAV pages do not prove that the return-link EWSS payload was exposed. We ran a capture gate; unless we can identify the complete recorded pages and expected decoded fields, we do not present the phone as a receiver.”

If a genuine capture was obtained:

> “Here is the unmodified log, device/build/logger metadata, timestamps, and the mentor-supplied expected decode. We classify it as a recorded test EWM with authentication not verified unless ADKD=2 verification was actually completed.”

#### Q2. “Which word or page carries the 122 bits?”

**Honest answer**

> “CAMF is the 122-bit payload format. The historical Galileo path uses the E1-B I/NAV SAR/return-link field, with 22 bits in a nominal page and long return-link framing. But the exact 2026 test encapsulation and receiver guideline were not available to us as a public production ICD. That is why we did not build the product on an assumed page layout.”

#### Q3. “Your ellipse looks rotated. Did you confuse compass bearing with CAMF azimuth?”

**Honest answer**

> “That was one of our unit tests. CAMF azimuth is measured from East toward North. We convert from GIS bearing using `azimuth_camf = 90° − bearing_from_north modulo 180°`, test the inverse, and render only the ellipse reconstructed by the decoder from integer codes.”

#### Q4. “How do you test whether a receiver is inside the ellipse?”

**Honest answer**

> “Not in raw degrees. We use a local azimuthal-equidistant projection centred on the ellipse, with geodesic checks for edge cases. The population calculation is separate and is done by projecting the ellipse into the GHSL native grid.”

#### Q5. “Can this run in the background on a locked phone?”

**Honest answer**

> “Not in this prototype, and we do not claim production handset behaviour. Android navigation callbacks in our test context require a suitable device, permissions, GNSS enabled, and a foreground client. Production EWSS display is a chipset and operating-system responsibility.”

---

### 7.2 Remote-sensing academics — IGiK archetype

#### Q1. “Is your flood polygon the peak flood, a forecast, or a later observation?”

**Honest answer**

> “It is a later observed-event product from EMSR756. We show the sensor, acquisition time, product version, and release time. It is a reference observation for retrospective targeting, not a peak-extent guarantee and not a forecast.”

#### Q2. “What did you know on 14 September?”

**Honest answer**

> “Not this polygon. EMSR756 was activated on 13 September and products arrived at different times, with some AOI work still in progress days later. A real first warning would need forecast or national hydrology inputs available to an authorised partner. Our prototype tests the targeting step after a reviewed polygon exists.”

#### Q3. “Why is EMSR756 called ground truth in some hackathon projects?”

**Honest answer**

> “We avoid that term. It is the best available reference observation for this exercise, but observed extent can miss areas, include product uncertainty, and represent a particular acquisition/product state rather than every flooded street.”

#### Q4. “Why use a 100 m residential population grid in a narrow valley?”

**Honest answer**

> “Because it is an open, reproducible European exposure layer. It is not a perfect measure of people present. We keep the grid native, avoid interpolation, report a sensitivity check, and use the same denominator for every candidate. That makes the comparison more defensible than the absolute count.”

#### Q5. “Your ‘additional population’ may still be flooded but unmapped. Why call it over-warning?”

**Honest answer**

> “We do not call those residents safe. We call them additional residents outside the selected mapped footprint. The footprint may be incomplete. That is also why missed residents are shown first and why Spec Mode remains the baseline.”

---

### 7.3 Space optics and sensor experts — Scanway archetype

#### Q1. “What did the sensor actually measure?”

**Honest answer**

> “For the selected EMSR756 product, we identify the actual sensor and product layer in the metadata. We do not make a generic Sentinel claim. The layer is an observed flood extent product, not a direct street-level water-depth measurement.”

#### Q2. “What can the observation miss?”

**Honest answer**

> “Depending on the source and product, flooding under vegetation or in complex urban/radar-shadow areas can be difficult, and areas outside the acquisition or product coverage must not be treated as dry. That uncertainty is why we label the counts as mapped-exposed rather than all people at risk.”

#### Q3. “Why not use Sentinel-3 fire data and claim a second hazard?”

**Honest answer**

> “Sentinel-3 FRP provides active-fire detections and fire radiative power, not a reliable evacuation perimeter. Turning detections into a warning ellipse would require a spread and exposure model we cannot validate this weekend. We cut it.”

#### Q4. “Sentinel-1 now has a six-day repeat. Does that make this near-real-time?”

**Honest answer**

> “No. Fact-checked current status is that Sentinel-1C and 1D restored nominal six-day same-track repeat in June 2026, but repeat is not a guaranteed acquisition and delivery time for a specific valley. GFM's target is roughly within eight hours of acquisition, and the 2024 case used the constellation and products available then.”

---

### 7.4 EO integration experts — Blue Dot Solutions archetype

#### Q1. “What does an operator do when there is no current flood footprint?”

**Honest answer**

> “The tool does not invent one. In production, the input must be a reviewed polygon from an authorised forecast, hydrological, or emergency-mapping workflow. In the hackathon prototype, the input is a dated retrospective CEMS product. If no reviewed polygon exists, there is no automatic proposal.”

#### Q2. “EFAS real-time data is restricted. Who operates this in production?”

**Honest answer**

> “An EFAS-partner authority or a vendor working with one. We are not proposing to bypass EFAS access controls. Our component begins after an authorised user supplies or approves the hazard polygon.”

#### Q3. “Does the official Galileo gateway preserve your chosen ellipse?”

**Honest answer**

> “That is one of the key pilot questions. The published service concept includes ground-side CAP-to-EWM conversion. If the gateway regenerates the ellipse and does not expose or retain an operator-reviewed target, our product becomes a preflight comparison and training module rather than part of the sending path. We would benchmark that before claiming integration.”

#### Q4. “Why is this not just another flood dashboard?”

**Honest answer**

> “Because the output is not a map for browsing. It is an auditable targeting decision: encoded ellipse candidates, covered/missed/additional resident counts, an approval action, and a testable CAMF payload. The map is only the interface to that decision.”

#### Q5. “Can the judge change the input and see the output change?”

**Honest answer**

> “Yes, within the prepared case. Changing the hazard geometry or selecting a different decoded candidate changes the counts and exported ellipse. We also show the sensitivity treatment. We do not depend on a live external API during the pitch.”

---

### 7.5 Cyber-defence specialists — Cyber Defence Forces / Military University of Technology archetype

#### Q1. “I spoof an EWSS warning with an SDR. What stops me?”

**Honest answer**

> “In the operational design, EWSS test messages are authenticated using OSNMA ADKD=2. But ADKD=2 is reserved in the current public SIS ICD material, and public receiver tooling may discard those tags. We therefore do not claim that our hackathon receiver verifies an alert in real time. We can discuss anomaly checks, audit logging, and fail-closed handling, but they are not a substitute for deployed ADKD=2 verification.”

#### Q2. “Your slide says OSNMA. Are you claiming this local payload is authenticated?”

**Honest answer**

> “No. The payload is explicitly labelled `LOCAL_EXERCISE`. Ordinary OSNMA status for navigation data would not authenticate this payload anyway. We separate local exercise data, recorded navigation data, and any recorded test EWM whose authentication has not been verified.”

#### Q3. “OSNMA authentication can be delayed. How can a receiver trust an urgent alert immediately?”

**Honest answer**

> “That is a real design tension. TESLA-style delayed disclosure can mean authentication is retrospective rather than available at first reception. A production receiver and operational doctrine must decide how to display pending, verified, and failed states. We do not solve that policy problem this weekend; we expose the state honestly.”

#### Q4. “What prevents your demo payload from being mistaken for a real alert?”

**Honest answer**

> “There is no transmission endpoint. The UI watermarks it as an exercise, the CAP fixture—if present—uses Test status, and unknown, expired, or malformed states fail closed. Raw logs and personal location data are not published.”

#### Q5. “What about jamming?”

**Honest answer**

> “Authentication does not prevent jamming. EWSS is a complementary channel, not a guarantee of reception. We do not claim anti-jamming capability.”

---

### 7.6 Business and incubation judges — ESA BIC Poland archetype

#### Q1. “EUSPA is procuring the operational system. STELLAR already computes an ellipse. What is left to sell?”

**Honest answer**

> “Not another turnkey gateway. The remaining hypothesis is a population-aware preflight and QA component: it compares the mechanical full-containment ellipse with alternatives, exposes missed residents, records the operator's decision, and produces test payloads for vendors and authorities. If the procured gateway already exposes equivalent population optimisation, override, and audit, our standalone thesis fails. That is why the first commercial step is a benchmark, not a platform build.”

#### Q2. “Who signs the first purchase order?”

**Honest answer**

> “Our first target is a product or integration team at a public-warning-system vendor, not a direct RCB purchase. The authority operator is the pilot user and validator. We do not have a letter of intent. **[UNVERIFIED: buyer commitment]**”

#### Q3. “Why would a vendor not build this in a week?”

**Honest answer**

> “A competent vendor could build a basic ellipse converter. The defensible work is the validated combination of CAMF quantisation, population exposure, uncertainty display, conformance tests, audit behaviour, and repeated benchmarking across national setups. That moat is not yet proven. The paid benchmark tests whether vendors value it or prefer to build internally.”

#### Q4. “EWSS is free. Why would anyone pay?”

**Honest answer**

> “The satellite channel is free in the same way a navigation signal can be free while software, integration, testing, and support are paid. We would charge for the targeting module, integration, test vectors, and support—not for access to Galileo.”

#### Q5. “What is the price?”

**Honest answer**

> “Only a hypothesis at this stage. The first offer should be priced from integration and analyst effort: a fixed-scope benchmark in the range of **[UNVERIFIED: €15,000–€40,000]** for a vendor pilot, followed by an annual integration/support licence if it enters a product. We would validate the range through buyer interviews before treating it as a forecast.”

#### Q6. “Why not sell directly to every voivodeship?”

**Honest answer**

> “Because warning procurement is authority-led, slow, and often delivered through incumbent suppliers. A vendor-first route is more realistic. Direct regional sales may follow if a national programme creates a standard requirement.”

#### Q7. “What is your post-hackathon milestone?”

**Honest answer**

> “Within 90 days: one gateway benchmark, one operator tabletop exercise, and a decision on whether the gateway exposes or retains an operator-reviewed ellipse. If vendors already match the result and expose the audit trail, we pivot to test-vector/QA tooling or stop.”

---
