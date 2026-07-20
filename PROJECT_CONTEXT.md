# Project Context: 1840s State Debt Credibility Test

## Research Question
Did bond markets treat the federal government's refusal to bail out defaulting
states in the early 1840s as a credible commitment? Test this by checking
whether defaulting states faced persistently higher bond yields afterward
compared to states that avoided default, and whether "risky but survived"
states landed in between.

## Background
In the 1830s, US states borrowed heavily from British/Dutch investors to fund
canals, railroads, and banks. The Panic of 1837 crashed state revenues. Nine
states plus Florida Territory defaulted in the early 1840s. The federal
government (Tyler administration) refused to bail any of them out, unlike the
1790 Hamilton assumption of state Revolutionary War debts. This project tests
whether bond markets actually believed that refusal was permanent, using real
price data rather than just historical narrative.

This ties to a March 2026 blog post by Stanford economist Hanno Lustig,
"Blue Bonds for Europe," which argues the EU's current debate over joint
"blue bonds" repeats this exact dilemma, and that credible no-bailout
commitments are what force real fiscal discipline.

## Open Clarifications (raised by advisor)

1. **Before/after framing ambiguity -- RESOLVED.** See "Analysis Windows"
   under Methodology below: the project distinguishes a "panic window"
   (1837 shock) from a "policy window" (the no-bailout signal), and the
   policy window is the primary test.
2. **Exact no-bailout date -- RESOLVED.** See "Confirmed No-Bailout
   Reference Date" below.
3. **Bond seniority not yet controlled for -- RESOLVED.** See "Seniority
   Check" below -- the old NY pick (S-1750/S-1820/S-1950) was a
   revenue-pledged canal bond, mismatched against four general-obligation
   states. A genuine NY general-obligation series was located
   (S-1320/S-1370/S-1560) and now replaces it in the primary comparison;
   the canal bonds (NY, plus Ohio's and Indiana's) are kept as a separate
   secondary/robustness comparison.

## Confirmed No-Bailout Reference Date

**Primary anchor: February-April 1843 (27th Congress, 3rd session;
Tyler administration).**

- **Feb 11, 1843**: Congress held its final substantive floor debate on
  federal assumption of state debts (Congressional Globe, 27th Congress,
  3rd session -- "Assumption of State Debts--Mr. Gwin," plus a companion
  appendix entry "Assumption of State Debts--Mr. McDuffie," Sen. George
  McDuffie of SC, a leading strict-constructionist opponent of assumption).
  This session also produced a congressional report on foreign-held U.S.
  debt: of $279M total, $231M was state (not federal) debt. No assumption
  bill emerged from this session.
- This is distinct from an earlier, weaker episode: in 1839-1840 (26th
  Congress, Van Buren administration, before any state had actually
  defaulted -- the first default was Mississippi, March 1841), a House
  measure linking assumption to distribution of public land-sale proceeds
  passed the House but died before Senate action. National Archives
  Senate records reference this as select-committee file 26A-D18. This
  1840 episode pre-dates the actual defaults and is a precursor, not the
  credible-refusal moment -- do not use it as the anchor date.
- **April-July 1843**: The clearest unambiguous statement of the federal
  position came from the executive branch, not Congress. Christopher
  Hughes, the U.S. consul at the Hague, meeting with a consortium of
  Dutch and British bankers (led by Hope & Co.) demanding that defaulted
  state debts be honored, stated on behalf of the U.S. government that it
  did not "consent, to be held, in any wise, or to any extent,
  responsible for any default, actual or eventual." (Christopher Hughes
  to A. van der Hoop, John Hodshon, and Crommelin, July 10, 1843, Baring
  Papers, Library and Archives Canada.)
- Context: this came after nine states had already defaulted or suspended
  payment (Mississippi, March 1841; Pennsylvania, February 1842) and after
  Secretary of State Daniel Webster's September 1842 Faneuil Hall address,
  which called repudiation "a stain" on the nation but placed the
  responsibility for remedy on the states themselves -- "by 1842 the
  federal government still refrained from direct intervention."

**Recommended single anchor date: February 1843** (the Feb 11, 1843
Gwin/McDuffie floor debate, the last time Congress seriously entertained
assumption), with the April-July 1843 Hughes statement treated as
confirmation of the same policy signal by the executive branch. Both fall
within the 27th Congress, 3rd session, Tyler administration.

