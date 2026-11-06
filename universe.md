# The known universe

How many crosswords have been published? Nobody knows, and this page doesn't
pretend to. It's where we keep the best current guess and the reasons for it,
so the guess can improve as the [catalog](README.md) fills in. Every number
here should say what it rests on; a line with nothing behind it says *unknown*.

## Two numbers, not one

- **Distinct puzzles**: grids that someone constructed. A syndicated daily is
  one puzzle a day, however many papers print it.
- **Printings**: appearances in print. The same syndicated grid in 400 papers
  is 400 printings. Printings dwarf distinct puzzles, but only distinct
  puzzles can ever be digitized once.

## Where the puzzles come from

For each category we want a count of outlets, puzzles a year, and the years
covered, as a low–high range. So far only the number of newspapers that
existed is known, from the Library of Congress directory in [census/](census/);
how many of them printed crosswords, and how many puzzles a year, is not
estimated yet. The outlet counts are distinct titles (one per title, city and
state) with a run reaching 1913 or later, computed from
`census/loc-titles.csv` on 2026-11-06; the directory's unknown end years make
these generous, and the directory stops in 2009.

| Category | Outlets | Puzzles a year | Years | Rests on |
|---|---|---|---|---|
| Daily newspapers, original puzzles (US) | at most about 10,300 dailies existed since 1913 (9,800 English-language); the share that printed crosswords is unknown | | | census/loc-titles.csv, `frequency_norm` daily, `latest_end` ≥ 1913 |
| Syndicated daily and Sunday features (US) | 9 features in 1924, 65 in 2000 (E&P's Syndicate Directory, sampled every five years) | | 1924–2000 | census/ep-crossword-features.md |
| Weekly and monthly papers, local papers | at most about 54,000 weeklies, 2,500 semiweeklies and 4,700 monthly newspapers existed since 1913; the share with crosswords is unknown | | | census/loc-titles.csv, as above |
| College and school papers | unknown | | | Research so far has only Bard Bulletin, the TASIS Echo and Campus Crosswords (2012 syndicated service); no systematic survey |
| Magazines, in-flight and trade | unknown | | | |
| Puzzle magazines (Dell, Penny Press, Kappa and others) | unknown | | | |
| Books and anthologies | unknown | | | |
| Indie and online (blogs, subscriptions, newsletters) | unknown | | | |
| Apps, minis and midis | unknown | | | |
| UK and Ireland (including cryptics, counted separately) | unknown | | | |
| India and other English-language editions | unknown | | | |
| Non-English | out of scope for now | | | |

## What the catalog knows so far

An entry that gives `crosswords.per_year` and a run adds to the total below,
and an entry with a `corpus` block adds its puzzles to the count of what is
already preserved. This part is rebuilt automatically.

<!-- universe:start -->
| Kind | Entries | With a puzzle count |
|---|---|---|
| newspaper | 53 | 0 |
| magazine | 20 | 0 |
| book | 2 | 0 |
| website | 49 | 0 |
| other | 7 | 0 |

Puzzles in entries that give a run and a yearly count: about 0. This is a floor, not an estimate: it only counts what the catalog knows.

Puzzles already preserved in the xd Crossword Corpus, from 107 of these publications: 129,284 (every series and mini the corpus files under the publication; syndicated features are not included).
<!-- universe:end -->

## How to improve the estimate

- Add entries, and give each a run and a `per_year` where you can source one.
  A well-documented sample of one category (say 30 US dailies) lets us
  extrapolate to the rest, with an honest range.
- Sightings widen a publication's known run. A publication with a sighting but
  no entry is the cheapest kind of fog to clear.
- Prefer counts from a finding aid, an index or a bibliography over our own
  tallies.
- Record cryptics, so they are not lost, but keep them out of the totals above.
