---
id: pat_5a5ff363e2854351a4b2b02a
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: feedback-adaptive-cycles
  principle: Information Shapes Systems
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: incentives-self-interest
  principle: Channel Self-Interest
  influence: 0.7
- hub_id: time-sliced-iterative-planning
  principle: Plan in Short Cycles
  influence: 0.7
slug: getting-problems-to-the-right-person
title: Getting Problems to the Right Person
aliases: []
summary: Set clear rules for when, how, and to whom problems get escalated so they're solved by someone who can actually fix
  them, not stuck waiting or lost in the shuffle.
context_labels: {}
ontology:
  domain: incident-issue-escalation-framework
  cross_domains: []
  search_hints:
    primary_tension: Speed of resolution vs. appropriate decision authority; individual empowerment vs. systemic coherence
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
    vitality_reasoning: A living escalation commons thrives when each participant knows their sphere of authority, when thresholds
      are visible rather than mysterious, and when feedback about decision outcomes flows back to improve categorization.
      The pattern is 'alive' because severity classifications and routing rules adapt as the system learns which triggers
      predict genuine risk. It is 'shared' because frontline staff and managers co-author decision rules; it is 'just' because
      escalation criteria are transparent and applied consistently; and it 'lasts' because the mechanism becomes a cultural
      norm, self-reinforcing without constant enforcement.
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

> Set clear rules for when, how, and to whom problems get escalated so they're solved by someone who can actually fix them

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every organization with multiple decision-makers and time-sensitive issues faces the same ecological pressure: issues must reach the person with authority to resolve them, but if every issue escalates, authority figures become bottlenecks and the system clogs. The escalation commons exists at the intersection of trust in frontline judgment and the reality that some situations exceed individual competence or risk tolerance. This pattern draws on subsidiarity (decisions made at the lowest capable level) and polycentric governance (authority distributed across nested centres). It also acknowledges incentives: frontline staff want to resolve issues without escalation overhead; supervisors want visibility into simmering problems before they explode; executives want to sleep at night knowing critical risks are being surfaced. Escalation pathways are the circulatory system through which information and authority flow together.

---

### Section 2: Problem

> **The core conflict is Speed of resolution vs. appropriate decision authority; individual empowerment vs. systemic coherence.**

Escalation fails in three modes: (1) Clarity failure — staff do not know when to escalate, so issues drift unresolved or escalate prematurely, wasting senior attention. (2) Speed failure — escalation routes exist but lack time targets, so issues bounce between levels or stall waiting for busy people. (3) Learning failure — each escalation is treated as a discrete event; patterns in what escalates are not fed back to improve initial categorization, so the same issues surface repeatedly. The tension is acute: frontline staff have local knowledge but limited authority; senior staff have authority but no real-time visibility of emerging risks. Systems that ignore this tension collapse into either chaos (no escalation clarity, information loss) or sclerosis (all decisions pushed upward, frontline paralysis).

---

### Section 3: Solution

The escalation commons is built on four interlocking mechanisms:

**1. Severity Taxonomy & Trigger Criteria (The Gate):** Define a small set of objective, observable signals that categorize issues by impact and risk — not by staff feeling but by measurable consequence (e.g., customer impact, revenue risk, regulatory exposure, systemic failure). Examples: service down (escalate immediately); single customer unhappy but contained (escalate if unresolved in 4 hours); data integrity concern (escalate within 1 hour). The taxonomy is public, versioned, and revisable based on what you learn. This gives frontline staff a clear decision rule without requiring them to second-guess authority.

**2. Role-Based Authority Matrix (Who Decides):** For each severity tier, explicitly name the role that has decision authority and the constraint they operate under. Example: Tier 1 (routine) = Support Specialist, can refund up to $500 without approval. Tier 2 (elevated) = Team Lead, can refund up to $2000 and authorize workaround. Tier 3 (critical) = Manager + on-call escalation, full discretion but must notify exec sponsor within 30 min. This is not a chain of command; it is a clarity of spheres. Each level knows their boundary.

