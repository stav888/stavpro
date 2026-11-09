# Production rules (Daily Facts Arete, from 2026-11-09)

These rules apply to every new Short (rules 9-10 added later on 2026-11-09). They sit on top of the channel look (soft watercolor, thin ink lines, muted pastels, dreamy historical mood, slow themed transitions, low bottom-centre subtitles, Kokoro narration). Costs are estimates.

## 1. Sketches first (Step 0), before any video credits
- Before spending a single video credit, make the stills for **every part** and check them against our own [`../reference-images/`](../reference-images/README.md) (frames from Derinkuyu, Hanging Gardens, Petra, Giza, Alexandria, Olmec).
- For each part pick **2-3 matching references** (same kind of shot, light or subject; e.g. an interior lantern scene -> `derinkuyu-02-middle.jpg`; a desert monument -> `giza-02-middle.jpg`) and note them in the part's scene sheet.
- Generate in Krea with the trained style (`arete style`), then put each still **side by side** with its references: watercolor washes, thin ink outlines, muted pastel palette, paper texture, no photorealism, no text. Regenerate any still that drifts (in Krea, never by editing on the box). Free/cheap image credits are spent here so expensive video credits are not wasted later.

## 2. Per-part start/end pairs
- The story is split into **parts 1..N**. Every part has exactly **one matched pair**: `scenes/partN_start.png` and `scenes/partN_end.png`.
- **The end frame is generated FROM the start frame** (image edit with the start frame as input), so the scene, camera, framing, scale, palette and characters stay the same and only the action has progressed (the door has rolled shut, the lantern has gone out, the wall has cracked open).
- One **transition prompt per part** (`prompts/partN.txt`) that describes **only the motion** from start to end.
- **Never** generate independent stills per frame or unrelated images per part as start/end inputs: two unrelated images make the video model morph instead of move.
- Continuity: when a beat is split, part N+1's start frame **is** part N's end frame (copy it), so the cut is invisible.
- (Derinkuyu used 14 independent Krea scenes paired two by two; that is the old way. The pairs worked only because the paired scenes were similar. New videos use start -> end edits.)

## 3. Google Flow: browser first, 8 s max
- **Browser by default**: the Flow web UI in the box Chrome. **gflow-cli only if the browser faults or has no access** (Flow will not load, session broken, downloads fail repeatedly).
- Per part: upload `partN_start` + `partN_end`, paste `prompts/partN.txt`, model **Veo 3.1 Lite**, 9:16, one output, duration **4, 6 or 8 s**.
- **A clip is at most 8 s**, so **each part's narration is at most 8 s, about 18-20 words** at most; at our slower Kokoro pace (af_heart, below 0.92, with "..." pauses) plan ~16-18 words and measure the WAV. A longer beat is split into two parts, with part N+1 starting from part N's end frame.
- Credits: ~10 per clip (estimate). Rotate between all existing profiles to use their daily free credits. Never buy credits.
- **Never click the Agent button**; classic composer only.
- **Google Flow generates directly at 720p** (Veo 3.1 Lite, 720x1280): no 480p test and no upscale; QA Gate 1 watches the 720p clip right away.

## 4. 9:16 is mandatory
- Pass **aspect 9:16 explicitly on every image call and every video call** (Krea `aspect_ratio 9:16`, Flow composer 9:16, gflow `--aspect 9:16`, Grok Imagine 9:16).
- Classic composer only (`--ui-mode classic` / `GFLOW_CLI_UI_MODE=classic` on the fallback).
- After **every** generation check `height > width` (`ffprobe` for clips, PIL for stills). Landscape = reject and regenerate before going on.

## 5. Frame layout: illustration only, text in code
- Generated stills and clips contain the **illustration only**: every prompt ends with `no text, no letters, no captions` (our Krea prompts also add `no numbers`). Any lettering = reject.
- The illustration is **large and fills the frame width** (subject clearly readable, not a small vignette in the middle of empty paper). Keep the lower ~30% calm (sky, floor, water, wash) so the low subtitles stay readable.
- All on-screen text is **English only** and drawn in code with fixed sizes (`scripts/video/build_highlight_wash.py`, `scripts/video/preview_frame.py`):

