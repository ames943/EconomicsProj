# Feb 11, 1843 Anchor Date -- Primary Source Attempt

Task: try to locate a primary or higher-quality source for the Feb 11,
1843 Gwin/McDuffie Congressional debate that anchors this project's
no-bailout policy signal (see PROJECT_CONTEXT.md, "Confirmed No-Bailout
Reference Date"), which currently rests on two secondary sources only.

**Result: partial progress, not a full resolution.** Found and confirmed
the correct freely-accessible primary-source digitization (no paywall,
no lending restriction), and extracted real corroborating snippets from
it -- but could not get a complete verbatim read of the debate text via
automated tools, due to a bot-check wall on the hosting site. The
existing "two secondary sources, not yet primary-confirmed" caveat in
PROJECT_CONTEXT.md should stay in place, now with this additional
partial corroboration noted alongside it, not replacing it.

## What was tried

1. **congress.gov** (`congressional-globe/page-headings/27th-congress/
   assumption-of-state-debts-mr-gwin/12352`) -- confirms the page-heading
   metadata exists (title "Assumption of State Debts--Mr. Gwin," dated
   Feb 11, 1843) but the actual page content is blocked by a Cloudflare
   challenge for automated access. Tried both the WebFetch tool and a
   direct `curl` request with a standard browser user-agent string --
   both return HTTP 403 with a Cloudflare "Just a moment..." challenge
   page. This matches the exact caveat already recorded in
   PROJECT_CONTEXT.md ("congress.gov blocks automated fetches") -- not a
   new finding, but independently re-confirmed rather than assumed.

2. **archive.org** -- the McGrane book was already flagged as
   lending-restricted. Checked whether the *Congressional Globe itself*
   (rather than McGrane's secondary account of it) might be freely
   available as a periodical scan. Found daily-issue-level records via
   archive.org's search API (e.g.
   `sim_united-states-congress-congressional-globe_1843-02-10_12_16`,
   `..._1843-02-14_12_17` -- Feb 11, 1843 was a Saturday with no
   same-day issue; the debate would appear in the Feb 10 or Feb 14
   issue). However, `archive.org/metadata/<identifier>` returned an
   empty record (`{}`) for these items -- they are indexed but not
   actually retrievable through the public API, consistent with the
   same "sim_" periodical-collection access restriction already
   encountered with McGrane's book. Did not find a way around this.

3. **UNT Digital Library** -- **this is the one genuinely new avenue**,
   not previously tried. Located **Volume 12 of the Congressional Globe**
   (`https://digital.library.unt.edu/ark:/67531/metadc30768/`), described
   by the library itself as covering "December 3, 1842 to March 11,
   1843" -- exactly the 27th Congress, 3rd session window this project
   needs. This is a straightforward university-library digitization with
   **no paywall and no lending restriction** stated anywhere on the item
   page (unlike the archive.org and congress.gov barriers above) -- a
   real, usable primary source in principle.

   **What was confirmed from it:** individual page-image URLs
   (`.../m1/<n>/`) and the site's own full-text search feature
   (`.../hits/?q=...`) are both gated behind an "Altcha" proof-of-work
   CAPTCHA ("Gauging your humanity...") that neither the WebFetch tool
   nor a direct `curl` request could get past -- confirmed on repeated
   attempts against several different page URLs and endpoint patterns
   (`/text/`, `/download/`, `/citation/`), all blocked the same way.
   Only the top-level item description page (no page images, no search)
   rendered successfully.

   **What was recovered anyway, via Google's own search index (not a
   direct fetch of the site):** Google has indexed real OCR'd snippets
   from inside this volume that a direct fetch could not reach.
   Searching for terms tied to this item's identifier turned up:
   - **Page 292** (viewer sequence `m1/308`): snippet confirms **"Mr.
     Gwin was insisting on his motion to go into committee."**
   - **Page 294** (viewer sequence `m1/310`): snippet confirms the
     debate concerned **"a proposition to distribute two hundred
     millions of a stock debt of the U.S. Government among the states,
     to enable them to pay their debts."**

   These are genuine excerpts of the primary-source OCR text (not a
   paraphrase from a secondary source), and they independently
   corroborate two specific things already claimed on secondary-source
   authority in PROJECT_CONTEXT.md: that Senator Gwin was an active
   participant in a floor debate in this exact volume, and that the
   debate concerned a federal assumption/distribution proposal for state
   debts -- consistent with McGrane's and Thomson's secondary accounts.
   The page-numbering offset (viewer index minus 16 = printed page
   number, e.g. `m1/308` = printed p. 292) is noted here for anyone who
   wants to try accessing this volume directly with a real browser later
   -- a human can very likely clear the Altcha challenge in seconds,
   where automated tools cannot.

## What this does NOT establish

- **Not a confirmed exact date match.** The snippets above come from
  pages 292 and 294 of a volume covering Dec 1842-Mar 1843; they are
  consistent with the Feb 11, 1843 dating already claimed, but the
  snippets themselves don't carry an explicit date stamp visible through
  search indexing alone.
- **Not a read of McDuffie's appendix entry.** Multiple targeted searches
  for "McDuffie" against this same volume's identifier returned no usable
  content snippets -- only generic UNT/library search-portal pages.
- **Not a roll-call or vote outcome.** Neither snippet confirms what, if
  anything, Congress actually voted on or decided -- only that the
  assumption/distribution question was actively being debated, which
  again matches (but doesn't go beyond) the existing secondary-source
  narrative.
- **Not independent of the existing secondary sources' framing** -- these
  snippets happened to be found via searches shaped by what McGrane and
  Thomson already claimed; this is corroboration, not a from-scratch
  independent primary read.

## Recommendation

**Leave PROJECT_CONTEXT.md's existing caveat in place, unchanged in
substance** ("corroborated by two independent secondary sources... not
by my own read of the vote tally"), but note this attempt as a real,
if partial, step toward primary confirmation: the correct freely-hosted
volume has now been identified and located to the specific page range
(printed pp. 292-294 or nearby), and two content snippets from inside it
independently support the secondary-source account. **If a primary-source
read still matters for the eventual write-up, the fastest path is a
human visiting
`https://digital.library.unt.edu/ark:/67531/metadc30768/m1/308/` through
`m1/312/` or so directly in a browser** (the Altcha challenge that
blocked automated access here is specifically designed to pass for real
browsers within seconds) -- rather than trying interlibrary loan for
McGrane's book, which was the previously-assumed next step.
