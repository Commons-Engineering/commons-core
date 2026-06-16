<!--
Template v2 — cloudsters/business-essentials/templates/blueprint.md
Living Blueprint (L1-L9 substrate) with the BEN Cascade at L5.

Two-layer document:
  • §0 Pipeline Annotation Card — Pipeline-side observer content,
    STRIPPED at copy-time when this .d is transferred into a customer's
    sovereign .o instance. See Spec §"Customer Transfer".
  • Foreword + Parts I/II/III + Appendices — Wir-Perspektive throughout,
    transfers verbatim to {customer-org}/{slug}.o on engagement.

Agent Briefs at the head of every section declare depth, triangulation
requirement, output shape, and time budget. Loop contract hooks per
value stream point to instance/operations/loops/ per COMMONS_LOOPS_MANIFEST §8.

Conforms to:
  • COMMONS_OS_MANIFEST · COMMONS_BLUEPRINT_MANIFEST · COMMONS_LOOPS_MANIFEST
  • LIGHTHOUSE_BUSINESS_SPEC/1.2 · BUSINESS_ENGINEERING_MANIFEST
  • INSTANCE_PIPELINE_SPEC v0.3.9+
-->

---
instance_type: domain
instance_class: business_digital_twin
version: 0.2
template_version: business-essentials/blueprint v2
last_updated: {{YYYY-MM-DD}}
subject: {{Subject Legal Name}}
slug: {{slug}}
language: {{de|en|fr|...}}
sector: {{sector slug}}
region: {{Region — cloudsters-EUROPE | cloudsters-AMERICAS | …}}
city: {{city slug if applicable}}
brightness_orbit: {{0–5 with label, e.g. "3 — Dim"}}
lifecycle_stage: {{Collect|Qualify|Nurture|Engage|Propose|Collaborate|Expand}}
archetype: {{archetype slug}}
commons_signal_score: {{n.n/9}}
sources:
  - {{primary URL}}
  - {{primary URL}}
  - {{statutory primary disclosure source, e.g. Northdata / Bundesanzeiger / EUIPO}}
sibling_g: {{org}}/{{slug}}.g
---

# Business Blueprint: {{Subject Name}}

> ⚠️ **Pipeline-side observation.** This is the Pipeline-side `.d` instance of {{Subject Name}} — a federation-readable Digital Twin built from public sources, authored by cloudsters. It is *not* the subject's own commons. If {{Subject Name}} engages, the Pipeline-side blueprint becomes the substrate for a sovereign `.o` in their own GitHub namespace: the §0 Pipeline Annotation Card is stripped at copy-time; everything below the strip marker transfers verbatim. The Wir-Perspektive of the main body is deliberate — it lets the customer adopt the document as their own voice without rewriting.

---

## §0 — Pipeline Annotation Card

> *Pipeline-side only; **removed on transfer to {{customer-org}}/{{slug}}.o**. The strip boundary is the `<!-- pipeline-annotation:end -->` marker below.*

### Stewardship Card

| Property | Value |
|---|---|
| **Steward** | {{Incubator-GmbH or @handle; *not assigned* if open}} |
| **Region** | {{cloudsters-REGION}} |
| **Brightness Orbit** | {{0 — Beacon | 1 — Bright | 2 — Active | 3 — Dim | 4 — Faint | 5 — Dark}} |
| **Lifecycle stage** | {{Collect → Expand per Spec}} |
| **MCP subscription status** | {{not active | bridging period | live; tier (Small Business / Mid-Market / Enterprise)}} |
| **Source freshness — last full refresh** | {{ISO date}} |
| **Source freshness — next due** | {{ISO date — driven by `{{slug}}-trajectory-refresh` Maintenance Loop}} |
| **Evidence quality** | {{low | medium | medium-high | high}} — {{one-sentence justification}} |
| **Account Issue** | {{org}}/{{ops-repo}}#{{number}} |
| **Workstream Board** | {{org}}/projects/{{n}} *(per Phase 5)* |

