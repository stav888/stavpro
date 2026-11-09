#!/usr/bin/env python3
"""Compose a 1080x1920 sample/approval frame from an illustration-only still.

Generated sketches must contain the drawing only (no title, underline, caption,
or page counter). This script applies the same layout as build.py so the
approval sample matches the finished Short.

Usage:
  PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf \\
    python preview_frame.py illustration.jpg \\
      --title "THE SPY WHO INVENTED SPIES" \\
      --subtitle "He invented an entire spy network that never existed." \\
      --i 1 --n 14 -o sample_frame.png
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
ART_MAX_W, ART_MAX_H = 1060, 1150
ART_CENTER_Y = 790
ART_Y_MIN, ART_Y_MAX = 200, 1400
BBOX_THRESH, BBOX_MARGIN = 200, 14

TITLE_SIZE, TITLE_Y = 64, 115
TITLE_COLOR = (20, 20, 20, 255)
UNDERLINE = ((400, 165), (680, 165))  # 280 px ≈ 26% of width
UNDERLINE_W, UNDERLINE_COLOR = 6, (225, 55, 40, 255)
SUB_SIZES = (62, 56, 52)
SUB_MAX_W, SUB_MAX_LINES, SUB_LINE_GAP, SUB_Y0 = 960, 2, 70, 1430
SUB_COLOR = (12, 12, 12, 255)
COUNTER_SIZE, COUNTER_Y = 32, 1835
COUNTER_COLOR = (130, 130, 130, 255)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def balanced_wrap(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    words = text.split()
    if draw.textlength(text, font=fnt) <= max_w:
        return [text]
    if len(words) <= 1:
        return [text]
    best = None
    skip = {"a", "the", "to", "and", "in", "of", "his", "an", "be", "at", "was", "from", "on", "by", "named"}
    for i in range(1, len(words)):
        if words[i - 1].lower().rstrip(",.:;") in skip and i < len(words) - 1:
            continue
        a = " ".join(words[:i])
        b = " ".join(words[i:])
        if not b:
            continue
        m = max(draw.textlength(a, font=fnt), draw.textlength(b, font=fnt))
        if m <= max_w and (best is None or m < best[0]):
            best = (m, [a, b])
    return best[1] if best else [text]


def art_bbox(img: Image.Image) -> tuple[int, int, int, int]:
    a = np.asarray(img.convert("L")) < BBOX_THRESH
    ys, xs = np.where(a)
    if len(xs) == 0:
        return 0, 0, img.width, img.height
    m = BBOX_MARGIN
    return (
        max(0, int(xs.min()) - m),
        max(0, int(ys.min()) - m),
        min(img.width, int(xs.max()) + m + 1),
        min(img.height, int(ys.max()) + m + 1),
    )


def place_art(canvas: Image.Image, src: Image.Image) -> None:
    x0, y0, x1, y1 = art_bbox(src)
    cropped = src.crop((x0, y0, x1, y1)).convert("RGBA")
    cw = max(2, (cropped.width // 2) * 2)
    ch = max(2, (cropped.height // 2) * 2)
    cropped = cropped.resize((cw, ch), Image.Resampling.LANCZOS) if (cw, ch) != cropped.size else cropped
    sc = min(ART_MAX_W / cw, ART_MAX_H / ch)
    sw = max(2, int(cw * sc) // 2 * 2)
    sh = max(2, int(ch * sc) // 2 * 2)
    scaled = cropped.resize((sw, sh), Image.Resampling.LANCZOS)
    x = (W - sw) // 2
    y = max(ART_Y_MIN, min(ART_Y_MAX - sh, ART_CENTER_Y - sh // 2))
    canvas.paste(scaled, (x, y), scaled if scaled.mode == "RGBA" else None)


def draw_overlays(
    canvas: Image.Image,
    title: str,
    subtitle: str,
    i: int,
    n: int,
    font_path: str,
) -> None:
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.text((540, TITLE_Y), title.upper(), font=font(font_path, TITLE_SIZE), fill=TITLE_COLOR, anchor="mm")
    d.line([UNDERLINE[0], UNDERLINE[1]], fill=UNDERLINE_COLOR, width=UNDERLINE_W)
    d.text(
        (540, COUNTER_Y),
        f"\u2014 {i} / {n} \u2014",
        font=font(font_path, COUNTER_SIZE),
        fill=COUNTER_COLOR,
        anchor="mm",
    )
    canvas.alpha_composite(ov)

    if not subtitle.strip():
        return
    sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(sub)
    lines = [subtitle]
    chosen = SUB_SIZES[-1]
    for fs in SUB_SIZES:
        fnt = font(font_path, fs)
        lines = balanced_wrap(d, subtitle, fnt, SUB_MAX_W)
        if len(lines) <= SUB_MAX_LINES and all(d.textlength(l, font=fnt) <= SUB_MAX_W for l in lines):
            chosen = fs
            break
    lines = lines[:SUB_MAX_LINES]
    fnt = font(font_path, chosen)
    y = SUB_Y0
    for line in lines:
        d.text((540, y), line, font=fnt, fill=SUB_COLOR, anchor="ma")
        y += SUB_LINE_GAP
    canvas.alpha_composite(sub)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("illustration", help="Illustration-only still (no baked-in text)")
    p.add_argument("--title", required=True, help="English title (UPPERCASE in the frame)")
    p.add_argument("--subtitle", default="", help="One English subtitle chunk for the sample")
    p.add_argument("--i", type=int, default=1, help="Page index (1-based)")
    p.add_argument("--n", type=int, default=1, help="Total pages")
    p.add_argument("-o", "--output", default="sample_frame.png", help="Output 1080x1920 PNG")
    p.add_argument(
        "--font",
        default=os.environ.get("PATRICK_HAND_TTF", "PatrickHand-Regular.ttf"),
        help="Path to PatrickHand-Regular.ttf (or set PATRICK_HAND_TTF)",
    )
    args = p.parse_args()

    if not os.path.isfile(args.font):
        print(f"Font not found: {args.font}\nSet PATRICK_HAND_TTF to PatrickHand-Regular.ttf", file=sys.stderr)
        return 1
    if not os.path.isfile(args.illustration):
        print(f"Illustration not found: {args.illustration}", file=sys.stderr)
        return 1

    src = Image.open(args.illustration).convert("RGBA")
    canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    place_art(canvas, src)
    draw_overlays(canvas, args.title, args.subtitle, args.i, args.n, args.font)
    out = canvas.convert("RGB")
    out.save(args.output)
    print(f"wrote {args.output} ({out.width}x{out.height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
