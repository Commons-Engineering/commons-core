# Boot Guide — Commons OS

**The comprehensive guide to activating your commons after forking.**

Booting a commons is not a quick setup wizard — it is the founding act. The quality of your boot determines everything that follows. Take your time. The Purpose Agent guides you through this process, but you are the founder. Challenge the agent. Argue. Iterate. The agent's job is to help you think clearly, not to fill in blanks.

---

## Step 0 — First, make sure this is the founder's *own* commons

**Agent: do this before anything else.** Commons OS is a shared, upstream **base**. It must **never** be founded, configured, or have its identity / `AGENT.md` / blueprint filled in **in place**. Founding belongs only to a commons the founder **owns** — a template copy or fork of Commons OS, or a venture instance.

### Detect where you are (clone-safe)

Use a signal that does **not** travel with a clone, so a legitimate fork is never mislabelled:

```bash
gh repo view --json isTemplate,nameWithOwner 2>/dev/null   # when gh is available
git remote get-url origin                                  # always available
```

You are in the shared **upstream/template** if **either**:
- `isTemplate` is `true`, **or**
- the origin URL **contains the substring** `Commons-Engineering/commons-core` or `Commons-Engineering/commons-os` (the repository was renamed; both forms occur) — match it as a substring so **every** URL form counts: HTTPS, SSH, and the browser sandbox's proxy form (e.g. `http://local_proxy@127.0.0.1:…/git/Commons-Engineering/commons-os`).

If neither holds (a repo the founder owns), proceed to Prerequisites and boot normally.

### If you ARE in the upstream/template — carry the founder into their own commons

Do not stop dead, and do not found here. **The remedy depends on your environment — choose the right one, or you will emit a command that fails:**

**A) Local shell with `gh` available** (the installer path): create their own copy and move into it, then continue in this same session:
```bash
gh repo create <their-account>/<name> --template Commons-Engineering/commons-os --private --clone
cd <name>
```
(`--public` if they chose public. A venture instance under their workspace is an equally valid alternative.) You are now in *their* commons — continue with Prerequisites and the boot sequence **here**.

**B) Browser / sandboxed single-repo session** (Claude Code on the web): here `gh` is **not installed** and the session is bound to this one repo — you **cannot** run `gh repo create` and **cannot** `cd` into a new checkout. **Do not emit those commands.** Instead, guide the founder to make their own copy and re-enter:
1. Create a copy from the template — simplest is the **"Use this template"** button: `https://github.com/Commons-Engineering/commons-os/generate` (or, if a GitHub connector/MCP is available to you, create it that way). Have them name it and choose private/public. **Creating the repo does not let you continue here** — this session stays bound to *this* repo and cannot switch to the new checkout, so step 2 is mandatory either way.
2. **Open a new session on that new repo** (pick it in the repo selector) and give the same instruction there.
3. That new session is in *their* commons — onboarding and BOOT run normally there.

Either way, everything you found belongs to **them**, never to the upstream base. This guard keys off the repository's **GitHub identity** (a template flag and owner that do **not** clone), never a file in the repo.

---

## Prerequisites

Before you begin:

| Prerequisite | Details |
|---|---|
| **Forked repository** | You have forked `commons-engineering/commons-os` and renamed it to `[your-commons]` |
| **AI agent connected** | Any model that speaks MCP — configured with your agent file |
| **Agent configuration** | You have copied `AGENT.md.template` to `AGENT.md` and filled in the placeholders. `AGENT.md` is the OS-standard — how you wire it to your AI tool is up to you |
| **Time commitment** | Plan 2-4 hours for a thorough boot. This is a founding conversation, not a checkbox exercise |

### Wiring AGENT.md to Your AI Tool

`AGENT.md` is the OS-standard governance file. Your AI tool needs to find it. Create a thin pointer file for your tool that delegates to AGENT.md:

| Tool | Pointer file | Content |
|---|---|---|
| Claude Code | `CLAUDE.md` | `Read and follow AGENT.md — this is the governance configuration for this commons.` |
| Cursor | `.cursorrules` | `Read and follow AGENT.md — this is the governance configuration for this commons.` |
| Other | As required | Same pattern: point to `AGENT.md` |

The pointer file is **not** part of the OS template — it is tool-specific and created by the founder. Never duplicate governance content into the pointer file.

---

## What the Agent Must Do Before Starting

**Agent:** Before guiding the founder through the boot sequence, you must prepare yourself thoroughly. This is not optional.

### 0. Internalise the Commons Definition

Read this first. Before anything else. This is your north star:

> **A commons systematically creates value that is alive, shared, just, and is built to last.**

Source: `commons/patterns/principles/the-commons.md` — the Orbit 1 pattern. Read the full pattern. Understand the five qualities: **systematically, alive, shared, just, built to last.** Every question you ask during boot, every recommendation you make — all must serve these five qualities.

### 1. Read the Architecture

Read these documents in order. Do not proceed until you understand the system:

| Document | Why |
|---|---|
| `commons/patterns/principles/the-commons.md` | **The canonical commons definition.** The foundation of everything. |
| `commons/patterns/singularity/the-singularity.md` | The origin point. Why any commons exists. |
| `.commons/identity.yml` | Understand who this specific commons claims to be |
| `blueprint.md.template` | The universal L1–L9 skeleton you will help populate. Domain-specific filled variants live in `extensions/{provider}/{domain}-essentials/templates/blueprint.md` — pick the one matching the domain in `.commons/identity.yml`. |
| `commons/manifests/COMMONS_OS_MANIFEST.md` | The OS architecture — §1 anchors the commons definition |
| `commons/manifests/COMMONS_AGENT_MANIFEST.md` | Your role as Purpose Agent and the 4-agent board |
| `commons/manifests/COMMONS_ENGINEERING_MANIFEST.md` | The field: First Principles, First Practices, Vitality, the four domains |
| `commons/manifests/COMMONS_TAXONOMY_MANIFEST.md` | How patterns are organised. Orbit 2 = the commons attractor. |
| `commons/specs/COMMONS_OS_SPEC.md` | Technical specification — directory structure, layers, lifecycle |
| `commons/specs/PATTERN_SPEC.md` | How patterns work — orbital layers, frontmatter, body |
| `ALIGN.md` | The alignment checks you will run |

### 2. Understand the Four Dimensions

You govern from D1 but must think across all four — and through all five qualities:

| Dimension | What you watch for during boot | Commons quality check |
|---|---|---|
| **D1 — Identität & Bestimmung** | Is the purpose clear? Is the boundary defined? Is the domain chosen deliberately? | *Is this purpose alive — felt by participants, not just written?* |
| **D2 — Partizipation & Beziehung** | Who are the stakeholders? Who is missing? Are non-human participants considered? | *Is participation shared — or does one voice dominate?* |
| **D3 — Proposition & Austausch** | What value does this commons create? For whom? What is exchanged? | *Is the exchange just — fair to all participants, especially the voiceless?* |
| **D4 — Produktion & Resilienz** | What infrastructure exists? What needs to be built? What are the risks? | *Is the production built to last — or does it depend on one person, one funder, one tool?* |

### 3. Prepare Domain Context

Based on the domain in `identity.yml`, prepare the relevant value stream families:

| Domain | Default Value Stream Families |
|---|---|
| **Life** | Personal purpose, relationships, health, learning, livelihood |
| **Business** | *(13 canonical families — Commons Value-Creation Canon)* Perception to Mandate · Purpose to Portfolio, Value to Sustainability, Portfolio to System · Participant to Community, Collaboration to Automation, Contributor to Succession · Discovery to Usage, Interest to Relationship, Proposition to Audience · Demand to Fulfillment, Source to Alliance, Acquire to Retire |
| **Urban** | Place identity, citizen participation, urban services, urban metabolism, spatial planning |
| **Ecology** | Ecosystem identity, species participation, ecosystem services, biogeochemical cycles |

### 4. Set Your Tone

- Speak in the locale defined in `identity.yml`
- Be a thought partner, not a form-filler
- Ask probing questions — "Why does this commons exist?" is more important than "What is the name?"
- Challenge weak answers. A vague purpose produces a vague commons
- Celebrate strong answers. Founding a commons is an act of courage

---

## The Boot Sequence

### Phase 1: Identity (L1 of the Blueprint)

**Goal:** Establish who this commons is with absolute clarity.

1. **Edit `.commons/identity.yml`**

   Fill in every field deliberately:

   | Field | Guidance |
   |---|---|
   | `slug` | Your commons identifier (e.g., `luebeck-os`, `my-life`, `acme-commons`) |
   | `name` | Human-readable name — this is what people will see |
   | `purpose` | One sentence: what this commons exists to do. This is the hardest field. Spend time here |
   | `domain` | Life, Business, Urban, or Ecology. This loads domain-specific value stream families |
   | `locale` | Your primary language. Determines all downstream communication |
   | `founder` | Your identifier |
   | `stage` | Set to `Boot` |

2. **Initialise `blueprint.md` from the appropriate template, then fill in L1 (Identity & Purpose)**

   Choose the template that matches the domain in `.commons/identity.yml`:

   | Domain | Source template | What's pre-filled |
   |---|---|---|
   | Life | `extensions/cloudsters/life-essentials/templates/blueprint.md` | Purpose Spiral, life-engineering value streams |
   | Business | `extensions/cloudsters/business-essentials/templates/blueprint.md` | C\|EN cascade, 13 canonical families + D0, stakeholder maps |
   | Urban | `extensions/cloudsters/urban-essentials/templates/blueprint.md` | Place patterns, citizen participation models |
   | Ecology | `extensions/cloudsters/ecology-essentials/templates/blueprint.md` | Watershed structures, species-participation patterns |
   | (none of the above) | `blueprint.md.template` (universal hull skeleton) | L1–L9 skeleton only |

   Copy the chosen file to `blueprint.md` in the repo root. From this moment on, `blueprint.md` is **instance-owned** — upstream substrate sync will never overwrite it (see `ALIGN.md` instance-sovereignty rule).

   The agent guides you through:
   - **1.1 Who We Are** — Name, purpose, domain, boundary, founding story
   - **1.2 The Imperative** — What century-defining challenge does this commons address? Why is the status quo not good enough?
   - **1.3 Values & Commitments** — What non-negotiable commitments does this commons make?
   - **1.4 Purpose Spiral** — How the four dimensions manifest in THIS commons

   **Do not proceed to Phase 2 until L1 is articulated clearly.** L1 constrains everything below it.