### Engagement Opportunity *(Pipeline observation)*

> *Agent Brief:* Depth = **medium**. Triangulation = the assessment must reference §2 SWOT, §4.3 Competitive Landscape, §4.4 Strategic Initiatives. Output = 3-5 sentences of structured opportunity logic. Time budget = 30 minutes.

{{Two-paragraph reasoning: where the cloudsters proposition lands on this account, what the most credible first conversation looks like, what makes a tractable initial engagement.}}

### Active Pipeline-side Loops *(Loop Registry summary; full contracts in `instance/operations/loops/`)*

| Loop | Class | Cadence | Status |
|---|---|---|---|
| `{{slug}}-trajectory-refresh` | Maintenance, Open | quarterly + event | {{status / next run}} |
| `{{slug}}-named-contacts-freshness` | Maintenance, Open | annual + LinkedIn event | {{status / next run}} |
| `{{slug}}-financial-refresh` | Maintenance, Open | annual *(post fiscal-year publication)* | {{status / next run}} |
| `{{slug}}-strategic-initiative-tracking` | Governance, Open | quarterly | {{status / next run}} |
| `{{slug}}-hiring-signal-scan` | Sensing, Closed-under-policy | monthly | {{status / next run}} |

### Known data discrepancies *(to verify in first dialogue)*

- {{e.g. "Statutory register lists X as alleinvertretungsberechtigt; website lists Y as operational lead. Resolve in first conversation."}}
- {{additional discrepancies}}

<!-- pipeline-annotation:end -->
<!-- Content above is Pipeline-side observation, removed on transfer to {{customer-org}}/{{slug}}.o -->

---

*— end of Pipeline Annotation Card. Everything below is customer-portable Wir-Perspektive. —*

---

## Foreword

> *Agent Brief:* Depth = **shallow**. Triangulation = none required. Output = ~3 short paragraphs, formal first-person. Time budget = 15 minutes. Wir-Perspektive disciplined throughout — no third-person observations bleed into the body.

### What this document is

This blueprint describes **us — {{Subject Name}}** — as a living system. It is a structured, time-layered specification of what we are today *(Baseline)*, what we aim to become *(Near Future)*, and how we move between the two *(Iterative Path)*. It is written as though the system itself were speaking.

Wir-Perspektive disciplined throughout: when we write "we", we mean {{Subject Name}} — its board, its leadership, its team, its members and partners. We do not speak about ourselves; we speak as ourselves.

### For whom it is written

| Reader | Why this lands on their desk |
|---|---|
| {{Board / Leadership}} | Strategic continuity — a structured baseline against which decisions can be tested |
| {{Funders / Owners / Shareholders / Members}} | Transparency at the level of structure, not only of finance |
| {{Operational partners}} | A shared reference for how the partnership holds itself coherent over time |
| {{Peer organisations in the sector}} | A reproducible reference; how our practice describes itself |
| {{Future co-creators}} | What we are, what we are becoming, what we ask of those who join us |

### A note on time

A blueprint is a *temporal specification*. It describes us **today** *(the Baseline, what we have committed to)* and points toward **what we are working to become** *(the Near Future, the next 12-24 months)*. The git history of this document is the record of every prior Baseline — each commit was, at some earlier moment, the Near Future, and is now what we have actually become. The long horizon *(2030+, 2040)* lives in our **Game** instance *(see §8)*.

---

# PART I — WHO WE ARE

## §1 Identity and Purpose

### §1.1 Profile

> *Agent Brief:* Depth = **shallow**. Triangulation = 2 sources for headcount, revenue, founding date. Output = the table below, every cell filled or marked `unknown`. Time budget = 20 minutes.

