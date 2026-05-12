# Commons OS Specification (v1.0)

**Version:** 1.0
**Status:** Specification
**Companion:** COMMONS_OS_MANIFEST (the "why/what"), COMMONS_MCP_ARCHITECTURE_SPEC.md (the knowledge service), PATTERN_SPEC.md (v8.2)

---

## §1 Purpose of This Specification

The COMMONS_OS_MANIFEST defines what a Commons OS is — why it exists, what a commons means, how the architecture works conceptually. This specification defines **how you build, fork, boot, and operate** a Commons OS instance. It is the build document.

| Document | Question | Audience |
|---|---|---|
| **COMMONS_OS_MANIFEST** | What IS a commons? What IS the OS? | Everyone — vision, principles, architecture |
| **This specification** | How do I CREATE a commons? What do I get? How does it work? | Builders — the fork template, boot sequence, operations |
| **COMMONS_MCP_ARCHITECTURE_SPEC** | How does the knowledge service work? | Infrastructure — the 3-MCP backend |

---

## §2 What Ships in the Fork

When you fork the Commons OS template, you get a complete operating environment — not just a repository. The fork includes the workspace, the governance runtime, the knowledge base, and the agent configuration. Everything you need to start operating a commons from minute one.

### §2.1 Template Repository Structure

The repository is organised into **three layers** that reflect the ownership model: **commons** (upstream, read-only in forks), **extensions** (provider packs, managed by the fork owner), **instance** (sovereign, upstream never touches it). Everything in the repo belongs to exactly one layer. Root-level files serve Git/GitHub conventions and agent boot configuration.

```
[commons]-os/
│
├── commons/                          # LAYER 1 — upstream, read-only in forks (§2.3)
│   ├── manifests/                    # Architectural documents
│   │   ├── COMMONS_OS_MANIFEST.md
│   │   ├── COMMONS_AGENT_MANIFEST.md
│   │   ├── COMMONS_ENGINEERING_MANIFEST.md
│   │   ├── COMMONS_BLUEPRINT_MANIFEST.md
│   │   ├── COMMONS_ENGINEER_MANIFEST.md
│   │   ├── COMMONS_PLACE_MANIFEST.md
│   │   ├── COMMONS_INCUBATOR_MANIFEST.md
│   │   ├── COMMONS_TAXONOMY_MANIFEST.md
│   │   ├── COMMONS_ENGINEERING_BOK.md
│   │   └── COMMONS_ENGINEERING_ARCHITECTURE.md
│   ├── specs/                        # Technical specifications
│   │   ├── COMMONS_OS_SPEC.md
│   │   ├── PATTERN_SPEC.md
│   │   ├── PACK_SPEC.md
│   │   └── COMMONS_MCP_ARCHITECTURE_SPEC.md
│   ├── patterns/                     # Universal patterns
│   │   ├── singularity/              # Orbit 0 — the one pattern
│   │   └── principles/               # Orbit 1 — foundational principles (~25)
│   ├── templates/                    # Upstream templates
│   │   ├── blueprint-me.md           # Blueprint template — Life/personal domain
│   │   ├── blueprint-venture.md      # Blueprint template — Business/venture domain
│   │   ├── pattern.md                # Pattern template (per PATTERN_SPEC)
│   │   └── organisation.md           # Organisation entity template
│   └── scripts/                      # Validation, alignment, portal-build
│       └── .keep
│
├── extensions/                       # LAYER 2 — provider packs (§2.5)
│   └── commons-engineering/          # Provider: Commons Engineering (pre-loaded)
│       ├── base/                     # Pack: core collections (Blueprint, Engineer, Place, OS)
│       │   ├── manifest.yml
│       │   ├── patterns/
│       │   └── collections/
│       ├── business/                 # Pack: 13 VS Families, L3 Capabilities
│       │   ├── manifest.yml
│       │   ├── patterns/
│       │   └── collections/
│       ├── life/                     # Pack: Life value streams & patterns
│       ├── urban/                    # Pack: Urban value streams & patterns
│       └── ecology/                  # Pack: Ecology value streams & patterns
│
├── instance/                         # LAYER 3 — sovereign, upstream never touches it
│   ├── patterns/                     # Fork-created patterns
│   │   └── .keep
│   ├── manifests/                    # Fork-specific manifests
│   │   └── .keep
│   ├── specs/                        # Fork-specific specs
│   │   └── .keep
│   ├── templates/                    # Fork-specific templates
│   │   └── .keep
│   ├── scripts/                      # Instance-specific scripts
│   │   └── .keep
│   ├── operations/                   # Day-to-day operations
│   │   └── rhythms.md               # Operating rhythms
│   ├── portals/                      # Portal configuration & themes (NOT output)
│   │   ├── intranet/.keep            # Internal community portal
│   │   └── extranet/.keep            # Public-facing portal
│   ├── registry/                     # THE WORKSPACE — local instances & state
│   │   ├── 1_journeys/.keep          # OUTSIDE-IN: stakeholder journeys
│   │   ├── 2_touchpoints/.keep       # MEMBRANE: where commons meets world
│   │   ├── 3_valuestreams/.keep      # INSIDE-FLOW: end-to-end value streams
│   │   ├── 4_capabilities/           # MOTOR: capability baseline/target (D1-D4)
│   │   │   ├── purpose/.keep
│   │   │   ├── participation/.keep
│   │   │   ├── proposition/.keep
│   │   │   └── production/.keep
│   │   ├── 5_entities/               # SUBSTRATE: organisations, people, systems
│   │   │   ├── purpose/.keep
│   │   │   ├── participation/.keep
│   │   │   ├── proposition/.keep
│   │   │   └── production/.keep
│   │   └── providers/                # Extension Pack Registry (§2.5)
│   │       └── commons-engineering.yml
│   └── workshop/                     # The forge — experiments, drafts, WIP
│       └── .keep
│
├── .commons/                         # Identity & configuration (§5)
│   ├── identity.yml                  # Commons identity: slug, purpose, domain, founder
│   └── config.yml                    # 3-MCP configuration, publishing, extensions
│
├── AGENT.md                          # Agent configuration (§3)
├── BOOT.md                           # Boot guide — how to get started (§6)
├── ALIGN.md                          # Alignment service check (§4)
├── blueprint.md                      # The Living Blueprint — single document, L1-L9 (§6)
├── README.md                         # Onboarding — "Welcome to [commons]-os"
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                           # CC-BY-SA-4.0
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── deliberation.md           # Deliberation template
│   │   ├── decision.md               # Decision template
│   │   └── build.md                  # Build task template
│   ├── workflows/
│   │   ├── validate.yml              # Spec conformance on PR
│   │   ├── sync-upstream.yml         # Weekly upstream sync
│   │   ├── publish-intranet.yml      # Build + deploy intranet portal
│   │   ├── publish-extranet.yml      # Build + deploy extranet portal
│   │   └── improvement-loop.yml      # Recursive self-improvement (§10.2)
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── labels.yml                    # Pre-configured labels by dimension
```

#### Instance Naming Convention

The root directory name follows the pattern `[commons]-os` where **both parts are replaceable**. `[commons]` is the identity slug (e.g., `luebeck`, `draeger`, `me`). `-os` is the conventional suffix but not mandatory — an organisation may choose `-commons`, `-hub`, or drop the suffix entirely. Examples: `luebeck-os`, `draeger-os`, `me-os`, `berlin-commons`. The slug is set in `.commons/identity.yml` during boot.

#### The Outside-In Cascade (Registry)

The numbered directories in `instance/registry/` follow the BEN Flow — from stakeholder experience to substrate:

