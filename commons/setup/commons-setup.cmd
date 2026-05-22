@echo off
REM ============================================================
REM  Commons Engineering - set up my working environment
REM
REM  A newcomer double-clicks this one file. It installs the
REM  toolchain, lets them pick an AI coding agent, then hands
REM  over to that agent, which does the conversational part
REM  (identity, GitHub, cloning, Commons MCP) by talking to them.
REM
REM  No terminal knowledge required. One double-click.
REM ============================================================

setlocal enableextensions enabledelayedexpansion
title Commons Engineering - setting up your working environment

REM  Disable QuickEdit so a stray click never freezes the window (best-effort).
powershell -NoProfile -Command "try{$s='[DllImport(\"kernel32.dll\")]public static extern IntPtr GetStdHandle(int n);[DllImport(\"kernel32.dll\")]public static extern bool GetConsoleMode(IntPtr h,out uint m);[DllImport(\"kernel32.dll\")]public static extern bool SetConsoleMode(IntPtr h,uint m);';$t=Add-Type -MemberDefinition $s -Name Q -Namespace CE -PassThru;$h=$t::GetStdHandle(-10);$m=0;[void]$t::GetConsoleMode($h,[ref]$m);[void]$t::SetConsoleMode($h,($m -band -bnot 0x40) -bor 0x80)}catch{}" >nul 2>&1

REM  All raw installer detail goes to this log; the screen stays calm.
set "LOG=%TEMP%\commons-setup-log.txt"
> "%LOG%" echo Commons Engineering setup log

cls
echo.
echo   Welcome to Commons Engineering
echo   ------------------------------
echo.
echo   I'm setting up everything you need to work.
echo   This takes a few minutes - you can just let it run.
echo.

REM --- 0. winget present? (ships with Windows 10 1709+ / Windows 11) ----------
where winget >nul 2>&1
if errorlevel 1 (
  echo   Preparing the package installer ^(one-time, this can take a few minutes^)...
  call :install_winget
  call :refresh_path
  echo       ^> package installer ready
  echo.
)
call :resolve_winget
if not defined WINGET (
  echo   [!] Couldn't set up winget automatically. Please open the Microsoft
  echo       Store, install "App Installer", then run this file again.
  echo.
  pause
  exit /b 1
)

REM --- 1. The toolchain - deterministic, silent, no judgement needed ----------
echo   Installing the tools the work runs on.
echo   Each one downloads and installs - some take a minute. Please wait.
echo.
call :install "Git.Git"                       "Git (versions your work)"
call :install "GitHub.cli"                     "GitHub CLI (reaches repositories)"
call :install "OpenJS.NodeJS.LTS"              "Node.js (runs the web instances and agents)"
call :install "Python.Python.3.12"             "Python (document and data tooling)"
call :install "Microsoft.VisualStudioCode"     "VS Code (the editor)"
echo.

REM --- Refresh PATH so freshly installed tools (node/npm) work this session ---
call :refresh_path

REM --- 2. Choose your AI coding agent(s) --------------------------------------
echo   Which AI coding agent would you like? You can pick more than one.
echo.
echo     [1] Claude Code   (recommended)
echo     [2] Gemini CLI    (Google)
echo     [3] Codex CLI     (OpenAI)
echo.
set "SEL="
set /p "SEL=  Enter numbers separated by spaces, or just press Enter for Claude Code: "
if not defined SEL set "SEL=1"
echo.
echo   Setting up your agent...
echo.

set "PRIMARY="
echo !SEL! | findstr /c:"1" >nul && ( call :install_claude    & if not defined PRIMARY set "PRIMARY=claude" )
echo !SEL! | findstr /c:"2" >nul && ( call :install_npm "@google/gemini-cli" "Gemini CLI" "gemini" & if not defined PRIMARY set "PRIMARY=gemini" )
echo !SEL! | findstr /c:"3" >nul && ( call :install_npm "@openai/codex"      "Codex CLI"  "codex"  & if not defined PRIMARY set "PRIMARY=codex" )
if not defined PRIMARY set "PRIMARY=claude"
call :refresh_path
echo.

REM --- 3. The bootstrap launch pad --------------------------------------------
REM     A visible, self-cleaning setup folder (the GUI app's folder picker must
REM     be able to see it). It is a SIBLING of repos\commons - never a parent -
REM     so it can't shadow real work sessions or collide with the Commons OS clone.
set "WORKROOT=%USERPROFILE%\repos\commons-setup"
if not exist "%WORKROOT%" mkdir "%WORKROOT%"