| Attribute | Value |
|---|---|
| **Legal name** | {{Full Legal Name}} |
| **Legal form** | {{e.g. GmbH, AG, e. V., Cooperative}} |
| **Statutory register** | {{Vereinsregister/Handelsregister entry, EUID where applicable}} |
| **NACE / sector code** | {{e.g. 94.99}} |
| **Tax / charity status** | {{gemeinnützig + tax ID / charity registration / —}} |
| **Founded** | {{Year(s) — note any predecessor / merger / rebrand}} |
| **Headquarters** | {{Street, city, country}} |
| **Contact** | {{phone · email · website}} |
| **Patron / Honorary roles** | {{Schirmherr / Honorary chair / —}} |
| **Primary geography** | {{Region of operation}} |
| **Sector / archetype** | {{Sector + Business Archetype slug}} |

### §1.2 Our purpose

> **A commons systematically creates value that is alive, shared, just, and built to last.**

{{Subject Name}} exists to {{one-sentence Bestimmung — the why; for German-language instances render "Purpose" as "Bestimmung", never "Zweck"}}.

We articulate this through the four dimensions:

| Dimension | In our system |
|---|---|
| **D1 — Bestimmung / Definition & Purpose** | {{What we exist for, the systemic outcome we serve}} |
| **D2 — Teilhabe / Participation & Relationship** | {{Who participates with us — human and non-human}} |
| **D3 — Angebot / Proposition & Exchange** | {{What we offer; what we receive in exchange}} |
| **D4 — Resilienz / Production & Resilience** | {{How value is produced and made resilient over time}} |

### §1.3 Our values and commitments

> *Agent Brief:* Depth = **medium**. Triangulation = our public commitments (Initiative Transparente Zivilgesellschaft / B-Corp / charter / Satzung / values statement). Output = 4-7 values, each with 1-2 sentences on how it is lived in practice. Time budget = 30 minutes.

| Value | How it is lived in our practice |
|---|---|
| **{{Value 1}}** | {{Lived practice — not aspiration}} |
| **{{Value 2}}** | {{Lived practice}} |
| **{{Value 3}}** | {{Lived practice}} |
| **{{Value 4}}** | {{Lived practice}} |

### §1.4 Commons-Qualities self-assessment

> *Agent Brief:* Depth = **medium**. Triangulation = the assessment is grounded in observable facts from §2 Situation Report and §5 Value Streams. Output = the table below with one-line justification per row, score 🟢 Strong / 🟡 Partial / 🔴 At Risk. Time budget = 30 minutes.

| Quality | How it shows in us | Assessment |
|---|---|---|
| **Systematic** | {{How is governance and value creation structured rather than ad hoc?}} | 🟢/🟡/🔴 |
| **Alive** | {{Does the system regenerate its participants and resources?}} | 🟢/🟡/🔴 |
| **Shared** | {{Is ownership, governance, or value shared among participants?}} | 🟢/🟡/🔴 |
| **Just** | {{Are exchanges fair? Do contributors receive proportionate value? Are the voiceless considered?}} | 🟢/🟡/🔴 |
| **Built to last** | {{Is the model sustainable? Would it survive its founders?}} | 🟢/🟡/🔴 |

### §1.5 Recent Trajectory — the events that shaped where we stand today

> *Agent Brief:* Depth = **deep**. Triangulation = primary register history *(Bundesanzeiger / Handelsregister / Vereinsregister)* plus press releases plus the company's own news archive — minimum 3 sources spanning the last 36-60 months. Output = chronological table, named-event with 1-2 sentence consequence per row. Time budget = 60-90 minutes.
> *Maintained by Loop:* `{{slug}}-trajectory-refresh` *(Maintenance, Open, quarterly + event trigger)*.

| Date / Period | Event | What it changed for us |
|---|---|---|
| {{ISO date}} | {{event}} | {{consequence}} |
| {{ISO date}} | {{event}} | {{consequence}} |

### §1.6 What we are *(in one paragraph for those who need it short)*

> *Agent Brief:* Depth = **shallow**. Triangulation = synthesis of §1.1-§1.5. Output = one paragraph, ~150 words, no bullets — readable aloud. Time budget = 20 minutes.