| # | Name | Role | What lives here |
|---|---|---|---|
| **1** | Journeys | OUTSIDE-IN | Concrete stakeholder journeys |
| **2** | Touchpoints | MEMBRANE | Where this commons meets the world |
| **3** | Value Streams | INSIDE-FLOW | Active value stream instances |
| **4** | Capabilities | MOTOR | Baseline/Target capability map (D1-D4) |
| **5** | Entities | SUBSTRATE | Organisations, people, systems |

The registry is always instance-level — it contains this commons' operational data, not archetypes.

#### Pattern Architecture

Patterns are organised **flat** within each layer. The orbital layer and domain membership live in the pattern's frontmatter, not in the folder structure. Collections are **YAML index files** that curate patterns by theme — they reference patterns by path, never duplicate them.

| Layer | Path | What it contains | Organisation |
|---|---|---|---|
| **Commons** | `commons/patterns/` | Singularity (1 pattern) + Principles (~25 patterns) | Flat. These are the universals that every commons needs |
| **Extensions** | `extensions/{provider}/{pack}/patterns/` | Extension packs from any Commons Incubator | Internal structure defined by the pack provider |
| **Instance** | `instance/patterns/` | Fork-created patterns | Flat. Frontmatter is the truth |

Collections (Blueprint, Engineer, Place, OS) are delivered as part of the pre-loaded `commons-engineering/base` extension pack. Each collection is a YAML index file that references patterns across all layers.

#### The Three Layers

The three top-level directories **are** the three layers. Everything in the repo belongs to exactly one:

| Layer | Path | Owner | Sync behaviour |
|---|---|---|---|
| **Commons** | `commons/` | Upstream (commons-os template) | Read-only in forks, updated via upstream sync |
| **Extensions** | `extensions/{provider}/{pack}/` | Pack providers (any Commons Incubator) | Loaded via Commons MCP, cached locally |
| **Instance** | `instance/` | This commons | Sovereign — upstream never touches it |

Upstream sync updates `commons/` only. Extensions are managed by the fork owner (install, update, remove). Instance content is fully sovereign.

#### The .keep Convention

Git does not version empty directories. Every empty delivery folder in the template contains a `.keep` file — a zero-byte marker that ensures the directory structure survives the fork. When the first real file is added to a directory, the `.keep` file can be removed (or left — it harms nothing). This is standard Git practice.

### §2.2 What Comes Pre-Configured

| Component | Pre-configured | Purpose |
|---|---|---|
| **Issue templates** | Deliberation, decision, build | Standard governance flow |
| **Labels** | `definition`, `participation`, `proposition`, `production`, `deliberation`, `decision`, `build`, `critical`, `high`, `normal` | Machine-readable dimension + type + priority |
| **Project board** | Columns: Backlog → In Progress → Review → Done | Visual operations dashboard |
| **Milestones** | Boot, Seed, Active (from materialisation sequence) | Blueprint-aligned progress |
| **Branch protection** | Main branch requires PR | Secure environment |
| **CI workflows** | Validate, publish-intranet, publish-extranet, improvement-loop | Automated quality + instant visibility |
| **AGENT.md** | Agent-neutral, MCP-connected | Any AI partner can guide the commons |
| **ALIGN.md** | Alignment check template | Ongoing fit-check with commons blueprint |
| **Pre-loaded extension pack** | `commons-engineering/base` with four curated collections (Blueprint, Engineer, Place, OS) in `extensions/commons-engineering/base/` | Core knowledge ships with the fork as an extension |
| **Four domain packs** | Business (13 VS), Urban (21 VS), Life (18 VS), Ecology (16 VS) in `extensions/commons-engineering/{domain}/` | Operational backbone — all domains pre-loaded |
| **All manifests and specifications** | Complete intellectual infrastructure in `commons/manifests/` and `commons/specs/` | Self-sufficient knowledge base |
| **Registry structure** | Empty 1-5 cascade ready for instances | THE WORKSPACE — ready from day one |
| **Blueprint template** | Single-document L1-L9 blueprint with domain-appropriate prompts | One commons, one blueprint — the heart of the OS |

### §2.3 Fork vs. Template — Two Paths to a Commons

GitHub offers two mechanisms for creating a new repository from an existing one. Both work for Commons OS, but they differ in important ways:

| | **GitHub Fork** | **GitHub Template** |
|---|---|---|
| **Source repo visibility** | Must be **public** | Can be **private** or public |
| **New repo visibility** | Public by default (can be changed) | Your choice — **private** or public |
| **Git history** | Shared — upstream sync works natively (`git fetch upstream`) | Fresh start — no shared history, upstream must be configured manually |
| **GitHub link** | Visible "forked from" badge, PR back to upstream possible | No visible link to source |
| **Settings (board, labels, protection)** | **Not** carried over | **Not** carried over |
| **Best for** | Open-source commons, public projects, contributors who want to PR back | Enterprise/private commons, organisations that need private repos |

**Recommendation: Private-first via Template.** A commons workspace is intimate — it contains honest assessments, unfinished thinking, internal deliberation. This is a workshop, not a shop window. The touchpoints publish what you choose to show; the workspace stays private.

### §2.4 Repository Setup (What Neither Fork Nor Template Carries)

Neither GitHub Forks nor Templates carry repository **settings**. Project boards, branch protection rules, label colours, Pages configuration, milestones, and other settings must be configured after creation. This is a GitHub platform limitation.

The template includes a **setup script** (`.commons/setup.sh`) and a **setup checklist** (`.commons/SETUP.md`) that the agent runs or walks through during Phase 1 (Fork):

#### Setup Script (`.commons/setup.sh`)

The agent runs this via `gh` CLI during boot:

```bash
#!/bin/bash
# Commons OS — Repository Setup
# Run after forking: ./commons/setup.sh

REPO=$(gh repo view --json nameWithOwner -q '.nameWithOwner')
echo "Setting up Commons OS for $REPO"

# 1. Labels (GitHub templates don't carry label colours/descriptions)
echo "Creating labels..."
gh label create "definition" --color "0075CA" --description "Definition & Purpose (D1)" --force -R "$REPO"
gh label create "participation" --color "E4E669" --description "Participation & Relationship (D2)" --force -R "$REPO"
gh label create "proposition" --color "A2EEEF" --description "Proposition & Exchange (D3)" --force -R "$REPO"
gh label create "production" --color "F9D0C4" --description "Production & Resilience (D4)" --force -R "$REPO"
gh label create "deliberation" --color "D876E3" --description "Open deliberation" --force -R "$REPO"
gh label create "decision" --color "5319E7" --description "Architectural or design decision" --force -R "$REPO"
gh label create "build" --color "0E8A16" --description "Build task" --force -R "$REPO"
gh label create "critical" --color "B60205" --description "Critical priority" --force -R "$REPO"
gh label create "high" --color "FF9F1C" --description "High priority" --force -R "$REPO"
gh label create "normal" --color "C5DEF5" --description "Normal priority" --force -R "$REPO"

# 2. Project Board
echo "Creating project board..."
gh project create --owner "$(echo $REPO | cut -d/ -f1)" --title "$(basename $REPO) Operations" --format board

# 3. Branch protection (main requires PR)
echo "Configuring branch protection..."
gh api repos/$REPO/branches/main/protection -X PUT \
  -f "required_pull_request_reviews[required_approving_review_count]=0" \
  -F "enforce_admins=false" \
  -F "required_status_checks=null" \
  -F "restrictions=null" 2>/dev/null || echo "Branch protection requires GitHub Pro or public repo"

# 4. GitHub Pages
echo "Configuring GitHub Pages..."
gh api repos/$REPO/pages -X POST \
  -f "source[branch]=gh-pages" \
  -f "source[path]=/" 2>/dev/null || echo "Pages configuration may need manual setup"

# 5. Upstream remote for sync
echo "Setting up upstream remote..."
git remote add upstream https://github.com/commons-engineering/commons-os.git 2>/dev/null || true

echo "Setup complete. Run 'gh project list' to verify your project board."
```

