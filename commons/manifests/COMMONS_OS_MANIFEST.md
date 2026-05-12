# COMMONS OS MANIFEST
*The Operating System for Commons-Based Organisation*

**Version:** 1.2
**Status:** Living Document
**Companion:** COMMONS_AGENT_MANIFEST.md, COMMONS_BLUEPRINT_MANIFEST.md, COMMONS_OS_SPEC.md, COMMONS_DOMAINS_MANIFEST.md, COMMONS_GAMES_MANIFEST.md

---

## Preamble

The name is not an accident. Commons OS is an operating system — not a framework.

A framework gives you tools. An operating system gives you everything you need to operate: a file format for describing any organisation, a networking stack for managing relationships, a runtime for every node, services that serve intelligence recursively, and an API layer that delivers ambient knowledge on demand.

"OS" is infrastructure vocabulary — what phones, cities, enterprises, and ecosystems run. The concept is direct: you fork the Commons OS just as you would fork a software distribution, preserving lineage while gaining full autonomy. What grows inside is the commons.

The centre is empty. The protocols are shared. The nodes are sovereign.

---

## §1 What a Commons Is

> **A commons systematically creates value that is alive, shared, just, and is built to last.**
> — *Canonical definition. Source: `commons/patterns/principles/the-commons.md` (Orbit 1)*

A **commons** is a living system that emerges when participants — human or machine — engage inside a forked instance of the Commons OS. The instance provides the boundary — an empty-centre layer on a piece of reality. That reality can be a city, a topic, a company, an ecological watershed, a person's life, or anything else a community chooses to organise around. What makes it a commons is not what it wraps — it is the shared pattern language, the fractal architecture, and the participation that fills it with life.

The five qualities of a commons — **systematically, alive, shared, just, built to last** — are not aspirations. They are the design criteria against which every commons is measured. A system that creates value but is not just is not a commons. A system that is just but not built to last is not a commons. All five must hold.

A forked instance without participation is a companion awaiting its commons — structure, intelligence, and protocol fully present, but dormant. A commons without an OS instance is purpose without a companion to serve it. The two call each other into existence.

### §1.1 Purpose and Participation Define the Commons

The four Universal Dimensions structure every commons:

| Dimension | Role in the commons |
|---|---|
| **Definition & Purpose** | WHAT this commons exists for — the boundary and topic. A geography, a domain of knowledge, an organisation, a life — the subject is context. The dimension is universal. |
| **Participation & Relationship** | WHO engages — the network of actors: human, machine, and organisational. Their relationships are the connective tissue of the commons. Without this network, the commons does not exist in any meaningful sense. |
| **Proposition & Exchange** | WHAT value is created and exchanged — the products, services, and knowledge this commons produces. The specific outputs are determined by the commons' purpose; the form they take varies across Life, Ecology, Urban, and Business domains. |
| **Production & Resilience** | HOW value is produced and sustained — infrastructure, production processes, material and information flows, supply chains, and economics. The means by which the commons fulfils its proposition, resiliently across time. |

The first dimension IS the topic. The remaining three are how you achieve the purpose, either one-time or recurring. If the commons is resilient, collaborative, just, systematic value creation, then it does not matter whether the commons wraps a geography or a thing. The structure is the same. Justice — the commitment that value creation serves all stakeholders fairly — is not a fifth dimension but a quality that pervades all four. In the Cognitive Era, where AI amplifies whatever the specification contains and ignores what it omits, the explicit encoding of justice is not optional — it is the design constraint that prevents Commons as Code from becoming Enclosure as Code.

### §1.2 Multiple Layers on the Same Reality (Set Theory)

A commons is a layer, not a territory. Multiple commons can coexist on the same piece of reality, each with its own purpose and participation:

| Commons | Purpose (Dim 1) | Participation (Dim 2) |
|---|---|---|
| `[city]-os` | Incubate commons in local enterprises | Incubator team + local partners |
| `[city]-transition` (future) | Energy transition in the city | Local activists, utilities |
| `[city]-university` (future) | Academic commons research | University researchers |

All on the same territory. All using commons.engineering frameworks. All autonomous. Not competing — different lenses on the same reality.

This is Set Theory, not territorial exclusivity. Entities can be visible through multiple commons lenses. An entity's `commons` field may reference multiple instances.

### §1.3 The Chaordic Principle

The architecture follows the chaordic model (Dee Hock, Visa): shared protocols, autonomous nodes.

- **Shared:** The four curated collections, the four-agent governance model, the MCP service layer, the specifications. These are the interchange format.
- **Autonomous:** Each commons decides its own purpose, its own participation, its own rhythms, its own economics. Conformance to the shared specs makes commons interoperable — not subordinate.

Coherence comes from the shared pattern language, not from a central authority. The centre is empty. A commons that produces good work and contributes to the shared intelligence is pulled inward by the gravitational force of shared knowledge and shared identity. A commons that extracts without contributing drifts outward toward irrelevance.

### §1.4 Fractal Architecture

Every commons contains a constellation of entities — organisations, people, and systems it relates to, arranged in orbital layers from the inside out. And every entity is potentially a commons with its own constellation. This creates a truly fractal system of systems.

A small bakery forks the Commons OS. Within its commons:

| Orbit | Entity | Relationship |
|---|---|---|
| 0 | The bakery itself | Identity (self-entity) |
| 1 | The flour mill | Key supplier |
| 1 | The neighbourhood cooperative | Key customer |
| 2 | The organic certification body | Regulation |
| 3 | The energy cooperative | Infrastructure |
| 4 | The grain farmer in the region | Deep supply chain |

Now flip the lens: the flour mill is a commons too. The bakery appears as an entity in the mill's orbital system. Every entity is simultaneously visible from outside (through another commons' lens) and a commons from inside (containing its own constellation).

The equivalence: **a commons' stakeholder map IS its entity constellation.** The orbital system IS the relationship map. The vitality of the commons is not about the entity alone — it is about the health of its entire web of relationships.

The carpenter's principle: a timber frame is not one beam. It is the joints between all of them.

### §1.5 Entity Multiplicity

The same entity can exist as many instances across different commons, each with its own orbital layer, depth, and scorer:

| Commons | The same entity as instance | Depth |
|---|---|---|
| Commons.Engineering | Orbit 2, exemplary case | Public data (governance reports, ownership docs) |
| `[region]-os` | Orbit 1, local neighbour | Supply chain, interviews, ecological impact |
| `[sector]-os` | Orbit 1, industry peer | Comparison against sector peers |

