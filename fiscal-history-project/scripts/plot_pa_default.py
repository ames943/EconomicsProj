"""Plot the S-2240 Philadelphia state-debt price series (1835-1845), with
Pennsylvania's August 1842 default marked, as a quick visual sanity check
of the default-risk pricing pattern found in scripts/identify_candidates.py.
"""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
CSV_PATH = OUTPUT_DIR / "philadelphia_state_debt_prices.csv"
CODE = "S-2240"
DEFAULT_DATE = pd.Timestamp("1842-08-01")

LINE_COLOR = "#2a78d6"
DEFAULT_COLOR = "#d03b3b"
GRID_COLOR = "#e1e0d9"
AXIS_COLOR = "#c3c2b7"
MUTED_TEXT = "#898781"
PRIMARY_TEXT = "#0b0b0b"
SURFACE = "#fcfcfb"


def main():
    df = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)
    s = df[CODE].dropna()
    s = s[(s.index >= "1835-01-01") & (s.index <= "1845-12-31")]

    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    ax.plot(s.index, s.values, color=LINE_COLOR, linewidth=2, solid_capstyle="round")

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
    ax.set_title(
        f"Pennsylvania State Bond Price ({CODE}), 1835–1845",
        color=PRIMARY_TEXT,
        fontsize=13,
        fontweight="bold",
        loc="left",
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

    fig.tight_layout()
    out_path = OUTPUT_DIR / "pa_default_chart.png"
    fig.savefig(out_path, dpi=150, facecolor=SURFACE)
    print(f"saved -> {out_path}")


if __name__ == "__main__":
    main()
