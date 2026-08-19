# COMMONS LOOPS MANIFEST
*How a Commons Holds Its Coherence Over Time*

**Version:** 0.1 (Draft)
**Status:** Living Document
**Companion:** COMMONS_CORE_MANIFEST.md, COMMONS_BLUEPRINT_MANIFEST.md, COMMONS_AGENT_MANIFEST.md, COMMONS_ENGINEERING_MANIFEST.md

---

## Preamble

A commons does not die from catastrophe. It dies from unattended drift.

Purpose grows stale because the environment shifted and no one reviewed it. Patterns accumulate in the library long after they have stopped working. Decisions remain on the books years after the conditions that justified them disappeared. Documents diverge from the reality they were meant to describe. Onboarding instructions reference systems that no longer exist. None of these failures is dramatic on the day it occurs. Each is small enough to ignore. Together, over time, they hollow out the vitality of the commons until the structure that was once load-bearing collapses under a load it would once have carried easily.

The work of holding a living system coherent against drift is not occasional. It is recurring. It is not a project to be completed. It is a rhythm to be sustained. In the language of this OS, it is a **loop**.

Loops are not new to Commons Engineering. They are already present, under other names, in many places: the Pattern Engine Lifecycle (Recognition → Application → Adaptation → Creation) is a loop. The three Production Engines under D4 are loops. The Blueprint Timeslices held side by side and continuously reconciled are a loop. The Triple Diamond cycle of Context → Pattern → Build is a loop. The Active Feedback Loop between Physiology and Anatomy described in the Blueprint Manifest §7 is the canonical loop of the architecture. The Recursive Self-Improvement workflow described in COMMONS_CORE_SPEC §10.2 is a concrete loop shipped with every fork.

What has been missing is the explicit statement that **these are all instances of the same architectural pattern**, and the shared vocabulary that lets a commons name, document, govern, and evolve its loops as first-class artefacts. This manifest establishes that vocabulary.

A Commons Core instance is healthy to the extent that its loops are running. Not because loops produce more — the production engines already do that. But because loops are the mechanism by which a living system holds its own coherence as the environment changes around it. The Anatomy keeps the system identifiable. The Physiology keeps the system operating. The loops keep the system **recognising itself**.

---

## §1 What a Loop Is in a Commons

A **loop** is a bounded, recurring, observable, governable process that maintains a specific property of the commons against drift.

Four qualifications carry weight in this definition.

**Bounded** — a loop has a stated purpose, a stated scope, and a stated stop rule. It is not an open-ended automation. A process that "just runs" is a daemon, not a loop. A loop runs because it has work to do, and it stops when that work is done.

**Recurring** — a loop runs more than once. A one-time script that processes a backlog is a job, not a loop. The defining property of a loop is that it returns: same shape, possibly different content, on a stated rhythm. Each return is an opportunity to detect drift the previous return did not see.

**Observable** — a loop produces a record visible to humans and agents. A loop that runs silently does not exist for the purpose of governance. Every loop emits at least: the fact that it ran, what it touched, what it found, and what it proposed or did. The Issue Board is the canonical observation surface.

**Governable** — a loop is owned by a named agent or human, has a documented contract, can be paused, can be modified, can be retired. A loop that no one can explain or stop is not a loop — it is a piece of debt.

Within this definition, many things in a Commons Core are loops: the weekly alignment check, the monthly board review, the quarterly Blueprint review, the upstream sync review, the Recursive Self-Improvement workflow, the pattern deprecation sweep, the entity registry refresh, the value stream retrospective. Each of these has a trigger, a state it inspects, a feedback it produces, and a rhythm on which it returns. The Loops Manifest is the place where they are named together.

What is **not** a loop in this manifest's sense: a single-execution build script; a CI validation that runs on every PR (this is event-driven, not recurring on a temporal rhythm); a human meeting (a meeting may be triggered by a loop, but a meeting is not a loop unless it has a documented contract and stop rule); a query against the MCP (a query is a read, not a process that maintains anything). The discipline of naming what is and is not a loop is itself part of the practice.

---

## §2 The Six Pieces of a Loop

