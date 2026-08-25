"""Cincinnati (city) vs. Ohio (state) and Pittsburgh (city) vs. Pennsylvania
(state) yield comparisons -- extends the Philadelphia-vs-Pennsylvania
comparison (scripts/compare_city_vs_state.py, NOT modified by this script)
to the two other city bond series flagged as usable in PROJECT_CONTEXT.md's
"City-Level Bonds -- Scoping Check" section.

Correction to the task framing: Pittsburgh compares against PENNSYLVANIA,
not Ohio
--------------------------------------------------------------------------
The task that requested this script described both comparisons loosely as
"Cincinnati/Pittsburgh vs. Ohio's S-2100/S-2110/S-2080/S-2010" -- but
Pittsburgh is a Pennsylvania city, not an Ohio one (already flagged in
PROJECT_CONTEXT.md's Not-Yet-Done list: "Pittsburgh vs. (no direct state
analog -- it's in Pennsylvania too, a second PA city comparison point)").
Per the task's own stated principle -- "compare the city's yield against
its OWN state's existing primary series" -- Cincinnati is compared to
Ohio, and Pittsburgh is compared to Pennsylvania (a second Philadelphia-
style test, not a repeat of the Ohio comparison).

Data source
-----------
Both C-0436 ("Cincinnati 6s") and C-1394 ("Pittsburg 6s") live on
Philadelphia1.xls's "Municipal Debt" sheet -- the same sheet C-1100
(Philadelphia) came from, already downloaded, no new file needed. Parsed
directly with the same paired code/code+"a" column convention and
"year.monthday" float date convention as compare_city_vs_state.py and
parse_securities.py.

Density check (see PROJECT_CONTEXT.md's caution about C-1100's hidden
343-day gap -- checked properly this time, not just total-obs/date-range)
---------------------------------------------------------------------------
Both cities: no gap over 90 days anywhere in their observed range (largest
gaps: C-0436 63 days, Aug-Oct 1848; C-1394 63 days, Dec 1848-Feb 1849) --
dense, continuous POST-signal coverage, unlike C-1100's gap problem.

BUT unlike C-1100 (dense on both sides of the Apr 1843 signal, 1835-1844),
both C-0436 and C-1394 only start trading Dec 31 1842 -- three months
before the Feb 11 1843 policy cutoff -- with just 5 observations each in
the ~6-week pre-signal window (Dec 31 1842-Jan 28 1843). This is NOT a
Philadelphia-style pre/post comparison; it is structurally closer to the
NYC/Brooklyn candidates already flagged in PROJECT_CONTEXT.md ("most NYC
candidates only start quoting at or after the signal, so they can't
support a pre/post-signal comparison... only a post-signal levels/trend
comparison"). The 5-observation pre-signal means are computed and reported
below for completeness, but are NOT treated as a load-bearing pre/post
divergence test -- per the task's own instruction not to force a
spillover/no-spillover verdict from insufficient data. The real test here
is a POST-signal LEVEL comparison: does the city trade persistently below
its state (as Philadelphia did) or does it move together with it?

Active-default check
---------------------
Neither city needed an override:
- Ohio (the state) never defaulted in this episode at all -- no override
  logic applies to Ohio's own primary series either.
- No historical record of a Pittsburgh-specific default distinct from
  Pennsylvania's state-level Aug 1842-Feb 1845 default was found (same
  absence-of-evidence already established for Philadelphia). The raw
  C-1394 price series corroborates this qualitatively: it opens already
  depressed (75-80, consistent with the tail of the general 1842 panic
  across all bonds, not a distress event of its own) and recovers to
  par/above-par (100-102) by 1844 -- nothing resembling Pennsylvania
  STATE's collapse to 37-40. Not independently re-verified against a
  primary source for Pittsburgh specifically -- inherited from the
  Philadelphia finding by analogy, flagged as such.

Coupon / maturity / yield measure
-----------------------------------
Neither C-0436 nor C-1394 has a maturity year in Securities Index.xls
(blank maturity field, same situation as Alabama/Indiana's primary
codes) -- both are ALWAYS current yield (coupon 6.0 / price x 100), never
YTM. No near/past-maturity truncation applies (mechanically impossible
without a maturity date), matching the NO_MATURITY_STATES convention in
calculate_yields.py.

Yield-measure parity, handled differently per pair (both flagged
explicitly, not hidden, per this project's established practice for
Alabama/Indiana's current-yield-vs-YTM mismatch in the primary comparison)
------------------------------------------------------------------------
- Cincinnati vs. Ohio: Ohio's own primary series (S-2100/S-2110/S-2080/
  S-2010) is reused as-is from primary_yields.csv -- mostly YTM (Ohio has
  real maturity dates and never defaulted, so the active-default override
  never applies to it). Cincinnati is current yield. This IS a genuine
  YTM-vs-current-yield mismatch, same category as the Alabama/Indiana
  situation already flagged and accepted elsewhere in this project --
  not hidden, called out here and in the chart footnote.
- Pittsburgh vs. Pennsylvania: Pennsylvania's own usable post-signal
  window (S-2330/S-2410, through Jan 25 1845) falls entirely inside PA's
  DEFAULT_PERIODS window (Aug 1842-Feb 1845), so it is ALREADY all
  current yield via the active-default override -- exactly the situation
  compare_city_vs_state.py already documented for Philadelphia. Current
  yield for both sides here is genuine parity, not a new choice.

Coverage ceilings (do not force a comparison past either side's real data)
---------------------------------------------------------------------------
- Cincinnati vs. Ohio: Ohio's primary series has dense coverage through
  Dec 1853 (S-2080/S-2110), comfortably covering Cincinnati's full range
  (through Dec 1850) -- no ceiling problem for this pair.
- Pittsburgh vs. Pennsylvania: Pennsylvania's own usable primary series
  ends Jan 25 1845 (the already-documented PA coverage ceiling -- see
  PROJECT_CONTEXT.md's "PA Full Bond Re-Scan" section), even though
  Pittsburgh itself keeps trading through Dec 1850. The matched post-
  signal comparison for this pair is therefore capped at Jan 25 1845,
  NOT compared through 1850 -- Pittsburgh's own price/yield trend past
  that date is still plotted (there is no reason to hide it), but with
  no Pennsylvania line to compare against past the ceiling.

Outputs
-------
- output/city_vs_state_cincinnati.csv
- output/city_vs_state_pittsburgh.csv
- output/chart_cincinnati_vs_ohio.png
- output/chart_pittsburgh_vs_pa.png
"""

