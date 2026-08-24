"""
render_model_status.py
------------------------
Turns each entry in model_status.py into a card and texts you when
they're ready. Run manually any time:

    python3 render_model_status.py
"""

import os
import subprocess
from datetime import datetime

import render_card
from model_status import MODEL_STATUS

PHONE_NUMBER = "+13122181509"


def build_entries():
    entries = []
    for item in MODEL_STATUS:
        entries.append({
            "headline": item["model"],
            "context": item["status"],
            "tag": item.get("tag", "MODEL STATUS"),
        })
    return entries


def send_notification(num_cards):
    message = (
        f"MODEL STATUS CARDS READY\n\n"
        f"{num_cards} card(s) generated in ~/count_room_content/output/\n"
        f"Review and post when you're back on the Mac."
    )
    script = (
        'tell application "Messages"\n'
        '    set targetService to 1st service whose service type = iMessage\n'
        f'    set targetBuddy to buddy "{PHONE_NUMBER}" of targetService\n'
        f'    send "{message}" to targetBuddy\n'
        'end tell'
    )
    subprocess.run(["osascript", "-e", script])


def main():
    if not MODEL_STATUS:
        print("No entries in model_status.py - add some before running this.")
        return

    entries = build_entries()
    render_card.ENTRIES = entries
    written_count = render_card.main(subfolder="model_status")

    send_notification(len(entries))
    print("\niMessage notification sent.")


if __name__ == "__main__":
    main()
