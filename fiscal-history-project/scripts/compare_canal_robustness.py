"""Canal/revenue-pledged bond robustness comparison -- the secondary series
flagged since the Seniority Check in PROJECT_CONTEXT.md but never built as
a standalone, reproducible script until now.

Scope and the Ohio drop
------------------------
Per PROJECT_CONTEXT.md's Seniority Check decision: the PRIMARY comparison
(scripts/calculate_yields.py, NOT touched by this script) uses only
general-obligation bonds. This script builds the SECONDARY/robustness
comparison of the canal/revenue-pledged bonds that were displaced from the
primary set: New York Canal (S-1750/S-1820/S-1950) and Indiana's 1847
Butler Bill canal tranches (S-0480/S-0490/S-0500/S-0506).

Ohio's only canal bond, S-2190 ("Ohio Canal 5s"), is DROPPED from this
comparison entirely, per the trade-density investigation already recorded
in PROJECT_CONTEXT.md ("2026-07-28: Trade-Density / Bank-Held Bonds
Investigation"): S-2190 has exactly 2 price observations, both from 1825
-- two decades before this project's 1837-1853 study window, and before
any of the relevant state banking law even existed. There is no data to
plot for the 1840s-50s regardless of the bank-held question. This was
flagged there as "pending sign-off"; the task that produced this script
treated it as approved, so Ohio is simply absent from the canal/robustness
set below rather than represented by two pre-panic data points -- this
shrinks the state-level canal comparison from a notional 3 states to 2
(New York, Indiana), consistent with that prior finding.

S-0470 ("Indiana Canal") is also excluded from the yield calculation
(though its raw trade-density is reported below for completeness): its
codebook interest-rate field is blank, so no coupon is available and no
yield -- current or YTM -- can be computed for it at all. This is a data
limitation, not a judgment call.

Yield methodology (mirrors calculate_yields.py's own rules exactly, not a
new convention)
------------------------------------------------------------------------
- New York canal bonds (S-1750/S-1820/S-1950): all have real maturity
  years in the codebook (1850/1860/1861) and New York never defaulted
  (DEFAULT_PERIODS has no New York entry, matching calculate_yields.py),
  so YTM applies with the same near/past-maturity truncation flags used
  everywhere else in this project (12-month near-maturity window,
  past-maturity dates excluded).
- Indiana canal tranches (S-0480/S-0490/S-0500/S-0506): no maturity year
  in the codebook (same situation as Indiana's primary GO codes,
  S-0510/S-0540) -- always current yield, never YTM, no truncation flags
  apply. The `active_default_override` column is still populated for
  these rows based on whether the observation date falls inside Indiana's
  DEFAULT_PERIODS window (Jan 1 1841, ongoing) -- exactly like
  calculate_yields.py's build_bond_frame does for its own NO_MATURITY_
  STATES branch: the flag records whether the row was *inside* the
  default period, even where it doesn't change which formula is used
  (there's no YTM to override in the first place for these codes).
  **Honest wrinkle, not swept under the rug:** because Indiana's default
  period has no documented end date within this project's window, EVERY
  observation of these four tranches (all dated 1850-1853, since they
  only start trading after the 1847 Butler Bill restructuring) falls
  inside `active_default_override=True` under this project's existing
  convention -- even though the whole point of the restructuring was to
  put the *preferred* tranche back on a paying basis. This is a known
  limitation of applying the established Indiana default-period rule
  mechanically here, not a new problem this script introduces -- flagged
  for the record rather than hand-tuning an exception.

Indiana preferred-vs-deferred tranche test
--------------------------------------------
Groups: "preferred" = S-0490 (Preferred 5s) + S-0500 (Special Preferred
5s); "deferred" = S-0480 (Deferred 5s) + S-0506 (Special Deferred 5s).
These four tranches only begin trading in 1850 (three years after the
1847 restructuring) and run through 1853 -- entirely AFTER this project's
panic-window and policy-window cutoffs, so this tranche test cannot speak
to the Feb/Apr 1843 signal at all. It tests something else: did the
market price the *seniority* difference the restructuring created,
independent of timing relative to the no-bailout signal.

Outputs
-------
- output/canal_robustness_yields.csv
- output/chart_canal_robustness.png
"""

