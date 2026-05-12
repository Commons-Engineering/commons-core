---
id: pat_330c4315ffd745e38240a668
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: conflict-resolution-evolving-rules
  principle: Conflict Evolves Systems
  influence: 0.7
- hub_id: carrying-capacity-ecological-limits
  principle: Every System Has Limits
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
slug: deciding-what-to-fix-or-discard
title: Deciding What to Fix or Discard
aliases: []
summary: Set up clear rules for when damaged materials get repaired versus thrown away, with transparent approval processes
  and complete tracking so you learn from each decision.
context_labels: {}
ontology:
  domain: rework-scrap-management
  cross_domains: []
  search_hints:
    primary_tension: Economic recovery (rework, regrade, salvage) vs. Quality assurance (scrap, containment, risk mitigation)
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
    vitality_reasoning: This pattern creates living value by embedding material disposition decisions within a transparent,
      nested governance structure that learns over time. Rather than ossified rules, it establishes thresholds and authorities
      that adapt as quality data accumulates. Every decision — scrap, rework, regrade, or release-as-is — is visible, traced,
      and fed back into system design. This creates a culture of stewardship over material and a commons of shared quality
      knowledge, where the cost of non-conformance becomes visible across all participants, incentivizing prevention over
      remediation.
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

> Set up clear rules for when damaged materials get repaired versus thrown away, with transparent approval processes and c

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every productive system generates non-conformance: materials that fail to meet specification, defects discovered mid-stream, or edge cases where economic recovery conflicts with quality assurance. Lineage flows through Carrying Capacity (every system has limits beyond which recovery becomes wasteful), Adaptive Management (disposition decisions are experiments, not edicts), Polycentric Organisation (different decision authorities exist at different scales and risk levels), and Visibility (opacity about material fate breeds cost-shifting and hidden defects). The tension between recovery and containment is not a flaw to eliminate but a structural reality to govern justly.

---

### Section 2: Problem

> **The core conflict is Economic recovery (rework, regrade, salvage) vs. Quality assurance (scrap, containment, risk mitigation).**

Non-conforming material creates three competing pressures: the economic incentive to recover value through rework or regrade; the quality imperative to contain risk and prevent defective product reaching customers; and the governance challenge of making these tradeoffs transparent and accountable. Without structured decision-making, rework decisions accumulate hidden costs, quality thresholds drift, and accountability dissolves into finger-pointing. Without distributed authority, bottlenecks form and local context — the engineer who knows the specific defect, the operator who understands the rework cost — goes unheard. Without traceability, decisions cannot be reviewed, patterns cannot be learned, and the system cannot adapt. The commons degrades when material fate becomes invisible or when authority is concentrated in a single approval gate.

---

### Section 3: Solution

Establish a nested, reversible governance structure for material disposition:

**1. Decision Authority Matrix (Subsidiarity):** Define disposition authorities by risk and cost threshold, not by title. Small, low-risk rework (cost <X, defect class <Y) is authorized by the front-line operator/engineer and logged. Medium-risk decisions (cost X-Z, safety implications, regulatory impact) go to a cross-functional review team. High-risk decisions (cost >Z, serialized products, customer-facing safety) require senior authority or customer waiver. Authority scales with local knowledge and reversibility.

**2. Transparent Disposition Record:** Every non-conformance generates a formal record that captures: what failed, why, the decision (scrap/rework/regrade/release-as-is), the authorization level and actor, the cost impact, and the outcome (rework succeeded or failed, customer return rate, etc.). This record is not buried in a database — it is visible to all contributors and periodically reviewed.

**3. Traceability Protocol:** Every reworked or regrade unit is serialized, tracked through its recovery path, re-inspected, and marked with a disposition certificate. If it fails again, the rework decision itself is flagged for review. Over time, this creates feedback: which defect classes are recoverable? Which decisions led to customer returns? This data informs the next iteration of thresholds.

**4. Adaptive Threshold Review Cycle:** Quarterly (or time-sliced to fit your rhythm), the disposition data is reviewed: rework costs by category, success rates, customer returns traced to previously reworked units, and waste trends. If rework costs for defect class X exceed the cost of prevention, the threshold changes. If certain operators consistently make high-quality disposition decisions, authority is delegated to them. If a threshold repeatedly produces hidden failures, it is tightened. The system learns.

**5. Economic and Ecological Accounting:** Every rework decision must account for: direct labor and material cost, lost time (carrying capacity cost), scrap material disposal or recycling, and estimated risk cost (probability × impact of customer failure). Over time, make this accounting visible; it becomes the commons knowledge that incentivizes prevention over recovery.

---

### Section 4: Implementation

Begin by mapping your current non-conformance landscape. Spend a week shadowing the people who encounter damaged materials—production floor, receiving, quality, warehouse. Document what they decide today: What gets reworked? What gets scrapped? On what basis? You'll likely find decisions happening in conversations, emails, intuition. Make that visible first.

Then build your decision framework in layers. Start with the simplest tier: define what low-risk rework looks like in your context. A cosmetic dent in a metal casting? A sewing error fixable in two minutes? Write it down. Make it so obvious that a new hire can decide alone—and log it in a shared system (even a spreadsheet works initially). The logging matters as much as the decision; you're building a memory.

Next, establish your approval gates. Create a simple cross-functional disposition committee (quality, operations, finance, customer-facing role if possible) that meets weekly. Bring actual non-conforming materials to the table when possible—seeing and touching the item changes how people think. Define your medium-risk threshold clearly: "Rework cost >$500 OR involves safety function OR requires process change" goes here. Make decisions in 15 minutes, not 15 meetings.

