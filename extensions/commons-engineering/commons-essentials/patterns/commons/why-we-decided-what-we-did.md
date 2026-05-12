---
id: pat_5ce1b2383a4f45dcabd22a0a
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: truth-seeking-transparency
  principle: Truth-Seeking Sustains Systems
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: conflict-resolution-evolving-rules
  principle: Conflict Evolves Systems
  influence: 0.7
- hub_id: time-sliced-iterative-planning
  principle: Plan in Short Cycles
  influence: 0.7
slug: why-we-decided-what-we-did
title: Why We Decided What We Did
aliases: []
summary: Document your decisions and the thinking behind them so your group learns from choices, stops relitigating old questions,
  and stays accountable.
context_labels: {}
ontology:
  domain: governance-decision-logging
  cross_domains: []
  search_hints:
    primary_tension: Institutional amnesia vs. adaptive learning
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
    vitality_reasoning: A commons thrives when it remembers its own history — not as rigid doctrine, but as living feedback.
      This pattern creates a shared archive of 'why we chose this' that evolves with the system. It prevents the slow decay
      of institutional knowledge, reduces the cognitive load of re-litigating old decisions, and makes governance visible
      so new members can understand the culture's logic. The pattern is alive because decisions are captured with context
      and rationale, not just outcomes — enabling future stewards to adapt the choice when conditions change, rather than
      blindly repeat or thoughtlessly abandon it.
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

> Document your decisions and the thinking behind them so your group learns from choices, stops relitigating old questions

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every collective makes choices: which technologies to adopt, how to organize work, which trade-offs to accept, which values to prioritize. In the early days, these decisions live in conversation and memory. But as the community grows, scales, or changes members, that oral tradition breaks down. Teams re-argue the same choice every 18–24 months. New stewards inherit structures without understanding their rationale and strip them away. Decisions made under one set of constraints persist unchanged when constraints shift. This pattern draws on Orbit 1 principles of Adaptive Management (treating decisions as experiments with embedded hypotheses), Conflict Resolution (capturing how competing values were weighed), and Truth-Seeking (making the reasoning transparent so it can be tested and refined). A governance memory is the nervous system of a mature commons.

---

### Section 2: Problem

> **The core conflict is Institutional amnesia vs. adaptive learning.**

Decision-making under opacity creates cascading costs. Without a record, each new stakeholder brings their own mental model of 'how we do things.' Decisions are re-litigated in hallway conversations rather than resolved in deliberate forums. Institutional memory lives only in the oldest members; when they leave, the knowledge vanishes. Teams make inconsistent choices across projects because no one knows what was decided before. Most damagingly, decisions made for sound reasons under one context persist unchanged when contexts shift — not because they are good, but because no one remembers why they were made at all. The result is a system that neither learns nor governs; it drifts. The tension is acute: making decisions transparent requires effort and ceremony, which can feel like bureaucratic drag. But hiding decisions creates amnesia, and amnesia is the enemy of living, adaptive systems.

---

### Section 3: Solution

Establish a Governance Memory — a shared archive where every significant decision is recorded with four elements: the choice made, the context in which it was made, the reasoning (including values and trade-offs weighed), and the date it was made. This is not a policy manual or a decision log that simply lists outcomes. It is a reasoning archive.

The mechanism has three parts:

**1. Capture at the Point of Decision.** When a community makes a consequential choice (architectural, organizational, strategic, governance), one steward writes a brief decision record within one week of the choice. This captures: What did we choose? Why did we choose it (what problem did it solve, what values did it honor)? What alternatives did we reject and why? Who was consulted? What assumptions are embedded in this choice? The record is time-stamped and attributed. This is not onerous if embedded in the decision workflow itself — a five-minute reflection at the end of a deliberation.

**2. Make It Retrievable and Living.** The archive is not a static vault. It is organized by domain (architecture, governance, values, operations) and searchable. More importantly, every decision record includes a review date — typically 18–24 months after the choice. At that review, the stewards responsible for the decision gather to ask: Does this choice still serve us? Have conditions changed? What have we learned? They update the record with new learning and either reaffirm the choice, adapt it, or retire it. This transforms the archive from a museum into a living feedback loop.

**3. Use It as a Teaching Tool.** When new members join, they read the decisions in their domain before they begin. They see not just what the community decided, but the reasoning — the values hierarchy, the constraints acknowledged, the trade-offs accepted. This accelerates their understanding of the culture's logic. When conflict arises, stewards can point to the reasoning behind an existing choice and either defend it (if conditions haven't changed) or deliberately update it (if they have). The archive becomes the commons' conscience — a shared reference point for what we care about and why.

The pattern is commons-native because it makes governance transparent, distributes memory across the collective (rather than concentrating it in one keeper), and creates feedback loops that let the community learn from its own choices. It embodies the principle that a living system must know itself — must make its reasoning visible so it can be tested, adapted, and ultimately held accountable by its own members.

---

### Section 4: Implementation

Start small. Don't wait for the "perfect system." Pick a single decision made in the last month—something that shaped how work flows or what you build. Gather the people who were in the room. Ask them:

- What did we decide?
- What problem were we trying to solve?
- What did we consider and reject, and why?
- What did we assume we'd revisit?

