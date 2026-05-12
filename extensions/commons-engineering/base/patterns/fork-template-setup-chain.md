---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: pat_01kkhc8hd5r49dm3w39cye3sjs
orbital_layer: 2
sector: "Universal"
gravitational_hubs:
  - hub_id: "core_composability"
    influence: 0.95
  - hub_id: "core_resilience"
    influence: 0.85
  - hub_id: "core_subsidiarity"
    influence: 0.75

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: fork-template-setup-chain
title: "Fork-Template-Setup Chain"
aliases: ["The Boot Sequence", "Commons in Minutes", "Scaffolding as Stewardship"]
summary: >-
  The mechanics of creating a new commons: a GitHub template
  repository, a setup script, and a governed boot sequence that
  produces an operational commons in minutes. Template for
  private-first (recommended), fork for intentionally public
  projects. The setup chain creates labels, project board,
  milestones, GitHub Pages, upstream remote, locale configuration,
  and agent seats — everything needed to start governing from
  minute one. This is not convenience automation. It is the
  encoding of governance defaults into infrastructure.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Enterprise Template and Onboarding Automation"
  government: "Institutional Setup and Compliance Scaffolding"
  activist: "Movement Starter Kit"
  tech: "Project Scaffolding and CLI Generators"
  academic: "Research Lab Setup and Standards Compliance"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: commons-engineering
  cross_domains: [business, life, urban, ecology]
  commons_domain:
    - commons-engineering
  search_hints:
    primary_tension: "Manual Craftsmanship vs. Automated Scaffolding"
    vector_keywords: ["fork", "template", "setup", "scaffolding", "boot sequence",
                      "automation", "GitHub template", "create-react-app",
                      "generator", "commons OS", "operational in minutes",
                      "governance defaults", "labels", "milestones",
                      "project board", "infrastructure as code"]
  commons_assessment:
    stakeholder_architecture: 4
    value_creation: 5
    resilience: 5
    ownership: 5
    autonomy: 5
    composability: 5
    fractal_value: 5
    vitality: 4.8
    vitality_reasoning: >-
      The setup chain is the mechanism through which the Commons OS
      replicates. Without it, creating a new commons requires manual
      configuration of dozens of components — governance labels,
      project boards, agent configurations, locale files, build
      pipelines. With it, a new commons is operational in minutes,
      with governance defaults that encode the accumulated wisdom of
      the pattern. This is composability at its most practical: the
      template is a seed that contains the full genome of the
      operating system, and the setup script is the germination
      process that brings it to life in a specific context.
    overall_score: 4.8

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  usage_stage: design
  adoption_stage: early_adopters
  status: stable
  version: 1.0
  confidence: 3

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: HARD RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  generalizes_from:
    - slug: patterns-over-protocols
      weight: 0.85
    - slug: time-sliced-specification
      weight: 0.8
  specializes_to:
    - slug: commons-blueprint
      weight: 0.9
    - slug: blueprint-application
      weight: 0.85
  enables:
    - slug: locale-first-identity
      weight: 0.9
    - slug: agent-seat-at-the-table
      weight: 0.9
    - slug: intranet-extranet-publishing
      weight: 0.85
    - slug: operational-cadence
      weight: 0.85
    - slug: governance-design
      weight: 0.85
    - slug: commons-as-practice
      weight: 0.8
  requires:
    - slug: purpose-definition
      weight: 0.9
    - slug: commons-boundary-definition
      weight: 0.85
  alternatives: []
  complementary:
    - slug: living-system-design
      weight: 0.85
    - slug: transformation-sequencing
      weight: 0.8
    - slug: engineering-attitude
      weight: 0.8
  tools:
    - slug: github-templates
      type: platform
    - slug: github-cli
      type: tool
    - slug: bash-scripting
      type: tool

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-03-12
  entities:
    - id: boot-sequence
      type: practice
      label: "Commons Boot Sequence"
      relevance: 1.0
    - id: template-repository
      type: concept
      label: "Template Repository as Seed"
      relevance: 0.95
    - id: governance-defaults
      type: concept
      label: "Governance Defaults in Code"
      relevance: 0.95
    - id: setup-script
      type: practice
      label: "Setup Script as Germination"
      relevance: 0.9
    - id: operational-in-minutes
      type: concept
      label: "Operational in Minutes"
      relevance: 0.85
  communities:
    - commons-os-foundations
    - commons-engineering-foundations
    - developer-tooling
  inferred_links:
    - target: locale-first-identity
      reason: "Shared entities: Boot Sequence includes locale question as first step"
      strength: 5
    - target: agent-seat-at-the-table
      reason: "Shared entities: Boot Sequence configures agent seats"
      strength: 5
    - target: intranet-extranet-publishing
      reason: "Shared entities: Setup configures dual build targets"
      strength: 4
    - target: commons-blueprint
      reason: "Shared entities: Template Repository contains blueprint structure"
      strength: 5

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources:
  - "Commons Engineering Framework"
  - "Commons OS Specification v0.1"
  - "GitHub Template Repositories documentation"
  - "create-react-app — scaffolding as architectural opinion (2016)"
  - "Ruby on Rails — convention over configuration (2004)"
  - "Yeoman — the web scaffolding tool (2012)"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
