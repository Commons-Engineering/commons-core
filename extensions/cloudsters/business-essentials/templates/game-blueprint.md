---
instance_type: game
version: 0.1
last_updated: {{YYYY-MM-DD}}
horizon: {{Target year, e.g. 2032}}
timeslices:
  - label: baseline
    year: {{Current year}}
    description: "{{1-sentence: where the system stands today}}"
  - label: transition
    year: {{Baseline + 2}}
    description: "{{1-sentence: what has changed after the first wave}}"
  - label: consolidation
    year: {{Baseline + 4}}
    description: "{{1-sentence: what has stabilised}}"
  - label: horizon
    year: {{Target year}}
    description: "{{1-sentence: what the system looks like at the target horizon}}"
  - label: north_star
    year: {{Target year + 8}}
    description: "{{1-sentence: the long-horizon aspiration beyond the game horizon}}"
scenario_resilience: {{Score}}/50
commons_signal_score_baseline: {{Domain Blueprint score}}/9
commons_signal_score_target: {{Target score}}/9
sources:
  - "{{slug}}.d/blueprint.md (Domain Baseline, {{date}})"
  - "{{slug}}.g/instance/scenarios-2050.md (50 Environment Scenarios)"
  - "cloudsters/business-essentials extension pack"
  - "{{Additional sources}}"
---

# Game Blueprint: {{Business Name}} — {{Horizon}} Horizon

## Foreword

### For whom is this document?

This is the **Game Blueprint** — a designed future state for {{Business Name}} at the {{horizon}} horizon. Where the Domain Blueprint describes the observed reality, this document describes what the system must become.

Every section carries an explicit **Delta column (Δ)** showing the change from Baseline to Horizon. This gradient is the work programme.

**Central thesis:** {{1-2 sentences: the core transformation argument. What must the system become, and why is the current trajectory insufficient?}}

### How to use this document

- **Investors / Board:** §0 (Delta Overview) first, then §6 (Change Programme) for the transformation roadmap.
- **Leadership team:** Part II shows capability gaps value stream by value stream. The Δ columns are the roadmap.
- **Brand / Market team:** §1.2 (Purpose) and §2 (Relationships) — this is where the value proposition transformation lives.
- **Agents:** The Δ rows are the issue backlog. The distance between Baseline and Target is the task.

### Relationship to Domain Blueprint

The Baseline column in every table is derived **verbatim** from the Domain Blueprint (§2.1 Key Metrics for §0; individual VSF tables for Part II). The Baseline is not re-estimated — it is the observed reality at the time of Domain Blueprint creation.

**Domain Blueprint Commit:** {{SHA of the domain blueprint commit used as baseline}}

---

## §0 — Delta Overview

*The Baseline→Horizon change at a glance. These are design targets, not forecasts.*

| Key Metric | Baseline ({{year}}) | Transition ({{year}}) | Consolidation ({{year}}) | Horizon ({{year}}) | Δ Baseline→Horizon |
|---|---|---|---|---|---|
| **Revenue** | {{From Domain §2.1}} | {{Projected}} | {{Projected}} | {{Target}} | {{Absolute + %}} |
| **Recurring Revenue %** | {{From Domain §2.1}} | {{}} | {{}} | {{Target}} | {{+Xpp}} |
| **Profitability Metric** | {{From Domain §2.1}} | {{}} | {{}} | {{Target}} | {{+Xpp}} |
| **Employees (FTE)** | {{From Domain §2.1}} | {{}} | {{}} | {{Target}} | {{+/-X}} |
| **Locations / Reach** | {{From Domain §2.1}} | {{}} | {{}} | {{Target}} | {{+/-X}} |
| **D2C / Digital Share** | {{From Domain §2.1}} | {{}} | {{}} | {{Target}} | {{+Xpp}} |
| **Digital Maturity** | {{From Domain §4.2}} | {{}} | {{}} | {{Target}} | {{Description}} |
| **Commons Signal Score** | {{From Domain frontmatter}} | {{}} | {{}} | {{Target}} | {{+X points}} |
| **{{Domain-specific metric 1}}** | {{From Domain}} | {{}} | {{}} | {{Target}} | {{Δ}} |
| **{{Domain-specific metric 2}}** | {{From Domain}} | {{}} | {{}} | {{Target}} | {{Δ}} |
| **Governance** | {{From Domain §1.2}} | {{}} | {{}} | {{Target}} | {{Description}} |