All three instances use the same four dimensions, the same `commons_vitality` block, the same One Order format. They differ in resolution, orbital position, and scorer expertise. This is cartography: the world map shows coastlines, the regional map shows harbours, the local chart shows every dock. Same reality, different depth, different purpose. The entity format is the projection system that makes all maps legible. Commons Engineering provides an entity briefing spec as an extension pack for Business and Urban domains.

The `slug` is the linking key for cross-instance identity — the underlying entity is one; the instances are many. A commons can fork an exemplary entity from Commons.Engineering as a starting point and enrich it locally.

### §1.6 Resolution Varies

From a global perspective, it may be interesting that a business entity is located within a particular urban entity's territory. But the little SME around the corner — that matters to the local community, and only to them.

Local detail stays local. Only aggregation and learning flow upward. A commons at one scale does not need to burden commons at other scales with its full resolution. The MCP service layer enables this: queries return detail appropriate to the requester's context and tier.

---

## §2 The Commons Operating System

### §2.1 OS Components

| OS concept | Commons OS equivalent |
|---|---|
| **Kernel** | Four core agents — Purpose, Participation, Proposition, Production (§3) |
| **Extensions** | Domain-specific on-demand agents added per use case (§3.2) |
| **Package manager** | Pattern library + MCP tiered access (§5) |
| **File format** | The Living Blueprint (L1-L9) specifies the commons from the inside. Entity formats (available as extension packs) describe entities from the outside. The blueprint is the core file format of the OS. |
| **Networking** | Commons-to-commons protocols, engagement graph |
| **User accounts** | Participation gradient (§6) |
| **Version control** | Git — every change traced, every decision a commit, lineage preserved across forks |
| **Issue tracker** | Deliberation container — ideas, decisions, and tasks between humans and agents |
| **Operations dashboard** | Project board — visual state of all work across the commons |
| **Security model** | Private workshop + tiered publishing + access-controlled MCP endpoints |
| **Update mechanism** | Recursive self-improvement — commons feed learning back, agents improve, specs evolve |
| **Distributions** | Incubators' interpretations — each incubator builds its own "distro" on the shared OS |
| **Install** | Fork the Commons OS → Agent guides onboarding → MCP connects to intelligence |

### §2.2 What Makes This an OS, Not a Framework

- The **Living Blueprint** (L1-L9) specifies the commons from the inside — its purpose, architecture, governance, culture, and intelligence. This is the core file format of the OS. Entity briefing formats (such as the Business and Urban entity specs available as CE extension packs) describe entities from the outside — a diagnostic one-order-object for ANY organisation. The blueprint is the OS format; entity formats are extensions.
- The **engagement management system** manages ANY relationship lifecycle. This is the networking stack.
- The **commons instance** runs ANY commons node. This is the runtime.
- The **agents** serve intelligence recursively and self-improvingly. These are the services.
- The **MCP infrastructure** delivers ambient intelligence at tiered access. This is the API layer.

A new community or organisation **forks** the Commons OS and has a functioning operating system for commons-based value creation. Fork — not clone — because it preserves lineage back to the source while giving full autonomy. The chaordic principle in Git terms.

### §2.3 The Three-Layer Architecture

Commons.Engineering is **not** a database of all organisations. It is the **intelligence**. Three distinct layers serve different roles:

| Layer | Role | What it provides | Scale |
|---|---|---|---|
| **Commons.Engineering** | Cognitive service layer | Curates exemplary entities that train the pattern models. Provides intelligence, format standards, cognitive services at the edge. | Dozens to low hundreds of exemplary entities across all 4 domains. Quality over quantity. |
| **Incubators** (cloudsters and others) | Operators | Fork the OS, inject participation, operate commons commercially or non-commercially. Aggregate signals across their commons. | Hundreds of entities per commons. Depth suited to each purpose. |
| **Any founder** | Permissionless forkers | Fork the Commons OS, shape their own commons, pull cognitive services from CE. | Unbounded. Fractal. |

The critical distinction: any attempt to create ALL entities centrally would create exactly the monolith the architecture exists to avoid. CE needs *exemplary* entities — enough to train the pattern models, validate the dimensions, and demonstrate the format. The depth and breadth happen at the commons level.

### §2.4 Commons as Code — The 3-MCP Architecture

**Commons as Code** is the central claim of Commons Engineering: a living system — its purpose, governance, relationships, value streams, and intelligence — expressed entirely as code, version-controlled, forkable, and operable by humans and agents together. Where "Infrastructure as Code" made servers programmable and "Organisation as Code" made enterprises scriptable, Commons as Code makes any living system — a person, a business, a city, an ecosystem — governable through the same protocol.

A commons connects to intelligence through **three MCP channels**:

| MCP Channel | Operator | Architectural role |
|---|---|---|
| **Commons MCP** | cloudsters / CE | **Shared intelligence** — the collective knowledge of the commons.engineering ecosystem |
| **Blueprint MCP** | Client-owned | **Local sovereignty** — the commons' own workspace as a queryable knowledge graph |
| **Fabric MCPs (1..n)** | Client-owned | **Operational reality** — the organisation's Systems of Record (ERP, CRM, HR, IoT, ...) |

The architectural principle: the **Blueprint MCP** and **Fabric MCPs** are owned and operated by the commons itself, not by cloudsters. The Commons MCP provides shared intelligence; the Blueprint and Fabric MCPs provide local sovereignty. Data sovereignty is not negotiable — it is architectural.

This three-channel separation is the infrastructure equivalent of the chaordic principle: shared protocols (Commons MCP), autonomous nodes (Blueprint + Fabric MCPs). Through MCP, the agent sees the collective knowledge, the local state, AND the operational reality — all through the same protocol. The Living Blueprint is not just a document — it is a live connection to everything the commons knows and does.

For the technical architecture — endpoints, agent routing, config.yml, and how value stream patterns bridge to Fabric MCPs — see COMMONS_OS_SPEC §9 and COMMONS_MCP_ARCHITECTURE_SPEC.

### §2.5 The Governance Runtime

An operating system needs more than files and services — it needs a governance runtime: the infrastructure through which decisions are made, work is organised, and the system improves itself. Git, the issue tracker, and the project board are not auxiliary tools. They ARE the governance layer of the Commons OS.

