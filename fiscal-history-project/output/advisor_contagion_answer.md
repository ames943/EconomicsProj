# Answering Hall's Contagion Question -- Talking Points for Next Meeting

*Plain-language notes, not a technical write-up. Sourced from
`output/city_vs_state_yields.csv`, `output/city_vs_state_cincinnati.csv`,
`output/city_vs_state_pittsburgh.csv`, and `output/ohio_yield_check.csv` --
none of which were recomputed to write this document, all numbers below
are pulled from those existing files as-is.*

## Hall's framing (Jul 30 2026 meeting)

Hall described state default as "contagious like a disease" -- spreading
to *other states'* bond prices -- and asked a sharper, distinct question:
does it also spread *downward*, from a defaulting state into its own
city's credit? Does Philadelphia get punished along with Pennsylvania, or
does the market tell the two apart even though they're the same place? He
called this "a research question that could become a paper."

**This project already has evidence on two separate questions that
shouldn't get merged into one answer:**

1. **State-to-other-state contagion** -- did PA's default raise NY's,
   Ohio's, or Alabama's *own* credit risk?
2. **State-to-own-city contagion** -- did PA's default raise
   *Philadelphia's* (or now, Pittsburgh's) borrowing cost, even though
   the city itself never defaulted?

Hall's question is specifically #2. Here's what we have on it.

## The direct answer: state-to-own-city, two data points now

### Philadelphia vs. Pennsylvania (the original test)

- Pre-signal (1835-Mar 1843): PA state 6.69% vs. Philadelphia city 5.06%
  -- a 1.63pp gap.
- Post-gap window (Feb-Dec 1844, the only period both series have data,
  apples-to-apples): PA state 7.56% vs. Philadelphia city 4.88% -- a
  2.68pp gap.
- **The gap widens almost entirely because PA's own yield rose (6.69% ->
  7.56%), not because Philadelphia's yield moved at all** (5.06% -> 4.88%,
  flat to very slightly lower).
- Reads as a clean **no-spillover** result: Philadelphia's own borrowing
  cost didn't react to either PA's Aug 1842 default or the Apr 1843
  no-bailout signal, while the state's cost climbed and stayed up.
- Caveat: a 343-day data gap (Feb 1843-Feb 1844) sits almost exactly on
  the immediate post-signal period, so we can't see the city's *immediate*
  reaction -- only that its level was still normal about a year later.
  One city, one state -- not yet generalizable on its own.

### Pittsburgh vs. Pennsylvania (new, second PA city -- Phase 1 of this pass)

- Post-signal window (Apr 1843-Jan 1845, capped at PA's own data
  ceiling): PA state 8.76% vs. Pittsburgh city 6.11% -- a **2.65pp gap**,
  almost identical in size to Philadelphia's 2.68pp post-gap number.
- Same direction, same rough magnitude, a *second* Pennsylvania city.
  This is exactly the kind of replication that turns "one case" into "a
  pattern" -- two different Pennsylvania cities, same no-spillover result.
- Caveat: Pittsburgh's pre-signal data is thin (5 observations, all in
  the six weeks right before the Feb 1843 cutoff), so this is a
  post-signal LEVELS comparison, not a full pre/post widening test the
  way Philadelphia's was. Still a real, second confirmation of the
  no-spillover direction.

### Cincinnati vs. Ohio (new, but a DIFFERENT kind of test -- also Phase 1)

- Post-signal window (Apr 1843-Dec 1850): Ohio state 6.25% vs. Cincinnati
  city 6.36% -- essentially **flat, -0.11pp**.
- This is NOT a third confirmation of "no spillover from a defaulting
  state" -- Ohio never defaulted. There's no state distress for Cincinnati
  to be insulated *from* in the first place. What this actually shows is
  the baseline case: when a state's own credit is fine, its city tracks
  it almost exactly, with no gap at all.
- **Useful as a contrast, not as more evidence for the same claim.** Line
  it up next to Pittsburgh/Philadelphia this way: safe-state city tracks
  its state (≈0pp gap, Cincinnati/Ohio) vs. defaulted-state cities pull
  away from their state (≈2.6-2.7pp gap, Pittsburgh & Philadelphia/PA).
  The gap only opens up when the state itself is under stress -- which is
  itself a nice piece of corroborating logic for the no-spillover finding,
  even though it isn't a second no-spillover test on its own.

**Bottom line for Hall: yes, this answers his question, and now with two
data points on the "defaulting state" side (Philadelphia and Pittsburgh)
both landing at essentially the same ~2.6-2.7pp gap, plus a baseline
comparison (Cincinnati/Ohio) confirming the gap only shows up when the
state itself is actually under stress.** Worth stating plainly that this
is still a small, PA-and-Ohio-only sample -- NYC/Brooklyn (vs. New York
state) remain open and unstarted, per PROJECT_CONTEXT.md.

## The other question: state-to-other-state contagion

This is closer to what the original three-bucket comparison (Defaulted
vs. Risky-but-survived vs. Safe) already tests -- but it's a different
mechanism than "contagion" in the literal spreading sense. The existing
~2pp premium Alabama and (post-correction) Pennsylvania carry over Ohio
in the medium term reflects the market pricing each state's *own* default
risk, not PA's default *causing* Alabama's or Ohio's yields to rise. Worth
being precise about this distinction with Hall: the bucket comparison
answers "did the market treat different states differently based on their
own default status," not "did PA's specific default event spread outward
and infect other states' credit." Different question, different
mechanism, even though the two are easy to conflate verbally.

## A useful cautionary example to mention directly: the Ohio yield-rise check

In the same meeting, Hall separately mentioned that Ohio (never defaulted,
"safe" bucket) "saw yield rise during the 1840s" -- floated as possible
evidence that contagion reached even the safe bucket. This was checked at
monthly resolution (`output/ohio_yield_check.csv`) and the rise is real --
all four Ohio bonds spike from ~90 to ~48-52 in price, bottoming in a
tight window, Mar 12-Apr 9 1842 -- but it happens **4.5-11 months before**
either PA's actual default (Aug 1842) or the Feb/Apr 1843 no-bailout
signal, and Ohio's yields are already falling back to baseline by the time
the signal actually happens. It's the general 1837-42 panic, not a
policy-signal contagion effect.

**Worth raising with Hall directly, framed as a positive, not a
correction for its own sake:** this is a good live example of why this
project insists on separating the "panic window" from the "policy window"
(see PROJECT_CONTEXT.md's Analysis Windows section) -- a real yield move
that looks at first glance like it could support a contagion story turns
out, once you check the actual dates, to be timed to the wrong event
entirely. It's a concrete illustration that the panic/policy distinction
is doing real analytical work in this project, not just a bookkeeping
split.

## Summary if short on time

- Hall's actual question (does default spread to the defaulting state's
  own city) -- **answered, twice now, same result both times**:
  Philadelphia and Pittsburgh both show a ~2.6-2.7pp gap where the state
  yield rises but the city yield doesn't. No spillover into either PA
  city, in this data.
- Cincinnati/Ohio is a useful contrast (no gap at all, because Ohio never
  defaulted) but not a third instance of the same test.
- The state-to-*other-state* contagion question is a different mechanism
  from state-to-own-city, and the existing bucket comparison speaks to it
  more directly, but should be described to Hall as "the market pricing
  each state's own risk," not literal contagion spreading between states.
- The Ohio yield-rise recollection is resolved: real move, wrong window --
  useful as a live demonstration of why the panic/policy split matters,
  worth mentioning as a positive rather than just a fact-check.
