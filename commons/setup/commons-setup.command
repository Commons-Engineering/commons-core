#!/bin/bash
# ============================================================
#  Commons Engineering - set up my working environment  (macOS)
#
#  Recommended invocation (process substitution keeps stdin connected
#  to your terminal, so Homebrew and sudo can prompt if they need to):
#
#    bash <(curl -fsSL https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/commons-setup.command)
#
#  The older form  curl ... | bash  makes Homebrew (and other sub-installers)
#  exit silently because stdin is the pipe, not your terminal.
#
#  Detailed setup log is written to $HOME/commons-setup.log.
#  No "set -u" is used: macOS shell init quirks across versions can trigger
#  it through no fault of the user. Each step reports its own status.
# ============================================================

LOG="$HOME/commons-setup.log"
: > "$LOG"

# say()   - print to user AND log
# logged() - run a command silently, capturing its output to the log only
say()    { echo "$@"; echo "$@" >> "$LOG"; }
logline(){ echo "$@" >> "$LOG"; }

# --- Banner -----------------------------------------------------------------
say ""
say "  Welcome to Commons Engineering"
say "  ------------------------------"
say ""
say "  I'm setting up everything you need to work."
say "  This takes a few minutes - you can just let it run."
say "  Detailed setup log: $LOG"
say ""

# --- Diagnostic context (to log only) ---------------------------------------
{
  echo "=== environment ==="
  echo "macOS:       $(sw_vers -productVersion 2>&1)"
  echo "arch:        $(uname -m)"
  echo "bash:        ${BASH_VERSION:-unknown}"
  echo "user:        $(whoami)"
  echo "shell:       ${SHELL:-unknown}"
  echo "PATH:        $PATH"
  echo "stdin is tty: $(test -t 0 && echo yes || echo no)"
  echo "/dev/tty:     $(test -e /dev/tty && echo present || echo MISSING)"
  echo ""
} >> "$LOG"

# --- 0. Homebrew present? ---------------------------------------------------
if command -v brew >/dev/null 2>&1; then
  say "  - Homebrew already present."
else
  say "  Installing Homebrew (the package installer)..."
  say "  Homebrew will ask you two things - this is normal:"
  say "    1. \"Press RETURN/ENTER to continue\"  -> just hit Return."
  say "    2. \"Password:\"  -> your Mac login password. The characters won't"
  say "       show as you type - that's normal, just type and Return."
  say ""
  # No NONINTERACTIVE here: Homebrew reads its own prompts from /dev/tty, which
  # works under  bash <(curl ...) . Setting NONINTERACTIVE=1 would force
  # Homebrew to require passwordless sudo and abort on a normal Mac.
  if /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 2>&1 | tee -a "$LOG"; then
    say "  - Homebrew installed."
  else
    say "  [!] Homebrew install reported an error (details in $LOG)."
  fi
fi