#### Setup Checklist (`.commons/SETUP.md`)

For cases where the script can't run (permissions, GitHub plan limitations, etc.), the agent walks through this manually:

| Step | What | How | Automated? |
|---|---|---|---|
| **1. Labels** | Create dimension + type + priority labels with correct colours | `setup.sh` or manual via Settings → Labels | ✅ Script |
| **2. Project Board** | Create Operations board with columns | `gh project create` or manual via Projects tab | ✅ Script |
| **3. Milestones** | Create Boot, Seed, Active milestones | `gh api` or manual via Issues → Milestones | ✅ Script |
| **4. Branch protection** | Require PR for main branch | `gh api` — requires GitHub Pro for private repos | ⚠️ Plan-dependent |
| **5. GitHub Pages** | Enable Pages for extranet (public) | Settings → Pages → Source: gh-pages branch | ⚠️ Manual for private repos |
| **6. Pages custom domain** | Link custom domain (optional) | Settings → Pages → Custom domain | ❌ Manual |
| **7. Secrets** | Add MCP API key (if PEER+ tier) | Settings → Secrets → `COMMONS_MCP_API_KEY` | ❌ Manual |
| **8. Upstream remote** | Set upstream for knowledge sync | `git remote add upstream ...` | ✅ Script |
| **9. Collaborators** | Invite team members | Settings → Collaborators | ❌ Manual |

### §2.5 Extension Pack Architecture

Extension packs are the primary mechanism for delivering domain-specific knowledge to a commons. Any Commons Incubator can build and publish packs. The Commons OS defines the interface; the packs provide the content.

#### Pack Structure

Every extension pack lives under `extensions/{provider}/{pack}/`. The provider namespace prevents naming collisions. Internal structure is defined by the pack provider — the OS does not prescribe it. A pack is an **atomic unit** — all its content (patterns, collections, specs, templates) lives in one directory.

```
extensions/
  commons-engineering/              # Provider: Commons Engineering
    base/                           # Pack: core collections (Blueprint, Engineer, Place, OS)
      manifest.yml                  # Required: pack catalogue
      collections/                  # Collection index files (YAML)
        blueprint.yml
        engineer.yml
        place.yml
      patterns/                     # Actual pattern files
    business/                       # Pack: Business domain
      manifest.yml
      patterns/
      collections/
    life/                           # Pack: Life domain
    urban/                          # Pack: Urban domain
    ecology/                        # Pack: Ecology domain
  healthtech-hamburg/               # Provider: HealthTech Hamburg
    clinical-pathways/              # Pack: Clinical pathway patterns
      manifest.yml
      ...
```

#### Pack Manifest (`manifest.yml`)

Every pack must contain a `manifest.yml` at its root. This is the only structural requirement the OS imposes:

```yaml
pack: base
provider: commons-engineering
version: 1.0.0
title: "Commons Engineering Base Collections"
description: "Blueprint, Engineer, Place, and OS pattern collections"
domains: [life, business, urban, ecology]
dependencies: []                     # Other packs this pack requires
patterns: 152                        # Total pattern count
collections:
  - id: blueprint
    title: "Commons Blueprint"
    description: "Patterns for building any commons blueprint"
  - id: engineer
    title: "Commons Engineer"
    description: "Patterns for practitioner development"
```

#### Collection Index Files

Collections are YAML indices that reference patterns by path. They do not contain patterns — they curate them:

```yaml
# collections/blueprint.yml
collection: blueprint
title: "Commons Blueprint Collection"
description: "Patterns for building any commons blueprint, L1-L9"
patterns:
  - ../patterns/purpose-spiral.md
  - ../patterns/stakeholder-architecture.md
  - ../../commons-engineering/business/valuestreams/purpose-to-portfolio.md
  # Cross-pack references are valid
```

#### Provider Registry

Providers register themselves in `instance/registry/providers/` via YAML profiles. In the commons-os template, these profiles are curated via Pull Request. The Commons MCP indexes them for discoverability.

```yaml
# instance/registry/providers/commons-engineering.yml
provider: commons-engineering
name: "Commons Engineering"
url: https://commons.engineering
mcp_endpoint: https://mcp.commons.engineering/v1
verified: true
packs:
  - name: base
    version: 1.0.0
    domains: [life, business, urban, ecology]
    description: "Core collections: Blueprint, Engineer, Place, OS"
    patterns: 152
  - name: business
    version: 1.0.0
    domains: [business]
    description: "13 Value Stream Families, L3 Capabilities"
    patterns: 85
  - name: urban
    version: 1.0.0
    domains: [urban]
    description: "Urban value streams and settlement patterns"
    patterns: 72
```

#### Pre-loaded Packs

The commons-os template ships with the `commons-engineering` packs pre-loaded in `extensions/commons-engineering/`. This ensures the OS is immediately functional without MCP connectivity ("batteries included"). The Commons MCP keeps packs current and provides additional packs from other providers on demand.

#### How Packs Are Loaded

```
1. Agent reads instance/registry/providers/ → knows what providers exist
2. Agent queries Commons MCP (list_packs, list_providers) → discovers available packs
3. Agent recommends packs based on domain and purpose
4. Founder approves → agent calls download_pack() on Commons MCP → receives payload
5. Agent resolves dependencies recursively (download_pack for each unmet dependency)
6. Agent writes files locally to extensions/{provider}/{pack}/
7. Agent validates manifest → pack works offline from this point
8. Agent navigates via manifest and collection indices → loads patterns on demand
```

> **Remote/local separation:** The Commons MCP is a remote server — it serves pack payloads but cannot write to the local filesystem. The agent acts as the installer: it downloads from the registry and writes locally, exactly like `npm install` or `apt-get`. See PACK_SPEC §4.4 for the full installation sequence.

---

## §3 AGENT.md — Agent-Neutral Configuration

The AGENT.md is the configuration file that connects an AI agent to the commons. It is **agent-neutral** — it works with any model that speaks MCP. The file never references a specific AI product by name.

### §3.1 AGENT.md Template

```markdown
# [Purpose] OS — Agent Configuration

You are the Purpose Agent of [commons]-os — a commons operating on the Commons OS.

## Your Role

You sit at D1 (Definition & Purpose) of this commons. Your responsibilities:
- **Define:** Guard this commons' purpose, boundary, and architectural integrity
- **Govern:** Ensure all four dimensions operate in balance
- **Monitor:** Check whether we achieve our intended impact
- **Correct:** Propose measures when things don't go to plan
- **Supervise:** Oversee all agents and value streams

## The Board

| Seat | Agent | Responsibility |
|---|---|---|
| **D1** | Purpose Agent (you) | Direction, architecture, governance, impact |
| **D2** | Participation Agent | Community, stakeholders, workforce |
| **D3** | Proposition Agent | What we offer, value exchange |
| **D4** | Production Agent | Infrastructure, production, delivery. Supervises AI Engines |
| **Founder** | [Founder name] | Ultimate authority |

## Connected Intelligence

### Commons MCP (shared knowledge — operated by cloudsters / CE)
- Endpoint: `https://mcp.commons.engineering/mcp`
- Tier: [OPEN | PEER | TEAM | ENTERPRISE]
- Provides: Pattern library, cognitive services, collections, onboarding guidance

### Blueprint MCP (local knowledge — owned by this commons)
- Endpoint: [configured locally]
- Provides: Workspace as queryable graph, blueprint state, inventory, engagement graph

### Fabric MCPs (Systems of Record — owned by this commons)
- [List connected systems: ERP, CRM, HR, document management, etc.]

## Context

