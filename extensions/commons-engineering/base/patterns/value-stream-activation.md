---
# ===============================================================
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ===============================================================
id: pat_01kkhc8hch2mdnv7295yf7eb2j
orbital_layer: 2
sector: "Universal"
gravitational_hubs:
  - hub_id: "commons-blueprint"
    influence: 0.9
  - hub_id: "value-stream-specification"
    influence: 0.8

# ===============================================================
# GROUP 1: CORE IDENTITY
# ===============================================================
slug: value-stream-activation
title: "Value Stream Activation"
aliases:
  - "Selective Stream Loading"
  - "Capability Feature Flagging"
  - "Stream Activation Matrix"
summary: >-
  A pattern for selectively activating and deactivating value streams
  based on the commons' current purpose, maturity, and capacity —
  ensuring that the operating system loads only the streams the
  system actually needs at this moment in its lifecycle.

# ===============================================================
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ===============================================================
context_labels:
  corporate: "Module Activation and Capability Roadmap"
  government: "Service Portfolio Prioritisation"
  activist: "Campaign Focus and Resource Allocation"
  tech: "Feature Flagging and Microservice Enablement"

# ===============================================================
# GROUP 3: ONTOLOGY & VITALITY (The RAG Fuel)
# ===============================================================
ontology:
  domain: meta
  cross_domains:
    - business
    - life
    - urban
    - ecology
  commons_domain:
    - commons-engineering
  search_hints:
    primary_tension: "Comprehensive Coverage vs. Focused Capacity"
    vector_keywords:
      - value streams
      - activation
      - feature flags
      - capacity management
      - module enablement
      - selective loading
      - portfolio management
      - operational focus
  commons_assessment:
    stakeholder_architecture: 4
    value_creation: 5
    resilience: 4
    ownership: 4
    autonomy: 5
    composability: 5
    fractal_value: 5
    vitality: 4.5
    vitality_reasoning: >-
      This pattern directly serves vitality by preventing the commons from
      overextending itself. A system that activates only the streams it can
      sustain is a system that breathes within its actual capacity, not one
      gasping for air under the weight of aspirational but unfunded processes.
      It enables focused growth and honest self-assessment.
    overall_score: 4.5

# ===============================================================
# GROUP 4: LIFECYCLE & CONFIDENCE
# ===============================================================
lifecycle:
  usage_stage: foundation
  adoption_stage: seed
  status: active
  version: 0.1
  confidence: 2

# ===============================================================
# GROUP 5: RELATIONSHIPS (Human-Curated Graph)
# ===============================================================
relationships:
  generalizes_from:
    - slug: value-stream-specification
      weight: 0.9
      source: curated
    - slug: self-organization-and-subsidiarity
      weight: 0.7
      source: curated
  specializes_to: []
  enables:
    - slug: operating-rhythms
      weight: 0.7
      description: "Active streams define what rhythms are needed."
    - slug: resource-orchestration
      weight: 0.8
      description: "Activation decisions drive resource allocation."
  requires:
    - slug: purpose-definition
      weight: 0.9
      description: "Purpose determines which streams matter."
    - slug: commons-boundary-definition
      weight: 0.7
      description: "Boundaries constrain what streams are feasible."
  alternatives: []
  complementary:
    - slug: transformation-sequencing
      weight: 0.7
      description: "Sequencing governs the order of activation over time."
  tools: []

# ===============================================================
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ===============================================================
graph_garden:
  last_pruned: 2026-03-12
  entities:
    - Value Stream
    - Feature Flag
    - SAP Module Activation
    - Commons OS
    - config.yml
    - Capacity Management
  communities:
    - commons-os-operations
    - value-architecture
  inferred_links: []

# ===============================================================
# GROUP 7: PROVENANCE
# ===============================================================
contributors:
  - higgerix
  - cloudsters
sources:
  - "Commons Engineering Framework"
  - "Commons OS Specification v0.1"
  - "SAP module activation methodology"
  - "Microservice feature flag patterns"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
---

> Not every commons needs every stream. Activate what you can sustain, deactivate what you cannot — and be honest about the difference.

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This rating reflects direct observation across enterprise module activation, feature flagging in distributed systems, and the Commons Engineering value stream family model. Not yet proven across all four domains at scale.

---

### Section 1: Context

**Lineage:** This pattern generalises from Value Stream Specification and Self-Organisation and Subsidiarity, serving the Universal sector as an Orbit 2 architectural building block for Commons OS.

