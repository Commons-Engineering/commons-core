---
id: pat_989a77a7d4e24ecc82229c5d
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: carrying-capacity-ecological-limits
  principle: Every System Has Limits
  influence: 0.7
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: truth-seeking-transparency
  principle: Truth-Seeking Sustains Systems
  influence: 0.7
- hub_id: feedback-adaptive-cycles
  principle: Information Shapes Systems
  influence: 0.7
slug: knowing-who-you-depend-on
title: Knowing Who You Depend On
aliases: []
summary: Keep track of the people and companies your business relies on, understand what could go wrong, and stay ready when
  things change.
context_labels: {}
ontology:
  domain: third-party-risk-management
  cross_domains: []
  search_hints:
    primary_tension: Autonomy vs. Interdependence — the need to act independently while depending on relationships beyond
      your control
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
    vitality_reasoning: This pattern treats dependencies not as static risks to be mitigated but as living relationships that
      must be continuously observed, evaluated, and adapted. By making dependency flows visible across the system, distributing
      stewardship responsibility, and renewing commitments at regular intervals, the pattern creates the conditions for both
      resilience (redundancy where critical, monitoring where uncertain) and evolution (relationships adjust as context shifts).
      The system becomes alive because it breathes—it absorbs feedback, learns when counterparties change, and rebalances
      before collapse. It remains just because evaluation criteria are transparent and applied equitably. It endures because
      stewardship is distributed, not concentrated in any single actor or assessment moment.
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

> Keep track of the people and companies your business relies on, understand what could go wrong, and stay ready when thin

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every viable system depends on relationships beyond its direct control: suppliers, platforms, partners, financiers, infrastructure providers, regulators. In healthy ecosystems, these interdependencies are transparent and actively cultivated. In fragile ones, they remain invisible until failure strikes. The tension between autonomy and interdependence is not resolved by isolation (which is impossible) but by systematic stewardship—making dependencies visible, evaluating them honestly, and renewing them deliberately. This pattern draws on principles of ecological resilience (carrying capacity, feedback loops), governance (polycentric stewardship, subsidiarity), and truth-seeking (transparency as a commons act). It applies across all sectors: supply chains, technology ecosystems, nonprofit missions, platform economies, and regulatory compliance.

---

### Section 2: Problem

> **The core conflict is Autonomy vs. Interdependence — the need to act independently while depending on relationships beyond your control.**

Organizations face three interlocking tensions: First, dependencies accumulate invisibly—new vendors, API integrations, platform dependencies, single points of failure—until crisis reveals what was always fragile. Second, evaluation happens once (at intake) and then atrophies; vendors change, conditions shift, risks evolve, but the assessment becomes stale. Third, risk ownership scatters—no one person holds the full map; stewardship fragments across procurement, IT, compliance, and operations; weak signals of degradation never surface. The result: critical relationships fail unexpectedly, mission-critical systems collapse due to invisible dependencies, compliance gaps emerge post-facto, and organizations discover they are far more dependent than they believed—often too late. The problem is not the existence of dependencies (unavoidable in any complex system) but the absence of living visibility and distributed stewardship.

---

### Section 3: Solution

Implement Dependency Stewardship as a continuous cycle with four integrated mechanisms:

**1. Living Inventory & Mapping (Visibility)** — Create a transparent, distributed map of all critical dependencies: third-party vendors, technology integrations, supply chain partners, regulatory requirements, single-person dependencies. This is not a static document but a living register updated whenever relationships change. Use a taxonomy that makes dependencies queryable: by domain (technology, supply, partners, compliance), by criticality (mission-essential, important, nice-to-have), by type (financial, operational, reputational, human rights). Distribute ownership—each team maintains its own dependencies; a central steward reconciles and surfaces systemic patterns.

**2. Periodic Assessment & Renewal (Evaluation)** — At defined intervals (quarterly, annually, or after material change), conduct structured reassessment of each critical dependency using transparent criteria: financial stability, regulatory compliance, alignment with your values, redundancy status, concentration risk, change velocity, data security posture, human rights due diligence (where applicable). Use a scoring system that is simple enough to be explained, not hidden in opaque algorithms. Document the reasoning, not just the score. Most importantly: treat assessment as a renewal ceremony, not a punitive audit. If a relationship survives review, strengthen it; if it is degrading, either invest in remediation or reduce dependency.

