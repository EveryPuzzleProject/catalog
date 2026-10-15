"""Who signed the puzzles: one row per Author as gxd prints it, with a person and a gender call.

    python tools/bylines.py draft <gxd> <pub-dir> <out.csv>   first draft of a table, for hand checking
    python tools/bylines.py stats <gxd> <pub-dir> <table.csv> counts by puzzle, person and year

<gxd> is a gxd checkout; <pub-dir> is a folder in it (judge, simonschuster/1924). Puzzles
are read from the files on disk. Tables live in bylines/; see bylines/README.md for the
columns and what each gender call rests on.
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

COLUMNS = ["author", "person", "gender", "basis", "note"]
TITLES = {"mrs": "F", "miss": "F", "mr": "M"}

# Given names read as one gender in the US of the 1920s-30s; anything else is left for a person to call.
WOMEN = set("""Agnes Amy Anna Anne Astrid Bee Betty Catherine Charlotte Dorcas Dorothy Edith Eliza
Elizabeth Ethel Evelyn Gertrude Gladys Grace Helen Henriette Ivy Janet Julie Lillian Lucille Madeleine
Madeline Madge Margaret Marie Marjorie Mary Maude Meg Mildred Mollie Peg Peggy Rosa Rose Ruth Vina
Virginia""".split())
MEN = set("""Albert Alfred Allen Andrew Arthur Benjamin Bob Carl Cecil Charles Charley Daniel Dennis Don
Donald Drake Earl Edward Elbert Eric Everett Frank Fred Gardner Geo George Harold Harry Henry Herbert
Homer Howard Hugh Hugo Irvan Irving Isidore Jack James Jesse John Joseph Karl Leonard Lewis Lionel Lloyd
Luther Mordecai Murray Nathan Norman Omer Oscar Paul Porter Ralph Raymond Rex Richard Robert Rolf Rudd
Russell Sam Samuel Saul Sidney Sylvan Theodore Thomas Virgil Walter Warren Wayne Willard William Wilmer
Wm Woody""".split())


def puzzles(pub: Path):
    for f in sorted(pub.rglob("*.xd")):
        head = {}
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                if head:
                    break
                continue
            k, _, v = line.partition(":")
            head[k.strip().lower()] = v.strip()
        yield f.stem, head


def guess(author: str, byline: str) -> tuple[str, str]:
    t = re.match(r"(Mrs|Miss|Mr)\.? ", author)
    if t:
        return TITLES[t[1].lower()], "title"
    if " and " in author or "&" in author:
        return "", "joint"
    t = re.search(r"\b(Mrs|Miss|Mr)\.? " + re.escape(author.split()[0]), byline)
    if t:
        return TITLES[t[1].lower()], "title in byline"
    first = author.split()[0].rstrip(".")
    if first in WOMEN:
        return "F", "given name"
    if first in MEN:
        return "M", "given name"
    if re.search(r",? Jr\.?$", author) or re.search(re.escape(author) + r",? Jr\b", byline):
        return "M", "Jr."
    if re.fullmatch(r"([A-Z]\. ?)+", author.split(",")[0].rsplit(" ", 1)[0] + " "):
        return "", "initials"
    return "", ""


def draft(gxd, pub, out):
    rows = {}
    for _, h in puzzles(Path(gxd) / pub):
        a = h.get("author", "")
        if a and a not in rows:
            g, basis = guess(a, h.get("byline", ""))
            rows[a] = {"author": a, "person": a, "gender": g, "basis": basis, "note": ""}
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, COLUMNS)
        w.writeheader()
        w.writerows(sorted(rows.values(), key=lambda r: r["author"]))


def stats(gxd, pub, table):
    rows = {r["author"]: r for r in csv.DictReader(open(table, encoding="utf-8"))}
    by_puzzle, by_year, people, missing = Counter(), defaultdict(Counter), {}, Counter()
    for xdid, h in puzzles(Path(gxd) / pub):
        a = h.get("author", "")
        if not a:
            by_puzzle["no byline"] += 1
            continue
        if a not in rows:
            missing[a] += 1
            continue
        g = rows[a]["gender"] or "unknown"
        by_puzzle[g] += 1
        by_year[h.get("date", xdid)[:4] if h.get("date") else "?"][g] += 1
        people[rows[a]["person"]] = g
    if missing:
        sys.exit(f"not in {table}: {dict(missing)}")
    order = ["F", "M", "mixed", "unknown", "pseudonym", "no byline"]
    def line(c):
        known = c["F"] + c["M"]
        share = f"{100 * c['F'] / known:.0f}% women of {known} known" if known else ""
        return "  ".join(f"{k} {c[k]}" for k in order if c[k]) + ("   " + share if share else "")
    print("puzzles:", line(by_puzzle))
    print("people: ", line(Counter(people.values())))
    for y in sorted(by_year):
        print(f"  {y}:", line(by_year[y]))


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    {"draft": draft, "stats": stats}[cmd](*args)
