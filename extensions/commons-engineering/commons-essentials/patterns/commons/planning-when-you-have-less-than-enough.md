---
id: pat_1379017d642a4d268b9f0f95
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: carrying-capacity-ecological-limits
  principle: Every System Has Limits
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: time-sliced-iterative-planning
  principle: Plan in Short Cycles
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: economic-constraint-scarcity-opportunity-cost
  principle: Every Choice Forecloses Others
  influence: 0.7
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
slug: planning-when-you-have-less-than-enough
title: Planning When You Have Less Than Enough
aliases: []
summary: Figure out what work actually fits with the people and time you have, then adjust as you learn what really happens
  versus what you predicted.
context_labels: {}
ontology:
  domain: portfolio-resource-allocation-planning
  cross_domains: []
  search_hints:
    primary_tension: Demand growth vs. Capacity limits
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
    vitality_reasoning: This pattern creates living adaptive value by treating capacity stewardship as a continuous ecological
      process, not a static allocation. It embodies the commons definition through systematic forecasting (repeatable structure),
      feedback-driven reallocation (alive and adapting), transparent governance (shared decision-making), fair distribution
      of constraint burden (just), and iterative cycles that preserve institutional knowledge and relationship durability
      (built to last). By making scarcity visible and distributing the work of trade-off decisions across appropriate levels,
      it prevents the system from oscillating between feast-famine cycles and builds collective ownership of throughput limits.
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

> Figure out what work actually fits with the people and time you have, then adjust as you learn what really happens versu

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

In organisations stewarding shared resources across competing initiatives — whether product portfolios, capital projects, or service delivery — capacity is the ultimate commons. It is finite, ecological, and alive: it fluctuates with demand seasonality, skill availability, infrastructure readiness, and external shocks. When capacity governance is opaque or reactive, the system exhibits pathology: repeated overcommitment, burnout, missed deadlines, and the false scarcity that emerges when actual capacity is unknown. This pattern draws from Carrying Capacity (every system has a sustainable load threshold), Time-Sliced Planning (adaptation requires short review cycles), Polycentric Organisation (decisions distributed across nested levels), and Subsidiarity (lowest competent level decides).

---

### Section 2: Problem

> **The core conflict is Demand growth vs. Capacity limits.**

Organisations face three interlocking tensions: First, forecasting: demand is rarely predictable, yet allocation decisions require forward visibility into both pipeline demand and available capacity. Second, contention: when multiple initiatives compete for scarce resources (specialist skills, infrastructure, vendor slots, time), conflicts over allocation reflect deeper disagreement about priorities and fairness. Third, adaptation: capacity itself changes (people leave, skills depreciate, infrastructure breaks, seasonality shifts), yet allocation frameworks often remain static for years, accumulating misalignment between committed plans and lived reality. Without explicit carrying capacity stewardship, organisations default to either rationing (authoritarian freeze) or overcommitment (hoping to catch up later), both of which erode trust and suppress truth-seeking about actual constraints.

---

### Section 3: Solution

Implement a nested capacity stewardship cycle operating at three scales: portfolio, cluster (team or service line), and project. The cycle comprises four repeating phases within a time-sliced horizon (quarterly or seasonal): (1) Forecast: each initiative owner and resource steward surfaces demand signals and capacity availability for the upcoming period, using structured templates that make assumptions explicit. Build a visible backlog of unmet demand and unused capacity. (2) Reconcile: gather the distributed decision-makers (initiative sponsors, resource stewards, cross-functional representatives) at the appropriate subsidiarity level to surface the carrying capacity gap. This is not a negotiation to hide scarcity but a truth-seeking forum to acknowledge it. Name which constraints bind throughput: people, skills, infrastructure, time, vendor availability. (3) Allocate: using transparent criteria agreed in advance (strategic priority, fairness rules, risk distribution), distribute both capacity and unmet demand. Make explicit which initiatives are deferred, which are reduced, which proceed. Record the rationale. Reserve buffer capacity (~20-30%) for emergencies and learning. (4) Execute and Observe: monitor actual throughput, resource utilisation, and forecast accuracy. Track variance between plan and reality. Celebrate accurate forecasting; investigate large surprises. Feed observations back into next cycle's forecast. At the start of each cycle, review the previous cycle's hypotheses: did we identify the true binding constraint? Did the allocation framework prove fair? Did buffer capacity prove adequate? Adjust rules and decision criteria based on evidence. The pattern's power lies in treating each cycle as an adaptive experiment and in distributing both the work and the governance of scarcity across the organisation rather than concentrating it in a single authority. This transforms capacity constraint from a source of resentment into a commons stewardship practice.

---

### Section 4: Implementation

Start by making visible what is actually happening. Before you forecast, map current work in flight: list every active initiative, the people it needs, and how much time it actually consumes—not the estimate, but the reality you can observe. Do this for two to three past periods. You'll find gaps between what was planned and what was real. That gap is your starting point.

Next, agree on your capacity unit. This might be full-time equivalents, story points, days per person per month, or something else—but make it concrete and consistent. Then, for each cluster (team, service line, or domain), explicitly state: How much capacity do we have? What's committed to ongoing work? What's available for new initiatives? Be honest about context-switching costs. If people are pulled across five projects, their actual capacity per project is lower than the hours suggest.

Now run a simple forecast cycle each quarter:

**Week 1-2:** Initiative owners submit demand—what work needs doing, when, and how many people-hours. Resource stewards surface capacity—who's available, for how long, at what skill level. Use templates that force specific assumptions visible. ("We need 3 engineers for 16 weeks" is better than "we need resources.")

