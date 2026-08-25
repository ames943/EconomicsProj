"""Export caption-free versions of the four newer comparison charts
(Philadelphia/Pittsburgh/Cincinnati city-vs-state, and the canal/
Indiana-tranche robustness chart) for presentation use -- the same
treatment `export_charts_no_caption.py` already gives the original
three-tier chart set.

Does NOT modify any protected script (compare_city_vs_state.py,
compare_city_vs_state_cincinnati_pittsburgh.py, compare_canal_
robustness.py) or their existing captioned output files. Imports each
module read-only, reuses its exact `build_chart(...)` function (same
colors, annotations, data), and temporarily monkeypatches
`Figure.text` (suppresses the caption block) and `Figure.savefig`
(redirects to a new "_clean" filename instead of overwriting the
captioned original) only for the duration of that one call.
"""

import sys
from contextlib import contextmanager
from pathlib import Path

import matplotlib.figure
import pandas as pd

SCRIPTS_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPTS_DIR.parent / "output"
sys.path.insert(0, str(SCRIPTS_DIR))

import compare_city_vs_state_cincinnati_pittsburgh as cin_pit  # noqa: E402
import compare_canal_robustness as canal  # noqa: E402


@contextmanager
def no_caption_saving_as(clean_name: str):
    orig_text = matplotlib.figure.Figure.text
    orig_savefig = matplotlib.figure.Figure.savefig
    orig_tight_layout = matplotlib.figure.Figure.tight_layout

    def noop_text(self, x, y, s, *a, **k):
        # Render an empty string instead of returning None -- suptitle()
        # internally calls Figure.text() too and expects a real Text
        # artist back (accesses ._autopos on it), so a bare no-op crashes
        # it. Only the caption-block calls (long wrapped strings at
        # (0.01, 0.01)) should actually be suppressed.
        if x == 0.01 and y == 0.01:
            s = ""
        return orig_text(self, x, y, s, *a, **k)

    def full_tight_layout(self, *a, **k):
        return orig_tight_layout(self)

    def redirected_savefig(self, fname, *a, **k):
        return orig_savefig(self, str(OUTPUT_DIR / clean_name), *a, **k)

    matplotlib.figure.Figure.text = noop_text
    matplotlib.figure.Figure.tight_layout = full_tight_layout
    matplotlib.figure.Figure.savefig = redirected_savefig
    try:
        yield
    finally:
        matplotlib.figure.Figure.text = orig_text
        matplotlib.figure.Figure.tight_layout = orig_tight_layout
        matplotlib.figure.Figure.savefig = orig_savefig


def main() -> None:
    # Pittsburgh vs. Pennsylvania
    pit = pd.read_csv(OUTPUT_DIR / "city_vs_state_pittsburgh.csv", parse_dates=["date"])
    with no_caption_saving_as("chart_pittsburgh_vs_pa_clean.png"):
        cin_pit.build_chart("Pittsburgh", pit)

    # Cincinnati vs. Ohio
    cin = pd.read_csv(OUTPUT_DIR / "city_vs_state_cincinnati.csv", parse_dates=["date"])
    with no_caption_saving_as("chart_cincinnati_vs_ohio_clean.png"):
        cin_pit.build_chart("Cincinnati", cin)

    # Canal robustness / Indiana tranche (single combined two-panel chart)
    robustness = pd.read_csv(OUTPUT_DIR / "canal_robustness_yields.csv", parse_dates=["date"])
    ny_canal = robustness[robustness.state == "New York"]
    indiana = robustness[robustness.state == "Indiana"]
    with no_caption_saving_as("chart_canal_robustness_clean.png"):
        canal.build_chart(ny_canal, indiana)

    print("done")


if __name__ == "__main__":
    main()
