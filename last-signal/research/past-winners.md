# Balloon Radar: what's missing and what we need

An honest gap list for the team, ranked by how much each gap could cost us with the jury. It builds on [`balloon_radar.md`](balloon_radar.md) (full design) and [`how_it_works.md`](how_it_works.md) (team explainer).

**Priorities:**
- **CRITICAL:** without it we lose points or the demo breaks.
- **IMPORTANT:** noticeably strengthens the pitch.
- **NICE TO HAVE:** only if time allows.

---

## What past winners teach us

We reviewed the winners of past CASSINI Hackathons, with a focus on the defence and security editions (5th and 8th) and the latest one (11th, won by Poland). Official pages rarely state why the jury chose a project, so these are patterns visible in the winners, not jury reasoning. The one exception is Viadrus.

| Pattern in winners | Example | Balloon Radar today |
|---|---|---|
| One narrow problem with a concrete user, not a platform | Viadrus: pipe leaks for a water utility; UIS: unexploded ordnance | ✅ |
| **A practitioner involved in the project** | Viadrus (1st place, 11th edition): the stated key differentiator was close collaboration with experts from Wrocław's water utility (MPWiK) | ❌ **missing** |
| Output is a decision or a priority, not a map | Viadrus: prioritisation layer of sites to inspect; BasinPulse: health score as evidence | ✅ by design, needs to show in the demo |
| Prediction / early warning | Leaks weeks ahead; avalanche probability; Firewatch: satellite data + simulation for responders | ✅ |
| Explicit business model | SpaceGuardian (1st place, 8th edition): subscription SaaS | ⚠️ hypothesis only |
| Not a repeat of past winners | GNSS spoofing detection (3rd, 2024) and GNSS-free drone navigation (2nd, 2024) already placed | ✅ we avoid both |

---

## Gaps

### 1. A practitioner. CRITICAL

**Why:** the only explicitly stated reason a past winner won was practitioner involvement. Right now nobody from aviation, ATC or the Border Guard has validated our problem or our output.

**What we need:**
- At least **one conversation** with someone from: air traffic control / an ANSP (PAŻP), an airport, the Border Guard, the military, or someone who has worked with them.
- **One quotable sentence** for the pitch, e.g. "a targeted closure window would be useful for ATC", and permission to cite it (name and role, or anonymised).
- **Validation of the output format:** what does a controller actually need? Probability, time window, sector? What would make them trust it?

**How:**
- **Saturday mentoring at 11:30 and 16:30:** ask every mentor "do you know anyone in aviation, ATC or the Border Guard?"
- Ask the organisers (Blue Dot Solutions) and the military / cyber-defence people on the jury pool for a contact.
- **Fallback:** cite public statements by Lithuanian ATC and authorities (they called it an attack on civil aviation). Weaker than a live practitioner, but better than nothing.

### 2. Realistic smuggling-balloon flight profile. CRITICAL

**Why:** our Monte Carlo needs priors for altitude, ascent rate and flight duration. If the ranges are invented, a technical juror will notice.

**What we need:**
- Publicly reported facts on smuggling balloons: type (weather balloons are mentioned in reports), payload, typical altitude, flight distance, how they come down, whether they carry GPS trackers.
- A short "assumptions" slide: which values we assumed, why, and how they get calibrated (every recovered balloon).

**How:** news reports and official statements from Lithuania and Poland (Friday night / Saturday morning research); ask mentors.

### 3. Live wind source decision. CRITICAL

**Why:** ERA5 has a delay of several days, so it is replay-only. The live radiosonde demo needs a forecast.

**What we need:** check tonight whether CAMS global forecasts expose wind on pressure levels.
- **If yes:** fully Copernicus.
- **If no:** ECMWF open data as the live source, and we say so openly, with Copernicus (ERA5 + CLMS) still central for the replay and the terrain.

### 4. GNSS feasibility: OSNMA and EGNOS. CRITICAL

**Why:** this is what makes Galileo and EGNOS real rather than decorative. GNSS hardware engineers on the jury will check.

**What we need:**
- [ ] Do our phones log Galileo navigation messages in GnssLogger? Test by a window tonight.
- [ ] OSNMA public key and Merkle tree root from the European GNSS Service Centre: how to get them, and how long it takes.
- [ ] OSNMAlib runs on a sample file.
- [ ] EGNOS data: EGNOS Message Server archive or EDAS registration.
- [ ] RTKLIB SBAS run on a sample log.

**Decision point Saturday 12:00:** if Path A (phone data) doesn't work, switch to Path B (recorded reference data) and stop spending time on it.

### 5. The lead-time number. IMPORTANT

**Why:** Viadrus sold "weeks before failure". We need our equivalent: "alert X minutes before the balloon enters the approach path" and "closure of Y minutes instead of Z hours".

**What we need:** the Vilnius replay with real incident times and ERA5 winds, producing these two numbers. **Don't put any number on a slide before the replay produces it.**

### 6. Exact incident data for the replay. IMPORTANT

