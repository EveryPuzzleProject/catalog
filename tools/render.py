#!/usr/bin/env python3
"""Render the census's web page, site/index.html, from publications/*.md,
syndicates/*.md and universe.md. Served at https://everypuzzleproject.org/census/
by .github/workflows/pages.yml.

    python tools/render.py

Uses build.py's front-matter parsing and checks, so an entry that fails
`build.py --check` fails here too. Metadata only: names, kinds, places, years,
counts. Needs PyYAML.
"""
import datetime as dt
import html
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/EveryPuzzleProject/census"
BLOB, TREE = f"{REPO}/blob/main/", f"{REPO}/tree/main/"
NEW_ISSUE = f"{REPO}/issues/new?template="
XD = '<a href="https://github.com/century-arcade/xdformat">xd</a>'
THIS_YEAR = dt.date.today().year
FIRST_DECADE = 1910
WEB_FROM = 1990  # a website's corpus files dated before the web are reprints of older puzzles
KIND_LABELS = {"newspaper": "Newspapers", "magazine": "Magazines", "book": "Books",
               "website": "Websites", "other": "Other", "syndicate": "Syndicates"}
STATUS_COLORS = {"lead": "var(--warm)", "researched": "color-mix(in srgb, var(--accent) 60%, var(--muted))",
                 "harvesting": "var(--accent)", "blitzing": "color-mix(in srgb, var(--accent) 55%, var(--good))", "corpus": "var(--good)", "archived": "var(--good)"}
STATUS_LABELS = {"corpus": "in the corpus"}

# The research, in the order README.md gives it. research-notes-*.md files not
# named here are added at the end under their own titles.
RESEARCH = [
    ("universe.md", "The known universe", "how many crosswords have been published, and what each number rests on"),
    ("first-runs.md", "The first runs, 1913–1924", "every paper known to have printed a crossword, from the New York World's first"),
    ("syndicates/", "Syndicates", "who distributed the puzzles: names, features, editors and copyright lines over time"),
    ("universe/", "The universe's data", "every US newspaper by year (Library of Congress) and every crossword feature in Editor & Publisher, 1924–2000"),
    ("research-notes-college.md", "College and school papers", "a first survey of student papers and their archives"),
    ("bylines/", "Bylines and people", "who signed the puzzles, publication by publication"),
    ("research-notes-weekly-syndication.md", "Weekly papers and ready-print syndication", "who supplied the small weeklies"),
    ("research-notes-directories.md", "Publication directories as a source", "can we list every US periodical by year?"),
    ("research-notes-boston-globe-doubles.md", "The Boston Globe's double-puzzle Sundays", ""),
    ("research-notes-leads-2026-10-18.md", "Leads and access notes", ""),
]


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def num(v) -> int | None:
    """The year in a front-matter value: 1924, 1924-11-01, "1920-10-31 (at the latest)"."""
    y = build.year(v)
    return int(y) if y[:4].isdigit() else None


def ranges(text) -> set[int]:
    """Years in "1917, 1980–1988, 1998–2026"."""
    out = set()
    for a, b in re.findall(r"(\d{4})(?:\s*[–-]\s*(\d{4}))?", str(text or "")):
        out.update(range(int(a), int(b or a) + 1))
    return out


def years(e: dict) -> set[int]:
    """Years the publication is known to have run crosswords: its stated run
    (first to last, "ongoing" meaning this year), widened by sightings, plus
    the years its puzzles in the corpus come from."""
    cw = e.get("crosswords") or {}
    seen = [y for y in (num(s.get("date")) for s in e.get("sightings") or []) if y]
    first, last = num(cw.get("first")), num(cw.get("last"))
    if str(cw.get("last") or "").startswith("ongoing"):
        last = THIS_YEAR
    ends = [y for y in [first, last, *seen] if y]
    out = set(range(min(ends), max(ends) + 1)) if ends else set()
    c = e.get("corpus") or {}
    held = ranges(c.get("years"))
    if e["kind"] == "website":
        held = {y for y in held if y >= WEB_FROM}
    return out | held


