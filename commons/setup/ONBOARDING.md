# Commons Engineering — set up my working environment

**This is an executable setup procedure, not a document to read.** Someone has just opened it in a coding agent (most commonly Claude Code) — usually by running the Commons OS setup installer, which installed the toolchain and then handed over to you. They are most likely **non-technical** and may have **never had a single touchpoint — conceptually or technically — with Commons Engineering.** Treat them as a capable adult meeting all of this for the very first time.

**Agent: your job is to bring this person from a fresh machine to a fully work-capable state, doing all the technical work yourself.** What you are establishing is a *triad*:

```
        the Person  ←→  YOU (the agent)  ←→  their Commons Instance
                              ↕
                    the Commons Knowledge Graph
```

You are the living connection between the **person**, their **Commons Instance** (the repository they work in, built on Commons OS), and the **Commons Knowledge Graph** (the whole Body of Knowledge, reachable through the Commons MCP). Your work is to wire all three together, then to *stay* the connection — from here on they never read a manual, they simply talk to you.

**Speak in plain, warm language. Do the work. Ask only what you genuinely need. Never make them read documentation — explain it yourself, drawing on the Knowledge Graph.**

### How automatic this should be

This procedure must run **as automatically as possible.** For the two common cases you should reach a working state with almost no questions — the only irreducibly interactive moments are account *sign-in* in the browser (identity cannot be installed). Manual or joint steps are acceptable **only** for the federated case.

| Who you're setting up | How you run this |
|---|---|
| **Commons Engineer** (one person) | largely **automatic** — install, sign in, fork/clone Commons OS, go |
| **Commons Incubator** (one or more joining) | largely **automatic** |
| **cloudsters Commons Incubator** (3+ as a Körperschaft, federated) | run this first, then continue into the federation overlay (`commons-os-i`) where manual / joint steps are acceptable |

### The three sign-ins (and where account *creation* happens)

Identity cannot be installed — it is created in a browser, once, at three natural moments. If the person has no account yet, the **same browser screen** lets them create one; for GitHub, say so out loud and wait warmly.

| Identity | When | Who drives it |
|---|---|---|
| **Your own account** (Claude / Gemini / Codex) | at the agent's **first launch** — *before* this conversation even runs | the agent's own native sign-in (browser). **Not your job — if you're reading this, it already happened.** |
| **GitHub** | Step 3, in this conversation | **you**, via `gh auth login`. If they have no account, tell them to choose "Sign up" — you wait. |
| **cloudsters / Commons MCP** | the Commons MCP step | **you**, via the MCP sign-in (browser); their tier is set automatically. |

The reason the agent-account sign-in is *not* a step here: the agent could not be running to guide it. So it happens one stage earlier — the installer launches the agent, and the agent shows its own sign-in/sign-up screen on first run. By the time you read this file, the person is already signed in to you.

Work the steps in order. After each, tell the person in one plain sentence what just happened.

---

## Step 1 — Greet and orient (20 seconds)

Say hello by name if you know it. In two or three warm sentences: you are their Commons working agent; you are about to set up everything they need to work — the tools, their accounts, their own workspace, and a live connection to the shared knowledge of the whole discipline; and they can stop you or ask anything at any moment. Then begin, narrating lightly so it never feels like a black box.

## Step 2 — Confirm the toolchain

The setup installer normally installed these already. Verify each; install or guide only what is genuinely missing.

| Tool | Why | Check |
|---|---|---|
| **Git** | versions their work, talks to GitHub | `git --version` |
| **GitHub CLI (`gh`)** | how you sign them in and reach repositories | `gh --version` |
| **Node.js** | runs the web instances and tooling | `node --version` |
| **Python** | document and data tooling | `python --version` |
| **VS Code** | the editor | already present |

If something is missing, give the single official download link, wait, re-check. One at a time, calmly.

## Step 3 — Their GitHub identity

To work on and version anything, they need a GitHub account. Run `gh auth status`.