**Week 3:** Bring them together in a room or structured conversation. Where does demand exceed capacity? Where is there slack? Which initiatives are most critical to your strategy? Adjust: defer lower-priority work, find ways to reduce scope, cross-train to increase capacity, or explicitly accept overallocation and name the risk.

**Week 4:** Communicate the plan simply. Who works on what, for how long, starting when. Include the assumptions that could break it: "This assumes Sarah stays healthy" or "This plan works if we don't get a major incident."

Then—and this is critical—**track what actually happens**. Every month, compare plan to reality. Did the initiative take the time we thought? Did someone leave or change roles? Did a dependency slip? Update the forecast. Let the pattern adapt. The forecast is not a contract; it's a living model of what you believe about the work ahead.

### Section 5: Consequences

When this pattern takes root, several things flourish. Teams know what they're responsible for and can focus. Conflicts over resources become explicit conversations about strategy rather than hidden tugs-of-war. Leaders can see tradeoffs clearly: adding this initiative means deferring that one. People are less burned out because work is bounded and predictable, even when it's ambitious. You catch overcommitment before it becomes a crisis.

But the pattern carries real risks if not tended. First, **forecast brittleness**: if you treat the quarterly plan as gospel and refuse to adapt, it becomes useless the moment reality diverges—which it always does. The antidote is to stay curious about the gap between plan and actual, and to re-forecast frequently enough that surprises stay small.

Second, **invisible exclusion**: capacity stewardship can privilege visible, quantifiable work over maintenance, mentoring, and learning. If you only track coded hours, you'll starve the work that keeps the system healthy. Build those into your capacity model explicitly.

Third, **politicking**: if resource allocation becomes zero-sum and high-stakes, people will optimize for gaming the forecast rather than honesty. Guard against this by making the conversation collaborative—"how do we solve for all of this?" rather than "whose work gets cut?"—and by rotating who leads prioritization.

Finally, **brittleness to shock**: a plan that assumes stable capacity breaks when someone departs unexpectedly or demand spikes. The remedy is slack—deliberately underallocating, keeping some capacity loose for adaptation and learning.

### Section 6: Known Uses

**Spotify's Squad Model (Music Streaming):** Organized engineers into cross-functional squads, each with explicit capacity commitments and a quarterly planning cycle. Squads forecasted what features they could ship given team size, dependencies, and on-call load. Reality checks happened monthly. This allowed them to scale from 50 to 500+ engineers while keeping teams autonomous and preventing constant thrashing.

**Ushahidi (Crisis Mapping, Kenya):** A small nonprofit routing volunteer mappers and developers across multiple disaster response initiatives. They ran a simple quarterly capacity census: how many active volunteers, with what skills, in which regions? Which crisis needed what? They matched explicitly and rotated people to prevent burnout and build resilience. This model let them scale impact without growing the core team unsustainably.

**UK National Health Service (Primary Care Networks):** During COVID-19, clinical networks forecasted staffing, vaccine supply, and appointment capacity on a rolling two-week basis. They made assumptions visible ("assuming 85% staff availability" rather than hiding absences). When reality diverged, they updated quickly. This lower-stakes version of capacity planning prevented some of the chaos seen elsewhere and created slack for surge capacity.

### Section 7: Cognitive Era

Distributed intelligence and AI change the texture of this pattern without eliminating it. Tools can now surface demand signals automatically—monitoring pipeline velocity, customer support tickets, and infrastructure metrics to forecast with less manual input. Models can simulate what-if scenarios: "If we defer feature X, what's the ripple effect across roadmap and revenue?" That's powerful.

But the core tension remains human: **What do we actually believe is possible, and who decides?** AI can help forecast; it cannot resolve the political question of which work matters most. It can surface hidden capacity—someone learning a new skill, a process that could be automated—but recognizing and cultivating that capacity still requires human judgment and care.

The pattern actually becomes more important as systems grow more complex. Humans need cognitive scaffolding to hold the full picture of what's possible. Capacity stewardship cycles become a ritual space where distributed teams align on shared reality before it fragments. And the discipline of tracking forecast vs. actual becomes more valuable: it's how you stay grounded when algorithmic recommendations pull in many directions.

One risk: over-automation of the forecast can hide the conversations that matter. If allocation becomes purely algorithmic, based on historical patterns and AI recommendations, you lose the chance to question whether the current pattern serves you well.

### Section 8: Vitality

**Signs of a healthy pattern:**

- Leaders can name, without hesitation, how much available capacity they have and what it's committed to. They sound certain but not rigid.
- When new work arrives, the first question is "What do we defer or reduce?" not "How do we squeeze it in?"
- Forecasts are wrong in interesting ways. You learn something each time you compare plan to reality and update accordingly.
- People say: "I know what I'm working on for the next quarter, and I have some breathing room." Not: "I'm overloaded" or "Nobody knows what's happening."
- Capacity conversations include non-billable, non-coded work: mentoring, learning, maintenance, slack.

**Signs of decay:**

- The plan exists but no one updates it. It's become paperwork.
- When reality diverges from forecast, the response is blame ("They didn't try hard enough") rather than curiosity ("What did we misunderstand about this work?").
- Allocation feels political or opaque. People don't know why their initiative was deferred.
- Capacity is only measured in one dimension: code commits, billable hours, tickets closed. Invisible work is invisible.
- The plan is treated as a contract: "You committed to this, so you must deliver," even when circumstances have changed fundamentally.

**A diagnostic question:** If you had to reallocate 20% of capacity tomorrow, could you do it in a day? Or would it take weeks of negotiation, because no one is clear on what's actually committed versus aspirational? The speed and ease of that reallocation tells you whether your capacity stewardship is alive or calcified.
