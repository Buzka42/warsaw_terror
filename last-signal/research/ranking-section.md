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
- **EWSS is not live yet: Initial Service is 2027.** But Galileo has been broadcasting *real* test alert messages (authenticated with OSNMA ADKD=2) from 23 Jul to 30 Nov 2026 (Service Notice #28) — the test window closes the day after the hackathon. If the team can capture or replay a genuine test EWM with OSNMAlib, the "simulated" objection mostly dies; if not, the demo injects alerts into recorded logs and a sceptic will call it simulated.
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
