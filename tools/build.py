"""Check every publication entry and rebuild the catalog table in README.md.

    python tools/build.py           check the entries and rewrite README.md's table
    python tools/build.py --check   only check the entries (pull requests)

Each entry is publications/<slug>.md: YAML front matter (the facts) and free
notes below it. Needs PyYAML.
"""
import re
import sys
from pathlib import Path

import yaml

KINDS = ["newspaper", "magazine", "book", "website", "other"]
STATUSES = {  # in pipeline order
    "lead": "Lead: reported, needs research",
    "researched": "Researched: ready to find scans",
    "harvesting": "Harvesting: scans being read",
    "blitzing": "Blitzing: puzzles being checked",
    "archived": "Archived",
}
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"
USTART, UEND = "<!-- universe:start -->", "<!-- universe:end -->"


def load(path: Path) -> tuple[dict, list[str]]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.S)
    if not m:
        return {}, [f"{path}: no front matter between --- lines"]
    try:
        e = yaml.safe_load(m[1]) or {}
    except yaml.YAMLError as err:
        return {}, [f"{path}: {err}"]
    errors = []
    if not e.get("name"):
        errors.append(f"{path}: needs a name")
    if e.get("kind") not in KINDS:
        errors.append(f"{path}: kind must be one of {', '.join(KINDS)}")
    if e.get("status") not in STATUSES:
        errors.append(f"{path}: status must be one of {', '.join(STATUSES)}")
    if not isinstance(e.get("sources", []), list) or any(not isinstance(s, dict) or not s.get("where") for s in e.get("sources") or []):
        errors.append(f"{path}: sources must be a list of entries, each with a 'where'")
    if not isinstance(e.get("sightings", []), list) or any(not isinstance(s, dict) or not s.get("date") for s in e.get("sightings") or []):
        errors.append(f"{path}: sightings must be a list of entries, each with a 'date'")
    cw = e.get("crosswords") or {}
    errors += dated_list(path, "crosswords.editors", cw.get("editors"), "name", allow_text=True)
    errors += dated_list(path, "carries", e.get("carries"), "feature")
    if cw.get("per_year") is not None and not isinstance(cw["per_year"], (int, float)):
        errors.append(f"{path}: crosswords.per_year must be a number (distinct puzzles a year, roughly)")
    return e, errors


def dated_list(path: Path, label: str, items, key: str, allow_text: bool = False) -> list[str]:
    """editors and carries: a list of {<key>, from, to, source}. Every entry
    needs a source, so a claim can be checked. Editors may also be plain text."""
    if items is None or (allow_text and isinstance(items, str)):
        return []
    if not isinstance(items, list):
        return [f"{path}: {label} must be a list"]
    bad = [i for i in items if not (isinstance(i, dict) and i.get(key) and i.get("source"))]
    return [f"{path}: every {label} entry needs a '{key}' and a 'source'"] if bad else []


def year(v) -> str:
    v = str(v or "?").split(" (")[0]
    return v[:4] if re.match(r"\d{4}", v) else v


def span(e: dict) -> str:
    """The known run: the stated first and last crosswords, widened by any
    reported sightings ("1994–1996 · 2 sightings")."""
    cw = e.get("crosswords") or {}
    seen = sorted(year(s.get("date")) for s in e.get("sightings") or [] if re.match(r"\d{4}", year(s.get("date"))))
    first, last = year(cw.get("first")) if cw.get("first") else "?", year(cw.get("last")) if cw.get("last") else "?"
    if seen:
        if not first[:4].isdigit() or seen[0] < first:
            first = seen[0]
        if (not last[:4].isdigit() and last != "ongoing") or (last[:4].isdigit() and seen[-1] > last):
            last = seen[-1]
    text = first if first == last else f"{first}–{last}"
    n = len(e.get("sightings") or [])
    return text + (f" · {n} sighting{'s' if n != 1 else ''}" if n else "")


def row(path: Path, e: dict) -> str:
    years = span(e)
    src = ", ".join(f"[{s['where']}]({s['url']})" if s.get("url") else s["where"] for s in e.get("sources") or [])
    return (f"| [{e['name']}](publications/{path.name}) | {e['kind']} | {e.get('place') or e.get('country') or ''} "
            f"| {years} | {src or '**Unknown: can you help?**'} | {e['status']} |")


def rollup(entries) -> str:
    """Counts for universe.md: entries by kind, and how many have the figures
    (a run and puzzles a year) that let us add up distinct puzzles."""
    kinds = {k: [e for _, e in entries if e["kind"] == k] for k in KINDS}
    lines = ["| Kind | Entries | With a puzzle count |", "|---|---|---|"]
    total = 0
    for k, es in kinds.items():
        if not es:
            continue
        counted = [e for e in es if (e.get("crosswords") or {}).get("per_year") and span(e)[:4].isdigit()]
        lines.append(f"| {k} | {len(es)} | {len(counted)} |")
    for _, e in entries:
        cw = e.get("crosswords") or {}
        a, b = year(cw.get("first")), year(cw.get("last"))
        if cw.get("per_year") and a.isdigit() and b.isdigit():
            total += int(cw["per_year"]) * (int(b) - int(a) + 1)
    lines += ["", f"Puzzles in entries that give a run and a yearly count: about {total:,}."
              " This is a floor, not an estimate: it only counts what the catalog knows."]
    return "\n".join(lines)


def main(check: bool) -> int:
    entries, errors = [], []
    for p in sorted(Path("publications").glob("*.md")):
        e, errs = load(p)
        errors += errs
        if not errs:
            entries.append((p, e))
    if errors:
        print("\n".join(errors))
        return 1
    order = list(STATUSES)
    entries.sort(key=lambda pe: (-order.index(pe[1]["status"]), pe[1]["name"].lower()))
    counts = {s: sum(1 for _, e in entries if e["status"] == s) for s in STATUSES}
    summary = ", ".join(f"{n} {s}" for s, n in counts.items() if n)
    table = "\n".join([
        f"**{len(entries)} publications so far** ({summary}).",
        "",
        "| Publication | Kind | Where | Crosswords | Scans | Status |",
        "|---|---|---|---|---|---|",
        *(row(p, e) for p, e in entries),
    ])
    readme = Path("README.md")
    text = readme.read_text(encoding="utf-8")
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: f"{START}\n{table}\n{END}", text, flags=re.S)
    if check:
        print(f"{len(entries)} entries look good.")
        return 0
    uni = Path("universe.md")
    if uni.exists():
        utext = uni.read_text(encoding="utf-8")
        uni.write_text(
            re.sub(re.escape(USTART) + ".*?" + re.escape(UEND), lambda _: f"{USTART}\n{rollup(entries)}\n{UEND}", utext, flags=re.S),
            encoding="utf-8", newline="\n")
    readme.write_text(new, encoding="utf-8", newline="\n")
    print(f"README.md: {len(entries)} publications")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