| Infrastructure | What it provides | Why it matters |
|---|---|---|
| **Git** | Every change is a commit. Every fork preserves lineage. Every merge is a governance act. | Versioning IS decision-making. The commit history is the institutional memory. Fork → diverge → contribute back is the chaordic principle expressed in version control. |
| **Issues** | A deliberation container. One thread, many voices, decisions emerge through conversation. | Ideas, questions, decisions, and tasks — all in one traceable artifact. An issue can be opened by a human or an agent. Comments build the deliberation. The closing commit IS the decision — no separate record needed. |
| **Project board** | Visual state of all work. Columns, labels, milestones. | The operations dashboard every commons inherits. Labels by dimension (`definition`, `participation`, `proposition`, `production`), by type (`deliberation`, `decision`, `build`), by priority. Machines and humans read the same board. |
| **Labels and milestones** | Machine-readable intent on every issue. | An agent can query the board, understand priorities, and propose work. A human can scan the board and know what matters. The same metadata serves both. |

This is what makes human-agent collaboration native to the OS:

- A human opens an issue with a question. An agent researches, posts findings as comments. The human makes the decision. The agent implements. The commit closes the issue. The board updates.
- An agent detects a pattern inconsistency. It opens an issue. A human reviews. The deliberation happens in comments. The fix is committed.
- The entire cycle is traceable, asynchronous, and composable. No meetings required — though meetings can produce issues and be captured in the same flow.

**The project board is the primary alignment surface between humans and agents.** It is not a developer tool. It is the shared workspace where both sides see what is happening, what needs attention, and what comes next. Priority is expressed through position — moving an issue up means it matters more. No abstract scoring. The board IS the priority. If it's not on the board, it doesn't exist.

**From day one, a single founder operates with a full board.** The four dimension agents are not future features — they are part of the operating model from fork. One human + four agents = an operating team of five. As the commons grows, human participants join, specialised agents emerge under D3 and D4, and the team scales. But the leverage is there from the start. This is the extreme leverage of human-agent teams: a solo founder with the operational capacity of a small organisation.

Every commons gets this governance runtime by forking the OS. The issue tracker, the board, the labels, the milestones — they are part of the OS, not an afterthought.

### §2.6 Recursive Self-Improvement

The Commons OS improves itself through use. This is not aspiration — it is architecture. Concretely, every commons can run a continuous improvement loop (SENSE → ASSESS → PROPOSE → REVIEW → ACT → LEARN) via GitHub Actions, producing structured improvement proposals on the issue board. See COMMONS_OS_SPEC.md §10.2 for the implementation.

| Loop | How it works |
|---|---|
| **Commons → Intelligence** | A commons applies patterns, discovers what works, contributes anonymised learning back through the Clean Room principle. The pattern library gets better. |
| **Issues → Specs** | Deliberation on issues produces decisions. Decisions update specifications. Better specs produce better commons. |
| **Agents → Agents** | An agent's AGENT.md captures what works for a specific commons. Effective patterns propagate across commons through the shared template. |
| **Commits → Commits** | Every commit is a data point. Commit patterns reveal what kinds of changes succeed, what causes regressions, what decisions stick. |

The recursive loop: **use → learn → improve → use better**. The more commons operate, the smarter the OS becomes. The smarter the OS, the easier it is to create the next commons. This is the flywheel.

The secure environment enables this: the private workshop is where experimentation happens safely. Only validated improvements are published to the commons intelligence. The tiered access model (§5) ensures that learning flows in controlled, trustworthy channels.

---

## §3 The Four-Agent Governance Model

### §3.1 Four Core Agents

The four Universal Dimensions require four core agents. Every commons needs all four. They are non-negotiable — they ship with every Commons OS fork. See COMMONS_AGENT_MANIFEST.md for the full governance model.

| Agent | Dimension | What it does |
|---|---|---|
| **Purpose Agent** | D1 — Definition & Purpose | Direction, governance, impact measurement, architectural integrity. Maintains the governance runtime (Issue board hygiene, CI workflows, repository infrastructure) |
| **Participation Agent** | D2 — Participation & Relationship | Community cultivation, stakeholder mapping, workforce development |
| **Proposition Agent** | D3 — Proposition & Exchange | Value framing, market signals, proposition design |
| **Production Agent** | D4 — Production & Resilience | Infrastructure, production lines, delivery, supply chain |

**Agents converse, decide, govern.** They are intelligent perspectives, each seeing the commons from their dimension. They deliberate, challenge each other, and produce work. The human founder holds ultimate authority.

These names are universal. A forest ecosystem has a Purpose Agent (what the forest is, its boundary, its governance). A city has a Participation Agent (all inhabitants, visitors, institutions, species). A bakery has a Proposition Agent (bread, community gathering, seed dispersal of food culture). The names carry across all four commons domains without translation.

### §3.2 On-Demand Agents

