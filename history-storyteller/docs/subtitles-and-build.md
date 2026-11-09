# 4. Timing, subtitles, compose

## Sentence timing table
`../scripts/video/sentence_timing.py` (run in the project folder) needs `audio/sentences.txt`, `audio/asr_words.json`, `audio/narration_norm.wav`:
- Aligns script words to ASR words (difflib), then snaps each sentence's first-word onset to the end of the preceding silence (< -45 dB).
- Sentence `start` = onset - 0.06 s; `end` = next sentence start. Checks the gap before each onset is silent.
- Writes `audio_timing.json` (rows + total) and `ons.json` (per-word onsets for subtitle splits).

## Build (`../scripts/video/build.py OUT.mp4`)
- 1080x1920, 24 fps, H.264 crf 20, AAC 192k 48 kHz. Hard cuts at sentence starts (frame-rounded).
- Per-scene art is auto-cropped to its non-white bbox and scaled to ~1060x1150 max, centred ~y=790, white pad.
- Static overlay per scene (English only): title at top UPPERCASE (Patrick Hand 64, colour `(20,20,20)` at y=115), red underline **x=400–680** (280 px, 6 px thick) at y=165 colour `(225,55,40)`, and `— i / N —` at y=1835 (Patrick Hand 32, grey). **Edit the title string per video.** Never ask the image generator to draw these.
- Subtitles (English only): Patrick Hand **62** (fallback 56 then 52), colour `(12,12,12)`, max 2 lines, 960 px wide, first line at y=1430, line spacing 70. Sentences <=10 words shown whole; longer split into 2–3 balanced chunks at commas or by per-sentence overrides `OV={sentence:[word indexes]}` (edit per video). Line breaks never after a/the/to/and/... Each chunk starts/ends on the frame grid **inside** its sentence; script asserts 0 boundary crossings.
- Scene mapping in this build is 1 scene per sentence row (`anim/scene{i}_r.mp4`); if a project has more scenes than sentences, extend `segs`.
- Concats clips and muxes `audio/narration_norm.wav`.
- Approval sample without a full build: `../scripts/video/preview_frame.py illustration.jpg --title "..." --subtitle "..." --i 1 --n N -o sample_frame.png` (same crop/scale + overlays).

## Frame layout (mandatory)

**All on-screen text in the video is English only** (title, subtitles, page counter). Never put Hebrew or any other language on the frame.

Generated stills and clips (sketches **and** video) contain the **illustration only**:
- **No title, no underline, no caption, no page counter, no letters of any kind.**
- Every image/video prompt must say: `no text, no letters, no captions`.
- Any lettering baked into a still or clip is a **reject** — regenerate it. Text is added afterwards by [`../scripts/video/build.py`](../scripts/video/build.py) (or [`../scripts/video/preview_frame.py`](../scripts/video/preview_frame.py) for the approval sample).

**Drawing size (fill the screen):**
- Make the scene fill nearly the whole **width** of the image. The Xiaohei character must be large and clearly doing the action — not a small vignette centred in the middle.
- `build.py` crops each clip to the drawing's bounding box (pixels darker than 200, plus a 14 px margin) and scales it to fit a **1060×1150** box, centred at about **y=790** and kept between **y=200** and **y=1400** of the 1080×1920 frame. A wide, well-filled drawing therefore ends up filling most of the screen; a small centred drawing stays small.

**Overlay layout on the 1080×1920 canvas** (Patrick Hand, `PatrickHand-Regular.ttf`, env `PATRICK_HAND_TTF`):

| Element | Spec |
|---|---|
| Title | English, **UPPERCASE**, 64 px, colour `(20,20,20)`, centred at `(540,115)` |
| Red underline | from **x=400 to x=680** (280 px ≈ 26% of width), **6 px** thick, at **y=165**, colour `(225,55,40)` |
| Subtitles | English, **62 px** (fallback 56 then 52 only if a line won't fit), max line width **960 px**, max **2 lines**, line spacing **70 px**, first line top at **y=1430**, colour `(12,12,12)`, centred |
| Page counter | `— i / N —`, 32 px, grey `(130,130,130)`, at **y=1835** |

At the 540×960 preview / reference size these are half: title 32 px, underline 140 px long and 3 px thick at y≈82, subtitles 31 px.

**Sample-frame approval:** build the approval sample by compositing the generated illustration with these overlays (`build.py`'s static overlay plus one subtitle chunk), **never** by asking the image generator to draw text. Helper: [`../scripts/video/preview_frame.py`](../scripts/video/preview_frame.py):

```bash
PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf \
  python ../scripts/video/preview_frame.py scenes/scene1.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

