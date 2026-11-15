#!/usr/bin/env python3
"""bootstrap.py — set up a new Commons CORE from this template in one command.

Run it from the root of the CORE:

    python bootstrap.py --you <github-login>                  the founding; your agent then asks what you want to
                                                              model and proposes a domain model
    python bootstrap.py --domain life --you <github-login>    the quick path, when you know the domain model already
    python bootstrap.py --domain life                         later, on a founded CORE: adds the domain model only

It does, in this order, and stops at the first step that fails, saying what went wrong:
  1. finds the library beside the CORE (../library), or clones federation.library there;
  2. reads from the library's index.yml the newest released Commons model, patterns extract and, with --domain, the
     chosen domain model, each with its folder and record digest;
  3. installs the Commons model with the install.py in the release's own copy, then the patterns extract and, with
     --domain, the domain model with the installed copy's install.py, and names the domain model in the graph's
     register; install.py checks every copy against its digest, and this script checks nothing itself;
  4. names you, by your GitHub login (--you), under SEED in .commons/access.yml as account:<login>, unless you are
     named there already, and records the founding, by github:<login>:
     one event in lifecycle/events/ and the stage Seed in lifecycle/stage.yml, unless the stage is recorded already;
  5. writes the connector entry of the CORE's own MCP, over stdio, into .mcp.json; federation.mcp is added there
     once it is in operation (access.yml names it already);
  6. generates AGENT.md with make_agent.py, so that it names what .mcp.json connects, then runs check_core.py.

A step already done is skipped, so the script can run again after a fix, or with --domain on a CORE founded without
one: then only the domain model is installed and registered, and AGENT.md is generated again to name it.
It needs Python 3.11 or newer, Git, and the package pyyaml (python -m pip install pyyaml jsonschema).
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time

LIBRARY_URL = "https://github.com/cloudsters/federation.library.git"
FEDERATION_MCP = "https://mcp.cloudsters.net/federation"   # every CORE names federation.mcp in access.yml (mcp R24);
                                                          # .mcp.json gets no entry until it is in operation
COMMONS = ("commons", None)          # the Commons model's id in the library's index, and its variant
PATTERNS = ("patterns", None)        # the patterns extract
DOMAINS = {                          # --domain → (id, variant)
    "life": ("life", None),
    "business/startup": ("business", "startup"),
    "business/corporate": ("business", "corporate"),
    "health": ("health", None),
    "urban": ("urban", None),
}

FIRST_QUESTION = {                   # a first question with content words, so that the domain's records answer it
    "life": "\"How do I keep track of what comes in and what goes out of my household?\"",
    "business/startup": "\"How do we keep our regular customers coming back?\"",
    "business/corporate": "\"How do we make sure our suppliers treat their workers fairly?\"",
    "health": "\"How do we plan beds for the winter?\"",
    "urban": "\"How can residents have a real say in what the city decides?\"",
    "*":"a sentence that names the work, the people or the thing it is about.",
}

try:
    import yaml
except ImportError:
    sys.exit("This script needs the Python package pyyaml. Install it with:\n    python -m pip install pyyaml jsonschema")


class Stop(Exception):
    """A step failed; the message says what went wrong and what to do, in plain words."""


def say(text):
    print(f"\n>> {text}", flush=True)


FINDINGS_SHOWN = 20                  # should and gap lines shown after the check; the check itself lists them all
ALIVE_EVERY = 30                     # seconds between the signs of life while a tool runs


def alive(done):
    """Print the elapsed time every ALIVE_EVERY seconds until `done` is set, so that a long step never looks hung."""
    start = time.monotonic()
    while not done.wait(ALIVE_EVERY):
        print(f"  ... still working, {int(time.monotonic() - start)} s", flush=True)


def run(cmd, what, findings=False, notice=None):
    """Run one tool; show its summary and its failures (with findings, its should and gap lines too), or else its
    last lines, and stop if it failed. A notice is printed before it starts, and a sign of life while it runs.
    The tools write UTF-8, and so does this script."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    if notice:
        print(f"  {notice}", flush=True)
    done = threading.Event()
    threading.Thread(target=alive, args=(done,), daemon=True).start()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    finally:
        done.set()
    out = (p.stdout + p.stderr).strip()
    lines = out.splitlines()
    picked = [l for l in lines if l.startswith("# ") or l.startswith("fail:")]
    shown = picked if picked else lines[-15:]
    if shown:
        print("  " + "\n  ".join(shown[:40]), flush=True)
    if findings:
        rest = [l for l in lines if l.startswith("should:") or l.startswith("gap:")]
        if rest:
            print("  " + "\n  ".join(rest[:FINDINGS_SHOWN]), flush=True)
        if len(rest) > FINDINGS_SHOWN:
            print(f"  ... and {len(rest) - FINDINGS_SHOWN} more; the check lists them all when run again.", flush=True)
    if p.returncode != 0:
        raise Stop(f"{what} did not succeed (exit code {p.returncode}). Its own report is above. "
                   "Fix what it names and run this script again; steps already done are skipped.")
    return out


