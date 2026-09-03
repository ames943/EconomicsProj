# FACTS LAB REPORT — 1840s State Debt Credibility Test

Dry, exhaustive, source-traced reference. No narrative framing, no
talking points, no meeting-prep material. Every number is re-verified
against the source CSV named beside it (verification run 2026-09-02, all
pipeline scripts reproduce byte-identically — `git status` clean after
rerun). Where a figure here differs from `PROJECT_CONTEXT.md` prose, the
difference is at the rounding level and is noted.

Working tree layout: `PROJECT_CONTEXT.md` is at the repository root; all
`scripts/`, `output/`, and `data/` paths below are under
`fiscal-history-project/`.

---

## 1. Research question

Did the transatlantic bond market treat the U.S. federal government's
early-1840s refusal to assume or bail out defaulting state debts as a
credible, permanent commitment? Operationalised as: after the no-bailout
signal, did bonds of states that defaulted carry persistently higher
yields than bonds of states that never defaulted, with "risky but
survived" states in between? Tested with computed yields from raw
secondary-market bond prices, 1830s–1850s, rather than from historical
narrative.

---

## 2. Data sources

| Source | File(s) in repo | Coverage | Contents |
|---|---|---|---|
| EH.net Early U.S. Securities Prices — New York | `data/raw/New-York.xls` | 1790–1865, weekly-ish | Sheets used: "NY State Debt" (New York state bonds), "Other State Debt" (other states' bonds quoted in NYC — Ohio, Alabama, Indiana, etc.), "City Debt" (NYC/Brooklyn municipal). Parsed to `output/new_york_state_debt_prices.csv` (3,492 date rows × 194 code columns). |
| EH.net Early U.S. Securities Prices — Philadelphia | `data/raw/Philadelphia1.xls` | 1786–1865 | Sheets used: "U.S. and State Debt" (Pennsylvania + some Ohio state bonds), "Municipal Debt" (Philadelphia city + county, Pittsburgh, Cincinnati, etc.). Parsed to `output/philadelphia_state_debt_prices.csv` (3,147 date rows × 37 code columns). |
| EH.net Securities Index (codebook) | `data/raw/Securities Index.xls` | 2,151 securities | Sheet "final": `Code | Name | Type | Interest rate | Maturity`. Sheet "Sheet1": same plus 3 bookkeeping columns. **No issue-date / authorizing-act field for any security.** Maps `S-####` / `C-####` codes to names, coupons, maturity years. |
| Bayley, "The National Loans of the United States" (1880 Census Vol. 7 ch.) | `data/raw/bayley_national_loans_1880.pdf`, `.txt` | 1776–1880 | History of *federal* Treasury loans. Retained for background only. Does **not** contain state-bond seniority/security detail — does not resolve any question in this project. |
| 1880 Census Vol. 7, Valuation/Taxation/Indebtedness | (URL only, not downloaded) | — | State debt totals as context. Not used for any number here. |

Date convention in the raw files: `year.monthday` float (e.g. `1841.0807`
= 1841-08-07). Parsing in `scripts/parse_securities.py` and
`scripts/compare_city_vs_state.py`.

Other EH.net city files (Baltimore, Boston, Charleston, New Orleans, etc.)
are **not downloaded**; not used.

### No-bailout reference date (anchor)

- **Primary anchor: February 1843**, specifically the Feb 11, 1843
  Gwin/McDuffie floor debate on assumption of state debts, 27th Congress
  3rd session (Tyler administration). Congressional Globe Vol. 12.
- Executive-branch confirmation: Christopher Hughes (U.S. consul, The
  Hague) to Dutch/British bankers, April–July 1843, denying any federal
  responsibility "for any default, actual or eventual" (Baring Papers,
  July 10, 1843).
- Earlier 1839–40 House episode (26th Congress, Van Buren, pre-default)
  explicitly ruled out as the anchor — it predates the actual defaults.
- **Evidence status:** two secondary sources (McGrane 1935; Thomson
  working paper) PLUS a manual primary-source read of the correct
  Congressional Globe volume (Gwin/Granger/Thompson, "Mississippi State
  Bonds," pages sitting ~8–9 printed pages before an already-confirmed
  Feb 16 1843 page). The **exact day (Feb 11 vs. an adjacent session day
  of the same multi-day debate) is not pinned** — neither page image
  carries a visible date stamp. Cite with that caveat; do not present as
  a pinned roll-call date. Full log: `output/anchor_date_source_check.md`,
  `output/anchor_date_manual_step.md`.

### Analysis windows

| Window | Definition | Role |
|---|---|---|
| Panic window | Pre-panic 1835–1837 vs. post-panic/default 1841–1845. Tests whether the 1837 economic shock itself repriced state risk. | Secondary / robustness |
| Policy window | Pre-signal 1841–Feb 11 1843 vs. post-signal **Apr 1 1843** onward. Tests the credibility question — divergence attributable to the federal refusal, holding the economic shock constant. | **Primary** |

Post-signal cutoff used in code: `1843-04-01`. Pre-signal cutoff for
observation counts: `1843-02-11`. The two are deliberately not identical
(Feb 11–Mar 31 1843 is treated as neither clean-pre nor clean-post).

---

## 3. Methodology

### 3.1 Yield formulas (`scripts/calculate_yields.py`)

- **Yield to maturity (YTM), Hastings/approximate:**
  `YTM = [C + (F − P)/n] / [(F + P)/2] × 100`
  where `C` = annual coupon per $100 face, `F` = 100, `P` = price, `n` =
  years to stated maturity. Used for **Pennsylvania, Ohio, New York** —
  states whose codebook entry gives an absolute maturity year.
- **Current yield:** `C / P × 100`. Used for **Alabama and Indiana** —
  Alabama has no codebook maturity field; Indiana's is "25 years" (a term
  length with no issue date to anchor it). YTM is not computable for
  these two. This is a genuine cross-state methodology inconsistency,
  carried openly in the `yield_measure_used` column, not hidden.