import textwrap
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

PHILADELPHIA_XLS = RAW_DIR / "Philadelphia1.xls"
MUNICIPAL_SHEET = "Municipal Debt"

SIGNAL = pd.Timestamp("1843-04-01")
PRE_SIGNAL_CUTOFF = pd.Timestamp("1843-02-11")
PA_DEFAULT = pd.Timestamp("1842-08-01")
PA_COVERAGE_CEILING = pd.Timestamp("1845-01-25")  # PA's own primary series ends here

SURFACE = "#fcfcfb"
PRIMARY_TEXT = "#0b0b0b"
SECONDARY_TEXT = "#52514e"
MUTED_TEXT = "#898781"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
SIGNAL_COLOR = "#e34948"
DEFAULT_COLOR = "#9a6b00"
STATE_COLOR = "#2a78d6"
CITY_COLOR = "#1f9e6d"  # third distinct color, not reused from Philadelphia (#7a3fc9)

CITY_SPECS = {
    "Cincinnati": {
        "code": "C-0436",
        "coupon": 6.0,
        "state": "Ohio",
        "coverage_ceiling": None,  # Ohio's own series stays dense through 1853
        "out_csv": "city_vs_state_cincinnati.csv",
        "out_chart": "chart_cincinnati_vs_ohio.png",
        "yield_parity_note": (
            "Ohio's series is reused as-is (mostly YTM -- Ohio never defaulted, so its "
            "active-default override never applies). Cincinnati is current yield (no maturity "
            "date in the codebook). This is a genuine YTM-vs-current-yield mismatch, the same "
            "category already flagged and accepted for Alabama/Indiana elsewhere in this "
            "project -- not hidden here either."
        ),
    },
    "Pittsburgh": {
        "code": "C-1394",
        "coupon": 6.0,
        "state": "Pennsylvania",
        "coverage_ceiling": PA_COVERAGE_CEILING,
        "out_csv": "city_vs_state_pittsburgh.csv",
        "out_chart": "chart_pittsburgh_vs_pa.png",
        "yield_parity_note": (
            "Pennsylvania's own usable post-signal window (through Jan 25 1845) falls entirely "
            "inside PA's active-default period, so it is already all current yield -- current "
            "yield for both sides here is genuine parity, the same situation already established "
            "for Philadelphia vs. Pennsylvania."
        ),
    },
}


def excel_year_monthday_to_datetime(series: pd.Series) -> pd.Series:
    as_str = series.astype(float).map(lambda v: f"{v:.4f}")
    year = as_str.str.slice(0, 4)
    month_day = as_str.str.split(".").str[1].str.ljust(4, "0")
    month = month_day.str.slice(0, 2)
    day = month_day.str.slice(2, 4)
    date_str = year + month + day
    return pd.to_datetime(date_str, format="%Y%m%d", errors="coerce")


