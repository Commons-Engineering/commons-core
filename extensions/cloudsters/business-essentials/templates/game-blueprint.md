<!--
Template v2 — cloudsters/business-essentials/templates/game-blueprint.md
Game Blueprint companion to the Domain (.d) blueprint.

Two-layer document:
  • §0 Pipeline Annotation Card — Pipeline-side observer content,
    STRIPPED at copy-time when this .g is transferred into a customer's
    sovereign .g instance.
  • Foreword + Δ overview + Per-VSF Δ tables + Change Programme +
    Scenarios reference + Decision Points — Wir-Perspektive throughout,
    transfers verbatim to {customer-org}/{slug}.g on engagement.

Agent Briefs at the head of every section. Loop hooks via §0.
Companion 50-scenario file at `instance/workshop/analysis/scenarios-2050.md`.

Conforms to:
  • COMMONS_CORE_MANIFEST · COMMONS_BLUEPRINT_MANIFEST · COMMONS_LOOPS_MANIFEST
  • INSTANCE_PIPELINE_SPEC v0.3.9+
-->

---
instance_type: game
instance_class: business_game
version: 0.2
template_version: business-essentials/game-blueprint v2
last_updated: {{YYYY-MM-DD}}
subject: {{Subject Legal Name}}
slug: {{slug}}
language: {{de|en|fr|...}}
sector: {{sector slug}}
region: {{Region}}
city: {{city slug if applicable}}
horizon: {{e.g. 2032}}
north_star: {{e.g. 2040}}
brightness_orbit: {{from sibling .d}}
lifecycle_stage: {{from sibling .d}}
timeslices:
  - label: baseline
    year: {{current year}}
    description: "{{one-sentence Baseline summary, verbatim from .d §1.6}}"
  - label: transition
    year: {{baseline + 2}}
    description: "{{one-sentence transition summary}}"
  - label: consolidation
    year: {{baseline + 4}}
    description: "{{one-sentence consolidation summary}}"
  - label: horizon
    year: {{horizon year}}
    description: "{{one-sentence horizon summary}}"
  - label: north_star
    year: {{north star year}}
    description: "{{one-sentence north star summary}}"
scenario_resilience: {{score}}/50
commons_signal_score_baseline: {{from sibling .d}}
commons_signal_score_target: {{target at horizon}}
sources:
  - "{{org}}/{{slug}}.d/blueprint.md (Domain Baseline, {{date}})"
  - "{{slug}}.g/instance/workshop/analysis/scenarios-2050.md (50 Environment Scenarios)"
  - "cloudsters/business-essentials extension pack"
  - "{{additional sources}}"
sibling_d: {{org}}/{{slug}}.d
---

# Game Blueprint: {{Subject Name}} — {{horizon year}} Horizon *(with {{north star year}} North Star)*

> ⚠️ **Pipeline-side designed-futures observation.** This is the Pipeline-side `.g` instance of {{Subject Name}} — a federation-readable Game blueprint built as scenario-of-development on top of the observed Baseline in the sibling `.d`. It is *not* the subject's own commons. If {{Subject Name}} engages, this `.g` becomes the substrate for a sovereign `.g` in their own GitHub namespace: the §0 Pipeline Annotation Card is stripped at copy-time; everything below transfers verbatim.

---

## §0 — Pipeline Annotation Card

> *Pipeline-side only; **removed on transfer to {{customer-org}}/{{slug}}.g**. Strip boundary: `<!-- pipeline-annotation:end -->` marker below.*

| Property | Value |
|---|---|
| **Steward** | {{Incubator-GmbH or @handle; not assigned if open}} |
| **Region** | {{cloudsters-REGION}} |
| **Brightness Orbit** | {{from sibling .d}} |
| **Lifecycle stage** | {{from sibling .d}} |
| **MCP subscription status** | {{from sibling .d}} |
| **Domain Baseline Commit** | `{{org}}/{{slug}}.d` @ {{SHA}} *(as of {{date}})* |
| **Last full refresh** | {{ISO date}} |
| **Next due** | {{ISO date — semi-annual scenario review loop}} |

### Active Pipeline-side Game Loops *(Loop Registry summary; full contracts in `instance/operations/loops/`)*

| Loop | Class | Cadence | Status |
|---|---|---|---|
| `{{slug}}-scenario-review` | Maintenance, Open | semi-annual | {{status / next run}} |
| `{{slug}}-timeslice-baseline-resync` | Sensing, Open | on `.d` commit | {{status}} |
| `{{slug}}-strategic-initiative-tracking` | Governance, Open | quarterly | {{status / next run}} |