*{{Single-paragraph summary of who we are.}}*

---

## §2 Situation Report — Where we stand

> *Agent Brief — section:* Depth = **deep**. Triangulation per Data Triangulation Standard. SWOT block in §2.2 is mandatory output. Time budget for the full §2 section = 2-3 hours.
> *Maintained by Loops:* `{{slug}}-trajectory-refresh` *(quarterly)* and `{{slug}}-financial-refresh` *(annual)*.

### §2.1 Key metrics

| Area | Metric | Value | Source | Status |
|---|---|---|---|---|
| **Headcount** | FTE | {{value}} | {{source}} | {{confirmed / unconfirmed / inferred}} |
| **Headcount** | Total people incl. volunteers / contractors | {{value}} | {{source}} | {{status}} |
| **Financial** | Revenue / total income | {{value}} | {{source}} | {{confirmed / unconfirmed / inferred}} |
| **Financial** | Equity / reserves | {{value}} | {{source}} | {{status}} |
| **Reach** | Locations / markets / users served | {{value}} | {{source}} | {{status}} |
| **Sector-specific 1** | {{e.g. members, volunteers placed/year, units shipped, ...}} | {{value}} | {{source}} | {{status}} |
| **Sector-specific 2** | {{...}} | {{value}} | {{source}} | {{status}} |

### §2.2 SWOT — at the {{year}} Baseline

| **Strengths** | **Weaknesses** |
|---|---|
| {{strength}} | {{weakness}} |
| {{strength}} | {{weakness}} |
| {{strength}} | {{weakness}} |

| **Opportunities** | **Risks** |
|---|---|
| {{opportunity}} | {{risk}} |
| {{opportunity}} | {{risk}} |
| {{opportunity}} | {{risk}} |

### §2.3 Strengths — narrative

{{Two paragraphs translating the strengths into the narrative of who we are.}}

### §2.4 Burdens

{{One paragraph on the structural fragility we live with.}}

### §2.5 Opportunities

{{One paragraph on the systemic openings we can move into.}}

### §2.6 Risks

{{One paragraph on the long-shadow risks.}}

---

## §3 Our Ecosystem — Who participates in our system

> *Agent Brief — section:* Depth = **deep**. Triangulation = named-people verification across at least 2 sources *(website + LinkedIn + register filings)*. Output = the tables below, named decision-makers with role + responsibility + LinkedIn. Time budget = 90-120 minutes.
> *Maintained by Loop:* `{{slug}}-named-contacts-freshness` *(Maintenance, Open, annual + change event)*.

### §3.1 Our governance — Vorstand / Board *(named decision-makers)*

| Name | Role | External context | Area of responsibility with us | LinkedIn |
|---|---|---|---|---|
| {{Name}} | {{Chair / Treasurer / Beisitzer / ...}} | {{employer / civic role}} | {{what they own with us}} | {{URL}} |
| {{Name}} | {{role}} | {{context}} | {{responsibility}} | {{URL}} |

### §3.2 Our leadership — Geschäftsführung / Executive

| Name | Role | Focus | LinkedIn |
|---|---|---|---|
| {{Name}} | {{Geschäftsführung / CEO / Co-Lead}} | {{remit}} | {{URL}} |
| {{Name}} | {{role}} | {{remit}} | {{URL}} |

### §3.3 Our team

| Name (or role) | Responsibility | Notes |
|---|---|---|
| {{Name or role}} | {{responsibility}} | {{notes}} |

### §3.4 Our members / contributors *(structural)*

| Member class | Count | Right / role |
|---|---|---|
| {{e.g. institutional members}} | {{n}} | {{voting / advisory / supportive}} |
| {{e.g. personal members}} | {{n}} | {{rights}} |

### §3.5 Our stakeholder landscape

| Stakeholder archetype | What we offer them | What they bring us | Scale |
|---|---|---|---|
| {{Archetype}} | {{value proposition}} | {{value received}} | {{scale}} |