Write it down in plain language. A paragraph or two. Post it somewhere shared—a wiki, a Slack channel pinned to a purpose, a Google Doc folder labeled "How We Got Here." Include the date and who was involved.

Then make it a habit. When your team makes a choice about infrastructure, process, hiring criteria, or values—anything that shapes how work happens—pause before the decision hardens into practice. Spend 20 minutes capturing the thinking. Not the meeting notes. The *reasoning*. What mattered. What we're betting on. What we're deferring.

Create a simple template:

**Decision:** (One sentence.)  
**Context:** (What problem prompted this? What was the state before?)  
**Reasoning:** (What values or constraints did this honor? What trade-offs did we accept?)  
**Uncertainties:** (What might we be wrong about? What should trigger a revisit?)  
**Date & Participants:** (So someone can ask follow-up questions later.)

Appoint a guardian—one person whose job is to nag gently when a significant choice is made without being captured. This person is not a bottleneck; they're a prompt. After a few months, the practice becomes reflex.

Review the archive quarterly. Not to enforce compliance, but to notice patterns. Are we making similar trades repeatedly? Are old assumptions still sound? Are new members able to understand *why* things work the way they do?

### Section 5: Consequences

When this pattern takes root, several things flourish:

**New members onboard faster.** They don't have to reverse-engineer culture from behavior. They can read why you chose async communication, or why you don't hire for "culture fit," or why you sunset that tool. Understanding the reasoning builds judgment, not just compliance.

**Decisions improve.** When you write down your thinking, you notice gaps—assumptions you didn't name, stakeholders you forgot to consider. The next similar choice benefits from that clarity.

**Trust deepens.** People see that choices aren't arbitrary. They were made for reasons. Even people who would have chosen differently can respect the thinking. Accountability becomes possible.

**But risks emerge if this pattern atrophies:**

The archive becomes a monument instead of a living thing. Decisions are recorded but never revisited. Old reasoning calcifies into dogma. People cite "that's how we decided it in 2021" instead of asking whether 2021's context still holds.

The pattern can also create false legitimacy. A badly reasoned decision, once written down, feels authoritative. If you're not careful, the archive becomes a defense against challenge rather than a tool for learning.

There's also the risk of *governance theater*—recording decisions to look organized while the real choices happen elsewhere, in side conversations or Slack threads. The archive only works if it captures the actual reasoning, not a sanitized version.

### Section 6: Known Uses

**Apache Software Foundation:** Major decisions about project direction, governance changes, and protocol shifts are recorded in RFC (Request for Comments) threads and archived. New contributors can understand why certain architectural choices were made years earlier, and proposals reference past reasoning to avoid repeating old debates.

**Basecamp:** The company documents decisions about product features, company practices, and values in a shared knowledge base. When a question about "why do we work async?" comes up, there's a recorded answer that explains the reasoning and trade-offs, not just the rule.

**Bugyo (Japanese artisan collectives):** Traditional craft guilds maintained written lineages of technique decisions—which methods were refined, which tools were adopted, which approaches were abandoned and why. This reasoning archive allowed apprentices to understand not just *how* to work, but the evolution of judgment within the craft.

**Ubuntu Community Council:** Decisions about governance, code of conduct enforcement, and community direction are recorded with full context. This prevents the same governance questions from cycling every few years and makes it clear how community values shaped structural choices.

### Section 7: Cognitive Era

AI changes how this pattern breathes.

With large language models, capture becomes cheaper—you can feed meeting transcripts into a tool that surfaces reasoning, flags assumptions, and suggests gaps. The work shifts from *creating* the archive to *curating* it. Teams will need to decide what stays in the foreground versus what's searchable but not emphasized.

But there's a deeper shift: distributed teams can now have reasoning assistants. An LLM trained on your decision archive could surface relevant precedent while a choice is being debated, or flag when you're re-litigating an old question. The archive becomes less static record and more active counsel.

The risk is automation-induced amnesia. If machines summarize and surface reasoning, teams may stop *thinking through* the reasoning themselves. The archive must remain a place where humans slow down, not a substitute for deliberation.

Asynchronously distributed teams—coordinating across time zones—especially benefit. The archive becomes a form of *documented presence*. When a decision-maker is asleep, their reasoning is still available to guide those awake.

### Section 8: Vitality

**Signs of health:**

- When a new proposal arrives, someone asks, "Did we consider this before?" and finds the answer in the archive.
- New members cite past reasoning to make their case for *change*—they understand the original logic well enough to argue for evolution.
- Decisions explicitly reference the archive: "We used to avoid hiring for this, and here's why that reasoning no longer holds."
- The archive grows without becoming unwieldy. You're capturing decisions, not drowning in noise.

**Signs of decay:**

- People have forgotten the archive exists, or it's so buried that no one searches it.
- Decisions get recorded but never consulted. The archive is a graveyard.
- New team members make choices without even knowing the reasoning-archive exists.
- The same question gets re-debated every 18 months as if it's never been considered.
- The archive becomes a tool for enforcement—"We decided this, so stop questioning it"—rather than learning.

**Diagnostic question:**

When someone new joins your team and asks "Why do we do it this way?" can you point them to where the reasoning lives, or does it only exist in the oldest member's head?
