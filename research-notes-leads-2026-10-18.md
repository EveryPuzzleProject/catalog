# Leads and access notes (2026-10-18)

From a planning session on getting more traction for the catalog. Everything
under **Confirmed** was seen on a page opened or a search result read that
day; the rest is marked as unverified.

## 1. Generate entries in bulk, flagged as generated

The catalog has 23 entries because entries are only made from hand-filed
sightings, while `census/` already holds about 2,800 dailies a year and 678
E&P crossword features. Ideas, roughly in order of payoff:

- One entry per publication in the gxd corpus, with first and last dates from
  the puzzles themselves. This alone should cover more than the catalog finds
  independently today.
- Chronicling America `q=crossword` hits grouped by title and year, as `lead`
  entries with 1924–1963 runs (see research-notes-directories.md for the API).
- E&P features as their own records, linked from papers through `carries`.

Quality: keep generated facts separate from hand edits (so a rebuild doesn't
overwrite corrections), record which tool and source produced each one, and
only let a cited source or a person move an entry past `lead`.

## 2. Carriage data doesn't exist yet

No database found records which papers carried which syndicated crossword,
when. Directories list features, not clients (research-notes-directories.md).
The closest precedent is comics: Allan Holtz's *American Newspaper Comics*
(2012) gives 7,000+ strips with dates, syndicates and source notes, still one
row per feature (https://en.wikipedia.org/wiki/Allan_Holtz). Holtz also lists
E&P features he could never find in any paper, so a directory listing does
not prove a feature ran
(https://comicstriphistory.com/2009/07/mystery-strips-of-e-p-listings.html).
Stripper's Guide's "News of Yore" series reprints E&P items and is a good
source generally.

Proposed record: paper × feature × date range × lag, each backed by
sightings. Lag is best measured by matching a paper's puzzle to a dated
reference copy by content (answer sets or black-square pattern survive bad
OCR). Seed records can come from historians' knowledge (Ben Zimmer, T.
Campbell), each with a citation or sighting to check later.

Finding carriers: syndicated puzzles usually printed a credit line, so
full-text search for a syndicate's name near "cross word" gives candidates.
Untested at scale (the loc.gov API timed out from the agent sandbox).

## 3. Books

Confirmed:
- NYPL transcribed the Catalog of Copyright Entries book volumes, 1923–1964,
  to XML (https://github.com/NYPL/catalog_of_copyright_entries_project), with
  renewals 1950–1991 in https://github.com/NYPL/cce-renewals/. Registration
  records exist whether or not LC kept the deposit copy.
- LC offers about 25 million MARC records, 1968–2014, as a free bulk download
  (https://loc.gov/item/prn-17-068).
- LC's current Sports, Recreation and Leisure collections policy (rev. Dec
  2022) puts crossword puzzles in GV1199–1565 at collecting Level 3 for US
  material, and says games in book format are collected
  (https://www.loc.gov/acq/devpol/sports.pdf). Selective, not excluded. Older
  versions are only available on request, so what applied 1968–2014 is
  unknown.
- LC holds and has digitized at least some 1920s puzzle books, e.g. Simon &
  Schuster's *Cross Word Puzzle Book, 2nd series* (1924), GV1507.C7C7, LCCN
  sv 87054725 (https://archive.org/details/crosswordpuzzleb00unse_0); the
  "sv 87" prefix suggests it was cataloged decades later (inference).

Gaps: 1965–67, post-2014, and mass-market books LC never cataloged. Test the
MARC dump's coverage against a known series (S&S, Dell).

## 4. Black newspapers

No prior work on early Black crossword constructors was found in a search
(2026-10-18).

Confirmed:
- ProQuest Historical Black Newspapers: 14 titles 1893–2010 (Atlanta Daily
  World, Baltimore Afro-American, Chicago Defender, Cleveland Call & Post,
  Houston Informer, Kansas City Call, Los Angeles Sentinel, Louisville
  Defender, Michigan Chronicle, NY Amsterdam News, Norfolk Journal and Guide,
  Philadelphia Tribune, Pittsburgh Courier, St. Louis American)
  (https://about.proquest.com/en/products-services/histnews-bn).
- Readex *African American Newspapers, 1827–1998* covers smaller-city papers
  (https://www.library.illinois.edu/hpnl/blog/2015/03/).
- The Associated Negro Press (Claude Barnett, 1919–1964) sent releases three
  times a week to nearly all Black papers; releases 1928–1964 survive in
  chronological order, unindexed, in the Barnett papers at the Chicago
  History Museum, microfilmed by University Publications of America
  (https://ibiblio.org/archives-archivists/msg23306.html,
  https://catalog.princeton.edu/catalog/993061683506421). Illinois lists them
  among collections now online (https://www.library.illinois.edu/hpnl/?p=69).
- KU's Spencer Library holds a copy of an ANP "list of newspapers served by
  ANP" (https://archives.lib.ku.edu/repositories/3/archival_objects/398032):
  a client list, which the E&P directory never had.
- The LoC newspaper directory has an ethnicity facet
  (research-notes-directories.md): filter the census for African American
  titles.

Open: did ANP ever distribute crosswords (releases were sorted into news,
features, sports and theater per a 1949 description,
https://nebnewspapers.unl.edu/lccn/2019270505/1949-10-27/ed-1/seq-4.pdf)? Did
Black papers run original puzzles, with bylines, or mainstream syndicated
ones?

## 5. Rhode Island access

Confirmed (library web pages, 2026-10-18):
- **Newport Public Library**: Newspapers.com Northeast Collection (library
  edition, through ProQuest; 800+ titles; excludes the Newport Daily News),
  remote; Providence Journal Historical Archive (NewsBank) 1829–1982, remote;
  ProQuest NYT/LAT/Tribune/WSJ/WaPo from the 1980s only; Readex Rhode
  Island's Historical Newspapers 1732–1921; PressReader (current papers).
  NPL's Community History Archive is digitizing its own Newport Daily News
  microfilm, keyword searchable, currently 1846–1923
  (https://newport.historyarchives.online/home; the site didn't work on
  2026-10-18): 1924–1930 is public domain and the obvious next stretch to ask
  for. https://newportlibraryri.org/resources/databases/
- **Pawtucket Public Library**: Pawtucket Library Digital Newspapers, the
  Pawtucket Times from its own microfilm; pages variously give 1886–1951,
  –1968, –1972 or –1976 online, with a later stretch in-library only.
  Confirm coverage. https://pawtucketlibrary.org/local_history/
- **Providence Journal Historical Archive** is statewide through AskRI, any
  RI library card, including the Evening Bulletin to 1981
  (https://www.askri.org/?p=1904).
- **Providence Public Library and the RI Historical Society** are the state's
  NDNP partners (2019 grant) (https://www.infodocket.com/2021/01/16/rhode-islands-historic-newspapers-now-available-to-search-on-library-of-congress-chronicling-america-website/).
- **URI** (Kingston, Narragansett): open to the public on site; all databases
  searchable from inside the libraries; free Rhode Island Resident card for
  RI residents 18+ (https://web.uri.edu/library/general-access-policies/).
- **Brown**: no walk-in access to Rockefeller or Sciences; building access
  card $75/yr, borrowing card $400/yr; HELIN members' faculty, staff and
  students get free cards with on-site database use at guest stations
  (https://lib.brown.edu/using-library/visiting-library). The John Hay is open
  to the public.

Not confirmed: whether URI or Brown subscribes to ProQuest Historical Black
Newspapers or the ANP releases (Brown's database list blocks automated
lookups).

## 6. Licensing

- ProQuest licenses prohibit systematic downloading to build a collection
  (https://library.missouri.edu/databases/proquestlicense); Georgetown and GMU
  list ProQuest among sources not open to text mining through the normal
  interface. The sanctioned route is ProQuest TDM Studio, which keeps raw
  content inside the tool (https://guides.libraries.emory.edu/main/text-data-mining/purchased);
  Michigan negotiated historical newspaper files
  (https://guides.lib.umich.edu/news/textmining).
- Newspapers.com's terms couldn't be read (the site blocks automated
  fetching). Read them before automating anything there.
- Taking notes while browsing (paper, date, page, credit line) is research;
  an agent driving a logged-in session, or saving page images, is the
  systematic downloading these terms forbid. Public domain status doesn't
  loosen a license.

## 7. Microfilm

- Production scanners scan whole reels fast: nextScan claims up to 2,000
  frames a minute for the Eclipse and 300 for the compact FlexView
  (https://www.datacomit.com.au/our-products/microform-scanners/eclipse,
  https://forefrontec.com/?p=4136).
- Workflow: carriage matrix picks reels; holdings MARC
  (research-notes-directories.md) says who holds them; a person feeds reels;
  the grid detector and content matching find and date the puzzles.
- Scans of public domain reels should go online (Internet Archive, or the
  holding library's own collection), with identifiers that include the LCCN
  and date range. Check for terms on the film itself before uploading.
- Unverified: how freely libraries lend newspaper film by interlibrary loan,
  and what duplicate reels cost.

## 8. Agents

Earlier agent runs gave up after a few web searches, concluding the answer
was in scans they couldn't reach. Web search indexes pages about newspapers,
not the newspapers. What should help: bulk data downloaded once and searched
locally (Chronicling America OCR batches, E&P text); tasks that end in
evidence rows (date, page, URL, credit line) rather than summaries; filing a
lead with the exact title, dates and query when the answer is behind a
subscription; and a separate checker agent that opens each cited page.