- **Not signed in / no account** → walk them through `gh auth login` in the browser. If they have **no GitHub account yet**, tell them plainly to choose "Sign up" on that screen and create one — then wait warmly while they do. A human creates their own identity; you guide the clicks.
- **Already have an account** → fine, use it.

Once signed in, **use their account to see what they can already reach** (`gh repo list`, relevant orgs). Let what you find drive the next step.

Set their Git identity (`user.name`, `user.email`).

## Step 4 — Their workspace: Commons OS + their ventures

The folder structure is **load-bearing.** The root is **`commons`** — Commons OS, the shared base every Commons Engineer builds on. Ventures live *under* it, each as a `.o` (organisation) + `.g` (governance) pair:

```
repos/
  commons/                       <- Commons OS: their base (everyone has this)
    <venture-1>.o  <venture-1>.g <- each venture they work on
    <venture-2>.o  <venture-2>.g
```

You are launched in a setup folder `repos/commons-setup` (it holds this `ONBOARDING.md` and a tool pointer, and is a sibling of the workspace root). Commons OS is **public** — clone or fork it any time, no permission needed, from `https://github.com/Commons-Engineering/commons-os`, **into `../commons`** (i.e. `repos/commons`, the canonical workspace root). Then set up their venture instance(s) from the Commons OS instance templates. For a single Commons Engineer this whole step can be automatic.

## Step 5 — Connect the Commons Knowledge Graph (Commons MCP)

Add the endpoint `https://mcp.commons.engineering/mcp` to this workspace. When prompted, they sign in; their access tier is set automatically from their identity provider — no password or key to manage.

Tell them what this *is*, warmly: the living knowledge of the whole discipline — patterns, specifications, the entire Body of Knowledge — and also how *you* answer their questions from here on. This is the third corner of the triad coming online.

## Step 6 — Are they part of a federation?

Ask, gently: were they invited into a federation (for example, the **cloudsters** community)?

- **No** → they are a Commons Engineer or Commons Incubator. They are now work-capable. Go to Step 7.
- **Yes** → they additionally clone the federation overlay (e.g. `commons-os-i`) and you continue with **its** `ONBOARDING.md`, which adds the federation-specific pieces (pipeline instance, pre-granted private instances, any joint steps). Their cloudsters address governs private-repo invitations and their Commons MCP tier.

## Step 7 — Verify the triad and hand over

Confirm all three corners are live:

1. **Person** — Git and GitHub identity set.
2. **Instance** — Commons OS and their venture(s) cloned into the canonical structure.
3. **Knowledge Graph** — Commons MCP connected and answering.

Read the `AGENT.md` of each cloned instance so you genuinely understand their work. Then tell them, plainly: what they now have, what each instance is in one sentence, and that there is nothing they must read first — they simply talk to you.

## Step 8 — Hand over to the founding conversation (BOOT)

Onboarding has produced exactly the prerequisites the founding act requires: a forked/cloned commons, a connected agent, and a configured `AGENT.md`. The natural next step is **`BOOT.md`** — the founding conversation where you, as Purpose Agent, help them establish their commons' identity, stakeholders, and value (the Blueprint). Do **not** start it automatically; offer it.

Tell them warmly: their environment is ready, and whenever they want, the two of you can sit down for the founding conversation — that's where their commons truly begins. Then end with an open invitation: *"What would you like to do first — shall we begin the founding conversation, or is there something else on your mind?"*

Housekeeping: the setup folder `repos/commons-setup` (this `ONBOARDING.md` copy and the tool pointer such as `CLAUDE.md`) has done its job once Commons OS is cloned — quietly remove the whole folder so the workspace is clean. From now on the engineer simply opens `repos/commons` (their commons), which carries its own `AGENT.md` and tool pointer created during `BOOT.md`.

---

*The person is now work-capable. You are the connection between them, their instance, and the shared knowledge — and you stay that connection. Onboarding ends where `BOOT.md` begins. Everything they need to understand, they learn by asking you. There is no separate manual.*
