---
name: Xiaohei History Shorts
description: >-
  Use this when creating a vertical 9:16 history-story Shorts video in the Ian
  Xiaohei illustration style with English narration and subtitles — the user's
  approved production settings.
---

> **Current option (since Nov 2026):** Chatterbox per-paragraph narration, expanded scripts (trial). (Live copy from the bot's skill store, 2026-11-09. The older option is [`SKILL-legacy-edge-tts.md`](SKILL-legacy-edge-tts.md); see the [comparison](README.md).)

# Xiaohei History Shorts — approved settings (updated 2026-11-09)

Create vertical history Shorts that tell one true story in strict chronological order. Full backup docs and scripts: github.com/stav888/stavpro/tree/master/history-storyteller. **Scene-by-scene how-to** (from the approved part-by-part script): `history-storyteller/docs/scene-by-scene-production.md`.

## Approval flow (mandatory)
- **Before any sketches or clips:** show the user the **part-by-part script table** with an up-front summary line: `This script = N parts / N clips, ~T s. Flow estimate: N × ~10 ≈ C credits (Veo 3.1 Lite).` Columns: part #, narration (English), word count, estimated seconds (≤8), start-frame idea, end-frame idea. Proposed total is ~50 s – ~1.5 min (~7–11 parts). Hebrew chat OK; narration text in the table stays English.
- After the table is approved: show **part 1** sample (`part1_start` + `part1_end` + `prompts/part1.txt` + composited preview) and wait for explicit approval. Approval of the preview does not by itself authorize publishing etc.
- Then produce **part by part**. Narration is written to fit ≤8 s per part (~18–20 words); measure each take; rewrite/split if over — never stretch audio.

## Script style
- Expanded, engaging storytelling (approved Garbo rewrite, 2026-11-07): developed chronological story, concrete details, clear setup and progression, strong ending. Propose a **suitable total length per story between ~50 s and ~1.5 min** (about **7–11 parts** of ≤8 s each). Do **not** force under 60 s unless it suits the story.
- This length band is a TRIAL since 2026-11-09 (starting with Garbo ~81 s). The YouTube SEO bot compares lengths; tell the SEO bot the video ID of every upload in the trial.
- **Never put the name "Xiaohei" in the story** (script, narration, subtitles, on-screen title, YouTube title/description/tags). The black character plays that story's real person/subject. "Xiaohei" is allowed **only** in image/video generation prompts (style descriptions).
- "A true story." ending only when it fits. Sensitive topics: respectful, no gore.

## Style (from github.com/helloianneo/ian-xiaohei-illustrations)
- Pure white background, thin wobbly black hand-drawn lines, lots of white space, only tiny red/orange/blue annotations.
- Xiaohei: solid-black character, white dot eyes, thin legs, blank expression, who PERFORMS the core action in every scene.
- Use `history-storyteller/reference-images/` (38 vertical 9:16 frames from our Shorts) as `reference_image_paths` for every GenerateImage / sketch call; Ian Xiaohei examples may supplement. **Per-part pairs** (`partN_start` / `partN_end` from start via edit). Sketches are **illustration only** — every prompt says `no text, no letters, no captions`; regenerate on any lettering or style drift. Large Xiaohei filling most of the frame width (not a small centred vignette). Sketches and finals are **vertical 9:16** (e.g. 1080×1920 / 540×960), never 16:9. **All on-screen text is English only** and is composited later by `build.py` / `preview_frame.py`.

## Frame layout (mandatory)
- **All on-screen text is English only.** Generated stills/clips = illustration only (`no text, no letters, no captions`); any baked-in lettering is a reject.
- Drawing fills nearly the whole width (large Xiaohei doing the action, not a small centred vignette). `build.py` bbox-crops (darker than 200 + 14 px) and scales into 1060×1150, centred ~y=790, clamped y=200–1400.
- Overlays on 1080×1920 (Patrick Hand): title UPPERCASE 64 px `(20,20,20)` at (540,115); red underline x=400–680 / 6 px at y=165 `(225,55,40)`; subtitles 62→56→52 px at y=1430 `(12,12,12)`, max 2 lines / 960 px / 70 px gap; counter `— i / N —` 32 px grey at y=1835.
- Sample-frame approval: composite with `scripts/video/preview_frame.py` (same layout), never by prompting the generator to draw text. Details: `docs/video-generators/google-flow.md` § Frame layout and `docs/subtitles-and-build.md`.

## Video format
- 1080x1920, 24 fps, H.264 + AAC, hard cuts. **Frame layout (mandatory):** illustration-only stills/clips; English UPPERCASE title 64 px at (540,115); red underline x=400–680 (280 px, 6 px) at y=165; English subtitles 62 px (fallback 56/52) at y=1430; counter `— i / N —` at y=1835. Art cropped to bbox and scaled into 1060×1150 centred ~y=790. Font: Patrick Hand. Approval sample via `scripts/video/preview_frame.py` — never ask the image generator to draw text.
- Locked static camera: NO zoom, pan, push-in or Ken Burns.

## Animation — CRITICAL
- **Step 0 — per-part start/end pairs (Flow/Krea/HF and any paid i2v):** split the story into parts 1..N. For **each** part make **exactly one** matched pair: `scenes/partN_start.jpg` + `scenes/partN_end.jpg` (end generated **FROM** the start via image-to-image / edit; same background, camera, framing, scale, Xiaohei and objects; only the action's progress changes) plus `prompts/partN.txt` (motion-only transition prompt). Pick 2–3 refs from `reference-images/` per part, match style, check the pair side by side, regenerate drift. **Never** generate independent stills of every frame or unrelated images per beat. Show **part 1** (start + end + prompt) for approval; after approval produce **part by part** (check → clip → **QA watches** → next). Always pass aspect **9:16** explicitly; verify height > width; reject landscape. Illustration only (`no text, no letters, no captions`); large Xiaohei filling most of the width.
- **Flow ≤8 s hard limit + 720p direct:** Veo 3.1 clip durations are **4 / 6 / 8 s only**. Each part's narration slot must be **≤ 8 s**; if a beat is longer, split into two parts and make the next start match the previous end for continuity. Choose 4, 6 or 8 s; RIFE retimes afterwards. Flow generates at **720p** — **no 480p test, no Real-ESRGAN**. QA watches the 720p clip immediately.
- **Grok Imagine per-part chain (default):** each part ≤8 s = **two 4 s clips chained** (i2v start-frame only). Clip A from `partN_start.jpg` animating toward the end state → extract A's last frame → clip B from that frame continuing to the end. `partN_end.jpg` is the **check target only**. Join A+B into one continuous one-way take (no loop/zoom/jump). **Never** animate the two sketches as unrelated clips. Generate at **480p** → **QA watches** the join → **upscale locally to 720×1280** with Real-ESRGAN (`scripts/video/upscale_720p.sh`, model `realesr-animevideov3`) → sharpness QA — do **not** regenerate at 720p (different motion). Regenerate 720p only if upscale is soft/broken, then full QA. Same 480p→upscale path for other tools whose max output is below 720p. Helpers: `scripts/video/chain_and_upscale.sh`, docs: `docs/video-generators/grok-imagine.md`, `docs/upscale-real-esrgan.md`.
- **Flow method (per part):** work in Flow's **web UI** in box Chrome by default. For part N: upload `partN_start.jpg` as start and `partN_end.jpg` as end, paste `prompts/partN.txt`, choose Veo 3.1 Lite / **720p** / **9:16** / 4|6|8 s, generate, download to `gen/partN.mp4`, self-verify, **send to QA סרטונים (watches 720p)**, then go to part N+1. Classic composer only; rotate profiles; never click Agent; never buy credits. Use the **gflow-cli MCP only as fallback** on browser fault / no access (then force `aspect: "9:16"` and `ui_mode: "classic"` / `GFLOW_CLI_UI_MODE=classic`). Krea stays MCP-primary with browser fallback; start-only Krea models use `partN_start` + prompt, with `partN_end` as the check target. Details: `docs/video-generators/google-flow.md`.
- Each part animated with image-to-video as ONE single-pass, one-direction take covering the part slot. NEVER loop, ping-pong, reverse, repeat, or freeze-hold >0.3s. Never slow/stretch the animation.
- Smoothness: RIFE-interpolate to true 24fps continuous motion (the user loved Stanley Meyer scenes 1 and 10). Never interpolate across a cut. Fix single-frame jolts with RIFE neighbor midpoints.
- Patch defects by frame-splicing on decoded final frames; prefer a one-pass rebuild of a broken scene over stacked patches. Self-check for regressions and seams before sending to QA.

## Narration — CRITICAL (Chatterbox, replaces old edge-tts)
- Voice: Chatterbox TTS (MIT) cloned from a Kokoro am_eric reference (Apache-2.0). Setup in /workspace/voice-samples/comm (cbk.py); scripts mirrored in the stavpro repo under scripts/voice.
- Approved settings (2026-11-07): seed 7, exaggeration 0.6, cfg_weight 0.45. Backup voice for serious stories: Kokoro bm_george through Chatterbox.
- Record per PARAGRAPH, then join paragraphs with natural pauses in the same voice. NO time-stretching, no atempo, no speed-up, no smearing. Remove quiet breath noises in pauses. loudnorm I=-16.
- Reading must observe punctuation with natural pauses; energetic, young (~20s) storyteller feel, never impatient or rushed.
- Reference of the approved sound: /workspace/lustig/sample/lustig-clean-ending-v2b-quiet-pauses.mp3.
- FIRST-WORD CHECK: no clipped onsets; verify RMS energy in the first ~400ms of each sentence and that an ASR (faster-whisper) transcript contains every sentence's first word.

## Subtitles
- Full **English-only** subtitles synced to speech using ASR word timestamps on the final audio. Each block stays strictly inside its sentence's audio (0 boundary crossings). Balanced chunks, no 2-4 word orphans (except a whole short sentence), max 2 lines, Patrick Hand 62 (fallback 56/52), y=1430, max width 960.

## Scene-by-scene production
- Follow `docs/scene-by-scene-production.md`: approved table → for each part N (narration → start/end sketches → clip → **QA stage 1 watches** → Flow stays 720p / Grok upscales after 480p QA → RIFE → retime) → assemble with `build.py` → **QA stage 3** → SEO → Buffer → append `docs/lessons-learned.md`. Includes folder layout, 3-part example, and per-part checklist.

## Story/part mapping
- Strict chronological order, visual change every ~6-11s (and **≤ 8 s per part** when using Flow). Map parts to sentences in a table (`partN` → sentence numbers); after render inspect midpoint frames of every part to confirm visual matches the spoken line. Naming: `scenes/partN_start.jpg`, `scenes/partN_end.jpg`, `prompts/partN.txt`, `gen/partN_a.mp4` + `gen/partN_b.mp4` + `gen/partN.mp4` (Grok chain; optional `partN_720p.mp4`).

## QA — CRITICAL (every stage)
- **Mandatory:** every production goes through **QA סרטונים** (id `3596d23d-e7aa-48cf-b8a1-91e84bcfa678`), which **actually watches** the video and checks for faults. Self-checks are not a substitute. Details: `docs/qa.md`, `bots/qa-videos.md`.
- **Stage 1 — per part:** after each clip (Flow: **720p** immediate; Grok: **480p** join before upscale) — seam/continuity, glitches, distortions, extra limbs, baked-in text, 9:16, one-way / no loop / no zoom, match end sketch.
- **Stage 2 — after upscale:** sharpness only for **Grok / sub-720p** tools. **Skip for Flow** (already 720p; no Real-ESRGAN).
- **Stage 3 — full assembled video:** audio (first words, pauses, no stretch, loudness), subtitle sync/size, title+underline layout, English only, animation never frozen, fit to script.
- Any fault → fix → QA again. **Nothing delivered or scheduled without a QA pass.**

## Continuous improvement
- Every production should be **better than the last**. After each video append `docs/lessons-learned.md` (QA faults, user feedback, fixes; SEO performance once known). **Before starting the next video, read the log** and apply its lessons to prompts, timing, sketches, audio, and layout.

## Publishing
- Metadata (title, description, tags) and the schedule (1-2 days apart) come from the YouTube SEO bot (id 3a604c03-1cb4-454e-96de-87e48bbbf239); ask it before each scheduling. **Never include "Xiaohei"** in the YouTube title, description, or tags.
- Host the MP4 in the public repo stav888/video-hosting and use a commit-pinned raw URL; verify 200 and sha256.
- Buffer create_post on Smart History Knowledge: YouTube title, categoryId 27, privacy public, madeForKids false, isAiGenerated true. Buffer cannot set tags; the SEO bot adds them after publication. The YouTube AI label may need setting manually in Studio.
- Only the user's own words approve scheduling/publishing.
- After scheduling, create a one-off cleanup routine (~1h after publish): if published, delete only the hosted mp4 (keep folder), send the user the YouTube link in Hebrew, and send the SEO bot the video ID for tags.

## File habits
- Final MP4 under /workspace with version suffix; keep previous versions. Verify with ffprobe, volumedetect, frame inspection, subtitle lock, English-only, first-word check.
- When any process/setting changes, ask the user whether to also update the stavpro repo docs.