# Make brew + its tools available in this session (Apple Silicon + Intel).
[ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
[ -x /usr/local/bin/brew ]   && eval "$(/usr/local/bin/brew shellenv)"

# Verify brew is now reachable. If not, stop with a helpful message.
if ! command -v brew >/dev/null 2>&1; then
  say ""
  say "  [!] Homebrew is not available - cannot continue."
  say ""
  say "  The most common cause: this script was started with"
  say "      curl ... | bash"
  say "  which prevents Homebrew's installer from asking for your password."
  say ""
  say "  Please re-run using this form (note the parentheses):"
  say ""
  say "    bash <(curl -fsSL https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/commons-setup.command)"
  say ""
  say "  Full log saved at: $LOG"
  exit 1
fi

# --- 1. The toolchain -------------------------------------------------------
say ""
say "  Installing the tools the work runs on."
say "  Some are large downloads and can take several minutes each - this is"
say "  completely normal. Please leave this window open and let it work."
say ""

install_formula() {  # $1 = formula, $2 = friendly name
  local formula="$1" name="$2"
  if brew list "$formula" >/dev/null 2>&1; then
    say "  - $name already present."
  else
    say "  - Installing $name ..."
    if brew install "$formula" >>"$LOG" 2>&1; then
      say "    > $name ready."
    else
      say "    [!] $name install reported an error - see $LOG."
    fi
  fi
}
install_cask() {     # $1 = cask, $2 = friendly name, $3 = (optional) app bundle name in /Applications
  local cask="$1" name="$2" app="${3:-}"
  if brew list --cask "$cask" >/dev/null 2>&1; then
    say "  - $name already present."
  elif [ -n "$app" ] && [ -d "/Applications/$app" ]; then
    # App exists in /Applications but brew doesn't track it (typical for apps
    # the user downloaded manually). --adopt brings it under brew management
    # without a re-download when the version on disk matches the cask's.
    say "  - $name found in /Applications - adopting into brew management ..."
    if brew install --cask "$cask" --adopt >>"$LOG" 2>&1; then
      say "    > $name adopted."
    else
      say "    [i] adopt didn't apply (version mismatch?); installing normally ..."
      if brew install --cask "$cask" >>"$LOG" 2>&1; then
        say "    > $name ready."
      else
        say "    [!] $name install reported an error - see $LOG."
      fi
    fi
  else
    say "  - Installing $name ..."
    if brew install --cask "$cask" >>"$LOG" 2>&1; then
      say "    > $name ready."
    else
      say "    [!] $name install reported an error - see $LOG."
    fi
  fi
}

install_formula git           "Git"
install_formula gh            "GitHub CLI"
install_formula node          "Node.js"
install_formula python@3.12   "Python 3.12"
install_cask    visual-studio-code "VS Code"             "Visual Studio Code.app"
say ""

# Resolve the VS Code 'code' CLI (PATH or app bundle fallback).
resolve_code() {
  if command -v code >/dev/null 2>&1; then echo "code"; return; fi
  local b="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
  [ -x "$b" ] && echo "$b"
}

# --- 2. Agent selection -----------------------------------------------------
say "  Setting up your agent. The Claude app is a larger download -"
say "  please wait, this part can take a few minutes."
say ""

SEL=""
if [ -n "${CE_TEST:-}" ]; then
  SEL="1"
  say "  [test mode] selecting Claude Code, non-interactive"
elif [ -e /dev/tty ]; then
  echo "  Which AI coding agent would you like? You can pick more than one."
  echo ""
  echo "    [1] Claude Code   (recommended)"
  echo "    [2] Gemini CLI    (Google)"
  echo "    [3] Codex CLI     (OpenAI)"
  echo ""
  read -r -p "  Enter numbers separated by spaces, or just press Return for Claude Code: " SEL </dev/tty || SEL=""
else
  say "  (no terminal available - defaulting to Claude Code)"
  SEL="1"
fi
[ -z "${SEL:-}" ] && SEL="1"
logline "agent selection: $SEL"
say ""

export PATH="$HOME/.local/bin:$PATH"
PRIMARY=""

install_claude() {
  install_cask claude "Claude Desktop app" "Claude.app"
  if command -v claude >/dev/null 2>&1; then
    say "  - Claude Code CLI already present."
  else
    say "  - Installing Claude Code CLI ..."
    if curl -fsSL https://claude.ai/install.sh | bash >>"$LOG" 2>&1; then
      say "    > Claude Code CLI ready."
    else
      say "    [!] Claude Code CLI install reported an error - see $LOG."
    fi
  fi
  local CODE_BIN
  CODE_BIN="$(resolve_code)"
  if [ -n "$CODE_BIN" ]; then
    say "  - Adding the Claude Code extension to VS Code ..."
    if "$CODE_BIN" --install-extension anthropic.claude-code --force >>"$LOG" 2>&1; then
      say "    > extension ready."
    else
      say "    [!] VS Code extension install reported an error - see $LOG."
    fi
  else
    say "    [i] VS Code 'code' CLI not on PATH yet; extension will install on next run."
  fi
}

install_npm() {  # $1 = package, $2 = friendly name, $3 = command
  local pkg="$1" name="$2" cmd="$3"
  if command -v "$cmd" >/dev/null 2>&1; then
    say "  - $name already present."
  else
    say "  - Installing $name ..."
    if npm install -g "$pkg" >>"$LOG" 2>&1; then
      say "    > $name ready."
    else
      say "    [!] $name install reported an error - see $LOG."
    fi
  fi
}

case "$SEL" in *1*) install_claude;                                          [ -z "$PRIMARY" ] && PRIMARY="claude";; esac
case "$SEL" in *2*) install_npm "@google/gemini-cli" "Gemini CLI" "gemini";  [ -z "$PRIMARY" ] && PRIMARY="gemini";; esac
case "$SEL" in *3*) install_npm "@openai/codex"      "Codex CLI"  "codex";   [ -z "$PRIMARY" ] && PRIMARY="codex";; esac
[ -z "$PRIMARY" ] && PRIMARY="claude"
say ""

