# Krea: MCP connector (primary), browser fallback

> **Scene-by-scene production:** how to build each part from the approved script table (narration ≤8 s, start/end sketches, generate, verify, upscale, RIFE, assemble): [`../scene-by-scene-production.md`](../scene-by-scene-production.md).

**Primary method: the Krea MCP connector** (namespace `user-Krea`, signed in to the user's Krea workspace). It submits jobs to the Krea public API with typed inputs and returns a job id and the result URL. Fallback: the web UI at https://www.krea.ai/video in the box's Chrome.

The model facts below were read with `list_models(category="video")` and `get_model_schema` on 2026-11-09, with no credits spent.


> ## 🖼️ Step 0: per-part start/end sketches (ACCORDING TO the reference images), then spend video credits
> Start-to-end-frame models need **one matched pair per part**, not a pile of unrelated stills. **Never** generate independent stills of every frame, or unrelated images per beat — those do not work as start→end video inputs.
>
> Split the story into **parts (scenes) 1..N** (e.g. part 1 / 4 / 9). Keep parts short enough for the chosen model's duration (and **≤ 8 s** if the same part plan may also be used on Flow/Veo). For **each** part make **exactly one** matched pair:
>
> | File | Role |
> |---|---|
> | `scenes/partN_start.jpg` | Start frame of part N |
> | `scenes/partN_end.jpg` | End frame of part N (result of one continuous one-way motion from the start) |
> | `prompts/partN.txt` | Transition prompt for part N (motion only: start → end) |
>
> ### Per part (before any video credits)
> 1. **Pick 2–3 relevant reference images** from [`../../reference-images/`](../../reference-images/) (38 vertical 9:16 frames from 13 Shorts). Note them by relative path in the part notes. Prefer refs whose action, props or composition match the beat.
> 2. **Generate `partN_start.jpg`** with free image generation only (`GenerateImage` or another free tool), passing those 2–3 refs as style references / describing their style. Match: pure white background, thin wobbly black lines, black Xiaohei doing the action, character size and composition, minimal colour accents **as in the chosen references**. **Vertical 9:16 only** (e.g. 1080×1920) — **never 16:9**. Illustration only: `no text, no letters, no captions`. Large Xiaohei filling most of the frame width (not a small centred vignette).
> 3. **Generate `partN_end.jpg` FROM `partN_start.jpg`** (image-to-image / edit, using the start frame as the reference image). Same scene: same background, camera, framing, scale, Xiaohei and objects. Differs **only** in the action's progress. Do **not** invent a new composition.
> 4. **Write / rewrite `prompts/partN.txt` from the actual sketches** — look at start+end, list what they show, write motion + **timed beats** matching those images (not only the script idea). One-way, locked camera, no zoom/pan/loop, keep style, no text. If a sketch is regenerated, rewrite the prompt. See § Transition prompt below and [`../scene-by-scene-production.md`](../scene-by-scene-production.md) §1b.
> 5. **Check the pair** side by side with the chosen references and the scene table (part → sentence numbers, see [images-and-animation](../images-and-animation.md)). Regenerate any style drift or mismatched pair — fix now, while it's free.
>
> ### Models with start frame only (Seedance 1.0 Pro Fast, LTX-2 19B, …)
> Upload **`partN_start.jpg`** plus the transition prompt from `prompts/partN.txt`. Keep **`partN_end.jpg`** as the **target for checking** the finished clip (does the last frame match the intended end pose?). Do not skip making the end sketch.
>
> ### Models with start + end (MiniMax H3 Max, Seedance 1.0 Pro, …)
> Upload **`partN_start.jpg`** + **`partN_end.jpg`** + the transition prompt.
>
> ### Transition prompt from the actual sketches (mandatory) + timed beats
> Write (or rewrite) `prompts/partN.txt` **after** `partN_start.jpg` and `partN_end.jpg` exist. Look at both images; list character pose/position, props, objects, background, accent colour; describe **exactly** the motion from start → end with those same elements in those same positions. Do not invent or contradict the images. Include a **timed beat breakdown** (8 s: 0–1 / 1–3 / 3–5 / 5–7 / 7–8; 6 s: 0–1 / 1–2.5 / 2.5–4 / 4–5.5 / 5.5–6; 4 s: 0–0.5 / 0.5–1.5 / 1.5–2.5 / 2.5–3.5 / 3.5–4). First beat = exact start state; last beat = settles on exact end state. If a sketch is regenerated, rewrite the prompt. Full checklist + good/bad examples: [`../scene-by-scene-production.md`](../scene-by-scene-production.md) §1b.
>
> ### Transition prompt template (`prompts/partN.txt`)
> ```
> Slow continuous one-direction motion matching the actual start and end sketches.
>
> Timed beats (<D> s total):
> - 0–… s: exact start-image state — <pose, props, objects, background, accent as in partN_start.jpg>
> - …–… s: <what moves, where, which direction>
> - …
> - …–<D> s: settles exactly on the end-image state — <as in partN_end.jpg>
>
> Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects in the same positions as the sketches. no text, no letters, no captions.
> ```
>
> ### Worked timed example — Emu War part 1 (8 s)
> After sketches show: soldier left-of-centre, Lewis gun low at side, fence left, wheat right, tiny red on cooling rings → same shot, step forward, gun at waist aimed right.
> ```
> Slow continuous one-direction motion matching the actual start and end sketches.
>
> Timed beats (8 s total):
> - 0–1 s: exact start-image state — soldier left-of-centre facing right, Lewis gun low at his side, fence left, wheat right, tiny red on gun cooling rings
> - 1–3 s: soldier begins one step forward; gun starts rising
> - 3–5 s: step completes; gun rises to hip height aimed right
> - 5–7 s: gun reaches waist height aimed right; body settles
> - 7–8 s: settles exactly on the end-image state — one pace forward, gun at waist aimed right, same fence/wheat/red accent
>
> Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same fence, wheat, gun and character. no text, no letters, no captions.
> ```
>
> ### Prompt-check (before Generate)
> Looked at both sketches · same elements/positions · nothing invented/contradicted · one-way locked camera · timed beats present and consistent · first=start / last=end · rewritten if a sketch changed.
>
> ### Approval, then produce part by part
> 0. **Before any sketches:** present the full **part-by-part script table** with up-front `This script = N parts / N clips, ~T s` (and Flow-equivalent credit note if relevant). Part count = clip count = start+end pairs. Columns: part #, narration, words, est. s ≤8, start/end ideas. Proposed total ~50 s – ~1.5 min (~7–11 parts). Wait for approval. Narration written to fit ≤8 s/part; never stretch audio.
> 1. Show the user **part 1** as the sample: `part1_start.jpg` + `part1_end.jpg` + `prompts/part1.txt` (and a composited approval sample via [`../../scripts/video/preview_frame.py`](../../scripts/video/preview_frame.py) from the start frame). Wait for explicit approval ([script-writing § Approval gate](../script-writing.md#approval-gate-mandatory)).
> 2. After approval, for each part **in order** (1, then 2, then 3…): check the pair → generate that part's clip (start [+ end if supported] + prompt) → self-verify → **QA סרטונים watches** the clip → only then move to the next part. If the model outputs **≥720p**, treat like Flow (QA at native res, **no** Real-ESRGAN). If max output is **below 720p**, treat like Grok (QA → upscale → sharpness QA).
> 3. Spend video credits **only** on approved parts, one clip per part. Use `preflight: true` for any cost question.


> ## ⚠️ Aspect ratio 9:16 is mandatory
> Always request a **vertical** frame. Landscape slips through when size/aspect is left to a default.
> - Always pass **`aspect_ratio: "9:16"` explicitly** on every Krea `generate_video` call (several models default to 16:9). Never rely on defaults.
> - For sketches made with the built-in `GenerateImage` or any other tool, request **9:16 / 1080×1920** explicitly.
> - Manual web UI: pick **9:16** in the composer **before** generating and confirm it shows 9:16.
> - After generating, verify every still/clip with `ffprobe` or PIL that **height > width** (e.g. 1080×1920 or 720×1280). Reject and regenerate anything landscape before going on.

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

> ## ⚠️ If MCP doesn't work → offer the browser as a choice
> If the Krea MCP connector fails, **don't switch on your own.** Failures include: a connector error, an auth or sign-in failure (HTTP 401), a tool missing from the `user-Krea` namespace, or the same error repeating after one retry (`provider_error`, `internal`, `timeout`).
> - **Ask the user to choose:** fix or retry MCP, or switch to **manual browser operation** at krea.ai/video in the box's Chrome (the steps in [§6 Fallback](#6-fallback-web-ui-in-box-chrome)).
> - Go to the browser **only after the user picks it**.
> - **A credit shortage isn't an MCP failure.** On HTTP 402 / `insufficient_balance`, stop and tell the user. Don't buy credits, don't open plan or pack offers, and don't switch routes or models to get around it.

## 1. Tools
| Tool | Spends? | Use |
|---|---|---|
| `list_models(category)` | no | `category: "video"` lists the video model ids |
| `get_model_schema(model)` | no | Exact input fields, enums and defaults for a model. Re-check it before a run, because schemas change. |
| `get_balance()` | no | The workspace plan and remaining compute units (credits) |
| `get_upload_url()` | no | A presigned upload URL valid for 3 h. Upload with `curl -X POST "$UPLOAD_URL" -F "file=@/workspace/<story>/scenes/partN_start.jpg"`; the response body has the asset URL. One URL can take many files, one POST each. |
| `generate_video(model, input, sync, timeoutSeconds, preflight)` | **yes**, unless `preflight: true` | Submits the job. `preflight: true` returns a cost quote and the available balance, and nothing is queued or charged. |
| `get_job(jobId)` | no | Job status and result. Statuses: backlogged / queued / scheduled / processing / sampling / intermediate-complete / completed / failed / cancelled. |
| `cancel_job(jobId)` | no | Cancels or deletes a job that isn't finished |

Image inputs (`start_image`, `end_image`, `reference_images`) accept an **external URL, a base64 data URI, or an uploaded asset URL**. For local stills, use `get_upload_url`; a data URI also works for small files.

## 2. Models for this style
| Model (id) | Start | End | Refs | Aspect | Resolution | Duration | Est. cost* |
|---|---|---|---|---|---|---|---|
| MiniMax H3 Max (`minimax/h3-max`) | yes | yes | `reference_images` up to 9 (use Xiaohei style refs) | incl. 9:16 (default 16:9) | 480p / 768p / 1080p (default 768p) | 5–15 s, integer | ~130 credits at 480p, 5 s |
| LTX-2 19B (`lightricks/ltx-video-2-19b`) | yes | **no** | – | 16:9 / 9:16 | 512p / 768p | 5 / 8 / 10 s | ~34 credits at 512p, 5 s |
| Seedance 1.0 Pro (`bytedance/seedance-1.0-pro`) | yes | yes | `reference_images` up to 4 | incl. 9:16 | **720p / 1080p only** via the API | flexible number | the user's ~31 credits at 480p, 4 s estimate likely **doesn't apply** (no 480p in the API) |
| Seedance 1.0 Pro Fast (`bytedance/seedance-1.0-pro-fast`) | yes | **no** | – | incl. 9:16 (default 16:9) | 480p / 720p / 1080p (default 720p) | 2–12 s | unknown, so use preflight |

\* **Estimates only; may be outdated.** The exact per-call cost isn't known until a `preflight` quote or the actual submission. API billing may differ from the credits shown in the web app.

Notes:
- LTX-2 has `generate_audio: true` by default. Always set it to **`false`**, because we add our own narration.
- Always pass `aspect_ratio: "9:16"` explicitly, since several models default to 16:9. Verify the result is vertical (height > width) before keeping it.
- **Clip length is chosen per part**, by what looks right for the narration slot. RIFE retimes it to the exact slot afterwards.
- Other video models in the list include Kling, Seedance 2/2.5, Veo 3.1, Hailuo, Runway, Luma and Grok Imagine. Check their schema before trying one.

## 3. Workflow for one part
1. `get_balance()`, and stop if it's too low.
2. Run `get_model_schema` for the chosen model to confirm the fields.
3. Upload `scenes/partN_start.jpg` (and `scenes/partN_end.jpg` when the model supports an end frame, plus a few `reference-images/` JPGs for H3 Max) with `get_upload_url` + curl, and note the asset URLs.
4. Run `generate_video` with `preflight: true` and the full input (prompt = contents of `prompts/partN.txt`), then read the quote. Only proceed for an approved part.
5. Run `generate_video` with the same input (async; `sync: false` is the default) and get the `job_id`.
6. Poll `get_job(jobId)` until it shows `completed`, or `failed` (then read `error.code`).
7. Download the result URL with `curl -L -o /workspace/<story>/gen/partN.mp4 "<result url>"`. For start-only models, check the last frame against `partN_end.jpg`.
8. Verify the clip, then move to the next part. After all parts: RIFE + `build.py` (see [README](README.md)).

Example: a 9:16 Xiaohei part with start and end frames (MiniMax H3 Max):
```json
{
  "model": "minimax/h3-max",
  "input": {
    "prompt": "<contents of prompts/partN.txt>",
    "start_image": "<asset URL of scenes/partN_start.jpg>",
    "end_image": "<asset URL of scenes/partN_end.jpg>",
    "reference_images": ["<asset URL of a reference-images/*.jpg>", "<another>"],
    "aspect_ratio": "9:16",
    "resolution": "480p",
    "duration": 5,
    "seed": 7
  },
  "preflight": true
}
```
Set `preflight` to `false` (or remove it) only for the real, approved run.

The LTX-2 variant: `"model": "lightricks/ltx-video-2-19b"`, with no `end_image` or `reference_images`, `"resolution": "512p"`, `"duration": 5`, `"generate_audio": false`.

## 4. Errors
| Signal | Meaning | Action |
|---|---|---|
| HTTP 402 / `error.code: insufficient_balance` | Out of credits | **Stop and tell the user.** Don't buy, don't open plan/pack offers, and don't switch to a cheaper model on your own. |
| HTTP 429 | Too many concurrent jobs | Wait for a running job to finish, then submit again |
| `validation_failed` / `invalid_request` (with `param`) | Bad value or unreadable file | Fix the named parameter and resubmit |
| `content_policy`, `model_unavailable`, `timeout`, `provider_error`, `internal` | – | Try once more at most, then report |

## 5. Rules
- **Never buy credits, plans or compute packs.** If the connector suggests showing plans after an out-of-credits error, don't. Just report it to the user.
- Generate only approved parts. Use `preflight` for any cost question.
- Same rules after generation as every option: one-direction motion, no loop/zoom/pan, **QA watches each part** ([`../qa.md`](../qa.md)), RIFE to 24 fps, 1080x1920 layout, **full-video QA** before delivery. Sub-720p → Real-ESRGAN after part QA; ≥720p → no upscale.

## 6. Fallback: web UI in box Chrome
Use this when the connector is unavailable or a model is only in the web app. Labels may change.
1. Open https://www.krea.ai/video and check the balance.
2. Pick the model. Upload `partN_start.jpg`, plus `partN_end.jpg` if the model supports an end frame.
3. Set **9:16**, resolution and duration, and turn audio off. Confirm the UI shows 9:16 before Generate.
4. Paste the transition prompt from `prompts/partN.txt`. Generate one clip for this part.
5. Download it; it lands in `/home/box/Downloads/`. Move it to `/workspace/<story>/gen/partN.mp4`. Verify height > width with `ffprobe` / PIL; reject landscape. Then move to the next part.