Every loop in a Commons Core — whether human-run, agent-run, or hybrid — is specified along six pieces. The six pieces are the contract a loop offers to the commons that hosts it. They are also the schema by which a loop is documented in the Loop Registry (§8).

### §2.1 Trigger

What causes the loop to run.

A trigger is one of three kinds. **Temporal triggers** fire on a clock: every Monday at 09:00, the first day of each month, every quarter. **Event triggers** fire when something happens on the board, in the repository, or in a connected Fabric MCP: an issue is closed, a commit lands on main, a supplier loses qualification. **Demand triggers** fire when a human or an agent requests the loop explicitly: a comment on an issue, a slash command, a manual invocation.

A loop may have multiple triggers, but it has one stated **default rhythm** — the cadence on which it is expected to run absent any other signal. The default rhythm is what makes the loop predictable.

### §2.2 Context

What the loop reads at the start of each iteration.

Context is the slice of the commons the loop is allowed to see. A loop is not given the whole instance. It is given exactly what it needs to do its work. The Context piece states this explicitly: the files, the registry sections, the Issue Board queries, the MCP channels, the Fabric MCPs. Context is what the loop reads; Isolation (§2.4) is what the loop is permitted to change.

In a well-specified loop, Context is also the contract that lets the loop be replayed. A loop whose context is fully named can be re-run against a historical snapshot and produce the same output. A loop whose context is implicit cannot. The discipline of stating Context is what makes a loop auditable.

### §2.3 State

What the loop carries between iterations.

Most loops are not memoryless. The pattern deprecation sweep needs to know which patterns it already reviewed. The alignment check needs to know which drift findings have already been escalated. The Blueprint review needs to know which timeslice it last reconciled. The piece of the commons the loop persists across runs is its State.

State is held in the instance, not in the loop runtime. A loop whose state lives only in the memory of the runtime that executes it is not a loop in this manifest's sense — it is a process that happens to repeat. State files are committed to the repository. They are diff-able, forkable, inheritable. When the loop is moved from one runtime to another — from a GitHub Action to a local cron, from a cron to an agent — the State travels with the loop.

A small number of loops are genuinely stateless: their iteration is a pure function of the current Context. These are the simplest loops to operate. Most useful loops accumulate some State, and the discipline is to keep that State small, structured, and human-readable.

### §2.4 Isolation

What the loop is permitted to change, and where.

Isolation is the security boundary of the loop. It answers: which files can this loop write? Which Issues can it open, close, label? Which branches can it push to? Which extension packs can it modify? Which Fabric MCPs can it call with side effects?

The default isolation in a Commons Core is strict. A loop proposes; it does not commit to main. A loop opens issues; it does not close them. A loop writes to a branch named after the loop; humans review and merge. This default is what makes the **Open Loop** (§4.1) the standard mode of operation.

Isolation is also the place where the loop's relationship to the three repository layers is declared. A loop in the `instance/` layer may not write to `commons/` (upstream is read-only in forks). A loop that runs against an extension pack may not modify another pack's content. The three-layer architecture of the OS is enforced at the loop level by the Isolation piece, not by the loop's good behaviour.

### §2.5 Feedback

What the loop produces, and to whom.

A loop that runs and produces nothing observable is a loop only in name. The Feedback piece states the artefacts the loop emits each iteration and the surfaces on which they appear. The canonical surfaces are:

The **Issue Board** is the primary feedback surface for loops that propose work. A loop that detects drift, finds a stale pattern, identifies a misaligned entity, or notices a missing rhythm opens an Issue. The Issue carries the dimension label, the loop name, the iteration timestamp, and the proposed action. The board is where the loop becomes legible to the human-agent team.

The **State files** are the feedback surface for loops that track progress over time. A loop that runs a sweep updates its State file with what it covered, what it found, and what it deferred. The State file is the loop's memory and the team's audit trail.

The **Blueprint** is the feedback surface for loops that produce structural insights. A loop that detects a persistent pattern of drift between L1 purpose and L7 operations does not just open an Issue — it updates the Blueprint's L9 Intelligence section with the finding. This is how loops connect upward into the Anatomy.

Feedback is also the piece that makes Maker/Checker separation (§5) operational. A loop's feedback is the surface against which another loop, or a human, checks the work.

