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

**Caveat, updated 2026-08-17 -- now partially primary-source confirmed.**
Automated tools could not read the original Congressional Globe
transcript directly (congress.gov blocks automated fetches) or the full
text of McGrane's book (archive.org copy is lending-restricted), but
Amey manually accessed Google Books' scan of Volume 12 (27th Congress,
3rd session) and read a real, on-topic House floor debate -- "Mississippi
State Bonds," involving Gwin (MS), Granger (Whig-NY), and Thompson (MS)
-- disputing the legality of Mississippi's Union Bank bonds and calling
on the President for correspondence on the debt's recognition, sitting
8-9 printed pages before an already-confirmed Feb 16 1843 page. See
"2026-08-17 (final prep pass): Feb 11 1843 Anchor Date -- RESOLVED" below
for the full read and participant verification. **This is not a pinpoint
date confirmation** -- neither page carries a visible date stamp, so Feb
11 specifically (vs. an adjacent session day of the same multi-day
dispute) is not 100% pinned -- but it upgrades the citation from
"secondary sources only" to "secondary sources plus a real, on-topic
primary-source read of the right participants and subject in the right
tight date window." Cite with this exact caveat, not as a fully pinned
roll-call date.

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

[Count note, added 2026-09-02: the per-state figures below (41 + 11 + 46
+ 29 + 200) sum to 327, but there are 326 *distinct* codebook rows --
`B-1186` "Ohio and Pennsylvania" is a railroad corporate bond whose name
matches two of the state strings, so a naive per-state tally double-counts
it. It is not a state bond and does not affect the seniority
conclusions.]

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
Output: `output/primary_yields.csv`. Columns as first built:
`date, state, code, price, coupon, yield_measure_used, yield,
current_yield, bucket, series_label, excluded_near_maturity,
excluded_past_maturity` (12 columns; a 13th, `active_default_override`,
was added later -- see the Active-Default YTM Override section below).
`series_label` is `"primary"` for all rows; the canal/robustness
comparison (S-1750/S-1820/S-1950 etc.) has not been built yet -- separate
follow-up script.

**Row count -- 3,711 (verified 2026-09-02, `wc -l` minus header /
`len(pd.read_csv(...))`).** This section originally said "3,441 rows,"
which was correct *at the time it was written*, when `BOND_SPECS` held 12
codes (PA: S-2240/S-2250/S-2270; Ohio: S-2100/S-2110/S-2080/S-2010;
Alabama: S-0030/S-0040; Indiana: S-0510/S-0540; New York: S-1650). The
later "PA Full Bond Re-Scan" (commit `5519087` "pa bridge") added two
Pennsylvania codes to `BOND_SPECS` -- **S-2330 (93 rows) and S-2410 (177
rows), +270 rows total** -- and this one sentence was never updated to
match. 3,441 + 270 = 3,711 exactly; confirmed by grouping the current
CSV by code (`total minus S-2330 and S-2410 = 3,441`). This was not a
data-quality problem, a copy-paste error, or a broken pipeline -- it was
a stale descriptive figure left behind by a later, separately-documented
expansion of the bond set. Every downstream number that draws on this
file has been re-verified against the 3,711-row version and is correct.
`output/primary_yields_before_default_override.csv` has the same 3,711
rows (the override changed yield *values* on 221 rows, not the row
count).

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
| 1843 | 8.23% | 8.18% | +0.05pp |
| 1844 | 6.20% | 6.13% | +0.08pp |
| 1845 | 7.11% | 6.31% | +0.81pp |
| 1846 | 7.45% | 6.73% | +0.72pp |
| 1847 | 8.22% | 6.22% | +2.00pp |
| 1848 | 8.12% | 6.11% | +2.01pp |
| 1850 | 6.21% | 4.83% | +1.38pp |
| 1851-53 | ~5.5% | ~4.5% | ~+1.0pp |

**1843 row corrected 2026-08-25** (was 7.36%/7.15%/+0.21pp): the original
figures did not reproduce from `primary_yields.csv` using the same
methodology that exactly reproduces every other row in this table
(full-calendar-year, date-grouped mean of the project's official `yield`
column -- YTM for Ohio, current yield for Alabama). Root-caused: the
1843 row was computed with a different, inconsistent methodology (most
likely Ohio's raw `current_yield` column rather than the blended
YTM-based `yield` column that every other year correctly uses, plus
possibly a narrower date window rather than the full calendar year) --
confirmed by testing that 1843 is the ONLY row that fails to reproduce
with the standard method (all 6 other years match to within 0.05pp), and
that 1843 is specifically the year Ohio's bond prices sat furthest from
par (mid-panic-recovery), which is exactly when YTM and current yield
diverge most -- making a stray use of the wrong column invisible in
every other year but visible here. The exact original computation (down
to the hundredth of a percent) could not be pinned further than that;
see "Alabama-vs-Ohio 1843 Discrepancy -- Root-Caused" below for the full
investigation. Corrected to the standard, consistent methodology:
**Alabama 8.23%, Ohio 8.18%, spread +0.05pp** -- if anything this makes
the "opens near-identical" claim in the paragraph below even more
literally true than the original (mistaken) 0.21pp figure did.

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

## 2026-07-30: Advisor Framing -- City Contagion Question

Advisor (Hall) articulated the city-spillover question -- already open as
item 1 in the prior "Immediate Next Steps" (Cincinnati/Pittsburgh/NYC
extension) -- more sharply, using a contagion/illness framing: state
default is like a disease that "spreads" to neighboring states' bond
prices via elevated yields, but the open question is whether it also
spreads downward to the defaulting state's own city -- does Philadelphia
get punished along with Pennsylvania, or does the market distinguish city
credit from state credit even when it's the same place?

