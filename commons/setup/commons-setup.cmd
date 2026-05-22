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

echo.
echo   Welcome to Commons Engineering.
echo   I'm setting up everything you need to work. This takes a few minutes.
echo.

REM --- 0. winget present? (ships with Windows 10 1709+ / Windows 11) ----------
where winget >nul 2>&1
if errorlevel 1 (
  echo   Windows package installer ^(winget^) not found - installing it for you...
  call :install_winget
  call :refresh_path
)
where winget >nul 2>&1
if errorlevel 1 (
  echo   [!] Couldn't set up winget automatically. Please open the Microsoft
  echo       Store, install "App Installer", then run this file again.
  echo.
  pause
  exit /b 1
)

REM --- 1. The toolchain - deterministic, silent, no judgement needed ----------
echo   Installing the tools the work runs on...
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

set "PRIMARY="
echo !SEL! | findstr /c:"1" >nul && ( call :install_claude    & if not defined PRIMARY set "PRIMARY=claude" )
echo !SEL! | findstr /c:"2" >nul && ( call :install_npm "@google/gemini-cli" "Gemini CLI" "gemini" & if not defined PRIMARY set "PRIMARY=gemini" )
echo !SEL! | findstr /c:"3" >nul && ( call :install_npm "@openai/codex"      "Codex CLI"  "codex"  & if not defined PRIMARY set "PRIMARY=codex" )
if not defined PRIMARY set "PRIMARY=claude"
call :refresh_path
echo.

REM --- 3. The bootstrap launch pad --------------------------------------------
REM     A hidden, self-cleaning setup folder. It is a SIBLING of repos\commons,
REM     never a parent - so its pointer file can never shadow the engineer's
REM     real work sessions, and it never collides with the Commons OS clone.
set "WORKROOT=%USERPROFILE%\repos\.commons-setup"
if not exist "%WORKROOT%" mkdir "%WORKROOT%"

REM --- 4. Fetch the onboarding procedure --------------------------------------
set "ONBOARDING_URL=https://raw.githubusercontent.com/Commons-Engineering/commons-os/main/commons/setup/ONBOARDING.md"
echo   Fetching the latest setup procedure...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "try { Invoke-WebRequest -Uri '%ONBOARDING_URL%' -OutFile '%WORKROOT%\ONBOARDING.md' -UseBasicParsing; Write-Host '   - procedure ready.' } catch { Write-Host '   - could not fetch the procedure; the agent will guide you anyway.' }"

REM --- 4b. Drop a tool-specific pointer so the agent finds the procedure ------
REM     The agent auto-loads this on startup, so it knows its mission even if
REM     the launch prompt is interrupted by first-run sign-in.
set "POINTER=CLAUDE.md"
if /i "%PRIMARY%"=="gemini" set "POINTER=GEMINI.md"
if /i "%PRIMARY%"=="codex"  set "POINTER=AGENTS.md"
(
  echo # Commons Engineering - setup session
  echo.
  echo Read ONBOARDING.md in this folder and execute it step by step to set up
  echo my Commons Engineering working environment. Clone Commons OS into ..\commons
  echo (the workspace root, i.e. repos\commons - a sibling of this setup folder).
  echo.
  echo I am new and may be non-technical. Guide me warmly, do the technical work
  echo yourself, and explain anything I ask. This is a one-time setup; when it
  echo hands over to BOOT.md, the founding conversation begins. You may remove
  echo this pointer file and ONBOARDING.md once setup is complete.
) > "%WORKROOT%\%POINTER%"
echo.

REM --- 5. Hand over to the chosen agent ---------------------------------------
echo   Tools are ready. Opening your agent now.
echo.
echo   On first launch your agent may open a browser to sign you in -
echo   that's normal. If you don't have an account yet, just choose
echo   "Sign up" on that screen. Once you're signed in, the agent takes
echo   over: it sets up your GitHub, clones your workspace, and connects
echo   you to the shared knowledge. From here on you just talk to it.
echo.
cd /d "%WORKROOT%"

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

if /i "%PRIMARY%"=="claude" (
  claude "%PROMPT%"
) else (
  echo   Starting %PRIMARY%. When it opens, tell it:
  echo     "%PROMPT%"
  echo.
  %PRIMARY%
)

endlocal
exit /b 0

REM ============================================================
:install
winget list --id %~1 -e >nul 2>&1
if errorlevel 1 (
  echo   - Installing %~2 ...
  winget install --id %~1 -e --silent --accept-package-agreements --accept-source-agreements >nul 2>&1
) else (
  echo   - %~2 already present.
)
exit /b 0

:install_claude
where claude >nul 2>&1
if errorlevel 1 (
  echo   - Installing Claude Code ...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://claude.ai/install.ps1 | iex"
) else (
  echo   - Claude Code already present.
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
call npm install -g %~1 >nul 2>&1
exit /b 0

:refresh_path
REM  Re-read PATH from the registry so this session sees freshly installed tools.
for /f "skip=2 tokens=2,*" %%A in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH 2^>nul') do set "SysPath=%%B"
for /f "skip=2 tokens=2,*" %%A in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "UsrPath=%%B"
set "PATH=%SysPath%;%UsrPath%;%USERPROFILE%\.local\bin;%LOCALAPPDATA%\Microsoft\WindowsApps"
exit /b 0

:install_winget
REM  Bootstrap winget on stripped/older images via Microsoft's official module,
REM  which resolves the whole dependency chain (VCLibs, UI.Xaml, WindowsAppRuntime)
REM  itself - far more robust than chasing individual appx dependencies.
REM  Written to a temp .ps1 to avoid fragile caret/quote escaping.
set "PS=%TEMP%\ce_winget_bootstrap.ps1"
> "%PS%"  echo $ErrorActionPreference='Stop'; $ProgressPreference='SilentlyContinue'
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
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS%"
del "%PS%" >nul 2>&1
exit /b 0
