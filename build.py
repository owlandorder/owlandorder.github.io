#!/usr/bin/env python3
"""Stránka odkazov Owl & Order: links.json -> index.html (statické HTML, bez JavaScriptu a sledovania).

Použitie (z koreňa repozitára):  python3 build.py
Mení sa len links.json; index.html sa vždy vyrobí znova týmto skriptom.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
ALLOWED = ("https://owlandorder.etsy.com", "https://owlandorder.github.io")


def esc(s):
    return html.escape(str(s), quote=True)


def check(d):
    errs = []
    for k in ("brand", "tagline", "intro", "description", "links", "footer"):
        if not d.get(k):
            errs.append(f"chýba pole {k}")
    for i, l in enumerate(d.get("links", []), 1):
        if not l.get("label") or not l.get("url"):
            errs.append(f"odkaz {i}: chýba label alebo url")
        elif not l["url"].startswith(ALLOWED):
            # Etsy Share & Save platí len pre odkazy v tvare owlandorder.etsy.com.
            # Nová doména (Payhip, Kit) sa pridá do ALLOWED vedome, nie omylom.
            errs.append(f"odkaz {i}: neschválená doména {l['url']}")
    if errs:
        sys.exit("links.json:\n- " + "\n- ".join(errs))


def render(d):
    items = []
    for l in d["links"]:
        badge = f'<span class="badge">{esc(l["badge"])}</span>' if l.get("badge") else ""
        note = f'<span class="note">{esc(l["note"])}</span>' if l.get("note") else ""
        items.append(
            f'<li><a class="btn" href="{esc(l["url"])}" rel="noopener">'
            f'<span class="label">{esc(l["label"])}{badge}</span>{note}</a></li>'
        )
    footer = "".join(f"<p>{esc(p)}</p>" for p in d["footer"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d["brand"])} | {esc(d["tagline"])}</title>
<meta name="description" content="{esc(d["description"])}">
<meta property="og:title" content="{esc(d["brand"])}">
<meta property="og:description" content="{esc(d["description"])}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://owlandorder.github.io/">
<link rel="canonical" href="https://owlandorder.github.io/">
<style>
:root {{
  --bg: #EDEBE6; --ink: #1F2A44; --muted: #4B5563; --card: #FFFFFF;
  --line: #D6D3CC; --accent: #0F766E; --gold: #B7791F;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  line-height: 1.5; -webkit-font-smoothing: antialiased;
}}
main {{ max-width: 34rem; margin: 0 auto; padding: 3.5rem 1.25rem 2.5rem; }}
header {{ text-align: center; margin-bottom: 2rem; }}
h1 {{ font-size: 1.9rem; letter-spacing: -0.02em; margin: 0 0 .35rem; }}
.tagline {{ font-weight: 600; color: var(--accent); margin: 0 0 .75rem; }}
.intro {{ color: var(--muted); margin: 0; }}
ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: .85rem; }}
.btn {{
  display: block; text-decoration: none; color: var(--ink); background: var(--card);
  border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.15rem;
  transition: border-color .15s, transform .15s;
}}
.btn:hover, .btn:focus-visible {{ border-color: var(--ink); transform: translateY(-1px); }}
.btn:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
.label {{ display: flex; align-items: center; gap: .5rem; font-weight: 650; font-size: 1.05rem; }}
.badge {{
  font-size: .72rem; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
  color: var(--gold); border: 1px solid currentColor; border-radius: 999px; padding: .05rem .5rem;
}}
.note {{ display: block; color: var(--muted); font-size: .92rem; margin-top: .15rem; }}
footer {{ margin-top: 2.5rem; text-align: center; color: var(--muted); font-size: .8rem; }}
footer p {{ margin: .25rem 0; }}
@media (prefers-reduced-motion: reduce) {{ .btn {{ transition: none; }} .btn:hover {{ transform: none; }} }}
</style>
</head>
<body>
<main>
<header>
<h1>{esc(d["brand"])}</h1>
<p class="tagline">{esc(d["tagline"])}</p>
<p class="intro">{esc(d["intro"])}</p>
</header>
<nav aria-label="Links">
<ul>
{chr(10).join(items)}
</ul>
</nav>
<footer>
{footer}
<p>&copy; 2026 {esc(d["brand"])}</p>
</footer>
</main>
</body>
</html>
"""


def main():
    d = json.loads((ROOT / "links.json").read_text(encoding="utf-8"))
    check(d)
    (ROOT / "index.html").write_text(render(d), encoding="utf-8")
    print(f"index.html vyrobený ({d.get('version', '?')}, {len(d['links'])} odkazy)")


if __name__ == "__main__":
    main()
