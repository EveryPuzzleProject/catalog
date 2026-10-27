# Syndicates

Who distributed the puzzles. Most crosswords in most newspapers were not the paper's
own: they came from a syndicate, and the copyright line and byline under the grid are
often the only clue to where a puzzle came from. This folder collects what we know
about each outfit that sold or distributed crosswords: its names over time, its
features, its editors, and how its copyright lines read. The aim is to make
archival work easier: when a copyright line says "Bell Syndicate" in 1963, or
"Andrews McMeel" in 2026, an entry here should say what that means.

Each entry is `syndicates/<slug>.md`: YAML front matter (the facts) and free text
(the evidence and what's left to check). A publication's `carries:` list (see the
[catalog README](../README.md)) records which features it printed; these files
record the features themselves.

```yaml
name: Tribune Content Agency          # the outfit's current or last name
kind: syndicate                       # see "Roles" below
names:                                # every name it went by, in order
  - name: Tribune Media Services
    from: 1984
    to: 2013
    source: ...
features:                             # crosswords it distributed
  - feature: The Daily Crossword
    from: 1972
    to: 2000
    editors: Herb Ettenson (1975–1996); Wayne Robert Williams (1999–2000)
    source: census/ep-crossword-features.csv
copyright_lines:                      # exactly as printed, with where it was seen
  - line: "© 1924 The Ball Syndicate"
    seen: gxd latimes/1924/lat1924-11-27.xd
sources:
  - ...
```

Most facts for 1924–2000 come from Editor & Publisher's annual Syndicate Directory,
extracted in [`census/ep-crossword-features.csv`](../census/ep-crossword-features.csv)
(see [its notes](../census/ep-crossword-features.md)). After 2000 there is no such
directory in hand, and the entries rest on press releases, articles and what's
printed in the papers. Say which, and say how sure.

## Roles

A copyright line, a byline and a syndicate credit can name three different
parties. Keeping them apart is most of the work of reading a puzzle's credits.

- **Rights holder**: who owns the puzzle; usually what the copyright line names.
- **Distributor**: who sells it to papers (the syndicate). Often the same as the
  rights holder, not always: Merl Reagle kept the rights to his puzzles and sold them
  himself; Universal Crossword is owned and distributed by Andrews McMeel Universal
  but edited by someone else.
- **Editor or constructor**: what the byline names. Many syndicated dailies carried
  no byline at all ("Staff" in E&P).
- **Host platform**: the software that serves a puzzle online (Amuse Labs' PuzzleMe,
  Arkadium). It never appears in print, but it decides what survives online.
- **Direct to the solver**: subscription services and clubs (AVCX, the Inkubator, the
  Crosswords Club) that skip newspapers entirely.

`kind` in an entry is one of `syndicate` (sells to papers), `self-syndicated` (an
editor or constructor selling their own puzzle to papers), `newspaper` (a paper
selling its own puzzle), `subscription` (direct to solvers), `publisher` (puzzle
magazines and books), `platform`.

The copyright line can lag behind the real owner. In 1963 the LA Times's comics say
"Bell-McClure Syndicate" while the crossword still says "Bell Syndicate"
([los-angeles-times.md](../publications/los-angeles-times.md)). A syndicated copy can
also run weeks after the original (the Boston Globe's Sunday puzzle, 49 days later
in LA Weekly from 2009; Judge's puzzles six to twelve weeks later as "Cross Word
Funnies"), so the date a puzzle was printed can be the syndicated date, not the
original's.

## The landscape over time

A first sketch, from E&P to 2000 and scattered sources after.

- **1924–1930: the craze.** The first directory (October 1924) lists 9 crossword
  features, from Bell, International (Baltimore), King Features, Ledger, McClure,
  Metropolitan, the New York Herald Tribune and New York World syndicates. By 1928
  11 syndicates have crossword series. Bylines are rare; a few names appear (Walter B.
  Gibson for Ledger, Richard H. Tingley for McClure, J. C. Boyd for King).
- **1930s–1960s: the big general syndicates.** The dailies most papers ran came from
  a handful of outfits: King Features (Eugene Sheffer), Central Press (King), AP
  (the Coopers), NEA, United Feature, Bell, the Chicago Tribune–New York News
  Syndicate, the Herald Tribune Syndicate, and from 1949 General Features (Margaret
  Farrar, Maynard Nichols).
- **1960s–1980s: mergers and renames.** Bell merges with McClure (1963). The Herald
  Tribune's puzzle passes to Publishers Newspaper Syndicate when the paper closes.
  The Los Angeles Times Syndicate takes over General Features (1973–74). Newspapers
  start selling their own puzzles: the New York Times from 1972, the Washington Post
  through the LA Times Syndicate in 1975 and its own Writers Group from 1991. NEA
  and United Feature are both United Media by 1980.
- **1980s–2000s: editors on their own.** Merl Reagle self-syndicates his Sunday
  puzzle from about 1988; Stan Newman's American Crossword Federation sells the
  Newsday puzzle (with Creators); Universal Press Syndicate launches the Universal
  Crossword (1997, Timothy Parker). Small puzzle packagers (Singer, Puzzle Features
  Syndicate, Megalo Media) list many titles, which is most of E&P's growth from 35
  features in 1980 to 65 in 2000.
- **2000s–now: consolidation and going direct.** Tribune Media Services becomes
  Tribune Content Agency (2013); Universal Press becomes part of Andrews McMeel
  Universal, which also distributes the USA Today crossword. Wayne Robert Williams
  self-syndicates after Tribune drops his puzzles (2009). Online, platforms
  (Amuse Labs, Arkadium) host papers' puzzles, and subscription services (AVCX,
  the Inkubator) and the puzzle clubs sell straight to solvers.

## Entries

| Entry | Kind | Crosswords |
|---|---|---|
| [Tribune Content Agency](tribune.md) (Chicago Tribune–New York News Syndicate, Tribune Media Services) | syndicate | 1925; 1934–now |
| [King Features Syndicate](king-features.md) (with Central Press, Premier) | syndicate | 1924– (E&P to 2000) |
| [Bell Syndicate / Bell-McClure](bell-mcclure.md) (and McClure) | syndicate | 1924–1971 |
| [AP Newsfeatures](ap-newsfeatures.md) | syndicate | 1930–2000 |
| [United Media](united-media.md) (NEA, United Feature Syndicate) | syndicate | 1928–2000 |
| [New York Herald Tribune Syndicate](herald-tribune.md) (then Publishers) | syndicate | 1924–1970 |
| [Los Angeles Times Syndicate](los-angeles-times-syndicate.md) (and General Features) | syndicate | 1949–2000 |
| [McNaught Syndicate](mcnaught.md) | syndicate | 1975–1990 |
| [New York Times](new-york-times.md) | newspaper | 1972–now |
| [Wall Street Journal](wall-street-journal.md) | newspaper | unknown |
| [Creators Syndicate](creators.md) | syndicate | 1991– (E&P to 2000) |
| [American Crossword Federation](american-crossword-federation.md) (Stan Newman) | self-syndicated | 1990–2000 |
| [Andrews McMeel Universal](andrews-mcmeel.md) (Universal Press Syndicate, Universal Uclick; Universal Crossword, USA Today, The Puzzle Society) | syndicate | 1984–now |
| [Merl Reagle](merl-reagle.md) | self-syndicated | about 1988–2015 |
| [Wayne Robert Williams](wayne-robert-williams.md) | self-syndicated | 2010– |
| [Penny Dell and Three Across](penny-dell.md) (the Crosswords Club, the Uptown Puzzle Club) | publisher | Dell 1921–; Penny 1973– |
| [American Values Club Crossword](avcx.md) (Ben Tausig) | subscription | 2012– (earlier in alt-weeklies) |
| [The Inkubator](inkubator.md) | subscription | 2018– |
| [Platforms](platforms.md) (Amuse Labs, Arkadium) | platform | 2010s– |

## Not written up yet

Outfits in the E&P census without an entry yet (years as listed there): International
Syndicate, Baltimore (1924–1957); Ledger Syndicate (1924–1929, Walter B. Gibson);
Metropolitan Newspaper Service (1924–25); New York World Syndicate (1924); Associated
Newspapers (1926–1957); Copley News Service (1972–2000; it sold Dell's puzzles in the
1970s and 80s and GAMES Magazine's in 1989); Washington Post Writers Group (1991–2000);
Register and Tribune Syndicate (1978–84, Charles Preston); Field Newspaper Syndicate and
News America Syndicate (1982–87, Jeanne Lutwiniak); Puzzle Features Syndicate
(1989–2000, the Mathewses); Megalo Media (1983–2000, J. Baxter Newgate); W. L. Gordon
and Al Smith Feature Service (weekly papers); Community and Suburban Press Service.

Mentioned elsewhere but not yet looked into: CrosSynergy (a team of constructors whose
puzzles ran in the Washington Post, per a book blurb); Campus Crosswords (a service
for college papers, 2012; see [universe.md](../universe.md)).

## Open questions

- After 2000 there is no directory in hand. Did E&P keep publishing its Syndicate
  Directory, and is it scanned?
- Merl Reagle is not in E&P at all, though he syndicated to 50 or more papers. Did
  self-syndicators list themselves? If not, E&P under-counts that whole category.
- For each long-running feature, collect the copyright lines as printed, year by
  year, so a puzzle can be dated and placed by its line alone.

## Where these notes came from

Started 2026-10-27 from Alex DeJarnatt's list of players (put together while working
out where the USA Today crossword comes from, from a conversation with Gemini), checked
against the E&P census and a round of web searches. Claims that come only from that
list and were not checked say so.
