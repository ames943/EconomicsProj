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

## NY General-Obligation Coverage Check (third advisor-cycle work, post S-1320/1370/1560 pick)

**S-1320/S-1370/S-1560 (the maturity-matched GO codes adopted in the
seniority-check decision above) are unusable: zero observations in
1839-1843**, the exact window the analysis depends on most. All three
don't start trading in this file until 1850 (S-1320 has one lone 1830
point, then a 7,172-day gap to 1851). They were picked purely on
name/maturity match against the canal series, without checking date
coverage.

**Replacement: S-1650 "New York 7s, 1849".** Scanned all 47 non-canal-
tagged codes in the S-1140-S-1656 GO range for coverage; S-1650 is by far
the best: 157 total obs, continuous 1842-07-02 to 1848-12-09 (one gap
>90 days), 22 obs pre-signal (Jul 1842-Mar 1843) and 135 post-signal
(Apr 1843-Dec 1848). This is now the **primary NY GO series**, replacing
S-1320/S-1370/S-1560. Tradeoff: it doesn't reach the 1850s.

**Splice to S-1370 for 1850s extension -- evaluated and REJECTED.**
S-1650 (7% coupon, matures 1849) and S-1370 (5% coupon, matures 1860) are
not the same underlying loan -- codebook has no issuance/authorizing-act
data to connect them, and the coupon/maturity mismatch is itself evidence
they're different instruments. Gap between S-1650's last obs (1848-12-09)
and S-1370's first obs (1850-01-12) is 399 days (~13.1 months). Worse:
S-1650 matures in 1849, so its own tail is inside a pull-to-par window
(see below) -- splicing a near-maturity short bond into a long-duration
bond would create an artificial kink at the seam that looks like a credit
signal but isn't. **Decision: no continuous NY GO series past 1848. The
1850s extension is dropped for NY**, not patched over.

## Maturity-Proximity / Pull-to-Par Check (primary-comparison codes)

Checked every primary code for price observations within 12 months of the
bond's own stated maturity, and separately for observations trading past
the bond's stated maturity date entirely (maturity convention: Jan 1 of
the codebook's maturity year, since only a year is given).

**Past-maturity trading (YTM undefined, more bonds than initially found):**
Pennsylvania's S-2240 was flagged first (45 of 420 obs trade past its
1841 nominal maturity, continuing through Sept 1842 -- PA's actual
default month; the bond was never redeemed on schedule). Applying the
same mechanical rule to every code turned up more: **S-2250 (PA, 115 of
548 obs past its 1846 maturity), S-2100 (Ohio, 29 of 519 obs past its
1850 maturity), S-2010 (Ohio, 3 of 167 obs past its 1850 maturity)**.
None of these are data errors -- they reflect real non-redemption, itself
a distress signal -- but YTM cannot be computed for them without a real
redemption date the codebook doesn't give.

**YTM vs. current yield in the near-maturity window -- tested on S-1650's
1847-48 tail (31 of 157 obs, within 12 months of its 1849 maturity):**
switching to YTM does not fix the pull-to-par distortion, it amplifies it.
Pre-1847 YTM std = 0.587; 1847-48 tail YTM std = 2.852 (~5x noisier), and
the final observation (Dec 9 1848, 23 days to maturity) produces YTM =
-8.8%, a formula artifact (near-zero denominator), not a real reading.
Current yield and YTM even *disagree on direction* in this tail (current
yield: 6.641 -> 6.913, +0.27; YTM: 5.555 -> 5.144, -0.41) -- neither
should be trusted uncritically this close to maturity.

**Decision: truncate, don't patch.** YTM is primary wherever computable;
current yield is retained as a diagnostic-only column. Two flags mark
rows to exclude from primary trend analysis (rows are kept in the CSV,
not deleted):
- `excluded_past_maturity`: obs on/after the bond's own maturity date.
  Yield is NOT computed (NaN) for these rows.
- `excluded_near_maturity`: obs within 12 months before maturity. YTM is
  still computed and stored (for transparency) but flagged as unreliable.

**Resulting usable primary-trend date ranges** (after excluding both
flag categories), from `scripts/calculate_yields.py`:

| Code | State | Usable range | Note |
|---|---|---|---|
| S-2240 | Pennsylvania | 1831-07-23 to **1839-08-17** | Contributes nothing to the policy-window test (1841-1848) -- usable data ends entirely within the panic window |
| S-2250 | Pennsylvania | 1831-07-23 to 1842-09-24 | Usable through PA's actual default, not past it -- no post-signal (post-Apr 1843) coverage |
| S-2270 | Pennsylvania | 1831-07-23 to 1843-12-23 | Only PA bond with any post-signal coverage (~8 months past Apr 1843) |
| S-2100 | Ohio | 1827-06-23 to 1843-10-21 | |
| S-2110 | Ohio | 1840-09-30 to 1853-12-14 | |
| S-2080 | Ohio | 1840-08-01 to 1853-12-14 | |
| S-2010 | Ohio | 1827-06-23 to 1848-07-22 | |
| S-0030 | Alabama | 1842-02-19 to 1853-06-18 | current yield only (no maturity data) |
| S-0040 | Alabama | 1842-06-25 to 1851-05-21 | current yield only |
| S-0510 | Indiana | 1843-01-21 to 1848-12-09 | current yield only (maturity is a 25yr term, not anchored) |
| S-0540 | Indiana | 1843-01-21 to 1848-09-16 | current yield only |
| S-1650 | New York (GO primary) | 1842-07-02 to **1848-01-01** | Primary NY series, see above |

**Flag for the write-up / advisor conversation:** of PA's three bonds,
only S-2270 has any usable post-April-1843 coverage, and only ~8 months
of it. S-2240 in particular is dead weight for the actual policy-window
test despite being PA's cleanest pre-default decline story -- it's useful
for the panic-window robustness check, not the primary test.

## calculate_yields.py (built)

`scripts/calculate_yields.py` implements the above: YTM (Hastings
approximation) for PA/Ohio/NY, current yield for Alabama/Indiana, both
truncation flags, current yield always retained as a diagnostic column.
Output: `output/primary_yields.csv` (3,441 rows) --
`date, state, code, price, coupon, yield_measure_used, yield,
current_yield, bucket, series_label, excluded_near_maturity,
excluded_past_maturity`. `series_label` is `"primary"` for all rows;
the canal/robustness comparison (S-1750/S-1820/S-1950 etc.) has not been
built yet -- separate follow-up script.

## Active-Default YTM Override (post-chart-review finding)

While reviewing the three-tier chart set (see below), Pennsylvania's line
spiked to 30-40% YTM. Traced to two distinct sources, only one of which
is legitimate:

- **S-2250 (Jan-Sep 1842):** prices fell 60->37, matching PA's documented
  pre-default collapse. Years-to-maturity was 4-4.7 (not a proximity
  issue). Largely legitimate, EXCEPT the last ~7 obs (Aug 13-Sep 24 1842)
  fall after PA's actual Aug 1 1842 default -- see override below.
- **S-2410 (Dec 1842-Dec 1844):** YTM averaged 30% (vs. ~9.5% current
  yield for the same data) across its ENTIRE usable window (n_years =
  1.0-3.0, outside the 12-month proximity rule). Root cause: YTM assumes
  the bond redeems at full par on schedule. That assumption is unsound
  for PA specifically, which was in active default this whole window and
  had already demonstrated non-redemption (S-2240 traded 631 days past
  its own unredeemed 1841 maturity, see Maturity-Proximity section
  above). This is not a near-maturity noise problem -- it's YTM's core
  assumption failing for a defaulted issuer, at any duration.

**Rule adopted: for any observation date inside a state's active-default
period, use current yield instead of YTM, regardless of years-to-
maturity.** This takes priority over (and supersedes, for those rows)
the near/past-maturity exclusion flags, which exist specifically to
guard YTM's maturity-proximity math -- moot once YTM isn't being used.