Every living system has the theoretical capacity to do far more than it actually does at any given moment. A human body contains the genetic instructions for every protein it will ever need, but at any given instant only a fraction of those genes are expressed. A city has the infrastructure for dozens of public services, but budget constraints mean only some operate at full capacity in any given fiscal year. An enterprise has a reference architecture describing hundreds of capabilities, but a startup with three people cannot — and should not — attempt to run all of them.

The same is true for a commons operating on Commons OS. The full value stream family catalogue describes the complete operational surface of a mature, fully realised commons: from Purpose to Portfolio, Participants to Community, Discover to Usage, Source to Pay. But a newly forked commons — whether it is a personal `me-os`, a startup forking `business-os`, or a neighbourhood forking `urban-os` — does not need all of them. Attempting to activate every stream from day one is not ambition; it is a form of organisational overreach that dilutes focus, burns capacity, and creates the illusion of completeness where none exists.

The question is not "which streams exist?" but "which streams should be alive right now?"

---

### Section 2: Problem

> **The core conflict is Comprehensive Coverage vs. Focused Capacity.**

The forces at play here are universal across every domain where a system must decide what to run and what to leave dormant.

**Force 1: Completeness vs. Reality.** Reference architectures and process frameworks — from APQC's Process Classification Framework to TOGAF capability maps — describe the full surface area of an idealised system. They are comprehensive by design. But comprehensiveness is a map, not the territory. The territory is constrained by actual people, actual funding, actual time. When a system treats the reference map as a to-do list rather than a menu, it drowns in process overhead before it delivers any value. The carpenter who lays out every tool in the workshop before cutting the first joint will never build the house.

**Force 2: Ambition vs. Honesty.** There is a cultural bias — especially in enterprise and startup contexts — toward declaring capabilities as "active" when they are aspirational at best. An organisation claims to run hire-to-retire when it has one spreadsheet tracking three contractors. A city claims to operate a citizen-engagement programme when it sends a quarterly newsletter. This dishonesty about actual operational state makes the system opaque to itself. It cannot diagnose what is missing if it believes everything is present.

**Force 3: Uniformity vs. Contextuality.** Not every fork of an OS needs the same streams. A `me-os` for personal knowledge management does not need source-to-pay. A cooperative bakery does not need distribute-to-market if it sells only from its shopfront. A mycorrhizal network has no use for hire-to-retire. Treating all instances as identical — requiring the same streams regardless of purpose, domain, or scale — violates the principle of subsidiarity and destroys the very composability that makes the OS valuable.

**Force 4: Stability vs. Evolution.** The set of active streams is not static. A commons grows, and as it grows, streams that were dormant become necessary. A startup that bootstrapped without hire-to-retire eventually needs it when it hires its tenth person. A forest recovering from fire reactivates nutrient-cycling streams as the canopy returns. The activation state must evolve with the system's lifecycle, not be frozen at fork time.

---

### Section 3: Solution

> **Therefore, maintain an explicit activation register that declares which value streams are active, which are dormant, and which are planned — and review this register as part of the commons' operating rhythm.**

The mechanism is straightforward. Every Commons OS instance carries a configuration file — canonically `config.yml` at the root of the repository — that lists all available value streams alongside their activation status. Each stream entry declares one of three states:

| State | Meaning |
|---|---|
| **active** | This stream is operational. Resources are allocated. Outcomes are expected and measured. |
| **dormant** | This stream exists in the reference catalogue but is intentionally not running. No resources are allocated. No outcomes are expected. |
| **planned** | This stream is scheduled for activation. A target date or trigger condition is defined. Resources are being prepared. |

The configuration is not buried in a strategy document or a slide deck. It lives in the same repository as the rest of the operating system — versioned, diffable, reviewable. When someone asks "do we run source-to-pay?", the answer is a `git grep`, not a meeting.

The activation register is governed by the Purpose Agent (D1), because the decision of which streams to activate is fundamentally a purpose-alignment decision. The Production Agent (D4) implements the activation by provisioning the operational infrastructure for each active stream. The Participation Agent (D2) and Proposition Agent (D3) advise, because their streams are the ones being activated or deactivated.

The key architectural insight is that **dormancy is not failure**. A dormant stream is not a gap to be anxiously filled. It is a conscious decision that this capability is not needed yet, or not needed here. The dormancy is itself information — it tells the system (and any observer) what this commons has chosen not to do, which is as important as what it has chosen to do.

