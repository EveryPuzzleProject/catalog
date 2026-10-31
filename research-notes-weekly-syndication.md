# Weekly papers and ready-print syndication (first pass, 2026-10-18)

Question: who supplied crosswords to the thousands of small weeklies, and why
doesn't the E&P Syndicate Directory show it?

## What started it

The Newport Mercury, a Rhode Island weekly, ran a numbered crossword series
credited to the Western Newspaper Union from 1925-01-10 to 1926-03-13 (see
[publications/newport-mercury.md](publications/newport-mercury.md)). Found by
Alex DeJarnatt in the Newspapers.com Northeast Collection (library edition),
2026-10-18.

## Confirmed

- **WNU is missing from the E&P extraction.** `census/ep-crossword-features.csv`
  (678 rows, 1924–2000) has no row mentioning Western Newspaper Union, under
  any spelling (checked 2026-10-18).
- **What WNU sold.** WNU's "ready-print" (or "Printed Service") was a
  preprinted half of a paper: four pages printed by WNU and shipped to a
  weekly, which printed its own news on the other four. An E&P item reprinted
  on Stripper's Guide says WNU still served 4,500 newspapers in 1923, had at
  one time printed four pages weekly for about 7,000, and ended Printed
  Service on 1952-03-29; at the end 1,412 weeklies used it
  (https://comicstriphistory.com/2007/11/news-of-yore-end-of-an-era-for-wnu.html).
- Wikipedia's "Patent insides" says WNU, the largest of five such companies,
  supplied more than 14,000 clients in the mid-1920s
  (https://en.wikipedia.org/wiki/Patent_insides). That disagrees with the
  4,500 figure; it may count clients of other services (plates, mats) too.
  Treat the size as unsettled until checked against E&P or a WNU source.

## Why it matters

- **Scale.** The LoC census (`census/`) estimates about 14,000 weeklies in
  1925 against about 2,900 dailies. If WNU's crossword was part of the
  ready-print pages, it may have been the most widely printed crossword of
  the craze, almost entirely outside the dailies most research looks at.
- **E&P's blind spot.** The Syndicate Directory lists features sold to
  papers; ready-print was a printing service sold to weeklies. Other
  ready-print and plate houses (Wikipedia names five companies in the 1890s)
  may be missing from the extraction for the same reason.
- **Matching is easy.** Ready-print pages came preprinted, so carrying papers
  may share the identical page, not just the puzzle, with a small lag.
- **Numbered series are clocks.** In the Mercury, Nos. 1–7 ran weekly and
  then the paper skipped at least six weeks. Whether WNU or the paper caused
  the gap needs a second carrying paper.

## Not confirmed

- That the WNU crossword was part of the ready-print sheets, rather than a
  plate or mat feature sold separately.
- How many puzzles WNU issued, and when the series started and ended. The
  Mercury's run (Jan 1925 – Mar 1926) is one paper's; "(copyright 1924)" on
  Nos. 1 and 5 says the series began in 1924.
- Whether the Mercury's switch to unnumbered puzzles (after No. 12) was WNU's
  change or the paper's.

## Next steps

1. Search Chronicling America (from a browser: loc.gov was blocked or timed
   out from the agent sandbox) for the titles "Stepping Stones" and "The Merry
   Go Round" near "cross-word", 1924–1926, and for "cross-word puzzle no"
   with "western newspaper union". Each hit is a carrier and a date.
2. Look for WNU in the E&P magazine itself (archive.org `pub_editor-publisher`
   full-text search, 1924–1926) for announcements of a crossword service.
3. Find a WNU catalog or price list. Stripper's Guide has written about WNU
   and reprints Elmo Scott Watson's *History of Newspaper Syndicates*
   (https://comicstriphistory.com/2016/07/history-of-newspaper-syndicates-by-elmo_22.html);
   not yet read for crossword mentions.
4. Add a `kind: other` or syndicate-level entry for the WNU series once a
   second carrying paper is found.

## Method notes from the Mercury search

- Full-text search found most puzzles but missed 1926-03-13, which was
  found by browsing. A missing hit is not a missing puzzle.
- Search terms that worked: "cross-word puzzle no." (numbered period),
  "western newspaper union", and "horizontal" + "vertical" + "solution" for
  unnumbered puzzles. Distinctive puzzle titles survive OCR better than grids.
- WNU's credit also appears on non-puzzle ready-print material (fiction,
  features), so a WNU hit must be opened to confirm it is a puzzle.