collection: commons-os
collection_ring: operating-patterns
7cs_arc: [composability, commons, capital]
---

> What took three years, a team of consultants, and brown paper on the wall — Commons OS makes accessible in minutes. Not because the work is less. Because the defaults are better.

> [!NOTE] Confidence Rating: ★★★ (High)
> Project scaffolding is one of the most proven patterns in software engineering. From Rails' "convention over configuration" (2004) to create-react-app (2016) to GitHub's template repositories (2019), the principle is well-established: a well-designed template with a guided setup sequence allows practitioners to start producing value immediately rather than spending days on infrastructure. The Commons OS applies this principle to organisational governance, not just code — making it simultaneously more ambitious and more consequential.

---

### Section 1: Context

Starting something new has always been disproportionately expensive. Not the work itself — the setup. Before a carpenter can build, the workshop must be organised: tools arranged, materials sourced, jigs built, workbench levelled. Before a software developer can code, the project must be scaffolded: repository created, dependencies installed, build system configured, deployment pipeline wired, linting rules set. Before a commons can govern, the infrastructure must be established: governance structure defined, communication channels created, decision records initialised, roles assigned, boundaries drawn.

In every domain, this setup cost creates a barrier to entry that is inversely proportional to experience. The veteran carpenter's workshop is already organised. The experienced developer has project templates. The seasoned governance practitioner has playbooks. The newcomer — the person who most needs to start — faces the highest setup cost.

Software engineering solved this problem decades ago with scaffolding tools. Rails gave developers `rails new` — a single command that produced a fully configured project with database, web server, test suite, and deployment pipeline. create-react-app did the same for React. Yeoman did it for arbitrary project types. GitHub's template repositories made it platform-native: click "Use this template" and get a new repository with the full directory structure, configuration files, and CI/CD pipelines of the template.

The insight behind all of these tools is the same: the defaults encode expertise. A well-designed template is not just empty structure waiting to be filled. It is a set of opinionated decisions about how things should be organised, what conventions should be followed, what governance (or coding) standards should apply. The practitioner who uses the template inherits these decisions without needing to make them from scratch — and can then modify them as they develop their own expertise and their own context demands.

Commons Engineering applies this insight to the most complex scaffolding challenge: not a code project, but a governed living system. The Commons OS template is a GitHub template repository that contains not just directory structure but governance architecture: the four agent seats, the nine-layer blueprint, the value stream families, the dimensional navigation, the locale configuration, the publishing pipeline, and the project management infrastructure. The setup script brings this template to life in a specific context — configuring it for a specific purpose, a specific language, a specific domain, a specific team.

---

### Section 2: Problem

> **The core conflict is Manual Craftsmanship vs. Automated Scaffolding.**

