"""
render_card.py
---------------
Turns each entry in entries.py into a 1080x1350 PNG image card,
saved into output/ for you to review before posting.

You don't need to edit this file — just run it:
    python3 render_card.py
"""

import os
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

from entries import ENTRIES

WIDTH, HEIGHT = 1080, 1350
BG_COLOR = (17, 24, 39)        # dark navy
ACCENT_COLOR = (56, 189, 175)  # teal
TEXT_COLOR = (240, 240, 245)
TAG_BG = (56, 189, 175)
TAG_TEXT = (17, 24, 39)

FONT_CANDIDATES_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]
FONT_CANDIDATES_REGULAR = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
]


def load_font(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    avg_char_w = font.getbbox("x")[2] or 10
    approx_chars = max(10, int(max_width / avg_char_w))
    lines = textwrap.wrap(text, width=approx_chars)
    return lines


def render_entry(entry, index):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    font_tag = load_font(FONT_CANDIDATES_BOLD, 32)
    font_headline = load_font(FONT_CANDIDATES_BOLD, 68)
    font_context = load_font(FONT_CANDIDATES_REGULAR, 42)
    font_footer = load_font(FONT_CANDIDATES_REGULAR, 30)

    margin = 80

    tag_text = entry.get("tag", "UPDATE")
    tag_bbox = draw.textbbox((0, 0), tag_text, font=font_tag)
    tag_w = tag_bbox[2] - tag_bbox[0] + 40
    tag_h = tag_bbox[3] - tag_bbox[1] + 24
    draw.rounded_rectangle(
        [margin, 100, margin + tag_w, 100 + tag_h], radius=tag_h // 2, fill=TAG_BG
    )
    draw.text((margin + 20, 108), tag_text, font=font_tag, fill=TAG_TEXT)

    headline_y = 100 + tag_h + 60
    for line in wrap_text(draw, entry["headline"], font_headline, WIDTH - 2 * margin):
        draw.text((margin, headline_y), line, font=font_headline, fill=TEXT_COLOR)
        headline_y += 82

    context_y = headline_y + 40
    for line in wrap_text(draw, entry["context"], font_context, WIDTH - 2 * margin):
        draw.text((margin, context_y), line, font=font_context, fill=(200, 200, 210))
        context_y += 56

    draw.rectangle([margin, HEIGHT - 180, margin + 100, HEIGHT - 174], fill=ACCENT_COLOR)

    draw.text((margin, HEIGHT - 150), "THE COUNT ROOM", font=font_footer, fill=TEXT_COLOR)
    draw.text(
        (margin, HEIGHT - 110),
        "Verified, self-sourced market signals",
        font=font_footer,
        fill=(150, 150, 160),
    )

    return img


def main(subfolder=None, prefix=""):
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    if subfolder:
        out_dir = os.path.join(out_dir, subfolder)
    os.makedirs(out_dir, exist_ok=True)

    if not ENTRIES:
        print("No entries in entries.py — add some before running this.")
        return

    stamp = datetime.now().strftime("%Y-%m-%d")
    written = []
    for i, entry in enumerate(ENTRIES, start=1):
        img = render_entry(entry, i)
        filename = f"{prefix}{stamp}_card_{i:02d}.png"
        path = os.path.join(out_dir, filename)
        img.save(path)
        written.append(path)

    print(f"Generated {len(written)} card(s) in {out_dir}/:")
    for p in written:
        print(f"  - {os.path.basename(p)}")
    print("\nReview these before posting. Nothing is auto-published.")
    return len(written)


if __name__ == "__main__":
    main()
