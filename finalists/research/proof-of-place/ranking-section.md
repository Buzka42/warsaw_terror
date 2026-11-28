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