```yaml
# config.yml — Value Stream Activation Register
value_streams:
  purpose_to_portfolio:
    status: active
    owner: d1_purpose
    since: 2026-03-01

  participants_to_community:
    status: dormant
    owner: d2_participation
    reason: "Solo founder phase — no community to cultivate yet"

  discover_to_usage:
    status: active
    owner: d3_proposition
    since: 2026-03-01

  source_to_pay:
    status: planned
    owner: d4_production
    target: 2026-Q3
    trigger: "First external supplier contract"
```

---

### Section 4: Implementation

**Step 1: Fork with defaults, then prune.**

When a commons forks its OS distribution, the fork comes with a default activation profile suited to its domain template. A `business-os` fork might activate purpose-to-portfolio and discover-to-usage by default, leaving hire-to-retire and source-to-pay dormant. A `me-os` fork activates only the personal streams. The first act of the new commons is to review these defaults and adjust them to its actual situation. This is not a planning exercise; it is a declaration of honest operational state.

**Step 2: Write the register into config.yml.**

The activation register lives in `config.yml` at the repository root, alongside other OS configuration. Each stream entry includes: the stream identifier, the activation status (`active`, `dormant`, `planned`), the owning agent dimension, the activation date (for active streams), and a reason (for dormant streams). The reason field matters. "Dormant because solo founder" is a different story than "dormant because we tried it and it failed." Both are valid; both are worth recording.

**Step 3: Connect activation to the operating rhythm.**

The activation register is reviewed during the quarterly alignment check (see: Operating Rhythms, pat_01kkhc8hcm3qbsvvzjc8v6vc9r). The Purpose Agent asks: "Are our active streams still the right ones? Has anything changed that means a dormant stream should wake up, or an active stream should go to sleep?" This is not a bureaucratic review; it is a vital signs check. The system is asking itself: "Am I running the right processes for who I am now?"

**Step 4: Use activation state to drive dashboards and sensing.**

Active streams have associated metrics, KPIs, and sensing mechanisms. Dormant streams do not. The activation state therefore drives what the system measures and monitors. There is no point in tracking customer acquisition metrics if the discover-to-usage stream is dormant. There is no point in monitoring supplier performance if source-to-pay is not active. The activation register is the control plane for the system's nervous system.

**Step 5: Define activation triggers for planned streams.**

A planned stream has a trigger condition: a date, a headcount threshold, a revenue milestone, a community size. When the trigger fires, the stream moves from planned to active. This can be automated — a CI pipeline checks triggers against current state and opens an issue when a stream is ready for activation — or it can be manual, surfaced during the operating rhythm review. Either way, the trigger makes the transition from dormancy to activity a conscious, traceable event.

**Step 6: Honour deactivation as a legitimate move.**

Streams can move from active to dormant. This is not failure; it is pruning. A commons that tried running a community programme and found it had insufficient participation to sustain it should deactivate the stream, record the reason, and revisit when conditions change. The record of activation and deactivation over time becomes a lifecycle narrative — the system's autobiography of what it tried, when, and why.

---

### Section 5: Consequences

**Benefits:**

| Benefit | Description |
|---|---|
| **Operational honesty** | The system knows what it actually runs, not what it wishes it ran. This honesty is the foundation for all other sensing and governance. |
| **Resource efficiency** | Resources flow only to active streams. There is no overhead from maintaining the fiction of capabilities that are not actually operating. |
| **Composability** | Different forks can activate different stream profiles, making the OS genuinely adaptable to different purposes, scales, and domains. |
| **Lifecycle awareness** | The activation history tells the story of the commons' evolution — from a focused seed to a more complex mature system. |
| **Diagnostic clarity** | When something goes wrong, the activation register is the first place to look. Is the relevant stream actually active? Is it staffed? Is it measured? |

**Liabilities:**

| Liability | Description |
|---|---|
| **Premature pruning** | A commons might deactivate streams too aggressively, leaving gaps that only become visible during a crisis — like removing smoke detectors because there has not been a fire. |
| **Status quo bias** | Once a stream is dormant, inertia may keep it dormant longer than it should be. The planned-state mechanism mitigates this, but only if triggers are actually defined and monitored. |
| **Activation theatre** | The register can be gamed — marking streams as "active" when they are minimally operational, to look more mature than the commons actually is. This defeats the purpose of honest self-assessment. |
| **Coordination cost** | Activating a new stream is not free. It requires resources, attention, and often new capabilities. The register makes the cost visible but does not eliminate it. |

---

### Section 6: Known Uses

