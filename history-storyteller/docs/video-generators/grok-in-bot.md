# Default method (in-bot Grok) — backup for reproducing outside the bot

> **Purpose:** write down **exactly** how this Grok Bot makes history Shorts **here** with built-in Grok tools, so you can search for other ways to do the same outside the bot.  
> **Related how-tos:** [grok-imagine.md](grok-imagine.md) · [scene-by-scene-production.md](../scene-by-scene-production.md) · [qa.md](../qa.md) · [narration.md](../narration.md) · [subtitles-and-build.md](../subtitles-and-build.md) · [upscale-real-esrgan.md](../upscale-real-esrgan.md) · [video-generators README](README.md)

This page is the **user’s default for history Shorts** in this bot: **built-in Grok only** (`GenerateImage` + `GenerateVideo`). No Google Flow, no Krea, no HF Spaces for the normal path (those remain documented alternatives below).

---

## 1) Default method (in-bot Grok)

### Tools (verified from the bot’s tool schemas)

| Step | Tool | Key inputs we use |
|---|---|---|
| Start sketch | `GenerateImage` | `description`, `aspect_ratio: "9:16"`, `reference_image_paths` (2–3 refs from [`../../reference-images/`](../../reference-images/)) |
| End sketch | `GenerateImage` again | Edit/image-to-image from the **start** still (start path in `reference_image_paths`); same scene, only action progress changes |
| Clip A / Clip B | `GenerateVideo` | **Image-to-video:** `image_path` = start frame (or A’s last frame for B). `duration` ≈ **4**. `resolution: "480p"`. Prompt = timed beats for that half. Always: locked camera, no zoom/pan, `no text, no letters, no captions` |

**`GenerateVideo` tool limits (schema):** `duration` **1–15** s (tool default **6** if omitted); `resolution` **`480p` | `720p` | `1080p`** (default **`480p`**); `aspect_ratio` enum includes **`9:16`** (for **image-to-video**, aspect follows the source image — `aspect_ratio` is ignored when `image_path` is set, same as the public API). Optional `last_frame_path`, `keyframes` (≤4), `reference_image_paths` (≤14) exist on the tool but **this history workflow does not use them for the per-part chain** (see below).

### Per-part visual pipeline (what we actually do)

1. **Script table approved** (parts ≤8 s narration each; ~50 s – ~1.5 min total). See [script-writing](../script-writing.md) / [scene-by-scene](../scene-by-scene-production.md).
2. **`scenes/partN_start.jpg`** — Ian Xiaohei style from **2–3** reference images; **vertical 9:16**; **illustration only** (prompt includes `no text, no letters, no captions`); large character filling most of the width. Verify **height > width**.
3. **`scenes/partN_end.jpg`** — generated **from** the start still (edit). Same background / camera / framing / scale / objects; only the one-way action progresses.
4. **`prompts/partN.txt`** — written **after** both sketches exist, from what the images **actually show**, with a **timed beat breakdown** across the ~8 s part (split across A then B). Full rule + Emu War example: [scene-by-scene §1b](../scene-by-scene-production.md). Reason: timed beats + image-matched prompt leave the generator nothing to guess → fewer lags/glitches.
5. **Clip A (~4 s, 480p):** `image_path = partN_start.jpg`, prompt = first half of beats (≈0–4 s), toward the end state.
6. **Extract A’s last frame** → `gen/partN_a_last.jpg` (`scripts/video/chain_and_upscale.sh extract-last`).
7. **Clip B (~4 s, 480p):** `image_path = partN_a_last.jpg`, prompt = second half of beats (≈4–8 s), continuing one-way to the end state.
8. **`partN_end.jpg` is the check target only** — compare B’s last frame to it. **Do not** animate start and end as two unrelated clips (hard jump at 4 s). **Do not** feed the end sketch as a second independent i2v start in this workflow.
9. **Join A+B** → `gen/partN.mp4` (`chain_and_upscale.sh join`).
10. **QA stage 1** — QA סרטונים **watches** the 480p join vs `prompts/partN.txt` (seam, one-way, no loop/zoom, 9:16, no baked text, beats timing, last ≈ end sketch). See [qa.md](../qa.md).
11. **Upscale** approved join to **720×1280** with Real-ESRGAN model `realesr-animevideov3` (`scripts/video/upscale_720p.sh` or `chain_and_upscale.sh upscale`). **Do not regenerate at 720p** if upscale is fine (new gen = different motion). Guide: [upscale-real-esrgan.md](../upscale-real-esrgan.md).
12. **QA stage 2** — sharpness check on the upscaled clip.
13. **RIFE** to true **24 fps** continuous motion (`scripts/video/rife_eq.py`); jolt fixes as needed. Never interpolate across a hard cut.
14. After all parts: **Chatterbox** narration ([narration.md](../narration.md)), **`build.py` overlays** (title / red underline / English subtitles / counter — [subtitles-and-build.md](../subtitles-and-build.md)), then **QA stage 3** on the full assembled **1080×1920** Short.

