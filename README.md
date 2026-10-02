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
**3 publications so far** (1 lead, 1 harvesting, 1 blitzing).

| Publication | Kind | Where | Crosswords | Scans | Status |
|---|---|---|---|---|---|
| [Judge](publications/judge.md) | magazine | New York | 1924–unknown | [Internet Archive](https://archive.org/details/pub_judge) | blitzing |
| [GAMES](publications/games.md) | magazine | US | 1977–ongoing | [Internet Archive](https://archive.org/details/games_magazine) | harvesting |
| [New York World](publications/new-york-world.md) | newspaper | New York | 1913–1931 · 1 sighting | **Unknown: can you help?** | lead |
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

The table above is rebuilt from these files whenever one changes.