### §2.6 Stop Rule

When the loop concludes its current iteration, and when the loop itself is retired.

Every loop has two stop rules. The **iteration stop rule** says when the current run is complete: when the queue is empty, when the budget is exhausted, when the cycle time is reached, when no new findings have appeared for K consecutive sub-iterations. The iteration stop rule is what makes a loop bounded. Without it, the loop is a daemon dressed as a loop.

The **lifecycle stop rule** says when the loop itself should be retired. A loop is created to maintain a property of the commons. When that property is no longer relevant — the artefact it maintained has been deprecated, the policy it enforced has changed, the drift it detected has been structurally eliminated — the loop should be retired. The lifecycle stop rule names the condition under which retirement is appropriate. A commons whose Loop Registry only grows is accumulating debt; a healthy commons retires loops as deliberately as it creates them.

The Pruning loop class (§3.4) is in part the loop that watches the lifecycle stop rules of other loops.

---

## §3 The Four Loop Classes

Loops in a Commons Core fall into four classes. The classes are not arbitrary categories — they correspond to the four kinds of work a living system must do to hold itself coherent over time. Every loop in the Loop Registry declares its class.

### §3.1 Production Loops

A Production loop creates new artefacts at volume. The artefacts may be patterns, lighthouses, briefings, posts, manifests, value stream documents, entity records, or any other content the commons produces. The Production loop's job is to keep the production line moving and to ensure that what it produces conforms to the relevant specifications.

Production Engines under D4, as described in the Agent Manifest, are Production loops in this sense. Each runs on a cadence, takes inputs from the registry or from the instance workshop (`instance/workshop/`), applies a specified transformation, and emits output to a defined surface. Which Production Engines a particular commons operates is determined by its purpose: a commons whose proposition is curated knowledge will run a pattern engine; a commons whose proposition is operating runbooks will run a build pipeline; a CE-style Incubator will additionally run a Lighthouse engine. The Production Engine loops are the most visible loops in a Commons Core because they are the loops most directly tied to the commons' offered propositions.

A Production loop's default mode is bounded fan-out: take a list of items, transform each, return results, write outputs. A pattern engine takes pattern drafts and produces validated patterns. A build pipeline takes value stream specifications and produces operating runbooks. The specific engines a commons runs are determined by its proposition, not by the OS.

Production loops are owned by the Production Agent (D4) by default. Other agents may invoke Production loops through D4; they do not own them.

### §3.2 Maintenance Loops

A Maintenance loop keeps existing artefacts coherent over time. The Production loop made the pattern; the Maintenance loop checks that the pattern still works. The Production loop produced the Briefing; the Maintenance loop checks that the Briefing's data still matches the reality it described. The Production loop wrote the manifest; the Maintenance loop checks that the manifest's cross-references still resolve.

Maintenance loops are the loops that hold the commons against drift. They are the operational expression of the principle this manifest exists to encode. The weekly alignment check, the monthly Blueprint review, the quarterly entity registry refresh, the upstream sync review, the cross-manifest cascade check — all are Maintenance loops.

A Maintenance loop's default mode is sweep-and-flag: walk a defined corpus, evaluate each item against a coherence criterion, open issues for items that fail. The Maintenance loop does not, by default, fix what it finds. It surfaces the drift and routes it to the appropriate decision-making layer. This is what keeps the loop **Open** (§4.1) and the human-agent team in charge of structural change.

Maintenance loops connect upward through the Blueprint's Active Feedback Loop (Blueprint Manifest §7): drift detected at L7 by a Maintenance loop is processed at L9, escalated through L5, and reaches L3 for governance decision. The Maintenance loop is the bottom of that feedback path.

### §3.3 Governance Loops

A Governance loop keeps human-agent decision-making legitimate and current. Where Maintenance loops detect drift in artefacts, Governance loops detect drift in decisions. A decision made under conditions that no longer hold is a Governance drift. A policy that has not been reviewed in two years is a Governance drift. An Issue that has been open for six months without movement is a Governance drift. A rhythm that has been scheduled but has not actually run for three iterations is a Governance drift.