**Caveat -- verify before citing in the writeup:** I was not able to read
the original Congressional Globe transcript directly (congress.gov blocks
automated fetches) or the full text of McGrane's book (archive.org copy is
lending-restricted). This date is corroborated by two independent
secondary sources citing McGrane's primary-source research, not by my own
read of the vote tally. If a precise roll-call record matters for the
writeup, pull McGrane via the library (interlibrary loan or JSTOR) or the
Congressional Globe itself (27th Congress, 3rd session, Feb 11 1843 and
the appendix) to confirm.

Sources:
- Reginald McGrane, *Foreign Bondholders and American State Debts* (New
  York: Macmillan, 1935), pp. 21-26 (assumption debate) and pp. 60-79
  (Pennsylvania default).
- David K. Thomson, "'A Disposition to Seize and Divide': A Transatlantic
  Financial Panic over United States State Debt Default in the 1840s,"
  unpublished working paper, Sacred Heart University -- pp. 17, 21-23, 37
  (Hughes quote, Webster speech, congressional foreign-debt report).
- Congress.gov, Congressional Globe, 27th Congress, 3rd session:
  "Assumption of State Debts--Mr. Gwin" (Feb. 11, 1843) and "Assumption of
  State Debts--Mr. McDuffie" (appendix).
- National Archives, Guide to Senate Records, ch. 18: select-committee
  file 26A-D18, "assumption of State debts by the Federal Government"
  (26th Congress, 1839-1841) -- earlier pre-default episode, for contrast.
- Blosser & Levitt, "Federalism and the Problem of State Debts" (Hamilton
  College working paper), pp. 31-32, citing McGrane pp. 24-28, on the 1840
  House vote and its failure to become policy.

## Methodology (current, post-meeting with advisor)
1. Group US states into three buckets:
   - Defaulted (e.g. Pennsylvania, Maryland, Indiana, Illinois, Michigan,
     Arkansas, Mississippi, Louisiana, Florida Territory)
   - Survived but were considered risky (e.g. New York, faced railroad
     bankruptcies and bank failures but never defaulted)
   - Always safe / never seriously at risk
2. Pull raw bond PRICE data (not yield) from the EH.net Early U.S. Securities
   Prices database, since yield isn't directly given, we compute it ourselves
   from price (and known coupon/interest terms per bond).
3. Convert prices to approximate yields (yield ≈ coupon rate / price, needs
   coupon rate info per bond, which may require the codebook or Bayley
   Treasury document for term details).