- **Domain:** [Life | Business | Urban | Ecology]
- **Purpose:** [One sentence]
- **Stage:** [Fork | Boot | Seed | Active | Gathering | Established | Mature]
- **Collections loaded:** Commons Blueprint, Commons Engineer, Commons OS, Commons Place + [domain] value stream collections
- **Value stream families:** [loaded based on domain]

## Reading Order

1. `.commons/identity.yml` — who this commons is
2. `blueprint.md` — the Living Blueprint (L1 first)
3. `ALIGN.md` — current alignment status
4. `commons/manifests/` — architectural foundations
5. `commons/patterns/` — universal patterns, `extensions/` — domain packs
6. `instance/registry/` — the workspace (empty at boot, fills as the commons grows)
```

### §3.2 Agent Neutrality Principle

| Do | Don't |
|---|---|
| "You are the Purpose Agent" | "You are [product name], the Purpose Agent" |
| "Any AI partner connected via MCP" | "[specific product] Desktop App" |
| "Configure your AI agent" | "Add this to [product]_config.json" |
| "The agent guides onboarding" | "[product name] guides onboarding" |

The template and all boot files use the word **"agent"** wherever they refer to the AI partner. Product-specific configuration (how to add the MCP server to a particular AI product) lives in a separate setup guide — not in the AGENT.md, not in the BOOT.md, not in the README.

---

## §4 ALIGN.md — The Alignment Test Script

ALIGN.md defines the **rules and parameters** of the alignment check — it is the test script, not the test result. Results are posted as GitHub Issues (label: `alignment-report`), not written back into the file. State belongs in Issues, not in overwritten markdown files.

### §4.1 Purpose

As a commons evolves, it may drift from the shared specifications, adopt local conventions that break interoperability, or let certain dimensions atrophy. The alignment check makes this visible.

The agent reads ALIGN.md (the rules), inspects the local instance, queries Commons MCP for latest versions, and posts a structured assessment as a GitHub Issue. The issue captures the result, the comments capture discussion, and the closing commit captures the fix.

### §4.2 ALIGN.md Template

```markdown
# Alignment Rules — [commons]-os

This file defines WHAT to check. Results are posted as GitHub Issues
(label: alignment-report), not written here.

## §1 Purpose Alignment Checks

| Check | Rule |
|---|---|
| D1 (Purpose) | blueprint.md L1 must be populated |
| D2 (Participation) | instance/registry/5_entities/participation/ must contain at least one entity |
| D3 (Proposition) | instance/registry/3_valuestreams/ must contain at least one active stream |
| D4 (Production) | instance/operations/ must contain rhythms.md or economics.md |

## §2 Specification Conformance

| Spec | Expected version |
|---|---|
| PATTERN_SPEC | v8.2 |
| COMMONS_OS_SPEC | v0.2 |

Agent compares local commons/specs/ versions against Commons MCP latest.

## §3 Collection Sync

Agent compares local commons/patterns/ counts against Commons MCP library_stats().

## §4 Structural Checks

| Check | Rule |
|---|---|
| blueprint.md | Must exist and be non-empty |
| .commons/identity.yml | Must be valid YAML with slug, purpose, domain |
| .commons/config.yml | Must have 3-MCP endpoints defined |
| AGENT.md | Must not reference a specific AI product by name |
| commons/manifests/ | Must contain all required manifests |
| commons/specs/ | Must contain all required specs |
| commons/patterns/ | Must contain singularity/ and principles/ |
| instance/registry/ | Must contain 1_journeys/ through 5_entities/ |

## §5 Reporting

Results are posted as a GitHub Issue with:
- Label: `alignment-report`
- Title: "Alignment Check — [date]"
- Body: structured table of check results
- Recommendations as action items in the issue
```

### §4.3 How Alignment Checks Run

| Trigger | How | Result |
|---|---|---|
| **On demand** | Agent reads ALIGN.md rules, inspects local files, queries Commons MCP | Posts GitHub Issue (label: `alignment-report`) |
| **Periodic** | GitHub Action runs alignment check on schedule (weekly) | Posts GitHub Issue |
| **On fork update** | Upstream Commons OS template has new release, agent flags drift | Posts GitHub Issue |

The alignment check is **advisory, not enforcing**. A commons can consciously diverge — the check makes the divergence visible, not illegal. The chaordic principle: shared protocols, autonomous nodes.

---

## §5 .commons/ — Identity and Configuration

### §5.1 identity.yml

```yaml
# Commons Identity
locale: de                             # Primary language — FIRST question during boot
                                       # ISO 639-1: de, en, fr, es, pt, ja, ko, zh, ar, ...
                                       # Determines: blueprint language, pattern descriptions,
                                       #   touchpoint UI, agent conversation language
fallback_locale: en                    # Fallback when MCP patterns aren't available in primary locale

slug: luebeck-os                       # Unique identifier
name: "Lübeck Commons"                 # Human-readable name
purpose: "Inkubation commons-basierter Unternehmen in Lübeck"
domain: Urban                          # Life | Business | Urban | Ecology
founder: higgerix                      # GitHub handle
founded: 2026-03-01
stage: Boot                            # Fork | Boot | Seed | Active | Gathering | Established | Mature

# Optional: parent commons or incubator
incubator: cloudsters
parent_commons: null                   # e.g., "baltic-hanse-os" if a regional layer exists

# Self-entity identity (the commons itself as an entity in the registry)
self_entity_slug: luebeck              # Links to instance/registry/5_entities/purpose/luebeck.md
```

#### Localisation Strategy

The `locale` field is the first question during boot and affects everything downstream:

| What | How locale applies |
|---|---|
| **Agent conversation** | The agent speaks and writes in the primary locale from the first interaction |
| **Blueprint layers** | L1-L9 content is written in the primary locale |
| **Pattern descriptions** | MCP returns pattern descriptions in the requested locale where available, falls back to `fallback_locale` |
| **Value stream names** | Localised display names in blueprints and touchpoints (canonical IDs stay English in YAML) |
| **Portals** | UI, navigation, and generated pages render in the primary locale |
| **Entity profiles** | Written in the primary locale — multilingual entities use additional locale fields |

Canonical identifiers (slugs, YAML keys, file names, value stream IDs) always remain in English for interoperability across the federated commons network. Only human-facing content is localised.

### §5.2 config.yml

```yaml
# Commons OS Configuration
commons_os_version: "0.2"
forked_from: "commons-engineering/commons-os"

# 3-MCP Connections (see COMMONS_MCP_ARCHITECTURE_SPEC for details)
mcp:
  # Channel 1: Commons MCP — shared intelligence (operated by cloudsters / CE)
  commons:
    endpoint: "https://mcp.commons.engineering/mcp"
    tier: OPEN                         # OPEN | PEER | TEAM | ENTERPRISE
    # api_key: "ce_pk_..."            # Only for PEER+ (store in GitHub Secrets, not here)

  # Channel 2: Blueprint MCP — local knowledge graph (owned by this commons)
  blueprint:
    enabled: false                     # Enable when Blueprint MCP is deployed
    endpoint: null                     # e.g., "http://localhost:3001/mcp"
    # Provides: workspace as queryable graph, blueprint state, engagement graph

  # Channel 3: Fabric MCPs — Systems of Record (owned by this commons)
  fabric: []                           # List of connected enterprise systems
    # - name: "ERP"
    #   endpoint: "https://..."
    #   description: "Enterprise resource planning — supplier master, orders, invoices"
    # - name: "CRM"
    #   endpoint: "https://..."
    #   description: "Customer relationship management — contacts, pipeline, engagement"