**Default periods (web-search-corroborated secondary sources -- same
caveat level as the no-bailout anchor date: not verified against a
primary document):**
- **Pennsylvania: Aug 1, 1842 - Feb 1, 1845.** Suspended its Aug 1842
  interest payment; resumed once 1845 property-tax revenue reached
  $1.318M, with back interest paid. (Consistent with the existing "PA
  Default (Aug 1842)" marker already used in scripts/plot_pa_default.py.)
- **Indiana: Jan 1, 1841 - ongoing through this project's data window.**
  Defaulted January 1841; the 1846-47 Butler Bill restructured the debt
  (ceded the Wabash & Erie Canal to creditors for half; a payment plan
  for the rest) but no clean "resumed normal payment" date was found
  within the analysis window, so Indiana is treated as in default
  through the end of its usable data (Dec 1848).
- **Alabama: NO default period -- Alabama did not default in this
  episode.** Multiple independent sources state Alabama raised direct
  taxation (early 1842) and used state-bank liquidation proceeds to keep
  meeting debt service, unlike PA/Indiana/Maryland/Illinois (temporary
  defaulters) or LA/AR/MI/MS/Florida Territory (outright repudiators).

**IMPORTANT -- open issue, not yet resolved:** Alabama has been carried
in this project's "defaulted" bucket since the very first candidate
scan (see Confirmed Results / Seniority Check sections above), used in
every table, chart legend, and comparison so far. If Alabama genuinely
did not default, that bucket label is wrong, and Alabama's current-yield
treatment is justified *only* by missing codebook maturity data (see
NO_MATURITY_STATES), not by a dual (missing-data + default)
justification the way Indiana now has. This may mean Alabama belongs
closer to New York's "risky but survived" bucket than to PA/Indiana's
"defaulted" one -- a bucket reclassification, not just a yield-formula
detail. NOT yet changed pending review; flagged here so it isn't lost.

**Result after applying the override (221 genuine yield-measure changes,
`scripts/calculate_yields.py`, re-run against `output/primary_yields.csv`):**

| Code | Rows changed | Window | Old (YTM) | New (current yield) |
|---|---|---|---|---|
| S-2240 | 8 (newly un-excluded) | Aug-Sep 1842 | NaN (was past-maturity excluded) | 12.49% (10.4-13.5%) |
| S-2250 | 7 | Aug-Sep 1842 | 33.47% (32.7-34.6%) | 12.79% (12.5-13.5%) |
| S-2270 | 12 | Aug 1842-Dec 1843 | 16.35% (12.2-19.8%) | 10.57% (7.3-13.5%) |
| S-2330 | 93 (~whole window) | Dec 1842-Dec 1844 | 9.64% (7.1-13.1%) | 8.74% (6.3-13.5%) -- modest change |
| S-2410 | 101 (~whole window) | Dec 1842-Jan 1845 | 30.60% (17.4-43.4%) | 9.83% (7.1-14.6%) -- the big one |

PA's post-default yields now cluster in the same 7-15% range as the rest
of the "defaulted" bucket instead of one bond (S-2410) dragging the
state average to 30-40%. `output/primary_yields.csv` now has a
14th column, `active_default_override` (bool). A pre-override snapshot
is saved at `output/primary_yields_before_default_override.csv` for
comparison.

**Stale artifact:** `output/pa_bridge_secondary.csv` (built in the prior
task) still reflects pre-override S-2330/S-2410 values -- needs
regenerating before it's used in any chart.

**Charts NOT yet rebuilt** -- `output/chart_panic_window.png`,
`chart_policy_short_medium.png`, `chart_policy_long_term.png` all still
reflect the pre-override YTM numbers and need to be regenerated once
this is reviewed.

## Alabama Reclassification: Defaulted -> Risky But Survived

Acted on the open issue flagged above. `STATE_BUCKET["Alabama"]` in
`scripts/calculate_yields.py` changed from `"defaulted"` to
`"risky_but_survived"`, with an inline comment marking it **pending
advisor confirmation**. Alabama's current-yield treatment is unchanged
(still justified solely by missing codebook maturity data -- unrelated
to the bucket question). `output/primary_yields.csv`,
`output/pa_bridge_secondary.csv`, and all three charts
(`chart_panic_window.png`, `chart_policy_short_medium.png`,
`chart_policy_long_term.png`) regenerated. Chart legends now show
"Alabama (risky, survived*)" with a footnote explaining the
reclassification; chart 3's title/subtitle updated since it's no longer
a defaulted-vs-safe comparison (Ohio vs. Alabama is now safe vs.
risky-but-survived). Fixed a footnote-wrapping bug in
`build_yield_charts.py` (methodology note was being clipped at the
figure's right edge) while rebuilding.

### Finding: Alabama vs. Ohio, does it pattern as "in between"?

| Year | Alabama | Ohio (safe) | Spread |
|---|---|---|---|
| 1843 | 7.36% | 7.15% | +0.21pp |
| 1844 | 6.20% | 6.13% | +0.08pp |
| 1845 | 7.11% | 6.31% | +0.81pp |
| 1846 | 7.45% | 6.73% | +0.72pp |
| 1847 | 8.22% | 6.22% | +2.00pp |
| 1848 | 8.12% | 6.11% | +2.01pp |
| 1850 | 6.21% | 4.83% | +1.38pp |
| 1851-53 | ~5.5% | ~4.5% | ~+1.0pp |

Alabama opens near-identical to Ohio right after the April 1843 signal,
widens to a genuine ~2pp premium by 1847-48, then narrows but never
fully closes through 1853. This is a clean "persistent but smaller than
the defaulters" pattern -- a good fit for the "risky but survived, lands
in between" bucket.

**Unexpected finding: New York (S-1650) does not show much premium over
Ohio at all.** NY's own yields (5.0-5.6% through 1847, only reaching 7.0%
in its final observed year, 1848) sit at or below Ohio's for most of the
overlap window. On this specific series, NY reads empirically closer to
"always safe" than "risky but survived" -- the qualitative historical
narrative (NY faced real railroad/bank-failure stress) isn't showing up
as a sustained yield premium in S-1650's price data. **Alabama, now
correctly classified, is arguably the cleaner empirical example of the
"in-between" bucket than NY is.** Flag for advisor discussion: worth
checking whether S-1650 is representative of NY's actual risk profile,
or whether NY's stress genuinely didn't transmit to bond pricing the way
Alabama's did.

### Finding: does PA still show elevated post-signal yield after the S-2410 fix?

Yes, but the magnitude changed by more than 6x:
- **Before the active-default override:** PA mean 19.81% vs. Ohio mean
  6.69% (Apr 1843-Dec 1844) -> **13.12pp spread**, dominated by the
  S-2410 YTM artifact.
- **After the override:** PA mean 8.77% (range 6.70-13.31%) vs. Ohio
  mean 6.69% (range 5.62-11.06%) -> **2.08pp spread**.

The persistence claim survives -- PA still shows a real, positive gap
over Ohio in the short/medium term -- but the honest post-correction
story is a modest ~2pp premium, not a dramatic ~13pp one. This is now
roughly the same order of magnitude as Alabama's peak premium (~2pp),
suggesting PA and Alabama sit on the same "moderate default premium"
curve rather than PA being a dramatic outlier. The dramatic-looking
early version of this chart was an artifact of the YTM/default-period
issue, not a real finding -- important to not cite the old 13pp number
anywhere in the writeup.

## Final Chart Captions + Meeting Prep Doc

Added two footnotes not previously present: an `NY_DATA_NOTE` ("New York
(S-1650) GO bond data begins Jul 1842; pre-1842 NY credit risk is not
directly observable in this series") on chart 1 (panic-window) and
chart 2 (policy-short/medium) -- the only two charts that include NY.
Chart 3 doesn't include NY so doesn't need it. Confirmed chart 1 already
carried the PA active-default-pricing note and chart 3 already carried
the Alabama-reclassification-pending note via the shared `METHOD_NOTE`
string -- no additional change needed there beyond what the Alabama
reclassification task already added. All three charts rebuilt in
`scripts/build_yield_charts.py`.

Built `scripts/build_meeting_prep_doc.py` (new dependency: `python-docx`,
added to `requirements.txt`) -- generates
`output/meeting_prep_final.docx`: title, research-question recap tied to
the Lustig "Blue Bonds" motivation, a "what's changed since last
meeting" section leading with the three resolved open items + the two
mid-session findings (active-default YTM fix, Alabama reclassification,
PA's headline-number panic/policy distinction), the three-tier empirical
results with embedded charts and full captions, a headline takeaway
paragraph, a full word-for-word talking-points script, and the four open
items for next phase (1850s extension ceiling, canal/robustness
comparison not yet built, Indiana preferred/deferred tranche test not
yet run, Feb 1843 anchor date still secondary-source-only). No prior
meeting-prep doc existed in the repo to match style against, so the
script was written in a direct, full-sentence style consistent with how
this analysis was conducted. Saved to
`fiscal-history-project/output/meeting_prep_final.docx` and copied to
`~/Desktop/meeting_prep_final.docx` for sharing outside git (no
`/mnt/user-data/outputs` equivalent exists on this machine).

## Advisor / meeting context
- Advisor: Professor George Hall (Brandeis), co-advisor Thomas Sargent (NYU)
- Goal: complete enough of the analysis to bring back concrete results/
  progress for the next advisor meeting
- This is an independent add-on project, separate from my assigned team
  work (Team Texas)
