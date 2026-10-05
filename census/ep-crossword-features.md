# Syndicated crossword features in Editor & Publisher's Syndicate Directory

Source: E&P's annual Syndicate Directory, read from archive.org OCR text
(`pub_editor-publisher`, `<item>_djvu.txt`). Every row in
[`ep-crossword-features.csv`](ep-crossword-features.csv) cites the item it came from.
Read in October 2026. OCR is often poor. Where feature and syndicate columns were split
apart by the OCR, the syndicate was matched by column order, and the row says so.

## What the counts mean

A "feature" is one listing: a syndicate's named crossword product, such as a daily
puzzle or a separate Sunday puzzle. A syndicate selling a daily and a Sunday puzzle
counts twice. Canadian-only distributors (Miller Services, Dominion News Bureau, Rapid
Grip and Batten, Canada Wide), features known only from display ads, and cryptics are
in the CSV but not in the counts below. Closely related grids are counted: diagramless,
acrostic/crostic, Spanish crosswords and crossword contests.

## Distinct US features per sampled year

| Year | Features | Item |
|---|---|---|
| 1924 (1st directory) | 9 | sim_editor-publisher_1924-10-25_57_22 |
| 1925 | 13 | sim_editor-publisher_1925-07-18_58_8 |
| 1930 | 11 | sim_editor-publisher_1930-08-30_63_15 |
| 1935 | 11 | sim_editor-publisher_1935-09-28_68_20 |
| 1940 | 14 | sim_editor-publisher_1940-09-14_73_37 |
| 1945 | 13 | sim_editor-publisher_1945-10-06_78_41 |
| 1950 | 18 | sim_editor-publisher_1950-07-29_83_31 |
| 1955 | 24 | sim_editor-publisher_1955-07-30_88_32 |
| 1960 | not in scans | the issue for 1960-07-30 lacks the directory |
| 1965 | 26 | sim_editor-publisher_1965-07-31_98_31 |
| 1970 | 29 | sim_editor-publisher_1970-08-01_103_31 |
| 1975 | 30 | sim_editor-publisher_1975-07-26_108_30 |
| 1980 | 35 | sim_editor-publisher_1980-07-26_113_30 |
| 1985 | 42 | sim_editor-publisher_1985-07-27_118_30_0 |
| 1990 | 60 | sim_editor-publisher_1990-07-28_123_30_0 |
| 1995 | 56 | sim_editor-publisher_1995-07-29_128_30 |
| 2000 | 65 | sim_editor-publisher_2000-07-31_133_31 |

## Distinct US features, every extracted year

Gap years were extracted later by helper agents with the same rules; counts are
listings, as above.

| Decade | Year: features |
|---|---|
| 1920s | 1924: 9 · 1925: 13 · 1926: 10 · 1927: 6 · 1928: 9 · 1929: 15 |
| 1930s | 1930: 11 · 1931: 15 · 1933: 11 · 1934: 14 · 1935: 11 · 1937: 9 · 1938: 14 · 1939: 14 |
| 1940s | 1940: 14 · 1942: 13 · 1945: 13 · 1947: 17 · 1948: 19 · 1949: 18 |
| 1950s | 1950: 18 · 1951: 18 · 1952: 20 · 1953: 22 · 1954: 23 · 1955: 24 · 1956: 25 · 1957: 28 · 1958: 28 · 1959: 27 |
| 1960s | 1961: 29 · 1962: 27 · 1963: 24 · 1964: 24 · 1965: 26 · 1966: 24 · 1967: 24 · 1968: 25 · 1969: 26 |
| 1970s | 1970: 29 · 1971: 22 · 1972: 29 · 1973: 30 · 1974: 29 · 1975: 30 · 1976: 39 · 1977: 39 · 1978: 43 · 1979: 42 |
| 1980s | 1980: 35 · 1981: 35 · 1982: 36 · 1983: 35 · 1984: 42 · 1985: 42 · 1986: 44 · 1987: 48 · 1988: 51 · 1989: 56 |
| 1990s | 1990: 60 · 1991: 64 · 1992: 62 · 1993: 63 · 1994: 63 · 1995: 56 · 1996: 59 · 1997: 60 · 1998: 56 · 1999: 60 |
| 2000s | 2000: 65 |

The 1937 listing is incomplete because its main crossword page is missing from the OCR.
Gap-year rows flag some judgment calls in their notes: acrostic-type and word-game items
filed near crosswords (Singer's Crosswordwise, Hart's Acrostics), contests, and items
marked "crossword status unconfirmed". These are in the counts; filter on the notes to
drop them.
Counts are listings, not distinct grids: one syndicate often sold the same puzzle under
two names. From the 1980s on, the count grows because small puzzle packagers (Singer,
Scrambl-Gram, Worldwide Media, regional "state" crosswords) list many titles. The number
of mainstream daily crosswords stayed roughly 10–15 throughout.

## Long-running features (as listed)

- **King Features / Eugene Sheffer crossword:** J. C. Boyd wrote the KFS puzzle in
  1925–26. Sheffer is named from 1934 (and for Rapid Grip and Batten in Canada from
  1933) to 2000. It was "Crossword Puzzle with Cryptoquip" from the 1970s.
- **King Features Sunday / Premier Sunday Cross Word Puzzle:** 1934–2000. Its authors
  were Sheffer, then Jo Paquin (1975–90), then Donna Stone (1995–2000).
- **Central Press Association (King) "CP Crossword Puzzle":** 1925–1970.
- **King Features Spanish crosswords:** 1947–1995 (Ramos and Alfaro from the 1970s).
  Also Thomas Joseph's crossword, 1975–2000.