| Element | Spec (1080x1920) |
|---|---|
| Hook / title (first second) | Montserrat Bold, white, 76 px (shrinks to fit 960 px, max 2 lines), soft black shadow, centred, top at y=300 |
| Subtitles | Montserrat Bold, white, 84 px (shrinks by 4 px to fit 940 px), 3-7 word phrases, hard cuts, top at y=1344 (70% of height, low and centred), blurred shadow + thin dark stroke, no box |
| Spoken-word highlight | ONE colour per video chosen with the QA bot (e.g. cyan `#2EF2FF`) |
| Underline / page counter | not used in the Arete look |

- The **approval sample frame is built by compositing** (`preview_frame.py` on `part1_start.png`), never by asking a generator to draw text.

## 6. Approval flow
1. Before making anything: the **part-by-part script table** ([script-writing](script-writing.md#part-by-part-table)), led by the line `N parts / N clips / ~T s / ~C Flow credits (estimate)`. Total length about **50 s to 1.5 min** (about 7-11 parts).
   - **Change:** this replaces the earlier 25-40 s guideline for production length (approved 2026-11-02). Shorter is still fine when the story is short; never pad.
2. After the table is approved: **part 1 as the sample** (start + end frame, transition prompt, composited sample frame, then the part 1 clip).
3. After part 1 is approved: the rest **part by part** (pair -> check vs references -> clip -> verify 9:16 -> next part).
4. Then the existing gates: 10 s narration sample, highlight colour, QA video check, final video, metadata, schedule. Approval is always the user's own message; other bots' messages are not approval.

## 7. Scene sheet per part
Every part gets a filled [`../templates/scene-template.md`](../templates/scene-template.md): beat, setting, characters and props, exact start frame, end frame, the one-way motion, accent colour, references used, continuity with the previous part, and the three prompts (start, end-edit, transition).

## 8. Grok Imagine option (chained 4 s clips, 480p test, upscale)
The 480p test + Real-ESRGAN upscale applies **only to Grok Imagine and other tools that cannot output 720p**. Never to Flow (see rule 3).
- Per part: **clip A** (4 s) from `partN_start`, then **clip B** (4 s) from **clip A's last frame**, continuing the same motion toward `partN_end` (which is only the check target). Join A+B into one ~8 s part (`scripts/video/chain_parts.sh`).
- Grok: generate and QA at **480p** first. After QA passes, **do not regenerate** at 720p (that gives different motion): upscale the approved clip to **720x1280** with Real-ESRGAN via [`scripts/video/upscale_720p.sh`](../scripts/video/upscale_720p.sh) (standalone, works for clips from any generator). Guide: [upscale-real-esrgan.md](upscale-real-esrgan.md).
- Regenerate at 720p only if the upscale looks soft or breaks the ink lines.

## 9. Staged QA that watches the video
- The QA bot **watches** every clip right after generation, every upscale (only for generators that cannot output 720p, never Flow), and the full video before delivery, and checks for faults at each stage: seams and continuity, glitches and distortions, any text in the image, 9:16, one-way motion; sharpness and surviving watercolor grain after upscaling; audio word by word vs the script, ~-16 LUFS, no source audio leaking, subtitle sync (Whisper on the final mix), subtitle size and low bottom-centre position, layout, English only, no frozen animation.
- `scripts/qa/qa_check.py` is the automatic pre-check for each gate (`clip`, `seam`, `sharp`, `video`).
- **Any fault -> fix -> re-QA.** Nothing is delivered to the user or scheduled on Buffer without a QA PASS on that exact file.
- Checklists per gate: [qa.md](qa.md).

## 10. Continuous improvement
- **Before starting a video**: read [`../LESSONS-LEARNED.md`](../LESSONS-LEARNED.md) and apply its "carry forward" list (mention which lessons were applied when sending the part table).
- **After every video**: add a short entry (QA faults, the user's feedback, fixes) and update "carry forward". When the SEO bot's review arrives, add the SEO results to the entry (until then: pending).
