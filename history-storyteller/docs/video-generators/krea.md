# Krea: MCP connector (primary), browser fallback

**Primary method: the Krea MCP connector** (namespace `user-Krea`, signed in to the user's Krea workspace). It submits jobs to the Krea public API with typed inputs and returns a job id and the result URL. Fallback: the web UI at https://www.krea.ai/video in the box's Chrome.

The model facts below were read with `list_models(category="video")` and `get_model_schema` on 2026-11-09, with no credits spent.


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
| `get_upload_url()` | no | A presigned upload URL valid for 3 h. Upload with `curl -X POST "$UPLOAD_URL" -F "file=@/workspace/<story>/scenes/sceneN.jpg"`; the response body has the asset URL. One URL can take many files, one POST each. |
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
- Always pass `aspect_ratio: "9:16"` explicitly, since several models default to 16:9.
- **Clip length is chosen per scene**, by what looks right for the narration slot. RIFE retimes it to the exact slot afterwards.
- Other video models in the list include Kling, Seedance 2/2.5, Veo 3.1, Hailuo, Runway, Luma and Grok Imagine. Check their schema before trying one.

## 3. Workflow for one scene
1. `get_balance()`, and stop if it's too low.
2. Run `get_model_schema` for the chosen model to confirm the fields.
3. Upload `scenes/sceneN.jpg` (and the end frame, plus a few `reference-images/` JPGs for H3 Max) with `get_upload_url` + curl, and note the asset URLs.
4. Run `generate_video` with `preflight: true` and the full input, then read the quote. Only proceed for an approved scene.
5. Run `generate_video` with the same input (async; `sync: false` is the default) and get the `job_id`.
6. Poll `get_job(jobId)` until it shows `completed`, or `failed` (then read `error.code`).
7. Download the result URL with `curl -L -o /workspace/<story>/gen/sN.mp4 "<result url>"`.
8. Post-process with RIFE + `build.py` (see [README](README.md)).

Example: a 9:16 Xiaohei scene with start and end frames (MiniMax H3 Max):
```json
{
  "model": "minimax/h3-max",
  "input": {
    "prompt": "Hand-drawn Ian Xiaohei style ink illustration comes alive: <slow one-direction action for the scene>. Static locked camera, no zoom, no pan, no camera movement, no text, no new characters.",
    "start_image": "<asset URL of scenes/sceneN.jpg>",
    "end_image": "<asset URL of scenes/sceneN_end.jpg>",
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
- Generate only approved scenes. Use `preflight` for any cost question.
- Same rules after generation as every option: one-direction motion, no loop/zoom/pan, RIFE to 24 fps, 1080x1920 layout, QA.

## 6. Fallback: web UI in box Chrome
Use this when the connector is unavailable or a model is only in the web app. Labels may change.
1. Open https://www.krea.ai/video and check the balance.
2. Pick the model. Upload the start image, plus the end image if the model supports it.
3. Set 9:16, resolution and duration, and turn audio off.
4. Use the same prompt pattern. Generate one clip.
5. Download it; it lands in `/home/box/Downloads/`. Move it to `/workspace/<story>/gen/sN.mp4`.