<!-- pipeline-annotation:end -->
<!-- Content above is Pipeline-side observation, removed on transfer to {{customer-org}}/{{slug}}.g -->

---

*— end of Pipeline Annotation Card. Everything below is customer-portable Wir-Perspektive. —*

---

## Foreword

### What this document is

This is our **Game Blueprint** — a structured set of designed futures for {{Subject Name}} at the {{horizon year}} horizon, with a long-shadow projection at {{north star year}} *(the North Star)*. Where the Domain Blueprint *(`{{slug}}.d/blueprint.md`)* describes what we have committed to today, this document describes **what we are working toward**.

These futures are not forecasts. Each one is a designed target — a deliberate position we choose to engineer toward over time, with explicit checkpoints, change drivers, and capability paths. The work of moving between Baseline and Horizon is **transition engineering**: sensing our current state, identifying the gap against the next timeslice, designing the transition path using proven patterns, and building the next state deliberately.

### Central thesis

> *Agent Brief:* Depth = **medium**. Triangulation = the thesis must be derivable from §1.5 Recent Trajectory + §6 Change Drivers in the sibling `.d`. Output = 2-3 sentences, no more — a single load-bearing claim about why the current trajectory is insufficient. Time budget = 30 minutes.

{{1-2 sentences: the load-bearing claim. What must the system become, and why is the current trajectory insufficient?}}

### How to read this document

| Reader | Focus |
|---|---|
| {{Board / Leadership}} | §0 Delta Overview and §6 Change Programme — the trajectory and the path |
| {{Owners / Funders}} | Part II *(per VSF Δ)* — the capability roadmap |
| {{Brand / Communications}} | §1.2 Purpose-Δ and §3 Stakeholder-Δ — where the relationship structure shifts |
| {{Agents}} | Δ rows are the issue backlog. The distance between Baseline and Target is the task. |

### Relationship to the Domain Blueprint

Every Baseline column in the tables below is read **verbatim** from the Domain Blueprint *(`{{slug}}.d/blueprint.md` §2.1 Key Metrics for §0; individual VSF Element tables for Part II)*. We do not re-estimate the Baseline here.

**Domain Baseline Commit:** `{{org}}/{{slug}}.d` HEAD as of {{ISO date}}.

---

## §0 — Delta Overview

> *Agent Brief:* Depth = **deep**. Triangulation = every Baseline value verbatim from `.d` §2.1. Targets justified in Part II. Time budget = 60-90 minutes.

| Key Metric | Baseline *({{year}})* | Transition *({{year}})* | Consolidation *({{year}})* | Horizon *({{year}})* | Δ Baseline → Horizon |
|---|---|---|---|---|---|
| **{{Headcount metric}}** | {{from .d §2.1}} | {{projected}} | {{projected}} | {{target}} | {{absolute + %}} |
| **{{Financial metric}}** | {{from .d §2.1}} | {{projected}} | {{projected}} | {{target}} | {{absolute + %}} |
| **{{Reach metric}}** | {{from .d §2.1}} | {{}} | {{}} | {{target}} | {{Δ}} |
| **{{Sector-specific metric 1}}** | {{from .d §2.1}} | {{}} | {{}} | {{target}} | {{Δ}} |
| **{{Sector-specific metric 2}}** | {{from .d §2.1}} | {{}} | {{}} | {{target}} | {{Δ}} |
| **Funder / Revenue diversification** | {{from .d}} | {{}} | {{}} | {{target}} | {{structural description}} |
| **Commons Signal Score** | {{from .d frontmatter}} | {{}} | {{}} | {{target}} | {{+X points}} |

---

## Part I — Who we become

### Wenn uns jemand fragt, was wir tun *({{timeslice}})*
<!-- SPOKEN FORM — D0 · Perception to Mandate (COMMONS_VALUE_CREATION_MANIFEST §3.3).
     In a Game Blueprint this is spoken FROM INSIDE the pole's timeslice: the pitch
     this commons gives once it has become what this pole describes. Present tense,
     not future — the pole is a full operative instance at its point in time.
     Four to five FLOWING paragraphs, ~170 words, first person plural, spoken register.
     NO framework labels, NO bullets — the beats shape the prose, they must not show.
     Spoken order: Name · Same · Pain · Fame · Aim · EXCHANGE · Game.
     Beats with backing belong in the workshop version, never on the stage. -->

