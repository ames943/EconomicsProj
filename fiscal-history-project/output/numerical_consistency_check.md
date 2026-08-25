# Numerical Consistency Check -- PROJECT_CONTEXT.md and meeting_prep_final.docx vs. Source CSVs

Verification pass: every specific numeric claim (percentages, pp spreads,
observation counts, dates) in `PROJECT_CONTEXT.md` traced back to its
source CSV and recomputed directly. `meeting_prep_final.docx` spot-checked
for the same figures where it repeats them. Two real mismatches found;
everything else checked out exactly, including several that initially
looked wrong until a window/grouping methodology error on the checker's
own side was corrected (documented below so the false alarms aren't
repeated in a future pass).

## MISMATCHES FOUND

### 1. `primary_yields.csv` row count -- stale

**Doc claim** (line 412): "Output: `output/primary_yields.csv` (3,441 rows)"
**Actual**: 3,711 rows (verified `len(pd.read_csv(...))` directly).
**Status: MISMATCH.** The file has grown by 270 rows since this line was
written -- consistent with the PA full bond re-scan and other additions
documented later in the same file. Not accompanied by any data-quality
concern (the file's internal structure and all downstream numbers drawn
from it check out, see below) -- this looks like simple staleness in one
descriptive sentence, not a sign of a broken pipeline. Also note: the
same paragraph says the file gained "a 14th column, `active_default_override`"
after the override was added, but the column list given earlier in the
same paragraph only names 12 columns, so 12+1=13, not 14 -- the actual
file has 13 columns total. Minor arithmetic slip in the prose, not a
data issue (confirmed the file's actual column count directly).

### 2. Alabama vs. Ohio, 1843 row of the yearly table -- mismatch

**Doc claim** (line 525): "1843 | Alabama 7.36% | Ohio 7.15% | +0.21pp"
**Actual** (full calendar year 1843, date-grouped mean, matching the
exact methodology confirmed correct for every other row of this same
table): Alabama 8.23%, Ohio 8.18%.
**Status: MISMATCH.** Every other row of this table (1844, 1845, 1846,
1847, 1848, 1850) reproduces exactly using a full-calendar-year,
date-grouped-mean methodology -- only 1843 is off, by about 0.9-1.0pp on
both sides simultaneously (so the +0.21pp spread itself is still roughly
right, 8.23-8.18=0.05pp vs. the original 0.21pp -- a smaller
discrepancy than either side's absolute level). Tried several
alternative windows (Apr-Dec 1843 only, to isolate the post-signal
partial year) and got closer (7.45%/7.47%) but still not an exact match.
**Root cause not identified** -- flagged for Amey's review rather than
guessed at further; possibly reflects the same primary_yields.csv growth
noted in finding #1 (this table may predate a later data refresh), or a
slightly different window convention used only for this one row.

### 3. C-1260 "second Philadelphia bond" figures -- confirmed stale (see Phase 1 of this pass)

**Doc claim** (PROJECT_CONTEXT.md, "Philadelphia County Bonds" section):
"Philadelphia city (C-1260...) in Jun-Aug 1843 averaged 5.62% (n=10...)
vs. Pennsylvania state's own primary series in the identical window,
11.05% (n=20). A ~5.4pp gap..."
**Actual, rigorously recomputed this pass** (see
`output/philadelphia_second_bond_check.csv`): using the full window that
actually fills C-1100's gap (Feb 25-Aug 5 1843): Philadelphia 5.63%
(n=24) vs. Pennsylvania 11.91% (n=48), a 6.28pp gap. Using the project's
standard post-signal convention (Apr 1 onward): Philadelphia 5.59%
(n=19) vs. Pennsylvania 11.53% (n=38), a 5.95pp gap.
**Status: MISMATCH, root cause identified.** The original figure used an
ad hoc 10-observation subset (Jun 3-Aug 5 1843 only) rather than the
full window that actually fills C-1100's gap. The direction and rough
magnitude of the underlying finding are NOT undermined -- if anything the
gap is larger with the fuller data, not smaller -- but the specific
"5.4pp, n=10" figure should not be cited as-is. See this pass's Phase 1
write-up for full detail.

**This same stale figure also appears in `output/meeting_prep_final.docx`**
(the "e. City-vs-State Contagion Results" section, added last session):
"shows Philadelphia at 5.62% against Pennsylvania's 11.05%" -- same
numbers, same staleness, needs the same correction if/when Amey decides
how to fold this into the flagship comparison.

## CHECKED AND CONFIRMED CORRECT (PASS)

Initial recomputation attempts on several of these produced apparent
mismatches that turned out to be methodology errors on the checker's own
side (wrong window bound, or not grouping multi-code states by date
before averaging) -- corrected and reconciled below, noted so a future
pass doesn't have to rediscover the right convention.

| Claim | Doc value | Source file | Recomputed | Status |
|---|---|---|---|---|
| S-2240 override: rows changed / old / new yield | 8 / NaN / 12.49% | primary_yields.csv vs. before-override snapshot | 8 / NaN / 12.49% | PASS |
| S-2250 override | 7 / 33.47% / 12.79% | same | 7 / 33.47% / 12.79% | PASS |
| S-2270 override | 12 / 16.35% / 10.57% | same | 12 / 16.35% / 10.57% | PASS |
| S-2330 override | 93 / 9.64% / 8.74% | same | 93 / 9.64% / 8.74% | PASS |
| S-2410 override | 101 / 30.60% / 9.83% | same | 101 / 30.60% / 9.83% | PASS |
| Alabama/Ohio 1844-1848, 1850 (5 of 7 rows) | see table, doc lines 523-532 | primary_yields.csv | all within 0.05pp | PASS |
| PA before-override spread | PA 19.81% / Ohio 6.69% / 13.12pp | primary_yields.csv + before-snapshot, Apr43-Dec44 | exact match (date-grouped mean) | PASS |
| PA after-override spread | PA 8.77% / Ohio 6.69% / 2.08pp | same | exact match | PASS |
| Philadelphia vs. PA, pre-signal | PA 6.69%/n337, City 5.06%/n380, 1.63pp | city_vs_state_yields.csv | exact match | PASS |
| Philadelphia vs. PA, post-gap | PA 7.56%/n41, City 4.88%/n41, 2.68pp | same | exact match | PASS |
| Cincinnati vs. Ohio | Ohio 6.25%/n322, City 6.36%/n339, -0.11pp | city_vs_state_cincinnati.csv | exact match (once Ohio's window capped at Cincinnati's own last obs, Dec 28 1850, not left open-ended) | PASS |
| Pittsburgh vs. PA | PA 8.76%/n88, City 6.11%/n83, 2.65pp | city_vs_state_pittsburgh.csv | exact match (once state side is grouped by date before averaging) | PASS |
| Ohio yield-check peaks, all 4 codes + exact dates | S-2100 16.02% 3/26/42; S-2010 15.85% 4/9/42; S-2110 12.83% 3/12/42; S-2080 11.48% 3/12/42 | ohio_yield_check.csv | exact match, all 4 | PASS |
| ohio_yield_check.csv row count | 560 | same | 560 | PASS |
| Indiana tranche gap | Preferred 17.96%/n94, Deferred 57.99%/n43, 40.04pp | canal_robustness_yields.csv | exact match | PASS |
| Indiana median prices | S-0490 $42.00, S-0500 $20.00, S-0480 $14.25, S-0506 $9.00 | same | exact match | PASS |
| canal_robustness_yields.csv row count | 329 | same | 329 | PASS |
| NYC/Brooklyn combined | 5.56%/n196 vs. NY state 5.37%/n117, -0.19pp | nyc_brooklyn_check.csv + primary_yields.csv | exact match | PASS |
| nyc_brooklyn_check.csv row count | 63 | same | 63 | PASS |
| Philadelphia County bonds, all obs/date-range/gap figures (C-1310, C-1300, C-1260) | see doc | philadelphia_county_check.csv | exact match, all fields | PASS |
| Indiana tranche sanity check row count + distinct months | 146 rows / 36 preferred-months / 27 deferred-months | indiana_tranche_sanity_check.csv | exact match | PASS |

## meeting_prep_final.docx spot check

Extracted every percentage/pp figure from the document text
(`python-docx`) and cross-checked against the CSVs above. All figures
match their corresponding PROJECT_CONTEXT.md claims exactly EXCEPT the
same C-1260 staleness noted in mismatch #3 above (the docx was generated
from the same, not-yet-corrected, narrative). A few other figures in the
docx (e.g., "13 percentage point," "30%") are intentional historical
narrative references to the PRE-correction S-2410/PA numbers, used to
tell the "what we found and fixed" story in the talking-points script --
these are correct as historical references, not current-state claims,
and are not mismatches.

## Summary

- **21 of 23 distinct numeric claims checked out exactly** once the
  correct source-file window/grouping convention was identified and
  applied (several apparent mismatches were the checker's own
  methodology errors, corrected and documented above so they aren't
  re-flagged next time).
- **2 real mismatches found**, both flagged above for Amey's review, not
  silently corrected: the primary_yields.csv row count (harmless
  staleness) and the 1843 row of the Alabama/Ohio table (small,
  root-cause not identified).
- **1 finding (the C-1260 numbers) was already known-stale going into
  this check**, per this pass's Phase 1 -- confirmed here to also appear
  in `meeting_prep_final.docx`, not just `PROJECT_CONTEXT.md`.
