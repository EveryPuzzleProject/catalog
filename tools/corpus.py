"""Seed and refresh census entries from the xd Crossword Corpus.

    python tools/corpus.py <checkout>          refresh every entry that has corpus.id
    python tools/corpus.py <checkout> --new    also create entries for corpus publications
                                               the census doesn't have yet

<checkout> is a clone of the corpus (the xd repo's gxd/ directory). Only
metadata leaves it: the publication names and URLs in its publications.tsv,
and for each publication the number of .xd files and the years in their
names. No puzzle content is read.

Each census entry can carry a `corpus:` block:

    corpus:
      id: latimes                 # the corpus directory (indie/<x>, student/<x> for those)
      puzzles: 10661              # .xd files under it, every series and mini included
      years: 1924, 1996–2026      # years with at least one puzzle
      as_of: 2026-11-06

This script rewrites puzzles, years and as_of; everything else in the entry
is left alone. Needs PyYAML.
"""
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ENTRIES = Path("publications")
# Corpus directories that are syndicated features, not publications: their
# puzzles appeared in many papers. They belong in syndicates/, not here.
FEATURES = {"king", "tribune", "commuter", "universal", "crossynergy"}
# What kind of thing each corpus publication is. Anything not listed here
# becomes `other` with a note asking for a classification.
KINDS = {
    "newspaper": "bostonglobe chicago kcstar lansing latimes newsday nyheraldtribune nysun nytimes "
                 "nyworld philadelphia usatoday wapost wsj stranger onion",
    "magazine": "aarp amherstmag atlantic billboard brownalumni chronicle cornellians harvardmag mygen "
                "newyorker nymag princetonalumni qrw theweek time unhmag judge walrus washexaminer",
    "website": "applenews arkadium autostraddle avclub bawdy blackcrossword buzzfeed cnn cwclub dailybeast "
               "dailypop defector morningbrew queerty salon slate vox vulture yahoo yalehumanities unshelved",
    "book": "simonschuster crosscanada",
    "other": "crosswordsclub uptown eltana puzzazz",
}
KIND = {d: k for k, ds in KINDS.items() for d in ds.split()}
# Names for corpus directories that hold several series under one maker or publisher.
NAMES = {"indie/gaffney": "Matt Gaffney's puzzles (Daily Crossword, Weekly Crossword Contest)",
         "indie/bequigley": "Brendan Emmett Quigley's puzzles (brendanemmettquigley.com)",
         "indie/abortion": "These Puzzles Fund Abortion",
         "simonschuster": "Simon & Schuster crossword books (The Cross Word Puzzle Book and successors)",
         "nytimes": "The New York Times", "latimes": "Los Angeles Times", "wapost": "The Washington Post",
         "stranger": "The Stranger (Seattle)", "theweek": "The Week", "onion": "The Onion",
         "atlantic": "The Atlantic", "newyorker": "The New Yorker", "walrus": "The Walrus",
         "student/thevarsity": "The Varsity (University of Toronto)",
         "student/villanovan": "The Villanovan (Villanova University)",
         "student/cavalierdaily": "The Cavalier Daily (University of Virginia)",
         "student/studentlife": "Student Life (Washington University in St. Louis)",
         "student/ricethresher": "The Rice Thresher (Rice University)",
         "student/tuftsdaily": "The Tufts Daily", "student/dukechronicle": "The Duke Chronicle",
         "student/cornellsun": "The Cornell Daily Sun", "student/columbiaspectator": "Columbia Daily Spectator",
         "student/amherststudent": "The Amherst Student", "yahoo": "Yahoo (games site)",
         "arkadium": "Arkadium (games site)", "applenews": "Apple News+", "lansing": "Lansing Star (Lansing, New York)"}
COUNTRY = {"walrus": "Canada", "crosscanada": "Canada", "student/thevarsity": "Canada"}
PLACE = {"bostonglobe": "Boston", "chicago": "Chicago", "kcstar": "Kansas City", "lansing": "Lansing, New York",
         "latimes": "Los Angeles", "newsday": "Long Island, New York", "nyheraldtribune": "New York",
         "nysun": "New York", "nytimes": "New York", "nyworld": "New York", "philadelphia": "Philadelphia",
         "wapost": "Washington, D.C.", "stranger": "Seattle", "eltana": "Seattle", "walrus": "Toronto",
         "student/thevarsity": "Toronto"}
YEAR = re.compile(r"(?<!\d)(19[1-9]\d|20[0-4]\d)(?!\d)")


def count(checkout: Path) -> dict[str, tuple[int, list[int]]]:
    """For each publisher directory: how many .xd files, and the years named
    in their paths (file name first, then the year folder)."""
    found: dict[str, tuple[int, set[int]]] = {}
    for p in checkout.rglob("*.xd"):
        rel = p.relative_to(checkout).parts
        pid = "/".join(rel[:2]) if rel[0] in ("indie", "student") else rel[0]
        n, years = found.setdefault(pid, (0, set()))
        m = YEAR.search(p.name) or next((YEAR.fullmatch(part) for part in rel[1:-1] if YEAR.fullmatch(part)), None)
        if m:
            years.add(int(m.group(1)))
        found[pid] = (n + 1, years)
    return {pid: (n, sorted(y)) for pid, (n, y) in found.items()}


def ranges(years: list[int]) -> str:
    out, start, prev = [], None, None
    for y in years + [None]:
        if start is not None and (y is None or y != prev + 1):
            out.append(str(start) if start == prev else f"{start}–{prev}")
            start = None
        if y is not None and start is None:
            start = y
        prev = y
    return ", ".join(out)


