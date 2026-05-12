# COMMONS AGENT MANIFEST
*The Board of a Commons — Four Agents, One Purpose*

**Version:** 1.0
**Status:** Living Document
**Companion:** COMMONS_OS_MANIFEST.md, COMMONS_BLUEPRINT_MANIFEST.md

---

## Preamble

Every commons has a board. Not a legal board — a governance structure that ensures the commons achieves its purpose in balance for all stakeholders.

The board consists of **four core agents** — one per Universal Dimension — and a **human founder** (or founding team) who holds the ultimate governance authority. The agents are intelligent perspectives, each seeing the commons from their dimension. They converse, deliberate, challenge each other, and produce work. The human decides.

This manifest defines the agent architecture, their value stream families, and the relationship between agents and engines.

---

## §1 The Four Core Agents

Every Commons OS fork ships with exactly four core agents. They are non-negotiable — the four Universal Dimensions require four perspectives.

| Agent | Dimension | Perspective | Human board equivalent |
|---|---|---|---|
| **Purpose Agent** | D1 — Definition & Purpose | Why do we exist? Are we achieving the impact we set out for? What must change? | CEO — direction, architecture, governance |
| **Participation Agent** | D2 — Participation & Relationship | Who participates? How do we build the machine? How do we grow and sustain the workforce? | CHRO/CPO — everyone who participates |
| **Proposition Agent** | D3 — Proposition & Exchange | What do we offer to ALL stakeholders? How is value distributed? | CFO — what we offer, what flows back |
| **Production Agent** | D4 — Production & Resilience | How do we build and deliver? What infrastructure sustains us? | CTO/CIO — systems, production, supply |

### §1.1 The Purpose Agent Governs

The Purpose Agent sits at the centre of the value creation model. It supervises all other agents and value streams. Its responsibilities:

- **Define:** Establish purpose, boundary, and identity of the commons
- **Govern:** Ensure all four dimensions operate in balance for all stakeholders
- **Monitor:** Check whether the commons achieves its intended impact
- **Correct:** Take measures when things don't go to plan
- **Arbitrate:** When agents disagree, the Purpose Agent holds the purpose lens

The Purpose Agent does not override the other agents — it ensures they serve the shared purpose. The human founder retains ultimate authority. The Purpose Agent is the founder's closest collaborator, not their replacement.

### §1.2 Agents Converse

The four agents are peers. They see from different dimensions and genuinely need each other. The inter-agent dialogue is not a feature — it IS the governance:

- The Proposition Agent discovers that a new market needs a capability the Production Agent hasn't built yet → deliberation
- The Participation Agent identifies workforce gaps that threaten the Production Agent's delivery → escalation to Purpose Agent
- The Production Agent detects resilience risks that affect the Proposition Agent's promises → course correction
- The Purpose Agent detects strategic drift and convenes all agents for realignment

This inter-agent deliberation happens through the Governance Runtime (issues, comments, commits). Every deliberation is traceable. Every decision is a commit.

**Vision:** Within months, this deliberation will happen through orchestrated agent-to-agent dialogue — automatically surfacing tensions, proposing resolutions, and escalating to the human board when needed.

---

## §2 Value Stream Families per Agent

Each agent governs a set of value stream families. These are **universal defaults for the Business domain** — other domains (Life, Urban, Ecology) will have their own families loaded from Curated Pattern Collections.

### §2.1 Purpose Agent — D1 Definition & Purpose

| Value Stream | Scope |
|---|---|
| **Definition & Purpose** | The foundational work — why does this commons exist, what is its boundary, who does it serve |
| **Purpose to Portfolio** | Translating purpose into a portfolio of strategic initiatives, investments, and bets |
| **Value to Profit** | Ensuring the value created translates into sustainable economics for all stakeholders |
| **Portfolio to System** | Translating portfolio decisions into systems of systems — architecture, technology, integration |

The Purpose Agent holds the full strategic arc: from defining why the commons exists, through portfolio governance, to ensuring the architecture delivers.

### §2.2 Participation Agent — D2 Participation & Relationship