**3. Time-Sliced Response Commitments (The Rhythm):** For each severity level, define the response time (acknowledgement) and resolution target (or escalation point if stuck). These are not aspirational; they are thresholds. If a Tier 2 issue is not resolved in 8 hours, it automatically escalates to Tier 3. This removes the need for a human to notice it got stuck — the time boundary itself becomes the trigger. This also creates visibility: if many Tier 2 issues are hitting the escalation boundary, the pattern feeds back that the Team Lead tier is overwhelmed or issues are miscategorized.

**4. Feedback Loop & Threshold Adjustment (The Learning):** Monthly, review escalated issues. Ask: Were they correctly categorized? Did the right person have the authority needed? Did the time targets reflect reality? If 30% of Tier 1 issues are escalating after 2 hours, either the severity taxonomy is wrong or Tier 1 staff are underskilled. Adjust one or the other, test for two weeks, measure again. This closes the adaptive cycle: experience informs rule, rule guides action, outcomes validate or falsify the rule.

The escalation commons does not aim to eliminate escalation — it aims to make escalation a coherent, visible, time-bounded act of governance rather than a hidden flight from responsibility. When severity criteria are transparent and authority is explicit, frontline staff escalate confidently (not with shame or uncertainty), and decision-makers receive signals they can act on, not noise they ignore.

---

### Section 4: Implementation

Start by mapping your current escalations—collect three months of tickets or incidents and ask: *Who decided this went up? Why? How long did it take?* You'll see the pattern. Muddiness here is the problem.

Build your taxonomy together. Gather frontline staff, team leads, and decision-makers in one room (or async if remote, but real dialogue matters). Define 3–5 severity levels tied to observable triggers, not feelings. A customer can't log in (P1). A feature request comes in (P3). Revenue is at risk within 24 hours (P2). Be specific enough that two different people would escalate the same situation the same way. Test it: "A customer complains about slow loading—which level?" If you get different answers, your taxonomy isn't clear yet.

Next, assign owners at each level. For each severity tier, name the person or role responsible for decision-making and include response time targets. P1: VP of Engineering within 15 minutes. P2: Team Lead within 2 hours. P3: Staff handles without escalation. Write it down. Make it visible—on a wiki, in your handbook, printed and taped to the wall if you must.

Create an escalation channel that bypasses email and Slack's chaos. A Slack thread where people state the severity, the trigger that got them there, and what decision is needed. Or a simple form. The friction here is intentional—it gives staff a moment to ask themselves, "Does this really need to go up?"

Crucify the assumption that escalation is failure. Celebrate it. When someone escalates correctly, say so. When a junior engineer spots a P1 and moves fast, that's excellence, not a black mark.

Run a monthly audit. Which issues escalated? Did they match your taxonomy? Did the right person make the decision? Did speed targets hold? Adjust the taxonomy quarterly. As your business changes, so do your thresholds.

### Section 5: Consequences

When this pattern works, the obvious prize appears: issues find the right decision-maker faster. Bottlenecks clear. Frontline staff feel empowered—they know their scope and they know when to call for backup without fear of blame. Decision-makers get fewer interruptions and more context when escalations do arrive.

But the deeper reward emerges over time: your organization develops a *shared language for urgency*. When everyone agrees on what "P2" means, communication becomes faster and more accurate across the whole system. Meetings run shorter. Decisions stop being second-guessed.

The risks, if you don't tend this carefully:

**Taxonomy becomes theater.** Staff learn the *formal* rules but don't trust them, so they escalate anyway, creating a shadow escalation layer that defeats the point. This happens when decision-makers punish escalations or ignore the taxonomy when it suits them.

**Authority hoards.** The people at the top redefine "P1" to include things only they can decide, pulling power downward instead of distributing judgment. The system re-clogs.

**The gap grows between what triggers say and what actually matters.* *Your business pivots, your market changes, a new regulatory risk emerges—but your taxonomy stays static. Staff escalate based on yesterday's logic.