### Settings summary (verified vs to verify)

| Item | Value | Source |
|---|---|---|
| Aspect for sketches | **`9:16`** explicit on `GenerateImage`; reject if width ≥ height | Skill + scene-by-scene |
| Style | Ian Xiaohei; 2–3 refs from `reference-images/`; name “Xiaohei” **only** in prompts, never in story/metadata | Skill + hard rules |
| Illustration | No text/letters/captions in stills or clips; overlays only in `build.py` / `preview_frame.py` | Frame layout docs |
| Part length | ≤ **8 s** narration (~18–20 English words); two×~**4 s** video clips chained | grok-imagine.md + scene-by-scene |
| Tool duration range | **1–15 s** | `GenerateVideo` schema |
| Test resolution | **`480p`** first | Approved workflow |
| Upscale target | **720×1280** Real-ESRGAN `realesr-animevideov3` | `upscale_720p.sh` |
| Final canvas | **1080×1920**, **24 fps**, H.264 + AAC | Skill + build.py |
| Camera | Locked static; no zoom / pan / loop / reverse / freeze >0.3 s | Animation rules |
| Narration | Chatterbox, seed **7**, exaggeration **0.6**, cfg **0.45**, loudnorm **I=-16**; no stretch | narration.md |
| Cost (in-bot) | Counts against the **Grok Bot plan**; one ~1-minute video ≈ **8–10%** of plan (**user measurement**) | grok-imagine.md |
| Exact 480p pixel size for 9:16 output | **to verify** on next run (`ffprobe`); older Garbo landscape clips were ~640×480 @24 fps — that was **not** the current 9:16 part workflow | grok-imagine.md note |
| Whether in-bot `last_frame_path` would replace chaining | Tool supports it; **current approved history path still uses start-only chain + end as check target** | Schema + grok-imagine.md |

### Scripts used after generation

- [`../../scripts/video/chain_and_upscale.sh`](../../scripts/video/chain_and_upscale.sh) — `extract-last`, `join`, `upscale`, `all`
- [`../../scripts/video/upscale_720p.sh`](../../scripts/video/upscale_720p.sh) — standalone Real-ESRGAN → 720×1280
- [`../../scripts/video/rife_eq.py`](../../scripts/video/rife_eq.py), `jolt_fix.py`, `fix_frames.py`
- [`../../scripts/video/build.py`](../../scripts/video/build.py), `preview_frame.py`, `sentence_timing.py`
- [`../../scripts/voice/`](../../scripts/voice/) — Chatterbox paragraph pipeline
- [`../../scripts/qa/`](../../scripts/qa/) — self-checks before QA bot

---

## 2) Alternative ways to reproduce outside the bot

Goal: same pipeline shape (script table → start/end sketches → prompt from images → i2v → QA → upscale if needed → RIFE → Chatterbox + `build.py` → full QA). Only the **image/video engine** changes.

### A) grok.com / Grok app — Imagine (web or mobile)