The forces pulling toward manual setup (each commons hand-crafted from scratch) and the forces pulling toward automated scaffolding (each commons instantiated from a template) are both legitimate, and the tension is productive.

**Force 1: The craftsmanship instinct.** A commons is a living system, not a manufactured product. Every community is different, every purpose is unique, every context has specific requirements. The instinct to hand-craft every commons from scratch honours this uniqueness. The carpenter who builds each joint individually produces work that fits perfectly. The danger of scaffolding is that it imposes uniformity where diversity is needed.

**Force 2: The setup cost barrier.** Without scaffolding, creating a new commons requires the founder to make hundreds of decisions before governance can begin: What labels do we use? What project board structure? What agent configuration? What directory layout? What publishing pipeline? Each decision is small, but the aggregate is overwhelming — especially for a founder who is energised by purpose, not by infrastructure. The setup cost delays the moment when the commons starts doing its actual work.

**Force 3: The governance default problem.** When commons are set up manually, governance defaults are whatever the founder happens to think of. Critical governance infrastructure — decision labels, dimensional categorisation, cadence milestones, visibility policies — may be omitted simply because the founder did not think of them. A template encodes governance best practices as defaults: the founder gets them automatically and can modify them if needed, rather than needing to invent them from scratch.

**Force 4: The fork vs. template question.** Git offers two mechanisms for replicating a repository: fork and template. A fork creates a linked copy — the new repository retains a connection to the original, can pull updates, and is public if the original is public. A template creates an independent copy — a fresh repository with no history, no link to the original, and private by default. For a commons, the choice matters: a fork is appropriate for intentionally public projects that want to stay connected to the upstream. A template is appropriate for private-first projects that want a clean start. Most commons should use template.

**Force 5: The upstream evolution question.** The Commons OS template will evolve — new patterns, improved governance structures, better agent configurations. A commons created from the template at time T has the template's state at time T. How does it receive improvements made at time T+1? A fork can pull upstream changes. A template-created repository cannot — unless it explicitly adds the template as a remote and selectively merges. The setup chain must provide the mechanism for this ongoing connection without forcing it.

**Force 6: The "operational in minutes" promise.** The setup chain must genuinely produce an operational commons — not just a directory structure, but a functioning governance environment with working labels, a configured project board, agent seats ready for use, and a publishing pipeline that builds. If the setup produces a half-configured environment that requires hours of manual finishing, the promise is broken and the pattern fails.

---

### Section 3: Solution

> **Therefore, provide a template repository and a setup script that together produce a fully operational commons in minutes — encoding governance defaults as infrastructure, configuring the four dimensions, and establishing the upstream connection for future evolution.**

The solution is the Fork-Template-Setup Chain — a three-stage process:

**Stage 1: Template (the seed).** The Commons OS template repository contains the full directory structure, governance architecture, and configuration files for a commons. It is a GitHub template repository — using "Use this template" creates a new, independent, private repository with the template's content and no Git history link. This is the recommended path for most commons. For intentionally public projects that want to maintain an upstream connection, fork is the alternative.

**Stage 2: Setup (the germination).** The `setup.sh` script (or its platform-appropriate equivalent) is run once after the template is instantiated. It is an interactive script that asks the founder a series of questions and configures the commons based on the answers. The setup script is the boot sequence — it transforms a generic template into a specific, purpose-configured commons.

**Stage 3: Operations (the growth).** After setup completes, the commons is operational. The project board has labels, milestones, and columns. The agent seats are configured. The locale is set. The publishing pipeline is wired. The founder can immediately create the first governance issue, begin the first blueprint conversation, or start the first deliberation. The setup cost is behind them; the governance work is ahead.

---

### Section 4: Implementation

**Step 1: Create the template repository structure.** The Commons OS template repository follows the structure defined in the Commons OS Specification (v0.1):