**Escalation becomes a career risk.* *If being associated with an escalated problem damages someone's advancement, they'll hide problems instead of raising them early. You'll get fewer escalations but worse ones.

Watch for these: Are escalations increasing? Are decision-makers complaining about "interruptions" rather than engaging with the taxonomy? Are frontline staff afraid to escalate? That's decay.

### Section 6: Known Uses

**Amazon's two-pizza rule and escalation framework:** Amazon builds escalation into decision rights by team size and scope. A two-pizza team (6–10 people) owns decisions up to a defined limit. Anything beyond requires a single escalation path and decision timeline. The framework spread across thousands of teams because it made escalation non-negotiable and transparent. When you know exactly who owns what and why, you escalate with confidence.

**Surgical teams in trauma centers:** Hospitals use a rigid severity taxonomy (trauma alert levels) that determines which surgeon, which OR, which anesthesiologist shows up and in what time window. A Level 1 trauma triggers a cascade in minutes. Everyone knows the triggers and their role. Lives depend on this pattern working—so it's designed with zero ambiguity. The escalation *is* the decision.

**Prato textile workers' cooperatives (Italy):** In small manufacturing collectives, escalation happens through face-to-face check-ins, but they've formalized *triggers*—a machine down (escalate to the mechanic), a customer order change (escalate to scheduling), a quality failure (escalate to the design circle). The taxonomy is cultural and practiced daily. There's no written handbook, but everyone knows when something goes up and to whom. It works because trust is high and roles are clear.

### Section 7: Cognitive Era

AI reshapes this pattern in two ways. First, severity classification can now be *learned*. Machine learning models can analyze incoming problems, extract features, and predict the right severity level—flagging it for human review before escalation. A support ticket comes in; the system pre-tags it P2 based on language patterns, keywords, and historical outcomes. Humans review and confirm. This reduces judgment friction and standardizes taxonomy application.

Second, distributed decision-making becomes viable. If your organization is large and geographically spread, you can now embed decision-making logic closer to the problem. AI systems can handle routine P3 and P4 escalations with little human input. They can synthesize context from multiple data sources and hand decision-makers a crisp brief instead of a raw issue. The escalation path becomes faster and smarter.

But a trap: over-automation of the taxonomy itself. If an AI system decides what counts as P1 without human calibration, you lose the shared meaning-making that makes escalation work. The system becomes efficient but illegible. Staff stop trusting it. You also miss the pattern recognition that humans do—noticing that certain *types* of P2s are clustering, which might signal a systemic problem.

The healthiest pattern in the cognitive era: AI as a classifier and briefing tool, humans as calibrators and decision-makers. Use AI to *speed* escalation and *clarify* severity, but keep humans in the loop for learning and refinement.

### Section 8: Vitality

**Signs of life:**
- Escalations happen within your time targets consistently.
- When you ask frontline staff "When do you escalate?" they answer quickly and similarly.
- Decision-makers report they have enough context when issues reach them, not confusion or missing pieces.
- You see patterns in escalations (e.g., a recurring P2 every Tuesday) and you act on them—fixing the underlying issue rather than accepting the recurrence.
- New hires ask about escalation policy early and feel confident using it.
- People celebrate good escalations—"You caught that fast and got it to the right person."

**Signs of decay:**
- Escalations miss your time targets. Decisions pile up with senior staff.
- Staff describe escalation as "political"—who you know matters more than the taxonomy.
- The same issues escalate repeatedly but nothing changes.
- You hear: "I'm not sure if this is a P2 or P3, so I'll just send it up."
- Decision-makers complain about "constant interruptions" and staff feel blamed for escalating.
- Issues that should escalate stay hidden until they explode.

**Diagnostic question:** If you removed all names and titles from your organization and showed an outsider your last 20 escalations, could they predict which person made each decision using only your taxonomy? If not, your escalation commons is broken—authority is flowing through relationships, not rules.