- Maturity date convention: codebook gives only a year; Jan 1 of that
  year is used as the maturity date.
- `current_yield` is always stored as a diagnostic column even when
  `yield` = YTM.

### 3.2 Truncation flags (rows kept in CSV, flagged not deleted)

- `excluded_past_maturity`: observation on/after the bond's maturity
  date. `yield` set to NA. (Several bonds traded past their nominal
  maturity — a non-redemption / distress signal in itself.)
- `excluded_near_maturity`: observation within 12 months before maturity.
  YTM computed and stored but flagged unreliable (denominator → 0
  amplifies quote noise; verified on S-1650's 1847–48 tail — std ~5×
  higher, final obs YTM = −8.8%).
- Standard analysis uses rows where **both** flags are False ("usable").

### 3.3 Active-default override (takes priority over the truncation flags)

For any observation whose date falls inside `DEFAULT_PERIODS[state]`,
**current yield is used instead of YTM regardless of years-to-maturity**,
and the near/past-maturity flags are cleared for those rows. Rationale:
YTM assumes redemption at par on schedule — invalid for an issuer already
missing scheduled payments. Surfaced by the S-2410 finding (YTM averaged
~30% across its whole window vs. ~9.5% current yield). Column:
`active_default_override` (bool) in `output/primary_yields.csv`.

`DEFAULT_PERIODS` (secondary-source dates — same caveat tier as the
anchor date; not primary-verified):
- **Pennsylvania: 1842-08-01 to 1845-02-01.** Suspended Aug 1842 interest;
  resumed after 1845 property-tax revenue reached $1.318M, back interest
  paid.
- **Indiana: 1841-01-01 to (open, through end of usable data 1848-12-09).**
  1846–47 Butler Bill was a restructuring, not a clean resumption; no
  in-window resumption date found.
- **Alabama: deliberately ABSENT** — per Wallis and others, Alabama raised
  direct taxation (early 1842) and used state-bank liquidation to keep
  paying; did not default in this episode. Alabama's current-yield
  treatment is justified *only* by missing maturity data.

### 3.4 Bond seniority handling

- Codebook `Type` field only distinguishes "Stock" vs. "Bond"
  (instrument form), not revenue source — cannot resolve seniority.
- Full codebook `Name`-field scan of all PA/OH/AL/IN/NY entries — 326
  distinct rows (per-state tallies of 41/11/46/29/200 sum to 327 because
  `B-1186` "Ohio and Pennsylvania", a railroad *corporate* bond, matches
  both state names; it is not a state bond and is irrelevant to
  seniority): PA and Alabama have **only** general-obligation (GO) bonds; Ohio has
  one revenue bond (S-2190, unusable — 2 obs, both 1825); Indiana has 5
  canal/revenue tranches (S-0470/0480/0490/0500/0506); New York has two
  parallel series — a GO series (S-1140–S-1656) and a canal/revenue
  series (S-1660–S-1980).
- **Decision (option a): primary cross-state comparison is GO-only.** The
  original NY pick (S-1750/S-1820/S-1950) was canal/revenue and is
  demoted to the secondary comparison. NY GO replacement went
  S-1320/S-1370/S-1560 → (all unusable, no 1839–43 data) → **S-1650**
  ("New York 7s, 1849"), the only NY GO code with continuous 1842–1848
  coverage. No continuous NY GO series exists past Dec 1848 (splice to
  S-1370 evaluated and rejected — different coupon/maturity, 399-day gap,
  pull-to-par distortion).
- Canal/revenue bonds (NY S-1750/1820/1950; Indiana tranches) are a
  labelled **secondary/robustness** comparison only.

---

## 4. State bucket assignments

