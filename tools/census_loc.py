"""Build a by-year census of US newspapers from the Library of Congress
US Newspaper Directory bulk MARC records.

    python tools/census_loc.py [titles.xml]

Reads titles-20091130.xml (default: ../census-data/ next to this repo; get it
from https://chronam-bib.s3.amazonaws.com/original_titles/titles-20091130.xml)
and writes census/loc-titles.csv (one row per record) and
census/loc-counts-by-year.csv (1880-2010). See census/README.md for the
cleanup rules. Stdlib only.
"""
import csv
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

NS = "{http://www.loc.gov/MARC21/slim}"
DUMP_YEAR = 2009  # the dump is dated 2009-11-30; nothing is "known" after that
FIRST, LAST = 1880, 2010
FREQS = ["daily", "weekly", "semiweekly", "monthly", "other", "unknown"]
CODE_FREQ = {"d": "daily", "w": "weekly", "c": "semiweekly", "m": "monthly"}  # 008/18
OTHER_CODES = set("abefghijkqstz")  # triweekly (i), biweekly (e), quarterly ...
YEAR = re.compile(r"\b(1[6-9]\d\d|20[0-2]\d)\b")
TERRITORIES = {"pr", "vi", "gu", "as", "nw", "cz", "xx"}


def text_freq(s: str) -> str:
    """Normalize a 310/321 frequency statement."""
    s = s.lower().replace("-", "")
    for word, norm in (("semiweekly", "semiweekly"), ("triweekly", "other"), ("biweekly", "other"),
                       ("daily", "daily"), ("weekly", "weekly"), ("semimonthly", "other"),
                       ("bimonthly", "other"), ("monthly", "monthly")):
        if s.startswith(word):
            return norm
    return "other" if s.strip() and not s.startswith("frequency varies") else "unknown"


def subs(el, tag: str) -> list[dict]:
    out = []
    for d in el.findall(f"{NS}datafield[@tag='{tag}']"):
        f = defaultdict(list)
        for s in d.findall(NS + "subfield"):
            f[s.get("code")].append((s.text or "").strip())
        out.append(f)
    return out


def first(fields: list[dict], code: str) -> str:
    for f in fields:
        if f.get(code):
            return f[code][0]
    return ""


def bounds(d: str, lo_default: int, hi_default: int) -> tuple[int, int]:
    """'18uu' -> (1800, 1899); 'uuuu' -> defaults."""
    if not re.fullmatch(r"\d[\du]{3}", d):
        return lo_default, hi_default
    return int(d.replace("u", "0")), int(d.replace("u", "9"))


def parse(el) -> dict:
    f008 = (el.findtext(f"{NS}controlfield[@tag='008']") or "").ljust(40)
    # LCCN from 010 (001 is usually an OCLC number); the same LCCN can come twice
    lccn = re.sub(r"\s", "", first(subs(el, "010"), "a")) or re.sub(r"\s", "", el.findtext(f"{NS}controlfield[@tag='001']") or "")
    changed = el.findtext(f"{NS}controlfield[@tag='005']") or ""
    dtype, d1, d2, code = f008[6], f008[7:11], f008[11:15], f008[18]
    t245 = subs(el, "245")
    title = " ".join(v for f in t245[:1] for c in "anp" for v in f.get(c, []))
    title = re.sub(r"[\s/:;,.=]+$", "", title)
    loc = subs(el, "752")
    city = re.sub(r"[.\s]+$", "", first(loc, "d")) or re.sub(r"[\s:;,]+$", "", first(subs(el, "260"), "a"))
    ctry = f008[15:18]
    state = ("NE" if ctry[:2] == "nb" else ctry[:2].upper()) if ctry[2] == "u" and ctry != "xxu" else ""
    if not state and ctry.strip()[:2] in TERRITORIES - {"xx"}:
        state = ctry[:2].upper()
    f310, f321 = subs(el, "310"), subs(el, "321")
    freq_text = first(f310, "a").rstrip(" ,")
    norm = CODE_FREQ.get(code) or ("other" if code in OTHER_CODES else text_freq(freq_text))
    # Years at which the paper is attested: imprint, numbering, "Description
    # based on"/"Latest issue consulted", frequency date ranges. Not 362 $z (citations).
    seen = []
    for tag, codes in (("260", "c"), ("362", "a"), ("310", "b"), ("321", "b")):
        for f in subs(el, tag):
            for c in codes:
                for v in f.get(c, []):
                    seen += map(int, YEAR.findall(v))
    for f in subs(el, "500"):
        a = " ".join(f.get("a", []))
        if re.match(r"(description based on|latest issue consulted)", a, re.I):
            seen += map(int, YEAR.findall(a))
    # Former frequencies with dates: [from, to) segments that override the current one.
    segments = []
    for f in f321:
        b = " ".join(f.get("b", []))
        ys = list(map(int, YEAR.findall(b)))
        fq = text_freq(" ".join(f.get("a", [])))
        if ys and fq != "unknown":
            lo = None if b.lstrip("< ").startswith("-") else ys[0]
            hi = ys[-1] if (len(ys) > 1 or lo is None) else None
            if hi is not None:
                segments.append((lo, hi, fq))
    succ = [re.sub(r"\s", "", w[5:]) for f in subs(el, "785") for w in f.get("w", []) if w.startswith("(DLC)")]
    return dict(lccn=lccn, changed=changed, title=title, city=city, state=state, dtype=dtype, d1=d1, d2=d2,
                freq_text=freq_text or code.strip(), norm=norm, lang=f008[35:38].strip(),
                seen=seen, segments=segments, succ=succ)