{{Wir sind … — wer wir in diesem Pol sind und wen „wir" umfasst. Wir machen … —
die vertraute Kategorie dieser Zeitscheibe.}}

{{Die Spannung im Feld, wie sie sich dann darstellt — und was wir darin können,
das andere in derselben Kategorie nicht können: der besitzbare Mechanismus.
Woran wir gerade arbeiten.}}

{{Was wir dazu brauchen, sagen wir offen: …}}

{{Das größere Spiel ist … — dieselbe Melodie wie die Kategorie oben, auf Welt-Höhe.}}

### Wo unsere Cores sitzen
<!-- CORE POSITIONING — D0 · boundary and sovereignty (COMMONS_CORE_MIGRATION).
     "We engineer Commons Cores as Centers of Alignment & Productivity for
     Value-Creating Systems." Plural grammar: a Commons Core · several Commons
     Cores · a Constellation. Cores are the sovereign centres; the Constellation
     is the whole. A Core is where alignment and productivity are actually HELD —
     where a decision binds and work becomes coherent. That is an observation
     about the organisation, not a wish: name where it sits TODAY.
     Roles: Core (sovereign centre) · Sub-Core (own coherence, inside a Core's
     mandate) · Companion Sphere (an own field alongside, not subordinate) ·
     outside the boundary (modelled across via Portfolio to System, never absorbed).
     A single-site organisation is one Core — say so plainly; do not invent a
     constellation. This section states WHAT IS; where a Core should first be
     instantiated is an engagement question and belongs in §0 (pipeline-side). -->

{{Ein Satz: Wir sind ein Commons Core — oder: Wir sind eine Constellation aus
N Cores. Und woran man das erkennt: wo eine Entscheidung bindet und Arbeit
kohärent wird.}}

| Einheit | Rolle | Warum |
|---|---|---|
| {{Einheit}} | {{Core / Sub-Core / Companion Sphere / außerhalb}} | {{worin ihre eigene Kohärenz besteht — oder warum sie keine hat}} |

{{Zwei bis drei Sätze: Was das für uns bedeutet — was zentral getragen wird und
was vor Ort entschieden werden muss. Wo die Ausrichtung heute reibt, gehört in
§5.0 Perception to Mandate, nicht hierher.}}



### §1.1 Identity-Δ — who we are at the horizon

*Same identity, different scale and position. The five-line summary.*

| | Baseline *({{year}})* | Horizon *({{year}})* | Δ |
|---|---|---|---|
| **Role in our context** | {{from .d}} | {{horizon}} | {{Δ}} |
| **External perception** | {{from .d}} | {{horizon}} | {{Δ}} |
| **Position in the federation / sector** | {{from .d}} | {{horizon}} | {{Δ}} |
| **Physical anchoring** | {{from .d}} | {{horizon}} | {{Δ}} |
| **Team self-understanding** | {{from .d}} | {{horizon}} | {{Δ}} |

### §1.2 Purpose-Δ — the four-dimension evolution

| Dimension | Baseline {{year}} | Horizon {{year}} | Δ |
|---|---|---|---|
| **D1 — Bestimmung** | {{from .d}} | {{horizon}} | {{Δ}} |
| **D2 — Teilhabe** | {{from .d}} | {{horizon}} | {{Δ}} |
| **D3 — Angebot** | {{from .d}} | {{horizon}} | {{Δ}} |
| **D4 — Resilienz** | {{from .d}} | {{horizon}} | {{Δ}} |

### §1.6 What we are at the horizon *(for those who need it short)*

*{{Single-paragraph horizon-state summary, ~150 words, no bullets — the answer to "what will we be in {{horizon year}}?"}}*

---

## Part II — How we get there — Per-VSF Δ

*Per Value Stream we show the movement from Baseline capabilities to Horizon capabilities. The full Δ column is the roadmap.*

### §2.1 Identity to Mandate

| Capability | Baseline {{year}} | Horizon {{year}} | Δ |
|---|---|---|---|
| **{{Capability A from .d §5.1}}** | {{from .d}} | {{horizon}} | Δ: {{required change}} |
| **{{Capability B}}** | {{from .d}} | {{horizon}} | Δ: {{required change}} |

### §2.2 Purpose to Portfolio

*(Per-capability Δ table per the §2.1 pattern, populated from .d §5.2)*

