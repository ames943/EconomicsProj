"""Build presentation_charts/ -- four standalone, screen-readable charts.

Regenerated from the same underlying data and plotting logic as the
protected comparison scripts (compare_city_vs_state.py,
compare_city_vs_state_cincinnati_pittsburgh.py,
compare_canal_robustness.py), NOT just cropped from their output PNGs, and
those scripts are not modified or touched by this one. What changed here is
purely readability for a chart shown alone on a screen with no surrounding
text:

- The dense technical methodology footnote (fig.text at the bottom of each
  original chart) is dropped entirely -- it belongs in PROJECT_CONTEXT.md,
  not on a slide.
- Every title is a plain-language question instead of a terse data label.
- All font sizes (titles, axis labels, tick labels, legends, annotations)
  are roughly 1.4-1.6x the originals, sized for a shared screen rather than
  a printed page.
- Nothing about what any chart actually shows has changed: same series,
  same colors per entity, same gap-handling (S-1750's 1,666-day gap and
  C-1100's 343-day gap still render as broken/dotted segments, not smoothed
  lines), same S-1820 transcription-error exclusion, same 500%-clip
  annotation for Indiana's S-0506 outlier. This is a readability pass, not
  a re-analysis.

Inputs (unchanged, read-only): output/city_vs_state_yields.csv,
output/city_vs_state_pittsburgh.csv, output/city_vs_state_cincinnati.csv,
output/canal_robustness_yields.csv.

Outputs: presentation_charts/1_philadelphia_vs_pennsylvania.png,
2_pittsburgh_vs_pennsylvania.png, 3_cincinnati_vs_ohio.png,
4_canal_and_indiana_tranches.png -- and nothing else in that folder.
"""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
PRESENTATION_DIR = PROJECT_ROOT / "presentation_charts"
PRESENTATION_DIR.mkdir(exist_ok=True)

SIGNAL = pd.Timestamp("1843-04-01")
PA_DEFAULT = pd.Timestamp("1842-08-01")
PA_COVERAGE_CEILING = pd.Timestamp("1845-01-25")

SURFACE = "#fcfcfb"
PRIMARY_TEXT = "#0b0b0b"
MUTED_TEXT = "#898781"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
SIGNAL_COLOR = "#e34948"
DEFAULT_COLOR = "#9a6b00"
STATE_COLOR = "#2a78d6"
PHILA_COLOR = "#7a3fc9"
CITY3_COLOR = "#1f9e6d"  # Pittsburgh / Cincinnati

NY_COLOR = "#2a78d6"
PREFERRED_COLOR = "#1f9e6d"
DEFERRED_COLOR = "#c9542c"

# --- Data-quality markers, reused as-is from the protected scripts ---
GAP_START = pd.Timestamp("1843-02-25")   # C-1100's last obs before its gap
GAP_END = pd.Timestamp("1844-02-03")     # C-1100's first obs after its gap
S1750_GAP_START = pd.Timestamp("1843-08-05")
S1750_GAP_END = pd.Timestamp("1848-02-26")
S1820_ANOMALY_DATE = pd.Timestamp("1848-10-14")

NY_CANAL_SPECS = [
    {"code": "S-1750", "name": "5s, 1850"},
    {"code": "S-1820", "name": "5s, 1860"},
    {"code": "S-1950", "name": "6s, 1861"},
]


def new_fig(figsize=(13, 7.5), year_step=1):
    fig, ax = plt.subplots(figsize=figsize, dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.grid(True, color=GRID_COLOR, linewidth=0.9)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(AXIS_COLOR)
    ax.tick_params(colors=MUTED_TEXT, labelsize=13)
    ax.xaxis.set_major_locator(mdates.YearLocator(year_step))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    return fig, ax


def finish(fig, ax, title, out_name):
    ax.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=15)
    ax.set_ylabel("Interest Rate (Yield, %)", color=PRIMARY_TEXT, fontsize=15)
    ax.set_title(title, color=PRIMARY_TEXT, fontsize=19, fontweight="bold", loc="left", pad=14)
    fig.tight_layout()
    out_path = PRESENTATION_DIR / out_name
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print(f"saved -> {out_path}  ({fig.get_size_inches()[0]*150:.0f}px wide)")


