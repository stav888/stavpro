# 3. Images and animation

## Style reference
Repo: https://github.com/helloianneo/ian-xiaohei-illustrations (MIT, Ian). Clone it into `<story>/refs/` and pass example images from `assets/examples/` as `reference_image_paths` to every image generation.
- Pure white background, thin wobbly black hand-drawn lines, lots of white space, tiny red/orange/blue accents only.
- Xiaohei: solid black character, white dot eyes, thin legs, blank face. He **performs** the key action of each scene.
- **Illustration only** in generated images: no title, underline, caption, or letters (`no text, no letters, no captions` in every prompt). Regenerate if any lettering or style drift appears. All on-screen text is English and is added later by `build.py` / `preview_frame.py`.
- Drawing fills nearly the whole width: large Xiaohei clearly doing the action, not a small centred vignette.

## Stills

## Step 0 — per-part start/end sketches according to `reference-images/` (before any video credits)

> End-to-end order of work after the script is approved: [`scene-by-scene-production.md`](scene-by-scene-production.md).

Start-to-end-frame models (Flow/Veo, Krea H3 Max / Seedance Pro, HF Wan last-image) need **one matched pair per part**. **Never** generate independent stills of every frame, or unrelated images per beat — those do not work as start→end video inputs.

Split the story into **parts (scenes) 1..N** (e.g. part 1 / 4 / 9).

**Part length when using Flow:** a Flow/Veo start→end clip is at most **8 seconds** (4 / 6 / 8 s only). Plan every part's narration slot to be **≤ 8 s**. If a beat is longer, split it into two parts; the next part's start frame should match the previous part's end frame for continuity. Choose 4, 6 or 8 s to cover the slot; RIFE retimes afterwards.

For **each** part:

| File | Role |
|---|---|
| `scenes/partN_start.jpg` | Start frame |
| `scenes/partN_end.jpg` | End frame — same scene after one continuous one-way motion; generate **FROM** the start frame (image-to-image / edit) |
| `prompts/partN.txt` | Transition prompt (motion only: start → end) |

1. From [`../reference-images/`](../reference-images/) (38 vertical **9:16** frames from 13 Shorts), pick **2–3 relevant refs per part** and note them by relative path.
2. Generate `partN_start.jpg` with free `GenerateImage`, passing those refs. Match white background, wobbly black lines, black Xiaohei doing the action, character size/composition, minimal colour accents. **Always request 9:16 / 1080×1920 — never 16:9.** Illustration only (`no text, no letters, no captions`); large Xiaohei filling most of the width.
3. Generate `partN_end.jpg` **FROM** `partN_start.jpg`. Same background, camera, framing, scale, Xiaohei and objects; only the action's progress changes.
4. Write `prompts/partN.txt` (what moves, which direction; one-way; locked camera; no zoom/pan/loop; keep style; no text).
5. Check the pair side by side with the chosen refs and the scene table; regenerate any style drift or mismatched pair. Verify height > width.
6. **Before any sketches:** present the part-by-part script table with up-front `This script = N parts / N clips, ~T s. Flow estimate: N × ~10 ≈ C credits (Veo 3.1 Lite).` (narration ≤8 s / ~18–20 words per part; proposed total ~50 s – ~1.5 min, ~7–11 parts). Then **approval sample = part 1** (start + end + prompt). After approval, produce part by part: check pair → generate that part's clip (Flow: upload start + end, paste prompt, Veo 3.1 Lite 9:16, ≤8 s) → verify → next part (2, 3, 4…).
7. Only then spend image-to-video credits. Krea start-only models (Seedance Fast, LTX-2): upload start + prompt; use the end sketch as the check target.

### Transition prompt template
```
Slow continuous one-direction motion: <what moves and in which direction from the start pose to the end pose>. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects. no text, no letters, no captions.
```