*Agent Prompt: Every Baseline value MUST come from the Domain Blueprint. Do not re-estimate. Cite the section reference for each value. Target values must be justified in Part II or Part III.*

---

# PART I — WHO WE ARE (Target State {{horizon}})

## 1. Identity & Purpose

### 1.1 Profile

| Attribute | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **Name** | {{From Domain §1.1}} | {{Target or unchanged}} | {{Change description}} |
| **Legal Form** | {{}} | {{}} | {{}} |
| **Location/HQ** | {{}} | {{}} | {{}} |
| **Locations / Reach** | {{}} | {{}} | {{}} |
| **Employees** | {{}} | {{}} | {{}} |
| **Revenue** | {{}} | {{}} | {{}} |
| **Markets** | {{}} | {{}} | {{}} |
| **Product World** | {{}} | {{}} | {{}} |

### 1.2 Purpose (Target State)

> **{{Rewritten purpose statement for the horizon — what the system has become.}}**

{{2-3 sentences describing how the purpose has evolved from the Domain Baseline to the Horizon Target. Reference the transformation thesis from the Foreword.}}

---

## 2. Relationships & Community

*How the stakeholder relationships must evolve from Baseline to Horizon.*

| Relationship Type | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Stakeholder group 1}}** | {{From Domain §3}} | {{Target}} | {{Change}} |
| **{{Stakeholder group 2}}** | {{}} | {{}} | {{}} |
| **{{Stakeholder group 3}}** | {{}} | {{}} | {{}} |
| **{{Stakeholder group 4}}** | {{}} | {{}} | {{}} |
| **{{Stakeholder group 5}}** | {{}} | {{}} | {{}} |
| **{{Stakeholder group 6}}** | {{}} | {{}} | {{}} |

*Agent Prompt: Every Baseline value comes from Domain Blueprint §3 (Ecosystem). Every Target must be traceable to a capability change in Part II.*

---

# PART II — WHAT WE DO (Value Streams, Target State)

*Each Value Stream follows the schema: Baseline | Target | Δ.*
*The Baseline for each capability is derived from the Domain Blueprint BEN Cascade (Part II, §5.1–5.14). The Target describes the designed future state at the Horizon.*

*Agent Prompt: Read the Domain Blueprint Part II first. For each VSF, extract the current capabilities from the BEN Cascade, then design the target state. The Δ must be specific, measurable where possible, and traceable to a Change Driver (Part III §6).*

---

### D1 — Identity & Purpose

#### VSF D1.1 — Identity to Mandate

*How the business defines its identity, secures its mandate, and manages risk — Horizon state.*

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.1}}** | {{From Domain BEN Cascade}} | {{Target}} | {{Change}} |
| **{{Capability 2}}** | {{}} | {{}} | {{}} |
| **{{Capability 3}}** | {{}} | {{}} | {{}} |
| **{{Capability 4}}** | {{}} | {{}} | {{}} |
| **Commons Signal D1** | {{From Domain}} | {{Target}} | {{+X points}} |

#### VSF D1.2 — Purpose to Portfolio

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.2}}** | {{}} | {{}} | {{}} |

#### VSF D1.3 — Value to Profit

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.3}}** | {{}} | {{}} | {{}} |

#### VSF D1.4 — Portfolio to System

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.4}}** | {{}} | {{}} | {{}} |

---

### D2 — Participation & Relationship

#### VSF D2.1 — Participants to Community

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.5}}** | {{}} | {{}} | {{}} |

#### VSF D2.2 — Collaboration to Automation

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.6}}** | {{}} | {{}} | {{}} |

#### VSF D2.3 — Hire to Retire

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.7}}** | {{}} | {{}} | {{}} |

#### VSF D2.4 — Welcome to Transition

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.8}}** | {{}} | {{}} | {{}} |

---

### D3 — Proposition & Exchange

#### VSF D3.1 — Discovery to Usage

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.9}}** | {{}} | {{}} | {{}} |