**What we need:** at least one Vilnius incident with date, time window, where balloons were detected or found, and how long the airport was closed.

**How:** Lithuanian and Polish news reports (LRT, PAP), statements by Lithuanian ATC and the crisis management centre.

### 7. Business model backed by numbers. IMPORTANT

**Why:** it is a third of the score, and today the pricing is a guess.

**What we need:**
- **Cost of a closure:** diversions, passenger compensation and airline costs, from public sources (e.g. EU passenger-rights compensation rules, reported diversion counts).
- **Price point:** one sentence on how we arrived at it.
- **Named first customer and path:** e.g. a pilot with one Baltic ANSP financed by EU defence-innovation grants, then expansion along the eastern flank.
- **Polish angle:** which Polish airports and Border Guard units are realistic customers.

### 8. Competition check. IMPORTANT

**Why:** "who else does this?" is a standard jury question.

**What we need:** 30 minutes of research:
- existing balloon trajectory predictors (SondeHub, NOAA HYSPLIT);
- counter-UAS / airspace security vendors;
- whether any of them already handle smuggling balloons.

Then **one slide or one sentence** on how we differ.

### 9. Submission requirements. IMPORTANT

**Why:** the deadline is **Sunday 15:00** and the rules are in a PDF we haven't read.

**What we need:** read the rules PDF from the event page and list what must be submitted (repo, slides, video, description?), in what format and where.

### 10. Backup demo. IMPORTANT

**Why:** live demos fail. The radiosonde may not launch, SondeHub may lag, the venue Wi-Fi may drop.

**What we need:**
- A screen recording of Saturday's 13:00 radiosonde run.
- The Vilnius replay working offline from cached data.
- Slides that tell the story without the live part.

### 11. Pitch and slides. IMPORTANT

**What we need:** a 3-minute pitch following the script in `balloon_radar.md`. Rehearse it at least twice. Attend Saturday's 16:00 pitching workshop and Sunday's 12:00 pitch training.

### 12. Team roles and skills. IMPORTANT

**Why:** there are two of us, plus maybe Kamila and others.

**What we need:** clear owners for:
- **forecast engine** (Python, xarray);
- **GNSS** (OSNMA, RTKLIB);
- **frontend** (map, alert panel);
- **pitch and business.**

If nobody is comfortable with GNSS processing, decide early to use Path B and keep it simple.

### 13. Nice to have

- A real Telegram/Discord alert arriving on a phone during the pitch.
- Land-cover split in the landing ellipse (CLMS).
- An EGNOS protection level computed properly (instead of just "with vs without EGNOS").
- A one-page PDF for the jury.

---

## Summary checklist

| # | Gap | Priority | Owner | Deadline |
|---|---|---|---|---|
| 1 | Practitioner conversation + quote | CRITICAL | | Sat 17:00 |
| 2 | Smuggling-balloon flight profile priors | CRITICAL | | Sat 10:00 |
| 3 | Live wind source decision (CAMS vs fallback) | CRITICAL | | Fri night |
| 4 | OSNMA + EGNOS feasibility, Path A/B decision | CRITICAL | | Sat 12:00 |
| 5 | Lead-time number from replay | IMPORTANT | | Sat night |
| 6 | Vilnius incident data | IMPORTANT | | Sat 10:00 |
| 7 | Business numbers (closure cost, pricing, first customer) | IMPORTANT | | Sat night |
| 8 | Competition check | IMPORTANT | | Sat |
| 9 | Submission requirements from rules PDF | IMPORTANT | | Fri night |
| 10 | Backup demo recording | IMPORTANT | | Sun 12:00 |
| 11 | Pitch + slides, 2 rehearsals | IMPORTANT | | Sun 13:00 |
| 12 | Team roles | IMPORTANT | | Fri night |

---

## Sources (past winners)

- 11th CASSINI Hackathon winners (EUSPA): https://www.euspa.europa.eu/newsroom-events/news/space-water-turning-tide-satellite-tech
- Viadrus AI and the role of MPWiK (Invest in Wrocław): https://invest-in-wroclaw.pl/satellites-ai-breakthrough-wroclaw-viadrus-ai-cassini
- 10th CASSINI Hackathon winners (EUSPA): https://www.euspa.europa.eu/newsroom-events/news/meet-10th-cassini-hackathon-winners
- 8th CASSINI Hackathon winners, defence and security (EUSPA): https://www.euspa.europa.eu/newsroom-events/news/8-cassini-hackathon-winners
- 8th edition outcomes, SpaceGuardian as SaaS (European Commission): https://defence-industry-space.ec.europa.eu/cassini-hackathon-november-2024-key-outcomes-and-takeaways-2024-12-10_en
- 5th CASSINI Hackathon winners, defence and security: https://hackathons.cassini.eu/5th-CASSINI-Hackathon-winners
- 7th CASSINI Hackathon winners: https://www.cassini.eu/hackathons/7th-cassini-hackathon-winners
