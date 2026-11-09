# Hugging Face Spaces — browser workflow

> **Scene-by-scene production:** how to build each part from the approved script table (narration ≤8 s, start/end sketches, generate, verify, upscale, RIFE, assemble): [`../scene-by-scene-production.md`](../scene-by-scene-production.md).

**Primary method: the Space page in the box's Chrome** (signed-in Hugging Face session, for ZeroGPU quota), operated by the bot's browser/desktop agent.

## Spaces
- **Image-to-video:** Wan 2.2 14B I2V + Lightning LoRA, https://huggingface.co/spaces/JCisHERE/wan2-2-i2v-v3
  - Inputs: input image, optional **last image**, prompt, negative prompt, duration (default 3.5 s), steps (default 6), seed / randomize, quality, scheduler, flow shift, frame multiplier, safe mode.
  - Output: 24 fps, dimensions rounded to multiples of 32. The page also has a frame-extract tool, useful for taking the last frame to chain a second clip.
- **Stills (optional):** Z-Image-Turbo, https://huggingface.co/spaces/mcp-tools/Z-Image-Turbo. It offers resolutions including 1152x864 (4:3) and 720x1280 / 1152x2048 (9:16). Xiaohei stills normally come from GenerateImage with the repo references.

## Step 0: per-part start/end sketches (ACCORDING TO the reference images)

Wan 2.2 I2V accepts an input image and an optional **last image**. Work **per part**, not with a pile of unrelated stills. **Never** generate independent stills of every frame, or unrelated images per beat.

Split the story into **parts (scenes) 1..N**. For **each** part make **exactly one** matched pair:

| File | Role |
|---|---|
| `scenes/partN_start.jpg` | Start / input image of part N |
| `scenes/partN_end.jpg` | Last image of part N (optional upload; always make it as the motion target) |
| `prompts/partN.txt` | Transition prompt for part N (motion only: start → end) |

### Per part
1. Pick 2–3 relevant refs from [`../../reference-images/`](../../reference-images/); generate `partN_start.jpg` with free `GenerateImage` (9:16, illustration only, large Xiaohei, style matched to refs).
2. Generate `partN_end.jpg` **FROM** `partN_start.jpg` (image-to-image / edit). Same background, camera, framing, scale, Xiaohei and objects; only the action's progress changes.
3. **Write / rewrite `prompts/partN.txt` from the actual sketches** (look at both images; motion + **timed beats**; same elements/positions; no invented cast). If a sketch is regenerated, rewrite the prompt. Full rule: [`../scene-by-scene-production.md`](../scene-by-scene-production.md) §1b.
4. Check the pair against the refs and the scene table; regenerate drift; re-run the prompt-check checklist before generate.

### Transition prompt from actual sketches (mandatory) + timed beats
Write the prompt **after** the sketches exist. Include timed beats (8 s: 0–1 / 1–3 / 3–5 / 5–7 / 7–8; 6 s: 0–1 / 1–2.5 / 2.5–4 / 4–5.5 / 5.5–6; 4 s: 0–0.5 / 0.5–1.5 / 1.5–2.5 / 2.5–3.5 / 3.5–4). First beat = exact start state; last = settles on end. QA compares clip timing to the beats.

### Transition prompt template
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (<D> s total):
- 0–… s: exact start-image state — <pose, props, objects, background, accent as in partN_start.jpg>
- …–… s: <what moves, where, which direction>
- …
- …–<D> s: settles exactly on the end-image state — <as in partN_end.jpg>

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects in the same positions as the sketches. no text, no letters, no captions.
```

### Worked timed example — Emu War part 1 (8 s)
After sketches show soldier left-of-centre, Lewis gun low, fence left, wheat right → step forward, gun at waist aimed right:
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (8 s total):
- 0–1 s: exact start-image state — soldier left-of-centre facing right, Lewis gun low at his side, fence left, wheat right, tiny red on gun cooling rings
- 1–3 s: soldier begins one step forward; gun starts rising
- 3–5 s: step completes; gun rises to hip height aimed right
- 5–7 s: gun reaches waist height aimed right; body settles
- 7–8 s: settles exactly on the end-image state — one pace forward, gun at waist aimed right, same fence/wheat/red accent

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same fence, wheat, gun and character. no text, no letters, no captions.
```

### Approval, then produce part by part
Show **part 1** (start + end + prompt) for approval. After approval: per part in order — check the pair → upload start (+ last image) + prompt → generate → self-verify → **QA סרטונים watches** the clip → if output is below 720p, upscale after QA pass (same as Grok; see [`../upscale-real-esrgan.md`](../upscale-real-esrgan.md)) → next part. HF is usually sub-720p, so expect the **480p-style test + upscale** path, not Flow's direct 720p.

## Steps (labels may change)
1. Open the Space page in box Chrome (signed in) and wait until it shows "Running".
2. Upload `scenes/partN_start.jpg`, and `scenes/partN_end.jpg` as the last image.
3. Paste the transition prompt from `prompts/partN.txt` (written from the actual sketches with timed beats; one-direction motion, locked static camera, no zoom, no pan, no text, no letters, no captions). Start stills must be illustration-only with large Xiaohei filling most of the width. Keep the default negative prompt (it already discourages static frames and subtitles).
4. Set the duration to fit the part slot (short clips are fine, since RIFE retimes them). Leave steps at 6.
5. Generate. If it's queued or the quota is exceeded, wait or stop; don't pay for compute.
6. **Download** the MP4 to `/home/box/Downloads/`, then move it to `/workspace/<story>/gen/partN.mp4`. Check the last frame against `partN_end.jpg`.
7. Send to **QA סרטונים** (watches the part). On pass: if below 720p, Real-ESRGAN upscale + sharpness QA; then RIFE. Then move to the next part.
8. After all parts: RIFE (if not done) + `build.py` layout → **full-video QA** before delivery.

## Limits and cost
- Free-ish: runs on ZeroGPU with a per-account daily GPU quota. Long or high-step runs use more quota.
- Queues can be long, and community Spaces can change or go offline.
- Never buy a PRO plan or paid hardware unless the user explicitly asks.

## Secondary note
The same Space tools are reachable through the Hugging Face MCP connector (`gr2_wan2_2_i2v_v3_generate_video`, `gr2_wan2_2_i2v_v3_extract_frame`, `gr1_z_image_turbo_generate`). Use it only if the user asks; the browser is the method.

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
  python ../../scripts/video/preview_frame.py scenes/part1_start.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