- **Herald Tribune crossword:** New York Herald Tribune Syndicate 1924–1965, then
  Publishers Newspaper Syndicate ("New York Herald-Tribune Staff") to 1970.
- **NEA crossword (daily, plus a weekly from 1945):** 1928–2000. It was sold as "The
  World Almanac Crossword Puzzle" in 1990 and "The Crossword Puzzle" later.
- **AP Newsfeatures crossword:** 1930–2000. J./G. Van Cleft Cooper wrote it 1930s–1970,
  then Nina Cooper and Doug Cooper. Chet Currier's Sunday puzzle ran 1980–1995.
- **Chicago Tribune–New York News / Tribune Media Services crossword:** 1925
  (weekly) and 1934–2000. Herb Ettenson was editor 1975–1995; Wayne Robert Williams
  in 2000.
- **United Feature Syndicate crossword:** 1929–2000. Lars Morris wrote it in the 1930s
  and 40s. It became "Crossword Puzzler" and "Today's Crossword" from 1975.
- **Bell Syndicate (later Bell-McClure):** 1924–1970.
- **International Syndicate (Baltimore):** 1924–1957.
- **Associated Newspapers:** 1926–1957.
- **Ledger Syndicate / Walter B. Gibson:** 1924–1929. Gibson is the later author of
  The Shadow. Ledger offered a weekly diagramless in 1934.
- **McClure / Richard H. Tingley:** 1924–1931.
- **General Features Corp.:** Maynard Nichols' Sunday crossword and Margaret Farrar's
  daily ran 1949–1970.
- **Los Angeles Times Syndicate:** Margaret Farrar's puzzle from 1975, then the LA Times
  daily and Sunday through 2000. Also Charles Preston's Quote-Acrostic (1970–2000) and
  the Washington Post crossword (1975).
- **New York Times crossword:** listed from 1975 to 2000 (Maleska, then Will Shortz).
- **Weekly-paper services:** W. L. Gordon (A. C. Gordon), 1947–1980. Smith-Mann / Al
  Smith (Bernice Paschen), 1953–1980s. Community Press Service and Community & Suburban
  Press Service.

## Notable names

Walter B. Gibson, J. C. Boyd, Richard H. Tingley, Eugene Sheffer, Lars Morris, G. Van
Cleft Cooper, Margaret Farrar, Maynard Nichols, Charles Preston, Herb Ettenson, Thomas
Joseph, Jo Paquin, William Lutwiniak, Eugene T. Maleska, Will Shortz, Stanley Newman
(Newsday, through Creators and the American Crossword Federation, 1990–2000), Timothy
Parker (Universal Crossword, 2000), Mike Shenk (Exmark weekly, 1980) and Gene Owens
(regional crosswords, 1990).

## E&P news items noticed (not searched for systematically)

- 1924-10-18 (`sim_editor-publisher_1924-10-18_57_21`): the International Syndicate,
  Baltimore, has added a daily cross word puzzle. Walter B. Gibson is drawing a new daily
  cross-word puzzle for the Ledger Syndicate. A Metropolitan Newspaper Service ad for
  puzzles "From the Second and Third Crossword Puzzle Books" names client papers
  (St. Louis Post-Dispatch, Washington Post, Cleveland Plain Dealer and others).
- 1928-08-25 (`sim_editor-publisher_1928-08-25_61_14`): E&P's directory commentary says
  that nothing has yet replaced the crossword's popularity and that 11 syndicates have
  crossword series.
- 1929-08-31 (`sim_editor-publisher_1929-08-31_62_15`): the commentary says puzzles
  "branching from the cross-word tree" still have vitality after five years of daily
  publication.
- 1930-08-30 (`sim_editor-publisher_1930-08-30_63_15`): a Columbia Pictures
  movie-promotion crossword offered to papers as a 15-cent mat.
- 1940-09-14 (`sim_editor-publisher_1940-09-14_73_37`): a readership summary reports
  that crossword puzzles attract few readers.
- 1950-07-29 (`sim_editor-publisher_1950-07-29_83_31`): Jane McMaster's article on
  the 25th directory says the first was Oct. 25, 1924 (18 pages, 900 features) and that
  no directories were published in 1943 and 1944. A second item says a News-Chronicle
  (apparently the London paper), cut to six pages, kept its crossword over its weather
  map.
- 1960-07-16 (`sim_editor-publisher_1960-07-16_93_29`): announces the 1960 directory
  for July 30. That issue's scan does not contain it.

## Gaps

- **Directory not found or not legible:** 1932, 1941, 1960, 1936 (located at
  `sim_editor-publisher_1936-09-26_69_39_0`, but the crossword pages are absent) and
  1946 (located at `sim_editor-publisher_1946-09-07_79_37`, but the listing OCR is
  unreadable; a Bell ad lists "Cross Words — D. & S."). 1943 and 1944 were never
  published.
- **Every other year from 1924 to 2000 is extracted.**
- **Directory issue dates:** 1924-10-25; 1925-07-18; 1926-06-05; 1927-08-27;
  1928-08-25; 1929-08-31; 1930-08-30; 1931-08-29; 1933-08-26; 1934-09-29; 1935-09-28;
  1937-09-25; 1938-09-24; 1939-09-30; 1940-09-14; 1942-09-19; 1945-10-06; 1946-09-07;
  1947-09-06; 1948-08-28; 1949-08-06. From 1950 on, the last issue of July or the first
  of August.