```
[purpose]-os/
├── AGENT.md                          # Agent configuration
├── ALIGN.md                          # Alignment service check
├── .commons/
│   ├── config.yml                    # MCP endpoints, tier, connections
│   ├── identity.yml                  # Commons identity (slug, purpose, domain, locale)
│   └── locales/                      # Locale files (see pat_01kkhc8hcwxj08z6nxhr34et2s)
│       ├── en.yml
│       └── de.yml
├── blueprint/                        # The Living Blueprint
│   ├── L1-identity-purpose.md
│   ├── L2-design-specification.md
│   └── ...                           # L3 through L9
├── inventory/                        # Locally owned entities
├── valuestreams/                     # Organised by four dimensions
│   ├── definition-purpose/
│   ├── participation-relationship/
│   ├── proposition-exchange/
│   └── production-resilience/
├── _patterns/                        # Local pattern adaptations
├── _specifications/                  # Local specifications
├── _manifests/                       # Local manifests
├── setup.sh                          # The boot sequence script
└── README.md                         # Generated during setup
```

**Step 2: Implement the setup script.** The `setup.sh` script performs the following steps in sequence:

1. **Locale question** (first, always): "In welcher Sprache arbeitest du?" / "What language do you work in?" Sets the locale for all subsequent interactions and configurations. (See pat_01kkhc8hcwxj08z6nxhr34et2s.)

2. **Purpose question**: "What is the purpose of this commons?" The answer is written to `.commons/identity.yml` as the `purpose` field and used to generate the README and the first blueprint layer (L1).

3. **Domain question**: "Which domain does this commons primarily serve?" Options: Life, Business, Urban, Ecology, Universal. Configures the default value stream families and dimensional labels.

4. **Slug question**: "What is the short name for this commons?" Must be kebab-case, ASCII-safe. Used for the repository name (`[slug]-os`), the domain configuration, and all canonical identifiers.

5. **GitHub infrastructure setup**: Using the GitHub CLI (`gh`), the script creates:
   - Labels by dimension: `definition`, `participation`, `proposition`, `production`
   - Labels by type: `build`, `spec`, `deliberation`, `decision`
   - Labels by priority: `critical`, `high`, `normal`
   - A project board with columns matching the operational cadence
   - Milestones matching the commons' first planning horizon
   - GitHub Pages configuration (private for intranet, with optional public site)

6. **Agent configuration**: Writes the four agent configurations to `AGENT.md` based on the selected domain and locale. Each agent gets its dimensional mandate, responsibilities, and standing instructions in the configured locale.

7. **Upstream remote**: Adds the Commons OS template as a remote named `upstream`, enabling the commons to selectively pull improvements from the template as it evolves. This is optional — the founder can decline the upstream connection for fully independent operation.

8. **Verification**: The script runs a verification check — confirming that all infrastructure was created successfully, all configuration files are valid, and the publishing pipeline builds without errors. The output is a summary of what was created and a link to the first governance issue (auto-created): "Define your purpose — complete L1 of the blueprint."

**Step 3: Handle the fork path.** For intentionally public commons, document the fork alternative:

| Criterion | Template (recommended) | Fork |
|---|---|---|
| Visibility | Private by default | Public (matches original) |
| Git history | Clean (no template history) | Full history of template |
| Upstream connection | Manual (add remote) | Automatic (fork relationship) |
| Independence | Full | Linked to original |
| Use case | Most commons | Intentionally public, community-visible |

The fork path skips the template instantiation and proceeds directly to `setup.sh`, which detects that it is running in a fork and adjusts accordingly (e.g., does not add an upstream remote, since the fork relationship already provides it).

**Step 4: Document the post-setup first steps.** The setup script ends with a clear list of recommended first actions:

1. Complete L1 of the blueprint (identity and purpose) — the auto-created issue links to the template.
2. Invite the first board members (if not a solo founder).
3. Configure the MCP endpoints in `.commons/config.yml` (if using the knowledge service).
4. Run the first deliberation: "Is our purpose well-defined?" — using the four-seat governance model (see pat_01kkhc8hd2asfzdp56q17jjz2h).

**Step 5: Build the upstream update mechanism.** For template-created commons that add the upstream remote, provide a documented workflow for pulling improvements:

