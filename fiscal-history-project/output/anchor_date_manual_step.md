# Feb 11, 1843 Anchor Date -- Manual 2-Minute Verification Step

This is a genuine "human needs 2 minutes" task, not a real blocker. Every
automated route was retried this pass (8 distinct hosts/methods) and each
one hits either a CAPTCHA/Cloudflare bot-check, or an access-restricted
metadata record -- none of which a script can solve, all of which a human
browser clears automatically. Full retry log below; **jump to "What to
actually do" if you just want the fast path.**

## What to actually do (pick either route, both take under 2 minutes)

**Route A -- UNT Digital Library (already-located pages, fastest):**
Open these two URLs in a normal browser (the "Gauging your humanity..."
challenge that blocks automated tools resolves itself in a couple of
seconds for a real browser -- no action needed beyond waiting):
- `
/` --
  printed page 292, already confirmed (via Google's search index, see
  `output/anchor_date_source_check.md` from the prior pass) to contain
  "Mr. Gwin was insisting on his motion to go into committee."
- `https://digital.library.unt.edu/ark:/67531/metadc30768/m1/310/` --
  printed page 294, already confirmed to contain "a proposition to
  distribute two hundred millions of a stock debt of the U.S. Government
  among the states, to enable them to pay their debts."

Read pages 292-296 (`m1/308` through `m1/312`) for the full Gwin debate
text and to see whether a vote or resolution is recorded. This is Volume
12 of the Congressional Globe, confirmed to cover Dec 3 1842-Mar 11 1843
-- exactly the 27th Congress, 3rd session window this project needs.

**Route B -- Google Books direct PDF download (new this pass, no
CAPTCHA at all, but the exact volume ID needs a human to find):**
This pass discovered that Google Books hosts direct, unrestricted PDF
downloads of Congressional Globe volumes (confirmed working: fetched a
305MB, 1,445-page PDF with zero bot-check). The one wrinkle is that an
automated text search couldn't reliably identify the correct volume ID
among many similarly-titled Congressional Globe volumes -- a first
attempt (`id=Kvre2Nur8z8C`) turned out to be the wrong Congress entirely
(40th Congress, 2nd session, 1867-68, confirmed by searching its text for
"Gwin" -- zero real matches, only unrelated "Gwinnett county" hits).
**To do this yourself:** go to `books.google.com`, search `Congressional
Globe twenty-seventh congress third session 1843`, open the correct
volume (check the "About this book" page for the date range before
committing), then use the "Download PDF" link on that page (URL pattern:
`books.google.com/books/download/The_Congressional_Globe.pdf?id=<ID>&output=pdf&sig=<SIG>`)
-- it downloads instantly with no login and no CAPTCHA. Once downloaded,
`pdftotext` + `grep -i "Gwin\|McDuffie\|assumption"` gets you the full
text search this project's automated tools couldn't do on the
CAPTCHA-gated sites.

## What I could NOT get past automated tools (full retry log, for the record)

1. **congress.gov** -- Cloudflare 403 challenge, confirmed again on both
   WebFetch and direct `curl` with a real browser user-agent string.
2. **archive.org, "sim_" periodical scans** (e.g.
   `sim_united-states-congress-congressional-globe_1843-02-10_12_16`) --
   indexed and findable via search, but the public metadata API returns
   an empty `{}` record -- access-restricted, not a transient error
   (confirmed on 6 repeated attempts with delays).
3. **archive.org, Google-Books-sourced scans** ("bailgoog" identifiers,
   e.g. `congressionalgl31bailgoog`) -- same empty-metadata restriction as
   above, confirmed on a sibling volume (`congressionalgl32bailgoog`) too
   once transient 502 "servers busy" errors were ruled out with retries.
4. **UNT Digital Library** -- both direct page URLs and the site's own
   full-text search are gated behind an Altcha proof-of-work CAPTCHA;
   confirmed blocked on repeated attempts against multiple endpoint
   patterns (`/m1/<n>/`, `/hits/`, `/text/`, `/download/`, `/citation/`).
   The one page that DID render for automated tools was the top-level
   item description (no page content) -- this is how the volume was
   confirmed to be the right one (Dec 1842-Mar 1843) without seeing its
   actual text.
5. **HathiTrust** (`catalog.hathitrust.org`) -- Cloudflare 403, same
   pattern as congress.gov, on both WebFetch and direct `curl`.
6. **Google Books web UI, direct search** -- the search-results page
   loads via JavaScript that a non-browser fetch can't execute; no
   snippet text or volume IDs were recoverable this way.
7. **Google Books official API** (`googleapis.com/books/v1/volumes`) --
   returned HTTP 429, "Quota exceeded... Queries per day... quota_limit_
   value: 0" -- a hard daily quota ceiling for unauthenticated requests
   from this environment, not something a retry fixes.
8. **The Online Books Page** (`onlinebooks.library.upenn.edu`) -- a
   legitimate curated free-book index, but its entry for the
   Congressional Globe just links onward to HathiTrust (blocked, see #5)
   rather than hosting the text itself.

**Net finding, same as last pass:** every host either blocks automated
access outright (Cloudflare, Altcha) or returns an access-restricted
record that looks findable in search results but isn't actually
retrievable (archive.org's two restricted collections). None of this is
a dead end for a human -- it's specifically an automation barrier. The
existing PROJECT_CONTEXT.md caveat ("corroborated by two independent
secondary sources... not by my own read of the vote tally") should stay
in place until one of the two routes above is completed by hand.
