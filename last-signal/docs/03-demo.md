# Last Signal — demo script (from the project dossier, unchanged)

## 6. Demo script

Total target: **4 minutes**. The script assumes the narrowed workbench. Square brackets indicate values that must be inserted only after the final run.

### Before the pitch

The presenter opens:

- the offline console;
- the selected EMSR756 case;
- the fallback recording in a separate, clearly named player window;
- the slides PDF.

Networking is off. No live Galileo reception is promised.

---

### Step 1 — Hook: the tower problem

**Time:** 0:00–0:25

**Presenter says:**

> “Lądek-Zdrój, evening, 15 September 2024. Reporters found districts without water, power problems, and no mobile coverage. The next day, Orange reported that nearly half of its base stations in the Kłodzko Valley were not working.  
>   
> Poland's Alert RCB uses SMS. SMS still needs a mobile network. So the question is: when the tower is down, how does an authority prepare a warning that can eventually travel by satellite instead?”

**On screen**

- Headline: **When the towers go down**
- Three short facts:
  - mobile coverage lost in parts of Lądek-Zdrój;
  - Orange reported major base-station failures the following day;
  - Alert RCB is SMS-based.

**Live step**

None. This is a slide.

**Offline fallback**

The slide is in the local PDF. No source page is opened live.

---

### Step 2 — Introduce EWSS honestly

**Time:** 0:25–0:50

**Presenter says:**

> “Galileo's Emergency Warning Satellite Service is designed to carry a coded warning through the satellite signal. Galileo has been running sporadic real test transmissions until 30 November 2026—this weekend—with Initial Service planned for 2027.  
>   
> But the message has only 122 bits. The authority cannot send the real flood outline. It must choose one coarse ellipse. Our question is: who does that ellipse cover, who does it miss, and who else does it warn?”

**On screen**

- `122 bits`
- A real irregular flood polygon beside a coarse ellipse.
- Status label: **Test transmissions in 2026 · Initial Service planned 2027**

**Live step**

None.

**Offline fallback**

Static diagram in the slide PDF.

**Do not say**

- “Galileo can now reach your phone.”
- “This alert will be delivered.”
- “Our phone receives EWSS.”

---

### Step 3 — Show the real Copernicus case

**Time:** 0:50–1:25

**Presenter action**

1. Open the authority console.
2. Select the prepared EMSR756 case.
3. Point to the product metadata panel.

**Presenter says:**

> “This is not a synthetic flood. It is an observed-event polygon from Copernicus Emergency Management Service activation EMSR756 for [AOI/product]. The satellite acquisition was [time] and the product was released at [time]. That means this is a retrospective targeting test—not a claim that this map could have produced the first warning before the flood.”

**On screen**

- Observed flood polygon.
- Product ID and layer name.
- Acquisition and release times.
- Label: **Reference observation, not a forecast**

**Live step**

The local console loads the pre-downloaded GeoJSON.

**Offline fallback**

If the console fails, show the pre-rendered SVG/PNG map with the same metadata. Continue verbally; do not troubleshoot for more than ten seconds.

---

### Step 4 — Show the population denominator

**Time:** 1:25–1:50

**Presenter action**

1. Toggle the GHSL population layer or exposure summary.
2. Point to the mapped exposed estimate.

**Presenter says:**

> “We overlay the European Commission's GHSL residential population grid. This estimates residents, not phones and not people present at a particular hour. Inside this observed footprint, it estimates [N] residents. Every option uses the same denominator, so the comparison is fair.”

**On screen**

- Mapped exposed estimated residents: `[N]`
- Method note: GHS-POP R2023A, 2020 epoch, 100 m
- Sensitivity note if available.

**Live step**

Counts are precomputed and also recalculated locally if the bundle permits.

**Offline fallback**

Use the frozen result table in the slide PDF. State that the values came from the final Saturday/Sunday run.

---

### Step 5 — Compare the mandated baseline with the trade-off

**Time:** 1:50–2:45

**Presenter action**

1. Show **Spec Mode**.
2. Show **Population Mode**.
3. Keep the missed-resident number visible.
4. Show the missed area on the map.

**Presenter says:**

> “The grey ellipse is the disciplined baseline: the smallest Galileo-encodable ellipse we found that contains the whole mapped footprint. It covers all [N] mapped exposed residents, but it also includes [A] residents outside the mapped footprint.
>
> The coloured ellipse is a population-focused alternative. It reduces the additional population to [B], but it misses [M] mapped exposed residents. We show those people first, in red. Our software does not silently decide that this is acceptable. A duty officer would have to approve it explicitly.”

