"""Build meeting_prep_final.docx -- advisor meeting prep document.

Assembles the current state of the 1840s state debt credibility test
(PROJECT_CONTEXT.md is the source of record) into a single Word document:
research question recap, what changed since last meeting, the three-tier
empirical results with embedded charts, headline takeaway, a talking-points
script, and open items for the next phase.
"""

from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

INK = RGBColor(0x0B, 0x0B, 0x0B)
MUTED = RGBColor(0x52, 0x51, 0x4E)


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item)


def add_caption(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = MUTED


def script_line(doc, text, speaker_note=None):
    p = doc.add_paragraph()
    p.add_run(text)
    if speaker_note:
        p2 = doc.add_paragraph()
        run = p2.add_run(f"[{speaker_note}]")
        run.italic = True
        run.font.color.rgb = MUTED
        run.font.size = Pt(10)


def main():
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = INK

    # --- 1. Title/header ---
    title = doc.add_heading(
        f"1840s State Debt Credibility Test — Advisor Meeting, {date.today().strftime('%B %-d, %Y')}",
        level=0,
    )

    # --- 2. Research question recap ---
    doc.add_heading("Research Question", level=1)
    doc.add_paragraph(
        "Did bond markets treat the federal government's refusal to bail out defaulting states in the "
        "early 1840s as a credible commitment? The test: whether states that actually defaulted show "
        "persistently higher bond yields after the federal no-bailout signal than states that never "
        "defaulted, with states that were at real risk but ultimately survived landing in between. This "
        "ties to Hanno Lustig's March 2026 \"Blue Bonds for Europe\" post, which argues the EU's current "
        "debate over joint \"blue bonds\" repeats this exact dilemma, and that a credible no-bailout "
        "commitment is what forces real fiscal discipline. The 1840s episode is a real historical test of "
        "that argument: does the market actually believe a no-bailout commitment once it's made, or does it "
        "keep pricing in the possibility of rescue?"
    )

    # --- 3. What's changed since last meeting ---
    doc.add_heading("What's Changed Since Last Meeting", level=1)
    add_bullets(doc, [
        "Resolved all three open items from last meeting: before/after framing (panic window vs. policy "
        "window are now both explicitly defined and kept separate, not conflated), the no-bailout anchor "
        "date (Feb 11 1843, the Gwin/McDuffie assumption debate, reinforced by U.S. consul Christopher "
        "Hughes's Apr-Jul 1843 statements denying federal responsibility to European bankers -- flag: this "
        "still rests on secondary sources, not a primary-document read), and bond seniority (New York's "
        "canal bonds carry a real revenue pledge that the other states' general-obligation bonds lack -- "
        "resolved by switching to a maturity-matched New York GO bond for the primary comparison instead).",
        "Found and corrected a significant yield-calculation issue: yield-to-maturity assumes the bond "
        "redeems at full par on schedule, an assumption that breaks down for an issuer already in active "
        "default. Discovered via Pennsylvania: one bond (S-2410) showed a spurious 30% average YTM against "
        "the same data that gives ~9.5% under current yield. Adopted a rule to use current yield instead of "
        "YTM for any observation falling inside a state's own active-default period, regardless of that "
        "bond's proximity to its own maturity.",
        "Discovered Alabama did not actually default in this episode -- it raised direct taxation in early "
        "1842 and used state-bank liquidation proceeds to keep meeting its debt service, unlike Pennsylvania "
        "and Indiana. Moved Alabama from the \"defaulted\" bucket to \"risky but survived,\" pending your "
        "confirmation.",
        "Found that Pennsylvania's original headline finding (price falling from ~90 to ~40 by Aug-Sept "
        "1842) is panic-window evidence, not policy-window persistence evidence -- the bond behind that "
        "number (S-2240) has zero usable observations after the April 1843 no-bailout signal. Pennsylvania's "
        "actual persistence evidence comes from two previously-unused bonds (S-2330, S-2410) found via a "
        "fuller codebook re-scan that turned up 34 Pennsylvania bond codes instead of the original 3.",
    ])

    # --- 4. Empirical results ---
    doc.add_heading("Empirical Results", level=1)

    doc.add_heading("a. Panic-Window Comparison (pre-1843)", level=2)
    doc.add_paragraph(
        "All five states/buckets, 1835-1845. Pennsylvania's price collapse is the sharpest and most visible "
        "move in the window (yield spiking above 15% into its Aug 1842 default). New York's canal bonds show "
        "real stress and a full recovery by 1843-45. Ohio dips hard alongside everyone else during the panic "
        "but recovers cleanly. Alabama and Indiana both show a sustained, not-fully-recovered elevation that "
        "persists through the end of this window."
    )
    if (OUTPUT_DIR / "chart_panic_window.png").exists():
        doc.add_picture(str(OUTPUT_DIR / "chart_panic_window.png"), width=Inches(6.3))
    add_caption(
        doc,
        "Yield = mean across each state's usable primary bonds per date. YTM (approx.) for Pennsylvania/Ohio/"
        "New York; current yield for Alabama/Indiana (no usable maturity data) and for any state during its "
        "own active-default period (PA Aug 1842-Feb 1845, Indiana from Jan 1841). Alabama reclassified from "
        "\"defaulted\" to \"risky but survived\" -- pending advisor confirmation. New York (S-1650) GO bond "
        "data begins Jul 1842; pre-1842 NY credit risk is not directly observable in this series.",
    )

    doc.add_heading("b. Policy-Window Persistence, Short/Medium-Term (Apr 1843 onward)", level=2)
    doc.add_paragraph(
        "Pennsylvania shows roughly a 2 percentage-point yield premium over Ohio in the ~20 months of "
        "post-signal data it can support (S-2270/S-2330/S-2410 combined). Alabama shows a premium of similar "
        "magnitude, also around 2pp, despite not technically defaulting. New York shows no measurable "
        "premium over Ohio in the window its GO bond is actually observable. Two caveats on the New York "
        "result, stated plainly: (1) New York's GO bond has zero price data before July 1842, so we cannot "
        "observe whether it was under stress during the actual 1839-42 trough -- this is a data-coverage "
        "gap, not a finding of safety. (2) Even within the window we can observe, New York's GO bond price "
        "never drops below par while its canal bonds do -- but the canal bonds carry toll-revenue risk that "
        "is distinct from general state creditworthiness, so this residual gap may not speak cleanly to "
        "New York's overall credit risk."
    )
    if (OUTPUT_DIR / "chart_policy_short_medium.png").exists():
        doc.add_picture(str(OUTPUT_DIR / "chart_policy_short_medium.png"), width=Inches(6.3))
    add_caption(
        doc,
        "Yield = mean across each state's usable primary bonds per date. YTM (approx.) for Pennsylvania/Ohio/"
        "New York; current yield for Alabama/Indiana (no usable maturity data) and for any state during its "
        "own active-default period (PA Aug 1842-Feb 1845, Indiana from Jan 1841). Lines end where each "
        "state's usable data ends -- not a shared cutoff; see per-line labels. Alabama reclassified from "
        "\"defaulted\" to \"risky but survived\" -- pending advisor confirmation. New York (S-1650) GO bond "
        "data begins Jul 1842; pre-1842 NY credit risk is not directly observable in this series.",
    )

    doc.add_heading("c. Policy-Window Persistence, Long-Term (through the 1850s)", level=2)
    doc.add_paragraph(
        "Ohio vs. Alabama only -- the two states with genuine decade-spanning, dense coverage. Pennsylvania, "
        "Indiana, and New York do not have comparable long-run data and are excluded from this comparison "
        "rather than artificially extended. With Alabama reclassified, this chart no longer tests defaulted "
        "vs. safe -- it tests whether a risky-but-survived state's yield converges toward the safe state's "
        "over time. Alabama opens near-identical to Ohio right after the signal, widens to a ~2pp premium by "
        "1847-48, then narrows but never fully closes through 1853."
    )
    if (OUTPUT_DIR / "chart_policy_long_term.png").exists():
        doc.add_picture(str(OUTPUT_DIR / "chart_policy_long_term.png"), width=Inches(6.3))
    add_caption(
        doc,
        "Restricted to Ohio (S-2110/S-2080) and Alabama (S-0030) -- the only two series with genuine "
        "decade-long density. Pennsylvania, Indiana, and New York cannot support this window with current "
        "data. Alabama reclassified from \"defaulted\" to \"risky but survived\" -- pending advisor "
        "confirmation.",
    )

    # --- 5. Headline takeaway ---
    doc.add_heading("Headline Takeaway", level=1)
    doc.add_paragraph(
        "The market appears to price a consistent, modest (~2 percentage point) yield penalty for states "
        "that actually defaulted -- and Alabama's near-miss shows a premium of similar size despite never "
        "technically defaulting, suggesting the market was pricing real distress rather than the formal "
        "default event itself. But we don't see a comparable premium for a state whose distress didn't "
        "culminate in default (Ohio, which is the safe baseline throughout) or for New York, where the only "
        "usable instrument doesn't cover the period that would show it. This is a more precise, if more "
        "modest, claim than the original three-tier \"graduated risk ladder\" framing -- the persistence "
        "effect is real but smaller than first thought, and the middle bucket is better evidenced by Alabama "
        "than by New York right now."
    )

    # --- 6. Talking-points script ---
    doc.add_heading("Talking-Points Script", level=1)
    doc.add_paragraph(
        "The following is written to be read aloud directly while screen-sharing this document, walking "
        "through the \"what's changed,\" \"results,\" and \"takeaway\" sections above."
    ).italic = True

    script_line(
        doc,
        "Since we last talked, I closed out all three open items you flagged, and along the way I found a "
        "couple of things that actually change the shape of the results -- so let me walk through those "
        "first, then show you where the analysis stands now."
    )
    script_line(
        doc,
        "On the three open items: the before/after framing is now cleanly split into two separate windows -- "
        "a panic window around the 1837 shock, and a policy window around the actual no-bailout signal -- "
        "and I don't conflate them anywhere anymore. For the no-bailout date itself, I've settled on February "
        "11, 1843, the Gwin/McDuffie assumption debate in Congress, which I'm treating as reinforced by "
        "consul Christopher Hughes's statements to European bankers that April through July. I want to flag "
        "that both of those rest on secondary sources -- I couldn't get into the Congressional Globe "
        "transcript or McGrane's book directly, so if the exact date matters for the writeup we should treat "
        "that as still needing a primary-source check.",
        speaker_note="Pause here if Hall wants to push on the date -- he may know a way to access McGrane directly.",
    )
    script_line(
        doc,
        "On seniority: it turned out the New York bonds I'd originally picked were canal bonds, which carry "
        "a real revenue pledge on canal tolls -- that's a different security structure than the general-"
        "obligation bonds I was using for the other four states. I found a genuine New York GO bond, "
        "maturity-matched to the canal picks, and swapped it in for the primary comparison. I kept the canal "
        "bonds as a secondary reference, but they're not doing any work in the main results anymore."
    )
    script_line(
        doc,
        "Now, the more consequential finding: I caught a real problem in how I was computing yield. I'd been "
        "using yield-to-maturity everywhere I had a maturity date, but YTM assumes the bond pays back full "
        "face value on schedule -- and that assumption just doesn't hold for a state that's actively in "
        "default. I found this because one of Pennsylvania's bonds was showing a 30 percent average yield, "
        "which is a huge outlier -- and when I checked, the same price data gives about 9.5 percent under "
        "current yield instead. So I built a rule: for any state, during its own active-default period, use "
        "current yield instead of YTM, no matter how far that bond is from its own maturity. That fix alone "
        "brought Pennsylvania's post-signal premium over Ohio down from about 13 percentage points to about "
        "2 -- which is a much more believable number, but it's also a much smaller effect than the original "
        "chart implied."
    )
    script_line(
        doc,
        "The other big finding: Alabama, which I'd had bucketed as \"defaulted\" since the very first pass "
        "through the codebook, actually didn't default in this episode at all. It raised taxes and liquidated "
        "its state bank to keep servicing its debt. So I've moved it into the \"risky but survived\" bucket "
        "alongside New York -- I want your sign-off on that before it's final, since it's been baked into "
        "every table and chart up to this point."
    )
    script_line(
        doc,
        "One more thing worth flagging: Pennsylvania's headline number from our very first pass -- the price "
        "falling from about 90 to about 40 by August-September 1842 -- turns out to be panic-window evidence "
        "only. The bond behind that number stops having usable data right around the signal date, so it "
        "can't actually speak to persistence. I found two other Pennsylvania bonds that do have real "
        "post-signal coverage, and those are what's driving the Pennsylvania numbers now."
    )
    script_line(
        doc,
        "So, walking through the three charts. First, the panic window -- this is the full five-state "
        "picture through 1845, and it looks close to what we expected: Pennsylvania's collapse is sharpest, "
        "New York's canal bonds dip and recover, Ohio dips with everyone else but comes back, and Alabama "
        "and Indiana both stay elevated without a clean recovery."
    )
    script_line(
        doc,
        "Second, the policy window, short and medium term. This is the one that actually tests the "
        "hypothesis. Pennsylvania and Alabama both show about a 2 percentage-point premium over Ohio, "
        "similar in size to each other even though only one of them technically defaulted. New York shows "
        "essentially no premium in this window -- but I want to be upfront that this comes with two caveats, "
        "not one clean finding. New York's GO bond simply has no price data before July 1842, so we can't "
        "see whether it was stressed during the actual worst of the crisis -- that's a coverage gap, not "
        "evidence of safety. And even in the window we can see, while the GO bond never drops below par, its "
        "canal bonds do -- but that could be a toll-revenue-specific risk rather than a statement about New "
        "York's general credit."
    )
    script_line(
        doc,
        "Third, the long-term window through the 1850s -- this only works for Ohio and Alabama, since "
        "they're the only two with real decade-spanning data. And here Alabama's premium over Ohio actually "
        "widens for a few years after the signal, peaking around 1847-48, then narrows but never fully closes "
        "through 1853."
    )
    script_line(
        doc,
        "So where that leaves us: the market does seem to price a consistent, modest penalty -- somewhere "
        "around 2 percentage points -- for states that actually got into real distress, whether or not they "
        "technically defaulted. What we don't have yet is a clean middle-bucket story from New York, because "
        "the instrument we have for it just doesn't cover the period that would show it. That's a more "
        "precise but more modest claim than the three-tier \"graduated ladder\" framing we started with, and "
        "I think that's an honest place to be right now rather than something to paper over."
    )
    script_line(
        doc,
        "That's where I'd like your input most: on the Alabama reclassification, and on whether it's worth "
        "chasing down a different New York instrument or additional data source to actually test the middle "
        "bucket properly."
    )

    # --- 7. Open items for next phase ---
    doc.add_heading("Open Items for Next Phase", level=1)
    add_bullets(doc, [
        "The 1850s extension is only supportable for Ohio and Alabama with current data; Pennsylvania, "
        "Indiana, and New York all hit real data ceilings well before 1850 and cannot be extended into a "
        "full-decade comparison without a new data source.",
        "The canal/robustness comparison (New York S-1750/S-1820/S-1950, plus Ohio's and Indiana's canal "
        "bonds) has not yet been built as a standalone script -- it exists conceptually but isn't a "
        "reproducible output yet.",
        "The Indiana preferred/deferred tranche test (splitting the 1846-47 Butler Bill restructuring into "
        "its preferred vs. deferred canal debt) has not yet been run.",
        "The February 1843 no-bailout anchor date still rests on two secondary sources (a summary of the "
        "Congressional Globe debate and Hughes's statements as reported elsewhere) -- the original "
        "Congressional Globe transcript and McGrane's book were paywalled/inaccessible and this is not yet "
        "primary-source confirmed.",
    ])

    out_path = OUTPUT_DIR / "meeting_prep_final.docx"
    doc.save(str(out_path))
    print(f"saved -> {out_path}")


if __name__ == "__main__":
    main()