Governance loops are the loops that keep the Issue Board honest. They scan for stale issues, for closed-without-decision threads, for decisions never recorded as commits, for labels missing on issues that require them, for milestones with no associated work. They do not enforce — enforcement is a human act — but they make the state of governance visible so that the human-agent team can act on it.

The most important Governance loop in every Commons Core is the **Decision Currency loop**: a periodic walk of all `decision`-labelled issues to ask whether the conditions under which each decision was made still hold. A decision whose conditions have changed should be re-opened for review. A decision whose conditions still hold should be reaffirmed in the loop's State file. This loop is what prevents the commons from drifting on the strength of decisions that have quietly become wrong.

Governance loops are owned by the Purpose Agent (D1) by default, because governance is the dimension of decision-making legitimacy. The Purpose Agent's "governance runtime hygiene" responsibility, named in the Agent Manifest, is operationalised as the Purpose Agent's Governance loop registry.

### §3.4 Pruning Loops

A Pruning loop removes what has lost its purpose. A pattern that has been deprecated and is no longer referenced anywhere; an entity record that is duplicated; a rhythm that no longer runs; a State file from a retired loop; an `instance/workshop/` draft that has not been touched in twelve months; a label that no longer applies to any issue — these accumulate, and the commons becomes harder to read.

Pruning loops are the loops that watch for waste. They do not delete unilaterally — deletion is a structural act, and the OS-level rule in COMMONS_CORE_SPEC §11 still applies — but they surface candidates for retirement and route them to the appropriate decision-maker. A pattern flagged as a deprecation candidate becomes an Issue. An entity flagged as a duplication becomes an Issue. A loop flagged as ready for retirement becomes an Issue against the Loop Registry itself.

Pruning loops are what give the Loop Registry its self-regulating property. A loop in the registry whose lifecycle stop rule (§2.6) has been met is surfaced by the Pruning loop as a retirement candidate. This is how the Loop Registry stays a living artefact and not an accumulation of historical good intentions.

Pruning loops are typically scheduled at lower frequency than Maintenance loops — monthly or quarterly rather than weekly — because the work they surface is structural rather than operational. They are usually owned by the Purpose Agent (D1), in close coordination with whichever Agent owns the artefact class being pruned.

---

## §4 Open Loops and Closed Loops

A loop is either Open or Closed. This is a property of the loop, declared in its registry entry, and it determines the loop's relationship to the human-agent team.

### §4.1 The Open Loop — Default

In an **Open** loop, the loop senses, assesses, and proposes — but it does not commit to main, does not close issues, does not change state outside its declared Isolation boundary. The human-agent team reviews the proposal and acts. The loop's output is **a suggestion in a legible form**, not a fait accompli.

The Open Loop is the default in a Commons Core. The architectural reason is given in the Agent Manifest: governance — decisions about purpose, design, culture, structural change — is human territory. The Anatomy of the commons is not revised by automation. A loop that detects drift in L1 purpose does not rewrite L1. It opens an Issue with the finding, labels it `definition`, and waits for the human-agent dialogue to produce a decision. The decision, when made, lands as a commit. The loop's job was to make the question visible. The closing of the loop is the human-agent team's decision, not the loop's continuation.

The Recursive Self-Improvement workflow (COMMONS_CORE_SPEC §10.2) is the archetypal Open Loop in the OS. Its six phases — SENSE, ASSESS, PROPOSE, REVIEW, ACT, LEARN — name explicitly the handoff: the loop owns SENSE, ASSESS, and PROPOSE; humans own REVIEW and ACT; both contribute to LEARN.

### §4.2 The Closed Loop — Exception Under Policy

In a **Closed** loop, the loop senses and acts. It updates files, closes issues, merges PRs, modifies Fabric MCP state, without an intervening human review per iteration. Closed loops are not forbidden, but they are exceptions, and they exist only under an explicit, governance-approved policy.

A Closed loop is appropriate when three conditions hold together. First, the action the loop takes is **reversible** — a mislabelled issue can be relabelled, a misplaced entity can be moved, a cache can be regenerated. Second, the action is **non-structural** — it touches operational state, not Anatomy. A loop that auto-labels issues by dimension is operational; a loop that auto-rewrites purpose statements is structural and forbidden. Third, the action is **policy-bounded** — the governance layer (L3) has explicitly approved the policy under which the loop acts, and the policy is documented in the loop's registry entry.

