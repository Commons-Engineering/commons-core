#!/usr/bin/env python3
"""
markdown_to_pdf — the CANONICAL Commons OS renderer.  Markdown -> styled HTML ->
headless Chromium/Edge -> PDF.  Pure Python (only the `markdown` package) + a
Chromium-family browser.  No pandoc / LaTeX / weasyprint / npm.

A first-class OS capability every fork inherits. Renders ANY deliverable markdown
(blueprint, analyses, management summary, game poles). Do NOT re-derive a PDF toolchain
per user/instance — declare a bundle in `.commons/deliverables.yml` and let
`generate_deliverables.py` + the deliverables workflow render it (see AGENT.md).
Cross-platform: browser discovery checks $CHROME_BIN, then PATH (google-chrome/chromium),
then the standard Windows Edge/Chrome paths (Linux CI and Windows both work).

HARD-WON GOTCHAS (keep them):
  1. SIMPLE headless invocation: --headless=new --disable-gpu --no-pdf-header-footer
     --print-to-pdf=OUT URL.  Do NOT add --virtual-time-budget /
     --run-all-compositor-stages-before-draw: they truncate to one page.
  2. Print to a SIMPLE temp path (no spaces/unicode), then move to the final name.
  3. The browser writes the PDF ASYNchronously; poll for the file before success.
  4. Title page must NOT use flexbox height; use top padding + page-break-after.

Usage:
    python blueprint_to_pdf.py INPUT.md OUTPUT.pdf [--title T] [--kicker K] [--subtitle S] [--foot F]
"""
import sys, re, os, subprocess, tempfile, shutil, time, argparse
from pathlib import Path
try:
    import markdown
except ImportError:
    sys.exit("Missing dependency: pip install markdown")

# Windows fallbacks (Holger's/Udo's machines); CI uses PATH discovery below.
BROWSERS = [
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
]

def find_browser():
    env = os.environ.get("CHROME_BIN") or os.environ.get("BROWSER")
    if env and os.path.exists(env):
        return env
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        p = shutil.which(name)
        if p:
            return p
    for p in BROWSERS:
        if os.path.exists(p):
            return p
    raise SystemExit("No Chromium/Chrome/Edge found (set $CHROME_BIN to the browser binary).")

def strip_pipeline(md_text):
    if md_text.startswith('---'):
        end = md_text.find('\n---', 3)
        if end != -1:
            md_text = md_text[end+4:]
    marker = '<!-- pipeline-annotation:end -->'
    idx = md_text.find(marker)
    if idx != -1:
        md_text = md_text[idx+len(marker):]
    h = re.search(r'(?m)^#{1,2} ', md_text)
    if h:
        md_text = md_text[h.start():]
    parts = re.split(r'(?m)^(?=#{1,2} )', md_text)
    kept = [p for p in parts if not re.search(
        r'(Pipeline|bei Transfer entfernen|nur Pipeline)', p.split('\n', 1)[0], re.I)]
    return ''.join(kept).strip()

def first_h1(md_text):
    m = re.search(r'(?m)^# (.+)$', md_text)
    return re.sub(r'[*`_]', '', m.group(1)).strip() if m else 'Blueprint'

