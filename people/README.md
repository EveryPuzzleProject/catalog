# People

Who made the puzzles. Most early crosswords were sent in by readers, and their bylines
are often all we know about them, but now and then a byline turns out to belong to
someone with a life on record. This folder collects what we find, one file per person,
so it can grow into biographies.

Each entry is `people/<slug>.md`: YAML front matter (the facts) and free text (the
evidence and what's left to check).

```yaml
name: Ottokar Čadek              # the person, as history knows them
lived: 1897–1956
known_for: violinist, New York String Quartet
identification: confirmed        # confirmed | likely | plausible
bylines:                         # exactly as printed
  - byline: Mr. and Mrs. Ottokar T. Cadek
    publication: The Cross Word Puzzle Book, Third Series (Simon and Schuster, 1924)
    puzzles: [ssb-134, ssb-141]  # gxd ids where they exist
sources:
  - https://...
```

**Identification** is about whether the byline is this person, not about the facts of
their life:

- **confirmed**: the publication itself says so, or a record ties the person to the
  puzzle (an address, a credit, a letter).
- **likely**: a rare name, plus the right place and time, plus a link to puzzles or
  to what the puzzle says about its maker.
- **plausible**: the right place and time, but nothing ties them to puzzles yet. A
  name match alone doesn't get an entry; it goes in [leads.md](leads.md).

Bylines stay as printed, misprints included; an entry can list several spellings of one
person. Write about these people as people: what they did, with sources, and say plainly
what isn't known.