The Closed Loop is the right mode for high-frequency, low-stakes operational maintenance: cache regeneration, link-rot patching in non-canonical content, automatic label propagation, draft formatting normalisation. It is the wrong mode for any work that touches the Blueprint's Anatomy layers.

The shift from Open to Closed is itself a governance act and is logged as a `decision`-labelled issue. A Closed loop that has been quiet for an extended period — making changes that humans never review — is itself a Governance drift, and the Decision Currency loop (§3.3) should surface it for review.

---

## §5 Maker/Checker Separation

A loop that produces is never the loop that approves.

This separation is structural, not procedural. The loop that generates a Lighthouse Briefing does not also validate it. The loop that drafts a pattern does not also accept it into the library. The loop that proposes a Blueprint update does not also commit it.

The principle has two roots. The first is operational reliability: a producer that judges its own output has no incentive to find its own errors. The second is governance legitimacy: the work of recognising what has been made is a different kind of work from making it, and the commons benefits from holding the two as distinct contracts.

In the four-agent governance model, the Maker/Checker separation often maps onto agent dimensions. A Production loop owned by D4 produces; a Maintenance loop owned by D1 checks. The Production Engine generates patterns; the Coherence Engine (§7) validates that the pattern library remains internally consistent. The producer reports completion; the checker reports findings. Each owns a different surface, and the cross-traffic between them is observable on the Issue Board.

Where Maker and Checker live in the same dimension — for example, two Production loops that feed each other — the separation is maintained at the loop level: distinct loops, distinct registry entries, distinct State files, distinct ownership. A loop whose Maker and Checker pieces have been collapsed into one loop is a loop whose governance has been weakened, and the commons should treat it as an Open Question (§11) for the next governance review.

Maker/Checker is the mechanism through which the Anatomy/Physiology distinction (Blueprint Manifest §4) becomes operational at the loop level. Physiology produces operational reality; Anatomy provides the standards against which Physiology is measured. The Maintenance loop class is, in this sense, the standing Checker on the standing Maker of the Production loop class.

---

## §6 Loops in the Living Blueprint

The Living Blueprint is the canonical location for the documented loops of a commons. Every loop in the Loop Registry is anchored in a specific Blueprint layer, and the Blueprint layers are the canonical homes for the four loop classes.

### §6.1 L7 Operations — The Operational Loops

L7 hosts the loops through which the commons' daily life is conducted. These are the loops whose cadence corresponds to the commons' operational rhythm: the weekly board review, the daily Pattern Engine cycle, the engagement-conversation check-in, the value stream operating runbook. Production loops typically root here.

L7 is also where the **Anomaly Response** loop lives — the loop that watches for signals from L8 sensing and routes them to the appropriate response level. The L7 loops do not decide whether an anomaly indicates structural drift; they ensure the signal reaches L9 for assessment.

### §6.2 L8 Sensing — The Observation Loops

L8 hosts the loops that observe the commons and its environment. These are the loops whose output is data rather than decision: performance sensing against L1 purpose, environment sensing against L2 scenarios, the engagement health check, the entity registry freshness check. Many Maintenance loops have their sensing component rooted at L8 and their proposal component rooted at L7 or L9.

The Sensing loops are the loops most likely to be Closed under policy. A loop that periodically refreshes the public profile of a Lighthouse from public sources is operational, reversible, and non-structural — a valid Closed Loop. A loop that periodically re-evaluates whether L1 purpose still describes the commons' actual value creation is decidedly Open: it produces a finding, and the finding goes to the Issue Board for governance review.

### §6.3 L9 Intelligence — The Loop Registry

L9 is where the commons holds its intelligence about itself, and the **Loop Registry** is a first-class element of L9.

The Loop Registry is the structured directory of every documented loop in the commons. Each entry contains the loop's six pieces (§2), its class (§3), its mode (§4), its Maker/Checker relationships (§5), its owning agent or human, its current State pointer, its lifecycle stop rule, and the date of its last governance review.