# ---------------------------------------------------------------------------
# 1. Philadelphia vs. Pennsylvania
# ---------------------------------------------------------------------------

def build_philadelphia():
    df = pd.read_csv(OUTPUT_DIR / "city_vs_state_yields.csv", parse_dates=["date"])
    pa = df[df.level == "state"].groupby("date")["yield"].mean().sort_index()
    city = df[df.level == "city"].set_index("date")["yield"].sort_index()

    fig, ax = new_fig()

    ax.plot(pa.index, pa.values, color=STATE_COLOR, linewidth=2.5, solid_capstyle="round")
    ax.annotate(
        "Pennsylvania (state, defaulted)", xy=(pa.index[-1], pa.values[-1]), xytext=(8, 0),
        textcoords="offset points", color=STATE_COLOR, fontsize=13, fontweight="bold",
        va="center", ha="left",
    )

    seg1 = city[city.index <= GAP_START]
    seg2 = city[city.index >= GAP_END]
    ax.plot(seg1.index, seg1.values, color=PHILA_COLOR, linewidth=2.5, solid_capstyle="round")
    ax.plot(seg2.index, seg2.values, color=PHILA_COLOR, linewidth=2.5, solid_capstyle="round")
    ax.plot([GAP_START, GAP_END], [seg1.values[-1], seg2.values[0]],
            color=PHILA_COLOR, linewidth=1.3, linestyle=":", alpha=0.6)
    ax.annotate(
        "Philadelphia (city, no default)", xy=(seg2.index[-1], seg2.values[-1]), xytext=(8, -12),
        textcoords="offset points", color=PHILA_COLOR, fontsize=13, fontweight="bold",
        va="center", ha="left",
    )
    ax.annotate(
        "no data here\n(gap in records)", xy=(GAP_START, seg1.values[-1]), xytext=(0, 22),
        textcoords="offset points", color=PHILA_COLOR, fontsize=10.5, ha="left", va="bottom",
        style="italic",
    )

    ax.axvline(PA_DEFAULT, color=DEFAULT_COLOR, linestyle="--", linewidth=1.6)
    ax.annotate(
        "PA Default\n(Aug 1842)", xy=(PA_DEFAULT, 0), xytext=(8, 8),
        textcoords="offset points", color=DEFAULT_COLOR, fontsize=13, fontweight="bold",
        va="bottom", ha="left",
    )

    ax.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.6)
    ax.annotate(
        "Federal \"no bailout\" announcement\n(Apr 1843)", xy=(SIGNAL, ax.get_ylim()[1]),
        xytext=(8, -8), textcoords="offset points", color=SIGNAL_COLOR, fontsize=13,
        fontweight="bold", va="top", ha="left",
    )

    finish(
        fig, ax,
        "Philadelphia (City) vs. Pennsylvania (State) — Does Default Spread to the City?",
        "1_philadelphia_vs_pennsylvania.png",
    )


# ---------------------------------------------------------------------------
# 2 & 3. Pittsburgh vs. Pennsylvania / Cincinnati vs. Ohio
# ---------------------------------------------------------------------------

