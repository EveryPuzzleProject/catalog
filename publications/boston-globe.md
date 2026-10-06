---
name: The Boston Globe
kind: newspaper
country: US
place: Boston
crosswords:
  first: 1917-02-25
  last: ongoing
  frequency: "Sunday from 1917; Saturday added 1923-05-26; Wednesday added 1924-02-06; daily (Mon–Fri) from 1924-10-06, alongside separate Saturday and Sunday series; still daily in December 1935, labeled \"The Globe Cross-Word Puzzle\" with no sign of syndication. In 1924 Saturday ran two puzzles a week, \"Crossword Puzzles for the Grown-Ups\" and \"Crossword Puzzle for Boys and Girls\", for a year or two. From late November 1924 the Saturday puzzle (still headed \"The Globe's Saturday Cross Word Puzzle\") joins the daily's schedule: there is one Saturday puzzle, its solution is printed the next Monday and again the next Saturday, and the Saturday paper also prints Friday's daily solution (1924-11-22's puzzle answered on 1924-11-24 and 1924-11-29; 1924-11-29's on 1924-12-01). Before that, Monday 1924-11-10 prints Friday's solution and 1924-11-17 none. The heading \"The Globe's Saturday Cross Word Puzzle\" last appears on 1924-12-13; from 1924-12-20 the Saturday puzzles are headed by audience (\"for grownups\", \"for boys and girls\", \"for the more expert\"), never \"Saturday\". From 1924-12-13 (\"Two Cross Word Puzzles Today\") Saturday has two puzzles again: a large one for grown-ups (17x17 to 21x21, sometimes a special: an irregular \"Real Brain Twister\" on 1925-01-03, literary allusions on 1925-01-10, a heart-shaped Valentine's puzzle by \"Yebo of Dorchester\" on 1925-02-14, a March lion on 1925-02-28) and one for boys and girls (13x13 or 15x15). For three Saturdays, 1925-02-14 to 1925-02-28, the second slot is instead \"Cross Word Funnies, selected by Judge\", copyright 1925, apparently syndicated from Judge magazine; the boys and girls puzzle is back on 1925-03-07. The pair ends 1925-04-04, the last \"for the grownups\" and \"boys and girls\" headings found by text search; after that the puzzle is plain \"Cross-Word Puzzle\". By 1936 Saturday's puzzle is answered on Monday (\"Solution next Monday\"). Still daily in 1970, with no attribution or copyright line, so whether it was still made in-house is unknown. Later the Sunday puzzle moved into the Globe Magazine"
  answers: "daily series: the next day (Friday's on Monday while Saturday was separate; Saturday's on Monday from 1924-11-24, and again the next Saturday for a while; Friday's on Saturday from 1924-11-29); Wednesday series: the next Wednesday; Saturday series: the next Saturday (January 1924 to at least 1924-12-06); Sunday series: probably the following week (to confirm)"
  constructors: "Sunday constructors include Jordan S. Lasher (1980s), Emily Cox and Henry Rathvon, Henry Hook (alternating weekly with Cox and Rathvon through 2015; last seen 2015-05-31; died 2015, editor's note in the 2015-11-01 Globe), Elizabeth C. Gorski (2008-08-10 to 2008-11-16, alternating with Hook while Cox and Rathvon were away), Brendan Emmett Quigley (from 2015-06-14, alternating with Cox and Rathvon) and Joon Pahk (from at least 2022-04-17, alternating with Quigley; Cox and Rathvon last seen 2022-05-01) (Newspapers.com print checks; gxd bostonglobe/; Wayback snapshots; Globe help center)"
  syndication: "the Sunday puzzle was syndicated, at least 2003–2015, to LA Weekly and others, running weeks after the Globe (0 to 56 days; 49 from 2009), with some holiday puzzles held a year. gxd's 2003–2015 files were dated by that syndicated run until corrected (see sources)"
carries:
  - feature: Universal Crossword (Universal Press Syndicate, later Andrews McMeel Syndication), as the online weekday "Globe crossword"
    from: 2015-02
    to: 2024-02
    source: "Wayback Machine snapshots of bostonglobe.com/lifestyle/crossword (2015–2020) and bostonglobe.com/games-comics/crossword/ (2019–2024); bylines read 2026-10-05. Start is the earliest snapshot checked, not a known start"
