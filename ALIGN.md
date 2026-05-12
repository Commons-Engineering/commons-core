# Alignment Rules — Commons OS

**Version:** 1.1
**Status:** Living Document

This file defines the alignment checks that keep a commons healthy. The Purpose Agent runs these checks regularly (see `instance/operations/rhythms.md` for frequency). Results are posted as GitHub Issues with the label `alignment-report`.

---

## §0 Commons Definition Alignment

The most fundamental check. If this fails, this is not a commons.

> **A commons systematically creates value that is alive, shared, just, and is built to last.**

| Check | Rule | Severity |
|---|---|---|
| **Systematically** | Value creation is designed, not accidental. Patterns and governance exist. If value depends on a single hero, this check fails. | Critical |
| **Alive** | The system regenerates through use. Participants grow. Knowledge compounds. If the system depletes its participants (burnout, extraction, churn), this check fails. | Critical |
| **Shared** | Value creation belongs to the participants collectively. If one actor captures disproportionate value, this check fails. | Critical |
| **Just** | The exchange serves all participants fairly — especially those with the least power. If voiceless participants are systematically disadvantaged, this check fails. | Critical |
| **Built to last** | Stewardship rotates. Knowledge is documented. No single dependency. If the system cannot survive a change of stewardship, this check fails. | Critical |

Source: `commons/patterns/principles/the-commons.md` (Orbit 1)

---

## §1 Identity & Purpose Alignment

The foundation. If these fail, nothing else matters.

| Check | Rule | Severity |
|---|---|---|
| **Purpose exists** | `identity.yml` must contain a non-empty `purpose` field (not the template default) | Critical |
| **Purpose in blueprint** | `blueprint.md` L1.1 must be populated with name, purpose, domain, boundary, and founding story | Critical |
| **Imperative articulated** | `blueprint.md` L1.2 must describe the challenge this commons addresses (min. 50 words) | High |
| **Values declared** | `blueprint.md` L1.3 must contain at least one non-negotiable commitment | High |
| **Purpose spiral** | `blueprint.md` L1.4 must describe all four dimensions as they manifest in this commons | Normal |
| **Domain consistency** | `identity.yml` domain must match `blueprint.md` L1.1 domain | Critical |
| **Stage accuracy** | `identity.yml` stage must reflect actual operational state | Normal |

## §2 Stakeholder & Participation Alignment

No commons exists without participants.

| Check | Rule | Severity |
|---|---|---|
| **Stakeholders mapped** | `blueprint.md` L2.1 must contain at least 3 stakeholders | High |
| **Participation model** | `blueprint.md` L2.2 must describe how stakeholders join and progress | Normal |
| **Non-human participants** | `blueprint.md` L2.3 must explicitly address non-human participation (even if "none yet") | Normal |
| **Entity registration** | `instance/registry/5_entities/` must contain at least one entity (the commons itself) | High |
| **Founder entity** | At least one entity in `instance/registry/5_entities/` must have the founder role | Normal |

## §3 Value Proposition Alignment

A commons must create value to sustain itself.

| Check | Rule | Severity |
|---|---|---|
| **Value proposition** | `blueprint.md` L3.1 must articulate what stakeholders gain (min. 50 words) | High |
| **Offers defined** | `blueprint.md` L3.2 must list at least one offer with status | Normal |
| **Exchange model** | `blueprint.md` L3.3 must describe how value flows | Normal |
| **Value streams** | `instance/registry/3_valuestreams/` must contain at least one value stream (after Seed stage) | Normal |

## §4 Production & Infrastructure Alignment

The commons must have the infrastructure to deliver on its promises.

| Check | Rule | Severity |
|---|---|---|
| **MCP configured** | `.commons/config.yml` must define at least the Commons MCP endpoint | High |
| **Operating rhythms** | `instance/operations/rhythms.md` must define at least alignment check and board review rhythms | Normal |
| **Blueprint depth** | After Active stage: `blueprint.md` must have content in L4-L6 (not just headers) | Normal |
| **Resilience assessed** | After Established stage: `blueprint.md` L8.3 must contain a resilience assessment | Normal |