```bash
# Fetch latest from the Commons OS template
git fetch upstream

# Review what changed
git log upstream/main --oneline -10

# Selectively merge improvements (never blind merge)
git cherry-pick <commit-hash>
```

The principle is selective adoption: the commons pulls improvements it wants and ignores changes that do not fit its context. This is governance, not automation — every upstream change adopted is a conscious decision.

---

### Section 5: Consequences

**What this pattern creates:**

A commons that is operational from minute one. The founder's first interaction with the system is not infrastructure configuration — it is purpose definition. The governance structure is already in place: labels exist, the board is configured, agent seats are ready, the publishing pipeline builds. The founder can immediately start the work that matters: articulating purpose, building community, designing propositions, producing value.

The pattern also creates consistency across the commons network. Every Commons OS instance shares the same foundational structure — the same dimensional labels, the same governance infrastructure, the same agent seat architecture. This consistency enables interoperability: patterns, tools, and practices developed in one commons transfer to another because the structural conventions are shared. The template is the mechanism through which the Commons OS achieves network effects.

For the broader community, the pattern lowers the barrier to entry dramatically. Creating a commons is no longer an expert activity requiring months of governance design. It is accessible to anyone who can answer four questions: What language? What purpose? What domain? What name? The expertise is encoded in the template; the founder provides the context.

**What this pattern risks:**

Template dependency — the risk that commons created from the template never customise their governance beyond the defaults. The defaults are good starting points, not final configurations. A commons that runs on unmodified defaults indefinitely is not governed — it is merely instantiated. The mitigation is the blueprint: the nine-layer boot sequence requires the founder to engage with each layer of governance, adapting the defaults to their specific context.

Template drift — the risk that the upstream template evolves in directions that do not serve all commons equally. If the template maintainers (cloudsters, as stewards) make opinionated changes, downstream commons that pull those changes may find their configurations overwritten. The mitigation is the selective adoption principle: upstream changes are cherry-picked, never blind-merged. And the upstream connection is optional — a commons can disconnect entirely if it outgrows the template.

Over-automation — the risk that the setup script does so much that the founder does not understand what was created. If the founder cannot explain why their project board has these specific labels or why their agents have these specific mandates, they cannot govern effectively. The mitigation is the narrated setup: the script explains each step as it executes, telling the founder what it is creating and why. The setup is automated but not opaque.

---

### Section 6: Known Uses

**create-react-app (2016-present).** Facebook's scaffolding tool for React projects established the modern standard for project generators. A single command (`npx create-react-app my-app`) produces a fully configured React project with build system, test runner, development server, and deployment pipeline. The tool encodes Facebook's opinions about project structure as defaults — developers can "eject" to customise, but most never need to. The Commons OS setup chain follows the same principle: opinionated defaults that work out of the box, with full customisation available when needed.

**Ruby on Rails convention over configuration (2004-present).** Rails' founding principle — convention over configuration — is the philosophical ancestor of this pattern. Rails generates project structure, database schemas, and routing configurations based on naming conventions rather than requiring explicit configuration for every component. The developer who follows the conventions gets a working application with minimal setup. The Commons OS extends this principle from code to governance: follow the conventions and get a working commons with minimal setup.

**GitHub Template Repositories (2019-present).** GitHub's template repository feature allows any repository to be marked as a template, enabling one-click creation of new repositories with the same file structure. This is the platform mechanism that the Commons OS uses. Template repositories are now standard practice for organisations that maintain consistent project structures across teams — the Commons OS applies the same mechanism to consistent governance structures across commons.

**Yeoman generators (2012-present).** Yeoman provided a framework for building custom project scaffolding tools — generators that ask questions and produce configured project structures. The Commons OS setup script is architecturally similar to a Yeoman generator: an interactive questionnaire that produces a configured environment. The difference is scope: Yeoman generates code projects; the setup chain generates governed commons.

