# Boot Guide — Commons Core

**The comprehensive guide to activating your commons once it has its own repository.**

Booting a commons is not a quick setup wizard — it is the founding act. The quality of your boot determines everything that follows. Take your time. The Purpose Agent guides you through this process, but you are the founder. Challenge the agent. Argue. Iterate. The agent's job is to help you think clearly, not to fill in blanks.

---

## Step 0 — First, make sure this is the founder's *own* commons

**Agent: do this before anything else.** Commons Core is a shared, upstream **base**. It must **never** be founded, configured, or have its identity / `AGENT.md` / blueprint filled in **in place**. Founding belongs only to a commons the founder **owns** — a template copy of Commons Core, or a venture instance.

### Detect where you are (clone-safe)

Use a signal that does **not** travel with a clone, so a legitimate fork is never mislabelled:

```bash
gh repo view --json isTemplate,nameWithOwner 2>/dev/null   # when gh is available
git remote get-url origin                                  # always available
```

You are in the shared **upstream/template** if **either**:
- `isTemplate` is `true`, **or**
- the origin URL **contains the substring** `Commons-Engineering/commons-core` or `Commons-Engineering/commons-os` (the repository was renamed; both forms occur) — match it as a substring so **every** URL form counts: HTTPS, SSH, and the browser sandbox's proxy form (e.g. `http://local_proxy@127.0.0.1:…/git/Commons-Engineering/commons-os`).

If neither holds (a repo the founder owns), make sure the commons has declared what it is and installed its content — `domain` and `instance_type` in `.commons/identity.yml`, then **Install** (Actions → Install → Run workflow, or `python .commons/scripts/install.py`). Then proceed to Prerequisites and boot normally.

### If you ARE in the upstream/template — carry the founder into their own commons

Do not stop dead, and do not found here. **The remedy depends on your environment — choose the right one, or you will emit a command that fails:**

**A) Local shell with `gh` available** (the installer path): create their own copy and move into it, then continue in this same session:
```bash
gh repo create <their-account>/<name> --template Commons-Engineering/commons-core --private --clone
cd <name>
```
(`--public` if they chose public. A venture instance under their workspace is an equally valid alternative.) You are now in *their* commons — have them declare `domain` and `instance_type` in `.commons/identity.yml`, run `python .commons/scripts/install.py`, then continue with Prerequisites and the boot sequence **here**.

**B) Browser / sandboxed single-repo session** (Claude Code on the web): here `gh` is **not installed** and the session is bound to this one repo — you **cannot** run `gh repo create` and **cannot** `cd` into a new checkout. **Do not emit those commands.** Instead, guide the founder to make their own copy and re-enter:
1. Create a copy from the template — simplest is the **"Use this template"** button: `https://github.com/Commons-Engineering/commons-core/generate` (or, if a GitHub connector/MCP is available to you, create it that way). Have them name it and choose private/public. **Creating the repo does not let you continue here** — this session stays bound to *this* repo and cannot switch to the new checkout, so step 2 is mandatory either way.
2. **Open a new session on that new repo** (pick it in the repo selector) and give the same instruction there.
3. That new session is in *their* commons — onboarding and BOOT run normally there.

Either way, everything you found belongs to **them**, never to the upstream base. This guard keys off the repository's **GitHub identity** (a template flag and owner that do **not** clone), never a file in the repo.

---

---

## Prerequisites

Before you begin:

| Prerequisite | Details |
|---|---|
| **Your repository** | Created from `Commons-Engineering/commons-core` with **Use this template**; `domain` and `instance_type` declared in `.commons/identity.yml`; the **Install** workflow run once |
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
| `blueprint.md.template` | The universal L1–L9 skeleton you will help populate. The domain's own template is `extensions/{provider}/{domain}-essentials/blueprint.template.md`, installed with the one essentials pack that matches the domain in `.commons/identity.yml`. |
| `commons/manifests/COMMONS_CORE_MANIFEST.md` | The architecture of the Commons Core — §1 anchors the commons definition |
| `commons/manifests/COMMONS_AGENT_MANIFEST.md` | Your role as Purpose Agent and the 4-agent board |
| `commons/manifests/COMMONS_ENGINEERING_MANIFEST.md` | The field: First Principles, First Practices, Vitality, the four domains |
| `commons/manifests/COMMONS_PATTERNS_MANIFEST.md` | How patterns are organised. Orbit 2 = the commons attractor. |
| `commons/specs/COMMONS_CORE_SPEC.md` | Technical specification — directory structure, layers, lifecycle |
| `commons/specs/COMMONS_PATTERNS_SPEC.md` | How patterns work — orbital layers, frontmatter, body |
| `ALIGN.md` | The alignment checks you will run |