def build_second_city(csv_name, city_name, state_name, out_name, title, is_pa):
    df = pd.read_csv(OUTPUT_DIR / csv_name, parse_dates=["date"])
    state_series = df[df.level == "state"].groupby("date")["yield"].mean().sort_index()
    city_series = df[df.level == "city"].set_index("date")["yield"].sort_index()

    span_years = (df["date"].max() - df["date"].min()).days / 365
    fig, ax = new_fig(year_step=2 if span_years > 22 else 1)

    ax.plot(state_series.index, state_series.values, color=STATE_COLOR, linewidth=2.5,
            solid_capstyle="round")
    ax.annotate(
        f"{state_name} (state)", xy=(state_series.index[-1], state_series.values[-1]),
        xytext=(8, 0), textcoords="offset points", color=STATE_COLOR, fontsize=13,
        fontweight="bold", va="center", ha="left",
    )

    ax.plot(city_series.index, city_series.values, color=CITY3_COLOR, linewidth=2.5,
            solid_capstyle="round")
    ax.annotate(
        f"{city_name} (city, no default)", xy=(city_series.index[-1], city_series.values[-1]),
        xytext=(8, -12), textcoords="offset points", color=CITY3_COLOR, fontsize=13,
        fontweight="bold", va="center", ha="left",
    )

    if is_pa:
        ax.axvline(PA_DEFAULT, color=DEFAULT_COLOR, linestyle="--", linewidth=1.6)
        ax.annotate(
            "PA Default\n(Aug 1842)", xy=(PA_DEFAULT, 0), xytext=(8, 8),
            textcoords="offset points", color=DEFAULT_COLOR, fontsize=13, fontweight="bold",
            va="bottom", ha="left",
        )
        ax.axvline(PA_COVERAGE_CEILING, color=MUTED_TEXT, linestyle=":", linewidth=1.3)
        y_mid = ax.get_ylim()[0] + 0.5 * (ax.get_ylim()[1] - ax.get_ylim()[0])
        ax.annotate(
            "PA state records\nend here", xy=(PA_COVERAGE_CEILING, y_mid), xytext=(8, 0),
            textcoords="offset points", color=MUTED_TEXT, fontsize=10.5, va="center", ha="left",
            style="italic",
        )

    ax.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.6)
    ax.annotate(
        "Federal \"no bailout\" announcement\n(Apr 1843)", xy=(SIGNAL, ax.get_ylim()[1]),
        xytext=(8, -8), textcoords="offset points", color=SIGNAL_COLOR, fontsize=13,
        fontweight="bold", va="top", ha="left",
    )

    finish(fig, ax, title, out_name)


# ---------------------------------------------------------------------------
# 4. Canal bonds + Indiana preferred vs. deferred
# ---------------------------------------------------------------------------

