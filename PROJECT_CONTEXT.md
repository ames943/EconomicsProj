# Project Context: 1840s State Debt Credibility Test

## Research Question
Did bond markets treat the federal government's refusal to bail out defaulting
states in the early 1840s as a credible commitment? Test this by checking
whether defaulting states faced persistently higher bond yields afterward
compared to states that avoided default, and whether "risky but survived"
states landed in between.

## Background
In the 1830s, US states borrowed heavily from British/Dutch investors to fund
canals, railroads, and banks. The Panic of 1837 crashed state revenues. Nine
states plus Florida Territory defaulted in the early 1840s. The federal
government (Tyler administration) refused to bail any of them out, unlike the
1790 Hamilton assumption of state Revolutionary War debts. This project tests
whether bond markets actually believed that refusal was permanent, using real
price data rather than just historical narrative.

This ties to a March 2026 blog post by Stanford economist Hanno Lustig,
"Blue Bonds for Europe," which argues the EU's current debate over joint
"blue bonds" repeats this exact dilemma, and that credible no-bailout
commitments are what force real fiscal discipline.

## Methodology (current, post-meeting with advisor)
1. Group US states into three buckets:
   - Defaulted (e.g. Pennsylvania, Maryland, Indiana, Illinois, Michigan,
     Arkansas, Mississippi, Louisiana, Florida Territory)
   - Survived but were considered risky (e.g. New York, faced railroad
     bankruptcies and bank failures but never defaulted)
   - Always safe / never seriously at risk
2. Pull raw bond PRICE data (not yield) from the EH.net Early U.S. Securities
   Prices database, since yield isn't directly given, we compute it ourselves
   from price (and known coupon/interest terms per bond).
3. Convert prices to approximate yields (yield ≈ coupon rate / price, needs
   coupon rate info per bond, which may require the codebook or Bayley
   Treasury document for term details).
4. Compare yield trends across the three groups from the 1840s through the
   1850s (extended window per advisor's suggestion, not just 1842-45).
5. Hypothesis: defaulting states should show persistently higher yields
   after default than states that never defaulted; "risky but survived"
   states should land in between.

## Data Sources
- EH.net Early U.S. Securities Prices database:
  https://eh.net/database/early-u-s-securities-prices/
  - New York file: https://eh.net/wp-content/uploads/2013/11/New-York.xls
  - Philadelphia file: https://eh.net/wp-content/uploads/2013/11/Philadelphia1.xls
  - Sheet needed: "U.S. and State Debt"
  - Structure: weekly date rows (~3,148 rows), paired columns per security
    (e.g. S-2420 / S-2420a), state debt columns prefixed "S-", US federal
    debt columns prefixed "US-". NO built-in legend mapping codes to state
    names, need a codebook (advisor may have this, or Kim & Wallis /
    Bayley Treasury document may help identify specific codes).
  - Already confirmed: several S-code columns show a sharp price decline
    from ~90 to ~60 in late 1841, consistent with pre-default risk pricing
    ahead of Pennsylvania's actual August 1842 default.
- 1880 Census, Vol. 7, Report on Valuation, Taxation, and Public Indebtedness:
  https://www.census.gov/library/publications/1884/dec/vol-07-valuation-taxation.html
  Has a "Public Indebtedness" section by state, useful for debt totals as
  context, not for yields directly.

## Key reference papers (background, not yet used in analysis)
- Hall & Sargent, Pennsylvania working paper (pennsylvania_1820_1860.pdf) -
  budget constraint framework for PA, defaulted August 1842
- Hall & Sargent, New York working paper (new_york_1813_1860.pdf) - budget
  constraint framework for NY, avoided default
- Sargent (2012) - balanced-budget rules as post-crisis credibility restoration
- English (1996), AER - 1840s defaults as sovereign default cost test case
- Kim & Wallis (2005), Economic History Review - transatlantic bond market

## Advisor / meeting context
- Advisor: Professor George Hall (Brandeis), co-advisor Thomas Sargent (NYU)
- Goal: complete enough of the analysis to bring back concrete results/
  progress for the next advisor meeting
- This is an independent add-on project, separate from my assigned team
  work (Team Texas)
