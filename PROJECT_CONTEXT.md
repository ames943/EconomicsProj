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

### 2026-07-28: Resolution of the "~30 cents on the dollar" railroad-bond flag

Followed up on the open flag from the Third Advisor Meeting section (item
1): a source mentioned Alabama paying bondholders roughly 30 cents on the
dollar on railroad-guaranteed bonds, unclear if same episode.

**Resolved: (b) a distinct, later episode -- Alabama's Reconstruction-era
railroad-aid bond crisis, not the 1840s episode this project studies.**
Confident dismissal, not a loose end:

- Alabama's 1867 internal-improvements act had the governor endorse
  railroad bonds ($12,000/mile per qualifying railroad); a Feb. 1870 act
  separately loaned $2M in state bonds to the Alabama & Chattanooga
  Railroad, which defaulted on interest in January 1871 (state seized the
  railroad's property mid-1871). Roughly $18M of these railroad-aid bonds
  were issued/endorsed in total.
- Governor George S. Houston's 1875-76 debt commission (Bethea and
  Lawler) recognized only $18M of claims as legitimate, later cut to
  $12.5M -- against original face claims cited around $30M -- with
  Alabama & Chattanooga bondholders hit hardest. This is consistent with
  (though I could not find an exact primary-source citation for) a
  "~30 cents on the dollar" summary of that reduction for the
  worst-affected bondholders.
- **Directly confirms the two episodes are distinct**, from the same
  Wallis NBER working paper ("Sovereign Debt and Repudiation," WP 10753)
  already cited elsewhere in this file as a source for Alabama's 1840s
  non-default: Wallis explicitly separates "Alabama early in 1842
  re-instituted direct taxation... managed... to meet its debt service"
  (the 1840s episode) from the "postbellum period," when "nearly
  $18,000,000 of railroad aid bonds were issued or endorsed, with the
  repudiated debt remaining at about $13,000,000" (the Reconstruction
  episode) -- two clearly separated paragraphs in the same source, not an
  ambiguous mixed account.
- **No possible date overlap with this project's data window.** Our
  Alabama price series (S-0030, S-0040) run 1842-1853; the railroad-aid
  bonds weren't issued until 1867 at the earliest -- 14 years after our
  data ends. Different instruments entirely (antebellum general-purpose
  state bonds vs. postbellum railroad-endorsement bonds), different
  political era (antebellum panic-era state finance vs. Reconstruction),
  different state government (this project's Alabama is the 1840s
  Democratic-controlled state; the railroad bonds were issued under the
  Reconstruction-era Republican government Houston's commission later
  moved against).
- **Conclusion: not relevant to the Alabama "risky but survived"
  reclassification for the 1840s window.** The reclassification (Alabama
  avoided default in the 1839-43 episode via taxation + bank liquidation)
  stands independent of this later, unrelated railroad-bond history.
  Confidently dismissed -- no further action needed on this flag.