def version_key(v):
    """Orders versions such as 0.3.0, 0.10.1 or v2026.11.3: each part compared as (is it a number, its value)."""
    return [(1, int(x), "") if x.isdigit() else (0, 0, x) for x in re.split(r"[.\-]", str(v).lstrip("v"))]


def find_release(lib, index, rid, variant):
    """The newest released entry of the index for an id (and variant): its folder and its record digest."""
    hits = []
    for r in index.get("releases") or []:
        if r.get("id") != rid or r.get("state") != "released":
            continue
        folder = os.path.dirname(r["record"])
        has_variant = r.get("variant") or (folder.split("/")[-2] if folder.count("/") >= 2 else None)
        if variant and has_variant != variant:
            continue
        if not variant and r.get("variant"):
            continue
        hits.append(r)
    if not hits:
        name = f"{rid}/{variant}" if variant else rid
        held = sorted({f"{r['id']}/{r['variant']}" if r.get("variant") else
                       (f"{r['id']}/{os.path.dirname(r['record']).split('/')[-2]}" if r["record"].count("/") >= 3 else r["id"])
                       for r in index.get("releases") or []
                       if r.get("state") == "released" and r.get("kind") == "model" and r.get("id") not in ("commons", "commons-essentials")})
        raise Stop(f"The library's index.yml has no released '{name}'. It releases these domain models: "
                   f"{', '.join(held) or 'none yet'}. Choose one of them with --domain, or update the library (git -C {lib} pull).")
    r = max(hits, key=lambda x: version_key(x["version"]))
    return os.path.join(lib, os.path.dirname(r["record"])), r["digest"], r["version"]


def installed(core, lib_id, rid, variant):
    """Where an installed model lies, if it does (models/commons/<library>/<model>[/<variant>]/)."""
    for base in (os.path.join(core, "models", "commons", lib_id), os.path.join(core, "extensions", lib_id)):
        p = os.path.join(base, rid, variant) if variant else os.path.join(base, rid)
        if os.path.isdir(p):
            return p
    return None


def register_domain(core, folder, sid):
    """Name the installed domain model in the graph's register, graph/sources.yml, so that its records answer (graph R3)."""
    path = os.path.join(core, "graph", "sources.yml")
    ref = os.path.relpath(folder, core).replace(os.sep, "/").rstrip("/") + "/"
    if os.path.isfile(path):
        text = open(path, encoding="utf-8").read()
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        text = ("sources:\n"
                "  - {id: runtime,  kind: runtime,  ref: models/runtime/,  class: member}\n"
                "  - {id: knowledge, kind: knowledge, ref: knowledge/, class: member}\n")
    entries = (yaml.safe_load(text) or {}).get("sources") or []
    if any(isinstance(e, dict) and str(e.get("ref", "")).rstrip("/") + "/" == ref for e in entries):
        print(f"  The graph's register names {ref} already.")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += f"  - {{id: {sid}, kind: emulation, ref: {ref}, class: member}}\n"
    yaml.safe_load(text)
    open(path, "w", encoding="utf-8", newline="\n").write(text)
    print(f"  The graph's register names {ref}, so that its records answer.")


def installed_version(folder):
    """The version an installed copy states in its release.yml, or None."""
    rec = os.path.join(folder, "release.yml") if folder else None
    if not rec or not os.path.isfile(rec):
        return None
    return str((yaml.safe_load(open(rec, encoding="utf-8")) or {}).get("version") or "") or None


def patterns_installed(core, lib_id):
    p = os.path.join(core, "patterns", "commons", lib_id)
    return p if os.path.isdir(p) and os.listdir(p) else None


def name_founder(core, you):
    """Add `you` under SEED in .commons/access.yml, keeping the file as it is otherwise."""
    path = os.path.join(core, ".commons", "access.yml")
    if not os.path.isfile(path):
        raise Stop("This folder has no .commons/access.yml. Run the script from the root of a CORE made from the template.")
    text = open(path, encoding="utf-8").read()
    data = yaml.safe_load(text) or {}
    users = data.get("users") or []
    if any(u.get("account") == you for u in users if isinstance(u, dict)):
        print(f"  {you} is already named in access.yml.")
        return data
    entry = f"  - account: {you}\n    shell: SEED\n"
    if re.search(r"^users:\s*\[\]\s*$", text, re.M):
        text = re.sub(r"^users:\s*\[\]\s*$", "users:\n" + entry.rstrip("\n"), text, count=1, flags=re.M)
    elif re.search(r"^users:\s*$", text, re.M):
        text = re.sub(r"^users:\s*$", "users:\n" + entry.rstrip("\n"), text, count=1, flags=re.M)
    else:
        text = text.rstrip("\n") + "\nusers:\n" + entry
    if not text.endswith("\n"):
        text += "\n"
    data = yaml.safe_load(text)
    open(path, "w", encoding="utf-8", newline="").write(text)
    print(f"  {you} is named under SEED in .commons/access.yml.")
    return data