CSS = """
@page { size: A4; margin: 1.9cm 1.7cm 1.7cm 1.7cm; }
body { font-family:'Segoe UI','Calibri','Helvetica Neue',sans-serif; font-size:10pt; line-height:1.46; color:#202124; }
.titlepage { padding-top: 6.5cm; page-break-after: always; }
.titlepage .kicker { font-size:10pt; letter-spacing:.18em; text-transform:uppercase; color:#8a6d3b; margin-bottom:1.1cm; }
.titlepage h1 { font-size:27pt; line-height:1.18; font-weight:600; color:#1a2b4a; margin:0; page-break-before: avoid; }
.titlepage .rule { width:3.2cm; height:3px; background:#b08d57; margin:1cm 0; }
.titlepage .sub { font-size:12.5pt; color:#5f6368; margin-top:.7cm; line-height:1.4; max-width:15cm; }
.titlepage .foot { font-size:9.5pt; color:#9aa0a6; margin-top:3.2cm; }
nav.toc { page-break-after: always; }
nav.toc > h2 { font-size:16pt; color:#1a2b4a; border-bottom:2px solid #e6e1d8; padding-bottom:.2cm; }
nav.toc ul { list-style:none; padding-left:0; margin:.2cm 0; }
nav.toc li { margin:.12cm 0; }
nav.toc ul ul { padding-left:.8cm; }
nav.toc ul ul li { font-size:9.2pt; color:#5f6368; }
nav.toc a { text-decoration:none; color:#202124; }
nav.toc ul ul a { color:#5f6368; }
h1 { font-size:18pt; color:#1a2b4a; font-weight:600; margin:0 0 .3cm 0; padding-bottom:.15cm; border-bottom:2px solid #b08d57; page-break-before: always; page-break-after: avoid; }
h2 { font-size:13.5pt; color:#1a2b4a; font-weight:600; margin:.7cm 0 .25cm 0; page-break-after: avoid; }
h3 { font-size:11pt; color:#34507a; font-weight:600; margin:.55cm 0 .2cm 0; page-break-after: avoid; }
h4 { font-size:10pt; color:#5f6368; font-weight:600; margin:.45cm 0 .15cm 0; }
p { margin:.28cm 0; }
strong { color:#1a1a1a; }
blockquote { border-left:3px solid #b08d57; background:#faf7f1; margin:.4cm 0; padding:.25cm .6cm; color:#444; font-size:9.6pt; }
code { font-family:'Consolas','Courier New',monospace; font-size:8.8pt; background:#f1f3f4; padding:.04cm .18cm; color:#7a3e00; }
table { width:100%; border-collapse:collapse; margin:.35cm 0; font-size:8.7pt; page-break-inside:avoid; }
th, td { border:1px solid #dfe1e5; padding:.13cm .28cm; text-align:left; vertical-align:top; }
th { background:#1a2b4a; color:#fff; font-weight:600; }
th strong, th a { color:#fff; }
tr:nth-child(even) td { background:#f7f8fa; }
ul, ol { margin:.25cm 0; padding-left:.7cm; }
li { margin:.1cm 0; }
hr { border:none; border-top:1px solid #e6e1d8; margin:.6cm 0; }
"""
EMOJI = [('\U0001F534','#c0392b'),('\U0001F7E1','#d68910'),('\U0001F7E2','#1e8449'),('\U0001F535','#2471a3')]

def build(md_path, out_pdf, title=None, kicker='', subtitle='', foot='cloudsters · Commons Engineering'):
    raw = Path(md_path).read_text(encoding='utf-8')
    title = title or first_h1(raw)
    body = strip_pipeline(raw)
    for emo, col in EMOJI:
        body = body.replace(emo, '<span style="color:%s;font-weight:bold">●</span>' % col)
    md = markdown.Markdown(extensions=['tables','toc','sane_lists','attr_list','md_in_html'],
                           extension_configs={'toc': {'toc_depth': '1-2'}})
    body_html = md.convert(body)
    inner = md.toc.strip()
    if inner.startswith('<div class="toc">'): inner = inner[len('<div class="toc">'):]
    if inner.endswith('</div>'): inner = inner[:-len('</div>')]
    toc_html = '<nav class="toc"><h2>Inhalt</h2>' + inner + '</nav>'
    html = ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>%s</style></head><body>'
            '<section class="titlepage"><div class="kicker">%s</div><h1>%s</h1>'
            '<div class="rule"></div><div class="sub">%s</div><div class="foot">%s</div></section>'
            '%s\n%s</body></html>') % (CSS, kicker, title, subtitle, foot, toc_html, body_html)
    tmp = tempfile.mkdtemp(prefix='bp_')
    html_path = os.path.join(tmp, 'doc.html'); pdf_tmp = os.path.join(tmp, 'doc.pdf')
    Path(html_path).write_text(html, encoding='utf-8')
    subprocess.run([find_browser(), '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--no-sandbox', '--print-to-pdf=' + pdf_tmp, Path(html_path).as_uri()],
                   capture_output=True, text=True, timeout=180)
    for _ in range(50):  # the browser writes the PDF asynchronously after the process returns
        if os.path.exists(pdf_tmp) and os.path.getsize(pdf_tmp) > 0:
            time.sleep(0.5); break
        time.sleep(0.3)
    if not (os.path.exists(pdf_tmp) and os.path.getsize(pdf_tmp) > 0):
        raise SystemExit("PDF render failed (no output) for " + md_path)
    os.makedirs(os.path.dirname(out_pdf) or '.', exist_ok=True)
    shutil.move(pdf_tmp, out_pdf)
    print('OK -> %s (%d KB)' % (out_pdf, os.path.getsize(out_pdf)//1024))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Render a Commons OS blueprint markdown to a sendable PDF.')
    ap.add_argument('input'); ap.add_argument('output')
    ap.add_argument('--title'); ap.add_argument('--kicker', default='')
    ap.add_argument('--subtitle', default=''); ap.add_argument('--foot', default='cloudsters · Commons Engineering')
    a = ap.parse_args()
    build(a.input, a.output, a.title, a.kicker, a.subtitle, a.foot)