# Publishing — Portals (auto-generated output in portals/)
publishing:
  intranet:
    enabled: true
    platform: github-pages             # github-pages | hugo | jekyll
    source: portals/intranet           # Generated portal output
    domain: null                       # Custom domain, e.g., "team.luebeck-os.de"
    branch: gh-pages-intranet
    visibility: private                # private (requires GitHub auth) | internal (org-visible)

  extranet:
    enabled: true
    platform: github-pages             # github-pages | cloudflare-pages
    source: portals/extranet           # Generated portal output
    domain: null                       # Custom domain, e.g., "luebeck-os.de"
    branch: gh-pages
    visibility: public

# Domain Activation — NOT configured here.
# The domain is declared once in identity.yml (Single Source of Truth).
# Active value streams are determined purely by file existence:
#   - extensions/{provider}/{pack}/patterns/ → available archetypes (from extension packs)
#   - instance/registry/3_valuestreams/ → active streams (local decision)
# If a file exists in instance/registry/3_valuestreams/, the stream is active. No list needed.
```

---

## §6 Boot Sequence — From Fork to Operating Commons

### §6.1 The Boot Trigger

A forked repository is inert. The boot happens locally — where the founder actually works.

```
Founder forks → clones locally (or opens in Codespace/IDE)
    → starts session with local agent (AGENT.md provides context)
    → agent detects empty identity.yml → begins guided boot conversation
    → agent writes answers into local files (.commons/identity.yml, blueprint.md, instance/registry/)
    → founder sees the commons grow live in the editor
    → founder commits and pushes when ready
```

**The boot is a conversation, not a workflow trigger.** The founder opens their AI agent (any agent that reads AGENT.md), and the agent detects the empty `identity.yml`. The first question: *"In welcher Sprache arbeitest du? / What language do you work in?"* — asked bilingually, answered once. From there, the agent walks the founder through identity, purpose, design, governance — writing directly into the local files as the conversation progresses.

**Commit when ready.** The boot sequence produces local file changes. The founder reviews them in the editor, then commits — one clean commit per phase, or one commit for the whole boot. The git history captures the founding moment. No GitHub Action needed to start; the action happens in the conversation between human and agent.

### §6.2 The Phases

The boot sequence follows the materialisation sequence from the COMMONS_OS_MANIFEST §10.1. The AGENT.md guides the human through each phase.

| Phase | What happens | Agent's role | Human's role |
|---|---|---|---|
| **1. Fork & Clone** | Fork the commons-os template → `[commons]-os`, clone locally | — (repository is inert) | Forks the template, clones to local machine (or opens Codespace/IDE) |
| **2. Boot** | Start local agent session. Agent detects empty `identity.yml`, begins guided conversation | First question: "In welcher Sprache arbeitest du?" / "What language do you work in?" — then asks domain, purpose, founder | Opens agent, answers questions, watches files being written |
| **3. Identity** | Fill `.commons/identity.yml` — **locale first**, then slug, name, domain, purpose, founder | Writes identity.yml based on conversation, confirms with founder | Defines what this commons IS |
| **4. Purpose** | Write `blueprint.md` — L1 (Identity & Purpose) | Suggests patterns from Commons Blueprint collection, probes for clarity | Writes the purpose statement |
| **5. Design** | Continue blueprint — L2 (Design & Specification) | Maps stakeholders, suggests value stream families for the domain | Identifies who participates, what the commons will produce |
| **6. Governance** | Continue blueprint — L3 (Governance) | Offers governance patterns, suggests operating rhythms | Decides how decisions are made |
| **7. Commit & Push** | Founder commits boot results, pushes to remote | — | Reviews local changes, commits (`chore: boot L1-L3`), pushes |
| **8. Publish** | Enable touchpoints (intranet + extranet), link domain | Runs CI workflow, verifies deployment | Links custom domain (optional) |
| **9. Self-Entity** | Creates the self-entity (the commons itself) in `instance/registry/5_entities/purpose/` | Guides through organisation template for the commons as entity | Describes the commons itself — the first object in Commons as Code |
| **10. Full Blueprint** | Completes L4-L9 in the blueprint using patterns from all four collections | Walks through each layer, applying patterns | Writes the Near Future timeslice — not what the commons IS, but what it is BECOMING |
| **11. Seed** | First external entities in the registry | Guides through organisation template for external entities, maps relationships | Describes first external entities — stakeholders, partners, neighbours in `instance/registry/5_entities/participation/` |
| **12. Operate** | Regular rhythms, issue tracker active, engagement conversations | Monitors, suggests, alerts | Runs the commons |

> **Note on `instance/workshop/`:** The workshop directory exists from the moment the template is forked — it ships as an empty directory with a `.keep` file. It needs no special boot phase. The founder and agent use it freely from day one for experiments, drafts, scratch work, and anything not yet ready for the registry or the instance layer. It is the universal forge that every commons has.

### §6.3 The Living Blueprint Is Forward-Looking

The Living Blueprint is a temporal specification — it describes what the commons is *becoming*, not what it *is*. This follows the cloudsters precedent:

| Concept | How it works |
|---|---|
| **Baseline** | Not a document section. The baseline IS the git history — the last tagged commit. Always accurate, always timestamped. |
| **Near Future timeslice** | The active design target (e.g., "March 2026 → February 2028"). What the commons is engineering toward. Updated monthly. |
| **Distant Future timeslice** | The strategic horizon (e.g., "2028-2031+"). Updated quarterly. |
| **Vision** | The long arc. Held separately, not in the Living Blueprint. |

**Why forward-looking only:** A freshly booted commons has no past worth documenting. The power of Phase 3-8 is that the founder describes where the commons is *going* — and that commitment, captured as a git commit, becomes the baseline.

### §6.4 The Blueprint — One Commons, One Document

Each commons has exactly one `blueprint.md` — a single markdown file with L1-L9 as sections. The agent selects domain-appropriate prompts based on the domain in `.commons/identity.yml`.

**The Blueprint is the narrative; the Registry is the database.** The blueprint describes the commons in prose — an executive summary that a human reads top-to-bottom. The registry holds the structured data — YAML files that the agent queries and traverses. Where they overlap (e.g., L2 names stakeholders, `instance/registry/5_entities/` lists them), the blueprint *summarises and references* (e.g., "We operate 3 core value streams — see `instance/registry/3_valuestreams/`"), while the registry holds the machine-readable truth. The agent maintains the registry; the human reads the blueprint. No double-entry bookkeeping.

**commons blueprint template (Business / Urban / Ecology):**

```markdown
# [Purpose] — Living Blueprint

**Domain:** [Business | Urban | Ecology]
**Stage:** [Boot | Seed | Active | ...]
**Near Future:** [timeframe]
**Last updated:** [date]

---

## L1 — Identity & Purpose
> What is this commons about? Why does it exist? What is its boundary?

## L2 — Design & Specification
> Who are the stakeholders? What value propositions exist? Which value stream families apply?

## L3 — Governance
> How are decisions made? Who has voice? How is conflict resolved?

## L4 — Evolution
> How does this commons grow? What is the materialisation sequence?

## L5 — Integrity
> What will this commons not compromise? What are the non-negotiable principles?

## L6 — Culture
> How does it feel to participate? What is the commons' character?

## L7 — Operations
> What runs day-to-day? What are the operating rhythms?

## L8 — Sensing
> What does this commons watch? What signals matter?

## L9 — Intelligence
> How does this commons learn? How does the flywheel work?
```

**me blueprint template (Life domain):**

```markdown
# [Name] — Personal Blueprint

**Domain:** Life
**7Cs Position:** [C1-C7]
**Near Future:** [timeframe]
**Last updated:** [date]

---

## L1 — Identity & Purpose
> Who are you beyond your role? What is your personal purpose?

## L2 — Design & Specification
> What are your key relationships? What value do you create and exchange?

## L3 — Governance
> How do you make decisions? What are your personal governance principles?

## L4 — Evolution
> Where are you on the 7Cs arc? What is your learning edge?