4. Compare yield trends across the three groups from the 1840s through the
   1850s (extended window per advisor's suggestion, not just 1842-45).
5. Hypothesis: defaulting states should show persistently higher yields
   after default than states that never defaulted; "risky but survived"
   states should land in between.

### Analysis Windows (resolves before/after framing)

Two distinct before/after splits exist in this project and must not be
conflated:

- **Panic window** -- before/after the 1837 economic shock and subsequent
  defaults. Pre-panic: 1835-1837. Post-panic/default: 1841-1845 (spans the
  wave of defaults; Pennsylvania's Feb 1842 default is the marquee case).
  Tests whether the underlying economic shock itself repriced risk,
  independent of any federal policy signal.
- **Policy window** -- before/after the confirmed no-bailout signal
  (Feb-April 1843, see "Confirmed No-Bailout Reference Date" above).
  Pre-signal: 1841-Feb 1843 (states have already defaulted; market doesn't
  yet know whether Congress/Tyler will intervene). Post-signal: April 1843
  onward through the 1850s (federal refusal is now confirmed). Tests the
  actual credibility question -- did yields on defaulted-state bonds
  diverge further, or fail to recover, specifically after the no-bailout
  signal, holding the underlying economic shock constant?

**Primary analysis: the policy window.** The research question is about
the credibility of the federal refusal, not the panic itself, so the main
yield comparison centers on the Feb/April 1843 cutoff.

**Secondary/robustness check: the panic window.** Included to confirm any
post-1843 divergence isn't just a continuation of panic dynamics already
in motion by 1842, rather than something attributable to the policy
signal specifically.

## Data Sources
- EH.net Early U.S. Securities Prices database:
  https://eh.net/database/early-u-s-securities-prices/
  - New York file: https://eh.net/wp-content/uploads/2013/11/New-York.xls
  - Philadelphia file: https://eh.net/wp-content/uploads/2013/11/Philadelphia1.xls
  - Codebook: https://eh.net/wp-content/uploads/2013/11/securities-index.xls,
    saved to data/raw/Securities Index.xls. Maps codes to confirmed security
    names -- resolves the earlier "no legend" gap. Two sheets: "final"
    (clean, 2152 rows: Code | Name | Type | Interest rate | Maturity) and
    "Sheet1" (an earlier draft version of the same mapping).
  - Sheet needed: "U.S. and State Debt"
  - Structure: weekly date rows (~3,148 rows), paired columns per security
    (e.g. S-2420 / S-2420a), state debt columns prefixed "S-", US federal
    debt columns prefixed "US-".
  - Parsing gotcha: New-York.xls splits state debt across two sheets, "NY
    State Debt" and "Other State Debt" (bonds of other states merely quoted
    on the NY market). A bare S-code is ambiguous without knowing which
    sheet it came from -- scripts/parse_securities.py now tags each column
    with its source sheet before concatenating, to avoid misattributing a
    bond to the wrong state.
  - Already confirmed: several S-code columns show a sharp price decline
    from ~90 to ~60 in late 1841, consistent with pre-default risk pricing
    ahead of Pennsylvania's actual August 1842 default.
  - Confirmed code identities so far (via Securities Index.xls):
    - Pennsylvania: S-2240 (5s, r. 1841), S-2250 (5s, r. 1846), S-2270
      (5s, r. 1850)
    - Ohio (candidate for "safe" group, never defaulted): S-2100, S-2110,
      S-2080, S-2010 -- from New-York.xls's "Other State Debt" sheet, not NY
    - Alabama (candidate for "defaulted" group): S-0030, S-0040 -- from
      New-York.xls's "Other State Debt" sheet, not NY
    - Indiana (candidate for "defaulted" group, partial default via the
      1846 Butler Bill): S-0510, S-0540 -- from New-York.xls's "Other State
      Debt" sheet, not NY
    - New York (real, from the "NY State Debt" sheet; candidate for
      "risky but survived"). Two distinct debt series exist in the
      codebook -- see "Seniority Check" below for which one to use:
      - **General-obligation series** ("New York Xs", no "Canal" tag):
        S-1320 (5s, 1850), S-1370 (5s, 1860), S-1560 (6s, 1861) --
        maturity-matched to the canal picks below, PRIMARY set.
      - **Canal series** ("New York Canal Xs", revenue-pledged):
        S-1750 (Canal 5s, 1850), S-1820 (Canal 5s, 1860), S-1950
        (Canal 6s, 1861) -- SECONDARY/robustness set only, do not mix
        with general-obligation comparisons across states.

## Seniority Check (resolves bond-seniority clarification)

Checked Securities Index.xls "Type" column for the original 14 candidate
codes, both sheets -- confirmed "Type" only ever takes two values across
the whole 2,151-row "final" sheet, "Stock" (1,170 rows) and "Bond"
(981 rows). That's a period instrument-form distinction (registered
stock vs. coupon-bearing bond), not a revenue-source/seniority
classification, so it can't answer the seniority question on its own.

**Follow-up: searched the full codebook Name field (not just Type) for
every Pennsylvania/Ohio/Alabama/Indiana/New York entry (327 rows total)
for revenue-pledge earmarking (e.g. "Canal," "Turnpike").** Results:

- **Pennsylvania (41 rows):** No revenue-pledged bonds found. Every state
  entry is a plain "Pennsylvania 5s/6s, r. [year]" -- all general
  obligation. PA has no revenue-pledged bond to compare against.
- **Alabama (11 rows):** Same -- no revenue-pledged bonds found. All
  entries are plain "Alabama 5s/6s [Sterling]" -- general obligation only.
- **Ohio (46 rows):** One revenue-pledged bond exists: **S-2190 "Ohio
  Canal 5s"** (undated/no maturity given). All of Ohio's other 15 state-
  bond codes (including the four already in use, S-2100/S-2110/S-2080/
  S-2010) are plain "Ohio Xs, [year]" with no earmarking -- general
  obligation.