The Loop Registry is the surface on which the commons' vitality becomes legible. A commons with an empty Loop Registry has no operational coherence machinery. A commons whose Loop Registry has grown without pruning has accumulated maintenance debt. A commons whose Loop Registry is governed — loops added deliberately, retired deliberately, reviewed at the same cadence as the rest of the Blueprint — is a commons whose self-improvement is alive.

The Loop Registry is also the place from which the operating rhythms surface in `instance/operations/rhythms.md` (§8.2). The rhythms file is a generated, human-readable view over the Loop Registry, not a separate truth.

### §6.4 L5 Integrity — The Coherence Loops

L5 hosts the loops that watch for coherence failures between Blueprint layers and across timeslices. These are the highest-level Maintenance loops in the commons. They run less frequently — typically monthly or quarterly — and their findings, when they appear, are usually consequential.

The L5 loops are the architectural guardians. They are what the Blueprint Manifest §7 names as the formal escalation path of the Active Feedback Loop. The Maintenance class as a whole connects upward into L5 through these loops.

### §6.5 L3 Governance — The Decision Currency Loops

L3 hosts the Governance loops whose subject is the legitimacy and currency of decisions. The Decision Currency loop named in §3.3 lives here. So does the **Consent Drift** loop — the loop that detects when stakeholder consent given at one point has expired, or when the conditions under which consent was given have changed materially. Governance loops at L3 are the loops through which the chaordic principle is held operational over time.

---

## §7 The Coherence Engine

The Commons Agent Manifest establishes that Engines are the production lines under D4. The Engines a particular commons operates — pattern engines, build pipelines, and any others its proposition requires — are the producers of the commons' offered artefacts at volume. This manifest establishes a distinct **class** of Engine that every commons needs, regardless of which production Engines it runs:

The **Coherence Engine** is the production line that keeps the others operable.

Where the production Engines turn inputs into outputs, the Coherence Engine turns the accumulating outputs of the commons back into a coherent operating environment. It runs the Maintenance, Pruning, and selected Governance loops described in §3. It is the home of the Decision Currency loop, the Loop Registry retirement loop, the cross-manifest cascade check, the pattern-deprecation sweep, and the operational rhythm audit.

The Coherence Engine sits under D4 because it is operationally a production line — the work it produces is structured findings and proposed corrections, at volume, on a schedule. But it differs from the production Engines in one decisive respect: its output is **never** committed to main directly. The Coherence Engine is by architecture an Open Loop engine. Every finding it produces is a proposal to the human-agent team. The production Engines produce; the Coherence Engine proposes corrections to what they have produced.

The Coherence Engine is the structural answer to the question this manifest opens with. A commons does not die from catastrophe. It dies from unattended drift. The Coherence Engine is the engine whose existence guarantees the drift will be attended to.

A commons that has not instantiated a Coherence Engine has not yet completed its production architecture. Whatever production Engines it runs, each produces in its direction; without a Coherence Engine, what each produces accumulates without supervision. The Coherence Engine is what closes the production system into a self-maintaining whole — and unlike the production Engines, whose presence and shape vary with the commons' proposition, the Coherence Engine is universal: every commons benefits from one.

---

## §8 The Loop Registry as Workspace Artefact

The Loop Registry is anchored in L9 of the Blueprint (§6.3) but is instantiated as concrete files in the instance workspace. This section specifies the workspace structure.

### §8.1 The `instance/operations/loops/` Directory

Every documented loop in the commons has a corresponding file under `instance/operations/loops/`. The filename is the loop's slug. The format is YAML with a brief Markdown description.

```
instance/operations/loops/
├── alignment-check.yml
├── blueprint-review.yml
├── decision-currency.yml
├── entity-registry-refresh.yml
├── pattern-deprecation-sweep.yml
├── upstream-sync-review.yml
├── recursive-self-improvement.yml
└── README.md
```

Each loop file declares the six pieces (§2), the class (§3), the mode (§4), the Maker/Checker relationships (§5), the Blueprint anchor layer (§6), the owning agent, the State file location, the lifecycle stop rule, and the date of last governance review. The loop's runtime — the GitHub Action, the local cron, the agent invocation — references this file as the source of truth for its contract.

The loop's State file lives alongside, in `instance/operations/loops/_state/<loop-slug>.yml` or, where the state is more substantial, in a subdirectory. State files are committed to the repository like everything else.