## §5 Specification Conformance

The commons must follow current specifications.

| Spec | Expected version | What to check |
|---|---|---|
| **PATTERN_SPEC** | v8.2 | All patterns in `commons/patterns/` and `extensions/` must conform — 8 frontmatter groups, 8 body sections |
| **COMMONS_OS_SPEC** | v1.0 | Directory structure, commons/extensions/instance layers, identity.yml schema |
| **COMMONS_MCP_ARCHITECTURE_SPEC** | v1.0 | 3-channel MCP configuration in `.commons/config.yml` |

Agent compares local `commons/specs/` versions against Commons MCP latest (when connected).

## §6 Structural Checks

The file system must match the specification.

| Check | Rule | Severity |
|---|---|---|
| **Identity valid** | `.commons/identity.yml` must be valid YAML with: slug, name, purpose, domain, locale, stage | Critical |
| **Config valid** | `.commons/config.yml` must be valid YAML | High |
| **Blueprint exists** | `blueprint.md` must exist and be non-empty | Critical |
| **Agent config** | `AGENT.md` must exist (OS-standard AI configuration file) and not reference a specific AI product by name | High |
| **Commons manifests** | `commons/manifests/` must contain all required manifests | High |
| **Commons specs** | `commons/specs/` must contain all required specs | High |
| **Commons patterns** | `commons/patterns/` must contain orbital layers 0-singularity through 2-commons | High |
| **Registry structure** | `instance/registry/` must contain `1_journeys/`, `2_touchpoints/`, `3_valuestreams/`, `4_capabilities/`, `5_entities/` | High |
| **Workshop exists** | `instance/workshop/` directory must exist | Normal |
| **Portals exists** | `instance/portals/` directory must exist | Normal |

## §7 Pattern Health

Patterns must maintain quality and spec conformance.

| Check | Rule | Severity |
|---|---|---|
| **Frontmatter complete** | Every pattern must have all 8 frontmatter groups (GROUP 0-7) | High |
| **GROUP 0 present** | Every pattern must declare `orbital_layer`, `sector`, and `gravitational_hubs` | High |
| **Vitality minimum** | Patterns with `vitality_score` below 2.0 are flagged for decomposition review | Normal |
| **Anchor rule** | Patterns in Orbit 3-4 must link to at least one gravitational hub in Orbit 0-2 | Normal |
| **Body sections** | Every pattern must contain all 8 body sections (Context through Vitality) | Normal |

## §8 Upstream Sync

Forks must stay connected to upstream evolution.

| Check | Rule | Severity |
|---|---|---|
| **Sync workflow** | `.github/workflows/sync-upstream.yml` must exist and be active | Normal |
| **Commons untouched** | Files in `commons/` must not be locally modified (check via git diff against upstream) | High |
| **Instance sovereign** | Upstream sync must never touch `instance/`, `extensions/`, or `blueprint.md` | Critical |

---

## Severity Levels

| Level | Meaning | Action |
|---|---|---|
| **Critical** | The commons cannot function without this | Fix immediately — block other work |
| **High** | The commons is degraded without this | Fix within the current operating rhythm |
| **Normal** | The commons is incomplete without this | Fix when capacity allows |

## Reporting

The Purpose Agent posts alignment results as a GitHub Issue:

- **Label:** `alignment-report`
- **Title:** `Alignment Check — [date]`
- **Body:** Structured table of all checks with pass/fail/skip status
- **Recommendations:** Prioritised action items grouped by severity
- **Stage context:** Checks are evaluated against the current lifecycle stage — a Seed-stage commons is not expected to pass Established-stage checks

---

*ALIGNMENT RULES v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
