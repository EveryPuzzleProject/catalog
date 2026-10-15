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
- **title** / **title in byline**: Mrs., Miss, Mr., or a military rank, in the Author or
  in the printed Byline (gxd's Author drops Miss and Mr.; the Byline keeps them).
- **same person**: the same name and town appear elsewhere with a fuller name.
- **Jr.**: printed as Jr.
- **given name**: a first name read as one gender in the US of the time. This is a
  guess; Marion, Leslie, Pat and the like are left `unknown`.
- **initials**: initials only, so `unknown`.

The tables are drafted by `tools/bylines.py draft` and then checked by hand, so they're
the record: correct a row here, not in the script. Counts:

    python tools/bylines.py stats <gxd checkout> judge bylines/judge.csv

A byline names who sent the puzzle in ("Submitted by…"), which is usually but not always
who made it.
