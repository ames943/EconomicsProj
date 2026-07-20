"""Print a console-only summary table: price at the nearest available date to
Jan 1841 and Aug 1842, and the percent decline between them, for the 3 PA
default candidates and 8 NY "recovered quickly" candidates.
"""

from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

PA_CSV = OUTPUT_DIR / "philadelphia_state_debt_prices.csv"
NY_CSV = OUTPUT_DIR / "new_york_state_debt_prices.csv"

PA_CODES = ["S-2240", "S-2250", "S-2270"]
NY_CODES = ["S-2100", "S-2110", "S-2080", "S-2010", "S-0030", "S-0040", "S-0510", "S-0540"]

JAN_1841 = pd.Timestamp("1841-01-01")
AUG_1842 = pd.Timestamp("1842-08-01")


MAX_GAP_DAYS = 45  # beyond this, treat as "no data near this date" rather than misleading


def nearest_valid(s: pd.Series, target: pd.Timestamp):
    """Nearest date (and value) to target among dates where s is non-null.
    Returns (None, None) if the closest available point is more than
    MAX_GAP_DAYS away (series didn't exist / wasn't recorded yet)."""
    s = s.dropna()
    gaps = (s.index - target).map(lambda d: abs(d.days))
    idx = s.index[gaps.argmin()]
    if gaps.min() > MAX_GAP_DAYS:
        return None, None
    return idx, s.loc[idx]


def main():
    pa = pd.read_csv(PA_CSV, index_col=0, parse_dates=True).sort_index()
    ny = pd.read_csv(NY_CSV, index_col=0, parse_dates=True).sort_index()

    rows = []
    for code in PA_CODES:
        jd, jp = nearest_valid(pa[code], JAN_1841)
        ad, ap = nearest_valid(pa[code], AUG_1842)
        pct_decline = 100 * (jp - ap) / jp if jp and ap else None
        rows.append(("PA", code, jd, jp, ad, ap, pct_decline))

    for code in NY_CODES:
        jd, jp = nearest_valid(ny[code], JAN_1841)
        ad, ap = nearest_valid(ny[code], AUG_1842)
        pct_decline = 100 * (jp - ap) / jp if jp and ap else None
        rows.append(("NY", code, jd, jp, ad, ap, pct_decline))

    print("(Price shown is from the nearest date with non-missing data for that")
    print(" specific bond, since not every code is populated on the same week.")
    print(f" 'N/A' means no price recorded within {MAX_GAP_DAYS} days of the target date.)")
    print()
    header = f"{'Grp':<4}{'Code':<9}{'Jan Date':<12}{'Jan Price':>10}  {'Aug Date':<12}{'Aug Price':>10}{'% Decline':>12}"
    print(header)
    print("-" * len(header))
    for grp, code, jd, jp, ad, ap, pct in rows:
        jd_s = str(jd.date()) if jd is not None else "N/A"
        jp_s = f"{jp:.2f}" if jp is not None else "N/A"
        ad_s = str(ad.date()) if ad is not None else "N/A"
        ap_s = f"{ap:.2f}" if ap is not None else "N/A"
        pct_s = f"{pct:.1f}%" if pct is not None else "N/A"
        print(
            f"{grp:<4}{code:<9}{jd_s:<12}{jp_s:>10}  {ad_s:<12}{ap_s:>10}{pct_s:>12}"
        )


if __name__ == "__main__":
    main()