def build_canal():
    df = pd.read_csv(OUTPUT_DIR / "canal_robustness_yields.csv", parse_dates=["date"])
    ny_canal = df[df.state == "New York"]
    indiana = df[df.state == "Indiana"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19, 8.5), dpi=150)
    for ax in (ax1, ax2):
        ax.set_facecolor(SURFACE)
        ax.grid(True, color=GRID_COLOR, linewidth=0.9)
        ax.set_axisbelow(True)
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_color(AXIS_COLOR)
        ax.tick_params(colors=MUTED_TEXT, labelsize=13)
        ax.xaxis.set_major_locator(mdates.YearLocator(2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.patch.set_facecolor(SURFACE)

    # Left: NY canal bonds
    for i, spec in enumerate(NY_CANAL_SPECS):
        s = ny_canal[(ny_canal.code == spec["code"])
                     & ~ny_canal.excluded_past_maturity & ~ny_canal.excluded_near_maturity]
        s = s[~((s.code == "S-1820") & (s.date == S1820_ANOMALY_DATE))]
        s = s.sort_values("date")
        color_alpha = 0.55 + 0.22 * i
        if spec["code"] == "S-1750":
            seg1 = s[s.date <= S1750_GAP_START]
            seg2 = s[s.date >= S1750_GAP_END]
            ax1.plot(seg1.date, seg1["yield"], linewidth=2, color=NY_COLOR, alpha=color_alpha,
                      label=f"NY Canal {spec['name']}")
            ax1.plot(seg2.date, seg2["yield"], linewidth=2, color=NY_COLOR, alpha=color_alpha)
            if len(seg1) and len(seg2):
                ax1.plot([seg1.date.iloc[-1], seg2.date.iloc[0]],
                          [seg1["yield"].iloc[-1], seg2["yield"].iloc[0]],
                          linewidth=1.3, linestyle=":", color=NY_COLOR, alpha=0.5)
                ax1.annotate("no data here\n(long gap in records)",
                              xy=(S1750_GAP_START, seg1["yield"].iloc[-1]),
                              xytext=(5, 12), textcoords="offset points", color=NY_COLOR,
                              fontsize=10, style="italic", ha="left")
        else:
            ax1.plot(s.date, s["yield"], linewidth=2, label=f"NY Canal {spec['name']}",
                      color=NY_COLOR, alpha=color_alpha)
    ax1.axvline(SIGNAL, color=SIGNAL_COLOR, linestyle="--", linewidth=1.6)
    ax1.set_title("New York's Canal Bonds", color=PRIMARY_TEXT, fontsize=17, fontweight="bold",
                   loc="left", pad=12)
    ax1.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=14)
    ax1.set_ylabel("Interest Rate (Yield, %)", color=PRIMARY_TEXT, fontsize=14)
    ax1.legend(fontsize=11, loc="upper right", frameon=False)

    # Right: Indiana preferred vs. deferred
    pref = indiana[indiana.tranche == "preferred"].groupby("date")["yield"].mean().sort_index()
    defr_raw = indiana[indiana.tranche == "deferred"].groupby("date")["yield"].mean().sort_index()
    Y_CAP = 100.0
    n_capped = int((defr_raw > Y_CAP).sum())
    defr = defr_raw.clip(upper=Y_CAP)
    ax2.plot(pref.index, pref.values, color=PREFERRED_COLOR, linewidth=2.8,
              label="Paid first (\"preferred\")")
    ax2.plot(defr.index, defr.values, color=DEFERRED_COLOR, linewidth=2.8,
              label="Paid second (\"deferred\")")
    if n_capped:
        capped_dates = defr_raw[defr_raw > Y_CAP]
        for dt, val in capped_dates.items():
            ax2.annotate(f"{val:.0f}%\n(off-chart)", xy=(dt, Y_CAP), xytext=(0, 8),
                          textcoords="offset points", color=DEFERRED_COLOR, fontsize=11,
                          ha="center", fontweight="bold")
    ax2.set_ylim(0, Y_CAP * 1.1)
    ax2.set_title("Indiana: Which Slice of Debt Got Paid First?", color=PRIMARY_TEXT,
                   fontsize=17, fontweight="bold", loc="left", pad=12)
    ax2.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=14)
    ax2.set_ylabel("Interest Rate (Yield, %, capped at 100)", color=PRIMARY_TEXT, fontsize=13)
    ax2.legend(fontsize=12, loc="upper right", frameon=False)

    fig.suptitle(
        "Canal Bonds & Indiana's Preferred vs. Deferred Debt — A Second, Independent Check",
        color=PRIMARY_TEXT, fontsize=20, fontweight="bold", x=0.01, ha="left", y=0.995,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.93))

    out_path = PRESENTATION_DIR / "4_canal_and_indiana_tranches.png"
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print(f"saved -> {out_path}  ({fig.get_size_inches()[0]*150:.0f}px wide)")


def main():
    # Wipe the folder first so it only ever contains exactly these four files.
    for f in PRESENTATION_DIR.glob("*"):
        f.unlink()

    build_philadelphia()
    build_second_city(
        "city_vs_state_pittsburgh.csv", "Pittsburgh", "Pennsylvania",
        "2_pittsburgh_vs_pennsylvania.png",
        "Pittsburgh (City) vs. Pennsylvania (State) — Does Default Spread to the City?",
        is_pa=True,
    )
    build_second_city(
        "city_vs_state_cincinnati.csv", "Cincinnati", "Ohio",
        "3_cincinnati_vs_ohio.png",
        "Cincinnati (City) vs. Ohio (State) — A Control Case, Ohio Never Defaulted",
        is_pa=False,
    )
    build_canal()

    print("\npresentation_charts/ contents:")
    for f in sorted(PRESENTATION_DIR.glob("*")):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
