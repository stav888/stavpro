# Hugging Face Spaces — browser workflow

**Primary method: the Space page in the box's Chrome** (signed-in Hugging Face session, for ZeroGPU quota), operated by the bot's browser/desktop agent.

## Spaces
- **Image-to-video:** Wan 2.2 14B I2V + Lightning LoRA, https://huggingface.co/spaces/JCisHERE/wan2-2-i2v-v3
  - Inputs: input image, optional **last image**, prompt, negative prompt, duration (default 3.5 s), steps (default 6), seed / randomize, quality, scheduler, flow shift, frame multiplier, safe mode.
  - Output: 24 fps, dimensions rounded to multiples of 32. The page also has a frame-extract tool, useful for taking the last frame to chain a second clip.
- **Stills (optional):** Z-Image-Turbo, https://huggingface.co/spaces/mcp-tools/Z-Image-Turbo. It offers resolutions including 1152x864 (4:3) and 720x1280 / 1152x2048 (9:16). Xiaohei stills normally come from GenerateImage with the repo references.

## Steps (labels may change)
1. Open the Space page in box Chrome (signed in) and wait until it shows "Running".
2. Upload the start image (`scenes/sceneN.jpg`), plus a last image if you want a fixed end pose.
3. Prompt: one-direction motion, "locked static camera, no zoom, no pan, no text, no letters, no captions". Start stills must be illustration-only with large Xiaohei filling most of the width. Keep the default negative prompt (it already discourages static frames and subtitles).
4. Set the duration to fit the slot (short clips are fine, since RIFE retimes them). Leave steps at 6.
5. Generate. If it's queued or the quota is exceeded, wait or stop; don't pay for compute.
6. **Download** the MP4 to `/home/box/Downloads/`, then move it to `/workspace/<story>/gen/sN.mp4`.
7. Continue with RIFE + layout.

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
  python ../../scripts/video/preview_frame.py scenes/scene1.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