REM --- 4. Fetch the onboarding procedure --------------------------------------
set "ONBOARDING_URL=https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/ONBOARDING.md"
echo   Fetching the latest setup procedure...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "try { Invoke-WebRequest -Uri '%ONBOARDING_URL%' -OutFile '%WORKROOT%\ONBOARDING.md' -UseBasicParsing; Write-Host '   - procedure ready.' } catch { Write-Host '   - could not fetch the procedure; the agent will guide you anyway.' }"

REM --- 4b. Drop a tool-specific pointer so the agent finds the procedure ------
REM     The agent auto-loads this on startup, so it knows its mission even if
REM     the launch prompt is interrupted by first-run sign-in.
REM     Written line-by-line (not a parenthesized block) so punctuation is safe.
set "POINTER=CLAUDE.md"
if /i "%PRIMARY%"=="gemini" set "POINTER=GEMINI.md"
if /i "%PRIMARY%"=="codex"  set "POINTER=AGENTS.md"
set "PFILE=%WORKROOT%\%POINTER%"
> "%PFILE%"  echo # Commons Engineering - setup session
>>"%PFILE%"  echo.
>>"%PFILE%"  echo Read ONBOARDING.md in this folder and execute it step by step to set up
>>"%PFILE%"  echo my Commons Engineering working environment. Clone Commons OS into ..\commons,
>>"%PFILE%"  echo the workspace root i.e. repos\commons, a sibling of this setup folder.
>>"%PFILE%"  echo.
>>"%PFILE%"  echo I am new and may be non-technical. Guide me warmly, do the technical work
>>"%PFILE%"  echo yourself, and explain anything I ask. This is a one-time setup; when it
>>"%PFILE%"  echo hands over to BOOT.md, the founding conversation begins. You may remove
>>"%PFILE%"  echo this pointer file and ONBOARDING.md once setup is complete.
echo.

REM --- 5. Hand over to the chosen agent ---------------------------------------
echo.
echo   ===========================================================
echo     Everything is installed. You're moments from working.
echo   ===========================================================
echo.
cd /d "%WORKROOT%"

if /i not "%PRIMARY%"=="claude" goto :handoff_terminal

REM --- Claude: hand off to the comfortable GUI (the Desktop app) --------------
echo   Let's finish in the Claude app - three small steps:
echo.
echo     1. The "Claude" app is opening. Sign in once - it's a button,
echo        no codes to copy. No account yet? Choose "Sign up".
echo     2. In the app, choose: Open folder.
echo     3. Open this folder ^(a window just opened showing it for you^):
echo            %WORKROOT%
echo.
echo   Then just tell it:  set up my Commons environment from ONBOARDING.md
echo   ...and I'll take it from there - sign you in to GitHub, clone your
echo   workspace, and connect you to the shared knowledge.
echo.
echo   Prefer something else? Both are installed too:
echo     - VS Code : the Claude Code extension is ready
echo     - Terminal: open the folder above and run  claude
echo.
REM Open the workspace folder so the user can find it in the app's picker.
start "" "%WORKROOT%"
REM Launch the Claude Desktop app by its real AppUserModelID, resolved at runtime
REM from the installed app list. This works whether the app is an MSIX/Store
REM package or an Electron build - both register a launchable AUMID.
set "CLAUDEAUMID="
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "(Get-StartApps ^| Where-Object { $_.Name -eq 'Claude' } ^| Select-Object -First 1).AppID"`) do set "CLAUDEAUMID=%%i"
if defined CLAUDEAUMID explorer.exe "shell:AppsFolder\!CLAUDEAUMID!"
echo   ^(If the Claude app didn't open by itself, start it from the Start menu.^)
echo.
pause
endlocal
exit /b 0

:handoff_terminal
REM --- Gemini / Codex: launch the chosen CLI in the terminal -----------------
where %PRIMARY% >nul 2>&1
if errorlevel 1 (
  echo   [i] Your agent was just installed. Please CLOSE this window,
  echo       open it again ^(double-click this file once more^), and I'll
  echo       launch straight into it.
  echo.
  pause
  exit /b 0
)
set "PROMPT=Read ONBOARDING.md in this folder and execute it step by step to set up my Commons Engineering working environment. I am new and non-technical - guide me warmly and do the technical work yourself."
echo   Starting %PRIMARY%. When it opens, tell it:
echo     "%PROMPT%"
echo.
%PRIMARY%
endlocal
exit /b 0

REM ============================================================
:install
REM  Always attempt the install. winget is idempotent (skips if already there),
REM  so we do NOT pre-check with `winget list` - its exit code is unreliable:
REM  a failing msstore source can make it falsely report "already present",
REM  which would skip every install. --source winget avoids msstore entirely.
REM  Delayed expansion (!PKGNAME!) keeps parentheses in names parse-safe.
set "PKGID=%~1"
set "PKGNAME=%~2"
echo     Installing !PKGNAME! ...
"%WINGET%" install --id "!PKGID!" -e --source winget --silent --accept-package-agreements --accept-source-agreements --disable-interactivity >> "%LOG%" 2>&1
echo       ^> !PKGNAME! ready
exit /b 0

:install_claude
REM  Claude is installed as a full trio so the engineer can choose their surface:
REM    - Desktop app (GUI)   : the comfortable default, with thread management
REM    - CLI                 : the engine; cleanest for MCP setup and automation
REM    - VS Code extension   : in-IDE chat for codebase work
REM  All three share one login via ~/.claude, so the user signs in only once.
call :install "Anthropic.Claude"     "Claude Desktop app - GUI"
call :install "Anthropic.ClaudeCode" "Claude Code CLI - engine"
where code >nul 2>&1 && (
  echo     Installing the Claude Code extension for VS Code ...
  call code --install-extension anthropic.claude-code --force >> "%LOG%" 2>&1
  echo       ^> VS Code extension ready
)
exit /b 0

:install_npm
REM  %~1 = npm package, %~2 = friendly name, %~3 = binary/command name
where %~3 >nul 2>&1
if not errorlevel 1 (
  echo   - %~2 already present.
  exit /b 0
)
where npm >nul 2>&1
if errorlevel 1 (
  echo   [i] %~2 needs Node.js, which was just installed. It will install
  echo       when you reopen this window.
  exit /b 0
)
echo   - Installing %~2 ...
call npm install -g %~1
exit /b 0

:resolve_winget
REM  Resolve a usable winget, even if the App Execution Alias isn't on PATH yet.
set "WINGET="
where winget >nul 2>&1 && set "WINGET=winget"
if defined WINGET exit /b 0
if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\winget.exe" set "WINGET=%LOCALAPPDATA%\Microsoft\WindowsApps\winget.exe"
if defined WINGET exit /b 0
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "$a=Get-AppxPackage Microsoft.DesktopAppInstaller ^| Select-Object -First 1; if($a){Join-Path $a.InstallLocation 'winget.exe'}"`) do if exist "%%i" set "WINGET=%%i"
exit /b 0