| Value Stream | Scope |
|---|---|
| **Participants to Community** | Building community across ALL stakeholders — human, machine, ecological. Not just customers — everyone. |
| **Collaboration to Automation** | The recursive self-improvement goal: manual collaboration → assisted → automated. Every process matures along this arc. |
| **Hire to Retire** | The full lifecycle of human AND machine workforce — recruitment, deployment, development, succession, retirement |
| **Welcome to Transition** | Onboarding, upskilling, and offboarding of workforce — the human experience of joining, growing, and leaving |

D2 is relational, not mechanical. Community emerges from good participation design — it is not manufactured.

### §2.3 Proposition Agent — D3 Proposition & Exchange

| Value Stream | Scope |
|---|---|
| **Discover to Usage** | The full arc from discovering a need to delivering a product/service into active usage. Modern "Idea to Market" — outside-in, user-centric. |
| **Lead to User** | The entire process of creating and keeping recurring users — from first contact to loyal relationship. Not "Demand to Revenue" — the focus is on the user, not the money. |
| **Distribute to Market** | Building and maintaining the entire go-to-market — channels, partners, platforms, touchpoints |

D3 is about what the commons offers to ALL stakeholders and how that exchange flows. The language is deliberately user-centric, not revenue-centric.

### §2.4 Production Agent — D4 Production & Resilience

| Value Stream | Scope |
|---|---|
| **Acquire to Retire** | Providing infrastructure — the full lifecycle of assets, systems, and platforms from acquisition to decommission |
| **Plan to Fulfill** | Production and fulfilment of finished and semi-finished products and services — the operational core |
| **Source to Pay** | The right material at the right time at the right place — procurement, supply chain, material flow, payment |

D4 is where things get built and delivered. This is the only dimension that runs **engines** as production lines.

---

## §3 Agents vs. Engines

This is a deliberate architectural distinction.

| Concept | What it is | What it does | Which dimensions |
|---|---|---|---|
| **Agent** | An intelligent perspective | Converses, decides, asks questions, governs | All four (D1–D4) |
| **Engine** | A production line | Processes inputs into outputs at volume | D4 primarily; other agents may invoke engines through D4 |

### §3.1 Why the Distinction Matters

- **You don't "produce" community.** The Participation Agent (D2) cultivates relationships. Community emerges. No engine needed.
- **You don't "produce" purpose.** The Purpose Agent (D1) defines, governs, monitors, corrects. No engine needed.
- **You don't "produce" propositions.** The Proposition Agent (D3) frames what's offered and how exchange works. No engine needed.
- **You DO produce things.** The Production Agent (D4) runs engines: pattern engines, lighthouse engines, build pipelines, infrastructure provisioning.

Engines are tools that the Production Agent supervises. When a commons needs to produce patterns at scale, D4 runs a Pattern Engine. When it needs to produce lighthouses at scale, D4 runs a Lighthouse Engine. When volume demands dedicated context, D4 can spin up specialised engine instances — but the Production Agent remains the supervisor.

### §3.2 Pragmatic Concession

In practice, high-volume production lines (like pattern enrichment or lighthouse generation) may need their own persistent context to avoid overwhelming the Production Agent's context window. In such cases:

- The **Production Agent remains the supervisor**
- Specialised engines run as **sub-agents with their own context**
- The Production Agent delegates, monitors, and integrates their outputs
- This is implementation detail, not architectural deviation

The same applies if any other agent needs heavy computational support — the agent delegates to the Production Agent, who runs the appropriate engine.

### §3.3 CE's Own Dogfood

Commons.Engineering, applying this architecture to itself:

| Agent | What CE's agent does | Engines it runs (via D4) |
|---|---|---|
| **Purpose Agent** | Oversees all engines, guards CE's mission, governs architecture | — |
| **Participation Agent** | Cultivates the commons engineering community | — |
| **Proposition Agent** | Positions lighthouses, collections, Commons OS to stakeholders | — |
| **Production Agent** | Supervises all production | Pattern Engine, Lighthouse Engine, Build pipelines |

