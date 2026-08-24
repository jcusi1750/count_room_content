"""
entries.py
----------
Fill this in by hand once a week, after you run `python3 report.py`
from ~/wallet_scout/.

RULES — keep every entry "content-safe":
  - NO wallet addresses
  - NO dollar amounts tied to a specific trader
  - NO anything that would let someone else copy your screening or
    identify a real person/wallet
  - Only pattern-level facts: what happened, not who/how much

Each entry is one card. Add as many as you want to post this week —
delete or comment out ones you don't want to publish.
"""

ENTRIES = [
    {
        "headline": "New Wallet Flagged",
        "context": "Consistent MLB-only activity detected. Entering 21-day consistency clock.",
        "tag": "WATCHLIST",
    },
    {
        "headline": "Wallet Disqualified",
        "context": "Cross-sport activity (esports) broke sport-purity screen.",
        "tag": "SCREENED OUT",
    },
    # Add more entries here, same shape as above.
]
