---
name: Xiaohei History Shorts
description: >-
  Use this when creating a vertical 9:16 history-story Shorts video in the Ian
  Xiaohei illustration style with English narration and subtitles — the user's
  approved production settings.
---

> **Current option (since Nov 2026):** Chatterbox per-paragraph narration, expanded scripts (trial). (Live copy from the bot's skill store, 2026-11-09. The older option is [`SKILL-legacy-edge-tts.md`](SKILL-legacy-edge-tts.md); see the [comparison](README.md).)

# Xiaohei History Shorts — approved settings (updated 2026-11-09)

Create vertical history Shorts that tell one true story in strict chronological order. Full backup docs and scripts: github.com/stav888/stavpro/tree/master/history-storyteller.

## Approval flow (mandatory)
- Before ANY full production: show the user the script (Hebrew translation for review; the video is English only) AND one sample frame, and wait for explicit approval. Approval of the preview does not by itself authorize anything else (publishing etc.).

## Script style
- Expanded, engaging storytelling (approved Garbo rewrite, 2026-11-07): developed chronological story, concrete details, clear setup and progression, strong ending, not a brief summary. Don't compress the story just to fit under 60s (typical result ~70-85s).
- This expanded style is a TRIAL since 2026-11-09 (starting with Garbo). The YouTube SEO bot compares expanded vs earlier short (<60s) Shorts; if results are worse, revert to short scripts. Tell the SEO bot the video ID of every expanded upload.
- "A true story." ending only when it fits. Sensitive topics: respectful, no gore.

## Style (from github.com/helloianneo/ian-xiaohei-illustrations)
- Pure white background, thin wobbly black hand-drawn lines, lots of white space, only tiny red/orange/blue annotations.
- Xiaohei: solid-black character, white dot eyes, thin legs, blank expression, who PERFORMS the core action in every scene.
- Use repo example images as reference_image_paths for every GenerateImage call. No/minimal text in images; regenerate once on garbled text or style drift.

## Video format
- 1080x1920, 24 fps, H.264 + AAC, hard cuts. Art big in the middle band; title at top, subtitles at bottom. Font: Patrick Hand.
- Locked static camera: NO zoom, pan, push-in or Ken Burns.

## Animation — CRITICAL
- Each still animated with image-to-video as ONE single-pass, one-direction take covering the scene slot. NEVER loop, ping-pong, reverse, repeat, or freeze-hold >0.3s. Never slow/stretch the animation.
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
- Full English subtitles synced to speech using ASR word timestamps on the final audio. Each block stays strictly inside its sentence's audio (0 boundary crossings). Balanced chunks, no 2-4 word orphans (except a whole short sentence), max 2 lines, Patrick Hand.

## Story/scene mapping
- Strict chronological order, visual change every ~6-11s. Map scenes to sentences in a table; after render inspect midpoint frames of every scene to confirm visual matches the spoken line.

## QA
- Send the final file to QA סרטונים (id 3596d23d-e7aa-48cf-b8a1-91e84bcfa678) and wait for pass before delivering. Fix reported faults with timestamps and re-check.

## Publishing
- Metadata (title, description, tags) and the schedule (1-2 days apart) come from the YouTube SEO bot (id 3a604c03-1cb4-454e-96de-87e48bbbf239); ask it before each scheduling.
- Host the MP4 in the public repo stav888/video-hosting and use a commit-pinned raw URL; verify 200 and sha256.
- Buffer create_post on Smart History Knowledge: YouTube title, categoryId 27, privacy public, madeForKids false, isAiGenerated true. Buffer cannot set tags; the SEO bot adds them after publication. The YouTube AI label may need setting manually in Studio.
- Only the user's own words approve scheduling/publishing.
- After scheduling, create a one-off cleanup routine (~1h after publish): if published, delete only the hosted mp4 (keep folder), send the user the YouTube link in Hebrew, and send the SEO bot the video ID for tags.

## File habits
- Final MP4 under /workspace with version suffix; keep previous versions. Verify with ffprobe, volumedetect, frame inspection, subtitle lock, English-only, first-word check.
- When any process/setting changes, ask the user whether to also update the stavpro repo docs.
