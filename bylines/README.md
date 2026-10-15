# Bylines

Who signed the puzzles, publication by publication, with a best guess at each person's
gender. One table per publication, one row per Author as gxd prints it:

| column | |
|---|---|
| `author` | the Author field in gxd, exactly |
| `person` | who we think it is; spelling variants of one person share a `person` |
| `gender` | `F`, `M`, `mixed` (a pair of a woman and a man), `pseudonym`, or `unknown` |
| `basis` | what the call rests on (below) |
| `note` | evidence: the town in the byline, a misprint, a link to `people/` |

What a call can rest on, strongest first:

- **record**: a `people/` entry identifies the person.
- **known**: a well-known constructor whose gender is on record (published interviews,
  their own site); the note says how.
- **title** / **title in byline**: Mrs., Miss, Mr., or a military rank, in the Author or
  in the printed Byline (gxd's Author drops Miss and Mr.; the Byline keeps them).
- **same person**: the same name and town appear elsewhere with a fuller name.
- **same person (initials)**: initials matching the only full name in the table with that
  surname and first initial ("R. Norris" is Rich Norris).
- **Jr.**: printed as Jr.
- **given name**: a first name read as one gender in the US of the time. This is a
  guess; Marion, Leslie, Pat and the like are left `unknown`. For Judge and S&S the names
  are called by hand; for the NYT, from Social Security records of US births 1880–2000
  (names.zip from ssa.gov), when at least 90% of babies with that name were one sex. The
  basis gives the share.
- **joint**: each name called separately; `mixed` is a woman and a man together.
- **initials**: initials only, so `unknown`.

The tables are drafted by `tools/bylines.py draft` and then checked by hand, so they're
the record: correct a row here, not in the script. Counts:

    python tools/bylines.py stats <gxd checkout> judge bylines/judge.csv
    python tools/bylines.py stats <gxd checkout> 'nytimes/[12]*' bylines/nytimes.csv decade

The stats give two shares: **women** (puzzles by women only) and **any woman** (with at
least one woman among the constructors, as XWord Info counts). Counts by person treat each
pair as one person, so they mean little where collaborations are common (the NYT after
2000). The NYT table is checked by hand only for its busiest and most ambiguous names.

A byline names who sent the puzzle in ("Submitted by…"), which is usually but not always
who made it.
