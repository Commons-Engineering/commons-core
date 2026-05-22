#!/bin/bash
# ============================================================
#  Commons Engineering - set up my working environment  (macOS)
#
#  A newcomer double-clicks this one file. It installs the
#  toolchain, lets them pick an AI coding agent, then hands
#  over to that agent, which does the conversational part
#  (identity, GitHub, cloning, Commons MCP) by talking to them.
#
#  No terminal knowledge required. One double-click.
#  (If macOS blocks it: right-click -> Open, once.)
# ============================================================

set -u

echo ""
echo "  Welcome to Commons Engineering."
echo "  I'm setting up everything you need to work. This takes a few minutes."
echo ""

# --- 0. Homebrew present? (the macOS package installer) ---------------------
if ! command -v brew >/dev/null 2>&1; then
  echo "  Installing Homebrew (the package installer)..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
# Make brew + its installed tools available in this session (Apple Silicon + Intel).
[ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
[ -x /usr/local/bin/brew ]   && eval "$(/usr/local/bin/brew shellenv)"

install_formula () {  # $1 = formula, $2 = friendly name
  if brew list "$1" >/dev/null 2>&1; then echo "  - $2 already present."
  else echo "  - Installing $2 ..."; brew install "$1" >/dev/null 2>&1; fi
}
install_cask () {     # $1 = cask, $2 = friendly name
  if brew list --cask "$1" >/dev/null 2>&1; then echo "  - $2 already present."
  else echo "  - Installing $2 ..."; brew install --cask "$1" >/dev/null 2>&1; fi
}

# --- 1. The toolchain - deterministic, no judgement needed ------------------
echo "  Installing the tools the work runs on..."
echo ""
install_formula "git"         "Git (versions your work)"
install_formula "gh"          "GitHub CLI (reaches repositories)"
install_formula "node"        "Node.js (runs the web instances and agents)"
install_formula "python@3.12" "Python (document and data tooling)"
install_cask    "visual-studio-code" "VS Code (the editor)"
echo ""

# --- 2. Choose your AI coding agent(s) --------------------------------------
echo "  Which AI coding agent would you like? You can pick more than one."
echo ""
echo "    [1] Claude Code   (recommended)"
echo "    [2] Gemini CLI    (Google)"
echo "    [3] Codex CLI     (OpenAI)"
echo ""
read -r -p "  Enter numbers separated by spaces, or just press Return for Claude Code: " SEL
[ -z "${SEL:-}" ] && SEL="1"
echo ""

export PATH="$HOME/.local/bin:$PATH"
PRIMARY=""

install_claude () {
  if command -v claude >/dev/null 2>&1; then echo "  - Claude Code already present."
  else echo "  - Installing Claude Code ..."; curl -fsSL https://claude.ai/install.sh | bash; fi
}
install_npm () {  # $1 = package, $2 = friendly name, $3 = command
  if command -v "$3" >/dev/null 2>&1; then echo "  - $2 already present."
  else echo "  - Installing $2 ..."; npm install -g "$1" >/dev/null 2>&1; fi
}

case "$SEL" in *1*) install_claude;                                  [ -z "$PRIMARY" ] && PRIMARY="claude";; esac
case "$SEL" in *2*) install_npm "@google/gemini-cli" "Gemini CLI" "gemini"; [ -z "$PRIMARY" ] && PRIMARY="gemini";; esac
case "$SEL" in *3*) install_npm "@openai/codex"      "Codex CLI"  "codex";  [ -z "$PRIMARY" ] && PRIMARY="codex";; esac
[ -z "$PRIMARY" ] && PRIMARY="claude"
echo ""

# --- 3. The bootstrap launch pad --------------------------------------------
#     A hidden, self-cleaning setup folder. It is a SIBLING of repos/commons,
#     never a parent - so its pointer file can never shadow the engineer's
#     real work sessions, and it never collides with the Commons OS clone.
WORKROOT="$HOME/repos/.commons-setup"
mkdir -p "$WORKROOT"

# --- 4. Fetch the onboarding procedure --------------------------------------
ONBOARDING_URL="https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/ONBOARDING.md"
echo "  Fetching the latest setup procedure..."
if curl -fsSL "$ONBOARDING_URL" -o "$WORKROOT/ONBOARDING.md"; then echo "  - procedure ready."
else echo "  - could not fetch the procedure; the agent will guide you anyway."; fi

# --- 4b. Drop a tool-specific pointer so the agent finds the procedure ------
#     The agent auto-loads this on startup, so it knows its mission even if
#     the launch prompt is interrupted by first-run sign-in.
POINTER="CLAUDE.md"
[ "$PRIMARY" = "gemini" ] && POINTER="GEMINI.md"
[ "$PRIMARY" = "codex" ]  && POINTER="AGENTS.md"
cat > "$WORKROOT/$POINTER" <<'EOF'
# Commons Engineering - setup session

Read ONBOARDING.md in this folder and execute it step by step to set up
my Commons Engineering working environment. Clone Commons OS into ../commons
(the workspace root, i.e. repos/commons - a sibling of this setup folder).

I am new and may be non-technical. Guide me warmly, do the technical work
yourself, and explain anything I ask. This is a one-time setup; when it
hands over to BOOT.md, the founding conversation begins. You may remove
this pointer file and ONBOARDING.md once setup is complete.
EOF
echo ""

# --- 5. Hand over to the chosen agent ---------------------------------------
echo "  Tools are ready. Opening your agent now."
echo ""
echo "  On first launch your agent may open a browser to sign you in -"
echo "  that's normal. If you don't have an account yet, just choose"
echo "  \"Sign up\" on that screen. Once you're signed in, the agent takes"
echo "  over: it sets up your GitHub, clones your workspace, and connects"
echo "  you to the shared knowledge. From here on you just talk to it."
echo ""
cd "$WORKROOT" || exit 1
export PATH="$HOME/.local/bin:$PATH"

if ! command -v "$PRIMARY" >/dev/null 2>&1; then
  echo "  [i] Your agent was just installed. Please CLOSE this window,"
  echo "      open it again (double-click this file once more), and I'll"
  echo "      launch straight into it."
  echo ""
  read -r -p "  Press Return to close." _
  exit 0
fi

PROMPT="Read ONBOARDING.md in this folder and execute it step by step to set up my Commons Engineering working environment. I am new and non-technical - guide me warmly and do the technical work yourself."

if [ "$PRIMARY" = "claude" ]; then
  claude "$PROMPT"
else
  echo "  Starting $PRIMARY. When it opens, tell it:"
  echo "    \"$PROMPT\""
  echo ""
  "$PRIMARY"
fi