def python_command():
    """The name under which this Python is called: python on Windows, else python where it exists, otherwise python3."""
    if os.name == "nt":
        return "python"
    return "python" if shutil.which("python") else "python3"


def record_founding(core, you):
    """The founding event and the stage Seed (core part 5), written once: skipped where lifecycle/stage.yml exists."""
    stage = os.path.join(core, "lifecycle", "stage.yml")
    if os.path.isfile(stage):
        print("  The stage is recorded already (lifecycle/stage.yml).")
        return
    settings = os.path.join(core, ".commons", "commons.yml")
    meta = yaml.safe_load(open(settings, encoding="utf-8")) if os.path.isfile(settings) else None
    name = (meta or {}).get("name") or os.path.basename(core)
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    eid = f"{today}-founding"
    events = os.path.join(core, "lifecycle", "events")
    os.makedirs(events, exist_ok=True)
    title = f"{name} is founded from the commons-core template".replace("'", "''")
    event = [f"id: {eid}", f"date: '{today}'", f"recorded: '{now}'", "kind: founding", "subject: commons",
             f"title: '{title}'", "by:", f"- {you}", "source: the commons-core template, set up by bootstrap.py"]
    open(os.path.join(events, f"{eid}.yml"), "w", encoding="utf-8", newline="\n").write("\n".join(event) + "\n")
    open(stage, "w", encoding="utf-8", newline="\n").write("\n".join(["stage: Seed", f"since: '{today}'", f"event: {eid}"]) + "\n")
    print(f"  The founding is recorded: lifecycle/events/{eid}.yml, and the stage Seed.")


def write_mcp_json(core, tools, you, federation):
    """The connector entry of the CORE's own MCP over stdio; other entries are kept. federation.mcp is not in operation
    yet, so it gets no entry, and the one an earlier run of this script wrote is removed, so that no client shows a
    server that cannot be reached."""
    path = os.path.join(core, ".mcp.json")
    cfg = {}
    if os.path.isfile(path):
        try:
            cfg = json.load(open(path, encoding="utf-8"))
        except ValueError:
            raise Stop(".mcp.json exists but is not valid JSON. Correct or remove it, then run this script again.")
    servers = cfg.setdefault("mcpServers", {})
    serve = os.path.relpath(os.path.join(tools, "serve_mcp.py"), core).replace(os.sep, "/")
    servers["commons"] = {"command": python_command(), "args": [serve, ".", "--stdio", "--as", you, "--state", "../.mcp-state"]}
    earlier = servers.get("federation")
    if isinstance(earlier, dict) and earlier.get("url") in (federation, FEDERATION_MCP):
        del servers["federation"]
    open(path, "w", encoding="utf-8", newline="\n").write(json.dumps(cfg, indent=2) + "\n")
    print("  .mcp.json names the CORE's own MCP over stdio.")


