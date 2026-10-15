#!/usr/bin/env bash
# ============================================================
#  Commons Engineering - cloud workspace setup (Codespaces)
#
#  The cloud equivalent of the local one-click installer. It runs once when
#  the Codespace is created, so a newcomer is work-capable entirely in the
#  browser - nothing installed on their own machine.
#
#  The toolchain (git, gh, node, python) comes from devcontainer features;
#  the Claude Code VS Code extension from devcontainer.json. This script adds
#  the Claude Code CLI and a tool pointer so the agent knows its mission.
# ============================================================
set -e

echo "Setting up your Commons Engineering cloud workspace..."

# Claude Code CLI (the VS Code extension is installed via devcontainer.json).
if ! command -v claude >/dev/null 2>&1; then
  echo "  - installing Claude Code CLI ..."
  curl -fsSL https://claude.ai/install.sh | bash || true
fi

# Drop a tool pointer at the workspace root so the agent picks up its mission.
# CLAUDE.md is git-ignored (it's a tool pointer, not OS template content).
WS="${CODESPACE_VSCODE_FOLDER:-$PWD}"
cat > "$WS/CLAUDE.md" <<'EOF'
# Commons Engineering - cloud setup session

You are running inside a **Commons Core Codespace** in the browser. Commons Core
is ALREADY here (this very workspace) - do NOT clone it again.

Read commons/setup/ONBOARDING.md and execute it to make me work-capable, with
this adjustment for the cloud context:
- Skip the "clone Commons Core" step - you are already inside it. Set up my
  venture instance(s) under this workspace instead.
- GitHub is usually already signed in here (check `gh auth status`); use it to
  see what I can reach.
- Set my Git identity, connect the Commons MCP, and handle the federation step.

I am new and may be non-technical. Guide me warmly, do the technical work
yourself, and explain anything I ask. When setup is done, the founding
conversation is BOOT.md.
EOF

echo "Cloud workspace ready. Open the Claude panel and say hello."