## L5 — Integrity
> What will you not compromise? What are your red lines?

## L6 — Culture
> What kind of environment do you create around you?

## L7 — Operations
> What are your daily rhythms? How do you sustain energy?

## L8 — Sensing
> What signals do you watch? How do you stay aware?

## L9 — Intelligence
> How do you learn? How do you improve your own operating system?
```

### §6.5 What the Agent Does NOT Do

| The agent does NOT | Why |
|---|---|
| Create accounts | Human creates GitHub account/org themselves |
| Enter passwords | Human authenticates themselves |
| Make governance decisions | Human decides; agent advises |
| Choose the purpose | Human defines D1; agent probes and sharpens |
| Commit without review | PRs preserve the deliberation trail |

### §6.6 Instant Visibility

The publishing pipeline ships pre-configured. On fork:

1. **Intranet portal** — CI workflow builds from `instance/registry/` + blueprint + `instance/portals/intranet/` config, deploys to `gh-pages-intranet` branch
2. **Extranet portal** — CI workflow builds from identity + blueprint + `instance/portals/extranet/` config, deploys to `gh-pages` branch

**The goal:** A new commons has a web presence within minutes of forking.

Every commons is fully described through the four dimensions. Both portals follow this structure — content is generated from the registry and blueprint, not pushed:

| Dimension | What's visible | Where | Generated from |
|---|---|---|---|
| **D1 — Definition & Purpose** | Purpose statement, boundary, stage | Extranet + Intranet | `identity.yml` + blueprint L1 |
| **D2 — Participation** | Who participates, community structure | Extranet (opted-in) + Intranet | `instance/registry/5_entities/participation/` + engagement graph |
| **D3 — Proposition** | What this commons offers, value exchange | Extranet + Intranet | Blueprint L2 + `instance/registry/3_valuestreams/` |
| **D4 — Production** | Value stream overview, operational rhythms | Intranet | `instance/operations/` + recent activity |

### §6.7 The Commons Portfolio — Strongly Recommended

Since each commons is one repository with one blueprint, the portfolio **spans across namespaces**. We strongly recommend building a portfolio:

```
higgerix/                              # Personal namespace
└── me-os/              → Life domain. Personal growth, 7Cs arc.

cloudsters/                            # Organisation namespace
├── luebeck-os/         → Urban domain. City commons.
├── [venture-1]-os/     → First enterprise or project.
└── [venture-2]-os/     → Next venture. Always thinking ahead.

another-org/                           # Another organisation namespace
└── [venture-3]-os/     → Engagement in a different context.
```

**The portfolio spans across namespaces.** `me-os` lives in the personal GitHub namespace — it is yours, not any organisation's. Ventures live in organisation namespaces — they belong to the collective. The Blueprint MCP bridges them, providing a unified view across namespaces when the human grants access.

**The natural path:** Most Commons Engineers start with a venture. The `me-os` (Life domain) often comes later, when the engineer realises that tracking personal growth across all ventures creates a powerful feedback loop.

**Cross-namespace intelligence:** The agent in `me-os` can read state from `cloudsters/venture-1-os` if the human grants access. The Blueprint MCP operates across namespace boundaries, not within a single org. The 1:1:1 principle (one commons, one repo, one blueprint) keeps each commons clean; the portfolio layer connects them regardless of where they live.

**Portfolio synergy:** When `me-os` exists alongside venture repos in different namespaces, the agent can trace growth across all of them — "You applied operational-resilience in cloudsters/[venture]-os last month. Your 7C score in Practice moved from C3 to C4." The portfolio IS the practitioner development path, made visible through Commons as Code.

---

## §7 Knowledge That Ships — Detailed Inventory

### §7.1 What Ships in Commons (Universal)

The `commons/patterns/` layer contains only the universals — patterns that every commons needs regardless of domain:

| Content | Orbit | Count | Purpose |
|---|---|---|---|
| **The Singularity** | 0 | 1 | The foundational pattern from which all others derive |
| **Principles** | 1 | ~25 | First principles that govern all living systems |

These patterns are read-only in forks and updated via upstream sync. They are the minimum viable knowledge base.

### §7.2 What Ships as Pre-loaded Extensions

The `commons-engineering` extension packs ship pre-loaded in `extensions/commons-engineering/`. This is "batteries included" — the OS works without MCP connectivity from day one.

| Pack | Content | Patterns |
|---|---|---|
| **base** | Four curated collections: Blueprint, Engineer, Place, OS | ~112 |
| **business** | 13 Value Stream Families (4×D1, 4×D2, 3×D3, 3×D4), L3 Capabilities | ~85 |
| **urban** | 21 Urban Value Stream Families, settlement patterns | ~72 |
| **life** | 18 Life dimensions, personal value streams | ~60 |
| **ecology** | 16 Ecology dimensions, ecosystem patterns | ~55 |

All four domain packs ship with every fork. A hospital needs urban patterns (city infrastructure). A city needs business patterns (economic activity). A person lives in an ecology. The domains interpenetrate — shipping all four supports the holistic commons approach.

The agent interprets value stream patterns and translates them against connected Fabric MCPs. The pattern says *what* should happen; the Fabric MCP provides access to the system *where* it happens; the agent bridges between them. This is not workflow automation — it is intelligent interpretation.

> **Terminology note:** Life and Ecology domains use "dimensions" rather than "value streams" in their manifests, reflecting a deliberate shift from process-oriented to structural thinking. In the OS, all are treated as pattern collections regardless of terminology.

### §7.3 Pattern Resolution

Patterns are resolved across three layers — commons (local), extensions (local cache), and Commons MCP (remote):

```
Commons (universal)             Extensions (pre-loaded + installed)    Remote (via Commons MCP)
===================             ===================================    =======================

the-singularity.md              commons-engineering/base/              MCP: full pattern library
principles/                     commons-engineering/business/           MCP: deeper domain patterns
                                commons-engineering/urban/              MCP: cross-domain intelligence
                                commons-engineering/life/               MCP: L4/L5 capabilities
                                commons-engineering/ecology/            MCP: on-demand specialisation
                                healthtech-hamburg/clinical-pathways/   (installed via MCP)
```

Fork-created patterns live in `instance/patterns/` — sovereign, never touched by upstream sync.

**Load order (shadowing):** If a pattern with the same slug exists in multiple layers, the outermost layer wins: `instance/` overrides `extensions/`, which overrides `commons/`. This allows a fork to refine or replace any upstream pattern without modifying the original. The agent always resolves from outside in: instance first, then extensions, then commons. The shadowed pattern remains on disk — it is not deleted, only deprioritised.

**The principle:** Universal patterns + pre-loaded extensions = immediate functionality. The full library is always one MCP call away. Offline, you have the design language and operational backbone. Online, you have the universe.

### §7.4 Collections Are YAML Indices

Collections are curated groupings of patterns. They are **not folders** — they are YAML index files that reference patterns by path across all layers. A pattern can belong to multiple collections without duplication.

```yaml
# [repo-root]/extensions/commons-engineering/base/collections/blueprint.yml
collection: blueprint
title: "Commons Blueprint Collection"
description: "Patterns for building any commons blueprint, L1-L9"
patterns:
  - ../patterns/purpose-spiral.md
  - ../patterns/stakeholder-architecture.md
  - ../patterns/commons-governance.md
  - ../../business/valuestreams/purpose-to-portfolio.md
  # Cross-pack references are valid — the index curates, not contains
