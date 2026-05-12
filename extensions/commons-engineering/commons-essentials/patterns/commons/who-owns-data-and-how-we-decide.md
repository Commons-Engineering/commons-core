---
id: pat_58f091a9598b4f178f23e334
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: conflict-resolution-evolving-rules
  principle: Conflict Evolves Systems
  influence: 0.7
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
slug: who-owns-data-and-how-we-decide
title: Who Owns Data and How We Decide
aliases: []
summary: A system where communities share control over data through clear roles, transparent rules, and fair processes that
  adapt when conflicts arise.
context_labels: {}
ontology:
  domain: data-governance-operating-system
  cross_domains: []
  search_hints:
    primary_tension: Centralized control vs. distributed stewardship — how to ensure data integrity and compliance without
      concentration of authority or loss of local knowledge
    vector_keywords: []
  commons_assessment:
    stakeholder_architecture: 4
    value_creation: 4
    resilience: 4
    ownership: 4
    autonomy: 4
    composability: 4
    fractal_value: 4
    vitality: 4.0
    vitality_reasoning: This pattern creates living value because it treats data stewardship not as compliance burden but
      as cultivated practice. By distributing authority across nested stewards while maintaining feedback loops, transparency,
      and periodic recalibration, the system remains adaptive to regulatory change, organizational evolution, and emerging
      risks. Stewards develop ownership and accountability (reciprocity), conflicts surface early through escalation (truth-seeking),
      and the system learns through attestation cycles and maturity assessment. The commonwealth lives because it circulates
      — data definitions evolve, roles clarify, policies adapt — rather than ossifying into static rules.
    overall_score: 4.0
lifecycle:
  status: draft
  version: '0.1'
  confidence: 2
relationships:
  manifests_as: []
  enables: []
  requires: []
  alternatives: []
  complementary: []
  tools: []
graph_garden:
  last_pruned: null
  entities: []
  communities: []
  inferred_links: []
contributors:
- higgerix
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: commons.engineering by cloudsters, https://cloudsters.net
---

> A system where communities share control over data through clear roles, transparent rules, and fair processes that adapt

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Most organizations treat data governance as a compliance layer imposed from above: committees establish policies, audits verify adherence, violations trigger penalties. This creates the illusion of control while producing the opposite — stewards lack authority, policies lag behind reality, business units route around governance, and conflicts smoulder unresolved. The 28 O1 principles suggest a different path: governance emerges through distributed stewardship, structured feedback, and nested decision-making. Data is not a resource to control but a commons to cultivate. Stewardship — the caring practice of tending something on behalf of others — replaces management. This pattern synthesizes domain ownership, role clarity, escalation pathways, and adaptive cycles into a coherent stewardship circulation.

---

### Section 2: Problem

> **The core conflict is Centralized control vs. distributed stewardship — how to ensure data integrity and compliance without concentration of authority or loss of local knowledge.**

Three forces collide: (1) Regulatory and operational pressure for data consistency, security, and compliance pushes toward centralization and rigid policy. (2) Distributed domain knowledge — only local stewards understand their data's real lineage, quality, and use — resists top-down rules. (3) Conflict over data definitions, ownership, and usage rights emerges naturally but lacks structured resolution, creating silent silos or paralysis. Committees form but lack teeth. Policies are written but not lived. Stewards burn out enforcing rules they didn't shape. Audit cycles reveal drift but produce no learning. The result: governance becomes theater — visible procedures that don't actually govern. Regulatory risk persists. Data quality deteriorates. Trust erodes.

---

### Section 3: Solution

