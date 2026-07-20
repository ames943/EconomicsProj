"""Plot the 8 "recovered quickly" candidate bonds found in New-York.xls's
"Other State Debt" sheet (1835-1845), with Pennsylvania's August 1842
default date marked for reference.

IMPORTANT: cross-referencing against Securities Index.xls confirmed these
are NOT New York bonds -- they live in the "Other State Debt" sheet of
New-York.xls (bonds of other states quoted on the NY market), not the
"NY State Debt" sheet. They are Ohio (never defaulted, a "safe" candidate),
Alabama, and Indiana (both likely "defaulted" candidates -- Indiana via the
1846 Butler Bill partial restructuring), not NY's "risky but survived" case.
See scripts/identify_candidates.py for genuine NY State Debt sheet
candidates instead.
"""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
CSV_PATH = OUTPUT_DIR / "new_york_state_debt_prices.csv"
DEFAULT_DATE = pd.Timestamp("1842-08-01")

# code -> (display name, state, state color slot)
# colors: dataviz skill categorical theme, fixed order (light mode)
BOND_INFO = {
    "S-2100": ("Ohio 6s, 1850", "Ohio (safe)", "#2a78d6"),
    "S-2110": ("Ohio 6s, 1856", "Ohio (safe)", "#2a78d6"),
    "S-2080": ("Ohio 6s, 1860", "Ohio (safe)", "#2a78d6"),
    "S-2010": ("Ohio 5s, 1850", "Ohio (safe)", "#2a78d6"),
    "S-0030": ("Alabama 5s", "Alabama (likely defaulted)", "#e34948"),
    "S-0040": ("Alabama 6s", "Alabama (likely defaulted)", "#e34948"),
    "S-0510": ("Indiana Dollar 5s, 25yr", "Indiana (likely defaulted)", "#eb6834"),
    "S-0540": ("Indiana Sterling 5s, 25yr", "Indiana (likely defaulted)", "#eb6834"),
}
LINESTYLES = ["-", "--", "-.", ":"]  # vary within a state's multiple bonds

DEFAULT_COLOR = "#d03b3b"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
MUTED_TEXT = "#898781"
PRIMARY_TEXT = "#0b0b0b"
SECONDARY_TEXT = "#52514e"
SURFACE = "#fcfcfb"


def main():
    df = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)

    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    style_counter = {}
    for code, (bond_name, state_label, color) in BOND_INFO.items():
        col = f"Other State Debt::{code}"
        s = df[col].dropna()
        s = s[(s.index >= "1835-01-01") & (s.index <= "1845-12-31")]
        n = style_counter.get(color, 0)
        style_counter[color] = n + 1
        ax.plot(
            s.index, s.values, color=color, linewidth=2,
            linestyle=LINESTYLES[n % len(LINESTYLES)],
            solid_capstyle="round", label=f"{bond_name} ({code})",
        )

    ax.axvline(DEFAULT_DATE, color=DEFAULT_COLOR, linestyle="--", linewidth=1.5)
    ax.annotate(
        "PA Default\n(Aug 1842)",
        xy=(DEFAULT_DATE, ax.get_ylim()[1]),
        xytext=(8, -8),
        textcoords="offset points",
        color=DEFAULT_COLOR,
        fontsize=10,
        fontweight="bold",
        va="top",
        ha="left",
    )

    ax.set_xlabel("Date", color=PRIMARY_TEXT, fontsize=11)
    ax.set_ylabel("Price", color=PRIMARY_TEXT, fontsize=11)

    fig.suptitle(
        "Ohio, Alabama & Indiana Bonds Quoted on the NY Market, 1835–1845",
        color=PRIMARY_TEXT,
        fontsize=13,
        fontweight="bold",
        x=0.02,
        y=0.985,
        ha="left",
    )
    fig.text(
        0.02, 0.945,
        "(Not New York bonds -- these live in New-York.xls's \"Other State Debt\" sheet, confirmed via Securities Index.xls)",
        color=SECONDARY_TEXT,
        fontsize=9,
        ha="left",
        va="top",
    )

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    ax.grid(True, color=GRID_COLOR, linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(AXIS_COLOR)

    ax.tick_params(colors=MUTED_TEXT, labelsize=9)

    ax.legend(
        loc="lower left", frameon=False, fontsize=8.5, ncol=2,
        labelcolor=PRIMARY_TEXT,
    )

    fig.tight_layout(rect=(0, 0, 1, 0.90))
    out_path = OUTPUT_DIR / "ny_candidates_chart.png"
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    print(f"saved -> {out_path}")


if __name__ == "__main__":
    main()