The Philadelphia-vs-Pennsylvania comparison already built in this project
(C-1100 vs. PA state bonds, see "Philadelphia (City) vs. Pennsylvania
(State) Yield Comparison" above) is a direct empirical answer to this
question, not just adjacent work -- should be framed that way explicitly
to Hall/Sargent at the next meeting: the existing no-spillover finding for
Philadelphia IS the answer to "why didn't it spread to the city."

Advisor also mentioned, in the same meeting, that Ohio (never defaulted,
bucketed "Safe") "saw yield rise during the 1840s" -- floated as possible
evidence of contagion reaching even the Safe bucket. Flagged as
UNVERIFIED pending a finer-resolution check against the existing yearly
snapshots (which show Ohio's yield *declining* over the medium/long run:
1843 7.15% -> 1845 6.31% -> 1847 6.22% -> 1848 6.11% -> 1853 4.44%) --
see resolution immediately below.

## 2026-07-30: Ohio Yield-Rise Check -- RESOLVED (real move, wrong window for contagion)

Investigated the advisor's comment above using
`output/ohio_yield_check.csv` (560 dated observations, 1839-1848, all
four Ohio primary codes: S-2100, S-2110, S-2080, S-2010), read directly
off `primary_yields.csv` -- no existing file modified, this was a
read-only pass.

**Finding: the rise is real, but it's the 1837 panic, not the 1843
policy signal.** All four Ohio bonds show a synchronized price collapse
from ~90 (Oct 1841) to ~48-52, bottoming in a tight four-week window,
Mar 12 - Apr 9 1842. Peak yields: S-2100 16.02% (Mar 26 1842), S-2010
15.85% (Apr 9 1842), S-2110 12.83% (Mar 12 1842), S-2080 11.48% (Mar 12
1842). Confirmed as a genuine price move, not a YTM/maturity artifact --
none of these rows carry near-maturity, past-maturity, or
active-default-override flags, and all four bonds had 8-18 years left to
maturity at the time.

**Timing rules out the policy-contagion story.** The spike bottoms ~4.5
months BEFORE PA's actual default (Aug 1842) and ~11 months BEFORE the
Feb 11 1843 no-bailout signal. Yields hold elevated (9-12.6%) through
late 1842 into early 1843, then fall back to a 6-7% baseline starting
May 1843 -- i.e. Ohio's yields were already normalizing by the time the
policy signal happened, the opposite of what policy-driven spillover
into the Safe bucket would predict.

**Verdict**: this is the same general 1837-42 panic-window credit crunch
already documented elsewhere in this file (see "Key finding, Ohio vs.
Alabama/Indiana" -- Ohio dips hard through 1842, fully recovers by 1844),
not a new policy-signal contagion effect. Reads as the advisor
conflating the panic-window and policy-window episodes -- a conflation
risk this project already explicitly flagged for itself (see "Resolved
Clarifications," point 1, before/after framing). Does NOT support
treating Ohio as a new "Safe bucket shows spillover" data point.

STATUS: Ohio yield-rise claim -- RESOLVED. Real panic-window move, not
policy-window contagion. Correct/clarify with Hall at the next meeting --
useful in that it shows the panic-vs-policy framing distinction is doing
real analytical work, not just a bookkeeping split.

## 2026-08-17: Cincinnati and Pittsburgh City-vs-State Comparisons

Extends the Philadelphia-vs-Pennsylvania comparison to the two other city
bond series flagged as usable in the "City-Level Bonds -- Scoping Check"
section. New script: `scripts/compare_city_vs_state_cincinnati_pittsburgh.py`
(does not touch `scripts/compare_city_vs_state.py` or any existing
output). New outputs: `output/city_vs_state_cincinnati.csv`,
`output/city_vs_state_pittsburgh.csv`, `output/chart_cincinnati_vs_ohio.png`,
`output/chart_pittsburgh_vs_pa.png`.

**Correction to how this task was framed: Pittsburgh compares against
Pennsylvania, not Ohio.** The task that requested this work described
both cities loosely as comparing to "Ohio's S-2100/S-2110/S-2080/
S-2010" -- but Pittsburgh is a Pennsylvania city, not an Ohio one (this
was already flagged as an open question in this file's prior Not-Yet-
Done list). Per the task's own stated principle -- compare each city
against its own state -- Cincinnati is compared to Ohio and Pittsburgh
is compared to Pennsylvania, a second PA city-vs-state test, not a
second Ohio one.

**Density check, done properly this time (per the C-1100 lesson --
total obs/date-range alone is not enough, check internal gaps):** both
C-0436 (Cincinnati 6s) and C-1394 (Pittsburgh 6s) have dense, gap-free
post-signal coverage (largest gap 63 days each) running from Dec 1842
through Dec 1850 (339/338 obs respectively). But BOTH have only **5
pre-signal observations each**, all within the six weeks immediately
before the Feb 11 1843 cutoff (Dec 31 1842-Jan 28 1843) -- neither
supports a Philadelphia-style pre/post divergence test. This is
structurally the same situation already flagged for the NYC/Brooklyn
candidates, not a repeat of Philadelphia's case. Both comparisons are
therefore **post-signal LEVELS comparisons only**, not pre/post
divergence tests -- stated explicitly rather than forcing a verdict from
thin pre-signal data.

Neither coupon has a codebook maturity date (same situation as Alabama/
Indiana's primary codes) -- both cities always use current yield, no
near/past-maturity truncation applies. No city-level default was found
for either (Cincinnati: Ohio itself never defaulted; Pittsburgh:
inherited, by analogy and a raw-price sanity check, from the same
absence-of-evidence already established for Philadelphia -- not
independently re-verified for Pittsburgh specifically, flagged as such).

**Results:**
- **Pittsburgh vs. Pennsylvania** (post-signal, Apr 1843-Jan 1845,
  capped at PA's own already-documented coverage ceiling): PA state
  8.76% vs. Pittsburgh city 6.11% -- a **2.65pp gap**, essentially
  identical in size and direction to Philadelphia's own 2.68pp post-gap
  spread. **A second Pennsylvania city replicates the no-spillover
  finding.**
- **Cincinnati vs. Ohio** (post-signal, Apr 1843-Dec 1850): Ohio state
  6.25% vs. Cincinnati city 6.36% -- essentially **flat, -0.11pp**. This
  is NOT a third no-spillover confirmation -- Ohio never defaulted, so
  there's no state distress for Cincinnati to be insulated from in the
  first place. It functions as a **baseline contrast**: when the state's
  own credit is fine, its city tracks it with no gap at all; the ~2.6-
  2.7pp gap only opens up for the two Pennsylvania cities, where the
  state itself was genuinely under stress.
- Yield-measure caveat, flagged not hidden (same practice as Alabama/
  Indiana elsewhere in this project): Cincinnati vs. Ohio mixes Ohio's
  mostly-YTM primary series with Cincinnati's current-yield series;
  Pittsburgh vs. Pennsylvania uses current yield on both sides
  (genuine parity, since PA's own post-signal window is already all
  current yield via the active-default override -- the same situation
  already established for Philadelphia).

STATUS: DONE. Two new data points on the state-to-own-city question, one
confirming (Pittsburgh) and one a useful contrast rather than a third
confirmation (Cincinnati). NYC/Brooklyn vs. New York state remains open
and unstarted.

## 2026-08-17: Advisor Contagion Question -- Direct-Answer Package

Hall's Jul 30 2026 framing (state default as contagion spreading to a
defaulting state's own city, see "Advisor Framing" above) is now
explicitly answered as a standalone talking-points document:
`output/advisor_contagion_answer.md`. Not a new computation -- synthesizes
the existing Philadelphia/PA finding plus the new Pittsburgh/PA and
Cincinnati/Ohio results above into plain-language meeting notes,
explicitly separating "state-to-own-city" (what Hall asked) from
"state-to-other-state" (closer to what the original three-bucket
comparison tests) so the two don't get conflated in conversation. Also
folds in the Ohio yield-rise resolution as a cautionary example worth
raising directly with Hall (a real yield move that looked like it could
support a contagion story until the dates were checked). See that file
for the full talking-points version; the headline is that Hall's specific
question now has two consistent data points (Philadelphia and Pittsburgh,
both ~2.6-2.7pp gaps) rather than one.

STATUS: DONE.

## 2026-08-17: Canal/Robustness Comparison Script (previously deferred multiple times)

Built as a standalone script: `scripts/compare_canal_robustness.py` -->
`output/canal_robustness_yields.csv`, `output/chart_canal_robustness.png`.
Does not touch `calculate_yields.py` or `primary_yields.csv`.

**Ohio dropped entirely**, per the trade-density finding already recorded
in this file (S-2190: 2 observations, both from 1825, no data in the
1840s-50s window) -- previously flagged as "pending sign-off," now
treated as approved. The canal/robustness comparison covers New York and
Indiana only, not three states.

**New York canal bonds (S-1750/S-1820/S-1950):** YTM with the same
near/past-maturity truncation rules used everywhere else in this
project; New York never defaulted, so no active-default override
applies. Two data-quality issues surfaced and handled explicitly (not
silently patched):
- S-1750 has the already-documented 1,666-day gap (Aug 1843-Feb 1848) --
  rendered as a dotted, non-connecting segment in the chart rather than a
  straight line implying a smooth multi-year climb that never happened.
- S-1820 has one isolated price of 160.00 (Oct 14 1848), sandwiched
  between prices of 96-99.5 on either side -- verified directly against
  the raw `New-York.xls` source (row 3256, "NY State Debt" sheet): this
  is a genuine value in the source file, not a parsing artifact, but
  almost certainly a transcription error in the original digitized price
  list (a state canal bond trading 60%+ above par for one week with nothing
  on either side to explain it). Kept as-is in the CSV (the raw source
  value is not altered), excluded only from the chart's line rendering,
  with the resulting nonsensical -0.27% YTM flagged rather than plotted.

**Indiana Butler Bill canal tranches (S-0480 Deferred / S-0490 Preferred
/ S-0500 Special Preferred / S-0506 Special Deferred):** current yield
only (no codebook maturity date, same convention as Indiana's primary GO
bonds). S-0470 ("Indiana Canal") is excluded from the yield calculation
entirely -- its codebook interest-rate field is blank, so no coupon
exists to compute a yield from either method. All four tranches only
begin trading in **1850**, three years after the 1847 restructuring and
entirely after both the panic and policy windows -- this comparison
cannot speak to the Feb/Apr 1843 signal at all; it tests something else
(did the market price the seniority split the restructuring created).
**Honest wrinkle, flagged rather than hand-tuned around:** because
Indiana's default period has no documented end date, every observation
of these four tranches (all 1850-53) falls inside
`active_default_override=True` under this project's existing mechanical
convention, even though the point of the restructuring was to put the
preferred tranche back on a paying basis. This doesn't change the yield
formula here (these codes were already current-yield-only), but is worth
knowing about if the convention is ever revisited.

**Indiana preferred-vs-deferred tranche test -- the seniority effect
this test was built to check for is dramatically, unambiguously
present:**
| Group | Mean current yield | Median price | n |
|---|---|---|---|
| Preferred (S-0490 + S-0500) | 17.96% | $42.00 / $20.00 | 94 (overlap window) |
| Deferred (S-0480 + S-0506) | 57.99% | $14.25 / $9.00 | 43 (overlap window) |

A **40.04pp gap**, confirmed directly in raw prices (not a current-yield
artifact of a few extreme low-price rows): preferred tranches trade at
roughly 2-4x the price of deferred tranches throughout the overlap
window. One deferred observation (S-0506, Oct 1851, price $1.00) prices
at 500% current yield -- real per the formula on a near-worthless
distressed claim, capped off-chart in the plot and labeled rather than
letting it crush the rest of the series to a flat line near zero.
**This is the cleanest, largest, least ambiguous finding of this entire
project to date** -- the market unmistakably priced Indiana's own
restructuring-created seniority split, exactly as the hypothesis
predicted, though it says nothing about the Feb/Apr 1843 signal
specifically since all the data postdates it by years.

STATUS: DONE. Canal/robustness comparison built for New York (2 states
originally planned, now 2 as approved) and Indiana; the preferred/
deferred tranche test produced the strongest confirmatory result in the
project so far, on a question genuinely independent of the primary
policy-window test.

## 2026-08-17: Feb 11 1843 Anchor Date -- Primary Source Attempt

Full write-up: `output/anchor_date_source_check.md`. **Partial progress,
not a resolution -- the existing "two secondary sources, not yet
primary-confirmed" caveat stays in place**, now with additional partial
corroboration noted alongside it.

- Re-confirmed (not newly discovered) that congress.gov blocks automated
  access with a Cloudflare challenge, on both the WebFetch tool and a
  direct `curl` request with a standard browser user-agent.
- Checked whether the Congressional Globe itself (distinct from
  McGrane's book) might be freely available on archive.org as a
  periodical scan -- found indexed daily-issue records but the metadata
  API returns them empty (`{}`), consistent with the same access
  restriction already hit for McGrane's book.
- **New avenue, not previously tried: UNT Digital Library hosts Volume
  12 of the Congressional Globe** (Dec 3 1842-Mar 11 1843, exactly the
  right session), freely, with no paywall or lending restriction stated
  -- `https://digital.library.unt.edu/ark:/67531/metadc30768/`. Direct
  page access and full-text search are both blocked by an Altcha
  proof-of-work CAPTCHA that automated tools couldn't clear (confirmed
  on repeated attempts, multiple endpoint patterns). **However, Google's
  own search index has crawled real OCR'd snippets from inside this
  volume that a direct fetch couldn't reach:** printed page 292 ("Mr.
  Gwin was insisting on his motion to go into committee") and page 294
  ("a proposition to distribute two hundred millions of a stock debt of
  the U.S. Government among the states, to enable them to pay their
  debts") -- genuine primary-source text (not a paraphrase) that
  corroborates Gwin's active involvement in an assumption-of-state-debts
  floor debate in this exact volume, consistent with McGrane's and
  Thomson's secondary accounts, though not carrying an explicit date
  stamp through search indexing alone and not confirming a vote outcome.
- **Recommendation for next steps:** a human visiting
  `https://digital.library.unt.edu/ark:/67531/metadc30768/m1/308/`
  through roughly `m1/312/` directly in a browser can very likely clear
  the Altcha challenge in seconds (it's designed to pass for real
  browsers) and get the full verbatim text -- a faster path than the
  previously-assumed interlibrary-loan route for McGrane's book.

STATUS: PARTIAL / OPEN. Real primary-source snippets found and
corroborate the existing secondary-source claim, but a full verbatim
read (and vote-outcome confirmation) still requires a human to clear a
CAPTCHA that automated tools cannot pass. Caveat in the "Confirmed
No-Bailout Reference Date" section above is unchanged, not weakened or
strengthened enough to rewrite.

## 2026-08-17 (final prep pass): Indiana Tranche Result -- Sanity Check

Stress-tested the 40.04pp preferred-vs-deferred gap the same way S-2410's
inflated YTM was caught, before presenting it as a headline finding.
Diagnostic output: `output/indiana_tranche_sanity_check.csv` (146 rows,
per-observation data with sanity flags) -- `canal_robustness_yields.csv`
and its chart were NOT touched.

**Result: the gap is real and does not need correction.** Unlike
S-2410, none of the three failure modes that inflated that number apply
here:
- **Not a thin-sample artifact:** the gap holds across 146 observations,
  spanning 36 distinct months (preferred) and 27 distinct months
  (deferred) over a ~2.7-3.3 year window -- not a handful of days
  driving the average.
- **YTM-vs-current-yield is moot, not mishandled:** none of the four
  tranches have a maturity year in the codebook, so current yield is the
  ONLY computable method (same as Indiana's other current-yield-only
  codes) -- there was never a YTM choice to get wrong.
- **No maturity-truncation contamination possible:** with no maturity
  date, `excluded_near_maturity`/`excluded_past_maturity` are
  mechanically always False for these four codes.
- **Ordering robustness:** checked every preferred observation against
  nearby (+/-10 day) deferred observations for a price crossover -- found
  in 90 of 91 pairs, preferred trades higher. The single exception is
  S-0480's own first recorded price (Sep 21 1850, $50.00) -- 2.4x its own
  second-highest value ever recorded ($21.00) -- flagged as a likely
  isolated data anomaly (same treatment as S-1820's 160.00 print), not
  evidence against the ordering.
- **Within-group heterogeneity noted, doesn't threaten the conclusion:**
  "Preferred" (S-0490, median $42) and "Special Preferred" (S-0500,
  median $20) trade at different levels, so the pooled average blends two
  sub-tranches. Even the weaker of the two (S-0500, median $20) still
  clearly exceeds both deferred codes (median $9-14.25).

**One genuine open caveat surfaced -- flagged for the advisors, not
resolved by more analysis.** Current yield (coupon/price x 100) assumes
the full nominal 5% coupon was actually paid in cash. Checked Wallis's
Indiana property-tax paper and the Wallis/Sylla/Grinath NBER working
paper (both already project sources) plus several web searches for
whether the "deferred" tranche's coupon was itself suspended/postponed
by the 1847 restructuring, or merely subordinated-but-still-paid --
**could not find an explicit answer either way.** This doesn't affect
the PRICE-based finding at all (that's solid regardless), but it does
affect how confidently the specific "40.04pp" and "500%" YIELD figures
should be described -- they may overstate actual cash income to a
deferred bondholder if coupon was suspended, or accurately reflect it if
merely subordinated. This is exactly the kind of institutional-detail
question Hall/Sargent's literature knowledge could resolve quickly where
more web search couldn't -- added to the advisor agenda below.

STATUS: DONE. Headline finding survives scrutiny -- present the price
gap with full confidence; caveat the specific yield percentages as
"assumes full coupon payment, not independently confirmed" until
discussed with advisors.

## 2026-08-17 (final prep pass): Feb 11 1843 Primary Source -- Retry, Still Blocked, Now a Documented 2-Minute Task

Full write-up: `output/anchor_date_manual_step.md`. Retried across 8
distinct hosts/methods this pass (congress.gov, archive.org's two
restricted collections, UNT, HathiTrust, Google Books web UI, Google
Books API, Online Books Page) -- **every automated route is blocked**,
either by a Cloudflare/Altcha challenge or an access-restricted metadata
record. Full retry log is in the output file; not repeated here.

**One genuinely new, useful discovery this pass:** Google Books hosts
direct, unrestricted PDF downloads of Congressional Globe volumes with
**no CAPTCHA at all** (confirmed by successfully downloading a 305MB,
1,445-page volume with zero bot-check). The catch: automated search
couldn't reliably identify the correct volume ID among many similarly-
titled Congressional Globe volumes -- the first guess (`id=Kvre2Nur8z8C`)
turned out to be the wrong Congress entirely (40th Congress, 2nd
session, 1867-68 -- confirmed by a zero-match text search for "Gwin"
against its full extracted text). A human picking the right volume via
Google Books' own search UI, then using the same download-link pattern,
would get instant full-text access with no CAPTCHA whatsoever -- this is
now the RECOMMENDED route (faster than UNT's Altcha challenge from the
prior pass, which still works too and is documented as a fallback).

STATUS: STILL OPEN, genuinely a 2-minute human task now (not a research
gap) -- see `output/anchor_date_manual_step.md` for both routes with
exact URLs/instructions. Existing secondary-source caveat in "Confirmed
No-Bailout Reference Date" is unchanged.

## 2026-08-17 (final prep pass): Feb 11 1843 Anchor Date -- RESOLVED, Real Primary-Source Text Found

Amey completed the manual step above: cleared UNT's Altcha CAPTCHA by
hand, then located the correct Google Books scan of Volume 12 directly
(Google Play listing confirmed "The Congressional Globe: Volume 12,"
published January 1843, ID `nlE9AQAAMAAJ` -- cover image fetched and
visually confirms "THIRD SESSION OF THE TWENTY-SEVENTH CONGRESS. VOLUME
XII."). Used the Google Books in-viewer search for "Gwin," which
returned signed page-image URLs (bulk PDF download was disabled for this
particular scan, but individual page images load fine with a valid
per-page token) -- three hits: printed pages 283, 284 (real match, read
below), and 374 (a different, unrelated Gwin mention re: naval coal
purchases at Pensacola -- confirms Gwin spoke on many topics, not every
hit is relevant).

**Pages 283-284: a genuine, substantive, on-topic House floor debate --
"MISSISSIPPI STATE BONDS."** Participants confirmed as real sitting
members of the 27th Congress at this exact time: Mr. GWIN (Mississippi),
Mr. GRANGER (Francis Granger, Whig-NY, confirmed via House.gov/Wikipedia
to be serving 1839/41-1843), and Mr. THOMPSON (likely Jacob Thompson,
also Mississippi). Content, read directly off the page images:

- Dispute over whether Mississippi's Governor was constitutionally
  authorized to issue $5,000,000 in bonds to capitalize the Union Bank
  of Mississippi -- i.e., whether the bonds were validly issued at all,
  the core legal question behind Mississippi's actual repudiation (this
  is the same Union Bank bond dispute that became central to the 1843
  Mississippi gubernatorial election, per independent web corroboration).
- A resolution calling on the President to furnish correspondence
  relating to recognition of Mississippi's disputed debt.
- A sharp personal exchange: Granger had written, in an earlier printed
  speech, that Gwin's objects in raising the issue were "two-fold: one
  was to get up a political excitement; the other was to bring into
  disrepute the credit of the United States." Gwin pressed him on the
  record to confirm or retract this; Granger denied impugning Gwin's
  motives specifically but stood by his substantive view -- that
  repudiation, not merely asking creditors for time, is what actually
  damaged the country's credit.

**Caveat, stated plainly:** neither page carries a visible date stamp
(the day's header would be a page or two earlier in the volume; not
fetched). Page position is strong circumstantial support for Feb 11,
1843 specifically -- these pages sit 8-9 pages before the already-
confirmed Feb 16, 1843 page (see the prior UNT read of printed page
292) -- but this is not a pinpoint date confirmation, only a tight
neighborhood one. The debate text itself references "a previous day,"
confirming this was a multi-day exchange, so Feb 11 could be either this
exact session or the one immediately before/after it.

**Assessment: this substantially strengthens, but does not 100% clinch,
the existing citation.** Upgrade the caveat from "corroborated by two
secondary sources only, no primary read attempted" to "corroborated by
two secondary sources AND a real, on-topic primary-source floor debate
matching the right participants, subject, and tight date window, though
the exact day (Feb 11 vs. an adjacent session day of the same dispute)
is not pinned to the page." This is a genuine, real primary-source read
-- not a Google-index snippet like the prior pass's "corroboration" --
and is sufficient to cite with confidence in the paper, with this exact
caveat carried forward rather than dropped.

STATUS: RESOLVED (with the above caveat carried forward, not erased).
No further manual work needed on this item.

## 2026-08-17 (final prep pass): NYC/Brooklyn vs. New York State -- Closed (insufficient data, proven not assumed)

Full write-up: `output/nyc_brooklyn_check.csv` (63 rows -- every genuine
NYC/Brooklyn/Jersey City code on New-York.xls's "City Debt" sheet, not
just the 6 candidates flagged in the original scoping check).

**Confirms, decisively this time, that no candidate supports a pre/post
divergence test.** The densest pre-signal candidates (C-0600: 471 obs,
but 1814-1823, entirely the wrong era; C-0740: 103 obs, but ends Apr
1842; C-0880: 86 obs across 1824-1851, but has a 4,802-day/13-year gap
that swallows the entire 1829-1841 stretch and leaves only 13 usable
observations anywhere near the 1842-43 window) are either irrelevant-era
or too gapped to help. The densest post-signal candidates are the same 6
already flagged in the prior scoping check (C-0698/C-0695/C-0696/C-0660/
C-0650/C-0320), all starting at/right before Jan-Feb 1843 with 0-5
pre-signal observations each. This was previously an assumption from a
6-candidate sample; it is now a proven conclusion from all 63.

**Post-signal LEVELS comparison built anyway** (the same "post-signal
only" treatment already used for Cincinnati/Pittsburgh), matched to NY
state's own S-1650 coverage ceiling (Apr 1843-Jan 1848): NYC/Brooklyn
combined (6 codes, current yield/YTM per the same per-code convention
used elsewhere) mean **5.56%** (n=196) vs. NY state (S-1650) mean
**5.37%** (n=117) -- essentially flat, actually a small **-0.19pp**
reversal (city very slightly above the state, not below).

**Reading:** consistent with the Cincinnati/Ohio pattern, not a third
Philadelphia-style confirmation. New York never defaulted, and (per this
project's own earlier finding, "NY Price Investigation") its own S-1650
series already reads empirically closer to "always safe" than "risky but
survived." A near-zero city/state gap here fits the emerging overall
shape: **the city-below-state gap only opens up specifically where the
state itself was genuinely under stress** (Philadelphia 2.68pp,
Pittsburgh 2.65pp, both Pennsylvania) -- it doesn't appear for cities of
states that were never in real distress (Cincinnati/Ohio -0.11pp,
NYC-Brooklyn/New York -0.19pp). Two "safe-state" baseline points now
exist, not just one.

STATUS: DONE / CLOSED. Real, caveated comparison built; no pre/post test
was possible and none was forced.

## 2026-08-17 (final prep pass): Philadelphia County Bonds -- Checked, One Valuable Finding

Full write-up: `output/philadelphia_county_check.csv`. Ran the same
rigorous gap-check that caught C-1100's 343-day gap on all three flagged
codes -- did not assume clean coverage from the original scoping pass's
total-obs/date-range numbers.

**C-1310 and C-1300 are Philadelphia COUNTY bonds -- a distinct
government entity from Philadelphia city (C-1100) or Pittsburgh.** Both
clean (0-1 gaps over 90 days), dense post-signal (349-357 obs through
Dec 1850), but only 5 pre-signal observations each (Dec 31 1842 onward)
-- the same thin-pre-signal situation as Cincinnati/Pittsburgh, not a
repeat of C-1100's case. Would be a legitimate 4th/5th post-signal-levels
data point (and the only county-level, as opposed to city-level, one) if
pursued further -- not done this pass, since three consistent
post-signal comparisons (Pittsburgh, Cincinnati, NYC/Brooklyn) already
exist and a 4th of the same type has diminishing marginal value right
before paper-writing begins.

**C-1260 ("Philadelphia 6s, r. 1852") is the SAME entity as C-1100 --
Philadelphia the city, not the county -- and this one matters.** It has
genuine pre-signal density (88 obs) AND post-signal density (272 obs),
with its own 231-day gap (Aug 5 1843-Mar 23 1844) -- but critically,
**this gap does not overlap with C-1100's own 343-day gap (Feb 25
1843-Feb 3 1844).** C-1260 has real data precisely in the Jun-Aug 1843
window that C-1100 is blind to -- the exact "immediate reaction to the
signal" period the original Philadelphia-vs-PA comparison explicitly
flagged as unobservable ("the city's immediate reaction to the Apr 1843
signal itself cannot be observed at all").

**Computed directly, CORRECTED 2026-08-25 (see "Second-Philadelphia-Bond
Figure -- Corrected Everywhere" below; the original Jun-Aug/n=10 window
here undercounted the actual data available and is superseded):**
Philadelphia city (C-1260, current yield, consistent with the existing
convention for this comparison), prices stable throughout, 105-110,
actually above par, vs. Pennsylvania state's own primary series in the
identical window -- **two verified figures, reported together rather
than picking one, since they trade off precision against coverage:**
- **5.95pp** (Philadelphia 5.59% vs. Pennsylvania 11.53%, n=19 city /
  n=38 state), using the project's standard post-signal convention
  (Apr 1, 1843 onward) through Aug 5, 1843.
- **6.28pp** (Philadelphia 5.63% vs. Pennsylvania 11.91%, n=24 city /
  n=48 state), using the full window that actually fills C-1100's gap
  (Feb 25-Aug 5, 1843).

**A 6-7pp gap observed DURING the immediate post-signal reaction, not
just a year later** -- this closes the single biggest stated limitation
of the flagship Philadelphia finding, and is if anything a stronger
result than first reported, not a weaker one. Not yet folded into
`compare_city_vs_state.py` or its outputs (per the ground rules for this
pass); flagged here as a strong candidate for that script's next
revision, since it directly answers a limitation that script's own
docstring states explicitly.

STATUS: DONE. C-1310/C-1300 (county) -- checked, low-priority if
extended further. C-1260 (city) -- genuinely valuable, closes the
"can't observe the immediate reaction" gap in the flagship finding;
recommend folding into `compare_city_vs_state.py` in a future pass (not
this one, per the ground rules keeping that script untouched here).

## 2026-08-17 (final prep pass): Data-Integrity Notes -- Confirmed Already Documented

Phase 5 of this pass asked to confirm the two data-quality catches from
the canal/robustness work (S-1750's 1,666-day gap, S-1820's likely
transcription-error price of 160.00) were documented with a clear
methodological note, not just silently patched. **Checked: both are
already fully documented**, with sourcing and rationale, in the
"2026-08-17: Canal/Robustness Comparison Script" section above (see the
two bullet points under "New York canal bonds"). No further writing
needed -- flagged here only to close the item explicitly, per this pass's
goal of leaving nothing unresolved sitting undone.

## 2026-08-17 (final prep pass): Meeting-Prep Materials Updated

`scripts/build_meeting_prep_doc.py` (not on the protected-files list for
this pass) was substantively rewritten, not just flagged as stale: added
new "What's Changed" bullets for the city-vs-state and canal/robustness
work and the Ohio yield-rise resolution; added two new results
subsections (d. Canal/Robustness -- Indiana Tranche, with the
`chart_canal_robustness.png` embed; e. City-vs-State Contagion Results,
with the Cincinnati and Pittsburgh chart embeds); extended the headline
takeaway with the two new findings (Indiana seniority pricing, city
no-spillover replication); added three new talking-points script
paragraphs covering the same; replaced "Open Items for Next Phase" with
the same closed/(a) vs. needs-advisors/(b) split used in this file's
"Immediate Next Steps" below. Regenerated
`output/meeting_prep_final.docx` (grew from 673KB to 1.32MB, reflecting
the two new chart embeds) and re-copied to `~/Desktop/meeting_prep_final.docx`.

**Update-email draft: searched the full project directory -- no draft
email file exists anywhere in this repo.** Cannot flag what needs
revision in a document that isn't here; if one exists, it's outside this
project's tracked files (e.g., directly in an email client) and wasn't
found by this pass. Noting this plainly rather than fabricating content
or silently skipping the instruction.

## 2026-08-17 (verification pass): C-1260 Second-Philadelphia-Bond Claim -- Stress-Tested, Real Correction Found

Prior sessions reported that C-1260 ("Philadelphia 6s, r. 1852") fills
C-1100's 343-day data gap and shows a ~5.4pp Philadelphia/PA gap during
the immediate post-signal reaction (n=10, Jun-Aug 1843) -- this was
flagged as never verified with the same rigor as other results and
treated as an unconfirmed claim going into this pass. Output:
`output/philadelphia_second_bond_check.csv` (367 rows, full C-1260
history with maturity-truncation flags). `compare_city_vs_state.py` and
its outputs were NOT touched.

**Confirmed real, and confirmed genuinely NEW data, not overlapping
C-1100's own gap:** C-1260 has exactly one gap over 90 days (Aug 5
1843-Mar 23 1844, 231 days) -- distinct from C-1100's own gap (Feb 25
1843-Feb 3 1844). No near/past-maturity contamination (matures 1852, all
367 observations end by Feb 1850, zero rows flagged). No price
anomalies of the S-1820-160.00 kind (clean 103-110 range throughout the
relevant window).

**But the specific "5.4pp, n=10" figure does not survive rigorous
recomputation -- it used an incomplete ad hoc window, not the full
window that actually fills C-1100's gap.** Using the correct window
(Feb 25-Aug 5 1843, the actual full period C-1100 has no data for),
n=24, not 10: Philadelphia 5.63% vs. Pennsylvania 11.91%, a **6.28pp**
gap. Restricting further to the project's standard post-signal
convention (Apr 1 onward), n=19: Philadelphia 5.59% vs. Pennsylvania
11.53%, a **5.95pp** gap. **Both corrected numbers are LARGER than the
original 5.4pp estimate, not smaller** -- the underlying finding is not
just confirmed but strengthened; only the specific cited figure needs
updating.

STATUS: DONE. Real finding, genuinely strengthens the flagship
Philadelphia result -- but cite **5.95pp (n=19, Apr-Aug 1843)** or
**6.28pp (n=24, Feb 25-Aug 5 1843)** going forward, not the earlier
5.4pp/n=10 figure. That earlier figure also appears verbatim in
`output/meeting_prep_final.docx`'s "City-vs-State Contagion Results"
section -- needs the same correction if/when this gets folded into the
protected comparison script (still not done, still requires editing
`compare_city_vs_state.py`, which remains out of scope for this pass).

## 2026-08-17 (verification pass): Indiana Deferred-Tranche Coupon Question -- One Real Attempt, Still Unresolved

Made one dedicated, serious attempt (not a repeat of the earlier light
search) before continuing to treat this as pure advisor judgment.
Checked: Lee Newcomer, "A History of the Indiana Internal Improvement
Bonds," *Indiana Magazine of History* 32(2) (1936), pp. 106-115; the
Indiana Historical Society's Wabash and Erie Canal Company finding aid
(collection M0758/OM0392); Wallis's Indiana property-tax paper (already
a project source); several additional targeted web searches for
period-specific "preferred"/"deferred" canal stock terminology.

**Found real, useful, citable context, but not a definitive answer.**
Newcomer (p. 110) confirms the mechanism for the canal-revenue-backed
half of the 1847 restructuring precisely: "the principal and half the
interest of these new securities were to be paid by the state and the
other half of the interest was to be paid by the revenues of the canal"
-- and confirms this was a genuinely contingent payment, not a
guaranteed one (p. 113: bondholders "saw their security steadily
shrinking" as railroads diverted canal traffic in later years).
**However, this source does not use the specific terms "preferred" and
"deferred" anywhere** -- confirmed by directly re-querying the text for
those terms. The codebook's exact tranche names likely reflect how these
securities were labeled/traded on Wall Street rather than the statute's
own language, and no period financial reference defining those specific
instrument names was located.

STATUS: STILL UNRESOLVED -- genuinely not findable with a serious,
real attempt (not a shallow one), confirmed appropriate to leave as a
live question for Hall/Sargent. Worth handing them the one real finding
above (canal-revenue interest was contingent on actual toll income, not
formally guaranteed) as useful context even though it doesn't pin down
preferred-vs-deferred specifically.

## 2026-08-17 (verification pass): Numerical Consistency Sweep

Full write-up: `output/numerical_consistency_check.md`. Every specific
numeric claim in this file (percentages, pp spreads, observation counts,
exact dates) was traced back to its source CSV and recomputed directly;
`meeting_prep_final.docx` was spot-checked for the same figures via
`python-docx` text extraction. Neither file was silently corrected --
mismatches are listed below for review, not fixed in place.

**Two real mismatches found, both flagged, neither fixed:**
1. `primary_yields.csv`'s stated row count (3,441, see the "calculate_yields.py
   (built)" section) is stale -- the file actually has 3,711 rows now.
   No accompanying data-quality problem found (every downstream number
   drawn from the file checked out correctly) -- looks like simple
   staleness in one descriptive sentence after later additions grew the
   file, not a broken pipeline.
   **RESOLVED 2026-09-02:** root cause pinned and the sentence corrected
   in place. The +270 rows are exactly S-2330 (93) + S-2410 (177), added
   to `BOND_SPECS` by commit `5519087` ("pa bridge") during the PA Full
   Bond Re-Scan; 3,441 + 270 = 3,711. The "calculate_yields.py (built)"
   section now carries the verified 3,711 figure with this explanation,
   and `output/FACTS_LAB_REPORT.md` uses 3,711 throughout. No two
   different counts remain on record.
2. The Alabama-vs-Ohio yearly table's 1843 row (7.36%/7.15%) doesn't
   reproduce -- actual full-calendar-year recomputation gives 8.23%/8.18%.
   Every other row of that same table (1844-1848, 1850) reproduces
   exactly with the same methodology. Root cause not identified; flagged
   for review rather than guessed at.

**One already-known issue (the C-1260 figures, see above) confirmed to
also appear in `meeting_prep_final.docx`**, not just `PROJECT_CONTEXT.md`.

**Everything else checked out exactly** -- 21 of 23 distinct claims
verified correct, including the S-2410 override table, the PA
before/after-override spread (13.12pp -> 2.08pp), the Philadelphia/
Pittsburgh/Cincinnati/NYC-Brooklyn city comparison numbers, the Ohio
yield-check peak dates and values, the Indiana tranche gap (40.04pp) and
median prices, and every row count across
`ohio_yield_check.csv`/`canal_robustness_yields.csv`/`nyc_brooklyn_check.csv`/
`philadelphia_county_check.csv`/`indiana_tranche_sanity_check.csv`.
Several numbers that initially appeared to mismatch turned out to be the
checker's own window/grouping errors (e.g., not capping Cincinnati's
comparison window at Cincinnati's own last observation date, or not
grouping multi-code states by date before averaging) -- corrected and
documented in the output file so a future pass doesn't have to
rediscover the right convention.

STATUS: DONE. Two real, minor mismatches flagged for Amey's review (not
fixed); one already-known issue confirmed to have a second footprint in
the meeting-prep doc; everything else confirmed solid.

## 2026-08-17 (verification pass): Reproducibility Check -- Both Newer Scripts

`scripts/compare_city_vs_state_cincinnati_pittsburgh.py` and
`scripts/compare_canal_robustness.py` were each rerun from scratch
(MD5-hashed outputs before and after). **Both scripts: PASS.** All CSV
outputs (`city_vs_state_cincinnati.csv`, `city_vs_state_pittsburgh.csv`,
`canal_robustness_yields.csv`) are byte-identical before and after
rerun; all chart PNGs (`chart_cincinnati_vs_ohio.png`,
`chart_pittsburgh_vs_pa.png`, `chart_canal_robustness.png`) are
MD5-identical. `git status` confirms zero diff from either rerun. Same
standard `compare_city_vs_state.py` was already held to. No
`output/reproducibility_check.md` needed -- no failure found.

STATUS: DONE. Both newer scripts confirmed fully reproducible, matching
the standard already set for the original city comparison script.

## 2026-08-25: Second-Philadelphia-Bond Figure -- Corrected Everywhere

Small targeted fix, not a new research pass. Searched `PROJECT_CONTEXT.md`
and `output/meeting_prep_final.docx` for every instance of the stale
"5.4pp, n=10" C-1260 figure (see "C-1260 Second-Philadelphia-Bond Claim"
above for the original correction, done 2026-08-17, which established
the right numbers but didn't propagate them everywhere yet).

**Found and fixed exactly one live location with the stale claim**: the
"Philadelphia County Bonds" section's "Computed directly" paragraph
(originally said Philadelphia 5.62%/Pennsylvania 11.05%/n=10/~5.4pp) --
now states both corrected figures together, since they trade off
precision against coverage rather than one being simply "more right":
**5.95pp (Philadelphia 5.59% vs. Pennsylvania 11.53%, n=19, Apr-Aug
1843)** and **6.28pp (Philadelphia 5.63% vs. Pennsylvania 11.91%, n=24,
full Feb 25-Aug 5 1843 gap-fill window)**. Every other mention of "5.4pp"
in this file (in the 2026-08-17 correction write-up and the meeting
agenda) was already historical narrative correctly describing the
correction, not a live restatement of the stale claim -- left as-is.

**Confirmed `output/philadelphia_second_bond_check.csv` is internally
consistent with both corrected figures** (re-verified directly, not
recomputed from scratch -- the CSV already had the right underlying
data, only the prose citing it was stale).

**`meeting_prep_final.docx` fixed at the source and regenerated.** The
docx is generated by `scripts/build_meeting_prep_doc.py` (not a protected
script), so this was a direct text edit to that script's "e. City-vs-State
Contagion Results" paragraph, followed by rerunning the script. No
LibreOffice/Word available in this environment to render the docx to
PDF/JPEG for a visual check, so verification was done instead by
re-extracting the document's text (`python-docx`) and confirming "5.4",
"5.62%", and "11.05%" no longer appear anywhere in it, while "5.95pp" and
"6.28pp" both do -- a more reliable check than a visual render would have
been anyway, since it inspects the actual text content directly rather
than a rendering. File regenerated in place and re-copied to
`~/Desktop/meeting_prep_final.docx`.

STATUS: DONE. The corrected figure now appears consistently everywhere
it's cited, in both files.

## 2026-08-25: Alabama-vs-Ohio 1843 Discrepancy -- Root-Caused

**Note on the task's own premise:** the request that triggered this
investigation cited "7.118%" as the current pipeline value for one side
of this discrepancy. That figure does not match this project's own prior
consistency-check finding (`output/numerical_consistency_check.md`
documents 8.23%/8.18%, not 7.118%, for the full-calendar-year figure) --
flagging this discrepancy plainly rather than silently treating either
number as ground truth. The closest match found for "7.118%" during this
investigation is Ohio's mean-of-per-code-means using the raw
`current_yield` column (7.110%, see below) -- close but not exact, and
notably this is exactly the WRONG methodology this investigation
identifies as the likely root cause, not the right one. Proceeded using
direct, independent recomputation from `output/primary_yields.csv`
throughout rather than assuming either cited number.

**Root cause identified with high confidence.** Recomputed every row of
the Alabama-vs-Ohio table (1843-1850) from `output/primary_yields.csv`
using the standard methodology already established elsewhere in this
project: full-calendar-year, date-grouped mean of the official `yield`
column (YTM for Ohio, current yield for Alabama, matching
`calculate_yields.py`'s own convention). **6 of 7 years (1844, 1845,
1846, 1847, 1848, 1850) reproduce the documented table to within
0.05pp on both Alabama and Ohio -- only 1843 fails, on both sides
simultaneously** (documented 7.36%/7.15% vs. recomputed 8.23%/8.18%).

Ruled out, in the order the task suggested:
- **Active-default override**: confirmed directly in `primary_yields.csv`
  -- `active_default_override` is `False` for all 23 Alabama and all 106
  Ohio rows in 1843 (neither state has a `DEFAULT_PERIODS` entry). Not
  the cause.
- **Bond-code substitution**: confirmed Ohio's 4 codes (S-2100/S-2110/
  S-2080/S-2010) and Alabama's 2 codes (S-0030/S-0040) in
  `calculate_yields.py`'s current `BOND_SPECS` are exactly the codes
  this project has used since the very first candidate scan -- no
  addition/removal, unlike PA's later re-scan. Not the cause.
- **Rounding/averaging methodology**: this IS the cause, isolated to
  1843 specifically. Testing current_yield instead of the blended
  YTM-based `yield` column for Ohio gets much closer to the documented
  7.15% (current_yield date-grouped mean: 7.245%; mean-of-per-code-means:
  7.110%) than the correct blended-yield column does (8.18%) -- while
  for every OTHER year, current_yield does NOT match the documented
  figure nearly as well as the blended-yield column does (e.g. 1850:
  blended-yield 4.831% exactly matches doc's 4.83%, while current_yield
  gives 5.553%, well off). **This means the 1843 row was almost
  certainly computed with the wrong yield-measure column (current
  yield instead of the project's official blended/YTM-for-Ohio
  column) -- an inconsistency invisible in every other year because
  1843 is specifically the year Ohio's bond prices sat furthest from
  par** (mid-panic-recovery, see the already-documented Ohio
  price-collapse-and-recovery finding elsewhere in this file), which is
  exactly when YTM and current yield diverge most. A narrower
  (non-full-calendar-year) date window may also be a contributing
  factor -- several partial-year windows tested came closer to the
  documented figures than the full year does, without landing on an
  exact match either. **The precise original computation could not be
  reconstructed to the hundredth of a percent** (no saved script exists
  for this table, matching the ad hoc computation pattern already noted
  elsewhere in this project for several other early tables) -- but the
  root cause (wrong/inconsistent yield-measure column, isolated to this
  one row) is established with high confidence, not a guess.
- **Simple transcription error**: not ruled out as a contributing factor,
  but the above finding (current-yield vs. blended-yield explaining most
  of the gap, in the specific year where that choice matters most) is a
  more complete and specific explanation than "someone mistyped a
  number" would be.

**Verdict: the documented 7.36%/7.15% was wrong; corrected to 8.23%/8.18%
(spread +0.05pp)** in the table above ("Finding: Alabama vs. Ohio, does
it pattern as 'in between'?"). This does not weaken the table's own
stated conclusion -- if anything the corrected spread (+0.05pp) is an
even tighter "opens near-identical" starting point than the original
(mistaken) +0.21pp was, so the qualitative story this table tells is
unaffected, only strengthened in its opening data point.

**Not systemic**: confirmed directly (see above) that all 6 other rows
of this same table reproduce exactly -- this is an isolated, one-row
issue, not a broader pipeline problem. No other table or figure in this
project checked in the prior consistency sweep showed this pattern.

STATUS: DONE. Root cause identified (wrong yield-measure column, unique
to 1843 because of Ohio's price levels that year), table corrected, confirmed
isolated to this one row.

## Immediate Next Steps (current, supersedes all earlier "next step" sections)

**This is the final prep pass before Amey moves to writing the paper.**
The list below is split into two categories on purpose: (a) things that
are genuinely finished and need no further action, and (b) the actual
short agenda for the next live meeting with Hall and Sargent -- items
that more analysis alone cannot resolve, because they're judgment calls,
institutional-knowledge questions, or a literal CAPTCHA only a human can
clear. Category (b) is the meeting agenda; nothing else needs to be
raised.

### (a) RESOLVED / CLOSED -- nothing further needed before the paper

- Before/after framing, no-bailout anchor date (subject to the one open
  verification in category (b) below), bond seniority, Alabama's
  yield-formula treatment, the S-2410 active-default YTM fix, the PA
  bond re-scan, the NY GO coverage saga (S-1320/1370/1560 -> S-1650), the
  Ohio yield-rise claim (real move, wrong window -- see 2026-07-30
  section), and the trade-density/bank-held investigation are all closed
  from earlier passes -- see their dated sections above.
- **Cincinnati vs. Ohio and Pittsburgh vs. Pennsylvania** -- built,
  checked for gaps properly, both closed (see "2026-08-17: Cincinnati and
  Pittsburgh City-vs-State Comparisons").
- **NYC/Brooklyn vs. New York state** -- now closed, not just deferred.
  Exhaustively scanned all 63 candidate codes (not the original 6) and
  proved no pre/post test is possible; built the post-signal levels
  comparison anyway (near-parity, -0.19pp, consistent with the
  Cincinnati/Ohio "safe state -> no city gap" pattern). See "2026-08-17
  (final prep pass): NYC/Brooklyn vs. New York State."
- **Philadelphia County bonds** -- checked properly (not assumed clean).
  C-1310/C-1300 are a legitimate but low-priority 4th post-signal-levels
  data point if ever extended further; not pursued this pass since three
  consistent comparisons already exist. See "2026-08-17 (final prep
  pass): Philadelphia County Bonds."
- **The Indiana 40.04pp tranche result** -- stress-tested like S-2410 was
  and survived: not a thin-sample artifact, no maturity-truncation
  contamination possible, ordering holds in 90/91 nearby-date pairs. Safe
  to present as the project's cleanest confirmatory finding. (The one
  open piece -- whether "yield" is the right word for it -- is in
  category (b) below, not a blocker to presenting the price-based
  finding itself.)
- **Canal/robustness comparison script, bank-held bonds trade-density
  pass, city-vs-state scripts (Philadelphia, Cincinnati/Pittsburgh)** --
  all built, all documented with clear methodological notes for their
  respective data-quality catches (S-1750's gap, S-1820's likely
  transcription error, C-1100's 343-day gap) -- confirmed properly
  written up, not silently patched.
- **Advisor talking-points package** (`output/advisor_contagion_answer.md`)
  -- ready to present as-is for Hall's Jul 30 contagion question.
- **Feb 11 1843 anchor date -- RESOLVED.** Amey manually cleared the
  CAPTCHA barrier and read a real, on-topic primary-source floor debate
  (Gwin/Granger/Thompson, "Mississippi State Bonds") in the correct
  Congressional Globe volume, in the right tight date neighborhood. See
  "2026-08-17 (final prep pass): Feb 11 1843 Anchor Date -- RESOLVED"
  above for the full read and the exact caveat to carry into the paper
  (strengthened, not 100% pinned to the literal day). No further action
  needed.
- **Both newer comparison scripts confirmed reproducible.**
  `compare_city_vs_state_cincinnati_pittsburgh.py` and
  `compare_canal_robustness.py` each rerun from scratch this pass --
  CSV outputs byte-identical, chart PNGs MD5-identical, matching the
  standard already set for `compare_city_vs_state.py`. See "Reproducibility
  Check -- Both Newer Scripts" above.
- **Numerical consistency sweep done.** 21 of 23 specific numeric claims
  in this file verified exactly against their source CSVs; the 2 real
  mismatches found are minor and listed as review items in category (b)
  below, not silently fixed. See "Numerical Consistency Sweep" above and
  `output/numerical_consistency_check.md`.

### (b) GENUINELY REQUIRES THE ADVISORS -- the actual meeting agenda

1. **Alabama reclassification (Defaulted -> Risky-but-survived) --
   still not personally confirmed by Hall or Sargent.** Strengthened by
   three independent secondary sources (see "Third Advisor Meeting"
   section above) but this is a judgment call about how to characterize
   a historical episode, not a data problem -- no further analysis can
   resolve it. **Needs a yes/no from the advisors before it can be
   stated as settled in the paper.**
2. **Indiana deferred-tranche coupon question -- does "deferred" mean
   interest was suspended, or merely subordinated-but-paid?** Surfaced
   by this pass's sanity check (see "Indiana Tranche Result -- Sanity
   Check" above). Web search (Wallis's papers, NBER WP 10753) couldn't
   settle it. This is exactly the kind of specific institutional detail
   Hall/Sargent's literature knowledge is likely to resolve in one
   sentence where more searching couldn't. Doesn't threaten the
   headline price-based finding, but affects how precisely the "40.04pp"
   and "500%" yield figures should be worded in the paper.
3. **C-1260's fill of the Philadelphia "immediate reaction" gap -- figure
   now corrected everywhere (2026-08-25), but still not folded into
   `compare_city_vs_state.py` itself.** A second Philadelphia city bond
   (C-1260) has data exactly where C-1100 doesn't, showing a real
   city/state gap during the immediate post-signal window the original
   comparison flagged as unobservable -- **5.95pp (n=19, Apr-Aug 1843) or
   6.28pp (n=24, full Feb 25-Aug 5 1843 gap-fill window)**, both now
   correctly stated in `PROJECT_CONTEXT.md` and `meeting_prep_final.docx`
   (see "Second-Philadelphia-Bond Figure -- Corrected Everywhere" above).
   The remaining task -- actually incorporating C-1260 into the protected
   comparison script and its outputs -- is still open. **Worth 15 minutes
   in a future pass, not advisor input.**
4. **`primary_yields.csv` row count -- RESOLVED 2026-09-02.** Was
   documented as 3,441 in the "calculate_yields.py (built)" section;
   verified current count is **3,711**. Cause: the PA Full Bond Re-Scan
   (commit `5519087`) added S-2330 (93 rows) + S-2410 (177 rows) = +270
   rows to `BOND_SPECS` and the old sentence was never updated
   (3,441 + 270 = 3,711, confirmed by per-code grouping). Not a data or
   pipeline problem. The "(built)" section now states 3,711 with the full
   explanation; `output/FACTS_LAB_REPORT.md` uses 3,711 throughout.
   The Alabama-vs-Ohio 1843 mismatch flagged alongside it is now
   **RESOLVED** -- root-caused and corrected in the table above (see
   "Alabama-vs-Ohio 1843 Discrepancy -- Root-Caused," 2026-08-25): the
   1843 row used an inconsistent yield-measure column, isolated to that
   one row, now corrected to 8.23%/8.18%/+0.05pp. See
   `output/numerical_consistency_check.md` for the original full sweep.

At the next meeting: present the Indiana tranche result and the two
Pennsylvania-city no-spillover confirmations (Philadelphia 2.68pp,
Pittsburgh 2.65pp, now strengthened by C-1260's immediate-reaction data
point) as the two headline results. Get a yes/no on Alabama and a quick
read on the Indiana deferred-coupon question, and the meeting's technical
agenda is complete -- everything else is ready for the paper as-is.

## 2026-09-02: Post-Meeting Follow-Up -- Indiana Tranche Issuance Timing (advisor Task 1)

Advisors asked for a more precise check of whether the five Indiana canal
codes (S-0470 "Indiana Canal", S-0480 Deferred, S-0490 Preferred, S-0500
Special Preferred, S-0506 Special Deferred) were all issued at one moment
in the 1847 Butler restructuring or in stages. This is a follow-up
subsection to the "2026-08-17: Canal/Robustness Comparison Script"
section above.

**1. Codebook has no issue-date field -- re-verified directly from the
raw file, not from memory.** `Securities Index.xls` "final" sheet has
exactly five columns: `Code | Name | Type | Interest rate | Maturity`.
"Sheet1" adds only `sort | from index file | Unnamed: 2` (bookkeeping
columns, all 0.0 for these codes). There is no issuance/authorizing-act
date anywhere in the codebook for any security, so the codebook cannot
answer the issuance-timing question at all. Maturity is blank for all
five canal codes; interest rate is "5s" for four of them and blank for
S-0470.

**2. Market-data first-quote dates on the New York exchange (from
`output/new_york_state_debt_prices.csv`, "Other State Debt" sheet) --
staged, but this is a trading-visibility fact, not an issuance date:**

| Code | Name | First NY quote | Last | n | Price range |
|---|---|---|---|---|---|
| S-0470 | Indiana Canal | 1850-01-19 | 1853-12-24 | 54 | 76.25-98.00 |
| S-0490 | Indiana Canal Preferred 5s | 1850-04-24 | 1853-07-09 | 65 | 10.00-49.50 |
| S-0500 | Indiana Canal Special Preferred 5s | 1850-09-18 | 1853-07-23 | 38 | 11.00-50.25 |
| S-0480 | Indiana Canal Deferred 5s | 1850-09-21 | 1852-12-01 | 22 | 6.00-50.00 |
| S-0506 | Indiana Canal Special Deferred 5s | 1851-01-01 | 1853-06-04 | 21 | 1.00-10.75 |

All five first appear in this price source in 1850-51, roughly three
years *after* the January 1847 supplemental act -- consistent with the
already-documented fact that these tranches contribute nothing to the
Feb/Apr 1843 policy-window test. The staggered first-quote order
(generic "Indiana Canal" -> Preferred -> Special Preferred/Deferred ->
Special Deferred) is real in the data but cannot be read as an issuance
sequence: first appearance in the New York quotation lists reflects when
a security became actively traded there, not when it was legally issued.

**3. Legislative history (web research, same source tier as the earlier
Butler Bill work -- Newcomer 1936 IMH, Indiana Historical Society
finding aid M0758/OM0392, Indiana History Blog, Wallis).** Original
Butler Bill passed January 1846; supplementary act "for the Funded debt
of the State of Indiana, and for the completion of the Wabash and Erie
Canal from Terre Haute to Evansville" approved January 27, 1847; Governor
Whitcomb conveyed all canal property to the three-man trust July 31,
1847. Sources describe old bonds being surrendered and "new bonds issued
to the holders" but give **no staged-rollout timeline** and **do not use
the words "preferred," "deferred," or "special" anywhere** -- confirmed
by re-querying Newcomer's text directly for those terms. As already
recorded in the 2026-08-17 verification-pass note, the codebook's tranche
names almost certainly reflect how these securities were labelled and
traded on Wall Street, not the statute's own language. No period
financial reference defining the four instrument names was located this
pass either.

**4. Is there an "anchor"/"original" bond among the five?** No codebook
entry is labelled "original." The pre-restructuring general-obligation
loan is a *separate* pair of codes -- S-0510/S-0540 ("Indiana
Dollar/Sterling 5s, 25 years"), already in the primary series. Among the
five canal codes, **S-0470 "Indiana Canal" is the odd one out**: no
coupon in the codebook, and it trades at 76-98 in 1850-53, far above the
four 5s tranches (which trade 1-50). Best inference (labelled as
inference, not confirmed): S-0470 is either a generic/aggregate
quotation or the surviving state-obligation portion of the settlement
(the half of the debt the state kept and resumed servicing as Indiana's
finances stabilised in the early 1850s), while S-0480/S-0490/S-0500/
S-0506 are the canal-revenue-dependent claims that stayed distressed
because canal toll revenue never materialised. S-0470 is already
excluded from the yield comparison (no coupon to compute from).

**Verdict: UNCLEAR / not resolvable from available records.** Same-date
1847 issuance can be neither confirmed nor refuted. The codebook is
silent on issue dates; the legislative-history sources describe a single
1846-47 settlement but give no rollout detail and never use the tranche
names; the staggered 1850-51 market appearance is a genuine data pattern
but is a trading-visibility fact, not an issuance date. Treated the same
way as the deferred-coupon question -- left as a live item for advisor
knowledge rather than forced.

## 2026-09-02: Post-Meeting Follow-Up -- Indiana Tranche Payment Mechanics (advisor Task 1b)

Hall's live follow-up ("who gets paid first, second") was about payment
mechanics, not issuance timing. Plain-English answer, for quotable use:

**Priority mapping (five codes):**
- **S-0490 "Indiana Canal Preferred 5s" and S-0500 "Indiana Canal
  Special Preferred 5s" -- PREFERRED. First claim on canal toll
  revenue.** (S-0500 "Special Preferred" trades consistently lower than
  plain S-0490 -- median price ~$20 vs ~$42 -- so within the preferred
  bucket there is a further sub-ordering; the pooled "preferred" average
  blends the two.)
- **S-0480 "Indiana Canal Deferred 5s" and S-0506 "Indiana Canal Special
  Deferred 5s" -- DEFERRED. Paid only after the preferred claims in any
  given period; S-0506 "Special Deferred" is the most junior of all
  (median price ~$9, and one 1851 print at $1.00).**
- **S-0470 "Indiana Canal" -- does NOT fit cleanly into either bucket.**
  It is a distinct, higher-grade instrument (no 5% coupon in the
  codebook; trades 76-98 while every tranche trades below 51). Most
  likely the state-obligation half of the settlement, not a canal-revenue
  tranche. Do not present it as "preferred" or "deferred."

**The dividing rule (preferred fully paid before deferred, or a
proportional split)?** The historical record checked does not state this
explicitly. Newcomer (1936, IMH, p. 110) confirms the *state-vs-canal*
split precisely -- "the principal and half the interest of these new
securities were to be paid by the state and the other half of the
interest was to be paid by the revenues of the canal" -- and confirms
the canal-revenue portion was genuinely contingent, not guaranteed
(p. 113: bondholders "saw their security steadily shrinking" as railroads
diverted traffic). But no source located this pass, or in the earlier
serious attempt (see 2026-08-17 verification pass), specifies whether
*preferred* holders had to be made whole before *deferred* holders
received anything, versus a fixed pro-rata division. Standard
19th-century "preferred"/"deferred" security mechanics would be strict
priority (senior satisfied in full first), same logic as modern
senior/subordinated debt -- but canal-revenue bonds are not guaranteed
to follow that convention, and this cannot be asserted from the sources.

**What the price data implies about the mechanism:** deferred bonds
traded at positive but deeply distressed prices throughout 1850-53 --
S-0480 mostly $6-15 (one $50 first print flagged as a likely data
anomaly), S-0506 $1-10.75. They were *not* priced at zero. So the market
expected deferred holders to receive *something* eventually (residual
value, or a share of proceeds if the canal were sold or reclaimed by the
state), i.e. not a total wipeout -- which argues against the strictest
reading ("deferred gets nothing until preferred is 100% satisfied, and
revenue never gets there"). At the same time preferred itself only
traded $20-50 (also well below par), so even the senior tranche was not
expected to be made whole. The overall picture the prices paint is a
strict-ish priority ordering in which *both* classes were impaired and
the deferred class was a highly subordinated residual claim -- but the
exact contractual rule (waterfall vs. pro-rata) remains an open
institutional-detail question for the advisors, alongside the
deferred-coupon question already on the agenda. **None of this changes
the 40.04pp price/yield gap finding, which is about the observed spread,
not the contractual mechanism.**

## 2026-09-02: City Default Mechanics -- Why the City Itself Stayed Solvent (advisor Task 2)

Distinct question from the market-pricing work already in this file. The
existing Philadelphia/Pittsburgh comparisons show the *bond market* did
not raise the city's borrowing cost when Pennsylvania defaulted (the
"no-spillover" finding). This section addresses the separate,
mechanical/legal question: why did the city of Philadelphia *itself* not
default, when the Commonwealth did? **Keep the two claims separate in the
paper -- "investors did not punish the city" (established, price-based)
vs. "the city stayed solvent because its finances were legally and
structurally separate from the state's" (this section, historical).**

**1. City and state finances were legally separate.** In 1840s
Pennsylvania, the city of Philadelphia and the ring of surrounding
districts (Northern Liberties, Southwark, Spring Garden, Kensington,
etc.) were each separate municipal corporations, each -- per the
Encyclopedia of Greater Philadelphia's Consolidation-Act essay -- holding
its own "powers to tax, borrow, and spend, and thus remained independent
of Philadelphia City's control," and all of them subordinate creations
of "the Commonwealth[,] which then, as now, held the power to create,
alter, and destroy local government." A municipal corporation of this era
is a distinct legal person with its own tax base and its own debt; the
state is not a co-obligor on municipal debt and the municipality is not a
co-obligor on state debt. This is a well-established general principle of
19th-century American municipal law -- flagged as such rather than
independently verified against an 1840s Pennsylvania statute or case in
this pass (see limitations).

**2. What Pennsylvania's state debt was for, and Philadelphia's
non-involvement.** Pennsylvania's ~$40M debt by 1841 was overwhelmingly
for the state-owned Main Line of Public Works (the Philadelphia-to-
Pittsburgh canal-and-portage-railroad system, ~$18M+ in construction
cost by 1834) plus other state canals and state investments in bank
stock. This was Commonwealth debt, serviced (inadequately) by state
canal tolls and state taxes. The city of Philadelphia was not a
co-obligor or guarantor on any of it -- the Main Line was a state asset,
not a municipal one. (Not independently re-verified against a bond
prospectus this pass; based on the standard secondary accounts -- Wallis,
Thomson, the Main Line histories.)

**3. What Philadelphia's own debt was for.** The city and districts
borrowed for genuinely municipal purposes with their own dedicated
revenue: the Fairmount Water Works and its expansions (municipal water,
sold to ratepayers), the Philadelphia Gas Works (from the 1830s,
municipal gas, sold to ratepayers), wharves, public buildings, district
street and drainage improvements, and -- from 1846 -- a large equity
subscription to the Pennsylvania Railroad. C-1100 ("Philadelphia 5s, r.
1846"), the bond used in this project's flagship city comparison, is a
city loan trading continuously from 1835, i.e. pre-dating the PRR
subscription. The city's revenue base -- municipal property tax plus
utility (water/gas) receipts -- was local and was not hit by the
collapse in *state* canal tolls and *state* tax shortfalls that drove
Pennsylvania's default.

**4. Direct historical statement?** Not located this pass. No contemporary
source was found that explicitly says, in so many words, "Philadelphia's
credit held while Pennsylvania's collapsed because X." The explanation
above is assembled from the structural facts (separate corporations,
separate revenue, no cross-guarantee) plus this project's own price
evidence, not from a single source that states the conclusion directly.
One adjacent, well-sourced fact: by the early 1850s the city proper had
become "far more heavily indebted than its neighbors" specifically
because of the PRR subscription -- so Philadelphia's credit was not
untouchable, it just was never in default; that strain is post-window
and railroad-driven, unrelated to the state's canal default.

**Limitations / open items:**
- The city/state legal-separation point rests on the general principle of
  19th-c municipal-corporation law plus the Consolidation-Act secondary
  essay, not an 1840s Pennsylvania statute or court case read directly.
- Philadelphia's non-co-obligor status on the Main Line debt is taken
  from standard secondary accounts, not from a state bond prospectus or
  the loan acts themselves.
- No single contemporary source stating the city-vs-state credit contrast
  outright was found; the writeup is inference from structure + this
  project's price data.
- Pittsburgh: the same municipal-corporation logic applies by analogy
  (Pennsylvania city, separate corporation), but was not researched
  city-specifically this pass.
