# Installation Guide

A walk-through of what happens when you set up your Commons Engineering working environment — for the human, not the agent. Tells you what the installer does, what you'll see, what decisions you'll make along the way, and what the workspace looks like when it's done. Read it once before you start, or alongside the install. The agent reads its own copy (`ONBOARDING.md` in the same folder) — this is yours.

---

## 1. The picture

You are setting up three things that work together — the **triad**:

| Corner | What it is | Where it lives |
|---|---|---|
| **You (the person)** | your identity — Git, GitHub, your cloudsters/Claude accounts | your machine and your browser |
| **Your instance** | your own Commons OS workspace + venture instances | your account on GitHub, mirrored to your local disk |
| **The knowledge graph** | the living body of knowledge of the discipline | a shared online service (the Commons MCP) |

The **agent** (Claude Code by default) is the living connection between them. Once it's running, you talk to it in plain language — it does the technical work for you.

---

## 2. Pick your door

Three ways in. Pick the one that fits your machine — they all end at the same place.

| Door | When to use it | How to start |
|---|---|---|
| **Windows installer** | your own Windows PC (Win 10/11) | Download `commons-setup.cmd` and double-click. ([raw URL](https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/commons-setup.cmd)) |
| **macOS installer** | your own Mac | Open Terminal (⌘+Space → "Terminal") and paste:<br>`bash <(curl -fsSL https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/commons-setup.command)`<br>The parentheses `<(...)` are essential — they keep your terminal connected so Homebrew and `sudo` can ask for your password if needed. |
| **Browser (zero install)** | locked-down or shared machine, no install rights | Open `commons-os` in [claude.ai/code](https://claude.ai/code) (Anthropic-hosted) or via the **Open in Codespaces** badge in the README. Nothing touches your machine. |

If you're on Windows and the installer launches but exits in a couple of seconds, you almost certainly need administrator rights on that machine to install software — use the **Browser** door instead. Same for any locked-down corporate laptop.

---

## 3. What the installer does for you (automatic)

The installer handles everything that can be automated. You don't need to understand or memorise this — it's listed so you know what's happening when you see the progress.

| Step | What it does |
|---|---|
| **Package manager** | Installs Homebrew (macOS) or makes sure winget (Windows) is present. This is the tool the installer uses to pull all the other tools cleanly. |
| **Toolchain** | Installs `Git`, the GitHub CLI (`gh`), Node.js, Python 3.12, and Visual Studio Code. Each one takes 1–3 minutes; large downloads are normal. |
| **Agent trio** | Installs the **Claude Desktop app** (your GUI agent), the **Claude Code CLI** (the engine, used for some setup tasks), and the **Claude Code extension** in VS Code. |
| **Workspace folder** | Creates a small setup folder (`repos/commons-setup`) with the procedure file the agent will follow. |
| **Hand off** | Opens that folder in Finder/Explorer and starts the Claude Desktop app. From here on, you talk to the agent. |

You don't need to keep the terminal in focus during these steps. Leave it open and let it work — the toolchain installs alone take roughly 5–10 minutes depending on your connection.

A detailed log of everything the installer did is saved at `~/commons-setup.log` (macOS) or `%TEMP%\commons-setup-log.txt` (Windows). If anything goes wrong, that file is what you (or a helper) needs to look at.

---

## 4. What the agent does — and the four small decisions you'll make

Once the installer hands off to the Claude Desktop app, the agent reads `ONBOARDING.md` from the setup folder and walks you through the rest. It does the technical work; you make four conscious decisions along the way.

### Decision 1 — Sign in to your accounts

Three sign-ins, all in the browser, all one-time:

| Account | When | Why |
|---|---|---|
| **Claude** | first time the Claude app starts | The agent itself needs an account. If you don't have one, click *Sign up* on the same screen. |
| **GitHub** | the agent prompts via `gh auth login` | Lets the agent see and use *your* repositories. You authorise it once; the permission lives in your GitHub account, not in the agent. |
| **Commons MCP** (cloudsters / federation members) | when the MCP step runs | Your tier in the knowledge graph is decided by your federation identity. If you don't have one, this step is skipped. |

For GitHub specifically: the agent uses **your** GitHub account, so any repository *you* can see, *it* can see. That includes repos in organisations you belong to (e.g. `cloudsters-EUROPE`). If an organisation has restricted third-party app access, you may need to ask an owner of that org to approve the GitHub App once.

### Decision 2 — Create your own commons (don't found the upstream)

`Commons-Engineering/commons-os` is the **shared base** for the whole network. Nobody founds it directly. To start your own commons, you need a copy that you own — the agent will help you make one.

What happens:

1. The agent notices it's sitting in the upstream and **does not** try to configure it in place. (There's a safety guard at the top of `BOOT.md` that detects this.)
2. It asks you for a **name** (e.g. `acme-commons`, `luebeck-os`, `my-life`) and whether the new repo should be **private** (recommended) or **public**.
3. It creates the new repo from the template into your GitHub account (`<your-account>/<your-name>`) using `gh repo create … --template … --clone`. On the browser door (claude.ai/code) the agent guides you to use GitHub's **"Use this template"** button instead, and to open a fresh session on the new repo.
4. From then on you're working in *your* commons. You can boot it, configure it, fill in the blueprint — all without touching the upstream.