**SAP Module Activation.** The enterprise resource planning world has practiced this pattern for decades. An SAP implementation does not activate all modules on day one. A company begins with Finance (FI) and Controlling (CO), then adds Materials Management (MM) when procurement becomes complex enough to warrant it, then Human Capital Management (HCM) when headcount crosses a threshold. The activation sequence is governed by the implementation roadmap, and each module activation is a project in itself. The parallel to value stream activation is direct: the ERP is the operating system, the modules are the value streams, and the activation register is the project plan. What SAP learned — and what every implementation consultant knows — is that activating too many modules too fast is the single most common cause of ERP project failure.

**Microservice Feature Flags.** In distributed systems architecture, feature flags allow engineering teams to deploy code for new capabilities without activating them for users. The code exists in the repository; the capability exists in the architecture; but the feature is dormant until the flag is flipped. This gives teams the ability to separate deployment from activation — to ship code on their own schedule and activate features on the user's schedule. LaunchDarkly, Unleash, and similar platforms have built entire businesses around this pattern. The underlying insight is identical to value stream activation: the capability catalogue is larger than the active capability set, and the gap between them is managed explicitly, not accidentally.

**Commons Engineering Value Stream Families.** The Commons Engineering project itself practices this pattern. In its current solo-founder phase, only a subset of value streams are active: purpose-to-portfolio (D1) and discover-to-usage (D3) are operational, while participants-to-community (D2) is dormant (no community to cultivate yet) and source-to-pay (D4) is planned for when external supplier relationships begin. The activation register in `config.yml` makes this explicit, and the quarterly review surfaces whether conditions have changed enough to activate a dormant stream.

**Seasonal Agricultural Rhythms.** A farm does not plant every crop in every season. The decision of which fields to plant, which to leave fallow, and which to prepare for the next rotation is a form of value stream activation governed by soil condition, market demand, and available labour. A field left fallow is not wasted; it is recovering. The farmer's crop plan is the activation register, reviewed and adjusted each season based on actual conditions, not aspirational yields.

---

### Section 7: Cognitive Era

In the Cognitive Age, value stream activation becomes a dynamic, AI-assisted capability rather than a static configuration reviewed quarterly. An AI Purpose Agent can continuously monitor the conditions that determine whether a stream should be active, dormant, or planned — and surface recommendations to the human founder or governance board when conditions change.

Imagine a commons where the Purpose Agent monitors external signals (market shifts, community growth, regulatory changes) and internal signals (resource utilisation, quality metrics, participant satisfaction) and generates an activation recommendation: "The discover-to-usage stream has reached capacity. Recommend activating distribute-to-market to handle the overflow." The human decides; the agent advises.

More powerfully, the activation register becomes a training signal for the AI itself. By observing the history of activations and deactivations — what worked, what was premature, what was delayed too long — the agent learns the commons' activation rhythm and can predict when streams will be needed before the humans notice. This is not automation replacing judgement; it is intelligence augmenting judgement with pattern recognition across a history that no single human can hold in memory.

The danger, as always, is over-automation. An AI that activates and deactivates streams without human oversight risks optimising for efficiency at the expense of values that are not easily measured — community warmth, creative exploration, strategic patience. The activation decision must remain a governance act, not a purely computational one.

---

### Section 8: Vitality

**Signs of life:** A commons practising healthy value stream activation has a crisp, honest answer to the question "what do you actually run?" The activation register is current, reviewed regularly, and reflects reality. Active streams are genuinely operational — staffed, measured, producing outcomes. Dormant streams have recorded reasons that make sense. Planned streams have defined triggers that the system is actively monitoring. There is no gap between the declared state and the actual state. The system is self-aware: it knows what it is, what it is not, and what it intends to become. When a new participant joins the commons, they can read the register and understand immediately what is operational and what is aspirational. This clarity is itself a form of vitality — the system is legible to itself and to others.

**Signs of decay:** The activation register has not been updated in months. Active streams exist on paper but have no resources allocated. Dormant streams have no recorded reasons — they are dormant by neglect, not by decision. Planned streams have no triggers, or their triggers fired long ago and nobody noticed. The declared state and the actual state have diverged, and nobody knows which is true. The system is performing completeness — pretending to run capabilities it does not actually have — rather than practising honesty about its actual operational surface. Participants are confused about what the commons actually does, because the map no longer matches the territory. This is the early stage of organisational decay: the system has lost its self-awareness, and without self-awareness, it cannot self-correct. The activation register has become a dead document rather than a living instrument of governance.
