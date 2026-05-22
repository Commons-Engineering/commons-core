#!/bin/bash
# ============================================================
#  Commons Engineering - set up my working environment  (macOS)
#
#  A newcomer double-clicks this one file. It installs the
#  toolchain, installs the Claude trio (Desktop GUI + CLI +
#  VS Code extension), then hands off to the Desktop GUI app.
#
#  No terminal knowledge required. One double-click.
#  (If macOS shows a prompt: right-click -> Open, once.)
# ============================================================

set -u

# All raw installer detail goes to this log; the screen stays calm.
LOG="${TMPDIR:-/tmp}/commons-setup-log.txt"
echo "Commons Engineering setup log" > "$LOG"

clear 2>/dev/null || true
echo ""
echo "  ============================================================"
echo "                 Welcome to Commons Engineering"
echo "  ============================================================"
echo ""
echo "    I'm setting up everything you need to work."
echo "    This takes a few minutes - you can just let it run."
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
  if brew list "$1" >/dev/null 2>&1; then echo "      > $2 ready"
  else echo "    Installing $2 ..."; brew install "$1" >>"$LOG" 2>&1; echo "      > $2 ready"; fi
}
install_cask () {     # $1 = cask, $2 = friendly name
  if brew list --cask "$1" >/dev/null 2>&1; then echo "      > $2 ready"
  else echo "    Installing $2 ..."; brew install --cask "$1" >>"$LOG" 2>&1; echo "      > $2 ready"; fi
}

# --- 1. The toolchain - deterministic, no judgement needed ------------------
echo "  Installing the tools the work runs on."
echo "  Each one downloads and installs - some take a minute. Please wait."
echo ""
install_formula "git"         "Git - versions your work"
install_formula "gh"          "GitHub CLI - reaches repositories"
install_formula "node"        "Node.js - runs the web instances and agents"
install_formula "python@3.12" "Python - document and data tooling"
install_cask    "visual-studio-code" "VS Code - the editor"
echo ""

# --- helper: locate the VS Code 'code' CLI (PATH or app bundle) -------------
resolve_code () {
  if command -v code >/dev/null 2>&1; then echo "code"; return; fi
  local b="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
  [ -x "$b" ] && echo "$b"
}

# --- 2. Choose your AI coding agent(s) --------------------------------------
echo "  Which AI coding agent would you like? You can pick more than one."
echo ""
echo "    [1] Claude Code   (recommended)"
echo "    [2] Gemini CLI    (Google)"
echo "    [3] Codex CLI     (OpenAI)"
echo ""
read -r -p "  Enter numbers separated by spaces, or just press Return for Claude Code: " SEL </dev/tty
[ -z "${SEL:-}" ] && SEL="1"
echo ""

export PATH="$HOME/.local/bin:$PATH"
PRIMARY=""

install_claude () {
  # Claude as a trio: Desktop GUI app, CLI engine, VS Code extension.
  # All three share one login via ~/.claude, so the user signs in only once.
  install_cask "claude" "Claude Desktop app - GUI"
  if command -v claude >/dev/null 2>&1; then echo "      > Claude Code CLI ready"
  else echo "    Installing Claude Code CLI ..."; curl -fsSL https://claude.ai/install.sh | bash >>"$LOG" 2>&1; echo "      > Claude Code CLI ready"; fi
  CODE_BIN="$(resolve_code)"
  if [ -n "$CODE_BIN" ]; then
    echo "    Installing the Claude Code extension for VS Code ..."
    "$CODE_BIN" --install-extension anthropic.claude-code --force >>"$LOG" 2>&1
    echo "      > VS Code extension ready"
  fi
}
install_npm () {  # $1 = package, $2 = friendly name, $3 = command
  if command -v "$3" >/dev/null 2>&1; then echo "      > $2 ready"
  else echo "    Installing $2 ..."; npm install -g "$1" >>"$LOG" 2>&1; echo "      > $2 ready"; fi
}

echo "  Setting up your agent..."
echo ""
case "$SEL" in *1*) install_claude;                                          [ -z "$PRIMARY" ] && PRIMARY="claude";; esac
case "$SEL" in *2*) install_npm "@google/gemini-cli" "Gemini CLI" "gemini";  [ -z "$PRIMARY" ] && PRIMARY="gemini";; esac
case "$SEL" in *3*) install_npm "@openai/codex"      "Codex CLI"  "codex";   [ -z "$PRIMARY" ] && PRIMARY="codex";; esac
[ -z "$PRIMARY" ] && PRIMARY="claude"
echo ""

# --- 3. The bootstrap launch pad --------------------------------------------
#     A visible, self-cleaning setup folder (the GUI app's folder picker must
#     be able to see it). It is a SIBLING of repos/commons - never a parent -
#     so it can't shadow real work sessions or collide with the Commons OS clone.
WORKROOT="$HOME/repos/commons-setup"
mkdir -p "$WORKROOT"

# --- 4. Fetch the onboarding procedure --------------------------------------
ONBOARDING_URL="https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/ONBOARDING.md"
echo "  Fetching the latest setup procedure..."
if curl -fsSL "$ONBOARDING_URL" -o "$WORKROOT/ONBOARDING.md"; then echo "  - procedure ready."
else echo "  - could not fetch the procedure; the agent will guide you anyway."; fi

# --- 4b. Drop a tool-specific pointer so the agent finds the procedure ------
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
echo ""
echo "  ==========================================================="
echo "    Everything is installed. You're moments from working."
echo "  ==========================================================="
echo ""
cd "$WORKROOT" || exit 1

if [ "$PRIMARY" = "claude" ]; then
  # Hand off to the comfortable GUI (the Desktop app).
  echo "  Let's finish in the Claude app - three small steps:"
  echo ""
  echo "    1. The \"Claude\" app is opening. Sign in once - it's a button,"
  echo "       no codes to copy. No account yet? Choose \"Sign up\"."
  echo "    2. In the app, choose: Open folder."
  echo "    3. Open this folder (a Finder window just opened showing it):"
  echo "           $WORKROOT"
  echo ""
  echo "  Then just tell it:  set up my Commons environment from ONBOARDING.md"
  echo "  ...and I'll take it from there - sign you in to GitHub, clone your"
  echo "  workspace, and connect you to the shared knowledge."
  echo ""
  echo "  Prefer something else? Both are installed too:"
  echo "    - VS Code : the Claude Code extension is ready"
  echo "    - Terminal: open the folder above and run  claude"
  echo ""
  open "$WORKROOT" 2>/dev/null || true        # Finder window at the folder
  open -a "Claude" 2>/dev/null || true        # launch the Desktop GUI app
  echo "  (If the Claude app didn't open by itself, open it from Launchpad or Applications.)"
  echo ""
  read -r -p "  Press Return to close this window." _ </dev/tty
  exit 0
fi

# --- Gemini / Codex: launch the chosen CLI in the terminal -----------------
export PATH="$HOME/.local/bin:$PATH"
if ! command -v "$PRIMARY" >/dev/null 2>&1; then
  echo "  [i] Your agent was just installed. Please CLOSE this window,"
  echo "      open it again (double-click this file once more), and I'll"
  echo "      launch straight into it."
  echo ""
  read -r -p "  Press Return to close." _ </dev/tty
  exit 0
fi
PROMPT="Read ONBOARDING.md in this folder and execute it step by step to set up my Commons Engineering working environment. I am new and non-technical - guide me warmly and do the technical work yourself."
echo "  Starting $PRIMARY. When it opens, tell it:"
echo "    \"$PROMPT\""
echo ""
"$PRIMARY"