| State | Bucket | Confidence | GO bond codes (primary) | Evidence |
|---|---|---|---|---|
| Pennsylvania | Defaulted | Confirmed | S-2240, S-2250, S-2270, S-2330, S-2410 (all "Pennsylvania 5s/6s, r. [year]") | Suspended interest Aug 1842; issued interest certificates not cash; resumed 1845. Marquee case. Hall & Sargent PA paper. |
| Indiana | Defaulted (partial / restructured) | Confirmed default; "partial" label = 1846–47 Butler Bill restructuring | S-0510, S-0540 ("Indiana Dollar/Sterling 5s, 25 years" — the pre-restructuring GO loan) | Defaulted Jan 1841. Butler Bill ceded Wabash & Erie Canal to creditors for half the debt. Wallis; Newcomer 1936. |
| Ohio | Safe (never defaulted) | Confirmed | S-2100, S-2110, S-2080, S-2010 ("Ohio 5s/6s, [year]") | No default in the episode. Dipped hard in the 1842 panic, fully recovered by 1844. Wallis; standard lists. |
| New York | Risky but survived | Bucket confirmed; empirical premium is weak/absent — see §6 | S-1650 ("New York 7s, 1849"), GO primary. Secondary: S-1750/S-1820/S-1950 (canal). | Faced railroad/bank-failure stress, never defaulted. 1838 Free Banking Act. Hall & Sargent NY paper. **Caveat: S-1650 has no data before Jul 1842, missing the worst of NY's 1839–42 stress.** |
| Alabama | Risky but survived | **ADVISOR-PENDING** (reclassified from "Defaulted") | S-0030, S-0040 ("Alabama 5s/6s [Sterling]") | Raised direct taxation early 1842 + state-bank liquidation to keep paying; not on standard 1840s default lists. 3 independent secondary sources (Wallis; two default-state lists). **Hall & Sargent have not personally confirmed.** The `~30¢-on-the-dollar` Alabama railroad-bond episode is Reconstruction-era (1867–76) and irrelevant to this window — resolved/dismissed. |

Bucket strings in code: `defaulted`, `safe`, `risky_but_survived`
(`STATE_BUCKET` dict, `scripts/calculate_yields.py`; also in the `bucket`
column of `output/primary_yields.csv`). Alabama's row currently reads
`risky_but_survived` with a "PENDING ADVISOR CONFIRMATION" code comment.

---

## 5. Final numeric results

All figures below re-verified 2026-09-02 against the named file. "n" is
observation count unless stated as "n_dates" (distinct dates after
grouping multi-code states by date). Yields in percent; spreads in
percentage points (pp).

### 5.1 Primary policy-window comparison — GO bonds, post-signal (≥ 1843-04-01)

Source: `output/primary_yields.csv` (via `scripts/calculate_yields.py`),
usable rows only, date-grouped mean of the `yield` column.

| State | Bucket | Mean yield | Range | n_dates | Post-signal span |
|---|---|---|---|---|---|
| Pennsylvania | Defaulted | 8.76% | 6.70–13.31 | 88 | 1843-04-01 … 1845-01-25 |
| Indiana | Defaulted | 13.87% | 10.61–21.74 | 203 | 1843-04-08 … 1848-12-09 |
| Alabama | Risky/survived* | 7.01% | 5.26–10.00 | 142 | 1843-04-08 … 1853-06-18 |
| Ohio | Safe | 5.78% | 2.77–11.06 | 444 | 1843-04-01 … 1853-12-14 |
| New York | Risky/survived | 5.37% | 4.07–7.00 | 117 | 1843-04-01 … 1848-01-01 |

\*Alabama bucket advisor-pending. Ohio's mean is pulled up by the 1843
tail of the panic recovery; see the yearly Alabama-vs-Ohio table for the
cleaner year-by-year picture.

**Direction of the result:** the two defaulted states (PA +~3pp over
Ohio in its short window; Indiana +~8pp) carry clear premia; Alabama sits
modestly above Ohio; New York sits at/below Ohio. Consistent with the
hypothesis for PA/Indiana, weak for NY (see §6).

### 5.2 Pennsylvania — active-default override effect

Source: `output/primary_yields.csv` vs.
`output/primary_yields_before_default_override.csv`. Window Apr 1843 –
Dec 1844, PA vs. Ohio, date-grouped.

| | PA mean | Ohio mean | Spread |
|---|---|---|---|
| Before override (inflated YTM) | 19.81% | 6.69% | **13.12pp** |
| After override (current yield in default window) | 8.77% | 6.69% | **2.08pp** |

The persistence claim survives but is ~2pp, not ~13pp. Do not cite the
13pp figure as a finding — it was a YTM artifact.

Per-bond override changes (from `PROJECT_CONTEXT.md`, "Result after
applying the override" table; underlying data in `primary_yields.csv`,
`active_default_override=True` rows):

| Code | Rows changed | Window | Old YTM mean | New current-yield mean |
|---|---|---|---|---|
| S-2240 | 8 (un-excluded) | Aug–Sep 1842 | NA (was excluded) | 12.49% |
| S-2250 | 7 | Aug–Sep 1842 | 33.47% | 12.79% |
| S-2270 | 12 | Aug 1842–Dec 1843 | 16.35% | 10.57% |
| S-2330 | 93 | Dec 1842–Dec 1844 | 9.64% | 8.74% |
| S-2410 | 101 | Dec 1842–Jan 1845 | 30.60% | 9.83% |

Total genuine yield-measure changes: 221 rows.

### 5.3 Alabama vs. Ohio, yearly (the "lands in between" test)

Source: `output/primary_yields.csv`, usable rows, full-calendar-year
date-grouped mean of `yield` (Alabama = current yield; Ohio = blended
YTM). Recomputed 2026-09-02.

