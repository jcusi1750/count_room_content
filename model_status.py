"""
model_status.py
----------------
Fill this in by hand once a week. Translate from your detailed
research notes (EDGE_ENGINE_STATE.md) into SHORT, SAFE public sentences.

RULES - keep every line "content-safe":
  - NO specific data sources (e.g. don't name "Open-Meteo")
  - NO script names (e.g. don't name "nfl_wind_revalidate2.py")
  - NO exact thresholds or gate numbers from VALIDATION_STANDARD.md
  - NO specific formulas or methodology details
  - Just the plain-English state: is it live, in testing, or killed,
    and roughly why

Each entry becomes one card. Add or remove as many as you want to
post this week.
"""

MODEL_STATUS = [
    {
        "model": "K-Props (High-Tier)",
        "status": "In dry-run testing, tracking toward a verdict.",
        "tag": "TESTING",
    },
    {
        "model": "MLB Hits",
        "status": "In dry-run. Strongest result we've found under our current validation standard, but not live-eligible yet.",
        "tag": "TESTING",
    },
    {
        "model": "NFL Wind Signal",
        "status": "Inconclusive so far - early results are promising but the sample is still too small to call.",
        "tag": "INCONCLUSIVE",
    },
    # Add more lines here, same shape as above.
]