def load_municipal_sheet() -> pd.DataFrame:
    wb = xlrd.open_workbook(PHILADELPHIA_XLS)
    sh = wb.sheet_by_name(MUNICIPAL_SHEET)
    header = sh.row_values(0)
    rows = [sh.row_values(r) for r in range(1, sh.nrows)]
    df = pd.DataFrame(rows, columns=header)
    df.index = excel_year_monthday_to_datetime(df[df.columns[0]])
    return df


def load_city_price_series(sheet_df: pd.DataFrame, code: str) -> pd.Series:
    price = pd.to_numeric(sheet_df[code].replace("", pd.NA), errors="coerce")
    price.index = sheet_df.index
    return price.dropna().sort_index()


def load_state_yield_series(state: str) -> pd.Series:
    """Reuses the state's existing primary series as-is from
    primary_yields.csv -- never recomputed, per instructions not to touch
    calculate_yields.py or primary_yields.csv."""
    df = pd.read_csv(OUTPUT_DIR / "primary_yields.csv", parse_dates=["date"])
    df = df[
        (df.state == state)
        & (df.series_label == "primary")
        & ~df.excluded_past_maturity
        & ~df.excluded_near_maturity
    ]
    return df.groupby("date")["yield"].mean().sort_index()


def build_comparison_frame(city_price: pd.Series, coupon: float, city_name: str,
                            state: str, state_df: pd.DataFrame) -> pd.DataFrame:
    city_yield = coupon / city_price * 100
    city_out = pd.DataFrame(
        {
            "date": city_price.index,
            "level": "city",
            "entity": city_name,
            "state": city_name,
            "code": CITY_SPECS[city_name]["code"],
            "price": city_price.values,
            "coupon": coupon,
            "yield_measure_used": "current_yield",
            "yield": city_yield.values,
            "current_yield": city_yield.values,
            "bucket": "no_default_confirmed",
            "excluded_near_maturity": False,
            "excluded_past_maturity": False,
        }
    )

    state_out = state_df.copy()
    state_out["level"] = "state"
    state_out["entity"] = state

    cols = [
        "date", "level", "entity", "state", "code", "price", "coupon",
        "yield_measure_used", "yield", "current_yield", "bucket",
        "excluded_near_maturity", "excluded_past_maturity",
    ]
    return pd.concat([state_out[cols], city_out[cols]], ignore_index=True).sort_values(["level", "date"])


def print_spread_summary(city_name: str, city_yield: pd.Series, state_yield_by_date: pd.Series) -> None:
    spec = CITY_SPECS[city_name]
    state = spec["state"]
    ceiling = spec["coverage_ceiling"]

    pre_city = city_yield[city_yield.index < PRE_SIGNAL_CUTOFF]
    pre_state = state_yield_by_date[
        (state_yield_by_date.index >= city_yield.index.min()) & (state_yield_by_date.index < PRE_SIGNAL_CUTOFF)
    ]
    print(f"=== {city_name} vs. {state} ===")
    print(f"Pre-signal window ({city_yield.index.min().date()} to {PRE_SIGNAL_CUTOFF.date()}) "
          f"-- THIN, n={len(pre_city)} city obs, NOT a load-bearing comparison:")
    print(f"  {state} (state): mean {pre_state.mean():.2f}%  n={len(pre_state)}")
    print(f"  {city_name} (city): mean {pre_city.mean():.2f}%  n={len(pre_city)}")
    print()

    post_end = ceiling if ceiling is not None else city_yield.index.max()
    post_city = city_yield[(city_yield.index >= SIGNAL) & (city_yield.index <= post_end)]
    post_state = state_yield_by_date[(state_yield_by_date.index >= SIGNAL) & (state_yield_by_date.index <= post_end)]
    ceiling_note = f" (capped at {state}'s own coverage ceiling, {post_end.date()})" if ceiling is not None else ""
    print(f"Post-signal window ({SIGNAL.date()} to {post_end.date()}){ceiling_note}, the load-bearing comparison:")
    print(f"  {state} (state): mean {post_state.mean():.2f}%  n={len(post_state)}")
    print(f"  {city_name} (city): mean {post_city.mean():.2f}%  n={len(post_city)}")
    print(f"  Spread (state - city): {post_state.mean() - post_city.mean():.2f}pp")
    print()


