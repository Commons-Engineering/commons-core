# Extension Pack Specification (v1.0)

**Version:** 1.0
**Status:** Specification
**Companion:** COMMONS_OS_SPEC.md (§2.5), COMMONS_MCP_ARCHITECTURE_SPEC.md (§4.4.6), PATTERN_SPEC.md (v8.2)

---

## §1 Purpose

Extension packs are the primary mechanism for delivering domain-specific knowledge to a Commons OS instance. They enable any Commons Incubator to build, publish, and maintain curated knowledge collections — patterns, specs, templates, scripts — that extend the OS beyond its universal commons layer.

The extension pack architecture follows the chaordic principle: shared interface (this spec), autonomous content (each provider's IP). A hospital consortium publishes clinical pathway patterns. A Hanseatic city publishes settlement governance patterns. A sustainability network publishes circular-economy patterns. All use the same pack format; all are discoverable through the same registry; all install with the same MCP tool.

This specification is the authoritative reference for anyone building, publishing, or consuming an extension pack.

---

## §2 Pack Structure

### §2.1 Directory Convention

Every extension pack lives at `extensions/{provider}/{pack}/`. A pack is an **atomic unit** — all its content (patterns, collections, specs, templates) lives in one directory.

| Segment | Rule | Example |
|---|---|---|
| `extensions/` | Fixed top-level directory (Layer 2) | `extensions/` |
| `{provider}` | Lowercase, hyphenated. Globally unique. Registered in provider registry. | `commons-engineering`, `healthtech-hamburg` |
| `{pack}` | Lowercase, hyphenated. Unique within a provider. Describes the content domain. | `base`, `business`, `clinical-pathways` |

A concrete example:

```
extensions/
  commons-engineering/              # Provider
    base/                           # Pack: core curated collections
      manifest.yml                  # Required
      collections/
        blueprint.yml
        engineer.yml
        place.yml
      patterns/
    business/                       # Pack: Business domain
      manifest.yml
      patterns/
      collections/
  healthtech-hamburg/               # Provider
    clinical-pathways/              # Pack
      manifest.yml
      ...
```

### §2.2 Required and Recommended Files

| File | Required | Purpose |
|---|---|---|
| `manifest.yml` | **Yes** | Pack identity, version, dependencies, content catalogue |
| `README.md` | Recommended | Human-readable description, usage guidance, examples |
| `CHANGELOG.md` | Recommended | Version history, breaking changes |

All other files and directories are defined by the pack provider. The OS does not prescribe internal structure beyond `manifest.yml`. This is deliberate — providers organise their knowledge the way that serves their domain best.

### §2.3 manifest.yml Schema

The manifest is the only structural contract between the OS and the pack. Every field is documented below.

```yaml
# ═══════════════════════════════════════════════════════════════════
# IDENTITY (required)
# ═══════════════════════════════════════════════════════════════════
pack: string                    # Pack identifier (lowercase, hyphenated)
provider: string                # Provider identifier (must match parent directory)
version: string                 # SemVer (major.minor.patch)
title: string                   # Human-readable title
description: string             # One-paragraph description

# ═══════════════════════════════════════════════════════════════════
# SCOPE (optional)
# ═══════════════════════════════════════════════════════════════════
domains: string[]               # Applicable domains: life, business, urban, ecology
dependencies: string[]          # Other packs required (format: "{provider}/{pack}")
license: string                 # SPDX identifier (default: CC-BY-SA-4.0)
min_os_version: string          # Minimum Commons OS version required

# ═══════════════════════════════════════════════════════════════════
# CONTENT CATALOGUE
# ═══════════════════════════════════════════════════════════════════
patterns: int                   # Total pattern count in this pack
collections:                    # Collection indices provided
  - id: string                  # Collection identifier (lowercase, hyphenated)
    title: string               # Human-readable title
    description: string         # One-sentence description
    index_file: string          # Relative path to YAML index file

specs: string[]                 # Spec files included (relative paths)
templates: string[]             # Template files included (relative paths)
scripts: string[]               # Script files included (relative paths)

# ═══════════════════════════════════════════════════════════════════
# METADATA
# ═══════════════════════════════════════════════════════════════════
created: string                 # ISO date (YYYY-MM-DD)
updated: string                 # ISO date (YYYY-MM-DD)
changelog: string               # Relative path to CHANGELOG.md (if exists)
```

#### Field Reference

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `pack` | string | **Yes** | — | Must match the pack directory name |
| `provider` | string | **Yes** | — | Must match the provider directory name |
| `version` | string | **Yes** | — | Semantic version: `major.minor.patch` |
| `title` | string | **Yes** | — | Human-readable name, capitalised naturally |
| `description` | string | **Yes** | — | One paragraph. What this pack delivers and who benefits. |
| `domains` | string[] | No | `[]` | Which of the four domains this pack serves |
| `dependencies` | string[] | No | `[]` | Format: `"{provider}/{pack}"`. Resolved at install time. |
| `license` | string | No | `CC-BY-SA-4.0` | SPDX license identifier |
| `min_os_version` | string | No | `1.0` | Minimum compatible Commons OS version |
| `patterns` | int | No | `0` | Must match actual file count when declared |
| `collections` | list | No | `[]` | Each entry describes one collection index |
| `specs` | string[] | No | `[]` | Relative paths to included spec files |
| `templates` | string[] | No | `[]` | Relative paths to included templates |
| `scripts` | string[] | No | `[]` | Relative paths to included automation scripts |
| `created` | string | No | — | ISO date of initial publication |
| `updated` | string | No | — | ISO date of most recent update |
| `changelog` | string | No | — | Path to CHANGELOG.md relative to pack root |

#### Example: CE Base Pack

```yaml
pack: base
provider: commons-engineering
version: 1.0.0
title: "Commons Engineering Base Collections"
description: "Blueprint, Engineer, Place, and OS pattern collections — the four curated views into the commons knowledge base."
domains: [life, business, urban, ecology]
dependencies: []
license: CC-BY-SA-4.0
patterns: 112
collections:
  - id: blueprint
    title: "Commons Blueprint"
    description: "Patterns for building any commons blueprint, L1-L9"
    index_file: collections/blueprint.yml
  - id: engineer
    title: "Commons Engineer"
    description: "Patterns for practitioner development"
    index_file: collections/engineer.yml
  - id: place
    title: "Commons Place"
    description: "Patterns for settlement and spatial governance"
    index_file: collections/place.yml
created: 2026-03-17
updated: 2026-03-17
```

### §2.4 Collection Index Files

Collections are YAML indices — they reference patterns by path, they do not contain them. This separation allows a single pattern to appear in multiple collections without duplication.

#### Collection Index Schema

```yaml
collection: string              # Collection identifier (must match manifest entry)
title: string                   # Human-readable title
description: string             # One-paragraph description
curator: string                 # Who curates this collection (provider or person)
patterns:                       # Ordered list of pattern paths
  - string                      # Relative path from index file to pattern
```

#### Field Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `collection` | string | **Yes** | Must match the `id` in the parent manifest's collections list |
| `title` | string | **Yes** | Human-readable collection name |
| `description` | string | **Yes** | What this collection covers and who it serves |
| `curator` | string | No | Attribution — the person or organisation curating this view |
| `patterns` | string[] | **Yes** | Relative paths to pattern files. Order matters — it defines reading sequence. |

#### Path Resolution Rules

| Path Form | Meaning | Example |
|---|---|---|
| `../patterns/purpose-spiral.md` | Pattern within the same pack | Typical intra-pack reference |
| `../../commons-engineering/business/valuestreams/lead-to-user.md` | Pattern in another pack from the same provider | Cross-pack reference within provider |
| `../../healthtech-hamburg/clinical-pathways/patterns/triage.md` | Pattern in another provider's pack | Cross-provider reference (dependency should be declared) |

Cross-pack references are valid. If a collection references patterns from another pack, that pack should be listed in the manifest's `dependencies` field.

#### Example: Blueprint Collection

```yaml
collection: blueprint
title: "Commons Blueprint Collection"
description: "Patterns for building any commons blueprint. Follow L1 through L9 — from purpose through portfolio to operating model."
curator: commons-engineering
patterns:
  - ../patterns/purpose-spiral.md
  - ../patterns/stakeholder-architecture.md
  - ../patterns/value-proposition-canvas.md
  - ../patterns/journey-architecture.md
  - ../../commons-engineering/business/valuestreams/purpose-to-portfolio.md
```

---

## §3 Provider Registry

### §3.1 Provider Profile Schema

Every provider is represented by a YAML profile at `registry/providers/{provider}.yml`. This profile serves as the provider's identity card in the ecosystem.

```yaml
# ═══════════════════════════════════════════════════════════════════
# PROVIDER IDENTITY
# ═══════════════════════════════════════════════════════════════════
provider: string                # Must match directory name and pack manifest references
name: string                    # Human-readable organisation name
url: string                     # Provider website
description: string             # One-paragraph description of the provider
mcp_endpoint: string            # MCP server URL (if provider runs one)
verified: boolean               # Verified by CE (curated via PR review)
contact: string                 # Contact email or URL

# ═══════════════════════════════════════════════════════════════════
# PACK CATALOGUE
# ═══════════════════════════════════════════════════════════════════
packs:
  - name: string                # Pack identifier
    version: string             # Current version (SemVer)
    domains: string[]           # Applicable domains
    description: string         # One-sentence pack description
    patterns: int               # Pattern count
    status: string              # active | deprecated | beta
```

#### Field Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `provider` | string | **Yes** | Lowercase, hyphenated. Must match directory and manifest references. |
| `name` | string | **Yes** | Human-readable organisation name |
| `url` | string | **Yes** | Provider's website |
| `description` | string | No | What this provider contributes to the ecosystem |
| `mcp_endpoint` | string | No | URL of the provider's MCP server, if they run one |
| `verified` | boolean | No | `true` if CE has reviewed and verified the provider. Default: `false`. |
| `contact` | string | No | Contact email or URL for the provider |
| `packs` | list | **Yes** | At least one pack must be listed |
| `packs[].name` | string | **Yes** | Must match the pack directory name |
| `packs[].version` | string | **Yes** | Current published version |
| `packs[].domains` | string[] | No | Which domains the pack serves |
| `packs[].description` | string | **Yes** | One sentence describing the pack |
| `packs[].patterns` | int | No | Pattern count |
| `packs[].status` | string | No | `active` (default), `beta`, or `deprecated` |

#### Example: CE Provider Profile

```yaml
provider: commons-engineering
name: "Commons Engineering"
url: https://commons.engineering
description: "Steward of the Commons OS. Publisher of the universal commons layer and four domain packs."
mcp_endpoint: https://mcp.commons.engineering/v1
verified: true
contact: hello@commons.engineering

packs:
  - name: base
    version: 1.0.0
    domains: [life, business, urban, ecology]
    description: "Core collections: Blueprint, Engineer, Place, OS"
    patterns: 112
    status: active
  - name: business
    version: 1.0.0
    domains: [business]
    description: "13 Value Stream Families, L3 Capabilities"
    patterns: 85
    status: active
  - name: urban
    version: 1.0.0
    domains: [urban]
    description: "Urban value streams and settlement patterns"
    patterns: 72
    status: active
  - name: life
    version: 1.0.0
    domains: [life]
    description: "Life dimensions, personal value streams"
    patterns: 60
    status: beta
  - name: ecology
    version: 1.0.0
    domains: [ecology]
    description: "Ecology dimensions, ecosystem patterns"
    patterns: 55
    status: beta
```

### §3.2 Registration Process

| Step | Action | Who | Where |
|---|---|---|---|
| 1 | Create provider profile YAML | Provider | Their fork of commons-os |
| 2 | Submit Pull Request to commons-os upstream | Provider | GitHub |
| 3 | Review: naming conflict check, basic quality check | CE (or community reviewers) | PR review |
| 4 | Merge | CE maintainer | GitHub |
| 5 | Provider is registered, packs discoverable via Commons MCP | Automatic | MCP indexes on sync |

The registration process is deliberately lightweight. The PR is the governance mechanism — it creates a record, enables review, and is reversible.

### §3.3 Naming Rules

| Rule | Rationale |
|---|---|
| Provider names are **globally unique** | No collisions in the extension directory |
| Pack names are **unique within a provider** | Providers manage their own namespace |
| Both use **lowercase-hyphenated** format | Filesystem compatibility, URL-safe, consistent with pattern IDs |
| Reserved providers: `commons-engineering`, `commons-os` | Upstream namespace protection |
| Provider names must not start with `commons-` | Prevents confusion with upstream. Exception: `commons-engineering`. |
| No single-character provider names | Avoids accidental collisions and ambiguity |

---

## §4 Pack Lifecycle

### §4.1 Creating a Pack

| Step | Action | Detail |
|---|---|---|
| 1 | **Register as provider** | Create `registry/providers/{provider}.yml` and submit PR (§3.2). Skip if already registered. |
| 2 | **Create pack directory** | `extensions/{provider}/{pack}/` |
| 3 | **Write manifest.yml** | Follow the schema in §2.3. Start with the five required fields. |
| 4 | **Add patterns** | All patterns must conform to PATTERN_SPEC v8.2. Place them in whatever directory structure suits the domain. |
| 5 | **Create collection indices** | Optional but recommended. YAML files that curate reading paths through the patterns (§2.4). |
| 6 | **Update provider profile** | Add the new pack to `registry/providers/{provider}.yml` |
| 7 | **Validate** | Run the ALIGN.md alignment check (§5.2) to verify conformance |

### §4.2 Versioning

Packs use **Semantic Versioning** (SemVer). The version field in `manifest.yml` is the source of truth.

| Change Type | Version Bump | Example |
|---|---|---|
| Breaking: renamed patterns, removed collections, restructured directories | **MAJOR** | `1.0.0` → `2.0.0` |
| Additive: new patterns, new collections, new optional fields | **MINOR** | `1.0.0` → `1.1.0` |
| Non-structural: description updates, typo fixes, metadata corrections | **PATCH** | `1.0.0` → `1.0.1` |

**Breaking change policy:** MAJOR version bumps should be rare. When renaming or removing patterns, prefer deprecation (add a `deprecated: true` field to the pattern frontmatter) over deletion. This gives downstream consumers time to update their references.

### §4.3 Publishing

| Method | How | Audience | Connectivity |
|---|---|---|---|
| **Pre-loaded** | Included in the commons-os fork template | Ships with every fork | Offline — works from day one |
| **Commons MCP** | Listed in provider registry, downloaded via `download_pack` tool, installed locally by agent | Any connected commons | Requires MCP connectivity |
| **Direct** | Provider shares the pack directory; fork owner places it in `extensions/` | Manual distribution | Offline |
| **Git subtree** | Provider maintains pack in separate repo; fork owner adds as subtree | Advanced distribution | Git remote access |

The pre-loaded method is reserved for CE packs. All other providers publish via MCP or direct distribution.

### §4.4 Installing via MCP

Pack installation follows the **registry/client separation** — the same model as npm, apt, or pip. The Commons MCP (remote) serves pack contents; the local agent writes them to disk.

#### Remote Tools (Commons MCP — COMMONS_MCP_ARCHITECTURE_SPEC §4.4.6)

| Tool | Tier | Purpose |
|---|---|---|
| `download_pack(provider, pack, version?)` | PEER (Tier 1) | Download pack payload (manifest + files) from the registry |
| `check_pack_updates(installed)` | PEER (Tier 1) | Compare locally installed versions against the registry |

The Commons MCP is a remote server — it **cannot** write files to the local instance. `download_pack` returns the pack contents as a structured payload (manifest + file tree). `check_pack_updates` receives the agent's locally known versions and returns available updates.

#### Local Installation Sequence (Agent)

The agent orchestrates the installation locally. This is the canonical flow:

1. Agent calls `download_pack(provider, pack, version?)` on Commons MCP
2. Agent reads the returned `manifest.yml` and checks the `dependencies` field
3. **If dependencies are declared, the agent resolves and installs them recursively** (depth-first), calling `download_pack` for each unmet dependency. Circular dependencies are detected and rejected with an error. The agent skips dependencies already installed at a compatible version.
4. Agent creates the local directory `extensions/{provider}/{pack}/`
5. Agent writes all files from the payload to disk
6. Agent validates the manifest against this spec (§5.2 alignment checks)
7. Agent reports success to the human — pattern count, collections loaded, dependencies resolved

**Dependency resolution order:** Dependencies are installed before the requesting pack (depth-first). If an incompatible version is already installed, the agent warns the human and asks for confirmation before upgrading.

> **For commons with a Blueprint MCP:** The Blueprint MCP may expose a local `install_pack` convenience tool that wraps the full download-validate-write sequence. This is a local tool — it calls the remote Commons MCP for the payload and handles the filesystem writes itself. The Blueprint MCP runs on the client's machine and has full local access.

### §4.5 Updating

| Scenario | Mechanism |
|---|---|
| Pre-loaded packs (CE) | Updated via upstream sync (`git pull upstream`) |
| MCP-installed packs | Agent calls `check_pack_updates()` to detect new versions; downloads and installs updates via `download_pack()` |
| Direct/subtree packs | Manual — fork owner manages updates |

---

## §5 Quality and Conformance

### §5.1 Pattern Conformance

All patterns within a pack **must** conform to PATTERN_SPEC v8.2. The pack provider is responsible for ensuring conformance before publication. Specifically:

| Requirement | Reference |
|---|---|
| Valid YAML frontmatter with all required fields | PATTERN_SPEC §4 |
| Correct orbital assignment (orbit 0-5) | PATTERN_SPEC §3 |
| Valid domain assignment | PATTERN_SPEC §4, Group 0 |
| Commons Alignment scores present | PATTERN_SPEC §4, Group 3 |
| Body sections follow the narrative structure | PATTERN_SPEC §5 |

### §5.2 Alignment Check

The Commons OS ALIGN.md alignment service validates installed packs. The checks:

| Check | What It Validates | Severity |
|---|---|---|
| **Manifest schema** | `manifest.yml` is valid YAML matching the schema in §2.3 | Error |
| **Pattern count** | Declared `patterns` count matches actual file count | Warning |
| **Pattern frontmatter** | All patterns have valid frontmatter per PATTERN_SPEC | Error |
| **Collection integrity** | All paths in collection index files resolve to existing patterns | Error |
| **Dependency resolution** | All declared dependencies are installed | Warning |
| **Provider match** | `provider` field matches the parent directory name | Error |
| **Pack match** | `pack` field matches the pack directory name | Error |
| **Version format** | `version` field is valid SemVer | Error |

Errors block publication. Warnings are advisory.

### §5.3 Pack Rating (Future)

The Commons MCP will support community ratings for packs at TEAM tier and above.

| Dimension | What It Measures |
|---|---|
| **Completeness** | Does the pack cover its declared domain adequately? |
| **Accuracy** | Are the patterns factually correct and well-sourced? |
| **Currency** | Are patterns up to date with current practice? |
| **Usefulness** | Do practitioners find the patterns actionable? |

Rating infrastructure is planned for Commons OS v2.0.

---

## §6 Pre-loaded Packs

The commons-os template ships with these CE packs pre-loaded in `extensions/commons-engineering/`:

| Pack | Provider | Content | Patterns | Status |
|---|---|---|---|---|
| `base` | commons-engineering | Four curated collections (Blueprint, Engineer, Place, OS) | ~112 | Active |
| `business` | commons-engineering | 13 Business Value Stream Families (4×D1, 4×D2, 3×D3, 3×D4), L3 Capabilities | ~85 | Active |
| `urban` | commons-engineering | 21 Urban Value Stream Families, settlement patterns | ~72 | Active |
| `life` | commons-engineering | 18 Life dimensions, personal value streams | ~60 | Beta |
| `ecology` | commons-engineering | 16 Ecology dimensions, ecosystem patterns | ~55 | Beta |

These packs are the "batteries included" promise. A forked commons works offline, without MCP connectivity, from day one.

All four domain packs ship with every fork. A hospital needs urban patterns (city infrastructure). A city needs business patterns (economic activity). A person lives in an ecology. The domains interpenetrate — shipping all four supports the holistic commons approach.

---

## §7 Design Decisions

| Decision | Rationale |
|---|---|
| **manifest.yml is the only structural requirement** | Maximum autonomy for providers. The OS doesn't dictate how you organise your knowledge — only that you declare what's in it. |
| **Collections reference, they don't contain** | A pattern can appear in multiple collections without duplication. The pattern file is the source of truth; collections are curated views. |
| **Provider namespace is global, pack namespace is local** | Mirrors package ecosystems (npm, PyPI). Simple, proven, scalable. |
| **Registration via PR, not self-service** | Lightweight governance. The PR creates a reviewable record. Community grows at the speed of trust. |
| **SemVer for packs** | Familiar convention. Breaking changes are visible in the version number. |
| **Pre-loaded packs are extension packs, not special** | No architectural privilege for CE packs. They follow the same spec. Any provider could, in theory, replace them. |
| **Cross-pack references are valid** | Knowledge doesn't respect namespace boundaries. A blueprint collection naturally references business patterns. Dependencies make this explicit. |
| **Remote/local separation for install** | The Commons MCP is a remote server — it cannot write to the local filesystem. `download_pack` returns a payload; the local agent writes files. Same model as npm/apt/pip. |
| **No version pinning in v1.0** | Dependencies use `"{provider}/{pack}"` without version constraints. This is sufficient for a young ecosystem where breaking changes are rare. For v1.1+, version pinning (e.g., `"commons-engineering/urban@^1.0.0"`) is planned to prevent breaking changes from cascading when packs reach major version bumps. |

---

## §8 Relationship to Other Specifications

| Specification | Relationship |
|---|---|
| **COMMONS_OS_SPEC §2.5** | Defines the three-layer knowledge architecture and the extension pack directory convention. This spec elaborates the full schema and lifecycle. |
| **COMMONS_MCP_ARCHITECTURE_SPEC §4.4.6** | Defines the MCP tools (`download_pack`, `check_pack_updates`) for browsing and downloading packs from the remote registry. |
| **PATTERN_SPEC v8.2** | All patterns within extension packs must conform. The pack spec does not redefine pattern format — it defers to PATTERN_SPEC entirely. |
| **COMMONS_OS_MANIFEST §4** | Describes what knowledge ships with the fork and why. This spec describes *how* that knowledge is packaged. |

---

*PACK_SPEC v1.0 — 17 March 2026*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