### Decision 3 — Pick the ventures the workspace should know about

A **venture** is a concrete thing you build (a business, a place, a life-system) — modelled as its own repo, named `<venture>.o` (operations) and optionally `<venture>.g` (governance / future scenarios). Each venture is sovereign — it has its own identity, its own agent configuration, its own blueprint.

When the agent inspects your GitHub account it lists what it can see and asks which ones to bring into your local workspace alongside your commons. Typical patterns:

- a single founder → one personal commons + one or two venture instances
- a cloudsters Commons Incubator → the federation venture (`cloudsters/…`) plus the incubator's own `.o` and `.g`
- an organisation → one organisational commons + per-domain ventures

You don't have to decide all of this now. You can add ventures later (`gh repo clone …` into the workspace, or ask the agent to do it).

### Decision 4 — Federation membership (cloudsters members only)

If your GitHub account belongs to cloudsters orgs, the agent recognises you as a federation member and **asks** rather than acting. The cloudsters federation is a **membership journey** — identity, MFA, OPEN→PEER curriculum, regional Urban Commons — done with the community, not through an automated script. The agent walks you through what's relevant and what you should do *with* humans, not *via* code.

---

## 5. The folder structure you end up with

This layout is intentional. The agent moves between folders to compare ventures, share context, and keep your work organised:

```
~/repos/
├── commons-setup/        ← transient setup folder; agent removes it at the end
└── commons/              ← Commons OS, your base (this is YOUR commons after Decision 2)
    ├── commons/          ← the OS payload (manifests, patterns, specs, templates)
    ├── extensions/       ← bundled extension packs (commons-engineering, cloudsters, ...)
    ├── instance/         ← your sovereign instance content
    ├── .commons/         ← your identity (slug, name, purpose, domain, locale)
    ├── BOOT.md, ALIGN.md, blueprint.md ...
    ├── <venture-1>.o/    ← a venture you brought in
    ├── <venture-1>.g/
    └── <venture-2>.o/
```

The agent treats this hierarchy as load-bearing: it knows where to find the OS, where to find your ventures, where it owns content vs. where you do. Don't rename or restructure these top-level folders by hand — let the agent do it. (If you reorganise, the agent can still figure it out, but it gets noisier.)

---

## 6. After the setup — using it day-to-day

| Task | How |
|---|---|
| Start a working session | Open **Claude** (the Desktop app). Choose *Open folder* → pick `~/repos/commons/<the commons or venture you want to work on>`. The agent loads that context (its `AGENT.md`) and you talk to it. |
| Switch between ventures | Open a different folder in the Claude app — `~/repos/commons/<other venture>`. The agent picks up the new context automatically. |
| Code edits with diffs | Use the **Claude Code extension** in VS Code — open the same folder there for inline diffs and side-by-side editing. |
| Run the installer again | Safe to do. All steps are idempotent: tools already present are skipped, the agent picks up where it left off. Useful if something failed mid-way. |
| Pull upstream Commons OS updates | Happens **automatically** via a weekly sync workflow in your commons repo. It opens a PR with the OS-layer changes; you review and merge. Your instance content is never touched. |

---

## 7. Common questions and small troubles

**The installer exits after a few seconds without doing anything.**
Most likely cause on macOS: you have no administrator rights on the machine (Homebrew can't install). Use the browser door instead. On Windows: the same situation usually shows up as a permission prompt that's been denied — also switch to browser.

**Homebrew asks me for a password and nothing shows when I type.**
That's correct. `sudo` (the macOS admin tool) deliberately doesn't echo the password — no dots, no stars, nothing. Type your Mac login password as if you can see it, then press Return.

**The agent says "I can only see *some* of my repos."**
GitHub's app permission model: the Claude GitHub App only sees orgs/repos you've explicitly granted it. Go to **GitHub → Settings → Applications → Claude → Configure** and grant access to the missing orgs (or set to "All repositories"). For org-owned repos an org owner may need to approve the app for that org.

**The Claude app downloads even though I already have it.**
On macOS: fixed — the installer now adopts your existing `Claude.app` into Homebrew's management without re-downloading (`brew install --cask --adopt`).
On Windows: similar pre-check before `winget install` — if Claude is already system-registered, the re-download is skipped.

**I'm stuck somewhere not covered here.**
Send the install log (`~/commons-setup.log` or `%TEMP%\commons-setup-log.txt`) plus a sentence about what you were trying to do — that's enough to diagnose almost anything.

---

## 8. The one paragraph version

Pick your door (Windows / macOS / Browser). Run it once. Watch the toolchain install for a few minutes — large downloads are normal. The Claude app opens; sign in. The agent reads `ONBOARDING.md`, asks you four things — your accounts, the name for your own commons (it'll fork from the upstream template), which ventures to bring in, and (for cloudsters members) about federation. The workspace ends up at `~/repos/commons/` with your commons as the base and ventures inside it. From then on you work by opening that folder in the Claude app and talking to it. There's nothing else you need to read.
