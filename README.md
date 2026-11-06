# Every Puzzle Project: Catalog

A census of the publications that have printed crosswords: newspapers,
magazines, books and websites, from the first one in 1913 to today. The goal
is every one of them, with what's known about each: when it ran crosswords,
who made them, where copies survive, and how far the project has got with
getting them preserved. The census is nowhere near done, and this page says
how far along it is.

<!-- census:start -->
**131 publications so far** (18 lead, 5 researched, 1 harvesting, 1 blitzing, 106 in the corpus).
<!-- census:end -->

How many should there be? Nobody knows yet, and that number is part of what
the census is for. The floor is large: the Library of Congress newspaper
directory alone lists about 10,300 US daily newspaper titles and 54,000
weeklies that existed at some point since 1913 (see
[the known universe](universe.md) for the count and what it rests on), before
a single magazine, book or website is counted. Which of them printed
crosswords, and when, is the question each entry answers. So the register
below is a start, not a list; what makes it credible is that every entry says
where its facts come from.

The method: an entry is made from evidence, never from a guess. Evidence comes
from three directions, roughly in order of how much it has yielded so far.

1. **The corpus.** The [xd](https://github.com/century-arcade/xdformat)
   Crossword Corpus already holds puzzles from more than a hundred
   publications. Each of those is an entry here, with how many of its puzzles
   the corpus has and from which years, so the catalog's count starts from
   what has actually been preserved. (Seeded by `tools/corpus.py`, from the
   corpus's publication list and file names only.)
2. **Reports.** Someone saw a crossword in a publication on a date. One
   sighting makes an entry; more sightings widen its known run.
3. **Directories and research.** Trade directories (Editor & Publisher's
   Syndicate Directory, Ayer's, the Library of Congress newspaper directory)
   say what existed and who sold puzzles to whom; our own research fills in
   the first runs and the college papers. The directories are the next seed.

## The research

The notes behind the register. These are original work; corrections and
additions are welcome.

- **[The known universe](universe.md)**: how many crosswords have been
  published? The best current guess and its reasons, kept honest: every number
  says what it rests on, or says *unknown*.
- **[The first runs, 1913–1924](first-runs.md)**: every paper known to have
  printed a crossword from the New York World's first (1913-12-21) to the end
  of 1924, paper by paper, keeping "first crossword in paper X" apart from
  "first crossword made by paper X". Most early papers reprinted the World's.
- **[Syndicates](syndicates/)**: who distributed the puzzles. One file per
  syndicate, self-syndicating editor, subscription service or platform, with
  its names over time, features, editors and copyright lines as printed, so a
  puzzle's credits can be read. Starts with an overview of the landscape from
  1924 to now.
- **[Census spine](census/)**: the denominator's raw material. Every US
  newspaper by year from the Library of Congress directory (checked against
  Ayer 1930 and Editor & Publisher), and every crossword feature in Editor &
  Publisher's Syndicate Directory, 1924–2000: 9 features in the first
  directory, 65 by 2000.
- **[College and school papers](research-notes-college.md)**: a first survey
  of student papers and their archives, and which ones are known to have run
  crosswords.
- **[Bylines](bylines/)** and **[people](people/)**: who signed the puzzles,
  publication by publication, with a best guess at each person's gender and
  how the guess was made; and one file per constructor whose byline turns out
  to belong to someone on record. Bylines worth a closer look are in
  [people/leads.md](people/leads.md).
- Smaller notes: [weekly papers and ready-print syndication](research-notes-weekly-syndication.md)
  (who supplied the thousands of small weeklies, and why Editor & Publisher
  doesn't show it), [publication directories as a source](research-notes-directories.md),
  [the Boston Globe's double-puzzle Sundays](research-notes-boston-globe-doubles.md),
  and [leads and access notes](research-notes-leads-2026-10-18.md).

## How to help

- **[Report a puzzle](https://github.com/EveryPuzzleProject/catalog/issues/new?template=report-puzzle.yml).**
  Seen a crossword somewhere? Tell us the publication and the date. A link
  or photo helps, but a paper copy in front of you counts. One puzzle in June
  1994 tells us a publication ran crosswords then, and another in 1996 gives
  us a range.
- **[Report a publication](https://github.com/EveryPuzzleProject/catalog/issues/new?template=report-publication.yml).**
  Know a newspaper, magazine, book or website that ran crosswords and isn't in
  the register? Tell us what you know about it.
- **Fill in a gap.** Every entry marked *Unknown: can you help?* below
  needs someone to find where its pages survive: the Internet Archive,
  Chronicling America, HathiTrust, a library's microfilm. Entries seeded from
  the corpus know their puzzle counts and nothing else: when the crosswords
  began, who edited them, where the printed copies are. Open the entry and use
  the pencil icon to edit it (GitHub turns your edit into a pull request), or
  add what you found to its issue.
- **Research with Claude.** Point your Claude at an entry or an open
  [lead](https://github.com/EveryPuzzleProject/catalog/issues?q=is%3Aopen+label%3Alead)
  and ask it to find out when the publication ran crosswords and where
  scans exist, then open a pull request with what it found.

## The register so far

**Status** follows a publication through the project: *lead* (reported,
needs research), *researched* (we know where copies are), *harvesting*
(scans being found and read), *blitzing* (puzzles being checked, see
[Blitz](https://github.com/EveryPuzzleProject/blitz)), *corpus* (some or all
of its puzzles are in the xd Crossword Corpus, and nobody is working on the
rest), *archived* (its whole known run is in the corpus). **In the corpus**
counts every series the corpus files under the publication, minis included,
and lists the years it has puzzles from.

<!-- catalog:start -->
| Publication | Kind | Where | Crosswords | In the corpus | Scans | Status |
|---|---|---|---|---|---|---|
| [3Across](publications/3across.md) | other | US | 2001–2008 | 163 · 2001–2008 | **Unknown: can you help?** | corpus |
| [Adam Aaronson](publications/adam-aaronson.md) | website | US | 2020–ongoing | 45 | [its own site](https://aaronson.org/crosswords/) | corpus |
| [American Values Club](publications/american-values-club.md) | website | US | 2012–2022 | 514 · 2012–2022 | **Unknown: can you help?** | corpus |
| [Amherst magazine](publications/amherst-magazine.md) | magazine | US | 2025–ongoing | 7 · 2025–2026 | [its own site](https://www.amherst.edu/news/magazine/) | corpus |
| [Andrew Ries](publications/andrew-ries.md) | website | US | 2014–2015 | 65 · 2014–2015 | [its own site](https://www.ariespuzzles.com/) | corpus |
| [Apple News+](publications/apple-news.md) | website | US | 2023–ongoing | 2,366 · 2023–2026 | [its own site](https://apple.news/puzzles) | corpus |
| [arctan(x)words (Christopher Adams)](publications/arctan-x-words.md) | website | US | 2017–ongoing | 198 | [its own site](https://arctanxwords.blogspot.com/) | corpus |
| [Arkadium (games site)](publications/arkadium.md) | website | US | 2018–2026 | 4,532 · 2018–2026 | [its own site](https://www.arkadium.com/) | corpus |
| [Autostraddle](publications/autostraddle.md) | website | US | 2022–2025 | 382 · 2022–2025 | [its own site](https://www.autostraddle.com/category/games/queer-crosswords-and-puzzles/) | corpus |
| [Bawdy Crosswords](publications/bawdy-crosswords.md) | website | US | 2013–2014 | 57 | **Unknown: can you help?** | corpus |
| [Billboard](publications/billboard.md) | magazine | US | 1999–2026 | 487 · 1999–2007, 2025–2026 | [its own site](https://www.billboard.com/p/billboard-crossword/) | corpus |
| [Black Crossword](publications/black-crossword.md) | website | US | 2023–ongoing | 1,348 · 2023–2026 | [its own site](https://www.blackcrossword.com/) | corpus |
| [Brendan Emmett Quigley's puzzles (brendanemmettquigley.com)](publications/brendan-emmett-quigley-s-puzzles.md) | website | US | 2008–2026 | 1,946 · 1910–1933, 2008–2026 | [its own site](https://brendanemmettquigley.com/) | corpus |
| [Brown Alumni Magazine](publications/brown-alumni-magazine.md) | magazine | US | 2020–ongoing | 70 · 2020–2026 | [its own site](https://www.brownalumnimagazine.com/category/crossword) | corpus |
| [BuzzFeed](publications/buzzfeed.md) | website | US | 2015–2016 | 177 · 2015–2016 | [its own site](https://www.buzzfeed.com/) | corpus |
| [Chicago Tribune](publications/chicago-tribune.md) | newspaper | Chicago | 1924–1941 · 4 sightings | 2,345 · 1995–2009 | [Internet Archive](https://archive.org/search?query=identifier%3Aper_chicago-daily-tribune_*), [Newspapers.com](https://www.newspapers.com/) | corpus |
| [Chronicle of Higher Education](publications/chronicle-of-higher-education.md) | magazine | US | 2004–2020 | 650 · 2004–2020 | **Unknown: can you help?** | corpus |
| [CNN](publications/cnn.md) | website | US | 2024–2025 | 84 · 2024–2025 | **Unknown: can you help?** | corpus |
| [Columbia Daily Spectator](publications/columbia-daily-spectator.md) | newspaper | US | 2021–2026 | 681 · 2021–2026 | [its own site](https://www.columbiaspectator.com/multimedia/crosswords/) | corpus |
| [Cornellians](publications/cornellians.md) | magazine | US | 2023–ongoing | 28 | [its own site](https://alumni.cornell.edu/cornellians/) | corpus |
| [Cross-Canada Crosswords](publications/cross-canada-crosswords.md) | book | Canada | 2000–2004 | 184 · 2000–2004 | **Unknown: can you help?** | corpus |
| [Crossroads Media](publications/crossroads-media.md) | other | US | 1997–2007 | 2,199 · 1997–2007 | **Unknown: can you help?** | corpus |
| [Crosstina Aquafina (Kelsey Dixon)](publications/crosstina-aquafina.md) | website | US | 2021–ongoing | 41 · 2021–2026 | [its own site](https://crosstina-aquafina.blogspot.com/) | corpus |
| [Crossword Club](publications/crossword-club.md) | website | US | 2022–ongoing | 1,626 · 2022–2026 | [its own site](https://crosswordclub.com/) | corpus |
| [Crossword Nation (Elizabeth C. Gorski)](publications/crossword-nation.md) | website | US | 2011–2025 | 180 · 2011–2015 | [its own site](https://www.crosswordnation.com/) | corpus |
| [Crosswords Club](publications/crosswords-club.md) | other | US | 1992–1996 | 70 · 1992, 1996 | **Unknown: can you help?** | corpus |
| [Cruciverbalist at Law (Andy Kravis)](publications/cruciverbalist-at-law.md) | website | US | 2013–2019 | 142 | [its own site](https://cruciverbalistatlaw.blogspot.com/) | corpus |
| [Daily Beast](publications/daily-beast.md) | website | US | 2009–ongoing | 1,703 · 2009–2010, 2020–2026 | [its own site](https://www.thedailybeast.com/crossword-puzzles) | corpus |
| [Daily POP Crosswords](publications/daily-pop-crosswords.md) | website | US | 2017–2026 | 3,426 · 2017–2026 | [its own site](https://puzzlenation.com/crosswords) | corpus |
| [David Alfred Bywaters](publications/david-alfred-bywaters.md) | website | US | 2017–ongoing | 367 · 2017–2026 | [its own site](https://www.davidalfredbywaters.com/) | corpus |
| [Defector](publications/defector.md) | website | US | 2023–2026 | 149 · 2023–2026 | [its own site](https://defector.com/category/crosswords) | corpus |
| [Eltana](publications/eltana.md) | other | Seattle | 2011–unknown | 114 | **Unknown: can you help?** | corpus |
| [Fireball Crosswords (Peter Gordon)](publications/fireball-crosswords.md) | website | US | 2010–ongoing | 233 · 2010–2015, 2022 | [its own site](https://www.fireballcrosswords.com/) | corpus |
| [Glutton For Pun](publications/glutton-for-pun.md) | website | US | unknown | 228 | [its own site](https://gluttonforpun.blogspot.com/) | corpus |
| [Grids These Days (Paolo Pasco)](publications/grids-these-days.md) | website | US | 2017–2023 | 94 | [its own site](https://gridsthesedays.blogspot.com/) | corpus |
| [Happy Little Puzzles (Matthew Stock)](publications/happy-little-puzzles.md) | website | US | 2020–2022 | 136 · 2020–2022 | [its own site](https://www.happylittlepuzzles.com/) | corpus |
| [Harvard Magazine](publications/harvard-magazine.md) | magazine | US | 2025–ongoing | 62 · 2025–2026 | [its own site](https://www.harvardmagazine.com/games/mini-crossword) | corpus |
| [I Swear Crossword (Victor Fleming)](publications/i-swear-crossword.md) | website | US | 2005–2016 | 550 · 2006–2008, 2010–2016 | **Unknown: can you help?** | corpus |
| [Ink Well (Ben Tausig)](publications/ink-well.md) | website | US | 2004–2014 | 492 · 2004–2014 | **Unknown: can you help?** | corpus |
| [Inteltainment](publications/inteltainment.md) | website | US | 2020–2026 | 186 · 2020–2026 | [its own site](https://inteltainment.org/) | corpus |
| [Jonesin' Crosswords (Matt Jones)](publications/jonesin-crosswords.md) | website | US | 2009–2016 | 690 · 2002–2016 | **Unknown: can you help?** | corpus |
| [Kansas City Star](publications/kansas-city-star.md) | newspaper | Kansas City | 2003 | 1 · 2003 | **Unknown: can you help?** | corpus |
| [Lansing Star (Lansing, New York)](publications/lansing-star.md) | newspaper | Lansing, New York | 2005–2014 | 369 · 2005–2014 | [its own site](https://web.archive.org/web/20101219051908/http://lansingstar.com/entertainment-archive/6186-puzzles-v6i23) | corpus |
| [Lexicon Devil (Richard D. Allen)](publications/lexicon-devil.md) | website | US | 2020–ongoing | 115 · 2020–2026 | [its own site](https://lexdevil.blogspot.com/) | corpus |
| [Life as a Puzzle (Todd McClary)](publications/life-as-a-puzzle.md) | website | US | 2011–2019 | 78 · 2018 | [its own site](https://tmcaylifeasapuzzle.wordpress.com/) | corpus |
| [Los Angeles Times](publications/los-angeles-times.md) | newspaper | Los Angeles | 1924–ongoing · 12 sightings | 10,661 · 1924, 1996–2026 | [Newspapers.com](https://www.newspapers.com/) | corpus |
| [luckystreak xwords (Ada Nicolle)](publications/luckystreak-xwords.md) | website | US | 2016–ongoing | 116 | [its own site](https://luckyxwords.com/) | corpus |
| [Malaika Handa](publications/malaika-handa.md) | website | US | 2021 | 310 · 2021 | [its own site](https://www.7xwords.com/) | corpus |
| [Matt Gaffney's puzzles (Daily Crossword, Weekly Crossword Contest)](publications/matt-gaffney-s-puzzles.md) | website | US | 2011–2015 | 1,648 · 2008–2015 | [its own site](https://mattgaffneydaily.blogspot.com/) | corpus |
| [Matthew Luter](publications/matthew-luter.md) | website | US | 2021–ongoing | 278 | [its own site](https://matthewluter.com/) | corpus |
| [Modern Maturity](publications/modern-maturity.md) | magazine | US | 1998–2003 | 29 · 1998–2003 | **Unknown: can you help?** | corpus |
| [Monday Fills (Dave Murchie)](publications/monday-fills.md) | website | US | 2012–ongoing | 749 · 2012–2026 | [its own site](https://www.mondayfills.com/) | corpus |
| [Morning Brew](publications/morning-brew.md) | website | US | 2021–ongoing | 742 · 2021–2026 | [its own site](https://www.morningbrew.com/games) | corpus |
| [My Generation](publications/my-generation.md) | magazine | US | 2001–2003 | 10 · 2001–2003 | **Unknown: can you help?** | corpus |
| [New York Herald Tribune](publications/new-york-herald-tribune.md) | newspaper | New York | 1924–1966 | 1 · 1943 | **Unknown: can you help?** | corpus |
| [New York Magazine](publications/new-york-magazine.md) | magazine | US | 2010–2026 | 396 · 2010, 2019–2026 | [its own site](https://nymag.com/games) | corpus |
| [New York Sun](publications/new-york-sun.md) | newspaper | New York | 2002–2009 | 1,746 · 2002–2009 | **Unknown: can you help?** | corpus |
| [New York World](publications/new-york-world.md) | newspaper | New York | 1913–1931 · 1 sighting | 2 · 1913 | [other papers' reprints of the World's Sunday FUN section (a second copy of each puzzle, printed later)](https://www.newspapers.com/) | corpus |
| [Newsday](publications/newsday.md) | newspaper | Long Island, New York | 1998–ongoing | 10,517 · 1998–2026 | [its own site](https://www.newsday.com/games) | corpus |
| [Princeton Alumni Weekly](publications/princeton-alumni-weekly.md) | magazine | US | 2024–ongoing | 26 · 2024–2026 | [its own site](https://paw.princeton.edu/games) | corpus |
| [Puzzazz](publications/puzzazz.md) | other | US | 2009 | 1 · 2009 | **Unknown: can you help?** | corpus |
| [Quarterly Review of Wines](publications/quarterly-review-of-wines.md) | magazine | US | 2004–2011 | 19 | [its own site](http://www.qrw.com/) | corpus |
| [Queerty Crossword](publications/queerty-crossword.md) | website | US | 2024–ongoing | 733 · 2024–2026 | [its own site](https://www.queerty.com/tag/crossword/) | corpus |
| [Rock and Roll Crossword](publications/rock-and-roll-crossword.md) | other | US | 2011–2015 | 233 · 2011–2015 | **Unknown: can you help?** | corpus |
| [Rossword Puzzles (Ross Trudeau)](publications/rossword-puzzles.md) | website | US | 2019–2022 | 153 · 2019–2022 | [its own site](https://rosswordpuzzles.com/) | corpus |
| [Salon](publications/salon.md) | website | US | 1997 | 27 · 1997 | **Unknown: can you help?** | corpus |
| [Simon & Schuster crossword books (The Cross Word Puzzle Book and successors)](publications/simon-schuster-crossword-books.md) | book | US | 1924 | 340 · 1924, 2002–2008, 2011 | [its own site](https://www.crosserville.com/CrossWordPuzzleBook/) | corpus |
| [Slate](publications/slate.md) | website | US | 1999–2026 | 1,623 · 1999–2003, 2024–2026 | [its own site](https://slate.com/life/crossword) | corpus |
| [Student Life (Washington University in St. Louis)](publications/student-life.md) | newspaper | US | 2022–2026 | 330 · 2022–2026 | [its own site](https://www.studlife.com/games) | corpus |
| [The Amherst Student](publications/amherst-student.md) | newspaper | US | 2021–2026 | 114 · 2021–2026 | [its own site](https://amherststudent.com/section/crossword/) | corpus |
| [The Atlantic](publications/atlantic.md) | magazine | US | 2018–2026 | 2,492 · 2018–2026 | [its own site](https://www.theatlantic.com/free-daily-crossword-puzzle/) | corpus |
| [The Boston Globe](publications/boston-globe.md) | newspaper | Boston | 1917–ongoing · 49 sightings | 1,589 · 1917, 1980–1988, 1998–2026 | [Newspapers.com](https://www.newspapers.com/), [Wayback Machine snapshots of the Globe's old crossword pages](https://web.archive.org/web/*/bostonglobe.com/lifestyle/crossword*), [Boston Globe games site (Puzzmo)](https://www.bostonglobe.com/games/crossword) | corpus |
| [The Brown Daily Herald](publications/brown-daily-herald.md) | newspaper | Providence, Rhode Island | unknown–ongoing | 197 · 2010–2011, 2022–2026 | [Brown Digital Repository (Brown University Library)](https://repository.library.brown.edu/) | corpus |
| [The Cavalier Daily (University of Virginia)](publications/cavalier-daily.md) | newspaper | US | 2024–2026 | 448 · 2024–2026 | [its own site](https://www.cavalierdaily.com/section/puzzles) | corpus |
| [The Cornell Daily Sun](publications/cornell-daily-sun.md) | newspaper | US | 2025–2026 | 133 · 2025–2026 | [its own site](https://www.cornellsun.com/section/games) | corpus |
| [The Daily Princetonian](publications/daily-princetonian.md) | newspaper | Princeton, New Jersey | unknown–ongoing | 516 · 2021–2026 | [Dupraz Digital Archives of the Daily Princetonian (Princeton University Library)](http://theprince.princeton.edu/) | corpus |
| [The Daily Tar Heel (UNC)](publications/daily-tar-heel.md) | newspaper | Chapel Hill, North Carolina | 2019–ongoing · 1 sighting | 32 · 2026 | [DigitalNC North Carolina Newspapers (The Tar Heel / Daily Tar Heel)](https://newspapers.digitalnc.org/lccn/sn92073227/) | corpus |
| [The Duke Chronicle](publications/duke-chronicle.md) | newspaper | US | 2023–2026 | 279 · 2023–2026 | [its own site](https://crosshare.org/chroniclecrossword) | corpus |
| [The Michigan Daily](publications/michigan-daily.md) | newspaper | Ann Arbor, Michigan | unknown–ongoing | 693 · 2023–2026 | [Michigan Daily Digital Archives (Bentley Historical Library / U-M Library)](https://digital.bentley.umich.edu/midaily) | corpus |
| [The New York Times](publications/new-york-times.md) | newspaper | New York | 1942–ongoing | 36,861 · 1942–2026 | [its own site](https://www.nytimes.com/crosswords) | corpus |
| [The New Yorker](publications/new-yorker.md) | magazine | US | 2018–2026 | 1,646 · 2018–2026 | [its own site](https://www.newyorker.com/crossword-puzzles-and-games) | corpus |
| [The Onion](publications/onion.md) | newspaper | US | 2006–2012 | 319 · 2006–2012 | **Unknown: can you help?** | corpus |
| [The Philadelphia Inquirer](publications/philadelphia-inquirer.md) | newspaper | Philadelphia | 1997–2015 | 942 · 1997–2015 | **Unknown: can you help?** | corpus |
| [The Rice Thresher (Rice University)](publications/rice-thresher.md) | newspaper | US | 2020–2026 | 128 · 2020–2026 | [its own site](https://www.ricethresher.org/section/crosswords) | corpus |
| [The Stranger (Seattle)](publications/stranger.md) | newspaper | Seattle | 2007–2010 | 140 · 2007–2010 | [its own site](https://www.thestranger.com/) | corpus |
| [The Tufts Daily](publications/tufts-daily.md) | newspaper | US | 2024–2026 | 188 · 2024–2026 | [its own site](https://www.tuftsdaily.com/section/crossword) | corpus |
| [The Varsity (University of Toronto)](publications/varsity.md) | newspaper | Toronto | 2023–2026 | 50 · 2023–2026 | [its own site](https://thevarsity.ca/category/crosswords/) | corpus |
| [The Villanovan (Villanova University)](publications/villanovan.md) | newspaper | US | 2024–2025 | 39 · 2024–2025 | [its own site](https://villanovan.com/category/crossword/) | corpus |
| [The Walrus](publications/walrus.md) | magazine | Toronto | 2024–ongoing | 139 · 2024–2026 | [its own site](https://thewalrus.ca/games/crossword/) | corpus |
| [The Washington Post](publications/washington-post.md) | newspaper | Washington, D.C. | 1971–ongoing | 1,946 · 1924, 1996–2008, 2010–2026 | **Unknown: can you help?** | corpus |
| [The Week](publications/week.md) | magazine | US | 2013–2015 | 103 · 2013–2015 | [its own site](https://theweek.com/puzzles) | corpus |
| [These Puzzles Fund Abortion](publications/these-puzzles-fund-abortion.md) | website | US | 2021–ongoing | 16 | [its own site](https://www.abortionpuzzles.com) | corpus |
| [Tim Croce](publications/tim-croce.md) | website | US | 2014–2026 | 1,188 · 2014–2026 | [its own site](https://club72.wordpress.com/) | corpus |
| [Time Magazine](publications/time-magazine.md) | magazine | US | 2000–2001 | 54 · 2000–2001 | **Unknown: can you help?** | corpus |
| [UNH Magazine](publications/unh-magazine.md) | magazine | US | 2003–2022 | 24 · 2003, 2014–2022 | [its own site](https://magazine.unh.edu/) | corpus |
| [unshelved](publications/unshelved.md) | website | US | unknown | 2 | **Unknown: can you help?** | corpus |
| [Uptown Puzzle Club](publications/uptown-puzzle-club.md) | other | US | unknown | 25 | **Unknown: can you help?** | corpus |
| [USA Today](publications/usa-today.md) | newspaper | US | 1986–ongoing | 9,591 · 1995–2026 | [its own site](https://play.usatoday.com/crossword) | corpus |
| [Vox](publications/vox.md) | website | US | 2019–ongoing | 2,138 · 2019–2026 | [its own site](https://www.vox.com/crossword) | corpus |
| [Vulture](publications/vulture.md) | website | US | 2022–ongoing | 1,242 · 2014, 2022–2026 | [its own site](https://www.vulture.com/tags/vulture-10x10/) | corpus |
| [Wall Street Journal](publications/wall-street-journal.md) | newspaper | US | 1998–ongoing | 4,509 · 1998–2026 | [its own site](https://www.wsj.com/news/puzzle) | corpus |
| [Washington Examiner](publications/washington-examiner.md) | magazine | US | 2019–2024 | 226 · 2019–2024 | [its own site](https://www.washingtonexaminer.com/section/magazine-crossword-puzzle/) | corpus |
| [Will Nediger](publications/will-nediger.md) | website | US | 2016–ongoing | 247 | [its own site](https://blog.bewilderinglypuzzles.com/) | corpus |
| [Women of Letters](publications/women-of-letters.md) | website | US | 2018 | 18 | [its own site](https://www.pattivarol.com/women-of-letters) | corpus |
| [Yahoo (games site)](publications/yahoo.md) | website | US | 2026 | 188 · 2026 | [its own site](https://www.yahoo.com/) | corpus |
| [Yale Public Humanities](publications/yale-public-humanities.md) | website | US | 2021–ongoing | 21 · 2021–2026 | [its own site](https://publichumanitiespuzzles.github.io/) | corpus |
| [Judge](publications/judge.md) | magazine | New York | 1924–1925 · 3 sightings | 531 · 1924–1939 | [Internet Archive](https://archive.org/details/pub_judge), [newspapers carrying "Cross Word Funnies, selected by Judge" (copyright 1925)](https://www.newspapers.com/) | blitzing |
| [GAMES](publications/games.md) | magazine | US | 1977–ongoing |  | [Internet Archive](https://archive.org/details/games_magazine) | harvesting |
| [Newport Mercury](publications/newport-mercury.md) | newspaper | Newport, Rhode Island | 1925–1926 · 9 sightings |  | [Newspapers.com Northeast Collection (library edition, via Newport Public Library)](http://newspaperslibrary.proquest.com/) | researched |
| [The Daily Collegian (Penn State)](publications/daily-collegian-penn-state.md) | newspaper | State College, Pennsylvania | 1976–1981 · 4 sightings |  | [Historical Digital Collegian Archive (Penn State University Libraries)](https://libraries.psu.edu/databases/psu00795) | researched |
| [The Daily Pennsylvanian](publications/daily-pennsylvanian.md) | newspaper | Philadelphia | unknown–ongoing |  | [Daily Pennsylvanian archives (University of Pennsylvania Libraries)](https://dparchives.library.upenn.edu/) | researched |
| [The Stanford Daily](publications/stanford-daily.md) | newspaper | Stanford, California | 1935–ongoing |  | [Stanford Daily Archives (run by The Daily)](https://archives.stanforddaily.com/) | researched |
| [The Tech (MIT)](publications/the-tech-mit.md) | newspaper | Cambridge, Massachusetts | unknown–ongoing |  | [The Tech website, historical issues](https://thetech.com/issues), [Internet Archive (MIT The Tech collection)](https://archive.org/details/mit_the_tech) | researched |
| [Bard Bulletin (probably Bard High School Early College)](publications/bard-bulletin.md) | newspaper | New York | unknown |  | **Unknown: can you help?** | lead |
| [Buffalo Courier](publications/buffalo-courier.md) | newspaper | Buffalo, New York | 1920–1925 · 2 sightings |  | [Newspapers.com (filed under "Buffalo Courier Express", the name after the 1926 merger with the Buffalo Express)](https://www.newspapers.com/) | lead |
| [Daily Bruin (UCLA)](publications/daily-bruin.md) | newspaper | Los Angeles | 2000 · 1 sighting |  | **Unknown: can you help?** | lead |
| [Detroit Free Press](publications/detroit-free-press.md) | newspaper | Detroit, Michigan | 1919–1920 · 1 sighting |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [Los Angeles Daily News (1923–1954)](publications/los-angeles-daily-news-1923.md) | newspaper | Los Angeles | 1941 · 1 sighting |  | **Unknown: can you help?** | lead |
| [Los Angeles Sunday Tribune](publications/los-angeles-sunday-tribune.md) | newspaper | Los Angeles, California | 1916–1917 · 3 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [New Orleans States](publications/new-orleans-states.md) | newspaper | New Orleans, Louisiana | 1917 · 2 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [Omaha Daily News](publications/omaha-daily-news.md) | newspaper | Omaha, Nebraska | 1920 · 1 sighting |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [Orange and White (University of Tennessee; now The Daily Beacon)](publications/orange-and-white-tennessee.md) | newspaper | Knoxville, Tennessee | 1925–unknown |  | [UT Libraries Digital Collections (Daily Beacon / Orange and White issues)](https://volopedia.lib.utk.edu/entries/daily-beacon) | lead |
| [Salt Lake Telegram](publications/salt-lake-telegram.md) | newspaper | Salt Lake City, Utah | 1917 · 2 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [The Daily Northwestern](publications/daily-northwestern.md) | newspaper | Evanston, Illinois | 2024–ongoing |  | **Unknown: can you help?** | lead |
| [The Minneapolis Journal](publications/minneapolis-journal.md) | newspaper | Minneapolis, Minnesota | 1914–1920 · 8 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [The Pittsburgh Press](publications/pittsburgh-press.md) | newspaper | Pittsburgh, Pennsylvania | 1916–1920 · 5 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [The Red & Black (University of Georgia)](publications/red-and-black-georgia.md) | newspaper | Athens, Georgia | 2019–ongoing · 1 sighting |  | **Unknown: can you help?** | lead |
| [The Shreveport Times](publications/shreveport-times.md) | newspaper | Shreveport, Louisiana | 1916–1917 · 3 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [The Tacoma Daily Ledger](publications/tacoma-daily-ledger.md) | newspaper | Tacoma, Washington | 1916–1917 · 7 sightings |  | [Newspapers.com](https://www.newspapers.com/) | lead |
| [The TASIS Echo (TASIS The American School in England)](publications/tasis-echo.md) | newspaper | England | 2000–2002 |  | **Unknown: can you help?** | lead |
| [The Ubyssey (University of British Columbia)](publications/the-ubyssey.md) | newspaper | Vancouver | 2025–ongoing · 1 sighting |  | **Unknown: can you help?** | lead |
<!-- catalog:end -->

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
corpus:                     # what the xd Crossword Corpus holds; kept by tools/corpus.py
  id: latimes               # the corpus directory
  puzzles: 10661
  years: "1924, 1996–2026"
  as_of: 2026-11-06
```

The table above and the counts in [universe.md](universe.md) are rebuilt from
these files whenever one changes (`python tools/build.py`). The `corpus`
blocks are refreshed from a checkout of the corpus with
`python tools/corpus.py <checkout>`; only names, counts and years are read,
never puzzle content.