#### VSF D3.2 — Lead to User

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.10}}** | {{}} | {{}} | {{}} |

#### VSF D3.3 — Distribution to Market

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.11}}** | {{}} | {{}} | {{}} |

---

### D4 — Production & Resilience

#### VSF D4.1 — Demand to Fulfillment

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.12}}** | {{}} | {{}} | {{}} |

#### VSF D4.2 — Source to Pay

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.13}}** | {{}} | {{}} | {{}} |

#### VSF D4.3 — Acquire to Retire

| Capability | Baseline | Horizon Target | Δ |
|---|---|---|---|
| **{{Capability from Domain VSF 5.14}}** | {{}} | {{}} | {{}} |

---

# PART III — CLOSING THE GAP

## 6. Change Drivers from Scenarios

*The scenarios with highest impact on the game horizon — and the system's transformation response.*

*Agent Prompt: Reference specific scenario codes (T1, D1, M1 etc.) from `scenarios-2050.md`. Minimum 5 scenarios cited. Explain the transformation response — not just what will be done, but what capability changes (from Part II) make it possible.*

| Scenario Code | Scenario Title | Impact | System Response | Enabling Capabilities |
|---|---|---|---|---|
| **{{T1}}** | {{Title}} | {{Transformative/High/Medium}} | {{Response}} | {{VSF refs: 5.x, 5.y}} |
| **{{D1}}** | {{}} | {{}} | {{}} | {{}} |
| **{{M1}}** | {{}} | {{}} | {{}} | {{}} |
| **{{E1}}** | {{}} | {{}} | {{}} | {{}} |
| **{{B1}}** | {{}} | {{}} | {{}} | {{}} |

---

## 7. Timeslice Transitions

*Concrete measures per transition window. Each measure traces to a Δ in Part II.*

### {{Baseline year}} → {{Transition year}}: Foundation

| Priority | Measure | Target | VSF Reference |
|---|---|---|---|
| 1 | {{}} | {{}} | {{5.x}} |
| 2 | {{}} | {{}} | {{}} |
| 3 | {{}} | {{}} | {{}} |
| 4 | {{}} | {{}} | {{}} |
| 5 | {{}} | {{}} | {{}} |

### {{Transition year}} → {{Consolidation year}}: Growth

| Priority | Measure | Target | VSF Reference |
|---|---|---|---|
| 1 | {{}} | {{}} | {{}} |

### {{Consolidation year}} → {{Horizon year}}: Harvest

| Priority | Measure | Target | VSF Reference |
|---|---|---|---|
| 1 | {{}} | {{}} | {{}} |

---

## 8. Transition / Exit Scenarios

*For PE-owned, succession, or structurally transitioning enterprises: the ownership pathway.*
*For enterprises without a pending transition: this section describes the governance evolution pathway instead.*

| Path | Buyer / Target Structure | Probability | Brand / Mission Compatibility | Prerequisites |
|---|---|---|---|---|
| **A — {{Primary path}}** | {{}} | {{High/Medium/Low}} | {{High/Medium/Low}} | {{}} |
| **B — {{Alternative path}}** | {{}} | {{}} | {{}} | {{}} |
| **C — {{Commons-aligned path}}** | {{}} | {{}} | {{}} | {{}} |

**Recommendation:** {{1-2 sentences on the recommended path and rationale.}}

---

## 9. Commons Bridge

*What is missing on the path to a commons-capable system at the North Star horizon?*

| Dimension | Commons Gap | Next Step |
|---|---|---|
| **D1 Purpose** | {{What is structurally preventing commons-aligned governance?}} | {{Concrete next action}} |
| **D2 Participation** | {{What is preventing genuine stakeholder participation?}} | {{}} |
| **D3 Proposition** | {{What is preventing shared value exchange models?}} | {{}} |
| **D4 Production** | {{What is preventing transparent, resilient production?}} | {{}} |

---

## Closing Note

*This Game Blueprint describes target states, not strategies. The concrete next steps are GitHub Issues on the project board of {{org}}/{{slug}}, assigned by Timeslice and VSF.*

*The Issue Board is the governance surface. If it is not on the board, it does not exist.*
