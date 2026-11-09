# Grok Imagine (default)

- **What:** the Grok Bot built-in `GenerateVideo` tool (Grok Imagine), image-to-video mode.
- **Input:** `image_path` = the approved still (`scenes/sceneN.jpg`, 1152x864 for Garbo). An optional `last_frame_path` pins the end frame. `duration` is 1–15 s, set to cover the scene slot. `resolution` is 480p by default.
- **Output seen on the box:** 640x480, 24 fps, ~7 s clips (`gen/sN.mp4`, inferred from the Garbo files).
- **Prompt pattern:** describe slow, continuous motion in one direction for the scene's action, and always say "locked static camera, no zoom, no pan, no text, no letters, no captions". Stills must be illustration-only and fill most of the frame width (large Xiaohei).
- **Rules:**
  - One take per scene.
  - If a clip is short, regenerate once; never loop it.
  - Using the same image as both first and last frame makes a loop, so never do that.
- **Then:** RIFE retime to the slot (`../../scripts/video/rife_eq.py`), jolt fixes, and layout with `build.py` into 1080x1920.
- **Cost:** counts against the Grok Bot plan (about 8–10% for a ~1-minute video, measured by the user).

## Frame layout (mandatory)

**All on-screen text in the video is English only** (title, subtitles, page counter). Never put Hebrew or any other language on the frame.

Generated stills and clips (sketches **and** video) contain the **illustration only**:
- **No title, no underline, no caption, no page counter, no letters of any kind.**
- Every image/video prompt must say: `no text, no letters, no captions`.
- Any lettering baked into a still or clip is a **reject** — regenerate it. Text is added afterwards by [`../../scripts/video/build.py`](../../scripts/video/build.py) (or [`../../scripts/video/preview_frame.py`](../../scripts/video/preview_frame.py) for the approval sample).

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

**Sample-frame approval:** build the approval sample by compositing the generated illustration with these overlays (`build.py`'s static overlay plus one subtitle chunk), **never** by asking the image generator to draw text. Helper: [`../../scripts/video/preview_frame.py`](../../scripts/video/preview_frame.py):

```bash
PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf \
  python ../../scripts/video/preview_frame.py scenes/scene1.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```


## Per-part chained workflow (Grok Imagine)

Grok Imagine i2v is used with a **start frame only** for this workflow (do not animate the two sketches as two unrelated clips). Each story part is **≤ 8 s** and is built from **two 4 s clips** chained into one continuous one-way motion.

### Why chain (not two independent clips)
Animating `partN_start.jpg` for 4 s and `partN_end.jpg` for 4 s as separate takes leaves a hard jump at the 4 s seam, because clip A does not end on the end sketch. Always chain:

1. **Clip A (4 s, 480p):** `image_path = scenes/partN_start.jpg`. Prompt: animate toward the `partN_end` state (describe the mid-action progress). Always include `locked static camera, no zoom, no pan, no text, no letters, no captions`. Save as `gen/partN_a.mp4`.
2. **Extract A's last frame:** with ffmpeg (or [`../../scripts/video/chain_and_upscale.sh`](../../scripts/video/chain_and_upscale.sh) `extract-last`), write `gen/partN_a_last.jpg`.
3. **Clip B (4 s, 480p):** `image_path = gen/partN_a_last.jpg`. Prompt: continue the same one-way motion to the end state. Same locked-camera / no-text rules. Save as `gen/partN_b.mp4`.
4. **`partN_end.jpg` is the check target only** — compare the last frame of the joined part against it; do not feed it as a separate i2v start (that causes the 4 s jump).
5. **Join A+B** with no cut/jump into `gen/partN.mp4` (~8 s continuous one-way motion). No loop, no zoom, locked camera.

**Never** animate the two sketches as separate unrelated clips.

### 480p test → local upscale to 720p (do not regenerate)

1. Generate and join the part at **480p** first.
2. **QA** the joined 480p part: continuity at the A→B seam, no glitches, Xiaohei style, vertical **9:16**, illustration only (no baked-in text).
3. After QA passes, **do not** regenerate the same part at 720p — a new generation produces **different motion**, not the same take sharper.
4. Instead **upscale** the approved 480p join locally to **720×1280** with **Real-ESRGAN** (anime/illustration model `realesr-animevideov3`), then RIFE to 24 fps as usual, then a short QA sharpness check.
5. Regenerate at 720p **only** if the upscale looks soft or broken; then run full QA again.

Helper scripts:
- [`../../scripts/video/chain_and_upscale.sh`](../../scripts/video/chain_and_upscale.sh) — `extract-last`, `join`, `upscale`, or `all` (A+B → joined → 720p).
- [`../../scripts/video/upscale_720p.sh`](../../scripts/video/upscale_720p.sh) — **standalone** Real-ESRGAN upscale for **any** clip (Grok / Flow / Krea / HF). Full guide: [`../upscale-real-esrgan.md`](../upscale-real-esrgan.md).

Install notes: [`../../requirements/system-deps.md`](../../requirements/system-deps.md). Real-ESRGAN licence: **BSD-3-Clause** (base-repos table in the root README).
