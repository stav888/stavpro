# 5. QA before delivery — mandatory at every stage

> ## 🚨 HARD RULE — QA סרטונים watches every stage
>
> **Every video production goes through the QA bot (QA סרטונים, id `3596d23d-e7aa-48cf-b8a1-91e84bcfa678`).** That bot **actually watches** the video (and extracts frames / runs measurements) and checks for faults. Self-checks on this bot are **not** a substitute.
>
> QA runs **at each stage** of the video — not only at the end:
>
> | Stage | When | What QA watches for |
> |---|---|---|
> | **(1) Per part — after each clip** | After the part's clip is ready (**Flow:** Veo 3.1 Lite **720p** download — **no 480p test, no upscale**; **Grok:** after A+B join at **480p**; other tools: after download; if max output &lt; 720p, treat like Grok) | Seam / continuity; glitches; distortions; extra limbs; text baked into the image; **9:16**; one-way motion with **no loop** and **no zoom**; match with the **end sketch** (`partN_end.jpg`); continuity with the previous part. **Flow:** QA watches the **720p** clip immediately |
> | **(2) After upscale to 720p** (**Grok / sub-720p only**) | After `scripts/video/upscale_720p.sh` on an approved 480p take. **Skip for Flow** (already 720p) | **Sharpness** check (line art stays sharp, not mushy / ringing / broken). Soft/broken → regenerate at native 720p, then full QA again |
> | **(3) Full assembled video before delivery** | After `build.py` muxes the final MP4 | **Audio:** first words audible, pauses, no stretch, loudness ~−16 LUFS. **Subtitles:** sync and size. **Title + underline** layout. **English only.** Animation never frozen. Overall fit to the script |
>
> **Any fault** → fix (narrow fix with timestamps) → **send to QA again**. Loop until pass.
>
> **Nothing is delivered to the user as final, scheduled, or published without a QA pass** on the relevant stage(s). The final delivery also needs a full-video QA pass.
>
> Bot profile and thresholds: [`../bots/qa-videos.md`](../bots/qa-videos.md). Handoffs: [`../bots/handoff-protocol.md`](../bots/handoff-protocol.md). Scene loop: [`scene-by-scene-production.md`](scene-by-scene-production.md).

Self-checks (this bot) run **before** each handoff to QA, then the independent QA bot. Nothing is shown to the user as final until the QA bot **passes** the full assembled video.

## Self-checks (producer, before each QA handoff)
- `ffprobe`: correct resolution for the stage (480p test / 720×1280 after upscale / final 1080×1920), 24 fps where expected, H.264 + AAC on finals, duration ≈ narration slot for that part / full narration for the final.
- `ffmpeg -af volumedetect` (final): not silent; loudness ~-16 LUFS.
- First words (final): ASR on the final MP4 contains the first word of each sentence; RMS present in first 400 ms of each onset.
- Subtitle lock (final): 0 crossings (printed by build.py); no orphan chunks of 2–4 words except whole short sentences.
- Animation: `../scripts/qa/static_runs.py file.mp4` (runs of near-identical frames >=5 frames, `TH` env threshold), `../scripts/qa/dup_frames.py` (dup ratio per scene; edit `cuts`), `../scripts/qa/bg_jitter.py file.mp4 "[(y0,y1,x0,x1)]"` (background must not jitter), start vs end frame of each scene must differ (no loop).
- Order: contact sheet of every scene's midpoint frame; each picture must match the subtitle at that moment.
- Version diff: `../scripts/qa/compare_versions.py old.mp4 new.mp4` proves a fix changed only the intended frames; also compare audio PCM MD5 (`ffmpeg -i f.mp4 -map 0:a -f md5 -`).
- Per-part (stage 1): last frame ≈ `partN_end.jpg`; A→B seam continuous (Grok); height > width; no baked-in letters.

## Stage 1 — Per-part clip QA (after generate / join)
Send to **QA סרטונים** with: absolute path of `gen/partN.mp4`, part number, path to `scenes/partN_end.jpg`, previous part end path if continuous, list of what changed, and **which generator / resolution** (Flow 720p vs Grok 480p join).

- **Google Flow:** generate **directly at 720p** (Veo 3.1 Lite). **No 480p test. No Real-ESRGAN.** QA **watches the 720p clip right away**.
- **Grok Imagine:** QA watches the **480p** A+B join first; upscale comes only after this pass.
- **Other tools:** if output is already ≥720p, same as Flow (QA at native res, no upscale). If max output is below 720p, same as Grok (QA then upscale).

QA must **watch** the clip and report pass/fail on:
- Seam / continuity (esp. Grok A→B join)
- Glitches, distortions, extra limbs
- Text / letters baked into frames
- Aspect **9:16** (height > width)
- One-way motion; **no loop**, **no reverse**, **no zoom**, locked camera
- Last frames match the **end sketch**
- Continuity with previous part (when the beat continues)

Fail → fix that part → QA again. **Do not** upscale (Grok) or start part N+1 until stage-1 QA passes (unless the user explicitly asks to continue drafting while a part is in rework — still no delivery).

## Stage 2 — Upscale sharpness QA (Grok / sub-720p only — skip for Flow)
**Not used for Google Flow** (Veo 3.1 Lite is already 720p).

After Real-ESRGAN ([`upscale-real-esrgan.md`](upscale-real-esrgan.md)) → `gen/partN_720p.mp4` (or equivalent) for Grok / other sub-720p tools:
- Send the upscaled clip to QA for a **short sharpness check**.
- Soft / mushy / ringing / broken line art → regenerate at native 720p (different motion) → full stage-1-style QA again, then sharpness.
- Stage 2 is mandatory **whenever you upscale**; never skip it after an upscale.

## Stage 3 — Full assembled video before delivery
After `build.py` produces `/workspace/<story>-history-vK.mp4`:
- Self-checks above, then send the final MP4 (+ version, change list, previous version path) to QA.
- QA watches the **whole** video and checks:
  - **Audio:** first words audible (no clipped onsets); pauses (between-sentence ~0.4–0.45 s; no long in-sentence silences); **no stretch / atempo**; loudness ~−16 LUFS, no clipping
  - **Subtitles:** sync to speech (≤ ~0.07 s), size (Patrick Hand 62 / 56 / 52), 0 boundary crossings, no short orphans
  - **Title + red underline** layout (64 px title; underline x=400–680, 6 px)
  - **English only** on screen
  - Animation never frozen; no loop / ping-pong / zoom; chronological fit to the script
- Fail → fix with timestamps → re-send → loop until pass.
- **No delivery, scheduling, or Buffer post** without this pass.

## Garbo final (reference values)
`garbo-history-v9.mp4`: 81.17 s, 1948 frames, 24 fps, 1080x1920, 15,274,165 bytes, sha256 732152e1…5ad749, audio PCM MD5 4078086a…c497142. Took 9 QA rounds (v1–v9) on the full video — the pattern for stage 3.

## Continuous improvement
Every production should be **better than the last**. After each video (and especially after QA rounds), append a short entry to [`lessons-learned.md`](lessons-learned.md): QA faults, user feedback, what was fixed, SEO performance once known. **Before starting the next video**, read that log and apply its lessons to prompts, timing, sketches, audio, and layout.