def new_fig():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.grid(True, color=GRID_COLOR, linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(AXIS_COLOR)
    ax.tick_params(colors=MUTED_TEXT, labelsize=9)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    return fig, ax


def build_chart(city_name: str, comparison: pd.DataFrame) -> None:
    spec = CITY_SPECS[city_name]
    state = spec["state"]
    fig, ax = new_fig()

    state_series = comparison[comparison.level == "state"].groupby("date")["yield"].mean().sort_index()
    ax.plot(state_series.index, state_series.values, color=STATE_COLOR, linewidth=2, solid_capstyle="round")
    ax.annotate(
        f"{state} (state)", xy=(state_series.index[-1], state_series.values[-1]), xytext=(6, 0),
        textcoords="offset points", color=STATE_COLOR, fontsize=9, fontweight="bold", va="center", ha="left",
    )

    city_series = comparison[comparison.level == "city"].set_index("date")["yield"].sort_index()
    ax.plot(city_series.index, city_series.values, color=CITY_COLOR, linewidth=2, solid_capstyle="round")
    ax.annotate(
        f"{city_name} (city, no default)", xy=(city_series.index[-1], city_series.values[-1]), xytext=(6, -10),
        textcoords="offset points", color=CITY_COLOR, fontsize=9, fontweight="bold", va="center", ha="left",
    )

    if state == "Pennsylvania":
        ax.axvline(PA_DEFAULT, color=DEFAULT_COLOR, linestyle="--", linewidth=1.3)
        ax.annotate(
            "PA Default\n(Aug 1842)", xy=(PA_DEFAULT, 0), xytext=(6, 6),
            textcoords="offset points", color=DEFAULT_COLOR, fontsize=9, fontweight="bold", va="bottom", ha="left",
        )
        ax.axvline(PA_COVERAGE_CEILING, color=MUTED_TEXT, linestyle=":", linewidth=1.1)
        y_mid = ax.get_ylim()[0] + 0.5 * (ax.get_ylim()[1] - ax.get_ylim()[0])
        ax.annotate(
            "PA state series\ncoverage ends", xy=(PA_COVERAGE_CEILING, y_mid), xytext=(6, 0),
            textcoords="offset points", color=MUTED_TEXT, fontsize=7.5, va="center", ha="left", style="italic",
        )

    ax.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.3)
    ax.annotate(
        "No-bailout signal\n(Apr 1843)", xy=(SIGNAL, ax.get_ylim()[1]), xytext=(6, -6),
        textcoords="offset points", color=SIGNAL_COLOR, fontsize=9, fontweight="bold", va="top", ha="left",
    )

    ax.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=11)
    ax.set_ylabel("Yield (%)", color=PRIMARY_TEXT, fontsize=11)
    ax.set_title(
        f"City vs. State Yields -- {city_name} (city) vs. {state} (state)",
        color=PRIMARY_TEXT, fontsize=13, fontweight="bold", loc="left",
    )

    method_note = (
        f"{city_name} ({spec['code']}, 6s, no codebook maturity date) is always current yield "
        f"(coupon/price x 100), no near/past-maturity truncation applies. {spec['yield_parity_note']} "
        f"{city_name}'s pre-signal coverage is thin (5 obs, Dec 31 1842-Jan 28 1843, right before the "
        "Feb 11 1843 cutoff) -- NOT a Philadelphia-style pre/post divergence test; the load-bearing "
        "comparison here is post-signal LEVELS only, same caveat already applied to the NYC/Brooklyn "
        "candidates in PROJECT_CONTEXT.md. This chart is one city/state pair only; see "
        "chart_city_vs_state.png (Philadelphia/PA) for the original comparison."
    )
    wrapped_lines = []
    for paragraph in method_note.split("\n"):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=155) or [""])
    wrapped = "\n".join(wrapped_lines)
    fig.text(0.01, 0.01, wrapped, color=SECONDARY_TEXT, fontsize=8, ha="left", va="bottom")
    bottom_margin = 0.02 + 0.018 * len(wrapped_lines)
    fig.tight_layout(rect=(0, bottom_margin, 1, 1))

    out_path = OUTPUT_DIR / spec["out_chart"]
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print(f"saved -> {out_path}")


def run_pair(city_name: str, sheet_df: pd.DataFrame) -> None:
    spec = CITY_SPECS[city_name]
    state = spec["state"]

    city_price = load_city_price_series(sheet_df, spec["code"])
    city_yield = spec["coupon"] / city_price * 100

    state_yields_raw = pd.read_csv(OUTPUT_DIR / "primary_yields.csv", parse_dates=["date"])
    state_df = state_yields_raw[
        (state_yields_raw.state == state)
        & (state_yields_raw.series_label == "primary")
        & ~state_yields_raw.excluded_past_maturity
        & ~state_yields_raw.excluded_near_maturity
    ]

    comparison = build_comparison_frame(city_price, spec["coupon"], city_name, state, state_df)
    out_path = OUTPUT_DIR / spec["out_csv"]
    comparison.to_csv(out_path, index=False)
    print(f"saved -> {out_path} ({len(comparison)} rows)")
    print()

    state_yield_by_date = load_state_yield_series(state)
    print_spread_summary(city_name, city_yield, state_yield_by_date)

    build_chart(city_name, comparison)
    print()


def main() -> None:
    sheet_df = load_municipal_sheet()
    for city_name in ["Cincinnati", "Pittsburgh"]:
        run_pair(city_name, sheet_df)


if __name__ == "__main__":
    main()