sources:
  - where: Newspapers.com
    url: https://www.newspapers.com/
    covers: "puzzle pages 1917–1936 checked; Sunday issues are missing from 1925 to June 1943 (they return July 1943), an archive gap (Alex DeJarnatt, 2026-10-05), so Sunday puzzles in that span need another source"
    access: subscription
  - where: gxd (Saul Pwanson's crossword corpus, private)
    covers: "786 puzzles, nearly all Sundays: one from 1917, 1980–1988 (sparse), 1998–2015 (2003-01 to 2015-10 complete except 9 Sundays). The 2003–2015 files were dated by a syndicated run (181 built from LA Weekly .puz files), 0 to 56 days after the Globe, 49 from March 2009, with some holiday puzzles a year late; checked Sunday by Sunday against print for 2003–2009 and by spot checks after (Alex DeJarnatt, Newspapers.com, 2026-10-05). Fix pending as gxd branch fix-bostonglobe-dates: re-dates 661 files, drops 3 syndication reruns of 2002 puzzles, corrects titles and bylines, adds bg2004-12-19a and bg2016-02-14a. Pre-2003 dates spot-checked and correct. Missing Sundays and 3 files with no solution listed in xword-ocr harvests/bostonglobe/missing-for-blitz.md"
    access: unknown
  - where: Wayback Machine snapshots of the Globe's old crossword pages
    url: https://web.archive.org/web/*/bostonglobe.com/lifestyle/crossword*
    covers: "287 Sundays recovered with answers, 272 of the 425 from 2016-01-03 to 2024-02-18 (epp globe-wayback, 2026-10-05); about 300 Sundays 2015–2024 have a snapshot (bostonglobe.com/lifestyle/crossword 2012–2020; bostonglobe.com/games-comics/crossword/ 2019–2024); each shows that day's puzzle with answers"
    access: free
  - where: Boston Globe games site (Puzzmo)
    url: https://www.bostonglobe.com/games/crossword
    covers: "2024-02-23 to now: 954 puzzles by 2026-10-05, weekdays mostly Universal (Andrews McMeel) but with the Globe's own quarterly Themeless Weeks (Mon–Sat, independent constructors, from 2024-06-24; about 36 puzzles) and a Themeless Friday (2026-06-19), 135 Sundays by Joon Pahk and Brendan Emmett Quigley alternating; no puzzle listed 2024-08-18 or 2024-09-22. Index: api.puzzmo.com/team/v1/boston-globe-amlaj/queues/crossword/puzzles?startDate=YYYY-MM-DD&days=N (id, name, publishDate, authors); content as xd: api.puzzmo.com/graphql, { puzzle(id: ...) { id name puzzle } } (both from Orta at Puzzmo, 2026-10-05)"
    access: free
sightings:
  - date: 1917-02-25
    puzzle: '"Cross-Word Puzzle", the first Globe crossword; a Sunday series follows'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05; also gxd bostonglobe/1917/bg1917-02-25.xd
  - date: 1917-08-19
    puzzle: Sunday crossword, replayed with full answers by the Globe in 2022
    seen: https://www.bostonglobe.com/2022/03/03/magazine/play-this-boston-globe-crossword-puzzle-1917/
  - date: 1923-05-26
    puzzle: 'the first Saturday puzzle: no previous solution, and a front-page "Solve the puzzle on page 3"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1923-12-09
    puzzle: 'Sunday crossword still running, with the note "A Crossword Puzzle Appears in the Globe Every Saturday"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1924-01
    puzzle: 'Saturday puzzle still its own series, printing last Saturday''s answers'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1924
    puzzle: 'two Saturday puzzles each week, "Crossword Puzzles for the Grown-Ups" and "Crossword Puzzle for Boys and Girls"'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1924-02-06
    puzzle: the first Wednesday puzzle
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1924-10-06
    puzzle: 'the first daily puzzle (Monday), "solution tomorrow"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1924-10-08
    puzzle: 'daily puzzle, with both "yesterday''s" solution and last Wednesday''s, so the Wednesday series ended 1924-10-01'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1924-11-03
    puzzle: 'Monday puzzle, with "solution to last Friday''s puzzle"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 1924-11-10
    puzzle: 'Monday puzzle printing Friday''s solution: Saturday still separate'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1924-11-17
    puzzle: 'Monday puzzle printing no solution at all'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1924-11-22
    puzzle: 'Saturday puzzle, 1-Across "Separate" (DIFFERENT); the paper prints only last Saturday''s solution. Its own solution runs on 1924-11-24 and again on 1924-11-29'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1924-11-24
    puzzle: 'Monday puzzle with "Solution of last Saturday''s puzzle" (also 1924-12-01)'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1924-12-13
    puzzle: '"Two Cross Word Puzzles Today": "How to Solve a Cross Word Puzzle" with a 15x15 "Boys'' and Girls'' Puzzle", beside "The Globe''s Saturday Cross Word Puzzle" (19x19)'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1924-12-20
    puzzle: '"Cross-Word Puzzle for Boys and Girls" (13x13) beside "Cross-Word Puzzle for Grownups" (17x17); same pairing 1924-12-27 (15x15 and 21x21) and 1925-01-17 to 1925-02-07'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1925-01-03
    puzzle: '"A Real Brain Twister for Cross-Word Puzzle Experts", an irregular shape, with "Cross-Word Puzzle for the Youngsters" (15x15)'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1925-01-10
    puzzle: '"Cross-Word Puzzle for Boys and Girls" beside "Literary Allusions Feature This Puzzle"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1925-02-14
    puzzle: '"Valentine''s Day Puzzle for Those Who Don''t Like ''Em Easy", a giant heart-shaped grid with hearts in it, by "Yebo of Dorchester", above "Cross Word Funnies, selected by Judge", copyright 1925'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1925-03-07
    puzzle: '"Crossword for the Boys and Girls" back, after three weeks of Judge''s Cross Word Funnies'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 1925-04-04
    puzzle: 'last "Cross-Word Puzzle for the Grownups" and last "Boys and Girls" puzzle found by text search; afterwards plain "Cross-Word Puzzle"'
    seen: Newspapers.com search, by Alex DeJarnatt, 2026-10-06
  - date: 1925-02-21
    puzzle: '"Cross-Word Puzzle for the More Expert" above "Cross Word Funnies, selected by Judge", copyright 1925; 1925-02-28 the big puzzle is a March puzzle ("Here''s the March puzzle lion: will he come in tomorrow?"), again with Judge''s'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1924-11-29
    puzzle: '"The Globe''s Saturday Cross Word Puzzle" by S. E. Hale, Boston (2-Across "The points of a pen", NIB), with both "Solution to last Saturday''s puzzle" and "Solution of yesterday''s cross-word puzzle" (also 1924-12-06); its solution runs Monday 1924-12-01'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1925-01
    puzzle: 'Monday puzzles printing Saturday''s solution'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-06
  - date: 1935-12
    puzzle: 'daily puzzle still running, labeled "The Globe Cross-Word Puzzle"; no syndicate credit'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-05
  - date: 1936
    puzzle: 'Saturday puzzle marked "Solution next Monday", so Saturday is now part of the daily series'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-05
  - date: 1947
    puzzle: 'for a while the daily is headed "Crossword Puzzle" and the Sunday "Cross-word Puzzle", so the heading tells the two series apart'
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-05
  - date: 1970
    puzzle: daily crossword still running; no attribution or copyright line
    seen: Newspapers.com scans, by Alex DeJarnatt, 2026-10-05
  - date: 2003-04-20
    puzzle: 'Easter Parade by Henry Hook, on Easter Sunday; the syndicated copy in gxd is dated 2004-04-11, held a year for the next Easter'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 2004-12-19
    puzzle: 'two Cox and Rathvon puzzles: It''s the Thought (the regular Sunday crossword) and Diamond Heaven, a diamond-shaped Red Sox puzzle headed "The Globe Puzzle" (Globe Magazine p. 53, answers p. 43; the printed solution has JOHNNY and ONEON where the clues call for AGENCY and GREEN)'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 2007-04-29
    puzzle: 'an untitled, uncredited 15x15 in the TV Week insert, besides the Sunday crossword (also 2007-12-09); a separate series, not yet looked into'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 2015-10-18
    puzzle: 'two Sunday crosswords: WITH STYLE by Brendan Emmett Quigley and OPERA REVIEW by Emily Cox and Henry Rathvon'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05; OPERA REVIEW also on the Wayback snapshot of 2015-10-18
  - date: 2015-10-25
    puzzle: 'THE LAST SHALL BE FIRST, Cox and Rathvon (1-Across "Packs", 1-Down "Loonballs"); matches the Wayback snapshot of that day'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2015-11-01
    puzzle: '"Crone with the Wind", Henry Hook (1-Across "Teen zine topics"), in the issue with the editor''s note on his death; not in gxd'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2015-11-08
    puzzle: 'DOWNFALLS, Cox and Rathvon (1-Across "Contacts good to have"), a different puzzle from their 2002-08-18 "Downfalls"; not in gxd'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2015-11-15
    puzzle: 'FRONT AND BACK, Cox and Rathvon; matches the Wayback snapshot of that day'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2016-02-14
    puzzle: 'two Cox and Rathvon puzzles on facing pages: LOVERS (the 21x21 crossword, also on the website that day) and ANAGRAM PAIRS, a 21x21 themed crossword headed "THE GLOBE PUZZLE" on magazine p. 80, answers on p. 76 (print only; never on the website)'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-05
  - date: 2017-04-02
    puzzle: 'double issue: "Harder" THEMELESS CHALLENGER by Quigley (1-Across "Maytag product") facing THAT''S EXTRA by Cox and Rathvon'
    seen: Newspapers.com search for "Themeless Challenger", by Alex DeJarnatt, 2026-10-06
  - date: 2017-06-18
    puzzle: 'double issue: "Harder" THEMELESS CHALLENGER by Quigley (1-Across "Most pessimistic") facing CRIME BUSTERS by Cox and Rathvon'
    seen: Newspapers.com search for "Themeless Challenger", by Alex DeJarnatt, 2026-10-06
  - date: 2018-02-11
    puzzle: 'double issue: "Harder" THEMELESS CHALLENGER by Quigley (1-Across "Parade fall out?") facing ALPHABET SOUP by Cox and Rathvon'
    seen: Newspapers.com search for "Themeless Challenger", by Alex DeJarnatt, 2026-10-06
  - date: 2018-04-01
    puzzle: 'double issue: "Harder" THEMELESS CHALLENGER by Quigley (1-Across "Paper format", matching the Wayback snapshot) facing STANDARD MODELS by Cox and Rathvon'
    seen: Newspapers.com search for "Themeless Challenger", by Alex DeJarnatt, 2026-10-06
  - date: 2018-06-17
    puzzle: 'two facing crosswords, "Harder": THEMELESS CHALLENGER by Quigley (1-Across "Fast, sci-fi style") and "Easier": TRINOMIALS by Cox and Rathvon; neither on the website that day'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2018-10-14
    puzzle: 'two facing crosswords, "Harder": THEMELESS CHALLENGER by Quigley (1-Across "Honeyed pastry") and "Easier": GLOBAL CAFE by Cox and Rathvon; neither on the website that day'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2019-02-10
    puzzle: 'two facing crosswords, "The Globe Puzzle / Harder: THEMELESS CHALLENGER" (Quigley; the one on the website) and "The Globe Puzzle / Easier: UNGORGEOUS GEORGE" (Cox and Rathvon); the cover promises "extra puzzles"'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2022-07-31
    puzzle: 'IMAGINARY FRIENDS by Joon Pahk; not on the website that day'
    seen: Newspapers.com scan, by Alex DeJarnatt, 2026-10-06
  - date: 2024-06-09
    puzzle: 'THEMELESS CHALLENGER by Quigley as the ordinary Sunday puzzle, no "Easier" partner (1-Across "Slacks, say"); also 2025-08-03 (1-Across "Beginning with a setback") and 2026-04-12 in the Puzzmo index'
    seen: Newspapers.com search for "Themeless Challenger", by Alex DeJarnatt, 2026-10-06
status: researched
---

Project home, with the status of every Sunday since 1980 and how to help:
https://github.com/EveryPuzzleProject/bostonglobe
(status page: https://everypuzzleproject.github.io/bostonglobe/).

The Globe has run crosswords since February 25, 1917. By late 1924 it had
three series running at once: a Sunday puzzle (from 1917), a Saturday puzzle
(from May 26, 1923) and a Monday–Friday daily (from October 6, 1924), which
absorbed a Wednesday puzzle that ran from February 6 to October 1, 1924.
Because the series fall on different days, each date has at most one puzzle.
Each series printed its answers on a different schedule, so matching puzzles
to answers has to go by series; the Wednesday, October 8, 1924 paper prints
two solutions.

Everything through 1930 is in the public domain. With all three series
running, that could be 2,000 or more puzzles; how long the daily lasted is
the biggest unknown.

In later years only the Sunday (Globe Magazine) puzzle is the Globe's own.
It was syndicated too: from at least 2003 to 2015 LA Weekly and other papers
ran it weeks later (49 days later from 2009), and held some holiday puzzles
over to the next year. The copies most collections have came from that
syndicated run, so their dates are the syndicated dates, not the Globe's;
check Globe dates against print.
Online, at least from 2015 to 2024, the weekday "Globe crossword" was the
syndicated Universal Crossword. The Globe's online archive before 2024 is
gone (its per-puzzle pages, `games-comics/crossword/BGPZyyyymmdd.puz.html`,
now return 404), but Wayback snapshots of the crossword page itself recover
many Sundays. In summer 2026 the Globe moved its games to Puzzmo, carrying
over puzzles from February 2024 on.

Open questions:
- Did the Sunday series run continuously from 1917 to 1923, or stop and
  restart?
- When did the daily end? Still running in 1970. Was it the Globe's own
  all along, or syndicated at some point? From 1936 to 1970 it carries no
  credit or copyright line.
- "Cross Word Funnies, selected by Judge" (Saturdays 1925-02-14 to
  1925-02-28): are these reprints of Judge magazine's own puzzles? The Judge
  harvest has Judge's weekly puzzles for these weeks to compare against.
- From late November 1924 each Saturday puzzle is answered twice, the next
  Monday and the next Saturday. When does the Saturday reprint stop? (The
  "Saturday Cross Word Puzzle" heading ends after 1924-12-13.)
- The Saturday pairs (grown-ups and boys and girls) end 1925-04-04 by text
  search. Was the children's puzzle dropped, or moved to another day or
  section under another name?
- The 1924 Saturday pair, "Crossword Puzzles for the Grown-Ups" and
  "Crossword Puzzle for Boys and Girls": when did each start and stop, and
  did the children's puzzle continue after Saturday joined the daily?
- Were the Globe's 1931–1963 issues' copyrights renewed? If not, these
  puzzles are public domain too.
- When did the Sunday puzzle move into the Globe Magazine?
- Where are Sunday issues from 1925 to mid-1943? Newspapers.com lacks
  them. Is the Sunday Globe filed there under a separate title? Otherwise:
  ProQuest Historical Newspapers (has a Boston Globe collection; coverage to check), library microfilm,
  and whether the Sunday magazine was filmed at all.
- Do the Sunday answers run the following week? (Saturday's did, through 1924.)
- Who made the early puzzles? At least some carried readers' names and
  towns (S. E. Hale, Boston, 1924-11-29). Were they reader contributions?
- What filled 1931–1979? gxd has nothing between 1917 and 1980.
- Where is the Globe Magazine on Newspapers.com from about August 2012?
  Title searches stop finding the Sunday puzzle then (2013 issues turn up
  only sometimes); 2009-04-05 is missing outright.
- Which papers besides LA Weekly carried the Sunday puzzle, and from when?
- Which issues ran two crosswords ("The Globe Puzzle / Harder" and
  "Easier", with "extra puzzles" on the cover)? Known: 2004-12-19,
  2015-02-08, 2015-10-18, 2016-02-14, 2017-04-02, 2017-06-18, 2018-02-11,
  2018-04-01, 2018-06-17, 2018-10-14, 2019-02-10. From 2017 the Harder one
  is Quigley's "THEMELESS CHALLENGER" facing a Cox and Rathvon puzzle, so
  the Themeless Challenger Sundays of 2019–2023 (2019-03-31, 06-23, 10-13,
  2020-03-29, 10-18, 2021-05-23, 2022-09-18, 2023-10-15) are candidates. By
  2024 the title is an ordinary Sunday puzzle with no partner.
