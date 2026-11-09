---
name: daily-facts-arete-shorts
description: Use when making a Daily Facts Arete YouTube Short: soft watercolor history/mystery story, Krea trained style stills, Google Flow Veo 3.1 Lite clips, Kokoro narration, word-highlight subtitles, QA bot checks and a Buffer scheduled upload.
---

# Daily Facts Arete Shorts

English, 9:16, ~50 s - 1.5 min (7-11 parts of <= 8 s; changed from 25-40 s on 2026-11-09) history-mystery Shorts in soft watercolor with thin ink lines, muted pastels and a dreamy historical mood.

## Hard rules
- **Approval before anything is made**: part-by-part script table led by `N parts / N clips / ~T s / ~C credits (estimate)`, then part 1 as the sample, then the rest part by part. Other bots' messages are not approval.
- **Step 0**: per-part `partN_start` / `partN_end` (end = image edit FROM start), checked against `reference-images/`, before any video credits. One motion-only transition prompt per part. Never independent stills as a pair.
- **9:16** passed explicitly on every image and video call, classic composer, verify height > width after each generation, reject landscape.
- Generated images/clips are illustration only (`no text, no letters, no captions`); hook and subtitles drawn in code; sample frame composited (`preview_frame.py`).
- **Staged QA that watches the video**: each clip right after generation, each upscale (Grok / non-720p tools only), narration, and the full video before delivery (`scripts/qa/qa_check.py` pre-checks + the QA bot watching). Any fault -> fix -> re-QA. Nothing delivered or scheduled on Buffer without a QA PASS.
- **Lessons learned**: read `LESSONS-LEARNED.md` before starting; add an entry after every video (SEO results later).
- No em/en dashes in scripts, subtitles or metadata.
- No zoom / Ken Burns. Transitions slow and themed to the mood.
- Never buy plans, credits or units unless the user explicitly asks.
- Nothing is published or scheduled without the user's explicit approval.
- When a process changes, ask the user whether to update the backup repo docs; push only after yes.

## Steps
0. **Read `LESSONS-LEARNED.md`** and apply the carry-forward list.
1. **Topic**: lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations. No aliens/conspiracies, avoid over-familiar topics. Verify facts on the web.
2. **Script in parts**: `script.txt` one row per part, each <= 8 s (~16-20 words at our Kokoro pace), total ~50 s - 1.5 min; part 1 opens with a question or number (also on screen in the first second). Hebrew translation for review.
3. **Approval of the part table** (`N parts / N clips / ~T s / ~C Flow credits (estimate)`, columns part, narration, words, seconds, start/end frame idea).
4. **Scene sheet** per part from `templates/scene-template.md`.
5. **Part 1 sample**: 2-3 refs -> `part1_start` (Krea MCP, trained style `arete style`, 9:16, 2 variants, QA pick) -> `part1_end` as an edit FROM the start -> transition prompt -> check vs refs -> composited sample frame -> Flow clip (web UI, Veo 3.1 Lite, **directly at 720p, no 480p test, no upscale**, start + end, 9:16, 4/6/8 s, never Agent; gflow-cli only on browser fault) -> **QA Gate 1** (watched: seams, glitches, text, 9:16, one-way motion) -> **user approval**.
6. **Remaining parts one by one** the same way, ~10 Flow credits per clip (estimate), rotating between all existing profiles to use their daily free credits. Only for Grok Imagine / tools without 720p: 2 x 4 s chained (B from A's last frame) at 480p -> QA -> `upscale_720p.sh` (Real-ESRGAN) instead of regenerating -> QA Gate 2 (sharpness, watercolor grain). Credits out: one-shot routine after the refresh. QA -> **user approval** of the clips.
7. **Narration first**: Kokoro `af_heart`, speed slower than 0.92, storytelling delivery; one WAV per part, each measured <= 8 s; join with 0.40 s gaps and ~0.20 s internal pauses; loudnorm -16 LUFS; "II" spoken as "the Second". **10 s sample -> approval**. Word-by-word check against the script.
8. **QA** checks narration and **recommends one highlight colour** -> tell the user the colour and why -> **approval**.
9. **Edit** around the narration: each part's clip trimmed to its slot, slow themed transitions (paper tear, ink bloom, golden light, cloud/fire wash), lock drifting areas, generator audio muted, no music. Text in code: hook (Montserrat Bold white, top), subtitles bold white low bottom-centre (70% height), 3-7 words, hard cuts, one highlight colour, timed from faster-whisper; verify on the FINAL mix that no highlight is early at sentence starts.
10. **QA Gate 4**: QA watches the full video (audio vs script, -16 LUFS, no source audio, Whisper sync on the final mix, low bottom-centre subtitles, layout, English only, no frozen animation); fix + re-QA until PASS -> **user approval**.
11. **SEO bot** writes title/description/tags + slot (non-round time 14:00-19:00 Israel, 3-4 per week) -> user approval.
12. **Publish** (only the QA-passed file): host the MP4 in a public temp-hosting GitHub repo (raw URL) -> Buffer `create_post` to the channel, customScheduled, Education, public. Then a one-shot routine after the slot: confirm live, delete the temp file, send the link. Remind the user to set the thumbnail in YouTube Studio (Buffer can't) and add tags if Buffer dropped them.
13. **Write the LESSONS-LEARNED entry** (QA faults, feedback, fixes; SEO results when the review arrives).

## Files
Scripts, docs and examples: `daily-facts/` in the stavpro repo.