Establish Stewardship Circulation — a polycentric governance structure organized around three nested cycles, each with explicit feedback and escalation: **1. Domain Stewardship Cycle (Local)**: Assign clear data stewardship ownership for each major domain (customer, finance, operations, risk) with written accountability matrices specifying roles (owner, custodian, steward, user) and decision rights. Stewards are not administrators but cultivators — responsible for data definition clarity, lineage documentation, quality thresholds, and local conflict resolution. Stewards meet monthly to surface issues, refine definitions, and flag escalations. **2. Governance Circulation Cycle (Regional)**: A cross-functional governance committee (steering + tactical working groups) meets on fixed cadence (monthly or quarterly) to resolve escalated conflicts, review policy drift, approve significant changes, and recalibrate standards based on emerging risks or regulatory shifts. Committee membership must include business, compliance, IT, and audit to embed multiple perspectives. This is where reciprocity is maintained — each steward contributes voice, each function has accountability. **3. Attestation & Adaptive Cycle (Organizational)**: Annual or semi-annual attestation by stewards that their domains meet governance, quality, and compliance standards, coupled with maturity assessment against a transparent framework (e.g., DAMA). Results surface systemic gaps, inform training investments, and trigger policy reviews. This cycle is alive — not punitive audit but generative learning. **Supporting infrastructure**: (a) Data Glossary — a living shared definition registry maintained by stewards, not IT, with version control and usage notes. (b) Escalation Pathways — clear, documented routes for conflicts unresolved at steward level to move to committee, then to steering, with defined timelines. (c) Visibility & Communication — all governance decisions, policy changes, and audit findings published transparently; stewards expected to communicate rationale to their teams. (d) Incident & Exception Tracking — governance violations and quality failures logged and analyzed monthly to reveal patterns and trigger rule evolution, not blame. **The mechanism**: Stewardship Circulation works because it inverts the typical flow. Instead of rules flowing down and compliance flowing up, stewardship circulates — stewards shape standards, committees synthesize steward input and escalate conflicts, learning flows back to refresh both policy and practice. Each cycle is short enough (monthly steward meetings, quarterly committee reviews, annual attestations) to catch drift early and adapt before compliance risk hardens. Authority is subsidiarity-first: stewards decide within domain until conflict or regulatory change forces escalation. This preserves local knowledge while ensuring coherence.

---

### Section 4: Implementation

Begin by mapping your data landscape through the eyes of those who live in it daily. Convene domain stewards — the people who actually create, maintain, and depend on the data — and document what they already know: where data lives, who touches it, what breaks when definitions shift, which conflicts resurface repeatedly. This isn't a project kickoff; it's recognition of stewardship already happening, often invisibly.

Establish three decision-making forums, each with clear membership and escalation paths:

**Domain Stewardship Circles** meet monthly within each data domain (customer master data, financial records, operational metrics). Members include the domain owner, custodians from systems that produce or consume the data, and representatives from compliance and risk. These circles review data quality issues, propose definition changes, settle disputes about access, and maintain a living data contract — a document that captures agreements about what the data means, who can change it, and how conflicts get resolved. Their authority is bounded: they manage their domain, period. They escalate structural conflicts upward.

**Governance Council** convenes quarterly, drawing one representative from each Domain Circle plus cross-functional peers (chief data officer, chief compliance officer, business leads). This body doesn't re-litigate domain decisions; it identifies patterns across domains, surfaces systemic conflicts, and adapts governance rules based on what the circles learned. Did three domains independently decide to change how they define "customer"? That's a Council signal. It proposes, doesn't impose.

**Escalation Protocol** handles rare, genuine deadlocks: when a domain circle can't resolve a conflict because it affects other domains, or when regulatory change forces a choice with broad consequences. A small arbitration panel (typically the CDO, a domain owner from an unaffected area, and one external advisor) hears the dispute, applies explicit criteria (compliance must-haves, operational feasibility, stakeholder impact), and decides within two weeks. Decisions are binding but documented with full reasoning — the next circle learns why.

Cultivate this structure through small acts: a shared data dictionary that circles maintain together. A monthly newsletter where each circle shares what they resolved. A rotating "steward exchange" where someone from one circle observes another. Over time, stewardship becomes visible, contestable, and genuinely shared.

### Section 5: Consequences

When stewardship circulation takes root, three things flourish: Data definitions become stable *because* the people who use them helped shape them. Business velocity increases because decisions move to the people with the knowledge to make them — no waiting for central governance to weigh in on every change. Conflicts surface earlier and resolve faster because there's a recognized channel and an expectation that disagreement is normal.

Trust deepens. People stop seeing governance as constraint and start seeing it as clarity — agreed-upon rules that protect *them* too, not just the organization.

But stewardship circulation creates new risks if neglected:

**Authority diffusion.** Without clear decision rights and escalation protocols, circles drift into turf warfare or defer everything upward, replicating the very centralization you tried to escape. The antidote: written decision authorities and real consequences for not using them.

**Hidden non-compliance.** If domain circles have too much autonomy, regulatory requirements can silently erode. A finance domain might define "revenue" in ways that pass local scrutiny but breach tax code. Vigilance: compliance and audit must attend circles and speak early, not audit after the fact.

**Steering without authority.** Circles become talk shops if they can't actually change things. People stop showing up. The work requires that decisions made in circles actually stick — that systems get updated, policies change, conflicts get resolved. Without visible impact, stewardship withers.