def syndicate_years(e: dict) -> set[int]:
    """A syndicate's crossword features, from each one's start to its end (or
    just its start year when the end isn't given)."""
    out = set()
    for f in e.get("features") or []:
        if isinstance(f, dict) and num(f.get("from")):
            a = num(f.get("from"))
            out.update(range(a, (num(f.get("to")) or a) + 1))
    return out


def decades(ys: set[int]) -> list[int]:
    return sorted({y // 10 * 10 for y in ys if FIRST_DECADE <= y <= THIS_YEAR})


def load_syndicates() -> list[dict]:
    out = []
    for p in sorted((ROOT / "syndicates").glob("*.md")):
        m = re.match(r"---\n(.*?)\n---\n", p.read_text(encoding="utf-8").replace("\r\n", "\n"), re.S)
        if m and p.name != "README.md":
            e = yaml.safe_load(m[1]) or {}
            e["_path"] = p
            out.append(e)
    return out


def universe() -> dict:
    """The denominator, from universe.md's prose: about N dailies and M weeklies since 1913."""
    text = (ROOT / "universe.md").read_text(encoding="utf-8")
    d = re.search(r"about ([\d,]+) dailies existed since 1913", text)
    w = re.search(r"about ([\d,]+) weeklies", text)
    if not (d and w):
        sys.exit("universe.md: can't find the daily and weekly counts (\"about N dailies existed since 1913\", \"about M weeklies\")")
    return {"dailies": d[1], "weeklies": w[1]}


def title_of(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return re.sub(r"\s*\(.*?\)\s*$", "", line[2:]).split(":")[0].strip()
    return path.stem


def main() -> int:
    entries, errors = [], []
    for p in sorted((ROOT / "publications").glob("*.md")):
        e, errs = build.load(p)
        errors += errs
        if not errs:
            e["_path"] = p
            entries.append(e)
    if errors:
        print("\n".join(errors))
        return 1
    order = list(build.STATUSES)
    entries.sort(key=lambda e: (-order.index(e["status"]), e["name"].lower()))
    syns = load_syndicates()
    uni = universe()

    # Coverage: publications known to have run crosswords, by decade and kind.
    kinds = [k for k in build.KINDS if any(e["kind"] == k for e in entries)]
    cols = kinds + ["syndicate"]
    rows = list(range(FIRST_DECADE, THIS_YEAR // 10 * 10 + 1, 10))
    grid = {(d, k): 0 for d in rows for k in cols}
    total = {d: 0 for d in rows}
    undated = 0
    for e in entries:
        e["_decades"] = decades(years(e))
        undated += not e["_decades"]
        for d in e["_decades"]:
            grid[d, e["kind"]] += 1
            total[d] += 1
    for s in syns:
        for d in decades(syndicate_years(s)):
            grid[d, "syndicate"] += 1
    peak = max([grid[d, k] for d in rows for k in kinds] or [1])
    speak = max([grid[d, "syndicate"] for d in rows] or [1])

    def cell(d, k):
        n = grid[d, k]
        if not n:
            return '<td class="blank" title="none known"></td>'
        share = (n / (speak if k == "syndicate" else peak)) ** 0.5
        pct = round(12 + 78 * share)
        ink = "var(--bg)" if pct > 50 else "var(--ink)"
        noun = "syndicate" if k == "syndicate" else KIND_LABELS[k].lower()[:-1]
        tip = f"{n} {noun}{'s' if n != 1 else ''} known in the {d}s"
        attrs = "" if k == "syndicate" else f' data-kind="{k}" data-decade="{d}" tabindex="0" role="button"'
        return (f'<td class="n" style="background:color-mix(in srgb, var(--accent) {pct}%, var(--surface));color:{ink}"'
                f' title="{tip}"{attrs}>{n}</td>')

    head = "".join(f"<th>{KIND_LABELS[k]}</th>" for k in cols)
    grid_rows = "\n".join(
        f'<tr><th scope="row">{d}s</th>{"".join(cell(d, k) for k in cols)}<td class="tot">{total[d] or ""}</td></tr>'
        for d in rows)

    # The register.
    def status_pill(s):
        return f'<span class="pill" style="--c:{STATUS_COLORS[s]}">{esc(STATUS_LABELS.get(s, s))}</span>'

    reg_rows = []
    for e in entries:
        cw = e.get("crosswords") or {}
        run = build.span({"crosswords": cw, "sightings": e.get("sightings")}).split(" · ")[0]
        ys = years(e)
        nsee = len(e.get("sightings") or [])
        c = e.get("corpus") or {}
        held = c.get("puzzles") or 0
        held_years = c.get("years") if c.get("years") not in (None, "unknown") else ""
        srcs = [s for s in e.get("sources") or [] if s["where"] != "the xd Crossword Corpus"]
        help_ = not srcs
        where = e.get("place") or e.get("country") or ""
        url = BLOB + e["_path"].relative_to(ROOT).as_posix()
        reg_rows.append(
            f'<tr data-kind="{e["kind"]}" data-status="{e["status"]}" data-decades="{" ".join(map(str, e["_decades"]))}"'
            f'{" data-help" if help_ else ""}>'
            f'<td data-s="{esc(e["name"].lower())}"><a href="{url}">{esc(e["name"])}</a>'
            f'{" <span class=help>Unknown: can you help?</span>" if help_ else ""}</td>'
            f'<td>{esc(e["kind"])}</td>'
            f'<td data-s="{esc(where.lower())}">{esc(where)}</td>'
            f'<td data-s="{min(ys) if ys else 9999}" class="nw">{esc(run)}</td>'
            f'<td data-s="{nsee}" class="r">{nsee or ""}</td>'
            f'<td data-s="{held}" class="r">{f"{held:,}" if held else ""}'
            f'{f"<div class=sub>{esc(held_years)}</div>" if held_years else ""}</td>'
            f'<td data-s="{order.index(e["status"])}">{status_pill(e["status"])}</td></tr>')
    n_help = sum(1 for r in reg_rows if " data-help>" in r)

    counts = {s: sum(1 for e in entries if e["status"] == s) for s in build.STATUSES}
    held_total = sum((e.get("corpus") or {}).get("puzzles") or 0 for e in entries)
    held_pubs = sum(1 for e in entries if (e.get("corpus") or {}).get("puzzles"))
    by_kind = ", ".join(f"{sum(1 for e in entries if e['kind'] == k)} {KIND_LABELS[k].lower()}" for k in kinds)
    status_bar = "".join(
        f'<span style="flex:{n};background:{STATUS_COLORS[s]}" title="{esc(STATUS_LABELS.get(s, s))}: {n}"></span>'
        for s, n in counts.items() if n)
    status_key = "".join(
        f'<span class="key"><span class="sw" style="background:{STATUS_COLORS[s]}"></span>{n} {esc(STATUS_LABELS.get(s, s))}</span>'
        for s, n in counts.items() if n)

    research = list(RESEARCH)
    named = {r[0] for r in research}
    for p in sorted(ROOT.glob("research-notes-*.md")):
        if p.name not in named:
            research.append((p.name, title_of(p), ""))
    research_html = "\n".join(
        f'<li><a href="{(TREE if path.endswith("/") else BLOB) + path}">{esc(t)}</a>{f": {esc(d)}" if d else ""}</li>'
        for path, t, d in research if (ROOT / path).exists())

    kind_opts = "".join(f'<option value="{k}">{KIND_LABELS[k]}</option>' for k in kinds)
    status_opts = "".join(f'<option value="{s}">{esc(STATUS_LABELS.get(s, s))}</option>' for s in build.STATUSES if counts[s])
    decade_opts = "".join(f'<option value="{d}">{d}s</option>' for d in rows)

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Crossword Census</title>
<meta name="description" content="A census of every publication that has printed crosswords: {len(entries)} so far.">
<link rel="stylesheet" href="https://everypuzzleproject.org/site.css">
<style>
.lede {{ font: 18px/1.5 var(--serif); max-width: 46em; }}
.big {{ font: 600 44px/1.1 var(--serif); margin: 4px 0 12px; }}
.big small {{ font: 400 18px var(--sans); color: var(--muted); }}
.statusbar {{ display: flex; height: 10px; border-radius: 3px; overflow: hidden; margin: 12px 0 6px; max-width: 46em; }}
.legend {{ display: flex; flex-wrap: wrap; gap: 4px 14px; font-size: 13px; color: var(--muted); }}
.key {{ display: inline-flex; align-items: center; gap: 6px; }}
.sw {{ width: 10px; height: 10px; border-radius: 2px; display: inline-block; }}
.scroll {{ overflow-x: auto; -webkit-overflow-scrolling: touch; }}
table {{ border-collapse: collapse; font-size: 14px; }}
th, td {{ padding: 6px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ font-weight: 600; }}
#grid {{ font-variant-numeric: tabular-nums; }}
#grid th, #grid td {{ text-align: center; border: 2px solid var(--bg); min-width: 52px; }}
#grid thead th {{ font-size: 12px; font-weight: 500; color: var(--muted); vertical-align: bottom; }}
#grid tbody th {{ text-align: right; color: var(--muted); font-weight: 500; }}
#grid td.blank {{ background: repeating-linear-gradient(135deg, transparent 0 5px, var(--line) 5px 6px); }}
#grid td.n {{ font-weight: 600; }}
#grid td[role=button] {{ cursor: pointer; }}
#grid td[role=button]:hover, #grid td[role=button]:focus {{ outline: 2px solid var(--ink); outline-offset: -2px; }}
#grid td.tot {{ color: var(--muted); }}
.filters {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 10px 0; font-size: 14px; }}
input, select, button {{ font: inherit; padding: 5px 8px; background: var(--surface); color: var(--ink); border: 1px solid var(--line); border-radius: 4px; }}
#q {{ flex: 1 1 14em; min-width: 0; }}
label.chk {{ display: inline-flex; gap: 6px; align-items: center; }}
#reg {{ width: 100%; }}
#reg th {{ cursor: pointer; white-space: nowrap; user-select: none; }}
#reg th[aria-sort=ascending]::after {{ content: " ▲"; font-size: 10px; }}
#reg th[aria-sort=descending]::after {{ content: " ▼"; font-size: 10px; }}
#reg td.r {{ text-align: right; font-variant-numeric: tabular-nums; }}
#reg td.nw {{ white-space: nowrap; }}
#reg tr[data-help] {{ background: color-mix(in srgb, var(--warm) 10%, transparent); }}
.help {{ display: inline-block; font-size: 12px; font-weight: 600; color: var(--warm); white-space: nowrap; }}
.sub {{ font-size: 12px; color: var(--muted); white-space: nowrap; }}
.pill {{ font-size: 12px; padding: 1px 7px; border-radius: 9px; white-space: nowrap; border: 1px solid var(--c); color: var(--c); }}
.count {{ font-size: 13px; color: var(--muted); }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; }}
.card b a {{ font-weight: 600; }}
.card p {{ margin: 4px 0 0; font-size: 14px; }}
ul.notes {{ padding-left: 20px; }} ul.notes li {{ margin: 3px 0; }}
footer {{ margin-top: 40px; font-size: 13px; color: var(--muted); }}
@media (max-width: 600px) {{ .big {{ font-size: 34px; }} #grid th, #grid td {{ min-width: 28px; padding: 4px 2px; }} #grid thead th {{ font-size: 10px; }} #grid {{ font-size: 13px; }} }}
</style></head><body>
<header class="epp-header"><div class="wrap">
  <a href="https://everypuzzleproject.org/">Every Puzzle Project</a>
  <span class="epp-page">Census</span>
  <nav><a href="{REPO}">Repo</a></nav>
</div></header>
<main class="wrap">
<h1>The Crossword Census</h1>
<p class="big">{len(entries)} publications <small>so far</small></p>
<p class="lede">A census in progress of the newspapers, magazines, books and websites that have run crosswords, from the
first one in 1913 to today: when each ran them, where copies survive, and how far each is from being preserved. It pairs
with the {XD} Crossword Corpus: the census is what exists, the corpus is what we have.</p>
<p class="lede">Against a floor of at most about <b>{uni["dailies"]}</b> US daily newspapers and <b>{uni["weeklies"]}</b> weeklies
that existed since 1913, before a single magazine, book or website is counted. Each entry is made from evidence, not a guess:
puzzles already in the {XD} Crossword Corpus, readers' sightings, and trade directories and research; the denominator is
counted from the Library of Congress newspaper directory, as <a href="{BLOB}universe.md">the known universe</a> explains.</p>
<div class="statusbar">{status_bar}</div>
<div class="legend">{status_key}</div>
<p class="muted" style="font-size:14px">{by_kind}. {held_total:,} puzzles from {held_pubs} of them are already preserved in the
{XD} Crossword Corpus.</p>

<h2>Coverage by decade</h2>
<p class="muted" style="font-size:14px">How many publications the census knows ran crosswords in each decade: the stated run,
widened by sightings, plus the years of its puzzles in the corpus. Hatched cells are the blank regions of the map, where
nothing is known yet. Syndicates (from <a href="{TREE}syndicates">syndicates/</a>, counted by their crossword features) are not
publications and aren't in the {len(entries)}; their counts rest mostly on Editor &amp; Publisher's Syndicate Directory, which
the census has read only to 2000, so after that they thin out. Click a number to list those publications.</p>
<div class="scroll"><table id="grid"><thead><tr><th></th>{head}<th>All</th></tr></thead><tbody>
{grid_rows}
</tbody></table></div>
{f'<p class="muted" style="font-size:13px">{undated} entr{"y has" if undated == 1 else "ies have"} no dated run yet and appear in no decade.</p>' if undated else ""}

<h2>The register</h2>
<p class="muted" style="font-size:14px">Every entry, with a link to its page of facts and sources. <span class="help">Unknown: can you help?</span>
marks the {n_help} entries with no known source for their pages yet. Click a column to sort.</p>
<div class="filters">
  <input id="q" type="search" placeholder="Search name or place…" aria-label="Search">
  <select id="fk" aria-label="Kind"><option value="">All kinds</option>{kind_opts}</select>
  <select id="fd" aria-label="Decade"><option value="">All decades</option>{decade_opts}</select>
  <select id="fs" aria-label="Status"><option value="">All statuses</option>{status_opts}</select>
  <label class="chk"><input id="fh" type="checkbox"> Needs help</label>
  <span id="count" class="count"></span>
</div>
<div class="scroll"><table id="reg"><thead><tr>
<th data-t="s">Publication</th><th data-t="s">Kind</th><th data-t="s">Where</th><th data-t="n">Years</th>
<th data-t="n">Sightings</th><th data-t="n">In the corpus</th><th data-t="n" aria-sort="descending">Status</th>
</tr></thead><tbody>
{chr(10).join(reg_rows)}
</tbody></table></div>
<p class="muted" style="font-size:13px"><b>Status</b> follows a publication through the project: <i>lead</i> (reported, needs research),
<i>researched</i> (we know where copies are), <i>harvesting</i> (scans being found and read), <i>blitzing</i> (puzzles being checked,
see <a href="https://github.com/EveryPuzzleProject/blitz">blitz</a>), <i>in the corpus</i> (some of its puzzles are preserved; the
rest of its run is unresearched), <i>archived</i> (its whole known run is in the corpus).</p>

<h2>How to help</h2>
<div class="cards">
  <div class="card"><b><a href="{NEW_ISSUE}report-puzzle.yml">Report a puzzle</a></b>
    <p>Seen a crossword somewhere? Tell us the publication and the date. One puzzle in June 1994 says a publication ran
    crosswords then; another in 1996 gives a range.</p></div>
  <div class="card"><b><a href="{NEW_ISSUE}report-publication.yml">Report a publication</a></b>
    <p>Know a newspaper, magazine, book or website that ran crosswords? Tell us what you know about it.</p></div>
  <div class="card"><b>Fill in a gap</b>
    <p>Entries marked <span class="help">Unknown: can you help?</span> need someone to find where their pages survive: the
    Internet Archive, Chronicling America, HathiTrust, a library's microfilm. Edit the entry on GitHub, or open a report.</p></div>
  <div class="card"><b><a href="{REPO}/issues?q=is%3Aopen+label%3Alead">Research a lead</a></b>
    <p>Point your Claude at an entry or an open lead and ask it to find when the publication ran crosswords and where scans
    exist, then open a pull request with what it found.</p></div>
</div>

<h2>The research</h2>
<p class="muted" style="font-size:14px">The notes behind the register: original work, and corrections are welcome.</p>
<ul class="notes">
{research_html}
</ul>

<footer>Part of the <a href="https://everypuzzleproject.org/">Every Puzzle Project</a>. Built from
<a href="{REPO}">EveryPuzzleProject/census</a> on {dt.date.today().isoformat()}. Metadata only: no puzzles are published here.</footer>
</main>
<script>
const rows = [...document.querySelectorAll('#reg tbody tr')];
const q = document.getElementById('q'), fk = document.getElementById('fk'), fd = document.getElementById('fd'),
      fs = document.getElementById('fs'), fh = document.getElementById('fh'), count = document.getElementById('count');
function filter() {{
  const t = q.value.trim().toLowerCase();
  let n = 0;
  for (const r of rows) {{
    const hide = (fk.value && r.dataset.kind !== fk.value) || (fs.value && r.dataset.status !== fs.value) ||
      (fd.value && !r.dataset.decades.split(' ').includes(fd.value)) || (fh.checked && !r.hasAttribute('data-help')) ||
      (t && !r.textContent.toLowerCase().includes(t));
    r.hidden = hide; if (!hide) n++;
  }}
  count.textContent = n === rows.length ? `${{n}} entries` : `${{n}} of ${{rows.length}} entries`;
}}
[q, fk, fd, fs, fh].forEach(el => el.addEventListener(el === q ? 'input' : 'change', filter));
const ths = [...document.querySelectorAll('#reg th')], body = document.querySelector('#reg tbody');
ths.forEach((th, i) => th.addEventListener('click', () => {{
  const dir = th.getAttribute('aria-sort') === 'ascending' ? -1 : 1, num = th.dataset.t === 'n';
  ths.forEach(h => h.removeAttribute('aria-sort'));
  th.setAttribute('aria-sort', dir > 0 ? 'ascending' : 'descending');
  const key = r => {{ const c = r.cells[i]; const v = c.dataset.s ?? c.textContent.trim().toLowerCase(); return num ? +v : v; }};
  rows.sort((a, b) => {{ const x = key(a), y = key(b); return (x < y ? -1 : x > y ? 1 : 0) * dir; }});
  rows.forEach(r => body.appendChild(r));
}}));
document.querySelectorAll('#grid td[role=button]').forEach(td => {{
  const go = () => {{ fk.value = td.dataset.kind; fd.value = td.dataset.decade; fs.value = ''; fh.checked = false; q.value = '';
    filter(); document.getElementById('reg').scrollIntoView({{behavior: 'smooth'}}); }};
  td.addEventListener('click', go);
  td.addEventListener('keydown', ev => {{ if (ev.key === 'Enter' || ev.key === ' ') {{ ev.preventDefault(); go(); }} }});
}});
filter();
</script>
</body></html>
"""
    out = ROOT / "site"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8", newline="\n")
    print(f"site/index.html: {len(entries)} publications, {n_help} need help, {held_total:,} puzzles in the corpus "
          f"from {held_pubs}; {len(syns)} syndicates; {undated} undated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