### §3.6 Non-human participants

| Non-human participant | What we tend | What it gives us |
|---|---|---|
| {{e.g. local ecosystem}} | {{stewardship act}} | {{regulation / context / identity}} |
| {{e.g. AI agents on our platform}} | {{governance of their use}} | {{capacity / reach}} |
| {{e.g. our open-source stack}} | {{contribution back}} | {{infrastructure}} |

### §3.7 Hiring Signals — where we are currently investing through hiring

> *Agent Brief:* Depth = **shallow**. Triangulation = the organisation's careers page + LinkedIn jobs + sector job boards. Output = top 5-10 open positions with role, focus area, and what it signals about our priorities. Time budget = 30 minutes.
> *Maintained by Loop:* `{{slug}}-hiring-signal-scan` *(Sensing, Closed-under-policy, monthly)*.

| Open position | Focus area | What this signals about our priorities |
|---|---|---|
| {{role title}} | {{area}} | {{signal}} |

---

## §4 Our Value Proposition

### §4.1 Our core offerings

> *Agent Brief:* Depth = **deep**. Triangulation = our own product/service catalogue + customer-facing collateral + at least one independent reference. Output = full per-offering table with key differentiator. Time budget = 60 minutes.

| Offering | Engagement shape | Scale | Key differentiator |
|---|---|---|---|
| {{Offering / Product / Service}} | {{one-time / subscription / project / programme}} | {{scale or volume}} | {{why it matters in market}} |

### §4.2 Our exchange models

| Model | Counterparty | Notes |
|---|---|---|
| {{Revenue stream / funding stream}} | {{Counterparty}} | {{Notes}} |
| {{...}} | {{...}} | {{...}} |

### §4.3 Competitive Landscape — the peers we compete with

> *Agent Brief:* Depth = **deep**. Triangulation = sector reports + competitor websites + market-intelligence sources. Output = 5-10 named peers with their positioning + relationship to us. Time budget = 60-90 minutes.

| Peer | What they do | Their positioning | Relationship to us |
|---|---|---|---|
| {{Peer name}} | {{focus}} | {{positioning}} | {{competitor / collaborator / both}} |

### §4.4 Strategic Initiatives — what we are currently doing concretely

> *Agent Brief:* Depth = **deep**. Triangulation = our press releases + investor / funder reports + named-people interviews on record. Output = 5-10 named initiatives with status, horizon, owner. Time budget = 60-90 minutes.
> *Maintained by Loop:* `{{slug}}-strategic-initiative-tracking` *(Governance, Open, quarterly)*.

| # | Initiative | Status | Time horizon | Owner |
|---|---|---|---|---|
| 1 | {{named initiative}} | {{planning / in flight / piloting / consolidating}} | {{e.g. 2026-2028}} | {{role / name}} |

---

# PART II — HOW WE WORK

## §5 Value Streams Overview

> *Agent Brief — section:* Depth = **very deep**. Triangulation per VSF: at least 2 sources for the Element table content; at least 2 sources for any named-people entry in Value Stream Team. Output per VSF: the 8-element BEN cascade table + Value Stream Team table + Linked Artifacts list. Time budget per VSF = 60-90 minutes. Section total = 16-20 hours; this is the heart of the work.

The 14 canonical business value-stream families. Each cascade is **outside-in**:

**Stakeholder → Value Proposition → Journey → Touchpoints → Value Stream → Capabilities → Solutions → Organisation.**

For every VSF the structure below is mandatory: the 8-element Element table, the Value Stream Team table (named customer-side stakeholders with the Steward-side practitioner mapping), and the Linked Artifacts block pointing to patterns, evidence files, and the loop contract that keeps that stream honest over time.

### Dimension 1 — Definition & Purpose

#### §5.1 Identity to Mandate

*How we define our identity, secure our mandate to operate, and govern ourselves.*