### §8.2 Relationship to `instance/operations/rhythms.md`

The existing `instance/operations/rhythms.md` is a human-readable summary of the operating rhythms of the commons. With the Loop Registry in place, `rhythms.md` becomes a **generated view** over the Loop Registry — the same trigger and cadence information, formatted as the existing rhythms table.

The Commons Core upstream provides a generator script that reads `instance/operations/loops/` and writes the rhythms table into `rhythms.md`. The narrative sections of `rhythms.md` — stage-specific rhythms, instance-specific notes — remain human-authored. The table at the top is generated.

This relationship preserves the existing surface for the team that has been reading `rhythms.md` and adds the structured backing that the Loop Registry provides. Forks that have not yet adopted the Loop Registry continue to operate from a hand-maintained `rhythms.md`. Forks that adopt the Loop Registry gain the structured backing without losing the human-readable surface.

### §8.3 Relationship to `.github/workflows/`

The existing `improvement-loop.yml` GitHub Action remains the implementation of the Recursive Self-Improvement loop. With the Loop Registry in place, the workflow reads its contract from `instance/operations/loops/recursive-self-improvement.yml` rather than from inline configuration.

Forks may choose to split the single `improvement-loop.yml` into class-specific workflows — `production-loops.yml`, `maintenance-loops.yml`, `governance-loops.yml`, `pruning-loops.yml` — once they have enough documented loops to justify the separation. The single-workflow default is sufficient for a young commons. The split becomes useful as the Loop Registry grows.

---

## §9 Operationalising Adaptive Management

This manifest does not introduce a new principle into Commons Engineering. The principle is already named in the discipline.

The COMMONS_ENGINEERING_MANIFEST §2.3 First Practices, under Governance, states:

> **Adaptive management** — continuous sensing, learning, and rule-revision as a governance practice rather than an exception.

This is the First Practice this manifest operationalises. The principle that a living system holds its coherence over time only through recurring, governed sensing and rule-revision — and that the work of recognising drift is built into the system's rhythm rather than triggered by crisis — is already canonical in the discipline. What has been missing is the operational shape: how does Adaptive Management actually run, day after day, in a commons that has forked the OS?

The Loops Manifest is the answer. The six pieces of a loop (§2), the four loop classes (§3), the Open/Closed distinction (§4), the Maker/Checker separation (§5), the Blueprint anchoring (§6), the Coherence Engine (§7), and the Loop Registry as a workspace artefact (§8) are together the operational specification of Adaptive Management as a Commons Core practice.

This positioning carries two consequences worth stating explicitly.

First, **no edit to the COMMONS_ENGINEERING_MANIFEST is required by this work**. The First Practice already names the principle. A small forward-reference from §2.3 to this manifest is the most that should be added — and only if the manifest hierarchy benefits from it. The discipline's foundational document remains foundational; this manifest takes its place one level down, as an operational specification.

Second, **the relationship to the Blueprint Manifest's Active Feedback Loop (§7) sharpens**. The Active Feedback Loop describes the architectural path through which sensing data ascends from Physiology to Anatomy in a single commons. Adaptive Management as a First Practice names the discipline of running that path on a stated rhythm. The Loops Manifest specifies the operational shape that running takes. Each manifest holds its level.

A commons that has internalised Adaptive Management treats loops as architectural artefacts, not as nice-to-haves. It documents them in the Loop Registry, governs them like any other policy, and retires them with the same deliberation it applies to retiring a pattern. A commons that has not internalised the practice accumulates drift in the spaces between catastrophes. The First Practice names what to do. This manifest names how to do it.

---

## §10 Relationship to Other Manifests

The Loops Manifest sits adjacent to the Blueprint and Agent manifests in the manifest hierarchy. It does not replace either; it operationalises the rhythm dimension that both assume but neither makes explicit.

- **Commons Engineering Manifest** — establishes the discipline, including the First Practice **Adaptive Management** in §2.3 Governance. The Loops Manifest is the operational specification of that First Practice.

- **Commons Core Manifest** — establishes the OS architecture, including §2.6 Recursive Self-Improvement at the OS-component level. The Loops Manifest expands this from a single workflow into a four-class loop taxonomy and a Loop Registry, with the Coherence Engine as a fourth Production Engine under D4.

