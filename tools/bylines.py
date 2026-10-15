"""Who signed the puzzles: one row per Author as gxd prints it, with a person and a gender call.

    python tools/bylines.py draft <gxd> <pub-dir> <out.csv> [<ssa-dir>]   first draft, for hand checking
    python tools/bylines.py stats <gxd> <pub-dir> <table.csv> [decade]    counts by puzzle, person and year

<gxd> is a gxd checkout; <pub-dir> is a folder in it (judge, simonschuster/1924) or a glob
("nytimes/[12]*": the NYT daily, leaving out the mini and the bonus puzzles).
Puzzles are read from the files on disk. <ssa-dir> is the unzipped Social Security baby-name
file (names.zip from ssa.gov, yobNNNN.txt); with it, given names the short lists below don't
cover are called from US births 1880-2000 when at least 90% went one way. Tables live in
bylines/; see bylines/README.md for the columns and what each gender call rests on.
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

COLUMNS = ["author", "person", "gender", "basis", "note"]
TITLES = {"mrs": "F", "miss": "F", "mr": "M"}
SSA_YEARS = range(1880, 2001)
SSA_SURE = 0.90

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
SUFFIX = r",? (Jr|Sr|II|III|IV|M\.?D|Ph\.?D)\.?$"


def puzzles(gxd, pub: str):
    """Every puzzle under gxd/<pub>; <pub> may be a glob ('nytimes/[12]*' is the daily, without the mini)."""
    dirs = sorted(Path(gxd).glob(pub)) if any(c in pub for c in "*?[") else [Path(gxd) / pub]
    for f in sorted(f for d in dirs for f in d.rglob("*.xd")):
        head = {}
        with f.open(encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    if head:
                        break
                    continue
                k, _, v = line.partition(":")
                head[k.strip().lower()] = v.strip()
        yield f.stem, head


def load_ssa(d):
    counts = defaultdict(Counter)
    for y in SSA_YEARS:
        for line in open(Path(d) / f"yob{y}.txt", encoding="utf-8"):
            name, sex, n = line.strip().split(",")
            counts[name][sex] += int(n)
    return counts


def given_name(name: str):
    """The name someone went by: 'Eugene T. Maleska' -> Eugene, 'F. Karl Travis' -> Karl."""
    words = [w for w in re.sub(SUFFIX, "", name).split() if not re.fullmatch(r"([A-Z]\.?)+", w)]
    return words[0].rstrip(".,") if len(words) >= 2 else None


def guess_one(name: str, byline: str, ssa) -> tuple[str, str]:
    t = re.match(r"(Mrs|Miss|Mr)\.? ", name)
    if t:
        return TITLES[t[1].lower()], "title"
    if name.split() and re.search(r"\b(Mrs|Miss|Mr)\.? " + re.escape(name.split()[0]), byline):
        t = re.search(r"\b(Mrs|Miss|Mr)\.? " + re.escape(name.split()[0]), byline)
        return TITLES[t[1].lower()], "title in byline"
    first = given_name(name)
    if first in WOMEN:
        return "F", "given name"
    if first in MEN:
        return "M", "given name"
    if re.search(r",? Jr\.?$", name) or re.search(re.escape(name) + r",? Jr\b", byline):
        return "M", "Jr."
    if first and ssa is not None and first in ssa:
        c = ssa[first]
        share = c["F"] / (c["F"] + c["M"])
        if share >= SSA_SURE:
            return "F", f"given name (SSA {share:.0%} F)"
        if share <= 1 - SSA_SURE:
            return "M", f"given name (SSA {1 - share:.0%} M)"
        return "", f"given name ambiguous (SSA {share:.0%} F)"
    if not first:
        return "", "initials" if re.search(r"[A-Z]\.", name) else "surname only"
    return "", ""


def split_joint(author: str) -> list[str]:
    parts = re.split(r" and | & | / |; |, (?!(?:Jr|Sr|II|III|IV|M\.?D|Ph\.?D)\b)", author)
    # 'Jan and Mike Dubin': the surname is shared
    last = parts[-1].split()[-1] if parts[-1].split() else ""
    return [p if len(p.split()) > 1 else f"{p} {last}" for p in parts if p.strip()]


def guess(author: str, byline: str, ssa=None) -> tuple[str, str]:
    if author.startswith("Mr. and Mrs."):
        return "mixed", "title"
    parts = split_joint(author)
    if len(parts) == 1:
        return guess_one(author, byline, ssa)
    calls = [guess_one(p, byline, ssa)[0] for p in parts]
    if "" in calls:
        return ("", "joint, partly unknown") if set(calls) - {""} != {"F"} else ("", "joint, a woman and unknown")
    return ({"F": "F", "M": "M"}.get("".join(sorted(set(calls))), "mixed"), "joint")


def link_initials(rows):
    """'R. Norris' is Rich Norris when he's the only Norris with an R. in the table."""
    full = defaultdict(list)
    for r in rows.values():
        first = given_name(r["author"])
        if first and r["gender"] in ("F", "M"):
            full[(first[0], r["author"].split()[-1])].append(r)
    for r in rows.values():
        a = re.sub(SUFFIX, "", r["author"])
        if r["gender"] == "unknown" and r["basis"] == "initials" and len(a.split()) > 1:
            match = full.get((a[0], a.split()[-1]), [])
            if len(match) == 1:
                r.update(person=match[0]["person"], gender=match[0]["gender"], basis="same person (initials)")