For high-stakes decisions (regulatory risk, repeated failure modes, high-value items), slow down intentionally. Bring in expertise—maybe a customer rep, maybe someone from another part of the organization. Ask: "Have we seen this failure before? What happened last time?" Build institutional memory, not just case-by-case judgment.

Critically, establish what you *will not* recover. Define your scrap line—the decision that closes the door. "Any defect affecting load-bearing function gets scrapped, period." Clear rules prevent the slow creep of lowered standards. Document the reasoning once; it holds until you deliberately change it.

Implement a simple audit cycle: monthly, pull 10 recent disposition decisions at random. Did they follow the framework? Did the outcomes match predictions? What did we learn? Feed this back into your authority matrix. Rules should evolve as your system learns.

---

### Section 5: Consequences

When this pattern takes root, several things flourish. First, your rework decisions become visible and comparable. You stop losing money to silent, repeated recovery attempts on items that should have been scrapped. Your team develops shared language: "This is a Tier 2 decision," everyone understands the implications. Quality doesn't drift; it becomes a deliberate choice, reviewed monthly. Your front-line people gain autonomy in their lane, which builds engagement and faster decisions. And you capture data—over six months, you'll see patterns: "We rework 40% of receiving defects, and 20% come back again. Time to talk to our suppliers."

The shadow side: if your authority matrix becomes too rigid, you'll create bottlenecks. A genuinely borderline item gets stuck waiting for committee approval. People start workaround decisions again to avoid the process. If you don't resource the weekly disposition review adequately, the backlog of items awaiting decision grows, and production stalls.

There's also a risk of hidden standards. Quality gets tighter in some areas, looser in others, depending on who's on the committee that week. Without consistent criteria and auditing, you can drift toward accepting more defects if cost pressure rises—precisely when you should be most vigilant.

The deepest risk: using the framework as theater. You document everything, but decisions are already made upstream by whoever controls the budget. Transparency without real authority is just bureaucracy.

---

### Section 6: Known Uses

**Toyota Production System (Automotive):** Toyota's andon cord and jidoka (autonomation) embed disposition authority at the line level for obvious defects—stop production, fix it now—while rolling up complex or repeated failures to cross-functional kaizen teams. The framework allows immediate recovery on clear cases and forces systematic thinking on the puzzling ones. This pattern has held for 70 years because it's reversible; a decision can be reopened if new information emerges.

**Patagonia (Apparel Repair & Regrade):** Patagonia's Worn Wear program and repair guarantee pushed disposition decisions outward deliberately. A returned jacket gets evaluated by trained technicians against transparent criteria: Can this be repaired and returned to customer? Regrade and sell as seconds? Recycle for materials? The company publishes its decision rates and learnings, making the tradeoff between recovery value and quality explicit. This turned a cost center into a brand signal.

**Sudanian pottery cooperatives (West Africa):** Women's clay-working circles in Niger and Mali have long practiced tiered disposition: minor firing cracks in functional pots are left as-is; structural cracks on cooking vessels get rejected before firing; defects on decorative ware are sometimes celebrated as signature variation. Decisions are made through apprenticeship and collective judgment, not written rules, but the logic is present: risk tolerance matches use case. The reversibility comes through: a pot deemed "not for cooking" can still be used for grain storage or water cooling.

---

### Section 7: Cognitive Era

AI changes the disposition landscape in three ways. First, defect detection becomes vastly faster and more consistent. Cameras and vision models spot cosmetic or incipient failures humans would miss or misclassify. This shifts the bottleneck from *detection* to *decision*—you'll know about problems faster than you can discuss them.

Second, historical data becomes actionable. Machine learning can now show you: "Items reworked in this category have a 15% return rate; scrap rate drops to 2% if we tighten the spec at step X instead." The pattern's audit cycle accelerates; you get signal from your disposition decisions in weeks instead of months.

But here's the risk: it's tempting to let the algorithm decide. "Run all borderline items through the classifier; it's 94% accurate." This erodes the cross-functional deliberation that keeps your system honest. The algorithm will optimize for what you measured last—cost, rework time—and won't see the reputational hit or the customer who received a marginal item. You need the framework *more* with AI, not less, to keep humans in the consequential decisions.

Distributed intelligence also means your supplier or customer may be part of the disposition decision. A defect that looks like a scrap call to you might be recoverable by your customer's process, or vice versa. The pattern evolves toward shared decision-making across the value chain, with transparent APIs replacing committee meetings. The authority matrix becomes negotiated, not dictated.

---

### Section 8: Vitality

**Signs of life:** Your disposition committee is diverse—operations person actually disagrees with quality person sometimes, and you work through it. People reference past decisions: "Remember the batch from March? We reworked it and regretted it." There's a waiting list of items for decision, which means the system is active, not ceremonial. You've changed your authority matrix in the last 12 months based on what you learned. Front-line staff make disposition calls confidently and log them without being asked. Scrap is trending down because you're catching failures earlier, not because standards loosened. You can articulate why you rework some categories and scrap others—the reasoning is alive, not just documented.

**Signs of decay:** Disposition decisions pile up unsigned. The committee meets but rehashes the same cases without referencing history. Your scrap rate is mysteriously flat or creeping upward even as quality metrics improve (a sign decisions are happening off-books). People avoid the process—items sit in a holding area because no one wants to make the call. You can't explain to a new hire why one defect gets reworked and a similar one doesn't. The rule book hasn't changed in three years, even though your process has. Your audit reveals that 30% of decisions violate the framework, but nobody acts on it.

**Diagnostic question:** *If I asked three different people on your team to make a disposition call on the same defective item, how much would their answers vary? If the answer is "a lot," your framework is either unclear or not trusted. If the answer is "they'd all decide the same way, and they could explain why," your pattern is vital.*
