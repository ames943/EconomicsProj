"""Compute bond yields for the primary general-obligation state comparison
(Pennsylvania/Ohio/Alabama/Indiana, all defaulted-or-safe, vs. New York's
general-obligation series) from parsed EH.net price data.

Yield methodology
------------------
- Yield-to-maturity (approximate/Hastings formula):
      YTM = [C + (F - P) / n] / [(F + P) / 2] * 100
  where C = annual coupon (dollars per $100 face), F = 100 (face value),
  P = price, n = years remaining to stated maturity. Used for Pennsylvania,
  Ohio, and New York, whose codebook entries give an absolute maturity year.
- Current yield (C / P * 100): used for Alabama and Indiana, whose codebook
  entries do not give a usable absolute maturity date -- Alabama has no
  maturity field at all, and Indiana's "25 years" is a term length with no
  issue date to anchor it. YTM cannot be computed for these two states.
  This is a genuine cross-state inconsistency in yield methodology, kept
  and flagged rather than hidden (see yield_measure_used column).

Maturity-date convention: the codebook gives only a maturity YEAR (e.g.
1850), not a specific date. Jan 1 of that year is used as the reference
maturity date throughout, consistent with the maturity-proximity check
that established the truncation rule below.

Truncation rule (flags rows for exclusion from primary trend analysis;
does not remove any row from the output CSV)
------------------------------------------------------------------------
- excluded_past_maturity: observation date on/after the bond's own stated
  maturity date. YTM is undefined here without a real redemption date --
  several bonds kept trading months to years past their nominal maturity
  (a distress/non-redemption signal in its own right, not a data error;
  see PROJECT_CONTEXT.md). Yield is NOT computed for these rows.
- excluded_near_maturity: observation within 12 months before maturity.
  YTM is computed but numerically unstable this close to maturity (the
  formula's denominator, years-to-maturity, shrinks toward zero and
  amplifies ordinary price-quote noise into large yield swings) -- see
  the S-1650 1847-48 tail finding in PROJECT_CONTEXT.md. Flagged for
  exclusion from primary trend lines; value retained for transparency.

Active-default override (takes priority over the truncation rule above)
------------------------------------------------------------------------
YTM assumes the bond redeems at full face value on schedule. That
assumption is unsound for an issuer already known to be missing
scheduled redemptions -- not just close to one bond's own maturity, but
for the whole stretch it is in default. For any observation whose date
falls inside DEFAULT_PERIODS[state], current yield is used instead of
YTM regardless of years-to-maturity, and the near/past-maturity
exclusion flags do not apply (they exist specifically to guard YTM's
maturity-proximity math, which is moot once YTM isn't being used).
See PROJECT_CONTEXT.md for the S-2410 finding that surfaced this and
source citations for the default/resumption dates below.

Alabama is deliberately NOT in DEFAULT_PERIODS: per Wallis and other
secondary sources, Alabama raised taxes and liquidated its state bank to
keep meeting its debt service, and did not default in this episode
despite being under similar pressure. Its current-yield treatment is
justified solely by missing codebook maturity data (see NO_MATURITY_
STATES), not by default status. The bucket label "defaulted" used for
Alabama throughout this project should be revisited -- see
PROJECT_CONTEXT.md.
"""

import re
from pathlib import Path
from typing import Optional

import pandas as pd
import xlrd

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
CODEBOOK_PATH = RAW_DIR / "Securities Index.xls"

FACE_VALUE = 100.0
NEAR_MATURITY_YEARS = 1.0

STATE_BUCKET = {
    "Pennsylvania": "defaulted",
    "Ohio": "safe",
    "Alabama": "defaulted",
    "Indiana": "defaulted",
    "New York": "risky_but_survived",
}

# Alabama and Indiana have no usable absolute maturity date in the codebook
# (Alabama: blank; Indiana: "25 years" term length, no issue date to anchor
# it) -- these states always use current yield, never YTM.
NO_MATURITY_STATES = {"Alabama", "Indiana"}

# Active-default windows: (start, end). end=None means "still in default
# through the end of this state's usable data" (no clean resumption date
# found within the analysis window). Sources: suspension/resumption dates
# corroborated via Wallis (2004/2005) and secondary summaries of the 1840s
# state-default episode (see PROJECT_CONTEXT.md for citations and caveats
# -- these rest on web-search-summarized secondary sources, not a primary-
# document read, same caveat level as the no-bailout anchor date).
# Alabama is intentionally absent: per those same sources, Alabama did not
# default in this episode.
DEFAULT_PERIODS = {
    "Pennsylvania": (pd.Timestamp("1842-08-01"), pd.Timestamp("1845-02-01")),
    "Indiana": (pd.Timestamp("1841-01-01"), None),
}

BOND_SPECS = [
    {"code": "S-2240", "state": "Pennsylvania", "source": "pa"},
    {"code": "S-2250", "state": "Pennsylvania", "source": "pa"},
    {"code": "S-2270", "state": "Pennsylvania", "source": "pa"},
    {"code": "S-2330", "state": "Pennsylvania", "source": "pa"},
    {"code": "S-2410", "state": "Pennsylvania", "source": "pa"},
    {"code": "S-2100", "state": "Ohio", "source": "ny_other"},
    {"code": "S-2110", "state": "Ohio", "source": "ny_other"},
    {"code": "S-2080", "state": "Ohio", "source": "ny_other"},
    {"code": "S-2010", "state": "Ohio", "source": "ny_other"},
    {"code": "S-0030", "state": "Alabama", "source": "ny_other"},
    {"code": "S-0040", "state": "Alabama", "source": "ny_other"},
    {"code": "S-0510", "state": "Indiana", "source": "ny_other"},
    {"code": "S-0540", "state": "Indiana", "source": "ny_other"},
    {"code": "S-1650", "state": "New York", "source": "ny_state"},
]