def spans(r: dict, starts: dict) -> None:
    """Fill start_lo/start_hi (earliest/latest possible start) and end_lo/end_hi
    (earliest/latest possible end). start_hi..end_lo is when it surely ran."""
    slo, shi = bounds(r["d1"], 1690, DUMP_YEAR)
    if r["dtype"] == "c" or r["d2"] == "9999":
        elo, ehi = DUMP_YEAR, DUMP_YEAR
    else:
        elo, ehi = bounds(r["d2"], slo, DUMP_YEAR)
    ehi = min(max(ehi, slo), DUMP_YEAR)
    seen = [y for y in r["seen"] if slo <= y <= ehi]
    if seen:
        shi, elo = min(shi, min(seen)), max(elo, max(seen))
    shi = min(shi, ehi)
    elo = max(elo, shi)
    # A linked successor that began in year S caps this run at S; the year S
    # itself goes to the successor so a title change isn't counted twice.
    r["drop"] = None
    nxt = [starts[s] for s in r["succ"] if starts.get(s)]
    if nxt and r["dtype"] != "c":
        s = min(nxt)
        if s >= elo:
            ehi = min(ehi, s)
            if elo == ehi == s and shi < s:
                r["drop"] = s
            elif ehi == s and elo < s:
                ehi = s - 1
    r.update(start_lo=slo, start_hi=shi, end_lo=elo, end_hi=max(ehi, elo))


def era(y: int) -> int:
    return 0 if y < 1900 else 1 if y < 1950 else 2


def lifetimes(rows: list[dict]) -> dict:
    """Kaplan-Meier survival S(t) = P(run >= t years) by (frequency, era of
    start), from records with exact start and end years; current titles are
    censored at the dump year."""
    groups = defaultdict(list)
    for r in rows:
        if not r["d1"].isdigit():
            continue
        s = int(r["d1"])
        if r["dtype"] == "d" and r["d2"].isdigit():
            t, dead = int(r["d2"]) - s, True
        elif r["dtype"] == "c":
            t, dead = DUMP_YEAR - s, False
        else:
            continue
        if 0 <= t <= 330:
            for key in ((r["norm"], era(s)), ("all", era(s))):
                groups[key].append((t, dead))
    out = {}
    for key, obs in groups.items():
        deaths, gone = Counter(t for t, d in obs if d), Counter(t for t, _ in obs)
        at_risk, S = len(obs), [1.0]
        for t in range(0, 331):
            h = deaths[t] / at_risk if at_risk else 0.0
            S.append(S[-1] * (1 - h))
            at_risk -= gone[t]
        out[key] = [max(v, 1e-6) for v in S]  # S[t] = P(T >= t)
    return out


def weight(r: dict, y: int, S: list[float]) -> float:
    """Expected probability the title ran in year y, given its bounds."""
    if y == r["drop"] or y < r["start_lo"] or y > r["end_hi"]:
        return 0.0
    surv = lambda t: S[min(max(t, 0), len(S) - 1)]
    w = 1.0
    if y < r["start_hi"]:  # start unknown: P(start <= y | ran at start_hi)
        if "cum" not in r:  # running sums of the prior over possible start years
            acc, r["cum"] = 0.0, []
            for s in range(r["start_lo"], r["start_hi"] + 1):
                acc += surv(r["start_hi"] - s)
                r["cum"].append(acc)
        w *= r["cum"][y - r["start_lo"]] / r["cum"][-1]
    if y > r["end_lo"]:  # end unknown: P(end >= y | end in [end_lo, end_hi])
        s0, top = r["start_hi"], surv(r["end_hi"] - r["start_hi"] + 1)
        den = surv(r["end_lo"] - s0) - top
        w *= (surv(y - s0) - top) / den if den > 1e-9 else (r["end_hi"] - y + 1) / (r["end_hi"] - r["end_lo"])
    return w


