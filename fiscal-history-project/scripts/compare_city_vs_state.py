"""Philadelphia (city) vs. Pennsylvania (state) yield comparison.

Scoped narrowly to this one city/state pair -- Cincinnati, Pittsburgh, and
NYC/Brooklyn are separate, unverified candidates flagged for later (see
PROJECT_CONTEXT.md) and are deliberately NOT included here.

Data source and a known gap
----------------------------
Philadelphia's bond (C-1100, "Philadelphia 5s, r. 1846") lives on
Philadelphia1.xls's "Municipal Debt" sheet, which `parse_securities.py`
has never touched (that script only parses the "U.S. and State Debt"
sheet). This script parses it directly, the same way `parse_securities.py`
parses state-debt sheets (paired code/code+"a" columns, "year.monthday"
float dates).

**Known 343-day gap: Feb 25 1843 to Feb 3 1844.** C-1100 has ZERO
observations for almost the entire immediate post-signal period (the
Apr 1843 no-bailout signal falls inside this gap). This was missed by an
earlier scoping-check pass that only looked at C-1100's overall date
range (1835-1844) and total observation count (421) without checking for
internal gaps -- exactly the kind of mistake this project has hit before
with code picks (see PA/NY bond re-scan history in PROJECT_CONTEXT.md).
The gap means the city's *immediate* reaction to the Apr 1843 signal
cannot be observed -- only its level from Feb 1844 onward. The chart
renders this gap explicitly (dotted segment, annotated), and the
pre/post-signal spread tables below are computed over the gap-aware
windows described in each function's docstring, not by pretending the
gap isn't there.

Why current yield for both sides, not YTM
-------------------------------------------
Pennsylvania's own primary series (`calculate_yields.py`) uses YTM by
default, but PA's entire usable post-signal window (S-2330/S-2410,
Dec 1842-Jan 1845) falls inside PA's own `DEFAULT_PERIODS` window
(Aug 1842-Feb 1845), so in practice ALL of PA's post-signal comparison
points already use current yield via the active-default override, not
YTM. Computing YTM for Philadelphia while PA is on current yield would
reintroduce exactly the yield-measure mismatch this project flagged and
fixed for Alabama/Indiana (see PROJECT_CONTEXT.md). Current yield for
both sides is therefore genuine methodological parity for this specific
comparison, not a simplification.

Confirmed separately (see PROJECT_CONTEXT.md, "Philadelphia vs.
Pennsylvania Yield Comparison"): C-1100 never approaches its own 1846
maturity within its observed window (last obs Dec 1844, a full year
before the 12-month near-maturity window would even open), so no
near/past-maturity truncation applies. And Philadelphia the city shows no
price pattern resembling default (mild dip to 91-94 in late 1842-early
1843, full recovery to 101-104.5 by 1844) and no historical record of a
city-level suspension distinct from the state's -- so no active-default
override is applied to it either.

Outputs
-------
- output/city_vs_state_yields.csv
- output/chart_city_vs_state.png
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
CITY_CODE = "C-1100"
CITY_COUPON = 5.0  # "Philadelphia 5s, r. 1846" (Securities Index.xls)

GAP_START = pd.Timestamp("1843-02-25")  # C-1100's last obs before the gap
GAP_END = pd.Timestamp("1844-02-03")  # C-1100's first obs after the gap
SIGNAL = pd.Timestamp("1843-04-01")  # no-bailout signal (falls inside the gap)
PA_DEFAULT = pd.Timestamp("1842-08-01")

SURFACE = "#fcfcfb"
PRIMARY_TEXT = "#0b0b0b"
SECONDARY_TEXT = "#52514e"
MUTED_TEXT = "#898781"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
SIGNAL_COLOR = "#e34948"
DEFAULT_COLOR = "#9a6b00"
STATE_COLOR = "#2a78d6"  # Pennsylvania -- same blue as build_yield_charts.py
CITY_COLOR = "#7a3fc9"  # Philadelphia -- new color, not reused from the state palette


def excel_year_monthday_to_datetime(series: pd.Series) -> pd.Series:
    """Convert a 'year.monthday' float (e.g. 1841.0807) to a datetime.

    Same convention as parse_securities.py: integer part is the year,
    fractional part read as a 4-digit zero-padded number is month+day.
    """
    as_str = series.astype(float).map(lambda v: f"{v:.4f}")
    year = as_str.str.slice(0, 4)
    month_day = as_str.str.split(".").str[1].str.ljust(4, "0")
    month = month_day.str.slice(0, 2)
    day = month_day.str.slice(2, 4)
    date_str = year + month + day
    return pd.to_datetime(date_str, format="%Y%m%d", errors="coerce")


def load_city_price_series() -> pd.Series:
    wb = xlrd.open_workbook(PHILADELPHIA_XLS)
    sh = wb.sheet_by_name(MUNICIPAL_SHEET)
    header = sh.row_values(0)
    rows = [sh.row_values(r) for r in range(1, sh.nrows)]
    df = pd.DataFrame(rows, columns=header)
    dates = excel_year_monthday_to_datetime(df[df.columns[0]])
    price = pd.to_numeric(df[CITY_CODE].replace("", pd.NA), errors="coerce")
    price.index = dates
    return price.dropna().sort_index()


def load_state_yield_series() -> pd.Series:
    """PA's existing primary series (already YTM/current-yield-blended,
    truncation-applied) -- reused as-is, not recomputed, per instructions
    not to touch primary_yields.csv or calculate_yields.py."""
    df = pd.read_csv(OUTPUT_DIR / "primary_yields.csv", parse_dates=["date"])
    df = df[
        (df.state == "Pennsylvania")
        & (df.series_label == "primary")
        & ~df.excluded_past_maturity
        & ~df.excluded_near_maturity
    ]
    return df.groupby("date")["yield"].mean().sort_index()


def build_comparison_frame(city_price: pd.Series, pa_state: pd.DataFrame) -> pd.DataFrame:
    city_yield = CITY_COUPON / city_price * 100
    city_out = pd.DataFrame(
        {
            "date": city_price.index,
            "level": "city",
            "entity": "Philadelphia",
            "state": "Philadelphia",
            "code": CITY_CODE,
            "price": city_price.values,
            "coupon": CITY_COUPON,
            "yield_measure_used": "current_yield",
            "yield": city_yield.values,
            "current_yield": city_yield.values,
            "bucket": "no_default_confirmed",
            "excluded_near_maturity": False,
            "excluded_past_maturity": False,
        }
    )

    pa_out = pa_state.copy()
    pa_out["level"] = "state"
    pa_out["entity"] = "Pennsylvania"

    cols = [
        "date", "level", "entity", "state", "code", "price", "coupon",
        "yield_measure_used", "yield", "current_yield", "bucket",
        "excluded_near_maturity", "excluded_past_maturity",
    ]
    return pd.concat([pa_out[cols], city_out[cols]], ignore_index=True).sort_values(["level", "date"])


def print_spread_summary(city_price: pd.Series, pa_yield_by_date: pd.Series) -> None:
    city_yield = CITY_COUPON / city_price * 100
    matched_start = city_yield.index.min()

    pa_pre = pa_yield_by_date[(pa_yield_by_date.index >= matched_start) & (pa_yield_by_date.index < SIGNAL)]
    city_pre = city_yield[(city_yield.index >= matched_start) & (city_yield.index < SIGNAL)]
    print(f"Matched pre-signal window ({matched_start.date()} to {SIGNAL.date()}):")
    print(f"  Pennsylvania (state): mean {pa_pre.mean():.2f}%  n={len(pa_pre)}")
    print(f"  Philadelphia (city):  mean {city_pre.mean():.2f}%  n={len(city_pre)}")
    print(f"  Spread: {pa_pre.mean() - city_pre.mean():.2f}pp")
    print()

    pa_overlap = pa_yield_by_date[(pa_yield_by_date.index >= GAP_END) & (pa_yield_by_date.index <= city_yield.index.max())]
    city_overlap = city_yield[(city_yield.index >= GAP_END) & (city_yield.index <= city_yield.index.max())]
    print(f"Post-gap overlap window ({GAP_END.date()} to {city_yield.index.max().date()}), apples-to-apples:")
    print(f"  Pennsylvania (state): mean {pa_overlap.mean():.2f}%  n={len(pa_overlap)}")
    print(f"  Philadelphia (city):  mean {city_overlap.mean():.2f}%  n={len(city_overlap)}")
    print(f"  Spread: {pa_overlap.mean() - city_overlap.mean():.2f}pp")
    print()

    gap_window = city_yield[(city_yield.index >= SIGNAL) & (city_yield.index < GAP_END)]
    print(f"Confirming the data gap: Philadelphia obs in {SIGNAL.date()}-{GAP_END.date()} = {len(gap_window)}")


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


def build_chart(comparison: pd.DataFrame) -> None:
    fig, ax = new_fig()

    pa = comparison[comparison.level == "state"].groupby("date")["yield"].mean().sort_index()
    ax.plot(pa.index, pa.values, color=STATE_COLOR, linewidth=2, solid_capstyle="round")
    ax.annotate(
        "Pennsylvania (state, defaulted)", xy=(pa.index[-1], pa.values[-1]), xytext=(6, 0),
        textcoords="offset points", color=STATE_COLOR, fontsize=9, fontweight="bold", va="center", ha="left",
    )

    city = comparison[comparison.level == "city"].set_index("date")["yield"].sort_index()
    seg1 = city[city.index <= GAP_START]
    seg2 = city[city.index >= GAP_END]
    ax.plot(seg1.index, seg1.values, color=CITY_COLOR, linewidth=2, solid_capstyle="round")
    ax.plot(seg2.index, seg2.values, color=CITY_COLOR, linewidth=2, solid_capstyle="round")
    ax.plot([GAP_START, GAP_END], [seg1.values[-1], seg2.values[0]], color=CITY_COLOR, linewidth=1, linestyle=":", alpha=0.6)
    ax.annotate(
        "Philadelphia (city, no default)", xy=(seg2.index[-1], seg2.values[-1]), xytext=(6, -10),
        textcoords="offset points", color=CITY_COLOR, fontsize=9, fontweight="bold", va="center", ha="left",
    )
    ax.annotate(
        "no data (343-day gap)", xy=(GAP_START, seg1.values[-1]), xytext=(0, 18), textcoords="offset points",
        color=CITY_COLOR, fontsize=7.5, ha="left", va="bottom", style="italic",
    )

    ax.axvline(PA_DEFAULT, color=DEFAULT_COLOR, linestyle="--", linewidth=1.3)
    ax.annotate(
        "PA Default\n(Aug 1842)", xy=(PA_DEFAULT, 0), xytext=(6, 6),
        textcoords="offset points", color=DEFAULT_COLOR, fontsize=9, fontweight="bold", va="bottom", ha="left",
    )

    ax.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.3)
    ax.annotate(
        "No-bailout signal\n(Apr 1843)", xy=(SIGNAL, ax.get_ylim()[1]), xytext=(6, -6),
        textcoords="offset points", color=SIGNAL_COLOR, fontsize=9, fontweight="bold", va="top", ha="left",
    )

    ax.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=11)
    ax.set_ylabel("Yield (%)", color=PRIMARY_TEXT, fontsize=11)
    ax.set_title(
        "City vs. State Yields, 1835-1845 -- Philadelphia (city) vs. Pennsylvania (state)",
        color=PRIMARY_TEXT, fontsize=13, fontweight="bold", loc="left",
    )

    method_note = (
        "Yield = current yield (coupon/price x 100) for both series, for direct comparability with PA's own "
        "active-default-override window (Aug 1842-Feb 1845), which already uses current yield for nearly all of "
        "PA's post-signal usable data. Philadelphia (C-1100, \"Philadelphia 5s, r. 1846\") never approaches its own "
        "maturity in this window and shows no price pattern resembling default -- no override applied. Philadelphia "
        "has a genuine 343-day data gap (Feb 1843-Feb 1844, dotted segment) spanning almost the entire immediate "
        "post-signal period -- the city's reaction to the Apr 1843 signal itself cannot be directly observed, only "
        "its level by Feb 1844 onward. Pennsylvania vs. Ohio/Alabama/Indiana/NY comparisons are in the separate "
        "three-tier chart set; this chart is Philadelphia vs. Pennsylvania ONLY -- Cincinnati, Pittsburgh, and "
        "NYC/Brooklyn were not included in this pass (see PROJECT_CONTEXT.md)."
    )
    wrapped_lines = []
    for paragraph in method_note.split("\n"):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=155) or [""])
    wrapped = "\n".join(wrapped_lines)
    fig.text(0.01, 0.01, wrapped, color=SECONDARY_TEXT, fontsize=8, ha="left", va="bottom")
    bottom_margin = 0.02 + 0.018 * len(wrapped_lines)
    fig.tight_layout(rect=(0, bottom_margin, 1, 1))

    out_path = OUTPUT_DIR / "chart_city_vs_state.png"
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print(f"saved -> {out_path}")


def main() -> None:
    city_price = load_city_price_series()
    pa_state = pd.read_csv(OUTPUT_DIR / "primary_yields.csv", parse_dates=["date"])
    pa_state = pa_state[
        (pa_state.state == "Pennsylvania")
        & (pa_state.series_label == "primary")
        & ~pa_state.excluded_past_maturity
        & ~pa_state.excluded_near_maturity
    ]

    comparison = build_comparison_frame(city_price, pa_state)
    out_path = OUTPUT_DIR / "city_vs_state_yields.csv"
    comparison.to_csv(out_path, index=False)
    print(f"saved -> {out_path} ({len(comparison)} rows)")
    print()

    pa_yield_by_date = load_state_yield_series()
    print_spread_summary(city_price, pa_yield_by_date)
    print()

    build_chart(comparison)


if __name__ == "__main__":
    main()
