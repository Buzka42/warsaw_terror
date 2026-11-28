# Last Signal — team planning folder

**Decision (2026-11-28): the team picked Last Signal.** Proof of Place may be merged in later if there is time; for now it is only reference material in here (`proof-of-place.md`, `proof-of-place-dossier.md`).

This folder is **read-only evidence and planning material**. Nothing in it decides the architecture — the technical notes are extracted verbatim from the research dossier and are marked for the team to use as input, not as decisions.

## Read in this order

| # | File | What it is |
|---|------|------------|
| 1 | `docs/00-full-dossier.md` | The complete project dossier (122 KB, 10 sections) — the single source of truth |
| 2 | `last_signal.md` | The team's 6-section design document, incl. the updated Friday-night checklist (§10) |
| 3 | `docs/01-build-plan.md` | 48-hour build plan, hour by hour, with go/no-go points |
| 4 | `docs/02-problems.md` | Consolidated problem register: severity, evidence, proposed solutions |
| 5 | `docs/03-demo.md` | 3–5 minute pitch + live demo script with fallbacks |
| 6 | `docs/04-jury-qa.md` | Hardest expected questions per jury archetype, with answers |
| 7 | `docs/05-business.md` | Buyer, pricing hypothesis, procurement path |
| 8 | `docs/06-technical-notes.md` | Technical description as researched — input for planning, not decisions |
| 9 | `checks/` | Five web-verified checklist checks (Muse Ember, primary sources): CAMF v1.2 · EMSR756 · GHSL · GnssLogger · EWSS ICD status |
| 10 | `research/` | The underlying research papers behind the dossier: independent reviews by GPT Sol 6.2 and Muse Wonder (Kimi K3.1 was unavailable), the web-verified fact-check table, hackathon guidelines, past-winners notes, the ranking section and the original design doc |
| 11 | `CASSINI_IDEA_RANKING.md` | The full 29-idea MoA ranking (context: Last Signal scored 7.4, ranked #1) |
| 12 | `proof-of-place.md`, `proof-of-place-dossier.md` | Future merge candidate — plain-language + technical dossier of the #3 idea |

## Key facts the team must not have to re-derive

- **Demo AOI is Nysa (AOI03), not Stronie Śląskie** — Stronie's observed flood area is 15.6 ha and shrinks to 3.6 ha; Nysa's is 3,463 ha. Exact product: `EMSR756_AOI03_DEL_MONIT01_v1.zip` via the CEMS Rapid Mapping API.
- **CAMF v1.2** is in force at `EWSS-CAMF_in_force.pdf` (GSC). Encode from its tables; v1.1 "00000 = empty" silently became "reserved".
- **EWSS test transmissions run 23 Jul–30 Nov 2026** (Service Notice #28, OSNMA ADKD=2). Submission falls inside the window. No public SIS ICD, no public capture, no test vectors — the spec is proprietary under NDU in EUSPA grant EUSPA-GSA-GA-G-04-2022. The demo starts at the CAMF payload boundary unless a ChipCraft/mentor contact supplies a capture.
- **A GnssLogger log cannot prove E1-B** (`TYPE_GAL_I` covers E1-B and E5b-I). E1-B identity must be inferred from Raw/Status rows.
- **GHSL GHS-POP R2023A** is the current global product (DOI `10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE`); confirm tile/NoData with `gdalinfo` after download.

Everything for this project is in this folder. No file you need is located anywhere else.