def freq_in(r: dict, y: int) -> str:
    for lo, hi, fq in r["segments"]:
        if (lo is None or lo <= y) and y < hi:
            return fq
    return r["norm"]


def main(src: Path) -> int:
    latest = {}  # one record per LCCN: the most recently changed copy
    total = 0
    for _, el in ET.iterparse(src):
        if el.tag == NS + "record":
            r, total = parse(el), total + 1
            if r["lccn"] not in latest or r["changed"] > latest[r["lccn"]]["changed"]:
                latest[r["lccn"]] = r
            el.clear()
    rows = list(latest.values())
    starts = {r["lccn"]: int(r["d1"]) for r in rows if r["d1"].isdigit()}
    for r in rows:
        spans(r, starts)
    S = lifetimes(rows)

    out = Path("census")
    out.mkdir(exist_ok=True)
    with open(out / "loc-titles.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["lccn", "title", "city", "state", "start", "end", "frequency", "frequency_norm",
                    "language", "surely_from", "surely_to", "latest_end"])
        for r in sorted(rows, key=lambda r: (r["state"], r["city"], r["title"], r["lccn"])):
            w.writerow([r["lccn"], r["title"], r["city"], r["state"], r["d1"], r["d2"], r["freq_text"],
                        r["norm"], r["lang"], r["start_hi"], r["end_lo"], r["end_hi"]])

    years = range(FIRST, LAST + 1)
    raw, sure, est = (defaultdict(Counter) for _ in range(3))
    english = defaultdict(Counter)
    groups = defaultdict(list)  # same title in the same place: microform copies, editions, recataloging
    for r in rows:
        if not r["state"] or r["state"].lower() in TERRITORIES:
            continue
        # raw: what a naive reading of 008 gives ('u' -> widest span, 9999 -> now)
        rlo = int(r["d1"].replace("u", "0")) if r["d1"][:1].isdigit() else 1690
        rhi = DUMP_YEAR if (r["dtype"] == "c" or not r["d2"][:1].isdigit()) else int(r["d2"].replace("u", "9"))
        for y in range(max(rlo, FIRST), min(rhi, LAST) + 1):
            raw[y][r["norm"]] += 1
        key = re.sub(r"^the|\W", "", r["title"].lower().replace("[microform]", ""))
        groups[(r["state"], r["city"].lower(), key)].append(r)
    for members in groups.values():
        g_est, g_sure = defaultdict(float), set()
        for r in members:
            for y in range(max(r["start_lo"], FIRST), min(r["end_hi"], LAST) + 1):
                fq = freq_in(r, y)
                curve = S.get((fq, era(r["start_hi"]))) or S[("all", era(r["start_hi"]))]
                p = weight(r, y, curve)
                if p:
                    g_est[(y, fq, r["lang"] == "eng")] = max(g_est[(y, fq, r["lang"] == "eng")], p)
                    if r["start_hi"] <= y <= r["end_lo"] and y != r["drop"]:
                        g_sure.add((y, fq))
        for (y, fq, eng), p in g_est.items():
            est[y][fq] += p
            if eng:
                english[y][fq] += p
        for y, fq in g_sure:
            sure[y][fq] += 1
    with open(out / "loc-counts-by-year.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["year"] + [f"{f}_{k}" for k in ("raw", "sure", "est") for f in FREQS]
                   + ["daily_est_english", "weekly_est_english"])
        for y in years:
            w.writerow([y] + [raw[y][f] for f in FREQS] + [sure[y][f] for f in FREQS]
                       + [round(est[y][f]) for f in FREQS]
                       + [round(english[y]["daily"]), round(english[y]["weekly"])])
    print(f"{total} records, {len(rows)} distinct LCCNs -> census/loc-titles.csv, census/loc-counts-by-year.csv")
    return 0


if __name__ == "__main__":
    default = Path(__file__).resolve().parents[2] / "census-data" / "titles-20091130.xml"
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else default))
