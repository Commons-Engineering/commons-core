---
id: pat_aba89b90c34e42f38c7d5c09
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: time-sliced-iterative-planning
  principle: Plan in Short Cycles
  influence: 0.7
- hub_id: incentives-self-interest
  principle: Channel Self-Interest
  influence: 0.7
- hub_id: carrying-capacity-ecological-limits
  principle: Every System Has Limits
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
slug: making-and-keeping-service-promises
title: Making and Keeping Service Promises
aliases: []
summary: Set clear response time commitments with your users, track how well you're doing, and adjust when things change.
  It builds trust.
context_labels: {}
ontology:
  domain: service-level-agreements-response-times
  cross_domains: []
  search_hints:
    primary_tension: 'Commitment certainty vs. adaptive capacity: how to make binding time promises in systems where load,
      complexity, and conditions evolve unpredictably'
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
    vitality_reasoning: This pattern creates living value by treating SLAs not as rigid contracts to be gamed, but as reciprocal
      covenants that strengthen trust when they are transparent, proportional, and openly recalibrated. Rather than incentivizing
      heroic overcommitment (which breeds burnout and hidden failure), it anchors response times in observable capacity, makes
      performance visible to all parties, ties consequences to fairness rather than punishment, and creates feedback loops
      that allow commitments to evolve as the system learns. This transforms SLAs from brittle control mechanisms into adaptive
      governance structures that reflect real stewardship of shared work.
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

> Set clear response time commitments with your users, track how well you're doing, and adjust when things change. It buil

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

In living systems that serve other agents—whether IT helpdesks, facilities teams, sales, security, or vendor relationships—time-based commitments create a form of covenant: "we promise to acknowledge, investigate, or resolve your need within X hours." These commitments matter because they shape trust, enable planning, and distribute workload fairly. But they are also fragile. Load spikes, scope creep, unforeseen complexity, and changes in team capacity make fixed timelines dangerous. The Commons Engineer must design SLAs as adaptive stewardship practices, not enforcement mechanisms. Lineage: Reciprocity Sustains Cooperation (SLAs are fairness frameworks), Governance as Experiment (all commitments need monitoring and recalibration), Time-Sliced Planning (short review cycles for capacity adjustment), Carrying Capacity (acknowledging that teams have sustainable limits), and Visibility (transparent tracking builds collective accountability).

---

### Section 2: Problem

> **The core conflict is Commitment certainty vs. adaptive capacity: how to make binding time promises in systems where load, complexity, and conditions evolve unpredictably.**

The inherited SLA model treats time commitments as contracts to be met or breached, with penalties for failure. This creates perverse incentives: teams overcommit to win contracts, hide problems to avoid penalties, and burn out chasing unrealistic targets. When actual capacity is invisible—when load varies wildly, when severity estimates are wrong, when team members leave—rigid SLAs become either fiction (promises routinely missed) or trauma (unsustainable pressure). The inverse problem: undercommitting or missing every deadline erodes trust. The core tension is temporal: how can we promise to respond in predictable time when the system is complex and conditions change? And how can we tie consequences to fairness rather than mere punishment, so that SLA breaches drive learning, not blame?

---

### Section 3: Solution

Steward response commitments through five integrated practices:

**1. Baseline from Visible Capacity, Not Aspiration.** Define initial response time targets by mapping actual team capacity—hours available per week, typical incident volume, severity distribution—and calculating realistic throughput. Publish these calculations transparently. The baseline is alive only when it reflects current reality; don't hide understaffing behind optimistic promises.

**2. Differentiate by Severity & Consequence.** Create response time tiers that reflect the actual harm of delay: critical issues that affect production/safety get fastest response; routine requests get longer horizons. This acknowledges that not all time is equal. Tie response time to severity, not to arbitrary "gold/silver/bronze" packages.

**3. Track & Surface Real Performance.** Implement continuous monitoring that makes actual response time visible—not just to managers, but to the team and to requesters. Show trend data: are we meeting targets? When? Why do some requests slip? This visibility is a commons act; it prevents hidden failure and creates shared accountability.

**4. Use Proportional Consequences, Not Penalties.** When SLAs are missed, use consequences that serve learning: service credits that acknowledge harm to the customer, escalation triggers that summon help early, and post-mortem reviews that surface systemic problems (overload, unclear specs, unexpected complexity). Avoid pure financial penalties, which incentivize gaming. Make the consequence proportional to the impact of the delay.