import textwrap
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
CODEBOOK_PATH = RAW_DIR / "Securities Index.xls"
NY_PRICES = OUTPUT_DIR / "new_york_state_debt_prices.csv"

FACE_VALUE = 100.0
NEAR_MATURITY_YEARS = 1.0
SIGNAL = pd.Timestamp("1843-04-01")
PRE_SIGNAL_CUTOFF = pd.Timestamp("1843-02-11")

# Indiana's documented default period (see calculate_yields.py / PROJECT_CONTEXT.md) --
# reused as-is, not re-derived.
INDIANA_DEFAULT_START = pd.Timestamp("1841-01-01")

NY_CANAL_SPECS = [
    {"code": "S-1750", "name": "New York Canal 5s, 1850", "coupon": 5.0, "maturity": 1850},
    {"code": "S-1820", "name": "New York Canal 5s, 1860", "coupon": 5.0, "maturity": 1860},
    {"code": "S-1950", "name": "New York Canal 6s, 1861", "coupon": 6.0, "maturity": 1861},
]

INDIANA_CANAL_SPECS = [
    {"code": "S-0480", "name": "Indiana Canal Deferred 5s", "coupon": 5.0, "tranche": "deferred"},
    {"code": "S-0490", "name": "Indiana Canal Preferred 5s", "coupon": 5.0, "tranche": "preferred"},
    {"code": "S-0500", "name": "Indiana Canal Special Preferred 5s", "coupon": 5.0, "tranche": "preferred"},
    {"code": "S-0506", "name": "Indiana Canal Special Deferred 5s", "coupon": 5.0, "tranche": "deferred"},
]

DROPPED = {
    "S-2190": "Ohio Canal 5s -- 2 total observations, both from 1825; unusable for the 1840s-50s "
              "study window (see PROJECT_CONTEXT.md trade-density investigation). Dropped entirely.",
    "S-0470": "Indiana Canal -- no coupon/interest-rate value in the codebook; yield cannot be "
              "computed by either method. Excluded from the yield comparison (trade-density noted "
              "below for completeness only).",
}

# S-1750 has a genuine 1,666-day gap (already documented in PROJECT_CONTEXT.md's trade-density
# pass) between its last pre-gap observation and its next one -- connecting these directly with a
# straight line would visually imply a smooth ~4.5-year climb from ~5% to ~12% that never happened.
# Rendered as a dotted, unfilled segment in the chart, same convention as compare_city_vs_state.py's
# treatment of C-1100's 343-day gap. Not a "real" data point pair to connect.
S1750_GAP_START = pd.Timestamp("1843-08-05")
S1750_GAP_END = pd.Timestamp("1848-02-26")

# S-1820 has one isolated price of 160.00 on 1848-10-14, sandwiched between prices of 96-99.5 on
# either side (verified directly against the raw New-York.xls source: row 3256, "NY State Debt"
# sheet -- this is a genuine value in the source file, not a parsing bug introduced here). Almost
# certainly a transcription error in the original digitized price list, not a real quote -- a state
# canal bond trading 60%+ above par with no economic event to explain it, surrounded by normal
# prices a week before and two weeks after. Left in canal_robustness_yields.csv as-is (the raw
# source value, not altered), but excluded from the chart line below to avoid rendering the
# resulting nonsensical -0.27% YTM as if it were a real data point. Flagged here rather than
# silently dropped from the CSV.
S1820_ANOMALY_DATE = pd.Timestamp("1848-10-14")

SURFACE = "#fcfcfb"
PRIMARY_TEXT = "#0b0b0b"
SECONDARY_TEXT = "#52514e"
MUTED_TEXT = "#898781"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
SIGNAL_COLOR = "#e34948"
NY_COLOR = "#2a78d6"
PREFERRED_COLOR = "#1f9e6d"
DEFERRED_COLOR = "#c9542c"


def load_codebook() -> dict:
    wb = xlrd.open_workbook(CODEBOOK_PATH)
    sh = wb.sheet_by_name("final")
    out = {}
    for r in range(1, sh.nrows):
        code, name, _type, interest, maturity = sh.row_values(r)
        out[code] = (name, interest, maturity)
    return out


def compute_ytm(price: pd.Series, coupon: float, n_years: pd.Series) -> pd.Series:
    return (coupon + (FACE_VALUE - price) / n_years) / ((FACE_VALUE + price) / 2) * 100


