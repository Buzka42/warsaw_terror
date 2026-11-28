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