**3. Distributed Stewardship & Escalation (Governance)** — Assign stewardship of each dependency to the team closest to it (subsidiary principle). Stewards conduct ongoing monitoring—tracking public signals of vendor health, noticing when contracts renew, flagging when performance degrades. They have authority to act within bounds (renegotiate terms, seek alternatives, invest in redundancy). Escalation pathways exist for dependencies that cross team boundaries or pose systemic risk. A commons-level steward maintains the master map and convenes cross-functional reviews when concentration risk emerges.

**4. Threshold-Based Response (Adaptation)** — Define carrying capacity thresholds for each dependency class: How many vendors in critical roles? How much of your revenue concentrated with one partner? How much technical debt from legacy integrations? When a threshold is approached, initiate deliberate reduction or redundancy-building. When a vendor shows signals of degradation (missed SLAs, regulatory action, leadership turnover), shift from renewal to contingency planning. This transforms reactive crisis response into proactive adaptation.

The pattern embodies commons logic: it makes interdependence (the lived reality) the design centre, not a problem to deny. It distributes stewardship so that intelligence is not concentrated in one person. It cycles continuously so that the system learns from feedback. It is just because evaluation criteria are transparent and applied equitably. It endures because dependency management becomes a ongoing practice, not a one-time intake event.

---

### Section 4: Implementation

Start by convening the people who actually know your dependencies—operations, engineering, procurement, finance. Not in a meeting to "create a document," but in a series of conversations to externalize what's already in their heads. Ask: *Who do we need to function tomorrow? What breaks our business if they disappear?*

Build your living inventory with three layers. First, the **obvious tier**: your major vendors, cloud providers, payment processors. Second, the **hidden tier**: the freelancer who maintains a critical tool, the legacy system only one person understands, the regulatory inspector who renews your license. Third, the **conditional tier**: dependencies that matter only under specific scenarios (a weather event, a policy change, a market shift).

Use a shared spreadsheet, a wiki, or a tool designed for this—the format matters less than accessibility. What matters is that any team member can add, update, or flag a dependency. Assign a **dependency steward** (or small rotating team) to tend this map monthly, not annually. This person's job is to ask: What's changed? What did we discover? What can we reduce?

For each critical dependency, ask three diagnostic questions:
- **What exactly could go wrong?** Not vague catastrophizing, but specific failure modes.
- **How would we know?** What signals tell us there's trouble?
- **What would we do?** Have a rough sketch of a contingency—not a 200-page plan, but a decision about whether you'd switch vendors, build an alternative, or accept the risk.

Then cultivate relationships deliberately. Meet your key vendors twice a year, not just when problems emerge. Share enough of your strategy that they understand why they matter. Ask them: *What could we do to make you more stable? What are you worried about?* Some of your best risk intelligence comes from the people closest to the edges of your system.

Finally, rotate people through dependency awareness. Have an engineer sit in on a procurement call. Have a finance person spend time understanding your platform risks. This cross-pollination keeps knowledge from calcifying in silos.

### Section 5: Consequences

When this pattern flourishes, several things become visible. First, **crises narrow**—you're not learning about problems from a complete blackout, but from early signals. You've built relationships that include difficult conversations. Second, **you make better trade-offs**—you consciously choose which dependencies to accept and which to reduce, rather than accepting them by default. Third, **antifragility emerges**—your system doesn't just survive disruption, it uses turbulence to find better suppliers, technologies, or ways of working.

Teams also become more resilient. When people understand the full ecology of their organization, they collaborate better. Engineers design for resilience instead of assuming infrastructure is eternal. Procurement thinks about redundancy instead of just cost. Finance understands why paying slightly more for stability sometimes matters.

But risks emerge if this pattern calcifies into bureaucracy. A dependency inventory can become a checkbox—updated once a year, ignored otherwise, owned by no one. Worse, over-mapping can paralyze: organizations can become so aware of risk that they move cautiously into immobility, unable to accept any dependency at all.

There's also a relational risk. If you start relationships by auditing vendors for failure modes, you can damage trust. The pattern works only when interdependence is framed as mutual—we depend on you, you depend on us, we're in this together.

