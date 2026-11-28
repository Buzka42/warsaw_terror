# Last Signal — business model and buyer (from the project dossier, unchanged)

## 8. Business model and buyer

### 8.1 Corrected market position

Last Signal should not be positioned as:

- the EWSS ground segment;
- a replacement national warning system;
- a consumer alert application;
- a certified receiver;
- the only company able to convert CAP into an ellipse.

The defensible position is:

> **A population-aware EWSS targeting, benchmarking, and conformance module that sits before or beside an existing public-warning gateway and makes the final Galileo ellipse decision inspectable and auditable.**

### 8.2 Buyer and user separation

| Role | Organisation type | What they care about |
|---|---|---|
| **Economic buyer** | Public-warning-system vendor, CAP platform supplier, national systems integrator | Faster EWSS product readiness, fewer national reimplementations, conformance evidence, differentiated authority offering |
| **Pilot user** | Civil-protection duty officer or crisis-centre operator | Clear trade-off, defensible approval, training, audit record |
| **Technical evaluator** | GNSS/receiver/chipset team | CAMF test payloads, decoder behaviour, ellipse/geofence edge cases |
| **Gatekeeper** | EUSPA/national EWSS implementation authority | Specification compliance, operational rules, provider codes, gateway behaviour |
| **Beneficiary** | Residents in a future warning area | Clearer, better-targeted warnings once EWSS devices exist |

No buyer commitment has been established. Any practitioner quote obtained at the hackathon is feedback, not procurement evidence.

### 8.3 The commercial unknown that decides the company

The first post-hackathon research task is to determine whether the production EWSS chain:

1. accepts a CAP polygon and mechanically converts it;
2. exposes the resulting ellipse to an operator;
3. permits operator adjustment;
4. uses population exposure in the choice;
5. preserves an approved ellipse;
6. logs who approved it;
7. supports exercises and historical replay;
8. provides test payloads to receiver and platform developers.

Possible outcomes:

| Gateway finding | Product consequence |
|---|---|
| No exposure, no population logic, no audit | Strongest opportunity: sell preflight targeting and QA module. |
| Ellipse exposed but not adjustable | Sell comparison, training, and benchmark reporting. |
| Ellipse adjustable but no population analysis | Sell optimiser component to vendor. |
| Population optimisation and audit already present | Standalone targeting product likely fails; pivot to independent conformance/test tooling or stop. |
| Gateway interface closed and target cannot be retained | Sell offline exercise and procurement-evaluation tooling only. |

### 8.4 First offer

**Offer:** Fixed-scope EWSS targeting benchmark and tabletop package.

**Deliverables**

- One historical flood case supplied or approved by the customer.
- Spec Mode and population-aware candidate comparison.
- Missed/additional resident report.
- CAMF exercise payloads.
- Independent decode report.
- Gateway comparison workshop.
- Operator tabletop session.
- Written integration requirements:
  - ellipse exposure;
  - override;
  - retention;
  - audit;
  - provider codes;
  - update/all-clear behaviour.

**Purpose**

The benchmark answers whether Last Signal improves on the customer's converter and whether operators trust the interface.

**Pricing hypothesis**

- Paid benchmark: **[UNVERIFIED: €15,000–€40,000]**, priced from integration and analyst effort.
- Follow-on annual module/support licence: **[UNVERIFIED: €25,000–€100,000 per national/product deployment]**, depending on integration scope.
- Chipset/device test package: later, priced per test campaign or support contract. **[UNVERIFIED]**

These numbers must not be presented as observed willingness to pay. They are interview hypotheses.

### 8.5 Revenue model after validation

Possible revenue lines, in order:

1. **Paid benchmark/tabletop** — first cash and validation.
2. **Integration fee** — connecting the module to a vendor's CAP chain.
3. **Annual licence/support** — CAMF updates, test suites, national configurations.
4. **Conformance and regression testing** — payload vectors for platform and receiver releases.
5. **Training/exercise packages** — historical replay and operator decision exercises.
6. **Chipset test support** — later, if EUSPA testing campaigns create demand.

Per-device consumer pricing is not credible. Direct citizen subscriptions should be removed.

### 8.6 Why now

- Galileo EWSS test transmissions end on 30 November 2026.
- Initial Service is planned for 2027.
- Authorities and vendors must prepare before operational use.
- The 2024 Polish floods provide a concrete national case in which mobile infrastructure failed.
- Public-warning vendors need to add a new channel without rebuilding their whole CAP workflow.
- CAMF v1.2 is public and in force, making preparation possible now.

The timing argument is preparation, not immediate citizen coverage.

### 8.7 Procurement path

Realistic path:

1. **Vendor discovery** — identify the product owner responsible for EWSS readiness.
2. **Technical benchmark** — compare against the existing converter.
3. **Operator tabletop** — civil-protection user reviews the trade-off interface.
4. **Gateway sandbox** — test whether the approved ellipse is exposed and retained.
5. **Security and accessibility review** — access control, audit, incident handling, data protection.
6. **Procurement or subcontract** — direct public procurement where required, or supply through an incumbent integrator.
7. **Authority approval** — operational use only after national rules and acceptance tests.

ESA BIC support is a possible incubation route, not an awarded pilot budget.

### 8.8 Legal and safety positioning

The prototype must state:

- not for operational emergency use;
- no transmission capability;
- human authority approval required;
- population values are estimates;
- observed hazard products may be incomplete;
- CAMF implementation is not certified;
- provider codes and operational rules must be assigned/confirmed nationally;
- raw GNSS logs may contain sensitive location or device information and must not be published without review.

Production liability cannot be transferred entirely to the operator through a button. The approval action helps create an audit trail, but a real product would need a formal safety case, procurement acceptance, accessibility work, cybersecurity review, and operational governance.

---
