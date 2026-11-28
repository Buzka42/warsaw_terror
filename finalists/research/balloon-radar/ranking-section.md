### 2. Balloon Radar: smuggling-balloon drift forecast
**Challenge 3 · Team doc (Polish original not double-counted) · 7.0 (base 7.0, no penalty)**

**What it is.** Balloon Radar forecasts where cigarette-smuggling balloons launched from Belarus will drift. It runs 500 simulated flights through Copernicus wind data to cover their unknown altitude and lift. Air traffic control gets a conflict probability and a targeted closure window for the approach corridor. Border guards get a landing area and a patrol app that checks Galileo OSNMA status.

**Pluses**
- **No AI leg proposed it**, and the hook is unforgettable and current: balloons cost Vilnius ~60 hours of suspensions and 300+ flights (47,000 passengers) in 2025, there were ~10 more disruptions in 2026, the latest on 10–11 Nov 2026, and the Border Guard confirmed balloons reaching Podlasie. (The "11 hours" single-closure figure from the team doc wasn't confirmed; use the verified totals.)
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
