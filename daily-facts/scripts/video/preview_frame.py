#!/usr/bin/env python3
"""Approval sample frame for Daily Facts Arete: composite a generated illustration (no text in it)
with our code-drawn overlays, exactly as build_highlight_wash.py draws them. Never ask an image
generator to draw text.

Layout on the 1080x1920 canvas (Montserrat Bold, env MONTSERRAT_TTF = the variable TTF):
  hook / title (optional, first second only): white, 76 px (shrinks to fit 960 px, max 2 lines),
      soft black shadow, centred, first line top at y=300
  subtitle phrase (3-7 words): white, 84 px (shrinks by 4 px until it fits 940 px), top at y=1344
      (70% of height, low and centred), soft blurred shadow + thin dark stroke, no box;
      word number --hi in the video's ONE highlight colour (--color, default cyan 2EF2FF)
  no underline, no page counter (not part of the Arete look)

Usage: python preview_frame.py picks/s01.png --subtitle "Twenty thousand people once lived" \
         --hi 2 --hook "20,000 PEOPLE. 85 METERS DOWN." -o sample_frame.png
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
ap = argparse.ArgumentParser()
ap.add_argument('image'); ap.add_argument('-o', '--out', default='sample_frame.png')
ap.add_argument('--subtitle', required=True); ap.add_argument('--hi', type=int, default=0, help='0-based word to highlight')
ap.add_argument('--color', default='2EF2FF'); ap.add_argument('--hook', default='')
a = ap.parse_args()
P = os.environ.get('MONTSERRAT_TTF', 'Montserrat-VariableFont_wght.ttf')
HI = tuple(int(a.color[i:i + 2], 16) for i in (0, 2, 4))

def font(sz):
    f = ImageFont.truetype(P, sz)
    try: f.set_variation_by_name('Bold')
    except Exception: pass
    return f

img = Image.open(a.image).convert('RGB')
if img.height <= img.width: raise SystemExit('reject: illustration must be vertical 9:16')
# cover-fit to 1080x1920 (the illustration fills the whole frame, edge to edge)
s = max(W / img.width, H / img.height)
img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
img = img.crop(((img.width - W) // 2, (img.height - H) // 2, (img.width - W) // 2 + W, (img.height - H) // 2 + H)).convert('RGBA')

def text_layer(lines_words, y0, sz_start, maxw, hi_idx=None, line_h=None):
    sz = sz_start; d = ImageDraw.Draw(Image.new('L', (1, 1)))
    while True:
        f = font(sz); sp = d.textlength(' ', font=f)
        widths = [sum(d.textlength(w, font=f) for w in ws) + sp * (len(ws) - 1) for ws in lines_words]
        if max(widths) <= maxw or sz <= 40: break
        sz -= 4
    lh = line_h or int(sz * 1.15)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for li, ws in enumerate(lines_words):
        x = (W - widths[li]) / 2; y = y0 + li * lh
        for w in ws: sd.text((x + 4, y + 5), w, font=f, fill=(0, 0, 0, 200)); x += sd.textlength(w, font=f) + sp
    lay = sh.filter(ImageFilter.GaussianBlur(6)); dd = ImageDraw.Draw(lay); k = 0
    for li, ws in enumerate(lines_words):
        x = (W - widths[li]) / 2; y = y0 + li * lh
        for w in ws:
            dd.text((x, y), w, font=f, fill=HI if k == hi_idx else (255, 255, 255), stroke_width=3, stroke_fill=(20, 12, 6, 180))
            x += dd.textlength(w, font=f) + sp; k += 1
    return lay

if a.hook:
    ws = a.hook.split(); half = (len(ws) + 1) // 2
    lines = [ws] if len(ws) <= 4 else [ws[:half], ws[half:]]
    img = Image.alpha_composite(img, text_layer(lines, 300, 76, 960))
img = Image.alpha_composite(img, text_layer([a.subtitle.split()], int(H * 0.70), 84, 940, hi_idx=a.hi))
img.convert('RGB').save(a.out); print(a.out)