### §2.3 Value to Profit

*(Per-capability Δ table)*

### §2.4 Portfolio to System

*(Per-capability Δ table)*

### §2.5 Participants to Community

*(Per-capability Δ table)*

### §2.6 Collaboration to Automation

*(Per-capability Δ table)*

### §2.7 Hire to Retire

*(Per-capability Δ table)*

### §2.8 Welcome to Transition

*(Per-capability Δ table)*

### §2.9 Discovery to Usage

*(Per-capability Δ table)*

### §2.10 Lead to User

*(Per-capability Δ table)*

### §2.11 Distribution to Market

*(Per-capability Δ table)*

### §2.12 Demand to Fulfillment

*(Per-capability Δ table)*

### §2.13 Source to Pay

*(Per-capability Δ table)*

### §2.14 Acquire to Retire

*(Per-capability Δ table)*

---

## §6 Change Programme — How we actually get there

> *Agent Brief:* Depth = **very deep**. Triangulation = each Initiative references a §4.4 Strategic Initiative or a §6/§7 Change Driver/Need from `.d`. Output = ordered by timeslice; every initiative has named owner, target metric, loop anchor. Time budget = 2-3 hours.

### Timeslice {{baseline year}} → {{transition year}} *(Transition)*

| # | Initiative | Owner | Target metric | Loop anchor |
|---|---|---|---|---|
| 1 | **{{Initiative}}** | {{role / name}} | {{measurable target}} | `{{loop-slug}}`, {{class}}, {{cadence}} |

### Timeslice {{transition year}} → {{consolidation year}} *(Consolidation)*

| # | Initiative | Owner | Target metric | Loop anchor |
|---|---|---|---|---|
| {{n}} | **{{Initiative}}** | {{role / name}} | {{target}} | `{{loop-slug}}`, {{class}} |

### Timeslice {{consolidation year}} → {{horizon year}} *(Horizon)*

| # | Initiative | Owner | Target metric | Loop anchor |
|---|---|---|---|---|
| {{n}} | **{{Initiative}}** | {{role}} | {{target}} | `{{loop-slug}}` |

### Beyond Horizon — {{horizon year}} → {{north star year}} *(North Star path)*

| # | Initiative | Owner | Goal |
|---|---|---|---|
| {{n}} | **{{Initiative}}** | {{role}} | {{goal}} |

---

## §7 Scenarios — three trajectories for our environment

> *Agent Brief:* Depth = **deep**. Triangulation = each scenario references at least 3 scenarios from `instance/workshop/analysis/scenarios-2050.md`. Output = three stress-scenarios with resilience score. Time budget = 60-90 minutes.
> *Full 50-scenario collection:* `instance/workshop/analysis/scenarios-2050.md`.

### Scenario A — *"{{Title}}"*

{{Description, our strategic response in 2-3 sentences.}}

### Scenario B — *"{{Title}}"*

{{Description, our strategic response.}}

### Scenario C — *"{{Title}}"*

{{Description, our strategic response.}}

### Resilience Assessment

| Scenario | Probability *(estimate)* | Impact on us | Strategy-path resilience |
|---|---|---|---|
| **A** | {{H/M/N}} | {{+/−}} | {{high/medium/low — reasoning}} |
| **B** | {{H/M/N}} | {{+/−}} | {{...}} |
| **C** | {{H/M/N}} | {{+/−}} | {{...}} |

*Scenario Resilience Score: **{{score}}/50** *({{indication note}})*.*

---

## §8 What this Game asks of us

The Game Blueprint is not a forecast and not an application. It is an invitation to choose deliberately between scenarios — not every day, but at marked decision points:

| Decision point | When | Who decides |
|---|---|---|
| **{{Decision}}** | {{timing}} | {{role}} |
| **{{Decision}}** | {{timing}} | {{role}} |

Each decision point is a variant of one loop question: *"Do the conditions under which we adopted this strategy still hold?"* If yes — continue. If no — re-open. This is the operational anatomy of Adaptive Management.

---

*Game Blueprint v0.2 · {{Subject Name}} · {{Pipeline-side | Customer-sovereign}} · {{Region or Customer Org}} · {{ISO date}}*
*Maintained on a semi-annual scenario review. Next refresh: {{ISO date}}. Sibling Domain instance: `{{org}}/{{slug}}.d`. Full scenario collection: `instance/workshop/analysis/scenarios-2050.md`.*