:refresh_path
REM  Augment PATH with freshly installed tool locations WITHOUT replacing it.
REM  The live PATH (System32 etc.) must stay first - registry values can carry
REM  unexpanded %vars%, so we never overwrite, only append.
for /f "skip=2 tokens=2,*" %%A in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH 2^>nul') do set "SysPath=%%B"
for /f "skip=2 tokens=2,*" %%A in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "UsrPath=%%B"
set "PATH=%PATH%;%SysPath%;%UsrPath%;%LOCALAPPDATA%\Microsoft\WindowsApps;%USERPROFILE%\.local\bin;%APPDATA%\npm"
exit /b 0

:install_winget
REM  Bootstrap winget on stripped/older images via Microsoft's official module,
REM  which resolves the whole dependency chain (VCLibs, UI.Xaml, WindowsAppRuntime)
REM  itself - far more robust than chasing individual appx dependencies.
REM  Written to a temp .ps1 to avoid fragile caret/quote escaping.
set "PS=%TEMP%\ce_winget_bootstrap.ps1"
> "%PS%"  echo $ErrorActionPreference='Stop'; $ProgressPreference='Continue'
>>"%PS%"  echo try {
>>"%PS%"  echo   [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12
>>"%PS%"  echo   Write-Host '   - preparing PowerShell package source'
>>"%PS%"  echo   Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force -ForceBootstrap ^| Out-Null
>>"%PS%"  echo   Set-PSRepository -Name PSGallery -InstallationPolicy Trusted -ErrorAction SilentlyContinue
>>"%PS%"  echo   Write-Host '   - installing winget client module'
>>"%PS%"  echo   if (-not (Get-Module -ListAvailable Microsoft.WinGet.Client)) { Install-Module Microsoft.WinGet.Client -Force -Scope CurrentUser -Confirm:$false }
>>"%PS%"  echo   Import-Module Microsoft.WinGet.Client
>>"%PS%"  echo   Write-Host '   - bootstrapping winget (this downloads its dependencies)'
>>"%PS%"  echo   Repair-WinGetPackageManager -Latest -Force
>>"%PS%"  echo   Write-Host '   - winget installed.'
>>"%PS%"  echo } catch { Write-Host ('   [!] winget bootstrap failed: ' + $_.Exception.Message) }
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS%" >> "%LOG%" 2>&1
del "%PS%" >nul 2>&1
exit /b 0