def draft(gxd, pub, out, ssa_dir=None):
    ssa = load_ssa(ssa_dir) if ssa_dir else None
    rows = {}
    for _, h in puzzles(gxd, pub):
        a = h.get("author", "")
        if a and a != "Unknown" and a not in rows:
            a_ = re.sub(r"^puzzle by ", "", a, flags=re.I)
            g, basis = guess(a_, h.get("byline", ""), ssa)
            rows[a] = {"author": a, "person": a, "gender": g or "unknown", "basis": basis, "note": ""}
    link_initials(rows)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, COLUMNS)
        w.writeheader()
        w.writerows(sorted(rows.values(), key=lambda r: r["author"]))


def stats(gxd, pub, table, group="year"):
    rows = {r["author"]: r for r in csv.DictReader(open(table, encoding="utf-8"))}
    by_puzzle, by_year, people, year_people, missing = Counter(), defaultdict(Counter), {}, defaultdict(dict), Counter()
    for xdid, h in puzzles(gxd, pub):
        a = h.get("author", "")
        y = (h.get("date") or "?")[:4]
        y = y[:3] + "0s" if group == "decade" and y != "?" else y
        if not a or a == "Unknown":
            by_puzzle["no byline"] += 1
            by_year[y]["no byline"] += 1
            continue
        if a not in rows:
            missing[a] += 1
            continue
        g = rows[a]["gender"] or "unknown"
        by_puzzle[g] += 1
        by_year[y][g] += 1
        people[rows[a]["person"]] = g
        year_people[y][rows[a]["person"]] = g
    if missing:
        sys.exit(f"not in {table}: {dict(missing)}")
    order = ["F", "M", "mixed", "unknown", "pseudonym", "no byline"]

    def line(c):
        known = c["F"] + c["M"] + c["mixed"]
        out = "  ".join(f"{k} {c[k]}" for k in order if c[k])
        if known:
            out += f"   women {100 * c['F'] / known:.0f}%, any woman {100 * (c['F'] + c['mixed']) / known:.0f}% of {known} known"
        return out
    print("puzzles:", line(by_puzzle))
    print("people: ", line(Counter(people.values())))
    for y in sorted(by_year):
        print(f"  {y} puzzles:", line(by_year[y]))
        if group == "decade":
            print(f"  {y} people: ", line(Counter(year_people[y].values())))


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    {"draft": draft, "stats": stats}[cmd](*args)