| Year | Alabama | Ohio (safe) | Spread | n_dates AL / OH |
|---|---|---|---|---|
| 1843 | 8.23% | 8.18% | +0.04pp | 18 / 47 |
| 1844 | 6.24% | 6.13% | +0.12pp | 32 / 50 |
| 1845 | 7.11% | 6.31% | +0.81pp | 15 / 52 |
| 1846 | 7.45% | 6.73% | +0.72pp | 19 / 51 |
| 1847 | 8.26% | 6.22% | +2.04pp | 23 / 44 |
| 1848 | 8.12% | 6.11% | +2.01pp | 10 / 49 |
| 1850 | 6.21% | 4.83% | +1.38pp | 13 / 40 |
| 1851 | 5.71% | 4.75% | +0.95pp | 7 / 40 |
| 1852 | 5.47% | 4.45% | +1.02pp | 4 / 44 |
| 1853 | 5.45% | 4.44% | +1.01pp | 4 / 38 |

Rounding note: `PROJECT_CONTEXT.md` prose states the 1843 spread as
+0.05pp and 1847 Alabama as 8.22%; recomputation gives +0.04pp and 8.26%.
Difference is rounding / minor grouping; the qualitative reading ("opens
near-identical, widens to ~2pp by 1847–48, narrows but never fully
closes") is unchanged. 1851–53 rows have very few Alabama dates (n=4–7)
and should be treated as thin.

### 5.4 New York (S-1650) vs. Ohio, yearly

Source: `output/primary_yields.csv`, usable rows, calendar-year
date-grouped.

| Year | NY (S-1650) | Ohio | Spread |
|---|---|---|---|
| 1843 | 5.59% | 8.18% | −2.59pp |
| 1844 | 5.04% | 6.13% | −1.09pp |
| 1845 | 5.34% | 6.31% | −0.96pp |
| 1846 | 5.62% | 6.73% | −1.11pp |
| 1847 | 5.49% | 6.22% | −0.74pp |
| 1848 | 7.00% | 6.11% | +0.89pp (n=1 NY date) |

NY trades at or below "safe" Ohio for the entire observable window
except a single Jan-1848 observation. See §6 for the coverage caveat.

### 5.5 Indiana GO (S-0510/S-0540), yearly

Source: `output/primary_yields.csv`, current yield.

| Year | Mean yield | n_dates |
|---|---|---|
| 1843 | 16.55% | 47 |
| 1844 | 12.62% | 50 |
| 1845 | 14.47% | 45 |
| 1846 | 14.50% | 37 |
| 1847 | 12.61% | 30 |
| 1848 | 14.79% | 3 |

Indiana's GO bonds carry a large, sustained premium (~6–10pp over Ohio)
across the whole window — the strongest of the "defaulted" bucket for
GO bonds.

### 5.6 Panic-window price levels (context; source: raw price CSVs)

| Series | Pre-panic level (1835–40) | Panic trough | Recovery |
|---|---|---|---|
| PA S-2240/S-2250/S-2270 | 90–110 | 37–40 (Aug–Sep 1842) | none in window (PA in default) |
| Ohio S-2100 | ~90 | 52.0 (1842-03-26), yield peak 16.02% | to 93.8–104.0 by 1844 |
| Ohio S-2010 | ~89 | 48.0 (1842-04-09), yield peak 15.85% | (sparse after) |
| Ohio S-2110 | ~90 | 50.0 (1842-03-12), yield peak 12.83% | full by 1844 |
| Ohio S-2080 | ~90 | 51.75 (1842-03-12), yield peak 11.48% | full by 1844 |
| Alabama S-0030 | — (first obs 1842-02-19) | 40.0 | partial |
| Indiana S-0510 | — (first obs 1843-01-21) | 20.5 | never in window |
| NY canal S-1750 | — | 74.00 (pre-Jul 1842) | to ~100 by 1843–45 |
| NY canal S-1820 | — | 73.50 (pre-Jul 1842) | — |
| NY canal S-1950 | — | 76.00 (pre-Jul 1842) | — |

Ohio panic-window yield peaks source: `output/ohio_yield_check.csv` (560
rows, `scripts` — ad hoc, see §8). Ohio's yield rise is the **1837
panic, not the 1843 policy signal** — yields normalise to 6–7% starting
May 1843, before the signal could have driven a rise. Resolved: not a
contagion data point.

### 5.7 City vs. state (state-to-own-city spillover)

Source: `scripts/compare_city_vs_state.py` →
`output/city_vs_state_yields.csv` (1,843 rows);
`scripts/compare_city_vs_state_cincinnati_pittsburgh.py` →
`output/city_vs_state_cincinnati.csv` (1,673),
`output/city_vs_state_pittsburgh.csv` (1,772). Current yield both sides
(methodological parity — PA's own post-signal window is all current
yield via the override). City bond = `C-1100` "Philadelphia 5s, r. 1846"
(coupon 5, matures 1846, no near/past-maturity truncation applies).

| Comparison | Window | State mean | City mean | Spread (state − city) | n |
|---|---|---|---|---|---|
| Philadelphia vs. PA — pre-signal | 1835-01-17 … 1843-04-01 | 6.69% | 5.06% | **1.63pp** | 337 / 380 |
| Philadelphia vs. PA — post-gap overlap (apples-to-apples) | 1844-02-03 … 1844-12-07 | 7.56% | 4.88% | **2.68pp** | 41 / 41 |
| Pittsburgh vs. PA — post-signal | 1843-04-01 … 1845-01-25 | 8.76% | 6.11% | **2.65pp** | 88 / 83 |
| Cincinnati vs. Ohio — post-signal | 1843-04-01 … 1850-12-28 | 6.25% | 6.36% | **−0.11pp** | 322 / 339 |

- **C-1100 has a 343-day gap (1843-02-25 → 1844-02-04)** covering almost
  the entire immediate post-signal period. Philadelphia obs in
  1843-04-01…1844-02-03 = **0**. The pre/post widening (1.63 → 2.68pp) is
  driven entirely by PA's own yield rising; Philadelphia's is flat.
- Pittsburgh: 2.65pp ≈ Philadelphia's 2.68pp — a second PA-city
  replication of "no spillover."
- Cincinnati: −0.11pp ≈ zero — but Ohio never defaulted, so this is a
  **baseline contrast**, not a third confirmation: the city/state gap
  only opens when the state itself is under stress.
- Pre-signal thin-data rows (Cincinnati/Pittsburgh, n=5 each pre-signal)
  are explicitly NOT load-bearing.

### 5.8 Second Philadelphia bond (C-1260) — fills the C-1100 gap

Source: `output/philadelphia_second_bond_check.csv` (367 rows). C-1260
"Philadelphia 6s, r. 1852", its own gap is 1843-08-05 → 1844-03-23 (does
NOT overlap C-1100's gap). PA side = `primary_yields.csv` PA usable rows,
date-grouped.

| Window | Phila (C-1260) | PA state | Spread | n (city / state) |
|---|---|---|---|---|
| Strictly post-signal 1843-04-01 … 1843-08-05 | 5.59% | 11.53% | **5.95pp** | 19 / 19 |
| Full gap-fill 1843-02-25 … 1843-08-05 | 5.63% | 11.91% | **6.28pp** | 24 / 24 |

Both figures LARGER than the flagship 2.68pp post-gap number →
strengthens, not weakens, the no-spillover finding: a 6–7pp city/state
gap is visible *during* the immediate post-signal reaction. **Not yet
folded into `compare_city_vs_state.py` / its protected outputs** — lives
only in the diagnostic CSV. Supersedes an earlier miscounted "5.4pp,
n=10" figure.

### 5.9 NYC/Brooklyn vs. New York state

Source: `output/nyc_brooklyn_check.csv` (63 candidate codes, all
checked). No usable pre-signal baseline exists for any NYC/Brooklyn code
(densest pre-signal candidates are wrong-era or too gapped). Post-signal
levels comparison only, matched to S-1650's ceiling (Apr 1843 – Jan
1848): 6 codes used (C-0698, C-0660, C-0650, C-0695, C-0696, C-0320),
combined **≈5.56% (n=196)** vs. NY state S-1650 **5.37% (n=117)** →
**≈ −0.19pp** (city very slightly above state). Consistent with the
Cincinnati/Ohio pattern (safe state → no city gap). No pre/post test
possible; none forced.

### 5.10 Canal / robustness comparison

Source: `scripts/compare_canal_robustness.py` →
`output/canal_robustness_yields.csv` (329 rows);
`output/chart_canal_robustness.png`.

**New York canal bonds (YTM; NY never defaulted, no override):** usable
means over full observed windows — S-1750 5.83% (n=73, 1831–1848),
S-1820 5.32% (n=75, 1841–1848), S-1950 6.31% (n=35, 1842–1843). Two
handled data issues: S-1750's 1,666-day gap (Aug 1843 – Feb 1848)
rendered as a non-connecting dotted segment; S-1820's single price of
160.00 (1848-10-14, between prices of 96–99.5) — verified as a genuine
value in `New-York.xls` row 3256 but almost certainly an original
transcription error; kept in CSV, excluded from the chart line, its
−0.27% YTM flagged not plotted.

**Indiana Butler Bill canal tranches (current yield only — no codebook
maturity):**

| Group | Codes | Mean current yield | Median price | n (overlap window) |
|---|---|---|---|---|
| Preferred | S-0490 + S-0500 | 17.96% | $42.00 / $20.00 | 94 |
| Deferred | S-0480 + S-0506 | 57.99% | $14.25 / $9.00 | 43 |
| **Gap (deferred − preferred)** | | **40.04pp** | | |

Overlap window 1850-09-21 … 1853-06-04. Full-window preferred mean =
18.39% (n=103); deferred = 57.99% (n=43). All tranche data is 1850–1853
— postdates the policy window by years; this tests whether the market
priced the restructuring-created seniority split (it did, unambiguously),
not the 1843 signal.

S-0470 "Indiana Canal" excluded from the yield calc (blank coupon in
codebook); trades $76.25–$98.00, far above every tranche.
S-2190 "Ohio Canal 5s" dropped entirely (2 obs, both Oct 1825).

### 5.11 Indiana tranche sanity check

Source: `output/indiana_tranche_sanity_check.csv` (146 rows). The 40.04pp
gap survives S-2410-level scrutiny:
- Not thin-sample: 146 obs, 36 distinct months (preferred) / 27
  (deferred), ~2.7–3.3 year window.
- No YTM choice to get wrong (no maturity → current yield is the only
  computable method).
- No maturity-truncation contamination possible.
- Ordering robustness: in 90 of 91 nearby-date (±10 day) preferred vs.
  deferred pairs, preferred trades higher. The one exception is S-0480's
  own first print (1850-09-21, $50.00 — 2.4× its own second-highest value
  ever; flagged as a likely isolated anomaly).
- Within-group heterogeneity: S-0490 (median $42) vs. S-0500 (median $20)
  differ, but even S-0500 exceeds both deferred codes.
- **Open caveat:** current yield assumes the full 5% coupon was actually
  paid in cash. Whether the "deferred" tranche's coupon was *suspended*
  or merely *subordinated-but-paid* is unresolved (see §7). Affects how
  the "40.04pp" / "500%" yield figures should be worded, not the
  price-based finding.

### 5.12 Trade density / bank-held bonds

Source: `output/trade_density.csv` (23 codes: 14 primary + 9
secondary/canal). Flags sparse bonds; diagnostic only — **no existing
result was changed by this pass.**

| Code | State | Series | obs/month | Largest gap | Classification |
|---|---|---|---|---|---|
| S-0040 | Alabama | primary | 0.18 | 1,467 d | (c) unknown; weak state-bank link |
| S-2010 | Ohio | primary | 0.60 | 1,764 d | (c) unknown; leans "liquidity concentrated on S-2080" |
| S-1750 | NY | secondary/canal | 0.36 | 1,666 d | (a) bank-held — best circumstantial fit (1838 NY Free Banking Act; timing fits) |
| S-2190 | Ohio | secondary/canal | n/a | — | 2 obs total (1825); unusable regardless of cause |

None of the four are explained by the near/past-maturity mechanism (all
gaps are mid-life). Bank bond-backing was **not** a uniform 1840s
practice: NY 1838 Free Banking Act (best fit); Ohio 1845 Kelley Act
(too small, postdates the gap); Alabama/Indiana state-bank structures
don't map; PA had no such law (and no sparse PA bonds). All secondary-
source sourced.

---

## 6. Caveats and limitations on record

Severity: **H** = affects a headline number or its magnitude; **M** =
affects scope / how broadly a claim generalises; **L** = affects only
precise wording.

| # | Caveat | Severity |
|---|---|---|
| C1 | **YTM/current-yield mixed across states.** PA/OH/NY use YTM; AL/IN use current yield (no maturity data). The two measures diverge most when prices are far from par (mid-panic). The Alabama-vs-Ohio 1843 row was once miscomputed for exactly this reason. | H (comparability of AL/IN levels vs. OH) |
| C2 | **PA post-signal window ends ~Jan 1845.** Only S-2330/S-2410 give continuous post-signal coverage, and only to Dec 1844 / Jan 1845. PA's "persistence" is really a ~20-month test, not a decade. S-2240/S-2250 contribute nothing post-signal. | H (limits the PA persistence claim's horizon) |
| C3 | **NY GO series (S-1650) starts Jul 1842**, missing the worst of NY's 1839–42 stress (canal bonds troughed at 73.5–76 *before* Jul 1842). Cannot know whether the GO bond also dipped then. NY's "no measurable premium over Ohio" is substantially a data-coverage artifact. In the shared Jul-1842-onward window S-1650 never drops below 99.50 while canal bonds hit 78–89 — but canal bonds carry toll-revenue risk distinct from NY state credit. | H (undermines "NY = risky but survived" as an empirical result; NY reads closer to "safe") |
| C4 | **NY GO series ends Dec 1848.** No continuous NY GO series into the 1850s (splice rejected). NY has no long-run persistence data. | M |
| C5 | **Alabama bucket = advisor-pending.** Reclassification (Defaulted → Risky/survived) rests on 3 secondary sources; Hall & Sargent have not confirmed. If wrong, Alabama's "lands in between" reading is misframed. | H (bucket assignment of a headline state) |
| C6 | **Alabama & Indiana have no codebook maturity** → current yield forced; also cannot run the near/past-maturity check for them (a genuine blind spot). | M |
| C7 | **C-1100's 343-day gap** covers the immediate post-signal reaction period. The flagship Philadelphia/PA comparison's post-gap number (2.68pp) is a level check ~1 year later, not a reaction-speed test. Partly mitigated by C-1260 (§5.8) which is not yet in the protected script. | M (mitigated) |
| C8 | **City comparison = few pairs.** Philadelphia + Pittsburgh (both PA) for the "stress" case; Cincinnati + NYC/Brooklyn as safe-state baselines. Not "cities in general." | M |
| C9 | **Default-period dates** (PA Aug 1842 – Feb 1845; Indiana Jan 1841 – open) are web-search secondary sources, not primary. The override rule's boundaries depend on them. | M |
| C10 | **No-bailout anchor date** — Feb 11 1843 not pinned to the literal day (adjacent session day of the same multi-day debate is possible). Primary-source read confirms subject/participants/tight window, not the exact date. | L |
| C11 | **Indiana canal tranches are all 1850–1853** — postdate the policy window; the 40.04pp gap tests seniority pricing, not the 1843 signal. | L (finding is correctly scoped already) |
| C12 | **Indiana "deferred" coupon status unknown** — suspended vs. subordinated-but-paid. Affects wording of the 40.04pp / 500% *yield* figures, not the *price* finding. | L |
| C13 | **Indiana tranche issuance timing unresolved** (this pass, Task 1) — codebook has no issue dates; legislative sources give no rollout detail; 1850–51 market appearance is trading-visibility, not issuance. | L |
| C14 | **Indiana tranche payment mechanics** (this pass, Task 1b) — waterfall vs. pro-rata between preferred and deferred not stated in available sources; price data implies strict-ish priority with both classes impaired. | L |
| C15 | **City-stayed-solvent mechanism** (this pass, Task 2) — no single contemporary source states the city-vs-state credit contrast outright; explanation is inference from municipal-corporation law + separate revenue bases + this project's price data. | M |
| C16 | **Trade-density findings** for S-0040/S-2010/S-1750/S-2190 are circumstantial; no primary bank/Comptroller bond-holding records consulted. Does not overturn any current result (these codes aren't sole evidence for any chart). | L |
| C17 | **S-1820's 160.00 print** and **S-0480's $50.00 first print** are likely original-source transcription errors; kept in CSVs, excluded from chart lines. | L |
| C18 | **`primary_yields.csv` = 3,711 rows** (verified 2026-09-02). An older `PROJECT_CONTEXT.md` sentence said "3,441" — RESOLVED: that was correct when written (12-code `BOND_SPECS`); the PA Full Bond Re-Scan (commit `5519087`) later added S-2330 (93 rows) + S-2410 (177 rows) = +270, and the sentence was not updated. 3,441 + 270 = 3,711 exactly. Not a data or pipeline problem. `PROJECT_CONTEXT.md` now states 3,711 with this explanation; no conflicting count remains on record. | L |
| C19 | **`bayley_national_loans_1880.pdf`** does not resolve bond seniority (it is federal-loan history). Seniority rests on the codebook Name-field scan + Hall & Sargent NY paper + Wallis/Sylla/Grinath. | L (already handled) |

---

## 7. Open items

### 7.1 Needs advisor judgment (exact question)

1. **Alabama reclassification (Defaulted → Risky-but-survived): yes or
   no?** 3 independent secondary sources support it; Hall & Sargent said
   at the last meeting they weren't sure. Not resolvable by more
   analysis. Blocks stating the bucket as settled in the paper.
2. **Indiana "deferred" tranche coupon: was interest suspended, or paid
   but subordinated?** Determines whether the "40.04pp" and "500%" yield
   numbers should be described as realised cash yields or as
   price-implied. Does not touch the price-gap finding.
3. **Indiana canal tranche payment rule: strict waterfall (preferred
   100% before deferred gets anything) or fixed pro-rata split?** (New,
   from Hall's "who gets paid first, second" question — Task 1b.)
   Price data implies strict-ish priority with both classes impaired;
   the contractual rule is not in available sources.

### 7.2 Needs more research (what has been tried)

4. **Indiana tranche issuance timing** (Task 1). Tried: raw codebook
   (no issue-date field); `new_york_state_debt_prices.csv` first-quote
   dates (staggered 1850–51, but that's trading visibility); web search
   — Newcomer 1936 IMH, IHS finding aid M0758/OM0392, Indiana History
   Blog, Wallis, FRASER Commercial & Financial Chronicle 1876 supplement.
   None give a rollout timeline or use the tranche names. Likely needs
   the actual 1847 act text + trustees' records or advisor knowledge.
5. **City-stayed-solvent, direct source** (Task 2). Tried: Encyclopedia
   of Greater Philadelphia (Consolidation Act, Main Line, Gas Works,
   Fairmount essays), Wallis, Thomson, Main Line histories. Found the
   structural facts (separate corporations with own tax/borrow powers;
   Main Line was a state asset) but no source stating the city-vs-state
   credit contrast outright. Would need Philadelphia city financial
   reports / contemporary press for the 1840s.
6. **C-1260 into the protected `compare_city_vs_state.py`** — figures
   corrected everywhere (§5.8) but the script and its CSV/PNG still don't
   include C-1260. ~15 minutes of work, not advisor input.
7. **No-bailout anchor exact day** — a human clearing the UNT/Google
   Books CAPTCHA can read the day header on Congressional Globe Vol. 12
   pages ~283–292. Routes documented in
   `output/anchor_date_manual_step.md`.

### 7.3 Permanently unresolvable (why)

8. **S-0040 (Alabama) and S-2190 (Ohio canal) sparsity** — too few
   records survive; primary bank-holding registers for the relevant
   states are not digitised / not in scope. Not an open task, a known
   data limit.
9. **Whether NY's GO bond dipped in 1839–42** — S-1650 simply was not
   quoted before Jul 1842 in this data source. No amount of processing
   recovers a price that was never recorded.
10. **Exact original computation of the old (wrong) Alabama-vs-Ohio 1843
    row** — no saved script; root cause identified (wrong yield-measure
    column, unique to 1843 because of Ohio's price levels that year) but
    the exact prior number cannot be reconstructed to the hundredth.
    Corrected value now stands.

---

## 8. Scripts and output files

### 8.1 Scripts (`fiscal-history-project/scripts/`)

| Script | Produces | Notes |
|---|---|---|
| `parse_securities.py` | `output/new_york_state_debt_prices.csv`, `output/philadelphia_state_debt_prices.csv` | Parses state-debt sheets; tags NY source sheet before concatenating. |
| `identify_candidates.py` | `output/candidate_state_codes.csv` | Early heuristic candidate scan (231 rows). |
| `calculate_yields.py` | `output/primary_yields.csv` (3,711), `output/primary_yields_before_default_override.csv` (3,711) | **Core pipeline.** YTM/current-yield, truncation flags, active-default override. |
| `compare_city_vs_state.py` | `output/city_vs_state_yields.csv` (1,843), `output/chart_city_vs_state.png` | Philadelphia (C-1100) vs. PA. Reuses `primary_yields.csv` for the PA side. |
| `compare_city_vs_state_cincinnati_pittsburgh.py` | `output/city_vs_state_cincinnati.csv` (1,673), `output/city_vs_state_pittsburgh.csv` (1,772), `output/chart_cincinnati_vs_ohio.png`, `output/chart_pittsburgh_vs_pa.png` | Cincinnati vs. Ohio; Pittsburgh vs. PA. |
| `compare_canal_robustness.py` | `output/canal_robustness_yields.csv` (329), `output/chart_canal_robustness.png` | NY canal + Indiana tranches. Ohio dropped. |
| `pa_bridge_secondary.py` | `output/pa_bridge_secondary.csv` (276) | S-2460 extended-view bridge (secondary only). |
| `build_yield_charts.py` | `output/chart_panic_window.png`, `output/chart_policy_short_medium.png`, `output/chart_policy_long_term.png` | The three-tier primary chart set. |
| `export_charts_no_caption.py`, `export_charts_no_caption_extended.py` | `*_clean.png` versions | Caption-stripped for slides. |
| `build_presentation_charts.py` | `presentation_charts/` | Slide-formatted charts. |
| `plot_pa_default.py` | `output/pa_default_chart.png` | PA price + default marker. |
| `plot_ny_candidates.py` | `output/ny_candidates_chart.png` | NY candidate exploration. |
| `summary_table.py` | (console) | Summary stats. |
| `build_meeting_prep_doc.py` / `_v2` / `_v3` / `_final_private` | `output/meeting_prep_*.docx` / `.pdf` | Meeting-prep documents (NOT source-of-truth; this file is). |
| `test_setup.py` | (console) | Environment check. |

### 8.2 Output files with no dedicated script (ad hoc / diagnostic)

`output/trade_density.csv`, `output/ohio_yield_check.csv`,
`output/nyc_brooklyn_check.csv`, `output/philadelphia_second_bond_check.csv`,
`output/philadelphia_county_check.csv`,
`output/indiana_tranche_sanity_check.csv`. Each was computed by a one-off
script run and would need to be re-scripted to reproduce exactly. All are
diagnostic; none feed a chart or a headline number in the primary
pipeline.

### 8.3 Markdown notes in `output/`

`advisor_contagion_answer.md` (talking points — Hall's contagion
question), `anchor_date_source_check.md`, `anchor_date_manual_step.md`,
`numerical_consistency_check.md`. **This file (`FACTS_LAB_REPORT.md`) is
the source of truth for the paper; the `meeting_prep_*` docs and the
talking-points notes are not.**

### 8.4 Charts (`output/*.png`)

`chart_panic_window`, `chart_policy_short_medium`, `chart_policy_long_term`
(three-tier primary set; `_clean` variants exist),
`chart_city_vs_state`, `chart_cincinnati_vs_ohio`, `chart_pittsburgh_vs_pa`,
`chart_canal_robustness` (`_clean` variants exist), `pa_default_chart`,
`ny_candidates_chart`. `output/charts_v3_cropped/` holds cropped copies.

---

## 9. Traceability statement

Every number in §5 was recomputed 2026-09-02 from the CSV named beside
it. Pipeline scripts (`calculate_yields.py`, `compare_city_vs_state.py`,
`compare_city_vs_state_cincinnati_pittsburgh.py`,
`compare_canal_robustness.py`, `pa_bridge_secondary.py`) were rerun and
produce byte-identical output (`git status` clean).

**Claims that could NOT be fully traced to a repo file:**

- The per-bond override table in §5.2 (old vs. new means per code) is
  transcribed from `PROJECT_CONTEXT.md` prose; the underlying
  `active_default_override=True` rows are in `primary_yields.csv` but the
  summary means were not independently re-derived per code in this pass
  (the aggregate 13.12pp → 2.08pp and the 221-row count WERE re-verified).
- All historical dates and institutional facts in §2–§4 (anchor date,
  default periods, bucket evidence, Butler Bill chronology, municipal-law
  points) trace to **secondary sources**, not to files in the repo. The
  repo contains only the price data and the codebook. These are flagged
  at their point of use and in §6.
- `bayley_national_loans_1880.pdf/.txt` is in `data/raw/` but is used for
  nothing — retained as background only.