def main():
    ap = argparse.ArgumentParser(description="Set up a new Commons CORE from this template in one command.")
    ap.add_argument("--domain", choices=sorted(DOMAINS),
                    help="the domain model closest to your commons; leave it out, and your agent proposes one with you")
    ap.add_argument("--you", help="your GitHub login, e.g. ada (a prefix account: or github: is dropped); "
                                  "needed for the founding, not when a domain model is added later")
    ap.add_argument("--library", default=os.path.join("..", "library"), help="the library's folder (default ../library)")
    a = ap.parse_args()
    core = os.getcwd()
    founded = os.path.isfile(os.path.join(core, "lifecycle", "stage.yml"))
    if not a.you and not (founded and a.domain):
        raise Stop("Give your GitHub login with --you, for example: python bootstrap.py --you ada. "
                   "Only a domain model added later to a founded CORE needs no --you.")
    you = person = None
    if a.you:
        login = a.you.split(":", 1)[1] if a.you.startswith(("account:", "github:")) else a.you
        if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?", login or ""):
            raise Stop(f"--you {a.you!r} is not a GitHub login. Give your login as GitHub shows it, for example --you ada.")
        you = f"account:{login}"      # access.yml and .mcp.json name the account as the sign-in reports it (mcp part 5)
        person = f"github:{login}"    # a record names a person as github: or person: (core R14)
    lib = a.library

    say("1. The library")
    if not os.path.isfile(os.path.join(lib, "index.yml")):
        print(f"  Cloning {LIBRARY_URL} into {lib} ...")
        run(["git", "clone", "--depth", "1", LIBRARY_URL, lib], "Cloning the library")
    else:
        print(f"  Found at {lib}.")
    index = yaml.safe_load(open(os.path.join(lib, "index.yml"), encoding="utf-8")) or {}
    lib_meta = yaml.safe_load(open(os.path.join(lib, "library.yml"), encoding="utf-8")) if os.path.isfile(os.path.join(lib, "library.yml")) else {}
    lib_id = (lib_meta or {}).get("id") or "commons-engineering"

    say("2. The releases")
    c_from, c_digest, c_ver = find_release(lib, index, *COMMONS)
    p_from, p_digest, p_ver = find_release(lib, index, *PATTERNS)
    if a.domain:
        d_id, d_var = DOMAINS[a.domain]
        d_from, d_digest, d_ver = find_release(lib, index, d_id, d_var)
        print(f"  Commons model {c_ver}, patterns {p_ver}, {a.domain} {d_ver}.")
    else:
        print(f"  Commons model {c_ver}, patterns {p_ver}; no domain model yet, your agent proposes one with you.")

    say("3. Installing")
    bootstrap_install = os.path.join(c_from, "specs", "tools", "install.py")
    if not os.path.isfile(bootstrap_install):
        raise Stop(f"The release {c_from} carries no specs/tools/install.py, so it cannot install itself. "
                   "Report this to the library's maintainers; nothing was changed.")
    tools_home = installed(core, lib_id, *COMMONS) or installed(core, lib_id, "commons-essentials", None)
    have = installed_version(tools_home)
    if tools_home and have is not None and version_key(have) < version_key(c_ver):
        print(f"  The Commons model {have} is installed; taking up {c_ver} in its place.")
        run([sys.executable, bootstrap_install, core, "--from", c_from, "--expect", c_digest, "--take-up"],
            "Taking up the newer Commons model")
        tools_home = installed(core, lib_id, *COMMONS) or installed(core, lib_id, "commons-essentials", None)
    elif tools_home:
        print(f"  The Commons model is installed already ({os.path.relpath(tools_home, core)}).")
    else:
        run([sys.executable, bootstrap_install, core, "--from", c_from, "--expect", c_digest], "Installing the Commons model")
        tools_home = installed(core, lib_id, *COMMONS)
        if not tools_home:
            raise Stop("install.py reported success, but the Commons model is not in models/commons/. Check its report above.")
    tools = os.path.join(tools_home, "specs", "tools")
    install = os.path.join(tools, "install.py")
    if patterns_installed(core, lib_id):
        print("  The patterns extract is installed already.")
    else:
        run([sys.executable, install, core, "--from", p_from, "--expect", p_digest], "Installing the patterns extract",
            notice="Installing the patterns extract, the whole pattern language (this takes a while)...")
    if a.domain:
        if installed(core, lib_id, d_id, d_var):
            print(f"  The domain model {a.domain} is installed already.")
        else:
            run([sys.executable, install, core, "--from", d_from, "--expect", d_digest], f"Installing the domain model {a.domain}")
        d_home = installed(core, lib_id, d_id, d_var)
        if not d_home:
            raise Stop(f"install.py reported success, but the domain model {a.domain} is not in models/commons/. Check its report above.")
        register_domain(core, d_home, f"{d_id}-{d_var}" if d_var else d_id)

    say("4. You, under SEED, and the founding")
    access = None
    if you:
        access = name_founder(core, you)
        record_founding(core, person)
    else:
        print("  The CORE is founded already; nothing to change here.")

    say("5. The connector for your agent")       # before AGENT.md, which names what .mcp.json connects
    if you:
        write_mcp_json(core, tools, you, (access or {}).get("federation"))
    else:
        print("  .mcp.json is written already; nothing to change here.")

    say("6. Generating AGENT.md and checking the CORE")
    run([sys.executable, os.path.join(tools, "make_agent.py"), core], "Generating AGENT.md")
    run([sys.executable, os.path.join(tools, "check_core.py"), core], "The check of the CORE", findings=True,
        notice="Checking the CORE (takes 1-3 minutes)...")

    if a.domain:
        say("Done. Commit what changed (git add -A, git commit, git push), then open the CORE with your agent "
            "and bring it a concrete need of your own, for example: " + FIRST_QUESTION.get(a.domain, FIRST_QUESTION["*"]))
    else:
        say("Done. Commit what changed (git add -A, git commit, git push). Open the CORE with your agent; "
            "it will ask what you want to model and propose a domain model.")


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    try:
        main()
    except Stop as e:
        print(f"\nSTOPPED: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)