**Cookiecutter (Python, 2013-present).** The Python community's project templating tool, Cookiecutter, uses Jinja2 templates and a `cookiecutter.json` configuration to generate project directories from templates. It popularised the concept of templated project creation in the Python ecosystem and has been adopted across languages. Its template variable approach (ask questions, substitute answers into templates) is the same mechanism the Commons OS setup script uses for generating locale-specific content and agent configurations.

---

### Section 7: Cognitive Era

The Cognitive Age transforms the setup chain from a script that generates files into an intelligent boot sequence that converses with the founder. Instead of a command-line questionnaire, the setup sequence can be a conversation with the Purpose Agent:

"Welcome. I am your Purpose Agent — I will help you set up your commons. Let me start with the most important question: In welcher Sprache arbeitest du?"

The agent guides the founder through each setup step with contextual explanation, adapts the questions based on previous answers (a Life-domain commons gets different follow-up questions than a Business-domain commons), and generates the blueprint's first layer from the founder's purpose statement rather than leaving it as a blank template.

This conversational setup has two advantages. First, it is more accessible — the founder does not need to understand bash scripting or YAML configuration. They answer questions in natural language and the agent translates their answers into infrastructure. Second, it is more intelligent — the agent can identify gaps in the founder's purpose statement, suggest domain-appropriate value stream families, and flag potential governance considerations that the founder might not have thought of.

The risk in the Cognitive Age is the illusion of completeness. A conversational setup that feels thorough may lead the founder to believe the commons is fully configured when it is only bootstrapped. The mitigation is the blueprint cadence: the setup creates the initial infrastructure, but the nine-layer blueprint requires ongoing engagement across multiple sessions. The setup is the first five minutes; the blueprint is the first five weeks.

Another Cognitive Age possibility is the template that learns. As more commons are created from the template, the patterns of customisation can inform template improvements. If 80% of German-language commons change a specific governance label, perhaps the German locale should include that change by default. This feedback loop — from downstream customisation back to upstream template improvement — is the mechanism through which the Commons OS evolves based on collective practice rather than individual opinion.

---

### Section 8: Vitality

**Signs of life:**

A healthy setup chain produces commons that are distinct from each other despite sharing the same template. The purpose is different, the locale is different, the domain is different, the community is different — but the governance infrastructure is consistent. This is the sign that the template is serving as a seed, not as a mould: same genome, different expression.

The strongest vitality signal is the time from "I want to start a commons" to "I am governing a commons." If that time is measured in minutes rather than weeks, the setup chain is working. If the founder's first governance issue is created on the same day they decided to start — rather than after weeks of infrastructure setup — the pattern has fulfilled its promise.

Another signal is the customisation ratio: how much of the template defaults does a typical commons modify after setup? A healthy ratio is moderate — enough customisation to show that the founder is engaging with the governance structure, not so much that the template provided no value. If commons routinely modify 80% of the defaults, the defaults need improvement. If they modify 0%, they are not governing — they are using.

The deepest signal is whether commons created from the template feel alive after their first cadence cycle. The setup chain produces infrastructure; the question is whether that infrastructure becomes inhabited. Do issues get created and resolved? Do deliberations happen? Do agents hold their seats? Does the blueprint progress beyond L1? If the commons is active after one cycle, the setup chain succeeded in its deeper purpose: not just creating infrastructure, but initiating the practice of governance.

**Signs of decay:**

Decay in the setup chain takes two forms. The first is template rot: the template does not keep pace with the evolving understanding of commons governance. New patterns are developed, new agent configurations are refined, new locale files are contributed — but the template still reflects the state of six months ago. The mitigation is a template maintenance cadence: a scheduled review (quarterly at minimum) that asks "what has the commons network learned that should be reflected in the template?"

The second form of decay is setup abandonment: founders run the setup script and then never engage with the governance infrastructure it created. The labels exist but no issues use them. The project board has columns but no cards. The agent configurations are present but no deliberations reference them. This signals that the setup chain created infrastructure without creating understanding — the founder got a commons but does not know how to govern it. The recovery is the onboarding sequence: the first auto-created issue should not just say "define your purpose" but should guide the founder through their first governance act with enough context to make the infrastructure meaningful.