| | |
|---|---|
| **Links** | [grok.com](https://grok.com) · [x.ai/pricing](https://x.ai/pricing) (consumer plans) · Imagine product overview often via [x.ai/api/imagine](https://x.ai/api/imagine) |
| **How to use with this pipeline** | Generate/edit **9:16** stills in Imagine (start, then edit toward end). Animate with **image-to-video** from the start (and chain a second clip from the first clip’s last frame if the UI does not pin an end frame). Keep prompts = timed beats from the actual sketches. Download MP4s → same QA / Real-ESRGAN / RIFE / `build.py` path as in-bot. |
| **Clip length / res / aspect** | **to verify** in the current UI for exact max duration and resolution pickers. Public API (same models family) documents **1–15 s**, **480p / 720p / 1080p**, i2v aspect **matches the input image**. Super plan marketing on [x.ai/pricing](https://x.ai/pricing) mentions **1080p, 15 s** videos. |
| **Cost / free tier** | Per [x.ai/pricing](https://x.ai/pricing) (checked 2026-11-09): **Free** = limited AI usage; **Plus** ($8/mo) includes Imagine in a shared weekly usage pool; **Premium** ($30/mo) highlights AI images & videos; **Super** ($100/mo) = larger pool + **1080p / 15 s**. Exact per-video quotas are **not published as fixed daily counts** — check in-app Usage. **to verify** whether Free includes any video. |
| **vs in-bot Grok** | Same model family, manual UI, no bot automation / no automatic chain helpers. You must download files and run local scripts yourself. |

### B) xAI API — image + video generation

| | |
|---|---|
| **Official docs** | [Imagine overview](https://docs.x.ai/developers/model-capabilities/imagine) · [Image generation](https://docs.x.ai/developers/model-capabilities/images/generation) · [Image editing](https://docs.x.ai/developers/model-capabilities/images/editing) · [Video overview](https://docs.x.ai/developers/model-capabilities/video/overview) · [Image-to-video](https://docs.x.ai/developers/model-capabilities/video/image-to-video) · [Video generation config](https://docs.x.ai/developers/model-capabilities/video/generation) · REST: [`/v1/images/generations`](https://docs.x.ai/developers/rest-api-reference/inference/images), [`/v1/videos/generations`](https://docs.x.ai/developers/rest-api-reference/inference/videos) · Landing: [x.ai/api/imagine](https://x.ai/api/imagine) · [API pricing](https://docs.x.ai/developers/pricing) |
| **How to use with this pipeline** | **Images:** `POST /v1/images/generations` with `aspect_ratio: "9:16"` (models e.g. `grok-imagine-image-2.0`; resolution `1k`/`2k`). **End sketch:** image **edit** endpoint with the start image as source (docs: up to several reference images). **Video:** async `POST /v1/videos/generations` + poll `GET /v1/videos/{request_id}`; pass still as `image` for i2v. Closest to in-bot chain: two ~4 s i2v calls (B from A’s last frame). On **`grok-imagine-video-1.5`**, official docs also support pinning **`last_frame`** (and keyframes) — that can replace chaining if you want start+end in one request (**to verify** quality vs our chain for Xiaohei ink). |
| **Clip length / res / aspect** | Duration **1–15 s** (default often **8** in docs). Resolutions **480p / 720p / 1080p** (model-dependent; lite reaches 1080p by upscaling 720p per docs). Aspect ratios include **9:16**; **i2v always matches the input image** (`aspect_ratio` ignored). |
| **Cost (official API, 2026-11-09)** | From [docs.x.ai/developers/pricing](https://docs.x.ai/developers/pricing) + [video overview](https://docs.x.ai/developers/model-capabilities/video/overview): images **$0.02–$0.04 / image** by model; video per second e.g. **`grok-imagine-video-1.5`**: 480p **$0.08**, 720p **$0.14**, 1080p **$0.25**; **`1.5-lite`**: 480p **$0.02**, 720p **$0.03**, 1080p **$0.14**; base `grok-imagine-video` listed **$0.05 / sec** on the pricing table (resolution rows on the model page). Re-check pricing before budgeting. |
| **vs in-bot Grok** | Programmable, billed per image/second (not bot-plan %). Can request 720p/1080p API-side (then you may skip Real-ESRGAN — still run QA). Needs an API key (never commit secrets to this public repo). |

### C) Google Flow / Veo (browser or gflow-cli)

| | |
|---|---|
| **Docs in this repo** | [google-flow.md](google-flow.md) |
| **How to use** | Upload **`partN_start` + `partN_end`**, paste timed `prompts/partN.txt`, Veo **3.1 Lite**, **720p**, **9:16**, duration **4 / 6 / 8** (hard max **8 s** per part). Browser at Flow is primary; **gflow-cli MCP only on browser fault**. |
| **Cost** | ~**10 Flow credits** per Veo Lite clip (account free daily credits — rotate profiles; never buy unless user asks). |
| **vs in-bot Grok** | **Native start+end** in one clip; **720p direct** → **no 480p test, no Real-ESRGAN**. Different account/credits. Not the history-bot default (user chose Grok-in-bot). |

### D) Krea

| | |
|---|---|
| **Docs in this repo** | [krea.md](krea.md) · UI: [krea.ai/video](https://www.krea.ai/video) |
| **How to use** | MCP `generate_video` / browser. Some models take **start+end**; others **start only** (end = check target — same idea as Grok chain). Keep timed prompts from the sketches. |
| **Cost** | Paid credits; quote with MCP `preflight` / `get_balance` before spend. Estimates in [krea.md](krea.md) may go stale. |
| **vs in-bot Grok** | Many model choices; may already be ≥720p (skip upscale) or need the Grok-style upscale path. |

### E) Hugging Face Spaces (Wan 2.2 i2v and similar)

| | |
|---|---|
| **Docs in this repo** | [huggingface.md](huggingface.md) |
| **Example Space** | [Wan 2.2 14B I2V + Lightning LoRA](https://huggingface.co/spaces/JCisHERE/wan2-2-i2v-v3) (inputs: image, optional **last image**, prompt, duration default **~3.5 s**) |
| **Cost** | Free with **ZeroGPU** quota; queues; don’t buy PRO/hardware unless user asks. |
| **vs in-bot Grok** | Often short / sub-720p → treat like Grok (**QA then Real-ESRGAN**). Optional last-image is closer to Flow than to start-only chain. |

### F) Local open-source on a GPU

| Option | Links | Pipeline fit | Notes |
|---|---|---|---|
| **Wan 2.2** | [github.com/Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) (Apache-2.0) · I2V-A14B supports **480p & 720p**; aspect follows input image | Start-frame i2v (+ optional chain from last frame); end sketch as check target | Full A14B is heavy (~**80 GB** VRAM class per official single-GPU note); **TI2V-5B** targets ~**24 GB**. Quantized community builds exist — quality **to verify**. |
| **LTX-Video / LTX-2.x** | [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) (older v0.9.x) · newer **LTX-2.5**: [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2), [docs.ltx.io](https://docs.ltx.io/models/ltx-2-5) | Image conditioning / i2v; resolutions divisible by 32; frame counts `8n+1` | README guidance: best under **~720×1280**, frames below **~257** (~few–10 s depending on fps). GPU **~16–24 GB** class often cited for local use. Exact LTX-2.5 i2v limits **to verify** on current docs. |
| **Similar** | Other open i2v (CogVideoX, HunyuanVideo, etc.) | Same: start (+ optional end/keyframe if supported) → QA → upscale if needed → RIFE → assemble | Always re-read the project README for duration/res before relying on it. |

**Local cost:** electricity + your GPU time (no per-clip SaaS fee). Setup and VRAM are the barriers.

---

## 3) How to switch engines — checklist

### Stays the same (any engine)

- [ ] Part-by-part **script table** + user approval before sketches/clips  
- [ ] Matched **`partN_start` / `partN_end`** (end from start; 9:16; illustration only; 2–3 refs)  
- [ ] **`prompts/partN.txt` written from the actual images** + **timed beats**  
- [ ] One-way motion, locked camera, no loop/zoom, no baked-in text  
- [ ] **QA סרטונים watches** each part (and full video) — nothing delivered without pass  
- [ ] **Chatterbox** narration settings (seed 7 / 0.6 / 0.45 / loudnorm −16)  
- [ ] **`build.py` / `preview_frame.py`** English overlays on 1080×1920  
- [ ] **RIFE → 24 fps**, then full QA  
- [ ] Never buy credits/plans unless the user explicitly asks; no secrets in the repo  

### Changes per engine

| Engine | What changes |
|---|---|
| **In-bot Grok (default)** | Built-in tools only; **2×~4 s @480p** chain; end = check target; Real-ESRGAN → 720×1280; plan usage |
| **grok.com / app** | Manual Imagine UI; download clips; same local post path; subscription pool |
| **xAI API** | Key + `/v1/images/*` + `/v1/videos/generations`; optional native `last_frame` on video-1.5; per-second $ |
| **Google Flow / Veo** | Start **and** end upload; **720p direct**; 4/6/8 s max; **no** Real-ESRGAN; Flow credits |
| **Krea** | Model-specific start-only vs start+end; credit quote first |
| **HF Spaces** | Browser ZeroGPU; often short/sub-720p → upscale path |
| **Local Wan / LTX / …** | Your GPU; install weights; match aspect via input still; verify max frames/res |

When you find a new outside path that works well, append a short note to [`../lessons-learned.md`](../lessons-learned.md) and link it from [README.md](README.md).