def build_ny_canal_frame(ny_df: pd.DataFrame) -> pd.DataFrame:
    frames = []
    for spec in NY_CANAL_SPECS:
        price = ny_df[f"NY State Debt::{spec['code']}"].dropna().sort_index()
        coupon = spec["coupon"]
        maturity_date = pd.Timestamp(f"{spec['maturity']}-01-01")
        n_years = (maturity_date - price.index).days / 365.25
        excluded_past = n_years <= 0
        excluded_near = (n_years > 0) & (n_years <= NEAR_MATURITY_YEARS)

        ytm = compute_ytm(price, coupon, n_years)
        yield_value = ytm.where(~excluded_past, other=pd.NA)
        current_yield = coupon / price * 100

        frames.append(pd.DataFrame({
            "date": price.index,
            "state": "New York",
            "code": spec["code"],
            "name": spec["name"],
            "tranche": "n/a",
            "price": price.values,
            "coupon": coupon,
            "yield_measure_used": "ytm",
            "yield": yield_value.values,
            "current_yield": current_yield.values,
            "series_label": "canal_robustness",
            "excluded_near_maturity": pd.Series(excluded_near).values,
            "excluded_past_maturity": pd.Series(excluded_past).values,
            "active_default_override": False,  # New York never defaulted
        }))
    return pd.concat(frames, ignore_index=True)


def build_indiana_canal_frame(ny_df: pd.DataFrame) -> pd.DataFrame:
    frames = []
    for spec in INDIANA_CANAL_SPECS:
        price = ny_df[f"Other State Debt::{spec['code']}"].dropna().sort_index()
        coupon = spec["coupon"]
        current_yield = coupon / price * 100
        default_override = price.index >= INDIANA_DEFAULT_START

        frames.append(pd.DataFrame({
            "date": price.index,
            "state": "Indiana",
            "code": spec["code"],
            "name": spec["name"],
            "tranche": spec["tranche"],
            "price": price.values,
            "coupon": coupon,
            "yield_measure_used": "current_yield",
            "yield": current_yield.values,
            "current_yield": current_yield.values,
            "series_label": "canal_robustness",
            "excluded_near_maturity": False,
            "excluded_past_maturity": False,
            "active_default_override": default_override,
        }))
    return pd.concat(frames, ignore_index=True)


def trade_density_report(ny_df: pd.DataFrame) -> None:
    print("=== Trade density, canal/robustness codes (including dropped/excluded) ===")
    all_codes = [s["code"] for s in NY_CANAL_SPECS] + [s["code"] for s in INDIANA_CANAL_SPECS] + list(DROPPED)
    sheets = {**{s["code"]: "NY State Debt" for s in NY_CANAL_SPECS},
              **{s["code"]: "Other State Debt" for s in INDIANA_CANAL_SPECS},
              "S-2190": "Other State Debt", "S-0470": "Other State Debt"}
    for code in all_codes:
        col = f"{sheets[code]}::{code}"
        s = ny_df[col].dropna().sort_index()
        status = f" -- {DROPPED[code]}" if code in DROPPED else ""
        if len(s) == 0:
            print(f"{code:8} n=0{status}")
            continue
        print(f"{code:8} n={len(s):4} range={s.index.min().date()} to {s.index.max().date()}{status}")
    print()


