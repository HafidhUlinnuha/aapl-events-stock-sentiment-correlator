# Apple Events Impact & Stock Sentiment Correlator

A personal data study analyzing how Apple's major product announcements 
influence short-term AAPL stock price movements using event-study methodology.

---

## Research Question
Do Apple's biggest product moments actually move the stock price — 
and if so, for how long?

## Methodology
- **Event Window:** H-0 (announcement day) to H+7 (7 days after)
- **Events Analyzed:** Major Apple announcements from 2020–2026
  (iPhone launches, WWDC, Apple Vision Pro, etc.)
- **Data Source:** AAPL historical price data via yfinance (Python)
- **Analysis:** Stock return isolation per event using Pandas

## Key Finding
5 out of 7 major Apple announcements resulted in negative 7-day returns:

| Event | Return (H-0 to H+7) |
|---|---|
| iPhone 12 Announcement | -4.42% |
| iPhone 13 Announcement | -0.87% |
| iPhone 14 Announcement | -3.37% |
| Apple Vision Pro (WWDC) | +2.43% |
| iPhone 15 Announcement | -1.34% |
| iPhone 16 Announcement | -0.10% |
| iPhone 17 Announcement | +1.51% |

Only Apple Vision Pro and iPhone 17 showed positive returns — 
suggesting markets reward genuine innovation leaps, not iterative releases.

## Tech Stack
- Python (yfinance, Pandas)
- Google Looker Studio (interactive dashboard)

## Files
- `AAPL_Fetch.py` — Script to extract AAPL historical price data via yfinance
- `AAPL_Event_Analysis_Clean.py` — Script to merge and analyze event data against stock prices
- `AAPL_Event_Analysis_Clean.csv` — Curated Apple major event timeline with 7-day return calculations

## Dashboard
[View Interactive Dashboard](https://datastudio.google.com/reporting/03c6e432-20a6-49a9-85bf-6f7492c6002e)

## Disclaimer
This project is for educational and portfolio purposes only. 
Nothing in this analysis constitutes financial advice.