**5. Recalibrate on a Predictable Cycle.** Review SLA targets quarterly or after significant load changes. If targets are consistently missed, adjust them downward—or add capacity. If consistently beaten, stabilize (don't ratchet up). If circumstances change (team growth, new tools, policy shift), revise openly. Treat every SLA as an experiment: hypothesis about what's achievable, tested against reality, updated as conditions evolve.

**6. Bind SLAs to Reciprocal Obligation.** SLAs are two-way covenants. If you promise a 4-hour response, the requester owes clarity and completeness in the initial request. If a supplier commits to uptime, the customer commits to proper usage. Make reciprocal obligations explicit, so that shared responsibility is visible.

The result: SLAs become stewardship instruments—frameworks that bind teams to fair promise-keeping while remaining adaptive, transparent, and grounded in real capacity rather than heroic fiction.

---

### Section 4: Implementation

Begin by measuring what you actually do before you promise anything. Spend 4–6 weeks logging every service request: arrival time, type, complexity, who handled it, how long it took, what happened next. You're not hunting for heroes or villains. You're building a map of your system's actual shape. From this baseline, calculate: How many requests arrive per week? What's the distribution by severity? How long does a typical response actually take? How much spare capacity exists in your team's week?

Now write your first commitment. Keep it honest. If you're currently responding to critical issues in 2 hours on average, don't promise 30 minutes. Promise 2 hours. If you're drowning and averaging 6 hours, say so. Publish these numbers alongside the data that generated them. This transparency signals respect—you're not hiding behind marketing language.

Establish a feedback loop. Create a simple dashboard (a shared spreadsheet works fine) that tracks every incoming request and when you touched it. Update it weekly. Include response time, resolution time, and severity level. This isn't about blame. It's about seeing patterns: Does Tuesday always spike? Do security requests take longer than updates? Are certain team members absorbing disproportionate load?

Quarterly, gather the team. Review the data together. Ask: Are we meeting our commitments? Where are we slipping? What changed since last quarter—staffing, tooling, scope creep? Use this conversation to adjust either your commitments or your capacity. If load grew 30%, you can't pretend your 2-hour promise still holds. Renegotiate it. If you added a person, you may genuinely improve. Say so.

Create buffers deliberately. Don't fill every hour of your week with promised work. Reserve 15–20% capacity for the unexpected: the person who quits, the severity spike, the tool that breaks. This breathing room keeps you human and keeps your promises survivable.

When you miss a commitment, own it. Document what happened. Tell your users. Adjust your next forecast. Repeat commitments aren't failures if you learn from them.

### Section 5: Consequences

When response commitments are stewarded well, several forms of life flourish. Users gain predictability. They can plan their own work, escalate intelligently, and stop assuming worst-case timelines. Your team gains clarity about priorities and permission to say no to work that doesn't fit the available capacity. You stop surprising your leadership with outages that "came from nowhere"—because you've been watching the load curve. Burnout diminishes because people aren't chasing impossible targets. And trust accumulates, because you've been honest about what you can and cannot do.

The risks emerge quietly if attention lapses. Commitments can calcify into dogma, disconnected from changing reality. You promise a response time that made sense two years ago, before your user base tripled or your team shrank. The dashboard becomes theater—updated but not read, not acted upon. Team members learn to game the metrics: they log a response without actually investigating, just to mark the box. Load spikes get hidden rather than escalated, because admitting you're struggling feels like failure. And gradually, users stop trusting your numbers because they've learned you don't adjust them when conditions change.

The hardest consequence is burnout that arrives slowly and looks like dedication. A team that commits to impossible timelines and nearly meets them appears high-performing for a while. But the cost compounds: overtime, shortcuts, institutional knowledge walking out the door when people leave. By the time you realize the system is failing, the damage is already baked in.

### Section 6: Known Uses

**Microsoft Support and Azure SLAs:** Microsoft publishes detailed response and resolution commitments for Azure services, tiered by severity and support plan. They update these annually based on actual performance data and changing infrastructure capabilities. When they miss SLAs, they publish post-mortem analysis. This transparency—admitting what they got wrong and how they'll improve—has become a model for enterprise credibility.

**Kenya Red Cross Emergency Response:** The organization committed to responding to disaster reports within 4 hours in urban areas, 8 hours in rural zones. Rather than enforce this top-down, they mapped actual team capacity per region, hired and trained to match commitment to resources, and built in seasonal buffers (rainy season needs different staffing). When they couldn't meet a commitment in a particular area, they communicated early and retrained volunteers. The commitment became a tool for fair resource allocation, not a stick for punishment.

**Shopify Merchant Support:** Shopify publishes response time commitments by ticket priority and support tier, and shares aggregate performance metrics monthly. Crucially, they adjust commitments when load patterns shift—for instance, during holiday selling seasons, they transparently lower response targets and over-staff to maintain quality. This honesty (rather than pretending capacity doesn't matter) strengthens merchant relationships even when response times are slower.

### Section 7: Cognitive Era

In systems augmented by AI and distributed decision-making, service commitments become more fluid and more visible simultaneously. AI-powered triage can pre-classify severity more accurately, meaning your response time commitments can be more granular—different promises for different kinds of work. Automation can handle routine responses instantly, freeing human judgment for genuine complexity.

But this also creates new traps. You can promise faster response times because an algorithm handles the first touch, then forget that the algorithm sometimes fails silently. You can distribute work across a network of agents (human and machine) and lose visibility into total capacity. A commitment that made sense when one team owned it becomes murky when responsibility is shared.

The antidote is the same: make your actual system visible. Track not just human response times but the full journey—including time spent in queues, in automation loops, waiting for human review. Publish commitments that account for the full pipeline, human and machine. Update them as your AI models change. When distributed agents share work, maintain a shared ledger of capacity and load. The commitment becomes less about a single team's promise and more about a network's coordinated covenant.

### Section 8: Vitality

A healthy service commitment system shows these signs of life: Your dashboard is read and discussed regularly. Team members can articulate why the commitment is what it is, pointing to actual data. Users reference your promises without cynicism—they trust them. When you miss a commitment, the response is analytical, not defensive. You adjust your next commitment or your capacity based on what you learned. Conversations about workload and feasibility happen before crises hit.

Signs of decay arrive subtly. The dashboard goes stale. Commitments haven't changed in two years, even though your context has shifted dramatically. Team members use phrases like "well, that's just what we tell them we do" or "nobody really expects us to meet that." When you miss a commitment, the response is explanation and blame-shifting rather than learning. Load spikes surprise leadership. Turnover accelerates among people who care about quality. Users ask "is that promise even real?" and keep their expectations low.

The diagnostic question: If you pulled up your data right now—actual response times from the last three months—would your current commitments need adjustment? If the answer is "I'm not sure" or "I haven't checked," that's a sign you've lost the thread. Recommit to the weekly review. It's not overhead. It's the practice that keeps the whole system alive.