**Latency in crisis.** Polycentric decision-making works well for steady-state evolution but can stall when speed matters — a data breach, a regulatory surprise, a major acquisition. Build an emergency protocol: certain decisions (security incidents, regulatory mandates) bypass circles and go straight to a standing crisis team, with rapid feedback loops back to circles once the crisis passes.

### Section 6: Known Uses

**The Dutch water boards** (Waterschappen) have governed shared water resources through nested circles for over 800 years. Local districts manage water quality and drainage for their territories, escalating basin-wide issues to regional assemblies, which coordinate with national bodies. Each level has explicit authority; conflict resolution is embedded. Data about water quality, usage, and infrastructure lives at the level closest to the actual watershed, with transparent protocols for aggregating upward. This pattern has survived market pressure, climate change, and political upheaval because stewardship stays rooted in local knowledge.

**Mondragon Corporation** (Spain's worker cooperative) uses domain councils for different business units (manufacturing, finance, retail) that operate with genuine autonomy yet coordinate through a federation structure. Data governance follows the same logic: each cooperative maintains its own records, stewards its own definitions, but participates in regular councils where shared standards are debated and conflicts resolved. No central data office imposes; instead, stewards negotiate. This has allowed Mondragon to scale across dozens of ventures without losing local responsiveness.

**The Linux Kernel project** governs code through subsystem maintainers who own specific domains (filesystems, networking, security), each with their own decision authority and escalation to Linus Torvalds and the core leadership team only when subsystems conflict. Data (bug reports, patches, commit history) lives distributed across these domains. Stewardship is deep and contested — maintainers actively debate changes — but transparent and federated. The pattern has enabled the largest collaborative software project in history to remain coherent without central control.

### Section 7: Cognitive Era

As AI and distributed intelligence reshape data work, stewardship circulation gains new texture and fragility.

Distributed AI systems — models running in edge locations, making decisions without central oversight — will multiply the number of "stewards" beyond what traditional governance can absorb. An ML model in operations that acts on customer data is now a stakeholder; so is the model auditor, the retraining engineer, the feedback loop that corrects it. Stewardship circles will need to expand to include machine actors and the humans who steward them, not as metaphor but as actual governance participants.

Simultaneously, AI can accelerate stewardship circulation's best moves. Intelligent data catalogs can surface conflicts automatically ("These three domains define 'customer' differently — here's the impact"). Audit trails become traceable, decisions documented and queryable. Circles can make faster, better-informed choices. But this automation can also erode stewardship — if AI suggests a "consensus" definition, do circles still deliberate, or do they defer to the model?

The deeper shift: as data flows faster and decision-making becomes more distributed, stewardship can't be a periodic role anymore. It becomes continuous. Stewards will need real-time feedback loops and algorithmic support to stay aware of how their data moves through systems, how it's transformed by AI, where it's misused. Circles won't meet monthly; they'll collaborate asynchronously through intelligent platforms that flag conflicts, highlight unintended consequences, and propose resolutions.

The risk: stewardship at scale becomes invisible again, buried in algorithms. The antidote is intentional — building governance structures that force human deliberation and trace accountability even as systems accelerate.

### Section 8: Vitality

**Signs of life:**

- Stewards can articulate the decision right they hold and cite the protocol that backs it. ("I own customer definitions in our domain; if it affects three other domains, it escalates to Council.")
- When conflicts arise, people know where to take them. A data dispute doesn't fester; it moves to the relevant circle, gets resolved or escalated within a known timeframe.
- Circles are genuinely contested. People disagree in them, and those disagreements are visible — documented, reasoned, often compromised. If circles are too smooth, stewardship is fake.
- New stewards are onboarded by existing ones; the practice is cumulative, passed down. Knowledge of "how we actually decide" lives in people, not just documents.
- The data dictionary, decision log, and escalation history are alive — recently updated, actively consulted, shaped by circles.

**Signs of decay:**

- Stewardship circles become theater. They meet, discuss, then a central office overrules them. Trust collapses.
- Authority concentrates anyway. Decisions that should move to circles get held at the top "to move faster." The pattern regresses.
- Escalations languish. Conflicts reach the Council or arbitration panel but decisions take months. People stop escalating; circles lose authority.
- Stewards are rotated too quickly or selected by hierarchy, not expertise. The pattern requires people who know their domain deeply.
- Documentation falls away. Without visible decision logs and data contracts, the structure becomes invisible, and the next crisis bypasses it.

**Diagnostic question:**

*When a significant data conflict arises today, can you trace it to a specific steward, circle, and resolution protocol? Or does it disappear into email, meetings without clear ownership, and decisions made somewhere you can't see?*

If you can't trace it, stewardship circulation isn't real yet. Start there.