Finally, there's the risk of false reassurance. You can map every dependency and still miss the one that matters most—often because it's so embedded you don't see it as a dependency anymore.

### Section 6: Known Uses

**Patagonia's Supply Chain Transparency** — The outdoor clothing company maintains one of the most detailed dependency maps in retail: every fabric mill, every dye supplier, every factory. They publish this information and invite audits because transparency reduces risk. When a supplier fails, they already understand alternatives. When regulations shift, they move fast. The living inventory isn't security theater; it's essential to their brand promise and operational resilience.

**Bugyo (Traditional Japanese Administrators)** — In feudal Japan, regional administrators maintained detailed maps of who depended on whom—not as surveillance, but as social infrastructure. They tracked artisans, merchants, farmers, and their relationships because disruption in one affected many others. When drought threatened, they understood which villages to support first. The pattern was oral and relational, not written, but the principle was identical: know your interdependencies or watch the system fracture.

**Early-Stage Startups at Y Combinator** — The most resilient startups maintain a simple "key person/vendor" document and review it quarterly. They ask: If our CTO left tomorrow, what breaks? If our cloud provider raised prices 10x, what do we do? If our largest customer represented 40% of revenue, how do we diversify? They don't ruminate on these questions—they sketch answers, build relationships with alternatives, and reduce exposure where it matters most. Teams that do this rarely get surprised by disruption.

### Section 7: Cognitive Era

Artificial intelligence and distributed systems are reshaping this pattern in subtle ways. On one hand, **AI tools can now map dependencies at scale**—crawling code repositories, analyzing contracts, tracing data flows—revealing hidden connections humans would miss. A tool can tell you that your business depends on a deprecated Python library used by exactly three services, each critical to different parts of your operation.

On the other hand, **dependency chains are becoming less legible, not more**. When you use a third-party LLM API, you're not just depending on that vendor—you're implicitly depending on their data sources, their fine-tuning decisions, their model vulnerabilities, their energy infrastructure. The map gets exponentially more complex.

This creates new forms of stewardship. Rather than maintaining a static list, organizations need **dynamic dependency monitoring**: automated systems that constantly test whether key integrations still work, whether APIs have changed, whether vendors are still reliable. You need to build the pattern into your infrastructure, not just your governance.

There's also a shift toward **diversification as a design principle**. With AI, it becomes feasible to maintain lightweight redundancy—multiple LLM providers, multiple data sources, multiple ways of doing critical work. The pattern shifts from "know and manage your one dependency" to "architect for resilience by building in options."

And there's an emerging tension: as systems become more distributed and opaque, the relational aspect of the pattern becomes even more important. You can't fully understand a complex system through mapping alone—you need conversations with the people inside it.

### Section 8: Vitality

A healthy dependency stewardship pattern shows these signs of life: **Conversations happen casually.** Someone notices a new vendor and drops it into the shared map without ceremony. A team member mentions a single-person knowledge bottleneck and someone starts documenting it. These aren't compliance tasks; they're natural responses.

**Surprises are smaller.** When a vendor changes terms or a key person leaves, you're adjusting, not panicking. You've thought about it before.

**Relationships feel mutual.** Your vendors mention they're going through changes, and they tell you early because they trust you'll understand and collaborate rather than hunt for alternatives immediately.

Signs of decay emerge when: **The inventory becomes stale.** It was updated once, six months ago. New hires don't know it exists. When a real problem hits, people don't check the map because they've learned it's not trustworthy.

**Responsibility diffuses.** Everyone is supposed to maintain it; no one does. It's "the business continuity person's job," not everyone's job.

**Relationships sour.** Vendors feel audited rather than partnered with. You're checking boxes on vendor scorecards instead of asking how you can support each other.

**The pattern becomes rigid.** New dependencies are treated as problems to be minimized rather than relationships to be managed. Innovation slows because every new integration is seen as additional risk rather than new capacity.

**Diagnostic question**: *If a key vendor announced they were shutting down tomorrow, would your response be "Oh no, we saw this coming" or "We had no idea"?* The answer tells you whether you're truly knowing your dependencies or just performing awareness.