Sources: Wallis, "Sovereign Debt and Repudiation: The Emerging-Market
Debt Crisis in the U.S. States, 1839-1843" (NBER WP 10753) -- already a
project source, and the one that directly resolves this; Encyclopedia of
Alabama, "Congressional Reconstruction in Alabama"; Bhamwiki, "Alabama &
Chattanooga Railroad"; secondary web summaries of the 1867 internal
improvements act and 1876 Houston debt commission (same caveat level as
other web-search-sourced claims in this file -- the exact commission
dollar figures rest on secondary summaries, not a primary reading of the
commission's report itself).

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

## PA Full Bond Re-Scan (34 codes, not just the original 3)

The original 3 PA codes (S-2240/S-2250/S-2270) were a heuristic pick from
the first codebook pass, not the full universe. The codebook actually has
34 PA "State Bond" codes; 27 have price data in Philadelphia1.xls.

Re-scanning all 27 for real post-signal (post-April-1843) coverage turned
up two previously-unused bonds that are now part of PA's primary series:
**S-2330 "Pennsylvania 5s, r. 1859"** (93 obs, Dec 1842-Dec 1844, no gaps
>90 days) and **S-2410 "Pennsylvania 6s, r. 1846"** (177 obs total, usable
window Dec 1842-Jan 1845, no gaps >90 days). Both give native continuous
coverage spanning the April 1843 signal date -- no splice needed -- and
replace S-2270's previous 5 observations / ~1.6 months as PA's only
post-signal data point. `scripts/calculate_yields.py`'s `BOND_SPECS` list
already reflects this (S-2240/S-2250/S-2270/S-2330/S-2410), it just was
never written up here.

**S-2460 bridge (secondary/extended view only, in `scripts/pa_bridge_secondary.py`,
NOT part of the primary series):** "Pennsylvania new annual 5s" starts 7
days after S-2330 ends (Dec 14 1844) and runs clean to Jan 1847, same 5%
coupon as S-2330 (no coupon mismatch). But it's a differently-named
instrument ("new annual" vs. S-2330/S-2410's dated fixed-maturity form) --
the same category of judgment call as the rejected NY S-1650/S-1370
splice below, just with a much smaller gap (7 days vs. 399) and no coupon
mismatch. Treated the same way: kept as a labeled secondary/extended
chart segment (distinct series, gap marked), not folded into PA's primary
persistence line. `pa_bridge_secondary.py` also confirms S-2410 and
S-2460 actually *overlap* by some days -- corroborating they're
independently-traded distinct instruments, not a continuation of the same
loan.

What didn't help, scanned and rejected: S-2260, S-2420, S-2430 (isolated
Feb-Dec 1850 chunks only, same trap as the original bad NY GO codes);
S-2400, S-2450 (almost entirely consumed by their own near/past-maturity
exclusion).

## Coverage Ceiling / Panic-Window vs. Policy-Window Coverage Check (ALL primary bonds)

Recomputed directly from `output/primary_yields.csv` (rows surviving the
near/past-maturity exclusion), counting observations before Feb 11 1843
(pre-signal) vs. on/after Apr 1 1843 (post-signal):

| State | Code | Pre-signal | Post-signal | Post-signal span (mo) | Latest usable obs |
|---|---|---|---|---|---|
| PA | S-2240 | 348 | 0 | -- | 1842-09-24 |
| PA | S-2250 | 433 | 0 | -- | 1842-09-24 |
| PA | S-2270 | 442 | 5 | 1.6 | 1843-12-23 |
| PA | S-2330 | 5 | 81 | 20.2 | 1844-12-07 |
| PA | S-2410 | 6 | 88 | 21.8 | 1845-01-25 |
| Ohio | S-2100 | 464 | 21 | 6.7 | 1843-10-21 |
| Ohio | S-2110 | 45 | 116 | 128.0 | 1853-12-14 |
| Ohio | S-2080 | 75 | 423 | 128.4 | 1853-12-14 |
| Ohio | S-2010 | 159 | 5 | 60.7 (sparse) | 1848-07-22 |
| Alabama | S-0030 | 18 | 140 | 122.3 | 1853-06-18 |
| Alabama | S-0040 | 10 | 9 | 97.4 (sparse) | 1851-05-21 |
| Indiana | S-0510 | 3 | 187 | 68.1 | 1848-12-09 |
| Indiana | S-0540 | 3 | 134 | 65.3 | 1848-09-16 |
| NY | S-1650 | 17 | 117 | 57.0 | 1848-01-01 |

**Bottom line:** full-1850s persistence coverage (dense, trustworthy) only
exists for Ohio (S-2110/S-2080) and Alabama (S-0030). PA (with
S-2330/S-2410 added) supports persistence only to ~Dec 1844/Jan 1845.
Indiana and NY both cap around late 1848. S-2010 (Ohio) and S-0040
(Alabama) technically span long periods but are too sparse (5-9 obs over
5-8 years, post-signal) to trust alone -- see the trade-density
investigation below, which digs into *why* these two are sparse.

## NY Price Investigation -- Why No Measurable Premium? (coverage artifact + genuine partial finding)

Checked S-1650's raw PRICE data directly: it never dips below 99.50 across
its entire observed history (Jul 1842-Dec 1848, 157 obs) -- trades at or
above par the whole time (mean 104.63). Compared to the canal bonds
(S-1750/S-1820/S-1950) over the identical window: those genuinely dip to
78-89 (mean 88.6-101.7).

**Catch:** S-1650 has zero price data before Jul 2, 1842 -- and the canal
bonds' actual troughs (73.5-76) happened *before* that date, entirely
outside S-1650's observed window. S-1650 was never quoted during the
worst of NY's 1839-42 stress, so we cannot know whether the GO bond also
dipped then. **This is primarily a data-coverage artifact, not a clean
"NY was safe" finding.**

Restricting to the identical window S-1650 covers (Jul 1842 onward), a
genuine (if confounded) gap remains: S-1650 never drops below 99.50 even
in the shared window, while all three canal bonds do (73.5-89 min).
Caveat: canal bonds carry toll-revenue risk specific to canal traffic,
distinct from NY's general state creditworthiness -- so this residual gap
may reflect canal-specific revenue risk, not clean evidence about NY's
overall credit. Does not fully rescue "NY is risky but survived" as a
state-level claim.

## Final Three-Tier Chart Structure (built, `output/` directory)

1. **`chart_panic_window.png`** -- all 5 states/buckets, pre-1843, full
   panic collapse-and-recovery story.
2. **`chart_policy_short_medium.png`** -- PA (S-2330+S-2410, ~20-22mo),
   Ohio, Alabama, Indiana, NY (S-1650) -- each truncated to its own real
   coverage ceiling, NY footnoted with the coverage-gap caveat above.
3. **`chart_policy_long_term.png`** -- Ohio (S-2110/S-2080) vs. Alabama
   (S-0030) only -- the two states with genuine decade-long density; PA/
   Indiana/NY explicitly labeled as not having comparable long-run data.

`_clean` versions of all three (built via `scripts/export_charts_no_caption.py`)
strip the footnote/methodology text for slide use; the captioned
originals remain the source of record. `output/pa_bridge_secondary.csv`
was regenerated to reflect post-active-default-override S-2330/S-2410
values after that override was applied (was briefly stale, now fixed).
`scripts/build_meeting_prep_doc.py` builds `output/meeting_prep_final.docx`
embedding all three captioned charts plus a talking-points script, saved
to the repo and copied to `~/Desktop/meeting_prep_final.docx` for sharing
outside git.

## Third Advisor Meeting (outcome)

Presented all of the above (PA re-scan, coverage ceiling, NY price
investigation, three-tier charts, Alabama reclassification). Three items
came out of this meeting:

1. **Alabama reclassification: NOT confirmed at the meeting.** Hall and
   Sargent said they don't know / weren't sure whether Alabama genuinely
   avoided default. STATUS: remains an open hypothesis -- keep the
   "pending confirmation" label everywhere (already in
   `scripts/calculate_yields.py`'s `STATE_BUCKET` comment and all three
   chart footnotes), do not treat as locked in.

   **Post-meeting follow-up (web search):** three independent sources now
   corroborate the reclassification -- Wallis's "Sovereign Default and
   Repudiation" work explicitly states Alabama "had banking problems" but
   did NOT default; a Wikipedia list and a general secondary summary of
   1840s defaulting states (Arkansas, Illinois, Indiana, Louisiana,
   Maryland, Michigan, Mississippi, Pennsylvania, Florida Territory) both
   exclude Alabama. This strengthens the case beyond what was presented at
   the meeting, but the advisors have still not personally confirmed it --
   treat as strengthened-but-still-open, not resolved.

   **Open flag, not yet checked:** a separate source mentions Alabama
   later paying bondholders roughly 30 cents on the dollar on
   railroad-guaranteed bonds. Unclear if this refers to this 1840s episode
   or a different/later one -- needs verification before being treated as
   relevant (or dismissed). Still open as of this writing.

2. **Traded vs. not-traded (bank-held) bonds -- new task, raised at this
   meeting.** Advisors flagged that many states required state-chartered
   banks to hold state bonds as backing for bank notes; a bond held this
   way would show sparse/no market price data for reasons unrelated to
   investor sentiment, which could distort the "market believed X"
   analysis. Candidate bonds flagged at the meeting as already known to be
   unusually sparse: Ohio's S-2010 (post-signal: 5 obs/60.7 months) and
   Alabama's S-0040 (post-signal: 9 obs/97.4 months). Not investigated
   at the time of the meeting -- see the dated investigation section
   below for the follow-up.

3. **New research question from advisors, not yet started:** does
   punishment for state default spill over onto CITY-level bonds
   (Philadelphia, New York City) that didn't themselves default, or did
   the market distinguish city credit from state credit? Requires
   checking whether `Securities Index.xls` / `Philadelphia1.xls` /
   `New-York.xls` contain genuine city-issued (municipal) bond codes
   distinct from the state bonds already in use -- NOT YET CHECKED
   whether this data even exists in the current sources.

**Note on this section:** this write-up (PA re-scan through this
third-meeting outcome) was reconstructed from carried-over session
context after being found missing from the version of this file
committed to git -- the underlying scripts, output CSVs, and charts all
independently confirm the work was actually done, but the documentation
of it apparently never got saved/committed in the prior session. Treat
the narrative above as accurate (spot-checked several of its numbers
directly against `output/primary_yields.csv` and the raw price files
while reconstructing it) but flag if anything here doesn't match your
own recollection of the third meeting.

## Advisor / meeting context
- Advisor: Professor George Hall (Brandeis), co-advisor Thomas Sargent (NYU)
- Goal: complete enough of the analysis to bring back concrete results/
  progress for the next advisor meeting
- This is an independent add-on project, separate from my assigned team
  work (Team Texas)

## 2026-07-28: Trade-Density / Bank-Held Bonds Investigation

Follow-up on Third-Meeting item 2 (traded vs. bank-held bonds). This was
an investigative/flagging pass only -- **no existing output file
(`primary_yields.csv`, `pa_bridge_secondary.csv`, or any chart) was
changed.** New artifact: `output/trade_density.csv` (23 rows: all 14
primary codes + 9 secondary/canal codes, computed ad hoc, not yet backed
by a saved script -- see "not yet done" below).

### Method

For every code currently in the primary series (`calculate_yields.py`'s
`BOND_SPECS`) plus every code in the not-yet-built canal/secondary series
(NY S-1750/S-1820/S-1950, Ohio S-2190, Indiana's five Butler Bill canal
tranches S-0470/S-0480/S-0490/S-0500/S-0506), pulled the raw price series
directly from `philadelphia_state_debt_prices.csv` / `new_york_state_debt_prices.csv`
(pre-truncation, i.e. before the near/past-maturity exclusion flags --
deliberately, since the question here is "was this bond traded at all,"
not "is this row usable for yield"), and computed total observations,
first/last date, span in months, observations/month, and the single
largest gap in days. Cross-checked totals against `primary_yields.csv`'s
per-code row counts -- exact match on all 14 primary codes, confirming
the raw pull is consistent with what `calculate_yields.py` already loads.

### Flagged sparse bonds

Confirmed the two already-known candidates, and found two more that
hadn't been flagged before:

| Code | State | Series | Obs/month | Largest gap | Verdict |
|---|---|---|---|---|---|
| S-0040 | Alabama | primary | 0.18 | 1,467 days (May 1847-May 1851) | Confirmed sparse (already known) |
| S-2010 | Ohio | primary | 0.60 | 1,764 days (Sep 1843-Jul 1848) | Confirmed sparse (already known) |
| **S-1750** | **New York** | **secondary/canal** | **0.36** | **1,666 days (Aug 1843-Feb 1848)** | **NEW flag -- nearly as sparse as S-0040** |
| **S-2190** | **Ohio** | **secondary/canal** | **8.7*** | **7 days (both obs Oct 1825)** | **NEW flag -- only 2 total observations, both from 1825, none in the 1840s-50s at all** |
| S-2110 | Ohio | primary | 1.04 | 2,289 days (Sep 1843-Jan 1850) | Lower-tier flag: sparser than sibling S-2080 (3.14/mo) by ~3x, though not as extreme as the two above |

*S-2190's obs/month figure is an artifact of its 7-day total span (2 obs /
0.2 months) and is meaningless on its own -- the real finding is that it
has no data whatsoever in the 1840s-50s study window. This directly
matters for the still-unbuilt canal/robustness script: S-2190 was the
only candidate Ohio canal bond, and **it cannot be used for this project
at all**, regardless of the bank-held question -- there's no data to
plot. Flagging this explicitly as a proposal, not acting on it: **Ohio
should be dropped from the canal/robustness comparison entirely** (it has
no other revenue-pledged bond -- see Seniority Check above), rather than
represented by 2 data points from a decade before the panic.

