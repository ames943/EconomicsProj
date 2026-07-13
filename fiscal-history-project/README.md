# Fiscal History Project: 1840s State Debt Credibility Test

Did bond markets treat the federal government's refusal to bail out
defaulting states in the early 1840s as a credible commitment? This project
tests that by comparing bond price/yield trends for states that defaulted,
states that were at risk but survived, and states that were never seriously
at risk, using real transatlantic bond price data rather than historical
narrative alone.

See [`PROJECT_CONTEXT.md`](../PROJECT_CONTEXT.md) in the repo root for full
background, methodology, data sources, and advisor context.

## Structure

```
fiscal-history-project/
├── data/
│   └── raw/          # downloaded xls files (EH.net securities prices)
├── scripts/           # parsing and analysis scripts
├── output/            # charts, tables, cleaned csvs
├── requirements.txt
└── README.md
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