# --- 3. Bootstrap launch pad ------------------------------------------------
WORKROOT="$HOME/repos/commons-setup"
mkdir -p "$WORKROOT"

# --- 4. Fetch the onboarding procedure --------------------------------------
ONBOARDING_URL="https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/ONBOARDING.md"
say "  Fetching the latest setup procedure..."
if curl -fsSL "$ONBOARDING_URL" -o "$WORKROOT/ONBOARDING.md" 2>>"$LOG"; then
  say "  - procedure ready."
else
  say "  - could not fetch the procedure; the agent will guide you anyway."
fi

# --- 4b. Drop a tool-specific pointer ---------------------------------------
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
say ""

# --- 5. Hand off ------------------------------------------------------------
say ""
say "  ==========================================================="
say "    Everything is installed. You're moments from working."
say "  ==========================================================="
say ""
cd "$WORKROOT" || exit 1

if [ "$PRIMARY" = "claude" ]; then
  say "  Let's finish in the Claude app - three small steps:"
  say ""
  say "    1. The \"Claude\" app is opening. Sign in once - it's a button,"
  say "       no codes to copy. No account yet? Choose \"Sign up\"."
  say "    2. In the app, choose: Open folder."
  say "    3. Open this folder (a Finder window just opened showing it):"
  say "           $WORKROOT"
  say ""
  say "  Then just tell it:  set up my Commons environment from ONBOARDING.md"
  say ""
  say "  Prefer something else? Both are installed too:"
  say "    - VS Code : the Claude Code extension is ready"
  say "    - Terminal: open the folder above and run  claude"
  say ""
  if [ -n "${CE_TEST:-}" ]; then
    say "  [test mode] skipping GUI launch and pause - install verification complete."
    exit 0
  fi
  open "$WORKROOT" 2>/dev/null || true        # Finder window at the folder
  open -a "Claude" 2>/dev/null || true        # launch the Desktop GUI app
  say "  (If the Claude app didn't open by itself, open it from Launchpad or Applications.)"
  say ""
  if [ -e /dev/tty ]; then
    read -r -p "  Press Return to close this window." _ </dev/tty || true
  fi
  exit 0
fi

# --- Gemini / Codex: launch the chosen CLI in the terminal -----------------
export PATH="$HOME/.local/bin:$PATH"
if ! command -v "$PRIMARY" >/dev/null 2>&1; then
  say "  [i] Your agent was just installed. Please re-run the command,"
  say "      and I'll launch into it."
  say ""
  if [ -e /dev/tty ]; then
    read -r -p "  Press Return to close." _ </dev/tty || true
  fi
  exit 0
fi
PROMPT="Read ONBOARDING.md in this folder and execute it step by step to set up my Commons Engineering working environment. I am new and non-technical - guide me warmly and do the technical work yourself."
say "  Starting $PRIMARY. When it opens, tell it:"
say "    \"$PROMPT\""
say ""
"$PRIMARY"