def load_codebook() -> dict:
    """Code -> (name, coupon_pct, maturity_year_or_None)."""
    wb = xlrd.open_workbook(CODEBOOK_PATH)
    sh = wb.sheet_by_name("final")
    out = {}
    for r in range(1, sh.nrows):
        code, name, _type, interest, maturity = sh.row_values(r)
        match = re.match(r"^(\d+(?:\.\d+)?)s?$", str(interest).strip())
        coupon = float(match.group(1)) if match else None
        mat_year = int(maturity) if isinstance(maturity, float) and maturity else None
        out[code] = (name, coupon, mat_year)
    return out


def load_price_series(spec: dict, pa_df: pd.DataFrame, ny_df: pd.DataFrame) -> pd.Series:
    if spec["source"] == "pa":
        return pa_df[spec["code"]].dropna()
    if spec["source"] == "ny_other":
        return ny_df[f"Other State Debt::{spec['code']}"].dropna()
    if spec["source"] == "ny_state":
        return ny_df[f"NY State Debt::{spec['code']}"].dropna()
    raise ValueError(spec["source"])


def compute_ytm(price: pd.Series, coupon: float, n_years: pd.Series) -> pd.Series:
    return (coupon + (FACE_VALUE - price) / n_years) / ((FACE_VALUE + price) / 2) * 100


def in_default_period(state: str, dates: pd.DatetimeIndex) -> pd.Series:
    if state not in DEFAULT_PERIODS:
        return pd.Series(False, index=dates)
    start, end = DEFAULT_PERIODS[state]
    mask = dates >= start
    if end is not None:
        mask &= dates < end
    return pd.Series(mask, index=dates)


def build_bond_frame(spec: dict, price: pd.Series, coupon: float, mat_year: Optional[int]) -> pd.DataFrame:
    state = spec["state"]
    current_yield = coupon / price * 100
    default_override = in_default_period(state, price.index)

    if state in NO_MATURITY_STATES or mat_year is None:
        yield_measure = pd.Series("current_yield", index=price.index)
        yield_value = current_yield
        excluded_near = pd.Series(False, index=price.index)
        excluded_past = pd.Series(False, index=price.index)
    else:
        maturity_date = pd.Timestamp(f"{mat_year}-01-01")
        n_years = (maturity_date - price.index).days / 365.25
        excluded_past = n_years <= 0
        excluded_near = (n_years > 0) & (n_years <= NEAR_MATURITY_YEARS)

        ytm = compute_ytm(price, coupon, n_years)
        yield_value = ytm.where(~excluded_past, other=pd.NA)
        yield_measure = pd.Series("ytm", index=price.index)
        yield_measure = yield_measure.mask(excluded_past, pd.NA)

        # Active-default override takes priority: YTM's par-redemption
        # assumption doesn't hold for an issuer already missing scheduled
        # redemptions, regardless of years-to-maturity. Un-excludes rows
        # that were near/past-maturity flagged too, since that flag exists
        # only to guard YTM math that no longer applies here.
        yield_value = yield_value.where(~default_override, current_yield)
        yield_measure = yield_measure.mask(default_override, "current_yield")
        excluded_near = excluded_near & ~default_override
        excluded_past = excluded_past & ~default_override

    return pd.DataFrame(
        {
            "date": price.index,
            "state": state,
            "code": spec["code"],
            "price": price.values,
            "coupon": coupon,
            "yield_measure_used": yield_measure.values,
            "yield": yield_value.values,
            "current_yield": current_yield.values,
            "bucket": STATE_BUCKET[state],
            "series_label": "primary",
            "excluded_near_maturity": pd.Series(excluded_near).values,
            "excluded_past_maturity": pd.Series(excluded_past).values,
            "active_default_override": default_override.values,
        }
    )


def main() -> None:
    codebook = load_codebook()
    pa_df = pd.read_csv(OUTPUT_DIR / "philadelphia_state_debt_prices.csv", index_col=0, parse_dates=True)
    ny_df = pd.read_csv(OUTPUT_DIR / "new_york_state_debt_prices.csv", index_col=0, parse_dates=True)

    frames = []
    print(f"{'code':8} {'state':12} {'coupon':>6} {'maturity':>8} {'total':>6} {'past_mat':>9} {'near_mat':>9} {'usable':>7}  usable_range")
    for spec in BOND_SPECS:
        name, coupon, mat_year = codebook[spec["code"]]
        price = load_price_series(spec, pa_df, ny_df)
        frame = build_bond_frame(spec, price, coupon, mat_year)
        frames.append(frame)

        total = len(frame)
        past = int(frame["excluded_past_maturity"].sum())
        near = int(frame["excluded_near_maturity"].sum())
        usable_mask = ~frame["excluded_past_maturity"] & ~frame["excluded_near_maturity"]
        usable = frame.loc[usable_mask]
        rng = (
            f"{usable['date'].min().date()} to {usable['date'].max().date()}"
            if len(usable)
            else "NONE"
        )
        print(
            f"{spec['code']:8} {spec['state']:12} "
            f"{('n/a' if coupon is None else f'{coupon}%'):>6} "
            f"{(mat_year or 'n/a'):>8} {total:>6} {past:>9} {near:>9} {len(usable):>7}  {rng}"
        )

    out = pd.concat(frames, ignore_index=True).sort_values(["state", "code", "date"])
    out_path = OUTPUT_DIR / "primary_yields.csv"
    out.to_csv(out_path, index=False)
    print(f"\nSaved -> {out_path}  ({len(out)} rows)")


if __name__ == "__main__":
    main()