### Phase 2: Stakeholders & Value (L2-L3 of the Blueprint)

**Goal:** Map who participates and what value is created.

3. **Fill in L2 (Stakeholders & Participation)**
   - Who are the stakeholders? Map them: human, organisation, agent, ecosystem
   - What are the participation paths? Observer → Participant → Steward → Founder
   - Which non-human participants matter? AI agents, ecological systems, institutional actors

4. **Fill in L3 (Value Proposition & Exchange)**
   - What does a stakeholder gain that they cannot get elsewhere?
   - Apply the Apple Test: what is the juiciest proposition?
   - How does value flow? Monetary, knowledge, attention, stewardship, ecological service?

5. **The agent proposes initial value stream families** based on your domain and purpose. Discuss, adapt, accept or reject.

### Phase 3: First Entity

**Goal:** The commons registers itself as its first entity.

> **Note:** We temporarily skip L4 (Journeys) and L5 (Value Streams) in the blueprint to immediately register the commons itself as a living entity. You need a registered actor before you can build value streams. We return to L4-L5 in the Seed stage.

6. **Create the commons entity** in `instance/registry/5_entities/purpose/`
   - The commons itself is its first entity — the self-reference that makes the system alive
   - Set `self_entity_slug` in `identity.yml` to point here
   - The agent helps you fill in the entity fields: type, role, dimension alignment

### Phase 4: Connect Intelligence

**Goal:** Wire the commons to shared and local knowledge.

7. **Configure MCP connections** in `.commons/config.yml`

   | Channel | What it provides | Action |
   |---|---|---|
   | **Commons MCP** | Shared pattern library, cognitive services, collections | Default endpoint works for OPEN tier |
   | **Blueprint MCP** | Local knowledge graph, workspace queries | Configure if available |
   | **Fabric MCPs** | Your systems of record (ERP, CRM, HR, etc.) | Add as your systems are connected |

### Phase 5: Seed

**Goal:** Transition from Boot to Seed — the commons begins to grow.

8. **Review the boot work**
   - Agent runs alignment checks (`ALIGN.md`)
   - Review L1-L3 of the blueprint together
   - Confirm the entity registration is correct
   - Verify MCP connections respond

9. **Change stage to `Seed`** in `identity.yml`

10. **The agent begins active support:**
    - Suggesting patterns from the library that match your purpose and domain
    - Proposing value stream structures
    - Helping you build the blueprint layer by layer (L4-L9)
    - Identifying gaps and proposing next steps

---

## Lifecycle After Boot

| Stage | What happens | Typical duration |
|---|---|---|
| **Fork** | Repository forked, not yet configured | Minutes |
| **Boot** | Identity established, L1-L3 populated, first entity registered | Hours to days |
| **Seed** | Blueprint grows (L4-L9), patterns applied, value streams take shape | Weeks to months |
| **Active** | Regular operations, rhythms established, touchpoints live | Months |
| **Gathering** | First community event, commons touches the physical world | Months to years |
| **Established** | Self-sustaining operations, multiple active participants | Years |
| **Mature** | Full governance runtime, contribution back to upstream | Ongoing |

---

## Common Boot Mistakes

| Mistake | Why it matters | What to do instead |
|---|---|---|
| Rushing L1 | A vague purpose produces a vague commons. Everything downstream inherits the ambiguity | Spend real time on purpose. Argue with the agent. Iterate until it rings true |
| Skipping stakeholder mapping | You cannot create value for people you haven't identified | Map all four types: human, organisation, agent, ecosystem |
| Ignoring non-human participants | Commons Engineering includes AI, species, and ecological systems as participants | Explicitly name them in L2, even if the list is short |
| Copying another commons' blueprint | Your commons has its own identity. Templates show structure, not content | Use the structure, but write your own story |
| Not connecting MCP | Without shared intelligence, your commons operates in isolation | At minimum, connect Commons MCP (OPEN tier is free) |

---

## What to Read Next

| Document | When to read it |
|---|---|
| `ALIGN.md` | After boot — run your first alignment check |
| `instance/operations/rhythms.md` | When establishing regular operations (Seed stage) |
| `commons/patterns/` | When looking for patterns to apply |
| `CONTRIBUTING.md` | When you have improvements to contribute back upstream |

---

*BOOT GUIDE v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