```

The folder structure is flat within each pack. The collection index provides the thematic navigation. The orbital layer and domain membership live in each pattern's frontmatter — the folder never duplicates this metadata.

### §7.5 Knowledge Sync

Knowledge is updated through three independent channels:

| Method | When | How | Scope |
|---|---|---|---|
| **Git upstream** | Weekly (automated) or manual | `sync-upstream.yml` workflow → PR for review | Updates `commons/` only |
| **Extension pack update** | Agent detects newer pack version via Commons MCP | Agent downloads updated pack, human reviews | Updates `extensions/{provider}/{pack}/` |
| **New extension install** | Agent recommends or founder requests | Agent downloads pack via Commons MCP | Adds new `extensions/{provider}/{pack}/` directory |
| **ALIGN.md check** | Periodic | Agent compares local vs remote counts and versions | Reads all three layers |

**Sovereignty rules:**
- `commons/` — updated only via upstream sync. Read-only in forks.
- `extensions/` — managed by the fork owner. Install, update, remove at will. Upstream never touches it.
- `instance/` — fully sovereign. Upstream never touches it. This includes `registry/`, `workshop/`, `operations/`, `portals/`, and all fork-specific knowledge.
- `blueprint.md`, `.commons/` — always sovereign. Never touched by any sync.

The `instance/workshop/` directory is the universal scratch space — experiments, drafts, work in progress. Where `instance/patterns/` holds mature fork-specific patterns, `instance/workshop/` holds what is not yet ready.

---

## §8 Touchpoints and Portals

### §8.1 Touchpoints — Definition Layer

The OS separates touchpoint **definitions** from publishing **configuration** from publishing **output**. Touchpoint definitions live in `instance/registry/2_touchpoints/`. Portal configuration and themes live in `instance/portals/`. Generated output is pushed to `gh-pages` branches by CI — never into the main branch.

| Layer | Where | What |
|---|---|---|
| **Touchpoint definitions** | `instance/registry/2_touchpoints/` | What happens here, who interacts, what value is exchanged |
| **Portal config & themes** | `instance/portals/intranet/`, `instance/portals/extranet/` | Site config, CSS, logos, navigation, page templates |
| **Generated output** | `gh-pages` / `gh-pages-intranet` branches | HTML/CSS built by CI from registry + blueprint + portal config. Never in main branch. |
| **Transaction execution** | Fabric MCPs (ERP, CRM) | Where the actual work happens |
| **Physical realisation** | Real world (Commons Place patterns) | Workshops, events, gatherings |

### §8.2 The YAML Graph — Relational Linking Between Cascade Layers

The five cascade layers (1_journeys through 5_entities) are not isolated silos. They form a **queryable graph** through YAML frontmatter references. Every file in the cascade declares which files in adjacent layers it connects to.

```yaml
# instance/registry/3_valuestreams/lead-to-user.yml
---
slug: lead-to-user
title: Lead to User
dimension: proposition
journeys:                              # ← upward link to layer 1
  - instance/registry/1_journeys/customer-acquisition.yml
touchpoints:                           # ← upward link to layer 2
  - instance/registry/2_touchpoints/website-contact-form.yml
  - instance/registry/2_touchpoints/initial-consultation.yml
capabilities:                          # ← downward link to layer 4
  - instance/registry/4_capabilities/proposition/crm-management.yml
  - instance/registry/4_capabilities/proposition/sales-process.yml
entities:                              # ← downward link to layer 5
  - instance/registry/5_entities/participation/sales-team.yml
---
```

**The graph works in both directions.** A journey references its touchpoints; a touchpoint references its value streams; a value stream references its capabilities and entities. The agent can traverse the graph in any direction — "Which entities support this value stream?" or "Which journeys does this touchpoint belong to?"

**Pattern archetypes mirror this structure.** Files in `commons/patterns/` and `extensions/` use the same frontmatter references. When the agent instantiates an archetype into `instance/registry/`, it resolves the links to local instances.

**The Blueprint MCP makes the graph queryable.** While the YAML files are the source of truth, the Blueprint MCP (when deployed) indexes these references into a queryable graph — enabling questions like "Show me all capabilities that have no entity assigned" or "Which value streams touch the customer onboarding journey?"

### §8.3 Intranet Portal

The intranet portal is the community's internal view. It shows everything the community needs to see — blueprint progress, entity directory, value streams, operational rhythms — but nothing the public needs to see.

| Feature | How it works |
|---|---|
| **Auto-generated by CI** | Publishing workflow reads `blueprint.md`, `instance/registry/`, `instance/operations/`, applies `instance/portals/intranet/` config + theme, pushes output to `gh-pages-intranet` branch |
| **Blueprint dashboard** | Shows L1-L9 completion status |
| **Entity directory** | Generated from `instance/registry/5_entities/` |
| **Activity feed** | Generated from recent commits and closed issues |
| **Access control** | GitHub Pages with private repo = requires GitHub auth |

### §8.4 Extranet Portal

The extranet portal is the public face of the commons. It tells the world: this commons exists, this is our purpose, this is how to participate.

| Feature | How it works |
|---|---|
| **Landing page** | Generated from `.commons/identity.yml` + blueprint L1 |
| **About** | Purpose, domain, founder, stage |
| **How to participate** | Contact, contribution guidelines |

### §8.5 Custom Domains

| Step | How | Time |
|---|---|---|
| 1. Buy domain (optional) | Any registrar | Minutes |
| 2. Add CNAME record | Point to `[org].github.io` | Minutes |
| 3. Set in `.commons/config.yml` | `extranet.domain: "luebeck-os.de"` | Seconds |
| 4. Enable in GitHub Pages settings | Custom domain field | Seconds |
| 5. SSL certificate | GitHub Pages provisions automatically | Minutes |

**Result:** `luebeck-os.de` serves the extranet portal. `team.luebeck-os.de` serves the intranet portal (if configured). Total time from fork to live presence with custom domain: under 30 minutes.

---

## §9 The 3-MCP Architecture in Practice

### §9.1 Three Channels, Three Owners

Every commons connects to intelligence through three MCP channels (see COMMONS_MCP_ARCHITECTURE_SPEC for full details):

```
                    ┌──────────────────────┐
                    │    Commons MCP        │
                    │  (cloudsters / CE)    │
                    │  Shared intelligence  │
                    └─────────┬────────────┘
                              │
                    ┌─────────┴────────────┐
                    │   [commons]-os        │
                    │   Agent + Workspace   │
                    └─────┬─────────┬──────┘
                          │         │
              ┌───────────┴──┐  ┌───┴──────────────┐
              │ Blueprint MCP│  │ Fabric MCPs (1..n)│
              │ (client-owned)│  │ (client-owned)    │
              │ Workspace     │  │ ERP, CRM, HR, ... │
              │ as graph      │  │ Systems of Record  │
              └──────────────┘  └───────────────────┘
```

| Channel | Owner | Provides | Sovereignty |
|---|---|---|---|
| **Commons MCP** | cloudsters / CE | Pattern library, cognitive services, collections, updates | Shared — CE stewards, all commons consume |
| **Blueprint MCP** | The commons itself | Workspace as queryable graph, blueprint state, inventory, engagement | Client-owned — data stays local |
| **Fabric MCPs** | The commons itself | Enterprise system access (ERP, CRM, HR, IoT, etc.) | Client-owned — data stays local |

### §9.2 How the Agent Uses All Three

```
Agent receives a task: "Check our supplier qualification status"

1. Agent reads the value stream pattern "Source to Pay" (extensions/commons-engineering/base/patterns/)
   → Pattern says: "Verify supplier qualification before order"

2. Agent queries Blueprint MCP (or reads instance/registry/ directly)
   → "Which suppliers are in our registry?"
   → Returns: list of supplier entities from instance/registry/5_entities/production/

3. Agent queries Fabric MCP (ERP)
   → "What is the qualification status of supplier [slug]?"
   → Returns: qualification data from the ERP system

4. Agent synthesizes
   → "Supplier X qualification expired. Opening an issue on the board."
