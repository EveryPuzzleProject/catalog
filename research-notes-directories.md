# Publication directories: feasibility survey (first pass, 2026-10-02)

Question: can we build "every US daily, weekly, monthly and quarterly, by year"
from bulk directories, then ask of each "did it carry a crossword, and which"?
This is a survey of sources, not the census. Everything under **Confirmed**
was seen on a page or API response opened in this session; everything else is
under **Not confirmed**.

## Tool caveats
- HathiTrust (catalog, Bib API, full-text search) returned 403 / a Cloudflare
  bot check to curl, WebFetch and the browser. Nothing about HathiTrust
  full-view vs search-only is confirmed here. Needs a human in a browser.
- loc.gov API limit is 20 requests/minute for collection/search endpoints, with
  a one-hour block if exceeded (https://www.loc.gov/apis/json-and-yaml/working-within-limits/).
  I hit it partway through; some per-year counts below are therefore missing.
- Google Books API: anonymous daily quota exhausted (429). Nothing checked there.
- UNT Digital Library search pages sit behind an ALTCHA bot check; item pages
  and collection pages opened fine through WebFetch.
- Crossword Tracker (crosswordtracker.com): expired TLS certificate and the home
  page returned "There was an error processing your request" (2026-10-02).
- archive.org full-text search (FTS) works without login:
  `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=...&page_type=collection_details&page_target=<collection>`,
  and per-item search-inside works via `https://<server>/fulltext/inside.php?item_id=..&doc=..&path=..&q=..`.
  Both started returning non-JSON after many calls, so they're probably rate-limited too.

## 1. Library of Congress: US Newspaper Directory + Chronicling America

### Confirmed
- **Directory of U.S. Newspapers in American Libraries** is a loc.gov collection
  with a JSON API:
  `https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/?fo=json`.
  Total: **159,019 title records** (2026-10-02). Facets include frequency
  (`fa=publication-frequency:daily`), state/county/city, language, ethnicity and
  holding type, and `dates=YYYY/YYYY` filters records whose run covers that year.
  Frequency facet totals: Weekly 109,967; Daily 23,235; Monthly 6,870;
  Semiweekly 5,293; Biweekly 2,138; Semimonthly 1,877; Triweekly 1,284.
  Records carry LCCN, OCLC number, the 260/362 publication statements
  ("Vol. 1, no. 1 (Mar. 16, 1973)-"), place hierarchy and per-library holdings
  (original / microfilm master / service copy, with date ranges).
- Example filtered counts (record counts, not distinct papers):

  | year | daily | weekly | semiweekly | monthly | all |
  |---|---|---|---|---|---|
  | 1913 | 5,351 | 28,815 | 1,302 | 1,581 | 40,526 |
  | 1925 | 5,312 | 28,366 | 1,249 | 1,765 | 40,524 |
  | 1940 | 5,151 | – | – | – | – |
  | 1960 | 5,073 | – | – | – | – |

  **Warning:** these look too flat and too high (see the Ayer figures below:
  Minnesota alone in 1930 had 43 dailies + 8 with Sunday editions). Likely
  causes: one record per title *variant* (title changes, editions), open-ended
  or coarse date ranges, and frequency being a single facet per record. The
  `dates` filter needs checking against the bulk MARC before anyone uses these
  numbers.
- **Bulk MARC, no API needed:** public S3 bucket `https://chronam-bib.s3.amazonaws.com/`
  (listable). Contents:
  - `original_titles/titles-20091130.xml` (449 MB MARCXML bib records, plus small
    incremental files to 2011). Opened the first 4 KB: records carry 008 (start/end
    year and frequency code), 245 title, 260 place/publisher/dates, 310 current
    frequency, 362 numbering, 752 country/state/county/city. That is exactly the
    "title, place, dates, frequency" we need.
  - `holdings/2025-09-02/metacoll.DLC.lhr.USNP.marcxml.*.xml` (10 files, 452 MB):
    current holdings records (852 library, 866 coverage).
  - `worldcat_titles/...` older bags.
- **Chronicling America** (now at loc.gov; the old `chroniclingamerica.loc.gov`
  search redirects with 308 to `https://www.loc.gov/chroniclingamerica/...`).
  JSON: `https://www.loc.gov/collections/chronicling-america/?q=crossword&dl=page&fo=json&c=1&at=pagination`.
  Coverage dates 1736–1963; 4,627 digitized titles; 23,833,657 pages (`dl=title` / facets).
- **Example queries (2026-10-02):**
  - `q=crossword`, all years: **73,372 pages**. By decade: 1920s 12,920; 1930s 19,026;
    1940s 20,817; 1950s 13,252; 1960s 5,522; 1910s 301; and ~1,500 hits before 1910
    (OCR noise or the word used in other senses).
  - `q="cross word"`: 23,379 pages (1920s 6,468; 1930s 4,317; plus many pre-1913 hits
    where the phrase means something else).
  - Per year, `q=crossword` pages / all pages in the collection that year:

    | year | crossword pages | all pages | share |
    |---|---|---|---|
    | 1913 | 39 | 573,989 | 0.007% |
    | 1920 | 5 | 564,713 | – |
    | 1923 | 28 | 242,750 | 0.01% |
    | 1924 | 1,730 | 220,584 | 0.8% |
    | 1925 | 7,238 (7,107 in an earlier identical query) | 196,068 | 3.7% |
    | 1926 | 1,089 | 167,740 | 0.6% |
    | 1930 | 1,612 | 133,442 | 1.2% |
    | 1935 | 2,767 | 149,428 | 1.9% |
    | 1940 | 2,868 | 121,015 | 2.4% |
    | 1945 | 2,243 | 133,949 | 1.7% |
    | 1950 | 1,204 | 86,845 | 1.4% |
    | 1955 | 1,452 | 81,544 | 1.8% |
    | 1960 | 1,445 | 79,324 | 1.8% |

    The 1924–26 spike matches the craze. These are pages matching the word, not
    puzzles: in 1935, 1,013 of the 2,767 hits are on page 1 (index boxes like
    "Crossword puzzle ... page 12", plus contest news). The hits are heavily
    concentrated: Washington DC titles were 1,517 of the 2,767 in 1935 (Evening
    Star 654, Washington Times 621), and the Evening Star has 21,593 of the
    73,372 all-time hits.
  - The title facet only returns the top 10. To count distinct titles per year,
    page through results (`c=160`, `at=results`) and collect `partof_title`.
    About 46 calls for 1925, which needs throttling to under 20/min.
- **Bulk OCR:** `https://chroniclingamerica.loc.gov/data/ocr/` still serves a
  directory index of per-batch `.tar.bz2` files (about 3,000 links; the first one
  is 768.84 MB). Not downloaded.
- NDNP scope: chronological scope 1690–1963; awardees must establish public-domain
  status for papers under 95 years old (NDNP Technical Guidelines 2026–28,
  https://www.loc.gov/ndnp/guidelines/NDNP_202628TechNotes.pdf). So
  Chronicling America after 1928 holds only papers cleared as PD (typically no
  copyright notice or not renewed), which skews which papers we can see.

### Not confirmed
- Whether the `dates` filter matches exactly by year.
- That the 2009 titles dump is still the bib source for the live directory (the
  holdings are refreshed to 2025-09-02, but I found no newer bib file).

## 2. Editor & Publisher: Year Book and Syndicate Directory

### Confirmed
- **E&P magazine itself is open on archive.org, 1901–2015**, collection
  `pub_editor-publisher` (identifiers `sim_editor-publisher_YYYY-MM-DD_vol_iss`).
  5,367 items, roughly 45–56 per year for 1909–2003, then about 12 a year for
  2004–2015 (monthly). No restricted items among them. OCR and full-text search
  work. Annual subject indexes are in the series for 1926 and 1936–1961 (e.g.
  `sim_editor-publisher_1943_76_index` indexes "Crossword puzzles in 1884",
  "... in London Times").
- **Syndicate Directory:** E&P's 1975 directory issue says its "first annual
  directory of syndicated features was published with the issue of October 18,
  1924", that the 1975 one is the 50th, and that "Two editions were skipped
  during World War II" (`sim_editor-publisher_1975-07-26_108_30`, p. 7). It ran
  as a pull-out section of a late-July issue in later decades (40th: 1965-07-31;
  48th: 1973-07-28; 63rd: 1988-07-30).
- **It lists crossword features by syndicate.** Examples:
  - 1926-06-05 (`sim_editor-publisher_1926-06-05_59_2`, p. 37 and 43): "Cross Word
    Puzzle(s)" entries for Graphic Syndicate, International Syndicate, King
    Features (J. C. Boyd), Ledger Syndicate (Walter B. Gibson), McClure (Richard
    Tingley), NY Herald Tribune Syndicate, Premier Syndicate (weekly), Star
    Newspaper Service, Associated Newspapers, Bell Syndicate. Each has a
    frequency code (d/w).
  - 1962-07-28 (`sim_editor-publisher_1962-07-28_95_30`): format is feature —
    frequency/size/medium — author — syndicate code (e.g. "Crossword Puzzle —
    w-2c-mat — Staff — C29"). It reported 235 syndicates that year.
  - 1972, 1973, 1974 and 1980 directories list several crossword features each,
    by syndicate and author.
- **It does not list client papers.** In the 1962 directory, "clients" occurs only
  in unrelated news items. Entries give feature, author, frequency and syndicate,
  never which papers carried them.
- **E&P International Year Book:** archive.org collection
  `pub_editor-and-publisher-international-year-book` holds only the **table of
  contents and index** pages for 1980–2004 (38 items); the full volumes are not
  there. Its description says the Year Book was established 1921 and published until
  2010, and that it was an issue of the magazine ("International Year Book
  Number") until 1959. The 1990 index (`sim_editor-and-publisher-international-year-book_1990_index`)
  has a "Syndicated features" section and an advertisers' list under
  "SYNDICATES & SPECIAL FEATURES". Full 2009 and 2010 volumes are on archive.org as
  lending-only (`editorpublisheri0000unse`, `editorpublisheri0000unse_t8r6`).
- The pre-1959 Year Book Number issues seem **not** to be in the magazine scans:
  `sim_editor-publisher_1925-01-31_57_36` (the date the 1924-12-20 issue announced
  for the Year Book Number) has only 17 images.
- **Trade-press crossword coverage:** FTS over `pub_editor-publisher` found
  "crossword" in 1,261 issues and "cross word puzzle" in 212 (1924: 13, 1925: 23 by
  issue). Useful finds: 1924-10-18 ("The International Syndicate, Baltimore, has
  added a daily cross word puzzle feature"; Walter B. Gibson drawing one for the
  Ledger Syndicate); 1944-03-18 (a paper able to "reinstate the daily cross word
  puzzle, dropped as a space conservation measure"); 1945-12-15 (a readership
  table ranking "Crossword Puzzle" against columns); 1979-07-07 (readership survey:
  "consumer information and crossword puzzles, each 30%").

### Not confirmed
- Which Year Book years HathiTrust or Google Books hold, or in what view (blocked).
- Whether any Year Book "Syndicated features" section lists features per paper.
  The Year Book's per-newspaper entries list staff and services, but I did not see
  a full volume.
- Whether every annual Syndicate Directory from 1924 to the 2000s is in the
  archive.org scans. The confirmed issues are 1924-10-18, 1926-06-05, 1962,
  1965, 1972–75, 1980, 1988 and 1997.

## 3. N. W. Ayer & Son's American Newspaper Annual / Directory

### Confirmed
- **UNT Digital Library, Newspaper Resources collection**
  (https://digital.library.unt.edu/explore/collections/NPRS/): Ayer's *American
  Newspaper Annual* 1880–1922 (43 items as "Annual", 25 as "Annual and Directory"),
  plus Rowell's directory 1869–1877. Items have searchable OCR and are Open Access
  (e.g. 1920 vol. 2, https://digital.library.unt.edu/ark:/67531/metadc9268/).
- **UNT OCR Text Dataset** (https://digital.library.unt.edu/ark:/67531/metadc1234371/):
  "volumes covering the years 1910 to 1922 ... 25 volumes comprised of 16,669 pages
  of text", in 2 zip files. This is a bulk-ready machine-readable Ayer, but it
  stops at 1922.
- **archive.org:**
  - 1930, v.62: `nwayersonsdirect6219unse` (University of Illinois scan, 1,806
    images, OCR). Each state has "NEWSPAPER AND PERIODICAL STATISTICS" by period of
    issue (e.g. Minnesota: Daily 43; Daily with Sunday 8; Weekly newspapers 500;
    Monthly 83 ...). The contents list "Statistics of American Publications" on
    pp. 12–13 and "380 classified lists". Search-inside for "crossword" and
    "puzzle" found 0. The OCR of maps is garbage; the text pages are fair.
  - 1884: `nwayersonsdirect00nwayuoft` (Toronto; title page reads "American
    Newspaper Annual"). Entries give politics, circulation and county.
  - 1880: `ayerdirectorypu00presgoog` (Google/Michigan).
  - 1969 (`nwayersonssdirec0000unse`) and 1983 IMS/Ayer
    (`imsayerdirectory0000unse`): lending-only.
  - `ayermediadata`: a Derek Long / Eric Hoyt CSV of about 500 media-trade titles
    drawn from Ayer 1900–1929 yearly and 1930–1960 every five years. It shows that
    UIUC/Media History people worked from Ayer volumes for those years.
- **Rowell's American Newspaper Directory**: many years 1869–1909 open on
  archive.org (e.g. `americannewspape1909newy`). All pre-crossword, but useful for
  title continuity.
- Copyright: works published in 1930 or earlier are public domain in the US as of
  2026, so Ayer 1923–1930 should be legally open even where not yet online.
- Gale Directory of Publications (Ayer's successor): archive.org has 1983 and
  1993–2017 lending-only (`pub_gale-directory-of-publications-and-broadcast-media`).

### Not confirmed
- HathiTrust holdings and views of Ayer 1923–1986 (a search-engine summary claimed
  full view 1884–1922 and limited view for 1929, 1930, 1931, 1941, 1945, 1951 and
  1961; I could not open HathiTrust to check).
- Whether Ayer lists any feature content. It doesn't appear to: it gives
  frequency, politics, established date, circulation and size.

## 4. Magazine / periodical directories

### Confirmed
- **Writer's Market** (F&W, Cincinnati) has a **"Crossword Puzzle Magazines"**
  market section, naming titles, publishers, editors and what they buy:
  - `writersmarket0000unse_c2g5` (1963, open): p. 37 "CROSSWORD PUZZLE MAGAZINES",
    listing Approved/Classic Crossword Puzzles (Florence Bierman), Best Crossword
    Puzzle (Popular Library), the Harle Publications line (Walter H. Holze),
    Charlton Crossword Magazines (Jane Bacon), and others.
  - `writersmarket1961cinc` (open; metadata says 1922, the series start; the
    identifier suggests 1961): contents list "Crossword Puzzle Magazines ... 26".
  - `writersmarket1995cinc` and `writersmarket00cinc` (open; misdated 1922; content
    is 1990s, e.g. GIANT CROSSWORDS, Scrambl-Gram Inc.). Here crosswords appear as
    "Fillers" lines in general magazine listings ("Fillers: Acrostic or crossword
    puzzles. Pays $25-50").
  - Other years on archive.org (1959, 1971–2017) are lending-only.
  This is the best open source for the puzzle-magazine category, and the filler
  lines flag general magazines that buy crosswords.
- **Ulrich's**: early editions are open via the Digital Library of India on
  archive.org (1932 `in.ernet.dli.2015.167772`, 1935 `in.ernet.dli.2015.158056`,
  1938 `in.ernet.dli.2015.157563`, 1942 `in.ernet.dli.2015.157562`). It is a
  selective list. The 1938 edition's subject "Puzzles" contains only The Cryptogram
  and The Enigma (National Puzzlers' League), with no crossword magazines. Later
  editions (1959, 1975–2012) are lending-only.
- **Standard Periodical Directory**: nothing usable on archive.org (lending-only
  1993, 1994 and 2000; the "1977" hit is a 2-page CIA reading-room document).

## 5. Puzzle-specific trackers and other leads
- Crossword Tracker: down (see caveats).
- E&P magazine is the strongest open trade source for crosswords (above). Its
  annual indexes (1926, 1936–61) give subject entries for crosswords.
- 1999-03-06 E&P (`sim_editor-publisher_1999-03-06_132_10`) on a Chicago Tribune
  electronic edition: "Comics and crossword puzzles have not yet been made
  available". Puzzles were the part left out of the digital product.
- Not researched: syndicate client lists (King, Tribune, Universal/Andrews McMeel,
  NEA, CNS). Per-paper carriage data probably has to come from the papers'
  own pages or from syndicate promo ads in E&P ("now in N papers").

## 6. Are crossword pages left out of microfilm and digitization?

### Confirmed
- The IFLA *Guidelines for Newspaper Preservation Microfilming* (copy fetched from
  https://www.ifla.org/wp-content/uploads/2019/05/assets/newspapers/publications/guidelines-for-newspaper-preservation-microfilming-en.pdf)
  say newspapers "should normally be filmed in full including all sections and
  supplements". However, only the main edition is filmed in full, and it is "often
  difficult to know if the contract between the publisher and the filming company
  stipulates that all supplements ... or variant editions will be filmed." So the
  standard doesn't exclude puzzles, but separately-printed supplements (Sunday
  magazines, comics sections, where many Sunday crosswords ran) are at risk.
- NDNP metadata records page and issue presence ("pagePresent" indicators), so
  missing pages in Chronicling America are at least flagged per page.
- Modern digital editions: Twipe reports US publishers "had left puzzles out of
  their digital products" because they could not replicate them
  (https://www.twipemobile.com/puzzling-case-of-puzzles/). The 1999 E&P item above
  is a second example.

### Not confirmed
- No guideline found that explicitly says to skip crosswords or puzzle pages. I
  found no evidence either way about how commercial vendors (ProQuest,
  Newspapers.com, NewsBank) treat puzzle pages. The user's caution stands as
  plausible but unquantified. The cheapest way to measure it: for a sample of
  papers known (from E&P or Syndicate Directory evidence) to have run a daily
  crossword, check Chronicling America's pages for that date range.

## Recommended backbone
1. **Newspapers, every year 1913–present:** the LoC US Newspaper Directory bib
   MARC (S3 `original_titles/titles-20091130.xml` plus increments). Parse 008
   start/end years and frequency, 310/321 frequency history, and 752 place, into
   one row per title-run. It covers all US newspapers libraries hold, with LCCNs
   that link straight to Chronicling America and holdings. Treat it as the title
   universe, not a count: deduplicate title changes via 780/785 linking fields.
2. **Calibrate counts against Ayer** for spot years (1910–1922 via the UNT OCR
   dataset; 1930 via archive.org's per-state statistics tables). Use E&P Year Book
   totals where reachable.
3. **Crossword carriage:** Chronicling America full-text per title per year for
   1913–1963 (API, throttled; or bulk OCR batches), plus the E&P Syndicate
   Directory for "which crossword" (features and syndicates, 1924–2000s) and E&P
   news items for named papers.
4. **Magazines:** Writer's Market crossword-magazine sections (1960s open, other
   years borrowable) for puzzle magazines. Ulrich's/Ayer only for general
   periodical counts.

## First concrete step
Write `tools/usnp_titles.py`. It should stream-parse
`https://chronam-bib.s3.amazonaws.com/original_titles/titles-20091130.xml` (one
449 MB download, kept outside the repo), emit a CSV of LCCN, title, place, start
year, end year and frequency, and print per-year counts of dailies and weeklies for
1913–2025. Check 1930 against Ayer's 1930 state tables (Minnesota: 51 dailies,
500 weekly newspapers). If the figures roughly agree, that CSV becomes the census
spine. In the same step, page through Chronicling America `q=crossword` for 1925
at 15 calls/min to get the first per-title "crossword seen" list.

## LoC census (2026-10-02)

Built `census/` from the 2009 bulk MARC (`tools/census_loc.py`; details,
caveats and sources in `census/README.md`).
- The flat ~5,300 dailies per year from the API come from naive date reading:
  one record per LCCN with unknown end digits widened (`1uuu` = 1999) gives
  5,082 / 5,085 / 4,900 for 1913 / 1925 / 1960. Other causes: 24,287 records
  repeat an LCCN; microform copies and editions; title-change overlap years.
- Cleaned estimate (lifetime-weighted dates, title+place dedup), dailies:
  1913 3,065; 1925 2,893; 1930 2,760; 1942 2,549; 1960 2,298; 1990 1,992;
  2009 1,869. Weeklies: 15,820; 14,072; 13,673; 13,515; 11,085; 8,776; 7,980.
- **Minnesota in Ayer 1930 resolved:** the state box says Daily 43 + "Daily, with
  Sunday edition" 8 = **51 dailies**, and 500 weekly newspapers (+51 weekly
  periodicals). The national table on p. 12 has 42 + 8. Ayer's US total
  (states, DC and territories) is 2,299 + 569 = 2,868 dailies (p. 13). LoC estimate
  for 1930 is 2,760 for states + DC, against Ayer's 2,802.
- Against E&P (Statistical Abstract 2012, table 1135) the LoC estimate runs
  20–27% high from 1970 to 2009 (e.g. 1990: 1,893 English vs 1,611), likely
  from stale "current" records and editions.

## E&P directories extracted (2026-10-02)
- Crossword features from the E&P Syndicate Directory are in
  `census/ep-crossword-features.csv` (678 rows; each row has its archive.org item id)
  and are summarized in `census/ep-crossword-features.md`.
- The first directory was in the 1924-10-25 issue, not 10-18 (as the 1950 issue
  confirms). Directories ran from June to October through 1949, then in late July or
  early August.
- Covered so far: 1924–31, 1933–35, 1937–40, 1942, 1945, 1947–50, 1955, 1965, 1970,
  1975, 1980, 1985, 1990, 1995 and 2000. Not found or not legible: 1932, 1936
  (crossword pages missing), 1941, 1946 (OCR unreadable) and 1960 (not in the scans).
  The other years 1951–1999 are located but not yet extracted.
- Locating directories: use `<year>_<vol>_index` items (1936–61) and FTS on "<Nth>
  annual" with `AND year:YYYY`. FTS rate-limits after roughly 10 quick calls.