- **Indiana (29 rows):** Multiple revenue-pledged bonds exist, reflecting
  Indiana's actual 1847 "Butler Bill" debt restructuring, which split the
  state's canal-related debt into canal-trustee-held, toll-secured
  tranches: **S-0470 "Indiana Canal"**, **S-0480 "Indiana Canal Deferred
  5s"**, **S-0490 "Indiana Canal Preferred 5s"**, **S-0500 "Indiana Canal
  Special Preferred 5s"**, **S-0506 "Indiana Canal Special Deferred 5s"**.
  The two codes already in use, S-0510/S-0540 ("Indiana Dollar/Sterling
  5s, 25 years"), are the original pre-restructuring general-obligation
  loan -- confirmed general obligation, not canal debt.
- **New York (200 rows):** Two clearly separate series. A plain
  general-obligation series ("New York 5s"/"6s"/etc., S-1140-S-1656, no
  "Canal" tag) and a canal series ("New York Canal 5s"/"6s", S-1660-
  S-1980, all explicitly tagged). The three codes already in use
  (S-1750, S-1820, S-1950) are all from the **Canal** series -- the
  "risky but survived" NY pick was, until now, unknowingly comparing a
  revenue-pledged bond against four general-obligation states.

**So a genuine NY general-obligation bond does exist**, maturity-matched
to the old canal picks: **S-1320 (New York 5s, 1850)**, **S-1370 (New
York 5s, 1860)**, **S-1560 (New York 6s, 1861)**. (Not yet verified for
data completeness in the price files -- do that in calculate_yields.py
before relying on them.)

**Bayley Treasury document -- located and downloaded, but not useful for
this specific question.** Found via web search: the U.S. Census Bureau
hosts Bayley's report as a chapter of the 1880 Census Vol. 7 (a source
already in this file's Data Sources list) at
https://www2.census.gov/library/publications/decennial/1880/vol-07-valuation-taxation/1880v7-06.pdf
-- no paywall or access restriction. Downloaded to
`data/raw/bayley_national_loans_1880.pdf` (and OCR'd companion text at
`data/raw/bayley_national_loans_1880.txt`). However, after extracting
and searching the text: **this document is a history of *federal*
Treasury loans (1776-1880), not a register of individual state bond
security structures.** Its handful of Pennsylvania/Alabama mentions are
about the 1790 assumption debate and the Whiskey Rebellion, not 1840s
state bond seniority. It does not contain canal-toll-vs-general-revenue
detail for any state. Keep it in data/raw/ as useful federal-debt
background, but it does not resolve the seniority question -- that rests
on the codebook Name-field check above plus the Hall & Sargent NY paper
and Wallis/Sylla/Grinath, "Sovereign Debt and Repudiation: The
Emerging-Market Debt Crisis in the U.S. States, 1839-1843" (NBER WP
10753), both already in the reading list.

### Decision

**Adopting option (a): restrict the primary comparison to
general-obligation bonds only, across all states**, now that a genuine
NY general-obligation series has been identified (S-1320/S-1370/S-1560).
This is cleaner than carrying a labeled covariate through every chart.

- **Primary bucket comparison (general obligation only):**
  Pennsylvania (S-2240/S-2250/S-2270, defaulted), Ohio (S-2100/S-2110/
  S-2080/S-2010, safe), Alabama (S-0030/S-0040, defaulted), Indiana
  (S-0510/S-0540, partial default), New York (S-1320/S-1370/S-1560,
  risky-but-survived -- **replaces** the old canal picks).
- **Secondary/robustness comparison (canal/revenue-pledged only, where
  available):** New York Canal (S-1750/S-1820/S-1950), Ohio Canal
  (S-2190), Indiana Canal tranches (S-0480 deferred / S-0490 preferred /
  S-0500 special preferred / S-0506 special deferred). Pennsylvania and
  Alabama have no revenue-pledged bond and are necessarily excluded from
  this secondary comparison. This secondary set also lets us test
  whether canal-vs-canal seniority tranching (preferred vs. deferred)
  within Indiana itself produced a yield gap -- a useful internal
  robustness check independent of the cross-state comparison.
- Going forward, every chart/table should be labeled by which set
  (general-obligation primary vs. canal-secondary) it draws from, so the
  distinction stays visible in outputs, not just in this doc.

- 1880 Census, Vol. 7, Report on Valuation, Taxation, and Public Indebtedness:
  https://www.census.gov/library/publications/1884/dec/vol-07-valuation-taxation.html
  Has a "Public Indebtedness" section by state, useful for debt totals as
  context, not for yields directly.

## Key reference papers (background, not yet used in analysis)
- Hall & Sargent, Pennsylvania working paper (pennsylvania_1820_1860.pdf) -
  budget constraint framework for PA, defaulted August 1842
- Hall & Sargent, New York working paper (new_york_1813_1860.pdf) - budget
  constraint framework for NY, avoided default
- Sargent (2012) - balanced-budget rules as post-crisis credibility restoration
- English (1996), AER - 1840s defaults as sovereign default cost test case
- Kim & Wallis (2005), Economic History Review - transatlantic bond market

## Advisor / meeting context
- Advisor: Professor George Hall (Brandeis), co-advisor Thomas Sargent (NYU)
- Goal: complete enough of the analysis to bring back concrete results/
  progress for the next advisor meeting
- This is an independent add-on project, separate from my assigned team
  work (Team Texas)