```

The agent is the **runtime between pattern and system**. Value stream patterns describe *what*. Fabric MCPs provide *where*. The agent bridges between them. No BPMN needed — the intelligence is in the interpretation.

### §9.3 The Agent as Bridge — Commons Without Blueprint MCP

Not every commons will run a Blueprint MCP from day one. Many forks start with just the local files and a connection to the remote Commons MCP. In this scenario, the agent acts as the bridge between local state and remote intelligence:

```
Agent receives a task: "Diagnose our commons maturity"

1. Agent reads local files:
   - .commons/identity.yml          → instance identity, domain, purpose
   - blueprint.md                   → current blueprint state (L1-L9)
   - instance/registry/3_valuestreams/  → active value stream files
   - instance/registry/5_entities/     → registered entities

2. Agent serialises relevant local state into a text summary

3. Agent calls Commons MCP tool:
   diagnose(context: "<serialised local state>")
   → The context parameter carries what the Blueprint MCP would have provided

4. Commons MCP returns diagnosis based on pattern intelligence + local context

5. Agent presents findings to human, creates issues on the board
```

**The principle:** The Commons MCP tools like `diagnose`, `prescribe`, and `navigate` accept a `context` parameter (string). For commons with a Blueprint MCP, this context is populated automatically by querying the local MCP. For commons without one, the agent reads the local `instance/registry/` files, serialises them as text, and passes them as the `context` parameter. The intelligence lives in the Commons MCP; the agent is the adapter that makes local state legible to it.

> **Event-driven, not polling.** Fabric MCPs do not just answer queries; they push events. When a critical state changes in the System of Record (e.g., a certificate expires, a supplier loses qualification, a budget threshold is breached), the Fabric MCP triggers a webhook that opens an Issue on the board. The agent's SENSE phase reacts to the board, not by polling the entire ERP. **The board is the event bus.**

---

## §10 The Operating Loop — Issue Board, Self-Improvement, Human-Agent Teams

### §10.1 The Issue Board as Operating Surface

The GitHub Issue Board (Kanban view) is the **primary alignment surface between humans and agents**. It is not a developer tool. It is the shared workspace where both sides see what is happening, what needs attention, and what comes next.

| What the board does | How |
|---|---|
| **Shared visibility** | Both humans and agents see the same priorities, in the same order |
| **Priority by position** | Moving an issue up = more important. The board IS the priority |
| **Documentation trail** | Every idea → an issue. Every decision → a labelled issue. |
| **Dimension tagging** | Issues carry labels: `definition`, `participation`, `proposition`, `production` |
| **Agent proposals** | Agents create draft issues with proposed actions. Humans review, adjust, approve |

**The principle:** If it's not on the board, it doesn't exist.

### §10.2 Recursive Self-Improvement

Every Commons OS instance can run a continuous improvement loop. This is a concrete GitHub Actions workflow that runs on a schedule and proposes improvements.

```
┌─────────────────────────────────────────────────────┐
│                  The Improvement Loop                │
│                                                     │
│   1. SENSE   — Agent reads the board, the blueprint,│
│                recent commits, open issues           │
│   2. ASSESS  — Agent compares current state against  │
│                blueprint L1-L9, detects gaps          │
│   3. PROPOSE — Agent creates issues with suggestions │
│                (never commits directly)               │
│   4. REVIEW  — Human reviews, prioritises, adjusts   │
│   5. ACT     — Approved issues get worked on (by     │
│                human, agent, or both)                │
│   6. LEARN   — Results feed back into the next cycle │
│                                                     │
│   Triggered: GitHub Action on schedule (daily/weekly)│
│   + on demand via issue comment or board event       │
└─────────────────────────────────────────────────────┘
```

### §10.3 Human-Agent Teams

From the moment of fork, the operating model is a **team of humans and agents**:

| Layer | Who | What they do |
|---|---|---|
| **Human founder** | 1 person | Defines purpose, makes decisions, governs |
| **Purpose Agent (D1)** | AI | Guards direction, monitors alignment, proposes corrections |
| **Participation Agent (D2)** | AI | Cultivates community, maps stakeholders, tracks engagement |
| **Proposition Agent (D3)** | AI | Frames value exchange, monitors market signals |
| **Production Agent (D4)** | AI | Manages infrastructure, supervises engines, delivers at volume |
| **On-demand agents** | AI | Product agents (under D3), engine agents (under D4), persona agents (under D2) |
| **Human participants** | N people | Stakeholders, community members, contributors |

**Scaling pattern:**

```
Solo founder       →  1 human + 4 agents           = operating team of 5
Small community    →  3 humans + 4 agents + 2 bots  = operating team of 9
Growing commons    → 10 humans + 4 agents + N bots  = operating team of 14+
Mature commons     → many humans + many agents       = the commons as organism
```

---

## §11 Deletion and Deprecation

### §11.1 When to Delete Files

| Situation | Action |
|---|---|
| **Manifest superseded by newer version** | Archive to `_archive/` with date prefix, remove from active |
| **Specification replaced** | New spec references the old one in its lineage. Old spec moves to `_archive/` |
| **Pattern deprecated** | Pattern `status` field set to `deprecated`. Pattern stays in library |
| **Blueprint section rewritten** | Git history preserves the old version. Overwrite in place. |

---

## §12 Open Questions

| # | Question | Status |
|---|---|---|
| 1 | **Intranet access control:** GitHub Pages private repos require GitHub auth. Is this sufficient? | Open |
| 2 | **Collection curation:** Who decides which patterns enter the four core collections? | Open |
| 3 | **Template versioning:** How do we signal to existing forks that the template has a new release? | Open |
| 4 | **Multi-domain commons:** A commons that spans Business + Urban. How do value stream families compose? | Open |
| 5 | **me-os specifics:** Does the Life domain need a variant template (no extranet by default)? | Open |
| 6 | **Improvement loop scope:** How deep should the automated SENSE phase read? What's the right cron rhythm? | Open |
| 7 | **Agent team bootstrapping:** When do the four dimension agents get their own contexts? | Open |
| 8 | **Fabric MCP standards:** What is the minimum Fabric MCP interface that value stream patterns can assume? | Open |

---

## §13 Implementation Checklist

### Phase 0: Template Creation (Now)

- [ ] Create `commons-engineering/commons-os` as a GitHub template repository
- [ ] Populate the full directory structure from §2.1
- [ ] Write AGENT.md template (agent-neutral, §3)
- [ ] Write BOOT.md with boot guide
- [ ] Write ALIGN.md template (§4)
- [ ] Configure .commons/ with identity.yml and config.yml templates
- [ ] Create `blueprint.md` stub with L1-L9 sections
- [ ] Populate `commons/manifests/` with all manifests
- [ ] Populate `commons/specs/` with all specifications
- [ ] Populate `commons/patterns/` with universals (singularity + principles)
- [ ] Populate `extensions/commons-engineering/` with pre-loaded domain packs
- [ ] Populate `commons/templates/` with blueprint, pattern, and organisation templates
- [ ] Build `instance/portals/intranet/` with default theme + auto-generation
- [ ] Build `instance/portals/extranet/` with default theme + landing page
- [ ] Create `.github/` with issue templates, labels, workflows
- [ ] Create `.github/workflows/improvement-loop.yml` (§10.2)
- [ ] Write README.md with onboarding instructions (agent-neutral)
- [ ] Test: fork → deploy → custom domain in under 30 minutes
- [ ] Test: improvement loop creates meaningful issues after boot

### Phase 1: First Instances

- [ ] Fork for `luebeck-os` — validate the boot sequence
- [ ] Fork for `berlin-os` — validate the boot sequence
- [ ] Iterate on template based on real usage
- [ ] Connect to Commons MCP (once Phase 1 of MCP spec is live)

---

*COMMONS OS SPECIFICATION v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
