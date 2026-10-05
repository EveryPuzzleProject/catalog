# Every Puzzle Project: Catalog

**Help us complete this catalog!**

We're mapping every publication that has ever printed a crossword:
newspapers, magazines, books and websites, from the first one in 1913 to
today. Nobody knows how many there have been. The catalog records what's
known about each one: when it ran crosswords, where copies survive, and how
far the project has got with it.

## How to help

- **[Report a puzzle](https://github.com/EveryPuzzleProject/catalog/issues/new?template=report-puzzle.yml).**
  Seen a crossword somewhere? Tell us the publication and the date. A link
  or photo helps, but a paper copy in front of you counts. Every report
  helps map the known universe: one puzzle in June 1994 tells us a
  publication ran crosswords then, and another in 1996 gives us a range.
- **[Report a publication](https://github.com/EveryPuzzleProject/catalog/issues/new?template=report-publication.yml).**
  Know a newspaper, magazine, book or website that ran crosswords? Tell us
  what you know about it.
- **Fill in a gap.** Every entry marked *Unknown: can you help?* below
  needs someone to find where its pages survive: the Internet Archive,
  Chronicling America, HathiTrust, a library's microfilm. Open the entry and
  use the pencil icon to edit it (GitHub turns your edit into a pull
  request), or add what you found to its issue.
- **Research with Claude.** Point your Claude at an entry or an open
  [lead](https://github.com/EveryPuzzleProject/catalog/issues?q=is%3Aopen+label%3Alead)
  and ask it to find out when the publication ran crosswords and where
  scans exist, then open a pull request with what it found.

## The catalog

<!-- catalog:start -->
**22 publications so far** (14 lead, 6 researched, 1 harvesting, 1 blitzing).

| Publication | Kind | Where | Crosswords | Scans | Status |
|---|---|---|---|---|---|
| [Judge](publications/judge.md) | magazine | New York | 1924–unknown | [Internet Archive](https://archive.org/details/pub_judge) | blitzing |
| [GAMES](publications/games.md) | magazine | US | 1977–ongoing | [Internet Archive](https://archive.org/details/games_magazine) | harvesting |
| [The Boston Globe](publications/boston-globe.md) | newspaper | Boston | 1917–ongoing · 10 sightings | [Newspapers.com](https://www.newspapers.com/), gxd (Saul Pwanson's crossword corpus, private), [Wayback Machine snapshots of the Globe's old crossword pages](https://web.archive.org/web/*/bostonglobe.com/lifestyle/crossword*), [Boston Globe games site (Puzzmo)](https://www.bostonglobe.com/games/crossword) | researched |
| [The Daily Collegian (Penn State)](publications/daily-collegian-penn-state.md) | newspaper | State College, Pennsylvania | 1976–1981 · 4 sightings | [Historical Digital Collegian Archive (Penn State University Libraries)](https://libraries.psu.edu/databases/psu00795) | researched |
| [The Daily Pennsylvanian](publications/daily-pennsylvanian.md) | newspaper | Philadelphia | unknown–ongoing | [Daily Pennsylvanian archives (University of Pennsylvania Libraries)](https://dparchives.library.upenn.edu/) | researched |
| [The Daily Princetonian](publications/daily-princetonian.md) | newspaper | Princeton, New Jersey | unknown–ongoing | [Dupraz Digital Archives of the Daily Princetonian (Princeton University Library)](http://theprince.princeton.edu/) | researched |
| [The Stanford Daily](publications/stanford-daily.md) | newspaper | Stanford, California | 1935–ongoing | [Stanford Daily Archives (run by The Daily)](https://archives.stanforddaily.com/) | researched |
| [The Tech (MIT)](publications/the-tech-mit.md) | newspaper | Cambridge, Massachusetts | unknown–ongoing | [The Tech website, historical issues](https://thetech.com/issues), [Internet Archive (MIT The Tech collection)](https://archive.org/details/mit_the_tech) | researched |
| [Bard Bulletin (probably Bard High School Early College)](publications/bard-bulletin.md) | newspaper | New York | unknown | **Unknown: can you help?** | lead |
| [Daily Bruin (UCLA)](publications/daily-bruin.md) | newspaper | Los Angeles | 2000 · 1 sighting | **Unknown: can you help?** | lead |
| [Los Angeles Daily News (1923–1954)](publications/los-angeles-daily-news-1923.md) | newspaper | Los Angeles | 1941 · 1 sighting | **Unknown: can you help?** | lead |
| [Los Angeles Times](publications/los-angeles-times.md) | newspaper | Los Angeles | 1924–ongoing · 12 sightings | [Newspapers.com](https://www.newspapers.com/) | lead |
| [New York World](publications/new-york-world.md) | newspaper | New York | 1913–1931 · 1 sighting | **Unknown: can you help?** | lead |
| [Orange and White (University of Tennessee; now The Daily Beacon)](publications/orange-and-white-tennessee.md) | newspaper | Knoxville, Tennessee | 1925–unknown | [UT Libraries Digital Collections (Daily Beacon / Orange and White issues)](https://volopedia.lib.utk.edu/entries/daily-beacon) | lead |
| [The Brown Daily Herald](publications/brown-daily-herald.md) | newspaper | Providence, Rhode Island | unknown–ongoing | [Brown Digital Repository (Brown University Library)](https://repository.library.brown.edu/) | lead |
| [The Daily Northwestern](publications/daily-northwestern.md) | newspaper | Evanston, Illinois | 2024–ongoing | **Unknown: can you help?** | lead |
| [The Daily Tar Heel (UNC)](publications/daily-tar-heel.md) | newspaper | Chapel Hill, North Carolina | 2019–ongoing · 1 sighting | [DigitalNC North Carolina Newspapers (The Tar Heel / Daily Tar Heel)](https://newspapers.digitalnc.org/lccn/sn92073227/) | lead |
| [The Michigan Daily](publications/michigan-daily.md) | newspaper | Ann Arbor, Michigan | unknown–ongoing | [Michigan Daily Digital Archives (Bentley Historical Library / U-M Library)](https://digital.bentley.umich.edu/midaily) | lead |
| [The Red & Black (University of Georgia)](publications/red-and-black-georgia.md) | newspaper | Athens, Georgia | 2019–ongoing · 1 sighting | **Unknown: can you help?** | lead |
| [The TASIS Echo (TASIS The American School in England)](publications/tasis-echo.md) | newspaper | England | 2000–2002 | **Unknown: can you help?** | lead |
| [The Ubyssey (University of British Columbia)](publications/the-ubyssey.md) | newspaper | Vancouver | 2025–ongoing · 1 sighting | **Unknown: can you help?** | lead |
| [The Washington Post](publications/washington-post.md) | newspaper | Washington, D.C. | 1971–ongoing | **Unknown: can you help?** | lead |
<!-- catalog:end -->

**Status** follows a publication through the project: *lead* (reported,
needs research), *researched* (we know where copies are), *harvesting*
(scans being found and read), *blitzing* (puzzles being checked, see
[Blitz](https://github.com/EveryPuzzleProject/blitz)), *archived*.

## How an entry works

Each publication is one file in [`publications/`](publications/): the facts
at the top, between `---` lines, and free notes below. For example (made up):

```yaml
---
name: Wine Spectator
kind: magazine            # newspaper, magazine, book, website, other
country: US
place: New York           # optional
crosswords:               # what's known about its run, if anything
  first: 1994
  last: unknown
  frequency: monthly
  answers: in the next issue
sources:                  # where copies survive
  - where: Internet Archive
    url: https://archive.org/details/...
    covers: 1990–1999
    access: free          # free, subscription, library, unknown
sightings:                # individual puzzles people have reported
  - date: 1994-06-18
    puzzle: by so-and-so
    seen: paper copy
    report: https://github.com/EveryPuzzleProject/catalog/issues/1
status: lead
---

Notes, open questions, anything else.
```

Optional fields, each entry with a `source` (a URL or a citation with page or
date) so a claim can be checked:

```yaml
crosswords:
  per_year: 52              # distinct puzzles a year, roughly; feeds universe.md
  editors:                  # or plain text
    - name: Margaret Farrar
      from: 1942
      to: 1968
      source: https://...
carries:                    # syndicated series this publication printed
  - feature: Universal Crossword
    from: 1997
    to: 2019
    source: https://...
```

How big is the whole thing? See [the known universe](universe.md).

The table above is rebuilt from these files whenever one changes.
