# Census spine: US newspapers by year (Library of Congress)

A first pass at "every US newspaper, by year", built from the Library of
Congress US Newspaper Directory's bulk MARC records by `tools/census_loc.py`.

## Files

- **`loc-titles.csv`**: one row per title record (147,625 rows, one per LCCN).
  `lccn`, `title`, `city`, `state` (postal code; PR/VI/GU/AS for territories,
  blank if unknown), `start` / `end` exactly as cataloged in MARC 008 (`u` =
  unknown digit, `9999` = still published), `frequency` as given (MARC 310, or
  the 008 code), `frequency_norm` (daily / weekly / semiweekly / monthly /
  other / unknown), `language`, and three derived years: `surely_from` /
  `surely_to` (the span the record shows the paper was certainly running) and
  `latest_end` (the latest it can have ended).
- **`loc-counts-by-year.csv`**: 1880–2010, one row per year, counts by
  normalized frequency in three versions:
  - `*_raw`: the naive reading (unknown digits widened as far as they go, so
    `18uu`–`19uu` means 1800–1999; "current" means running until 2009). This
    is close to what the loc.gov directory API's `dates=` filter returns.
  - `*_sure`: titles certainly running that year (a floor).
  - `*_est`: the cleaned estimate (see below). **Use this one.**
  - `daily_est_english`, `weekly_est_english`: the estimate for English-language titles only.

Regenerate with `python tools/census_loc.py [path/to/titles-20091130.xml]`
(default path `../census-data/`; about a minute, stdlib only).

## Source

`https://chronam-bib.s3.amazonaws.com/original_titles/titles-20091130.xml`
(449,431,467 bytes, MD5 `affc98a49fb3310603b5a07f7c68e745`, matching the S3
ETag; downloaded 2026-10-02). It is the MARCXML of the US Newspaper Directory
as of 2009-11-30: 171,912 records, all serial type "newspaper". The bucket
also has small incremental title files to 2011 (not applied) and 2025
holdings files (not used).

## Why the raw counts are wrong, and the cleanup

The directory API gave about 5,300 dailies for 1913, 1925 and 1960 alike. The
raw column reproduces that (5,082 / 5,085 / 4,900). The causes, in order of size:

1. **Unknown end years.** About a quarter of daily records have no exact end:
   `19uu` (17,088 records of all frequencies), `1uuu` (8,657), `18uu`,
   `uuuu`. Read naively, an 1879 mining-camp daily with end `1uuu` "runs"
   until 1999. Cleanup: each record gets bounds from everything it attests
   (imprint dates, numbering, "Description based on" / "Latest issue
   consulted" notes, dated frequency statements, and the start year of a
   linked successor title). Within those bounds, the chance it was still
   running in a given year comes from a Kaplan-Meier lifetime curve of
   exactly dated titles with the same frequency and era (pre-1900, 1900–49,
   1950+). Unknown start years are treated the same way in reverse. This
   gives the fractional `*_est` counts. `*_sure` counts only the certain span.
2. **Duplicate records.** 24,287 records repeat an LCCN already in the file
   (OCLC and LC copies of the same title); we keep the most recently
   changed one. Separately, microform reproduction records (`[microform]`),
   editions (zoned, morning/final, etc.) and recataloged titles appear under
   the same title in the same place. For `sure`/`est`, records with the same
   normalized title, state and city count once per year.
3. **Title changes counted twice.** When a linked successor (785) starts in
   the year its predecessor ends, that year is credited to the successor only.
4. **Frequency over the whole run.** The 008 frequency is the current (last)
   one. Where a dated former frequency (321) exists, e.g. "Weekly, -1937",
   those years use the former frequency.
5. **Not removed:** non-English papers (about 7% of dailies; Ayer counts them
   too, so they stay in, with an English-only column alongside), territories
   (excluded from the counts, kept in `loc-titles.csv`).

Effect on dailies in 1960: raw 4,900 → sure 1,996 → estimate 2,298.

## Checks against outside counts

**Ayer 1930** (N. W. Ayer & Son's Directory of Newspapers and Periodicals,
1930, archive.org `nwayersonsdirect6219unse`; "Tabulated Statement" p. 12 and
"Summary and Comparative Statement" p. 13, and the state statistics boxes).
Ayer counts "Daily" and "Daily, with Sunday edition" separately; the sum is
the number of dailies.

| 1930 | Ayer dailies | LoC est | LoC sure | LoC raw | Ayer weekly newspapers (+ weekly periodicals) | LoC weekly est |
|---|---|---|---|---|---|---|
| Minnesota | 51 (43 + 8; p. 12 table says 42 + 8) | 44 | 40 | 59 | 500 (+51) | 562 |
| Missouri | 80 (67 + 13) | 75 | 65 | 118 | 498 (+69) | 550 |
| Kansas | 68 (58 + 10) | 60 | 57 | 76 | 447 (+32) | 515 |
| Illinois | 170 (141 + 29) | 173 | 128 | 370 | 695 (+148) | 936 |
| US states + DC | 2,802 (2,299 + 569, less 66 in territories) | 2,760 | 2,255 | 5,015 | 11,159 (+1,604) | 13,673 |

Ayer leaves out papers founded in 1929 and lists "only those well
established" (introduction, p. 7), so it runs a little low. On dailies the
estimate agrees with Ayer to within a few percent nationally and within
about 10–15% by state. Weeklies run 10–35% above Ayer's weekly newspapers
(23% nationally; 7% if Ayer's weekly periodicals are added). The LoC file
includes Sunday-only papers and religious, ethnic and other weekly titles that
Ayer files as "weekly periodicals".

**Editor & Publisher, via the Census Bureau** (Statistical Abstract of the
United States 2012, tables 1135–1136,
https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s1135.pdf;
English-language dailies only):

| year | E&P dailies | LoC est (English) |
|---|---|---|
| 1970 | 1,748 | 2,129 |
| 1980 | 1,745 | 2,078 |
| 1990 | 1,611 | 1,893 |
| 2000 | 1,480 | 1,777 |
| 2009 | 1,397 (MN 25, MO 42, KS 35, IL 63) | 1,776 (MN 30, MO 53, KS 45, IL 87) |

After about 1960 the LoC estimate is 20–27% above E&P. Likely causes:
"current" records that were never updated after a paper ceased or merged
(most current records were last touched in a 2004 batch, so the change date
proves nothing); editions or zoned papers cataloged under their own titles;
and legal, business and campus dailies that E&P does not count.

**Illinois Newspaper Project** (https://www.library.illinois.edu/illinoisnewspaperproject/about/identify/number-of-newspapers/,
from Census of Manufactures and directories) gives 120 Illinois dailies in 1930,
against Ayer's 170 and the estimate's 173. Sources disagree on what a daily is.

## Caveats

- Nothing after November 2009. The 2010 row is empty, not a real count.
- Coverage is what US libraries reported holding. A paper with no surviving
  copy anywhere may be missing.
- The live directory (159,019 records at loc.gov in 2026) has been edited
  since 2009. This file is not refreshed.
- `est` is a statistical estimate (fractional, rounded per year). Use it for
  totals and trends, not to decide whether one paper existed.
- The lifetime curves come from the records with exact dates, which may be
  better-documented (longer-lived) papers than the rest.
- The title+place merge can join two different papers that shared a name in
  the same city at the same time. It can also miss a duplicate whose city is
  spelled differently.
- Monthlies here are monthly *newspapers* only; Ayer's 3,756 monthlies are
  mostly magazines, which this directory doesn't cover.