Also notable: three of Ohio's four *primary* codes (S-2010, S-2100,
S-2110) show a similarly-timed multi-year quiet stretch starting
Sep-Oct 1843, while the fourth (S-2080, "Ohio 6s, 1860") stays
continuously quoted through the same years. This pattern -- one issue
staying liquid while its same-state siblings go quiet -- looks more like
quoting activity concentrating onto a single benchmark issue than a
uniform bank-absorption effect across all of a state's debt (see
research below on why the timing doesn't fit a bank-holding story for
Ohio specifically).

### Web research: did state law require banks to hold state bonds as note-issue backing?

Findings vary sharply by state -- this is genuinely NOT a uniform 1840s
practice, contrary to the implicit assumption in "many states required
this."

- **New York -- clearly documented, well-timed.** The 1838 Free Banking
  Act required any bank organized under it to purchase specified state
  bonds (or approved mortgages) and deposit them with the state
  Comptroller in exchange for circulating notes -- a bank issuing $90 of
  notes needed to buy and deposit roughly $100 face value of eligible
  bonds. This is the clearest, best-documented mechanism found for any of
  our 5 states, and NY was the first state to adopt it (1838), with only
  Michigan and Georgia also adopting free banking in the 1830s -- most of
  the other ~15 states that eventually followed did so later, in the
  1850s. Timing fits S-1750's observed quiet period (starts Aug 1843,
  5 years after the Act). **Caveat: could not confirm from search results
  whether canal-pledged stocks specifically (vs. general-obligation
  stocks) were on the eligible-securities list** -- the sources describe
  "state bonds" generically. Sources: NBER WP 10654 ("Free Banking and
  Bank Entry in Nineteenth-Century New York"), Richmond Fed *Econ Focus*
  2018 Q1 "When Banking Was 'Free'", EH.net *Antebellum Banking in the
  United States*.
- **Ohio -- a real but smaller, later, and mistimed mechanism.** The
  State Bank of Ohio (est. 1845, the "Kelley Bank Act") required a safety
  fund equal to only 10% of note circulation, in "money or bonds of the
  state or of the United States," deposited with a central board -- much
  smaller in scale than NY's ~100%-collateralized system. Critically,
  **this law postdates the start of Ohio's observed trading gap by about
  two years** (gap begins Sep/Oct 1843; the Act is 1845) -- so it cannot
  explain the *onset* of S-2010/S-2100/S-2110's quiet period, only a
  possible continuation after 1845. This is real evidence *against* a
  clean bank-holding story for Ohio, at least as the sole explanation.
  Source: Ohio History Central, "Kelley Bank Bill of 1845"; Holdsworth,
  *Money and Banking*, ch. 74 ("State-Owned Banks").
- **Alabama -- a different mechanism entirely, doesn't map onto the
  question.** The Bank of the State of Alabama (est. 1823, branches added
  through the 1830s) was capitalized by the *state selling bonds and
  using the proceeds to fund the bank* -- the reverse direction of NY's
  system, where independent banks buy and hold state bonds as backing.
  This doesn't predict reduced open-market trading of Alabama bonds the
  way a note-backing requirement would; if anything it implies more
  bonds were issued/sold, not fewer withdrawn from circulation. It's
  possible the state's own bank held unsold bond inventory internally,
  but that's a different, unconfirmed channel from what the advisors
  asked about, not something found in these sources. Source:
  FindLaw/*Darrington v. Bank of Alabama* (1851), Encyclopedia of
  Alabama, "Banking Industry in Alabama."
- **Indiana -- no mechanism found.** The State Bank of Indiana (chartered
  1834) was half state-owned (state bought half the shares directly with
  cash capital), similar in structure to Alabama's system, not a
  free-banking bond-deposit scheme. Indiana's actual free banking law
  came in 1852, after this project's entire data window. No evidence
  found of an 1830s-40s Indiana requirement for banks to hold state bonds
  as note backing -- moot anyway, since Indiana's primary GO codes
  (S-0510/S-0540) aren't flagged as sparse (2.1-2.8 obs/month, actively
  traded).
- **Pennsylvania -- no mechanism, consistent with no sparse PA bonds.**
  PA did not adopt free banking until 1860, well outside this project's
  window, and maintained a restrictive, case-by-case bank-chartering
  policy up to that point. No PA-specific bond-backing requirement found.
  Consistent with the trade-density check above: none of PA's 5 primary
  codes are flagged sparse. Source: EH.net *Antebellum Banking in the
  United States*.

**Overall caveat, matching this project's existing citation standard:**
all of the above rests on web-search-summarized secondary sources (NBER
working papers, Federal Reserve historical retrospectives, state
historical societies), not a primary-document read of any state's actual
banking statutes or a bank's or Comptroller's actual bond-holding
records. This is the same caveat level as the no-bailout anchor date and
the default-period citations elsewhere in this file -- treat as a
plausible, reasonably well-sourced narrative, not a proven mechanism tied
to these specific bond codes.

### Classification: (a) bank-held / (b) known maturity exclusion / (c) unknown, per flagged bond

Checked whether the near/past-maturity exclusion flags (already used
elsewhere in this project) could explain any of the four flagged bonds'
sparseness. **Answer: no, for all four** -- none of the observed gaps
fall inside a 12-month pre-maturity or post-maturity window:

- **S-0040 (Alabama):** has no maturity year in the codebook at all (see
  `NO_MATURITY_STATES`), so the maturity-exclusion mechanism doesn't even
  apply to it by construction. **(c) unknown**, with a weak, unconfirmed
  circumstantial link to Alabama's state-bank structure (see research
  above) -- not strong enough to call it (a).
- **S-2010 (Ohio):** matures 1850; its near-maturity window would be
  Jan 1849-Jan 1850, but the observed 1,764-day gap (Sep 1843-Jul 1848)
  ends a full 5 months before that window even opens. **(c) unknown**,
  leaning toward the "liquidity concentrated onto S-2080" explanation
  above rather than (a), since the Kelley Act's 1845 date doesn't line up
  with the gap's 1843 start.
- **S-1750 (NY canal):** matures 1850; its entire observed history ends
  Feb 1848, nearly two years before its own near-maturity window would
  open -- the gap is squarely mid-life. **(a) bank-held is the most
  plausible of the three states**, given NY's clearly-documented and
  well-timed 1838 Free Banking Act, though this is circumstantial (timing
  and legal mechanism both fit; no direct record of this specific bond
  sitting in a bank vault was found).
- **S-2190 (Ohio canal):** no maturity year given, and its 2 total
  observations are both from 1825 -- decades before this project's study
  window and before any of the relevant banking law existed. **(c)
  unknown / not applicable** -- this isn't a "thinly traded during our
  window" problem, it's "essentially absent from this data source during
  our window," a data-coverage limit rather than a trading-pattern
  finding.

**Bottom line for the "does sparse data undermine the yield findings"
question:** for Ohio (S-2010) and NY (S-1750), the evidence leans toward
genuine post-1843 illiquidity in specific issues (plausibly, but not
provenly, bank-absorption for NY; more likely a liquidity-concentration
effect for Ohio) rather than a data-processing artifact of this
project's own maturity-truncation rules. Neither S-2010 nor S-1750 are
used as PA/Ohio/NY's sole evidence in any current chart (Ohio's primary
persistence claim rests mainly on S-2080/S-2100/S-2110; NY's rests on
S-1650, not the canal codes) so this doesn't overturn any existing
finding, but it's a real caveat on data quality for the secondary/canal
comparison specifically, which hasn't been built yet.

### Not yet done / open follow-ups from this pass

- `output/trade_density.csv` was generated by an ad hoc script run
  directly, not saved as a `scripts/*.py` file -- if this check needs to
  be reproducible or re-run after new bonds are added, it should be
  turned into a proper script (not done yet, out of scope for this pass
  per instructions to only touch `output/trade_density.csv` and this
  file).
- Did not check whether the *actual* NY Comptroller bond-deposit
  registers (a primary source, not currently in `data/raw/`) could
  directly confirm which specific bonds banks held -- would be the real
  test of the (a) vs (c) classification for S-1750, but wasn't sourced in
  this pass.
- Did not check Ohio's, Alabama's, or Indiana's state banking statutes
  directly (primary documents) -- everything above is secondary-source
  web search, per the caveat.
- The Alabama ~30-cents-on-dollar railroad bond mention (flagged at the
  third meeting) is now resolved -- see the dated note under "Alabama
  Reclassification" above: it's a distinct Reconstruction-era episode
  (1867-76), not relevant to this project's 1840s window.
- The city-bond question (state vs. city credit spillover) from the third
  meeting has now had its scoping check done -- see "City-Level Bonds --
  Scoping Check" below. The comparison itself is still not built.

## 2026-07-28: City-Level Bonds -- Scoping Check

Follow-up on Third-Meeting item 3 (does default punishment spill onto
city bonds that didn't themselves default?). Scoping only -- **no
comparison script or chart was built**, no existing output file was
touched. This required parsing two sheets that `parse_securities.py`
has never touched: Philadelphia1.xls's **"Municipal Debt"** sheet and
New-York.xls's **"City Debt"** sheet (both previously unused -- confirmed
via `xlrd.Book.sheet_names()` that both files have dedicated municipal-
debt sheets, distinct from the "U.S. and State Debt" / "NY State Debt" /
"Other State Debt" sheets already parsed). Both use the same paired
code/code-`a` column layout as the state-debt sheets, prefixed **"C-"**
(codebook `Type` = "Municipal Bond") instead of "S-".

**Answer: yes, genuine city-issued bond codes with real price data exist
-- and for Philadelphia, some are as dense or denser than the state
bonds already in the primary series.**

### Philadelphia (Philadelphia1.xls, "Municipal Debt" sheet)

43 distinct C-codes on this sheet. Filtering the codebook Name field to
entries actually named "Philadelphia" (as opposed to other cities also
sold on the Philadelphia exchange, see below), the strongest candidates
for a like-for-like city-vs-state test:

| Code | Name | Obs | Date range | Note |
|---|---|---|---|---|
| C-1100 | Philadelphia 5s, r. 1846 | 421 | 1835-01-17 to 1844-12-07 | Maturity-matched to state's S-2250 ("Pennsylvania 5s, r. 1846") almost exactly; spans the Apr 1843 signal date with dense coverage on both sides |
| C-1310 | Philadelphia County 5s, old r. 1860 | 369 | 1842-12-31 to 1850-12-28 | Full post-signal coverage into the 1850s |
| C-1300 | Philadelphia County 5s, new r. 1860s | 361 | 1842-12-31 to 1850-12-28 | Same |
| C-1260 | Philadelphia 6s, r. 1852 | 367 | 1840-12-19 to 1850-02-16 | Spans signal date, good density |
| C-1330 | Philadelphia County 6s, r. 1860 | 295 | 1842-12-31 to 1850-02-16 | |
| C-1090 | Philadelphia 5s, r. 1845/6 | 213 | 1831-07-23 to 1847-05-01 | |
| C-1140 | Philadelphia 5s, r. 1850-1872 | 255 | 1844-12-14 to 1850-12-28 | Starts right where C-1100 ends -- a possible bridge, same category of judgment call as PA's own S-2410/S-2460 bridge |

C-1100 in particular is directly comparable in density to PA's own
primary bonds (S-2330: 93 obs / S-2410: 177 obs over similar windows) --
**Philadelphia the city was, if anything, more actively quoted than
Pennsylvania the state** in this exact window, which is itself a
suggestive data point (a city untouched by its state's default kept
trading busily) worth noting even before building the formal comparison.

Note: `C-1015` ("Philadelphia City" -- the one codebook entry literally
matching that name from the earlier keyword search) has **zero price
data** in either the Municipal Debt sheet or anywhere else checked -- a
codebook-only listing. The real usable Philadelphia city bonds are the
"Philadelphia [5s/6s], r. [year]" and "Philadelphia County [5s/6s]"
series above, found by scanning the sheet's actual columns rather than
by keyword-matching the codebook Name field alone -- the keyword search
alone would have wrongly concluded Philadelphia had no usable city bond.

**Bonus finding:** this same sheet also carries other cities' bonds sold
on the Philadelphia exchange, already downloaded, no extra file needed:
**Cincinnati 6s (C-0436, 351 obs, Dec 1842-Dec 1850)** and **Pittsburgh
6s (C-1394, 350 obs, Dec 1842-Dec 1850)** are both dense and span the
policy window well. (Allegheny City/County, St. Louis, Nashville, and a
second New Orleans series are also present but short/sparse -- mostly a
single isolated 1850 window each.) Cincinnati is notable as an
in-state comparison point for Ohio (our "safe" bucket).

### New York City (New-York.xls, "City Debt" sheet)

70 distinct C-codes, covering New York City Corporation bonds, NYC water/
fire loan bonds, Brooklyn bonds, and one Jersey City entry. Density is
much thinner and choppier overall than Philadelphia's -- most codes have
under 20 scattered observations -- but several usable candidates exist:

| Code | Name | Obs | Date range |
|---|---|---|---|
| C-0698 | New York City 5s, Water Loan, 1870 | 147 | 1843-01-07 to 1853-11-30 |
| C-0695 | New York City 5s, Water Loan, 1858 | 123 | 1843-01-21 to 1853-11-16 |
| C-0696 | New York City 5s, Water Loan, 1860 | 98 | 1843-10-07 to 1853-12-24 |
| C-0660 | New York City 7s, 1857 | 79 | 1843-01-21 to 1852-08-11 |
| C-0650 | New York City 7s, 1852 | 68 | 1843-01-21 to 1852-04-03 |
| C-0320 | Brooklyn 6s | 55 | 1843-02-11 to 1853-06-18 |

All six start right around the policy signal (Jan-Oct 1843) and run well
into the 1850s -- genuinely usable, though none match Philadelphia's
C-1100 for pre/post-signal density on both sides of the April 1843 cutoff
specifically (most NYC candidates only start quoting *at or after* the
signal, so they can't support a pre/post-signal comparison the way
C-1100 can -- only a post-signal levels/trend comparison).

### Other city files (Baltimore, Boston, Charleston, New Orleans, etc.)

**Not checked -- not currently downloaded.** Per the Data Sources list,
only `New-York.xls`, `Philadelphia1.xls`, and `Securities Index.xls` are
actually present in `data/raw/`; the other EH.net city files are listed
as "available if needed" from the source site but were never fetched.
Given Philadelphia1.xls's Municipal Debt sheet already yields a usable
Philadelphia-vs-Pennsylvania pair (plus bonus Cincinnati/Pittsburgh data)
and New-York.xls's City Debt sheet yields a usable NYC/Brooklyn set, a
first city-vs-state comparison doesn't require downloading anything new.
Downloading additional city files (e.g. Baltimore, which would let a
Maryland state-vs-city comparison), would be a separate future step, not
done here since it wasn't necessary to answer the scoping question and
wasn't asked for in this pass.

## 2026-07-28: Philadelphia (City) vs. Pennsylvania (State) Yield Comparison

Built the first city-vs-state comparison (Third-Meeting item 3), scoped
narrowly to Philadelphia vs. Pennsylvania only -- Cincinnati, Pittsburgh,
and NYC/Brooklyn deliberately NOT included in this pass (see Next Steps).
New outputs: `output/city_vs_state_yields.csv` (1,843 rows: 1,422
Pennsylvania-state + 421 Philadelphia-city) and `output/chart_city_vs_state.png`.
No existing file was modified. As with the trade-density pass, this was
computed via an ad hoc script, not saved to `scripts/` -- see Next Steps.

### Step 1 finding, before anything else: C-1100 has a critical internal gap the earlier scoping check missed

The prior scoping-check pass reported C-1100 as "421 obs, 1835-01-17 to
1844-12-07... dense coverage on both sides" of the Apr 1843 signal. That
was true of the overall date *range* but wrong about *density inside it*
-- exactly the kind of mistake this project has hit before with code
picks (see PA/NY re-scan history). Checking gaps directly (mirroring
`calculate_yields.py`'s methodology) found a **343-day gap, Feb 25 1843
to Feb 3 1844** -- C-1100 has **zero observations for the entire
immediate post-signal period** (Apr 1843 through Jan 1844). Its only
other gap over 90 days is this one; everything else is dense.

**Maturity check (also step 1):** C-1100 matures 1846 (codebook: coupon
5%, maturity 1846); its near-maturity window would be Jan 1845-Jan 1846
and past-maturity on/after Jan 1846. The bond's entire observed range
ends Dec 1844, a full year before either window opens -- **no
near/past-maturity truncation applies at all**, cleanly, unlike several
of PA's own state bonds.

**Active-default override check (also step 1) -- confirmed NOT needed.**
Web search found no record of the City of Philadelphia (as a government
distinct from the Pennsylvania state government) suspending interest
payments in this era -- only the state's 1842 default is documented
anywhere. The price data itself corroborates this directly: C-1100 only
dips from ~99 (1841) to a 91-94 range (late 1842-early 1843) -- a mild
~6-8% decline -- then fully recovers to 101-104.5 by 1844, actually
*above* its 1841 level. Nothing resembling PA state's collapse to the
37-40 range. **No override applied; current yield is used throughout
for a different reason -- see below.**

### Method: current yield for both sides, not YTM, and here's why

The task instruction was to match "the same method/conventions as the
existing primary series," specified as current yield. This isn't a
simplification -- it's actually the correct apples-to-apples choice
given how PA's own numbers already work: PA's entire usable post-signal
window (S-2330/S-2410, Dec 1842-Jan 1845) falls **inside** PA's own
`DEFAULT_PERIODS` window (Aug 1842-Feb 1845), so `calculate_yields.py`
already computes ALL of PA's post-signal comparison points using current
yield via the active-default override, not YTM. Computing YTM for
Philadelphia while PA is on current yield would have reintroduced
exactly the yield-measure mismatch this project flagged and fixed for
Alabama/Indiana. Current yield for both sides is therefore genuine
methodological parity for this specific comparison, not a shortcut.

### Result

**Matched-window pre-signal (1835-01-17, Philadelphia's first obs,
through Mar 31 1843):**
| Entity | Mean yield | n |
|---|---|---|
| Pennsylvania (state) | 6.69% | 337 |
| Philadelphia (city) | 5.06% | 380 |
| **Spread** | **1.63pp** | |

**Post-gap overlap window (Feb 3 1844-Dec 7 1844, the only period both
series actually have data -- true apples-to-apples, n=41 each side):**
| Entity | Mean yield | n |
|---|---|---|
| Pennsylvania (state) | 7.56% | 41 |
| Philadelphia (city) | 4.88% | 41 |
| **Spread** | **2.68pp** | |

For context, PA's own broader post-signal average (Apr 1843-Jan 1845,
n=88, including the period Philadelphia has no data for) is 8.76%,
giving an 8.76% vs. 4.88% (n=41) = **3.88pp** spread if compared without
matching windows -- included for reference but the 2.68pp matched-window
figure above is the fair number, matching this project's established
practice of not comparing series over mismatched windows (see the NY
S-1650-vs-canal coverage-window discussion elsewhere in this file).

**Reading:** the state-city gap widens from 1.63pp to 2.68pp across the
signal, but the widening is driven almost entirely by Pennsylvania's own
yield rising (6.69% to 7.56%), not by Philadelphia's yield moving at all
(5.06% to 4.88%, essentially flat, if anything very slightly lower).
This is a clean **no-spillover** finding for this one city-state pair:
Philadelphia's own borrowing cost shows no reaction to either the state's
Aug 1842 default or the Apr 1843 no-bailout signal, while the state's
cost climbed and stayed elevated around it, in line with the state-level
persistence finding already established for PA elsewhere in this file
(the "PA still shows elevated post-signal yield after the S-2410
correction" finding -- Philadelphia looks like an *outside* observer of
that story, not a participant in it.

**Important limitation, stated plainly per the task instructions:** the
343-day data gap sits almost exactly on top of the immediate post-signal
period, so **the city's immediate reaction to the Apr 1843 signal itself
cannot be observed at all** -- this result only speaks to "was the city's
credit still normal by Feb-Dec 1844," a level check about a year later,
not a reaction-speed test. And this is **one city vs. one state** --
Cincinnati, Pittsburgh, and NYC/Brooklyn were deliberately excluded from
this pass per the task scope and remain open, unverified candidates
(flagged in the prior scoping-check section) -- this finding should not
yet be read as "cities in general were insulated from state default,"
only as "in this one case, Philadelphia specifically was."

### Not yet done

- No script was saved for this comparison (parsing + yield calc +
  chart were all done ad hoc, matching how the trade-density pass was
  handled) -- would need `scripts/city_vs_state_yields.py` if this needs
  to be reproducible or extended to other city/state pairs later.
- Cincinnati vs. Ohio, Pittsburgh vs. (no direct state analog -- it's in
  Pennsylvania too, a second PA city comparison point), and NYC/Brooklyn
  vs. New York state are all still open, per the prior scoping check.
- Did not re-verify whether other Philadelphia city bonds (C-1310/
  C-1300/C-1260, flagged in the scoping check for 1850s reach) have the
  same kind of hidden internal gap C-1100 had -- worth checking before
  using them to extend this comparison past 1844.

## Immediate Next Steps (current, supersedes all earlier "next step" sections)

1. If extending the city-vs-state comparison: check C-1310/C-1300/C-1260
   (Philadelphia County bonds, flagged for 1850s reach) for internal gaps
   the same way C-1100 was just checked -- don't assume density from
   total-obs-and-date-range alone, that undercounted C-1100's real gap.
   Cincinnati (C-0436) vs. Ohio state, and NYC/Brooklyn vs. New York state
   (S-1650), are both still open and unstarted.
2. If pursuing the bank-held question further: source NY Comptroller
   bond-deposit registers (primary document) to directly test whether
   S-1750 specifically was bank-held, rather than relying on the
   circumstantial timing/legal-mechanism argument in the trade-density
   section above. Same for Ohio's state banking statute text, to check
   whether it names eligible bond series explicitly.
3. Canal/robustness comparison script (S-1750/S-1820/S-1950 for NY, plus
   Indiana's Butler Bill preferred/deferred tranches) still NOT built as
   a standalone script. Per the trade-density pass's finding, **build it
   without Ohio's S-2190** (no usable-window data) rather than including
   it as a token/placeholder -- needs a decision confirmed with advisors
   first, since it changes the shape of the canal-comparison chart from 3
   states to 2.
4. Feb 11 1843 anchor date still rests on two secondary sources only --
   not yet verified against a primary document (Congressional Globe
   transcript, McGrane's book).