### Worked example — part 1 (Lustig / Eiffel Tower)
- `part1_start.jpg`: Xiaohei left of frame looking at the Eiffel Tower.
- `part1_end.jpg` (from start): same shot; Xiaohei closer, arm raised pointing at the tower.
- `prompts/part1.txt`: Xiaohei walks toward the tower and raises his arm to point at the top (locked camera, one-way, no text).

- Tool: Grok Bot `GenerateImage` with [`../reference-images/`](../reference-images/) (and/or Ian Xiaohei examples) as `reference_image_paths`. For Flow/Krea/HF sketches, output **vertical 9:16** (e.g. 1080×1920). Older Grok Imagine Garbo stills were 1152×864 JPG per scene (`scenes/sceneN.jpg`) — that landscape size and the old `sceneN.jpg` naming are **not** the target for new Flow/Krea/HF per-part sketches.
- Map parts to sentences in a scene table (part → sentence numbers). Garbo: 14 parts = 14 sentence rows in `sentences.txt` (one part per sentence). When using Flow, also check each part's audio slot is ≤ 8 s (or split the part).


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
  python ../scripts/video/preview_frame.py scenes/part1_start.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

## Image-to-video
> Options: Grok Imagine is the default. Google Flow (Veo) is worked in the Flow **web UI** in box Chrome (gflow-cli MCP only as fallback on browser fault / no access); Krea runs via the Krea MCP connector (browser fallback); Hugging Face Spaces are run directly in the browser; see [`video-generators/`](video-generators/README.md) for the comparison, **Step 0 (per-part start/end sketches according to reference-images)**, the Flow **≤8 s per part** rule, and the mandatory **9:16** aspect rules.

- Tool: Grok Bot `GenerateVideo` (Grok Imagine) image-to-video, `image_path=scenes/partN_start.jpg`. Result for Garbo: 640x480, 24 fps, ~7 s (`gen/partN.mp4` / legacy `gen/sN.mp4`).
- One take **per part** that covers the whole narration slot. Grok Imagine: duration = ceil(slot), max 15 s. **Flow/Veo: hard max 8 s** (pick 4/6/8); split longer beats into two parts.
- Prompt for slow, continuous, **one-direction** progressive motion, and always state a locked static camera: no zoom, no pan, no push-in.
- Forbidden: loops, ping-pong, reverse, `stream_loop`, freeze/hold >0.3 s, Ken Burns. If a clip is short: regenerate once; never loop it.

## Retime to 24 fps with RIFE (smooth motion the user asked for)
`scripts/video/rife_eq.py <scene numbers>` reads `gen/sN.mp4` and `audio_timing.json`, then writes `anim/sceneN_r.mp4` with exactly slot+3 frames:
- Motion-equalized one-way retime: cumulative frame-difference curve (85%) blended with linear (15%). Positions between source frames are synthesized with RIFE 4.7 (`IFNet(arch_ver="4.7")`, scales `[8,4,2,1]`).
- Never interpolate across a cut, and never between scenes.
- Env: `CFI_RIFE_DIR` (ComfyUI-Frame-Interpolation `vfi_models/rife`), `RIFE47_WEIGHTS` (rife47.pth). See `../requirements/system-deps.md`.

## Fixes
- `jolt_fix.py anim/sceneN_r.mp4 ...`: phase-correlation finds single-frame jolts (shift >0.4 px that returns next frame) and replaces them with RIFE midpoints of the neighbours. Keeps `_prejolt.mp4` backup.
- `fix_frames.py in.mp4 out.mp4 <unused> n1 n2 ...`: replace listed frames with RIFE midpoint of n-1/n+1.
- Late fixes are done by **frame splicing on decoded final frames** (replace only the bad frame range, keep everything else bit-identical) to avoid regressions elsewhere. Small moving details (medals, a dot) were fixed with opaque composites and feathered round masks; a figure mask was built per frame over a clean static background. These were one-off inline scripts, not saved as reusable files.