def print_tranche_summary(indiana: pd.DataFrame) -> None:
    pref = indiana[indiana.tranche == "preferred"]
    defr = indiana[indiana.tranche == "deferred"]
    ov_start = max(pref.date.min(), defr.date.min())
    ov_end = min(pref.date.max(), defr.date.max())
    pref_ov = pref[(pref.date >= ov_start) & (pref.date <= ov_end)]
    defr_ov = defr[(defr.date >= ov_start) & (defr.date <= ov_end)]

    print("=== Indiana preferred vs. deferred tranche test ===")
    print(f"Preferred (S-0490 + S-0500): full-window mean {pref['yield'].mean():.2f}%  n={len(pref)}, "
          f"{pref.date.min().date()} to {pref.date.max().date()}")
    print(f"Deferred  (S-0480 + S-0506): full-window mean {defr['yield'].mean():.2f}%  n={len(defr)}, "
          f"{defr.date.min().date()} to {defr.date.max().date()}")
    print(f"Overlap window ({ov_start.date()} to {ov_end.date()}), apples-to-apples:")
    print(f"  Preferred: mean {pref_ov['yield'].mean():.2f}%  n={len(pref_ov)}")
    print(f"  Deferred:  mean {defr_ov['yield'].mean():.2f}%  n={len(defr_ov)}")
    print(f"  Gap (deferred - preferred): {defr_ov['yield'].mean() - pref_ov['yield'].mean():.2f}pp")
    print()
    print("Raw price levels (not just yield) for a sanity check against a current-yield artifact:")
    for spec in INDIANA_CANAL_SPECS:
        s = indiana[indiana.code == spec["code"]]["price"]
        print(f"  {spec['code']} ({spec['tranche']:>9}, {spec['name']}): "
              f"median price {s.median():.2f}, range {s.min():.1f}-{s.max():.1f}")
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
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    return fig, ax