def publications(checkout: Path) -> dict[str, dict]:
    """The corpus's own table, one row per publisher directory (the row for
    its main series, or the first row if it has none)."""
    rows = {}
    path = checkout / "publications.tsv"
    if not path.exists():
        return rows
    head, *lines = path.read_text(encoding="utf-8").splitlines()
    cols = head.split("\t")
    for line in lines:
        r = dict(zip(cols, line.split("\t")))
        pub = r.get("PublisherAbbr", "")
        if not pub or not r.get("PublicationName"):
            continue
        base = "/".join(pub.split("/")[:2]) if pub.startswith(("indie/", "student/")) else pub.split("/")[0]
        if base not in rows or (pub == base and rows[base]["PublisherAbbr"] != base):
            rows[base] = r
    return rows


def entries() -> dict[str, Path]:
    """Corpus id -> entry file, for every entry that has corpus.id."""
    out = {}
    for p in sorted(ENTRIES.glob("*.md")):
        m = re.match(r"---\n(.*?)\n---\n", p.read_text(encoding="utf-8").replace("\r\n", "\n"), re.S)
        e = yaml.safe_load(m[1]) if m else {}
        cid = ((e or {}).get("corpus") or {}).get("id")
        if cid:
            out[cid] = p
    return out


def block(cid: str, n: int, years: list[int], today: str) -> str:
    return f"corpus:\n  id: {cid}\n  puzzles: {n}\n  years: \"{ranges(years) or 'unknown'}\"\n  as_of: {today}"


def refresh(path: Path, cid: str, n: int, years: list[int], today: str) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    new = re.sub(r"^corpus:\n(?:[ \t]+.*\n)+", block(cid, n, years, today) + "\n", text, count=1, flags=re.M)
    if new == text:
        new = re.sub(r"^(status:.*\n)", block(cid, n, years, today) + "\n\\1", text, count=1, flags=re.M)
    path.write_text(new, encoding="utf-8", newline="\n")


def slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s[4:] if s.startswith("the-") else s


def create(cid: str, row: dict, n: int, years: list[int], today: str) -> Path:
    base = row.get("PublicationName") or cid
    name = NAMES.get(cid, base)
    if cid not in NAMES and cid.startswith("indie/") and row.get("Contact") and row["Contact"] not in name:
        name = f"{name} ({row['Contact']})"
    kind = "website" if cid.startswith("indie/") else "newspaper" if cid.startswith("student/") else KIND.get(cid, "other")
    first = row.get("FirstIssueDate") or (str(years[0]) if years else "unknown")
    last = row.get("LastIssueDate") or (str(years[-1]) if years else "unknown")
    first = first[1:] + " (or earlier)" if first.startswith("<") else first
    last = "ongoing" if last == "today" else last
    lines = [f"name: {name}", f"kind: {kind}", f"country: {COUNTRY.get(cid, 'US')}"]
    if cid in PLACE:
        lines.append(f"place: {PLACE[cid]}")
    lines += ["crosswords:", f"  first: {first}", f"  last: {last}"]
    if row.get("Contact") and not cid.startswith("indie/"):
        lines.append(f"  editors: {row['Contact']}")
    lines.append("sources:")
    lines.append("  - where: the xd Crossword Corpus")
    lines.append("    url: https://xd.saul.pw/")
    lines.append(f"    covers: \"{n:,} puzzles, {ranges(years) or 'years unknown'}\"")
    lines.append("    access: the corpus itself is private; its publication list and counts are public")
    for url in (row.get("Sources") or "").split():
        if url.startswith("http"):
            lines.append("  - where: its own site")
            lines.append(f"    url: {url}")
            lines.append("    access: unknown")
            break
    lines.append(block(cid, n, years, today))
    lines.append("status: corpus")
    notes = [f"Seeded from the xd Crossword Corpus on {today}: the corpus holds {n:,} of its puzzles "
             f"({ranges(years) or 'years unknown'}), counted from file names, every series and mini included. "
             "Everything else about this publication is still to be researched: when its crosswords began "
             "and ended, who made them, and where printed copies survive."]
    if cid not in KIND and not cid.startswith(("indie/", "student/")):
        notes.append("Kind not established: what sort of publication this was is not known from the corpus's "
                     "metadata. Can you help?")
    text = "---\n" + "\n".join(lines) + "\n---\n\n" + "\n\n".join(notes) + "\n"
    path = ENTRIES / f"{slug(base if cid not in NAMES else name.split(' (')[0])}.md"
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    checkout = Path(args[0])
    today = date.today().isoformat()
    counts = count(checkout)
    rows = publications(checkout)
    have = entries()
    for cid, path in have.items():
        if cid in counts:
            refresh(path, cid, *counts[cid], today)
            print(f"refreshed {path} from {cid}: {counts[cid][0]:,} puzzles")
        else:
            print(f"{path}: corpus.id {cid} not in the checkout", file=sys.stderr)
    if "--new" in argv:
        for cid in sorted(counts):
            if cid in have or cid in FEATURES:
                continue
            path = create(cid, rows.get(cid, {}), *counts[cid], today)
            print(f"created {path} from {cid}: {counts[cid][0]:,} puzzles")
    skipped = sorted(FEATURES & counts.keys())
    if skipped:
        print(f"syndicated features left out (see syndicates/): {', '.join(skipped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