- **Commons Blueprint Manifest** — establishes the Living Blueprint (L1–L9), including §7 Active Feedback Loop. The Loops Manifest anchors specific loops in specific Blueprint layers (§6) and adds the Loop Registry as an L9 Intelligence artefact.

- **Commons Agent Manifest** — establishes the four-agent governance model and the distinction between Agents and Engines. The Loops Manifest adds the Coherence Engine as a distinct, universally-needed class of Engine under D4 and assigns default loop-class ownership to the four Agents.

- **Commons Core Spec** — implements the file-level reality of the OS. The Loops Manifest extends the spec with `instance/operations/loops/` as the workspace location for the Loop Registry and clarifies the relationship to `rhythms.md` and `.github/workflows/`.

- **Commons Engineer Manifest** — establishes the practitioner. Working with loops is a practice that grows along the 7Cs. A Commons Engineer who has not yet developed the discipline of running maintenance loops on their own work cannot yet hold the discipline operational for a commons.

---

## §11 Open Questions

| # | Question | Status |
|---|---|---|
| 1 | **Loop Registry schema versioning:** How do loop registry entries declare their schema version, and how do forks migrate when the schema evolves? | Open |
| 2 | **Closed Loop policy template:** What does a governance-approved Closed Loop policy look like as a structured artefact? | Open |
| 3 | **Cross-commons loop sharing:** Can a Maintenance loop be packaged in an extension pack and reused across forks? What is the contract? | Open |
| 4 | **Loop budget enforcement:** When loops run on shared infrastructure, how is per-loop budget declared and enforced? | Open |
| 5 | **Loop telemetry:** What is the minimum telemetry a loop must emit to support the Decision Currency review of its own usefulness? | Open |
| 6 | **Human-only loops:** A loop whose Trigger, Context, and Feedback are entirely human-mediated (a weekly standup) — is it in the Loop Registry, or only its automated companion? | Open |
| 7 | **Coherence Engine bootstrapping:** What is the minimum Coherence Engine a young commons should ship from fork — which loops are non-negotiable defaults? | Open |
| 8 | **Loop deprecation versus loop retirement:** Should the Loop Registry distinguish between a loop that is paused pending review and a loop that is permanently retired? | Open |

---

## §12 Implementation Notes

This manifest is published as v0.1 (Draft). Its operational instantiation in the Commons Core proceeds in the following sequence; each step is independently shippable.

1. **This manifest** lands in `commons/manifests/COMMONS_LOOPS_MANIFEST.md` and is referenced from `COMMONS_CORE_MANIFEST.md` and `COMMONS_BLUEPRINT_MANIFEST.md` companion blocks.

2. **The Loop Registry section** is added to the `COMMONS_BLUEPRINT_MANIFEST.md` description of L9 Intelligence, with a forward reference to this manifest.

3. **Optional forward-reference** is added to `COMMONS_ENGINEERING_MANIFEST.md` §2.3 at the "Adaptive management" entry, pointing to this manifest as the operational specification. No new principle is introduced; the First Practice already names it.

4. **The Coherence Engine** is added to the `COMMONS_AGENT_MANIFEST.md` §3 distinction between Agents and Engines, as a distinct, universally-needed class of Engine under D4.

5. **The workspace skeleton** is added to the Commons Core template: `instance/operations/loops/.keep`, `instance/operations/loops/_state/.keep`, and a starter `README.md` describing the directory's contract.

6. **The Recursive Self-Improvement workflow** in `COMMONS_CORE_SPEC §10.2` is annotated as an instance of the Open Loop pattern, of class Governance (with embedded Maintenance and Pruning passes), with a forward reference to this manifest.

7. **The `rhythms.md` generator** is added to `commons/scripts/` as an optional utility that forks may adopt when their Loop Registry has matured to a useful size.

These seven steps complete the integration of Loops as a structural principle into the Commons Core without breaking any existing fork. A fork that does not adopt the Loop Registry continues to operate as before. A fork that adopts it gains the structural backing without changing its operating surface.

---

*COMMONS LOOPS MANIFEST v0.1*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