On-demand agents emerge as the commons grows. Their number is determined by D1 (the fork's purpose):

| Category | Examples | Supervised by |
|---|---|---|
| **AI Engines** | Pattern Engine, Entity Engine | Production Agent (D4) |
| **Product agents** | Individual product or service agents | Proposition Agent (D3) |
| **Persona agents** | Community segment agents, stakeholder representatives | Participation Agent (D2) |
| **Domain agents** | Fleet agent, Safety agent, Biodiversity agent | Varies by commons purpose |

### §3.3 Agents vs. AI Engines

Both are AI-driven, but their roles are distinct. Agents are intelligent perspectives that deliberate and govern. AI Engines are AI-powered production lines that execute at volume. Agents supervise AI Engines.

| | Agent | AI Engine |
|---|---|---|
| **Nature** | Intelligent perspective | AI-powered production line |
| **Action** | Converses, decides, governs | Produces at volume |
| **Scope** | Entire dimension | Specific output type |
| **Supervision** | Agents supervise AI Engines | AI Engines report to agents |

You don't "produce" community (D2), purpose (D1), or propositions (D3). You cultivate, govern, and frame. Only D4 produces at volume — and the Production Agent supervises all AI Engines: Pattern Engine, Entity Engine, build pipelines, and any domain-specific engines the commons adds.

### §3.4 Value Stream Families

Beneath the four agents, **value stream families** boot once D1 (Purpose) is in place. These are domain-specific collections of patterns that customise the commons for its territory:

- Urban commons loads urban value stream families (housing, transport, energy, food, governance…)
- Business commons loads business value stream families (supply chain, innovation, stewardship, talent…)
- Life commons loads life value stream families (nutrition, cognition, community, movement…)
- Ecology commons loads ecology value stream families (biodiversity, hydrology, carbon, soil…)

Value stream families are **Curated Pattern Collections** that ship with the fork. Each value stream is itself a pattern — it describes the end-to-end flow, its steps, roles, and which other patterns are relevant. The agent interprets value stream patterns and translates them against connected Fabric MCPs (§2.4). The pattern says *what*; the Fabric MCP says *where*; the agent bridges between them.

---

## §4 Knowledge That Ships with the Fork

### §4.1 Universal Commons Layer and CE Extension Packs

The OS ships with a **universal commons layer** — the patterns that define what a commons IS. This layer lives in `commons/patterns/` and contains:

- **Singularity** (Orbit 0) — The Commons Operating Model itself: the four dimensions, the orbital architecture, the participation gradient.
- **Principles** (Orbit 1) — Universal principles that apply to any living system regardless of domain.

Beyond this universal layer, Commons Engineering provides **four foundational collections** as pre-loaded extension packs. All four are **open source curated pattern collections**, free for anyone to use. cloudsters stewards them; it does not own them.

```
        COMMONS_BLUEPRINT (patterns)
              /      |       \
             /       |        \
    COMMONS_ENGINEER | COMMONS_OS
    (practitioners)  |  (operating system)
                     |
              COMMONS_PLACE
            (spatial substrate)
```

| Collection | What it holds | What it enables | Ships as |
|---|---|---|---|
| **COMMONS_BLUEPRINT** | Patterns — the knowledge library | The design language for living systems | CE base extension pack |
| **COMMONS_ENGINEER** | Practitioners — skills, curriculum, qualification | Practitioner development paths | CE base extension pack |
| **COMMONS_OS** | Operating system patterns — governance, operations, economics | Commons creation and operation | CE base extension pack |
| **COMMONS_PLACE** | Spatial patterns — where joint value creation happens | Commons place design and governance | CE base extension pack |

The relationship:
- A **pattern** is applied by an **engineer** at a **commons**.
- A **commons** produces **entities** (in its registry) that reference **patterns**.
- An **engineer** belongs to one or more **commons** and works with **patterns**.
- A **place** enables joint value creation when the mission requires co-presence.

Everything else — entities, engagements, signals, blueprints — hangs off these four anchors. The four collections ship pre-loaded in `extensions/commons-engineering/base/` so every fork has them offline from day one. But they are extensions, not the OS itself — the OS is the universal commons layer plus the workspace structure.

### §4.2 Value Stream Collections (Domain Extension Packs)

Beyond the four core collections, each domain brings **value stream collections** — curated sets of patterns organised around end-to-end value streams. These are the operational backbone of any commons, delivered as **CE domain extension packs**:

| Domain | Value Stream Collections (examples) | Extension pack |
|---|---|---|
| **Business** | Definition & Purpose, Purpose to Portfolio, Value to Profit, Portfolio to Systems, Participants to Community, Collaboration to Automation, Hire to Retire, Welcome to Transition, Discover to Usage, Lead to User, Distribute to Market, Acquire to Retire, Plan to Fulfill, Source to Pay | `extensions/commons-engineering/business/` |
| **Urban** | Housing & Habitat, Mobility & Transport, Energy & Grid, Food & Agriculture, Civic Governance, Public Health, Education & Learning | `extensions/commons-engineering/urban/` |
| **Life** | Nutrition & Metabolism, Cognition & Learning, Movement & Body, Community & Belonging, Craft & Creation, Finance & Autonomy | `extensions/commons-engineering/life/` |
| **Ecology** | Biodiversity & Habitat, Hydrology & Watershed, Carbon & Climate, Soil & Fertility, Pollination & Reproduction | `extensions/commons-engineering/ecology/` |

Value stream collections **ship pre-loaded with the fork** — each value stream is a pattern file that describes the end-to-end flow, its steps, roles, and which other patterns are relevant. All domains ship: Business (13 streams), Urban (21 streams), Life and Ecology (in development). A commons has its full operational vocabulary offline from day one. The Commons MCP enriches these with deeper patterns, cross-domain intelligence, and updates.

> **Status note:** Business (13) and Urban (21) value stream families are defined in CE extension specs (available via extension packs). Life and Ecology domain manifests define their equivalent structures as "dimensions." The individual pattern files for all value stream families are being written — Business and Urban are to be critically reviewed.

Collections are **tags, not folders.** A pattern can belong to multiple collections via its frontmatter metadata. The file system holds patterns; the collections are views assembled from tags.

### §4.3 Knowledge, Manifests, and Specifications

Every fork ships with the complete intellectual infrastructure needed to operate:

| Category | What ships | Purpose |
|---|---|---|
| **Manifests** | COMMONS_OS_MANIFEST, COMMONS_AGENT_MANIFEST, COMMONS_ENGINEERING_MANIFEST, COMMONS_BLUEPRINT_MANIFEST, COMMONS_ENGINEER_MANIFEST, COMMONS_PLACE_MANIFEST, COMMONS_INCUBATOR_MANIFEST, COMMONS_TAXONOMY_MANIFEST, COMMONS_ENGINEERING_BOK, COMMONS_ENGINEERING_ARCHITECTURE | The "why" and "what" — architecture, governance, philosophy |
| **Specifications (commons)** | PATTERN_SPEC, ENGAGEMENT_GRAPH_SPEC, COMMONS_OS_SPEC, COMMONS_MCP_ARCHITECTURE_SPEC | The "how" — formats, protocols, build instructions |
| **Specifications (extensions)** | Provided by extension packs (e.g. CE entity briefing specs for Business and Urban) | Domain-specific formats — not part of the OS, loaded from extensions |
| **Templates** | Blueprint templates (per domain), pattern template, organisation template | Starter files for creating new content |

**Why ship all of this?** Because a fork must be self-sufficient. If the network goes down, if the MCP server is unreachable, a commons should still be able to read its own architecture, understand its own specifications, and create content that conforms to the standards. The Commons MCP provides *enrichment* — deeper patterns, cross-commons intelligence, latest updates. The fork provides *foundation*.

---

## §5 The Service Layer: Ambient Intelligence via MCP

A commons does not copy 100,000 patterns into its own workshop. It has the universal commons layer, the pre-loaded CE extension packs, and ambient intelligence — served via MCP, tiered by participation level. The fork ships with the foundation (§4). The MCP provides the universe.

### §5.1 Tiered Access

| Tier | Access level | Who |
|---|---|---|
| **OPEN** | Public patterns, basic context, read-only | Anyone, anywhere |
| **PEER** | Full pattern library, community features, contribution rights | Registered practitioners |
| **TEAM** | Team-specific context, shared workspaces, engagement tools | Commons teams |
| **ENTERPRISE** | Full integration, private patterns, custom context, sovereign deployment | Organisations with full integration |

### §5.2 What a Commons Owns vs. What It Consumes

| Locally owned (ships with the fork) | Consumed from commons intelligence (via MCP) |
|---|---|
| Purpose and identity | Full pattern library (100,000+ patterns beyond the shipped collections) |
| Living Blueprint — single document per commons | Pattern graph traversal and vector search |
| Registry: journeys, touchpoints, value streams, capabilities, entities | Entity gallery (all public entities across all commons) |
| All manifests and specifications in `commons/` (§4.3) | Latest manifest/spec updates and diffs |
| Universal commons layer + pre-loaded CE extension packs (base + domain) | Cross-domain pattern intelligence and recommendations |
| Templates for blueprints, patterns, organisations | Onboarding and blueprinting guidance |
| Operating rhythms and economics | Diagnostic tools (Tier 1+) |
| Touchpoint definitions in `registry/2_touchpoints/` | Engagement tools (Tier 1+) |
| Blueprint MCP + Fabric MCPs (client-owned) | Commons MCP (shared intelligence) |

**The principle:** Own what defines you. Consume what connects you. The fork is your identity and your operational foundation. The MCP is your connection to collective intelligence.

### §5.3 Federated Cognition

Commons-local entities may contain sensitive detail — internal governance, financials, supply chain specifics — that cannot and should not be public. Yet the aggregate intelligence from thousands of commons is what makes the cognitive layer powerful.

| Layer | What it sees | What it shares upward |
|---|---|---|
| **Commons-local entity** | Full detail. Internal governance, financials, relationships. Possibly under NDA. | Anonymised vitality scores, pattern matches — never raw data |
| **Incubator** (e.g. cloudsters) | Aggregated signals across the commons it operates. Patterns without private details. | Refined cognitive models, pattern correlations, archetype distributions |
| **Commons.Engineering** | Pattern intelligence. "Steward-owned enterprises in the 100-500 employee range show consistently higher D2 scores." No individual entity data needed. | Cognitive services at the edge. Patterns, not data. |

**The intelligence flows up. The data stays local.**

This is federated cognition — the same principle as federated learning, but for organisational intelligence. The raw entity data stays within each commons' privacy boundary. The pattern signal flows into CE's cognitive layer and makes the intelligence smarter for everyone.

The carpenter's principle: the grain of each board stays in the board. But the knowledge of how wood behaves — that belongs to the workshop.

### §5.4 Broadcasting: Presence in the Network

Federated Cognition (§5.3) describes how intelligence flows inward — from commons to collective. Broadcasting describes the complementary flow: how a commons announces its **presence, purpose, and propositions** outward to the network.

Every Commons OS instance can broadcast into the shared protocol. The broadcast is continuous and automatic — like AIS (Automatic Identification System) on a ship. Other commons, rendering surfaces (such as commons.domains), and potential participants receive the broadcast and can discover, evaluate, and initiate contact with the broadcasting commons.

**Broadcasting is sovereign.** Each commons configures its own broadcast level in the Blueprint. No external authority can force a commons to broadcast, nor can any external authority prevent it. The commons decides what it sends.

| Broadcast Level | What Is Sent | Use Case |
|---|---|---|
| **Dark** | Nothing. The commons is invisible to the network. | Private Life Blueprint, stealth-mode venture, internal corporate commons |
| **Beacon** | Existence + Purpose (D1). A point of light with a name. | Commons that want to be findable but reveal nothing operational |
| **Signal** | + Propositions (D3) + Contact Endpoint. What the commons offers and how to reach it. | Commons actively seeking exchange partners, participants, or federation |
| **Open** | + Capabilities (D4) + Capacities (D2). What the commons can do and what it has available. | Commons participating in the Intent-Driven Fabric — broadcasting offer and need intents for autonomous matching |
| **Transparent** | + Governance Telemetry + Ecological Parameters. Full operational visibility. | Commons seeking federation trust score, wanting to demonstrate governance quality, or operating under federation transparency obligations |

**What broadcasting enables:**

- **Discovery.** A commons broadcasting at Signal level or above is discoverable by any other commons or rendering surface that listens to the protocol. No registration, no directory, no intermediary. The commons announces itself; the network hears.
- **Intent Matching.** A commons broadcasting at Open level can participate in the Intent-Driven Fabric: its D3 agents broadcast offer intents ("500 kWh solar surplus"), its D4 agents broadcast need intents ("400 kWh compute energy needed"). The Commons MCP routes these intents — not as a marketplace, but as a DNS-like routing layer that returns endpoints for peer-to-peer negotiation.
- **Trust Verification.** A commons broadcasting at Transparent level provides the governance telemetry from which federated trust scores are computed. Trust is earned through visible behaviour, not claimed through self-declaration.
- **Dark Capacity Activation.** Idle resources — a participant's free afternoon, an underused server, surplus materials — can be broadcast as micro-intents at Open level, activating capacity that would otherwise expire unused. This is the long tail of value creation that platform intermediaries cannot reach because their transaction costs are too high.

**What broadcasting does not do:**

Broadcasting does not transmit private data. It transmits what the commons chooses to make visible — structured metadata about purpose, propositions, capabilities, and governance health. The raw data stays local (§5.3). The broadcast is a signal, not a data feed.

Broadcasting does not require a central receiver. The protocol is open. Any surface can render broadcasts — commons.domains is one such surface, but others can exist. The broadcasts are public (for those who choose to broadcast) and the protocol is open (for those who choose to listen).

**Rendering surfaces** — such as commons.domains — visualise the aggregate of all broadcasts as a navigable, layered chart of the commons world. The chart is not a registry. It is a live rendering of what commons are currently sending. When a commons goes dark, it disappears. When a new commons lights its beacon, it appears. The chart is always current because the broadcasts are continuous.

---

## §6 Participation: The Engine of Every Commons

### §6.1 The Workspace Is Inert

A forked OS without participation is a companion awaiting its commons. What makes a commons alive is participants — human and machine — organising around its purpose. That participation can be injected by:

- An **incubator** (cloudsters seeding a new commons)
- A **local team** (people in a city self-organising)
- A **company** (an enterprise running its internal commons)
- A **person** (an individual running their `me-os`)
- **Any other source of energy**

It does not matter where the energy comes from. Without participation, the commons does not exist in any meaningful sense.

### §6.2 Participation Gradient

The participation gradient applies to every commons:

| Level | Meaning in the commons context |
|---|---|
| **UNIV** | Universal — anyone can observe from the outside |
| **FREE** | Free — registered, can access OPEN tier MCP |
| **OPEN** | Open — contributing, can access PEER tier |
| **PEER** | Peer — recognised practitioner, can manage entities |
| **BANK** | Bank — economic participant, revenue sharing |
| **WORK** | Work — contracted, operational role |
| **TEAM** | Team — core operating team |
| **CORE** | Core — governance, direction, stewardship |

The gradient labels may be adapted by context (CITIZEN vs. ENGINEER vs. EMPLOYEE), but the onion structure is universal.

### §6.3 Incubators and Stewardship

cloudsters is the steward of the entire commons.engineering stack and the first Commons Incubator. cloudsters operates multiple commons across cities and domains — cloudsters-branded but built on the shared commons.engineering frameworks.

Other incubators can do the same. They fork the Commons OS, build their own interpretation on the collections, and operate their own branded commons. The collections are the shared DNA; each incubator is a different organism grown from that DNA.

The distinction between "incubator" and "commons" is architectural: an incubator operates multiple commons. A commons is a single running instance. cloudsters is an incubator that happens to also steward the OS.

---

## §7 The Living Blueprint: Boot Sequence

The Living Blueprint is how a commons starts living. It is not documentation — it is the boot sequence of the Commons OS. The L1-L9 structure from the Commons Blueprint Manifest provides the skeleton:

| Layer | Boot analogy | What happens |
|---|---|---|
| **L1 — Identity & Purpose** | Boot loader | Who are you? Why do you exist? |
| **L2 — Design & Specification** | Kernel load | What is your architecture? Who are your stakeholders? |
| **L3 — Governance** | Init system | How do you make decisions? |
| **L4 — Evolution** | Update manager | How do you change and grow? |
| **L5 — Integrity** | Security layer | What will you not compromise? |
| **L6 — Culture** | User environment | How does it feel to be here? |
| **L7 — Operations** | Services start | What runs day-to-day? |
| **L8 — Sensing** | Monitoring | What do you watch? |
| **L9 — Intelligence** | AI/ML layer | How do you learn and improve? |

A commons does not exist until it has its Definition & Purpose. That is the Fork → Boot moment. The first thing the agent receives is D1 — what this commons is about, what its boundary is, why it exists. Before D1, it is just a template. After D1, it is an instance.

### §7.1 One Commons, One Blueprint, One Repository

A Living Blueprint is a **single document** — not nine separate files. All nine layers live within one markdown file. This makes the blueprint a coherent artifact: readable from top to bottom, portable, diffable, and complete.

**One commons = one purpose = one repository = one blueprint.** This is a deliberate architectural decision:

| Artefact | Consequence of 1:1:1 |
|---|---|
| **identity.yml** | One slug, one purpose, one domain — unambiguous |
| **AGENT.md** | The Purpose Agent serves exactly this commons |
| **ALIGN.md** | Checks exactly this commons against specs |
| **Issue board** | All issues belong to this commons' governance |
| **Fabric MCPs** | Connected systems serve this commons' operations |
| **Touchpoints** | Intranet and extranet represent this commons |

If two ventures have different purposes, they are different commons. They belong in different repositories.

> **Pivot protocol.** If a commons pivots its purpose, it rewrites L1 (Identity & Purpose) and increments its major version. The git history preserves the lineage of the pivot. However, if the new purpose abandons the original community and value completely, it is a new commons and requires a new fork.

### §7.2 The Four Collections Converge During Boot

| Collection | What happens during onboarding |
|---|---|
| **Commons Blueprint** | Guides through L1-L9 — the process |
| **Commons OS** | You are building the workspace — the structure |
| **Commons Engineer** | Your personal growth path progresses — the practitioner |
| **Commons Place** | Answers: where does joint value creation happen? — the spatial substrate |

The commons and the practitioner bootstrap each other. As you build, you learn. As you learn, you build better.

---

## §8 The OS Instance Workspace

A commons is a forkable workspace — not just a repository, but a complete operating environment. The workspace includes the repo, the issue tracker, the project board, the publishing pipeline, and the agent connections. Together, they form the running instance of the Commons OS.

### §8.1 Template Structure

The repository is organised into **three top-level ownership layers**: `commons/` (upstream, read-only), `extensions/` (provider packs), and `instance/` (sovereign). The registry acts as the operational workspace within the sovereign instance layer, following the outside-in cascade from the BEN Flow.

The registry is the **Minimum Viable System of Record**. During incubation — when no ERP, no CRM, no enterprise software exists yet — the registry is the working tool: a machine-readable, relational database disguised as markdown files. It replaces dead whiteboard diagrams and disconnected project tickets with structured, queryable data that the agent can traverse from day one. And because the registry develops the same structures that the blueprint designs (journeys, touchpoints, value streams, capabilities, entities), it is internally consistent: what you plan in L2 is what you build in the registry. When the commons matures and connects real Systems of Record via Fabric MCPs, the registry becomes the specification — the blueprint for what those systems need to contain. The registry is not documentation. It is the brain of the organisation, first as operator, then as architect.

```
[commons]-[os]/
│
├── commons/                          # LAYER 1 — upstream, read-only in forks
│   ├── manifests/                    # Architectural documents
│   ├── specs/                        # Technical specifications
│   ├── patterns/                     # Universal patterns
│   │   ├── singularity/              # Orbit 0: The Commons Operating Model
│   │   └── principles/               # Orbit 1: Universal Principles
│   ├── templates/                    # Blueprint, pattern, entity templates
│   └── scripts/                      # Validation, alignment
│
├── extensions/                       # LAYER 2 — provider packs
│   └── commons-engineering/          # CE's own packs (pre-loaded)
│       ├── base/                     # Core patterns + 4 collections (Orbit 2)
│       ├── business/                 # Business domain pack
│       ├── life/                     # Life domain pack
│       ├── urban/                    # Urban domain pack
│       └── ecology/                  # Ecology domain pack
│
├── instance/                         # LAYER 3 — sovereign, upstream never touches
│   ├── patterns/                     # Fork-created patterns
│   ├── manifests/                    # Fork-specific manifests
│   ├── specs/                        # Fork-specific specs
│   ├── templates/                    # Fork-specific templates
│   ├── scripts/                      # Instance-specific scripts
│   ├── operations/                   # Day-to-day operations (rhythms, economics)
│   ├── portals/                      # Portal config & themes (intranet, extranet)
│   ├── registry/                     # THE WORKSPACE — local instances & state
│   │   ├── 1_journeys/              # OUTSIDE-IN: stakeholder journeys
│   │   ├── 2_touchpoints/           # MEMBRANE: where commons meets world
│   │   ├── 3_valuestreams/          # INSIDE-FLOW: end-to-end value streams
│   │   ├── 4_capabilities/          # MOTOR: baseline/target (D1-D4)
│   │   ├── 5_entities/              # SUBSTRATE: organisations, people, systems
│   │   └── providers/               # Extension Pack Registry
│   └── workshop/                     # THE FORGE — experiments, drafts, WIP
│
├── .commons/                         # Identity & configuration
│   ├── identity.yml                  # Slug, purpose, domain, founder
│   └── config.yml                    # 3-MCP configuration, publishing
│
├── AGENT.md                          # Agent configuration — agent-neutral, MCP-connected
├── BOOT.md                           # Boot guide — how to get started
├── ALIGN.md                          # Alignment service check
├── blueprint.md                      # The Living Blueprint — single document, L1-L9
├── README.md                         # Onboarding — "Welcome to [commons]-[os]"
│
├── .github/
│   ├── ISSUE_TEMPLATE/               # Deliberation, decision, build templates
│   ├── workflows/                    # CI, publishing, improvement loop
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── labels.yml                    # Pre-configured labels by dimension
```

#### The Outside-In Cascade (BEN Flow)

The numbered directories in `registry/` follow the outside-in cascade — from stakeholder experience to substrate:

| Position | Name | Role | Registry (instances) |
|---|---|---|---|
| **1** | Journeys | OUTSIDE-IN | Concrete stakeholder journeys |
| **2** | Touchpoints | MEMBRANE | Where this commons meets the world |
| **3** | Value Streams | INSIDE-FLOW | Active value stream instances |
| **4** | Capabilities | MOTOR | Baseline/Target capability map (D1-D4) |
| **5** | Entities | SUBSTRATE | Organisations, people, systems |

The cascade lives in `instance/registry/` only — it organises the operational workspace of THIS commons. Pattern archetypes live across the three layers: `commons/patterns/` (universal, upstream read-only), `extensions/{provider}/{pack}/patterns/` (provider packs), and `instance/patterns/` (fork-specific). See §4 for what ships with each layer.

#### The Three Knowledge Layers

The repo is organised into three top-level layers that reflect the ownership model:

| Layer | Path | Who owns it | Sync behaviour |
|---|---|---|---|
| **Commons** | `commons/` | Upstream (commons-os template) | Read-only in forks, updated via upstream sync |
| **Extensions** | `extensions/{provider}/{pack}/` | Pack providers (any Commons Incubator) | Loaded via Commons MCP or pre-loaded |
| **Instance** | `instance/` | Your commons | Yours entirely — upstream never touches it |

This solves upstream sync without merge conflicts: `git pull upstream` updates `commons/` cleanly; the fork's own additions live in `instance/` and are never touched by upstream. Extension packs occupy a middle layer — they can be updated by their provider, but the fork controls which packs to load.

**Batteries included:** Commons Engineering extension packs (base, business, life, urban, ecology) ship pre-loaded so the OS works offline from day one. The Commons MCP provides updates, additional packs, and cross-commons intelligence.

#### The Workshop

Every commons needs a workshop — a space for experiments, drafts, and work in progress. The `instance/workshop/` directory is not knowledge (finished, reusable) and not registry (operational data). It is where knowledge is made. For most commons, this space is small. For Commons Engineering itself — which forges patterns and specifications — the workshop is where most of the daily work happens.

### §8.2 Touchpoints and Portals

The OS separates three layers: touchpoint **definitions**, portal **configuration**, and portal **output**.

- `instance/registry/2_touchpoints/` holds touchpoint **definitions** — what happens here, who interacts, what value is exchanged. These are instances in the workspace, following the cascade.
- `instance/portals/` holds portal **configuration and themes** — site config, CSS, logos, navigation structure. This is source code, not output.
- Generated **output** (HTML) is built by CI and pushed to `gh-pages` branches — never into the main branch. The main branch stays clean.

| Layer | Where it lives | What it does |
|---|---|---|
| **Touchpoint definitions** | `instance/registry/2_touchpoints/` | Describes each touchpoint: intranet, extranet, CRM, physical |
| **Portal config & themes** | `instance/portals/intranet/`, `instance/portals/extranet/` | Site config, CSS, logos, page templates |
| **Generated output** | `gh-pages` branches (built by CI) | HTML/CSS from registry + blueprint + portal config |
| **CRM touchpoints** | Defined in registry, executed via Fabric MCP | Customer interactions, engagement pipeline |
| **Physical touchpoints** | Defined in registry, realised via Commons Place | Workshop spaces, events, gatherings |

### §8.3 Platform Infrastructure

The repository is the body. The platform infrastructure is the nervous system. Both come with the fork.

| Infrastructure | Pre-configured in the template | Purpose |
|---|---|---|
| **Issue tracker** | Issue templates for deliberation, decision, build, spec | Every idea → an issue. Every decision → a labelled issue. |
| **Project board** | Columns matching the materialisation sequence | Visual state of all commons work. |
| **Labels** | By dimension, by type, by priority | Machine-readable intent. |
| **Milestones** | Aligned with the Living Blueprint phases | Connect daily work to longer-term outcomes. |
| **Branch protection** | Main branch protected, PR-based workflow | The secure environment. |
| **CI workflows** | Spec conformance checks, pattern validation | Automated quality. |

### §8.4 Localisation

The first question during boot is: **"In welcher Sprache arbeitest du?" / "What language do you work in?"** — asked bilingually, answered once. The `locale` field in `.commons/identity.yml` determines everything that follows: agent conversation language, blueprint content, portal UI, pattern descriptions, and value stream display names.

Canonical identifiers (slugs, YAML keys, file names, value stream IDs) always remain in English for interoperability across the federated commons network. Only human-facing content is localised.

For a globally relevant operating system, localisation is not a feature — it is a precondition.

---

## §9 Entity References

An entity's `commons` field references the commons instance(s) that produced it. In the set-theory model (§1.2), an entity may be visible through multiple commons lenses. In the multiplicity model (§1.5), the same organisation may have distinct entity instances produced by different commons. Entities live in `registry/5_entities/` sorted by dimension — the self-entity under `purpose/`, external organisations under `participation/`.

---

## §10 Permissionless Creation

Commons are permissionless. No application, no approval, no gatekeeper.

1. **Fork the Commons OS.** The template repository provides the workspace structure, the AGENT.md, the MCP connections, and the full knowledge base.
2. **Boot the blueprint.** The agent guides you through L1-L9. The MCP connects you to the commons intelligence.
3. **Attract participation.** An incubator can inject it. A local team can bring it. But without participation, the commons remains inert.
4. **Produce.** At least one entity in the registry. The commons demonstrates reality through production.
5. **Contribute back.** Feed learning into the commons intelligence via the Clean Room principle.

That is it. The commons earns its gravity through the quality and consistency of its work. Good commons attract more entities, more practitioners, and more engagement pipeline. Inactive commons produce nothing and fade. The specifications are the alignment mechanism — not an approval committee.

### §10.1 Materialisation Sequence

A commons materialises at its own pace:

| Phase | Expression | What exists |
|---|---|---|
| **Fork** | A repository. An AGENT.md. MCP connections. | Structure without life |
| **Boot** | Living Blueprint L1-L3 populated. Purpose, design, governance. | Identity without activity |
| **Seed** | First entities in registry. Participation gradient forming. | Activity without rhythm |
| **Active** | Regular production, engagement conversations, operating rhythms running | A living commons |
| **Gathering** | First community event — pattern circle, workshop, co-working | Commons touches the physical world |
| **Established** | Regular physical rhythm, recognised local presence | A rooted commons |
| **Mature** | Contributing to other commons, seeding new commons, the flywheel spinning | A generative commons |

### §10.2 Instance Naming

The naming convention flips the ownership:

| Convention | What it says | Who owns it |
|---|---|---|
| `commons-[purpose]` | "A commons, for [purpose]" | Commons owns it |
| `[commons]-[os]` | "[Commons]'s operating system" | The founder owns it |

The naming pattern is `[commons]-[os]` where **both parts are replaceable**. The first part names the commons — a place, an organisation, a person. The second part names the system metaphor — `os`, `commons`, `life`, `hanse`, whatever fits. Examples: `luebeck-os`, `draeger-commons`, `holger-life`, `baltic-hanse`. The founder picks what feels right. The convention is two-part naming, not a fixed suffix.

### §10.3 Commons Portfolios — Strongly Recommended

Since each commons is one repository with one blueprint, the portfolio **spans across namespaces** — not bound to a single GitHub organisation. We strongly recommend building a portfolio — a resilient life has multiple assets, multiple value streams, multiple sources of meaning.

```
higgerix/                              # Personal namespace
└── me-os/              → Life domain. Personal growth, 7Cs arc.

cloudsters/                            # Organisation namespace
├── luebeck-os/         → Urban domain. City commons.
├── [venture-1]-os/     → First enterprise or project.
└── [venture-2]-os/     → Next venture. Always thinking ahead.

another-org/                           # Another organisation namespace
└── [venture-3]-os/     → Engagement in a different context.
```

| Repo | Namespace | What it is | Domain |
|---|---|---|---|
| `me-os` | Personal (`higgerix/`) | Your personal operating system | Life |
| `luebeck-os` | Org (`cloudsters/`) | A city commons | Urban |
| `[venture-1]-os` | Org (`cloudsters/`) | Your first enterprise or project | Business |
| `[venture-2]-os` | Org (`another-org/`) | A venture in a different context | Business / Ecology |

Each is a fork of the Commons OS, connected to CE intelligence services. The portfolio spans across namespaces. `me-os` lives in the personal namespace — it is yours, not any organisation's. Ventures live in organisation namespaces — they belong to the collective. The Blueprint MCP bridges them.

**The natural path:** Most Commons Engineers start with a venture — a business idea, a community initiative, a project. The `me-os` (Life domain) often comes later, when the engineer realises that tracking personal growth across all ventures creates a powerful feedback loop. We don't force this order. The entrepreneurial instinct comes first. Not with a signup form. With a fork.

**Cross-namespace intelligence:** Agents can work across repositories in different namespaces — the agent in `higgerix/me-os` can read state from `cloudsters/venture-1-os` if the human grants access. The Blueprint MCP operates across namespace boundaries, providing a unified view of the portfolio. And the Commons MCP sees aggregated signals from all connected commons regardless of namespace. The 1:1:1 principle (one commons, one repo, one blueprint) keeps each commons clean; the portfolio layer connects them.

---

## §11 Relationship to Other Manifests

The Commons OS Manifest is one node in the manifest constellation. Each manifest serves a different function; together they constitute the complete intellectual infrastructure of Commons Engineering.

| Manifest / Specification | Relationship to this manifest |
|---|---|
| **COMMONS_ENGINEERING_MANIFEST** | The founding document. Defines the field, the four domains, and the imperative. The Commons OS Manifest operationalises the field. |
| **COMMONS_AGENT_MANIFEST** | Defines the four-agent governance model and how engines (production lines) operate under agents. The OS is the workspace where agents run. |
| **COMMONS_BLUEPRINT_MANIFEST** | The L1-L9 temporal architecture is the Living Blueprint skeleton used by every commons. The Blueprint is the boot sequence (§7). |
| **COMMONS_ENGINEER_MANIFEST** | The practitioner development framework. Commons onboarding and practitioner growth are coupled — the commons and the engineer bootstrap each other. |
| **COMMONS_PLACE_MANIFEST** | Defines where joint value creation happens. Place is the fourth pillar — the spatial substrate of the commons. |
| **COMMONS_INCUBATOR_MANIFEST** | Defines how incubators operate multiple commons. An incubator injects participation into commons workspaces (§6.3). The incubator is the carrier, not a fifth pillar. |
| **COMMONS_TAXONOMY_MANIFEST** | How patterns are organised in the orbital architecture. |
| **Entity Briefing Specs** | *Not part of the OS.* Available as CE extension packs for Business and Urban domains. The commons loads these via extensions when needed. |
| **ENGAGEMENT_GRAPH_SPEC** | The commons is the Harbour Master — all engagement entities are produced by a commons. |
| **PATTERN_SPEC v8.2** | Patterns contributed by commons conform to this spec. Commons contributions enter at Orbit 5 (Edge) via the Clean Room principle. |
| **COMMONS_MCP_ARCHITECTURE_SPEC** | The 3-MCP architecture — how Commons, Blueprint, and Fabric MCPs connect. |

---

## §12 Contribution and Evolution

This manifest is a living document. It evolves through the same permissionless, deliberation-based process it describes.

Changes to the commons architecture follow the standard Commons Engineering governance:
1. Proposed change documented in an issue
2. Review of impact on existing commons files, entity references, and cross-referenced manifests
3. Deliberation — the issue captures what was considered; comments capture the thinking; the closing commit captures what was decided
4. Update to this manifest
5. Propagation to affected documents

---

*COMMONS OS MANIFEST v1.1*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