### 2. Understand the Five Dimensions

You govern from D1 but must think across all five — and through all five qualities:

| Dimension | What you watch for during boot | Commons quality check |
|---|---|---|
| **D0 — Perception & Identity** | Does the commons see itself as a whole? Who grants it the right to exist — its mandate, and from whom? | *Is the mandate held — or merely assumed?* |
| **D1 — Purpose & System** | Is the purpose clear? Is the boundary defined? Is the domain chosen deliberately? | *Is this purpose alive — felt by participants, not just written?* |
| **D2 — Participation & Relationship** | Who are the stakeholders? Who is missing? Are non-human participants considered? | *Is participation shared — or does one voice dominate?* |
| **D3 — Proposition & Exchange** | What value does this commons create? For whom? What is exchanged? | *Is the exchange just — fair to all participants, especially the voiceless?* |
| **D4 — Production & Resilience** | What infrastructure exists? What needs to be built? What are the risks? | *Is the production built to last — or does it depend on one person, one funder, one tool?* |

### 3. Prepare Domain Context

Based on the domain in `identity.yml`, prepare the value model of that domain. Every domain shares the same
thirteen value-stream families of the canon (`commons/specs/value-creation-canon.yml`); what differs is the value
streams beneath them, which the installed essentials pack proposes:

| Domain | Essentials pack | What it proposes |
|---|---|---|
| **Business** | `extensions/cloudsters/business-essentials/` | the value streams of an enterprise of any size, legal form or industry |
| **Health** | `extensions/cloudsters/health-essentials/` | the value streams of a hospital, a hospital group or a care network — care, research, teaching and the enterprise that carries them |
| **Life** | `extensions/cloudsters/life-essentials/` | the value streams of a person's or a household's life |
| **Place** | `extensions/cloudsters/place-essentials/` | the value streams of a commons place — a building or site run with its community |
| **Urban** | `extensions/cloudsters/urban-essentials/` | the value streams of a city or a region |
| **Ecology** | `extensions/cloudsters/ecology-essentials/` | the value streams of an ecosystem |

The pack's `MANIFEST.md` says what it carries and how it comes alive in a house.

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

   | Domain | Source template |
   |---|---|
   | Business · Health · Life · Place · Urban · Ecology | `extensions/cloudsters/{domain}-essentials/blueprint.template.md` of the installed pack |
   | (none of the above) | `blueprint.md.template` (universal hull skeleton), L1–L9 skeleton only |

   Copy the chosen file to `blueprint.md` in the repo root. From this moment on, `blueprint.md` is **instance-owned** — upstream substrate sync will never overwrite it (see `ALIGN.md` instance-sovereignty rule).

   The agent guides you through:
   - **1.1 Who We Are** — Name, purpose, domain, boundary, founding story
   - **1.2 The Imperative** — What century-defining challenge does this commons address? Why is the status quo not good enough?
   - **1.3 Values & Commitments** — What non-negotiable commitments does this commons make?
   - **1.4 Purpose Spiral** — How the five dimensions manifest in THIS commons

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

6. **Create the commons entity** in `instance/registry/7_entities/`
   - The commons itself is its first entity — the self-reference that makes the system alive
   - Set `self_entity_slug` in `identity.yml` to point here
   - The agent helps you fill in the entity fields: type, role, dimension alignment

### Phase 4: Connect Intelligence

**Goal:** Wire the commons to shared and local knowledge.

7. **Configure MCP connections** in `.commons/config.yml`

   | Channel | What it provides | Action |
   |---|---|---|
   | **Commons MCP** | Shared pattern library, cognitive services, collections | Served by ring — the OPEN ring is the default |
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
| **Fork** | Repository created from the template, not yet booted | Minutes |
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
| Not connecting MCP | Without shared intelligence, your commons operates in isolation | At minimum, connect the Commons MCP |

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