**On screen**

| Mode | Covered | Missed | Additional outside footprint |
|---|---:|---:|---:|
| Spec Mode | `[N]` | `0` or measured value | `[A]` |
| Population Mode | `[N-M]` | `[M]` | `[B]` |

**Important wording rules**

- Say “best candidate found,” not “global optimum,” unless proven.
- Say “additional residents outside the mapped footprint,” not “people definitely safe.”
- If Population Mode performs badly, say so. The honest result remains useful.

**Live step**

Switch between two precomputed decoded candidates.

**Offline fallback**

Use the comparison screenshot. Do not rerun a long search on stage unless it was rehearsed and timed.

---

### Step 6 — Approve and encode

**Time:** 2:45–3:20

**Presenter action**

1. Select Spec Mode, or select Population Mode and use the explicit approval control.
2. Press **Export exercise draft**.
3. Show the field breakdown and hexadecimal payload.

**Presenter says:**

> “When the operator approves the exercise draft, we encode it into the 122-bit CAMF structure: hazard, severity, onset, duration, instruction code, and the quantised ellipse. This uses a test message type and placeholder provider—production codes are assigned nationally. And this button does not transmit anything to Galileo.”

**On screen**

- `EXERCISE · LOCAL PAYLOAD · NOT BROADCAST`
- 122-bit length indicator
- Field-by-field breakdown
- Ellipse centre, axes, and azimuth codes

**Live step**

Local encoder runs.

**Offline fallback**

Open the pre-generated payload JSON and field breakdown. State that it was produced by the same frozen bundle.

---

### Step 7 — Decode and test who is inside

**Time:** 3:20–3:50

**Presenter action**

1. Paste or load the exported payload into the decoder.
2. Show the reconstructed ellipse.
3. Move a test point inside the ellipse: **would receive**.
4. Move it outside: **would not receive**.
5. If rehearsed, switch the point to the wrong country or expired state.

**Presenter says:**

> “Our separate decoder reconstructs the ellipse from the bits—not from the optimiser's internal geometry. This point inside both Poland and the ellipse would be in the target. This point outside would not. That is the reference behaviour a device or warning-system supplier needs to test.”

**On screen**

- Phone-sized preview.
- Verified Polish instruction.
- One other verified language if available.
- Provenance: `LOCAL_EXERCISE`

**Live step**

Local decoder and phone-sized preview.

**Offline fallback**

Show the pre-recorded decoder sequence or static screenshots. Do not claim the phone received a radio signal.

**Do not do**

- Do not switch the phone to airplane mode and imply that this proves satellite reception.
- Do not show Ukrainian text as though it came from the CAMF library.
- Do not display a green “authenticated” badge.

---

### Step 8 — Integrity, without overclaiming

**Time:** 3:50–4:10

**Presenter says:**

> “On integrity: Galileo's test notice says EWSS messages are authenticated with a new OSNMA code, ADKD=2. But that code is still reserved in the public interface material, and today's public tools may discard it. So our prototype does not pretend that this local payload is authenticated. It separates exercise payloads from recorded navigation data and fails closed on expired or unknown messages.”

**On screen**

- `EWSS test authentication: OSNMA ADKD=2`
- `This local exercise payload: NOT AUTHENTICATED`
- `Ordinary navigation OSNMA ≠ alert verification`

**Live step**

None.

**Offline fallback**

Static slide.

---

### Step 9 — Business close

**Time:** 4:10–4:35

**Presenter says:**

> “We are not selling the Galileo channel; that is operated by the Galileo programme and is free for authorised authorities. The product is the preflight tool around it: population-aware targeting comparison, audit, and test payloads for public-warning vendors and authorities preparing for 2027. Our first sale would be a fixed-scope historical and tabletop benchmark for a warning-platform integrator, reviewed by an operator.”

**On screen**

- Buyer: public-warning-system vendor/integrator
- User: authorised civil-protection operator
- First offer: paid tabletop benchmark
- Later: integration licence, support, chipset test packages

**Live step**

None.

**Offline fallback**

Static slide.

---

### Step 10 — Final line

**Time:** 4:35–4:45

**Presenter says:**

> “Copernicus shows where the danger was observed. Galileo will provide another way to carry the warning. Last Signal helps the operator decide exactly who that warning should target—and makes the cost of that decision visible before anyone presses send.”

**On screen**

> **Last Signal**  
> Prepare the warning before the network fails.

---