The old naming (Pattern Engine, Lighthouse Engine, Community Engine, Context Engine, Hub Engine) was pre-architecture — five peer engines. The new architecture: **four peer agents, with engines as production lines under D4.**

---

## §4 On-Demand Agents

Beyond the four core agents, a commons may need additional agents for specific purposes:

| Type | What it is | Example |
|---|---|---|
| **Engine agents** | Persistent sub-agents running production lines under D4 | Pattern Engine agent, Lighthouse Engine agent |
| **Product agents** | Specialised agents for specific products or services | A "Commons OS" agent that manages fork lifecycle |
| **Persona agents** | Agents embodying a specific stakeholder perspective | A "Passenger Agent" for BVG, a "Patient Agent" for a hospital |

On-demand agents are never peers to the four core agents. They operate **under the umbrella** of the relevant core agent:

- Engine agents → under Production Agent (D4)
- Product agents → under Proposition Agent (D3)
- Persona agents → under Participation Agent (D2)

The Purpose Agent (D1) may also have on-demand agents for specific governance tasks (compliance agent, impact measurement agent), but these are rare.

---

## §5 The Board in Practice

The commons board operates through the Governance Runtime (§2.5 of the COMMONS_OS_MANIFEST):

| Activity | How it happens |
|---|---|
| **Strategic alignment** | Purpose Agent convenes quarterly review. All agents report from their dimension. |
| **Operational coordination** | Agents communicate through issues and the project board. Labels by dimension. |
| **Conflict resolution** | When agents disagree, the Purpose Agent frames the tension. The human founder decides. |
| **Impact monitoring** | Purpose Agent tracks impact metrics. Proposition Agent tracks value flow. Production Agent tracks delivery. Participation Agent tracks engagement. |
| **Course correction** | When impact deviates from plan, Purpose Agent proposes adjustments. All agents deliberate. Human founder approves. |

The human founder is always part of the board. The agents advise, execute, and deliberate — but the human holds the final say. This is not a technocracy. It is a partnership.

---

## §6 Value Stream Family Renames (from this session)

The following renames reflect the shift to outside-in, user-centric language:

| Previous name | New name | Reason |
|---|---|---|
| Agents to Community | **Participants to Community** | Warmth, non-human inclusion (C1 of naming constraints) |
| Idea to Market | **Discover to Usage** | Outside-in: starts with discovery, ends with usage — not with "market" |
| Demand to Revenue | **Lead to User** | Focus on the user relationship, not the revenue extraction |

These renames must propagate to:
- `_specifications/LIGHTHOUSE_BUSINESS_SPEC.md` §6, §4
- All existing business lighthouse files
- Any scripts that reference these value stream names

---

## §7 Lineage

This agent architecture descends from:

- **MHP Business Engineering Department** (2016–2025, ~200 briefings) — the Purpose Spiral, value stream families, capability mapping, the outside-in methodology
- **BEN Ecosystem Framework** — the Business Architecture Timeslice, the five-phase methodology (Verstehen → Use Cases → Value Streams → Domain Model → Sourcing)
- **DPO Golden Ratio Framework** — shared rhythm, shared language, shared portfolio, shared strengths at differentiated speeds
- **BVG 3-year blueprint** — proof that the methodology works at enterprise scale; proof that it needs AI to be accessible to all organisations
- **APQC Process Classification Framework** — lineage for value stream families, but modeled as value streams not processes

The ambition: what took 3 years and a consulting team on brown paper should be accessible to any organisation through an AI-enabled Commons OS.

---

## §8 Open Questions

| # | Question | Status |
|---|---|---|
| 1 | Life and Ecology value stream families — what are they? | Open — needs domain-specific deliberation |
| 2 | Urban value stream families — does the current 21-stream model need the same rethink? | Open |
| 3 | Should the Purpose Agent also have "on-demand" governance engines? | Open — probably not at this stage |
| 4 | How do persona agents get loaded? From lighthouse stakeholder maps? | Open — interesting for BVG-style commons |
| 5 | Inter-agent dialogue protocol — what format? Issues? Structured messages? | Open — needs design |

---

*COMMONS AGENT MANIFEST v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