| Element | Manifestation |
|---|---|
| **Primary stakeholders** | {{named people, roles, entities}} |
| **Value proposition** | {{what this stream delivers to its stakeholders}} |
| **Journeys** | {{the stakeholder journeys this stream serves}} |
| **Touchpoints** | {{interaction points, systems, documents}} |
| **Value Stream** | {{Step A → Step B → Step C → ...}} |
| **Capabilities** | {{named capabilities required}} |
| **Solutions** | {{specific tools, systems, platforms in use}} |
| **Organisation** | {{responsible roles, teams, governance}} |

##### Value Stream Team

| Member | Role | Lens |
|---|---|---|
| {{Name from §3 board / leadership / team}} | {{their role here}} | {{customer-side perspective}} |

##### Linked Artifacts

- Pattern: {{cross-reference to operational patterns}}
- Evidence: `instance/workshop/evidence/{{file}}.md` *(Phase 1 source)*
- Loop contract: `instance/operations/loops/{{slug}}-identity-mandate-review.yml`

#### §5.2 Purpose to Portfolio

*How our purpose is translated into a concrete portfolio of offerings.*

*(Element table + Value Stream Team + Linked Artifacts per the §5.1 pattern. Loop contract: `instance/operations/loops/{{slug}}-purpose-portfolio-review.yml`)*

#### §5.3 Value to Profit

*How value created is captured, accounted for, and reinvested.*

*(Element table + Value Stream Team + Linked Artifacts per the §5.1 pattern. Loop contract: `instance/operations/loops/{{slug}}-financial-currency-check.yml`)*

#### §5.4 Portfolio to System

*How the technological and informational architecture is designed and managed.*

*(Element table + Value Stream Team + Linked Artifacts per the §5.1 pattern. Loop contract: `instance/operations/loops/{{slug}}-portfolio-system-review.yml`)*

### Dimension 2 — Participation & Relationship

#### §5.5 Participants to Community

*How isolated stakeholders become a living community. Public narrative, governance participation.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-community-pulse.yml`)*

#### §5.6 Collaboration to Automation

*How collaboration turns into reliable patterns, quality management, and eventual automation.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-collaboration-quality-check.yml`)*

#### §5.7 Hire to Retire

*How contributors are attracted, developed, retained, and transitioned.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-workforce-pulse.yml`)*

#### §5.8 Welcome to Transition

*How entry and exit are designed to ensure psychological safety and knowledge transfer.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-transition-pulse.yml`)*

### Dimension 3 — Proposition & Exchange

#### §5.9 Discovery to Usage

*How offerings are designed, developed, and experienced by the user.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-discovery-pulse.yml`)*

#### §5.10 Lead to User

*How potential users find us, build trust, and become active participants.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-pipeline-pulse.yml`)*

#### §5.11 Distribution to Market

*How the value proposition reaches the market and the ecosystem.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-distribution-pulse.yml`)*

### Dimension 4 — Production & Resilience

#### §5.12 Demand to Fulfillment

*How products or services are actually produced and delivered.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-fulfillment-pulse.yml`)*

#### §5.13 Source to Pay