def build_chart(ny_canal: pd.DataFrame, indiana: pd.DataFrame) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=150)
    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        ax.grid(True, color=GRID_COLOR, linewidth=0.8)
        ax.set_axisbelow(True)
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_color(AXIS_COLOR)
        ax.tick_params(colors=MUTED_TEXT, labelsize=9)
        ax.xaxis.set_major_locator(mdates.YearLocator(2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.patch.set_facecolor(SURFACE)

    # Left panel: NY canal bonds, usable (non-excluded) rows
    for i, spec in enumerate(NY_CANAL_SPECS):
        s = ny_canal[(ny_canal.code == spec["code"]) & ~ny_canal.excluded_past_maturity & ~ny_canal.excluded_near_maturity]
        s = s[~((s.code == "S-1820") & (s.date == S1820_ANOMALY_DATE))]  # drop the 160.00 anomaly from the line only
        s = s.sort_values("date")
        color_alpha = 0.55 + 0.22 * i
        if spec["code"] == "S-1750":
            # Break the line across the known 1,666-day gap instead of connecting it directly.
            seg1 = s[s.date <= S1750_GAP_START]
            seg2 = s[s.date >= S1750_GAP_END]
            ax1.plot(seg1.date, seg1["yield"], linewidth=1.6, color=NY_COLOR, alpha=color_alpha,
                      label=f"{spec['code']} ({spec['name']})")
            ax1.plot(seg2.date, seg2["yield"], linewidth=1.6, color=NY_COLOR, alpha=color_alpha)
            if len(seg1) and len(seg2):
                ax1.plot([seg1.date.iloc[-1], seg2.date.iloc[0]], [seg1["yield"].iloc[-1], seg2["yield"].iloc[0]],
                          linewidth=1, linestyle=":", color=NY_COLOR, alpha=0.5)
                ax1.annotate("no data\n(1,666-day gap)", xy=(S1750_GAP_START, seg1["yield"].iloc[-1]),
                              xytext=(4, 10), textcoords="offset points", color=NY_COLOR, fontsize=6.5,
                              style="italic", ha="left")
        else:
            ax1.plot(s.date, s["yield"], linewidth=1.6, label=f"{spec['code']} ({spec['name']})", color=NY_COLOR,
                      alpha=color_alpha)
    ax1.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.2)
    ax1.set_title("New York Canal Bonds (secondary/robustness)", color=PRIMARY_TEXT, fontsize=11, fontweight="bold", loc="left")
    ax1.set_ylabel("Yield (%)", color=PRIMARY_TEXT)
    ax1.legend(fontsize=7, loc="upper right", frameon=False)

    # Right panel: Indiana preferred vs. deferred. One deferred observation (S-0506, 1851-10-08,
    # price $1.00) yields 500% current yield -- real per the formula, but plotting it directly would
    # crush the rest of the series to a flat line near zero. Capped off-chart with an annotation
    # instead of silently excluding or rescaling the whole axis around a single point.
    pref = indiana[indiana.tranche == "preferred"].groupby("date")["yield"].mean().sort_index()
    defr_raw = indiana[indiana.tranche == "deferred"].groupby("date")["yield"].mean().sort_index()
    Y_CAP = 100.0
    n_capped = int((defr_raw > Y_CAP).sum())
    defr = defr_raw.clip(upper=Y_CAP)
    ax2.plot(pref.index, pref.values, color=PREFERRED_COLOR, linewidth=2, label="Preferred (S-0490 + S-0500)")
    ax2.plot(defr.index, defr.values, color=DEFERRED_COLOR, linewidth=2, label="Deferred (S-0480 + S-0506)")
    if n_capped:
        capped_dates = defr_raw[defr_raw > Y_CAP]
        for dt, val in capped_dates.items():
            ax2.annotate(f"{val:.0f}%\n(off-chart)", xy=(dt, Y_CAP), xytext=(0, 6), textcoords="offset points",
                          color=DEFERRED_COLOR, fontsize=7, ha="center", fontweight="bold")
    ax2.set_ylim(0, Y_CAP * 1.08)
    ax2.set_title("Indiana Butler Bill Tranches: Preferred vs. Deferred", color=PRIMARY_TEXT, fontsize=11, fontweight="bold", loc="left")
    ax2.set_ylabel("Current yield (%), capped at 100% -- see note", color=PRIMARY_TEXT, fontsize=9)
    ax2.legend(fontsize=8, loc="upper right", frameon=False)

    fig.suptitle(
        "Canal / Revenue-Pledged Bond Robustness Comparison (secondary series)",
        color=PRIMARY_TEXT, fontsize=14, fontweight="bold", x=0.01, ha="left",
    )

    method_note = (
        "LEFT: New York canal bonds (S-1750/S-1820/S-1950), YTM with the same near/past-maturity truncation "
        "rules used throughout this project; New York never defaulted, so no active-default override applies. "
        "Ohio's only canal bond (S-2190) is dropped -- 2 observations, both from 1825, no data in the study "
        "window. RIGHT: Indiana's 1847 Butler Bill canal tranches, current yield (no maturity date in the "
        "codebook, same convention as Indiana's primary GO bonds). These only begin trading in 1850, three "
        "years after the restructuring and entirely after the panic/policy windows -- this side of the chart "
        "tests whether the market priced the preferred-vs-deferred seniority split, not the Feb/Apr 1843 signal. "
        "All Indiana canal-tranche rows fall inside Indiana's documented (open-ended) default period under this "
        "project's existing convention -- flagged, not hidden. S-1750's dotted segment marks a genuine 1,666-day "
        "gap in the source data, not interpolation. One S-1820 price (160.00, Oct 1848, likely a source "
        "transcription error -- verified against the raw file) is excluded from this chart's line only, kept "
        "as-is in the CSV. One deferred-tranche point (S-0506, Oct 1851, price $1.00, 500% current yield) is "
        "capped off-chart and labeled rather than rescaling the whole axis around it. See PROJECT_CONTEXT.md."
    )
    wrapped_lines = []
    for paragraph in method_note.split("\n"):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=200) or [""])
    wrapped = "\n".join(wrapped_lines)
    fig.text(0.01, 0.01, wrapped, color=SECONDARY_TEXT, fontsize=7.5, ha="left", va="bottom")
    bottom_margin = 0.02 + 0.02 * len(wrapped_lines)
    fig.tight_layout(rect=(0, bottom_margin, 1, 0.94))

    out_path = OUTPUT_DIR / "chart_canal_robustness.png"
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print(f"saved -> {out_path}")


def main() -> None:
    ny_df = pd.read_csv(NY_PRICES, index_col=0, parse_dates=True)

    trade_density_report(ny_df)

    ny_canal = build_ny_canal_frame(ny_df)
    indiana = build_indiana_canal_frame(ny_df)

    cols = [
        "date", "state", "code", "name", "tranche", "price", "coupon",
        "yield_measure_used", "yield", "current_yield", "series_label",
        "excluded_near_maturity", "excluded_past_maturity", "active_default_override",
    ]
    out = pd.concat([ny_canal[cols], indiana[cols]], ignore_index=True).sort_values(["state", "code", "date"])
    out_path = OUTPUT_DIR / "canal_robustness_yields.csv"
    out.to_csv(out_path, index=False)
    print(f"saved -> {out_path} ({len(out)} rows)")
    print()

    print_tranche_summary(indiana)

    build_chart(ny_canal, indiana)


if __name__ == "__main__":
    main()
