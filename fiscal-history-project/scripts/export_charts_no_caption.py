"""Export caption-free versions of the three yield charts (no gray
footnote block) for presentation use. The captioned originals in
output/*.png remain the source of record (embedded in
meeting_prep_final.docx, referenced in PROJECT_CONTEXT.md) -- these are
a separate, visual-only variant, not a replacement.
"""

from pathlib import Path

import build_yield_charts as byc

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

CHARTS = [
    (byc.build_chart_1, "chart_panic_window_clean.png"),
    (byc.build_chart_2, "chart_policy_short_medium_clean.png"),
    (byc.build_chart_3, "chart_policy_long_term_clean.png"),
]


def finish_no_caption(fig, ax, title, methodology_note, out_name):
    ax.set_xlabel("Date", color=byc.PRIMARY_TEXT, fontsize=11)
    ax.set_ylabel("Yield (%)", color=byc.PRIMARY_TEXT, fontsize=11)
    ax.set_title(title, color=byc.PRIMARY_TEXT, fontsize=13, fontweight="bold", loc="left")
    fig.tight_layout()
    out_path = OUTPUT_DIR / out_name
    fig.savefig(out_path, dpi=150, facecolor=byc.SURFACE)
    byc.plt.close(fig)
    print(f"saved -> {out_path}")


def main():
    byc.finish = finish_no_caption
    df = byc.load_usable()
    name_map = dict(zip(
        ["chart_panic_window.png", "chart_policy_short_medium.png", "chart_policy_long_term.png"],
        ["chart_panic_window_clean.png", "chart_policy_short_medium_clean.png", "chart_policy_long_term_clean.png"],
    ))
    # monkeypatch OUTPUT_DIR writes by renaming inside finish_no_caption via closure over name_map
    orig_finish = finish_no_caption

    def finish_renamed(fig, ax, title, methodology_note, out_name):
        orig_finish(fig, ax, title, methodology_note, name_map.get(out_name, out_name))

    byc.finish = finish_renamed
    byc.build_chart_1(df)
    byc.build_chart_2(df)
    byc.build_chart_3(df)


if __name__ == "__main__":
    main()