*How materials, tools, and external services are procured and paid for.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-procurement-pulse.yml`)*

#### §5.14 Acquire to Retire

*How physical and digital assets are managed throughout their lifecycle.*

*(Element table + Value Stream Team + Linked Artifacts. Loop contract: `instance/operations/loops/{{slug}}-asset-pulse.yml`)*

### §5.15 Capability Heatmap *(consolidated)*

> *Agent Brief:* Depth = **deep**. Triangulation = drawn from the 14 VSF cascade tables above. Output = consolidated table with one row per named capability, scored Maturity 🟢/🟡/🔴 with named gap and priority. Time budget = 60 minutes.

| Dimension | Capability | Maturity | Gap | Priority |
|---|---|---|---|---|
| D1 | {{Capability}} | 🟢 Strong | — | — |
| D1 | {{Capability}} | 🟡 Partial | {{gap}} | {{High / Mid / Low}} |
| ... | ... | ... | ... | ... |

*Heatmap reading: {{2-3 sentences synthesising where we are strong, where we are fragile, what investments matter most.}}*

---

# PART III — WHERE WE ARE HEADING

## §6 Change Drivers — What is forcing the system to change

> *Agent Brief:* Depth = **deep**. Triangulation = §1.5 Recent Trajectory + §4.3 Competitive Landscape + §2.6 Risks + §1.4 Commons-Qualities assessment. Output = 5-10 drivers in the table, intensity scaled ●●●●●. Time budget = 60 minutes.

| # | Driver | Time horizon | Affected VSFs | Intensity |
|---|---|---|---|---|
| T1 | **{{Driver}}** — {{description}} | {{years}} | {{e.g. 5.3, 5.10}} | ●●●●○ |
| T2 | **{{Driver}}** — {{description}} | {{years}} | {{...}} | ●●●○○ |

## §7 Change Needs per Value Stream

| # | Value Stream | Driver | Required Change | Urgency |
|---|---|---|---|---|
| 5.X | {{Name}} | T1 | {{Required change}} | 🔴 High |
| 5.Y | {{Name}} | T2 | {{Required change}} | 🟡 Medium |

## §8 Bridge to OS and Game

### §8.1 The three instances

| Instance | Suffix | Owner / Author | Visibility | Location |
|---|---|---|---|---|
| **Domain** | `.d` | {{this document — Pipeline-side cloudsters / sovereign customer post-transfer}} | {{visibility}} | {{location}} |
| **Operations** | `.o` | {{Customer-sovereign — post-engagement only}} | {{visibility}} | {{location}} |
| **Game** | `.g` | {{Pipeline-side cloudsters / sovereign customer post-transfer}} | {{visibility}} | {{location}} |

### §8.2 What the Game Blueprint projects *(short version)*

*See `{{slug}}.g/blueprint.md` for the full Δ view and `{{slug}}.g/instance/workshop/analysis/scenarios-2050.md` for the 50-scenario environment scan. In short:*

- **Near-term *(transition timeslice)*:** {{1-2 sentences}}
- **Mid-term *(consolidation timeslice)*:** {{1-2 sentences}}
- **Horizon *(2032 / equivalent)*:** {{1-2 sentences}}
- **North Star *(2040)*:** {{1-2 sentences}}

### §8.3 What is next concretely

| # | Initiative | Driver | Dimension | Urgency |
|---|---|---|---|---|
| 1 | {{Concrete next step}} | T1 | `d1-purpose` | 🔴 Immediate |
| 2 | {{...}} | T2 | `d4-production` | 🟡 Next 12 months |

---

# APPENDICES

## Appendix A — Entity Map

*The core entities involved with us. Activated in `instance/registry/5_entities/`.*

| Entity | Type | Relationship to us |
|---|---|---|
| {{Entity}} | {{type from business-essentials pack}} | {{relationship}} |

## Appendix B — Capability Map

*Critical capabilities for our operating model. See §5.15 for the heatmap.*

- {{Capability 1}}
- {{Capability 2}}
- ...

## Appendix C — Source References

*All sources used in the construction of this blueprint. Underpins the evidence directory at `instance/workshop/evidence/`.*

- [{{Source title}}]({{URL}})
- ...

## Appendix D — Open Questions for First Dialogue *(Pipeline-side annotation; stripped on transfer)*

> *Pipeline-side observer questions that sharpen what we know. Removed on transfer to customer's `.o`.*

| # | Question | Why it helps |
|---|---|---|
| 1 | {{Question}} | {{Why}} |

---

*Domain Blueprint v0.2 · {{Subject Name}} · {{Pipeline-side | Customer-sovereign}} · {{Region or Customer Org}} · {{ISO date}}*
*Maintained on the loops declared in §0 / `instance/operations/loops/`. Companion: `{{slug}}.g/blueprint.md` (Game).*
