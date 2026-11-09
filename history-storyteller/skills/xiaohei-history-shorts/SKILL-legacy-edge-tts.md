---
name: Xiaohei History Shorts
description: >-
  Use this when creating a vertical 9:16 history-story Shorts video in the Ian
  Xiaohei illustration style with English narration and subtitles — the user's
  approved production settings.
---

> **Legacy option:** edge-tts en-US-ChristopherNeural single-pass narration, used Oct 19–30 2026; shorter <60 s scripts. (Copy of the skill as it was before the Nov 2026 update. The current option is [`SKILL.md`](SKILL.md); see the [comparison](README.md).)

# Xiaohei History Shorts — approved settings (locked by the user 2026-10-19 after the Yamaguchi video)

Create vertical history explainer Shorts that tell one true story in strict chronological order.

## Style (from github.com/helloianneo/ian-xiaohei-illustrations)
- Pure white background, thin wobbly black hand-drawn lines, lots of white space in the source art, only tiny red/orange/blue annotations.
- Xiaohei: solid-black character, white dot eyes, thin legs, blank expression, who PERFORMS the core action in every scene (never decoration).
- Download the repo example images and use them as reference_image_paths for every GenerateImage call. No/minimal text inside generated images. Regenerate once if there is readable/garbled text or style drift.
- Sensitive topics: respectful tone, no gore/graphic detail; show violence as a distant flash/silhouette moment.

## Video format
- 1080x1920 (9:16), H.264 + AAC, hard cuts between scenes.
- Art placed BIG: ~85-100% of frame width in the middle band (crop only white edges, never subjects). Title at top, subtitles at bottom, scene counter (e.g. 3 / 8).
- Font: Patrick Hand (handwritten) for title and all captions/subtitles, large and legible.
- Locked static camera: absolutely NO zoom, NO pan, NO push-in, NO Ken Burns (the user explicitly rejected the zoom/flicker).

## Animation — CRITICAL, no loops
- Animate each still with GenerateVideo image-to-video as ONE single-pass take whose generated duration covers the scene's full narration slot (generate duration = ceil(slot), max 15s; trim the end to the exact slot).
- NEVER ping-pong/boomerang, never reverse, never stream_loop/repeat a clip, never freeze-hold >0.3s.
- Prompt for slow, continuous, progressive, non-repetitive motion in one direction of action for the whole clip, locked camera wording in every prompt.
- If a clip returns shorter than its slot: regenerate once for longer duration; if still short, slow that single pass with setpts by at most 1.35x. A loop or a freeze is never acceptable.
- Verify no-loop: frames at ~1s / mid / end of checked scenes must PROGRESS (end pose clearly differs from start pose), with pixel-diff reported.

## Narration and subtitles — CRITICAL, continuous single pass
- Conversation with the user is in Hebrew; EVERYTHING inside the video is English only.
- Narration: edge-tts voice en-US-ChristopherNeural, rate -5% (natural, relaxed pace the user approved), loudnorm I=-16. NEVER speed up (no higher rate, no atempo). If the video must be shorter, trim the script — never accelerate speech.
- Generate the narration as ONE SINGLE edge-tts pass over the whole script in one file — NEVER per-sentence files concatenated. Per-sentence generation makes each segment sound disconnected and can clip first words; a single pass keeps one continuous storytelling flow with natural pauses only.
- TTS punctuation trick (learned on the Wojtek video, QA-verified): feed edge-tts the script with SEMICOLONS instead of sentence-ending periods (wording unchanged). With periods, this voice gives every sentence a soft 125-225ms fade-in attack so first words sound cut; with semicolons it flows through clause boundaries with sharp attacks (measured 5-75ms). Displayed subtitles keep normal sentence punctuation. Afterwards normalize inter-sentence gaps to ~0.4s by editing only digital silence in the gaps, and check for any long (>0.45s) pause hiding INSIDE a sentence too — trim it the same way.
- Derive the sentence timing table from that single file using edge-tts SentenceBoundary events (or WordBoundary when available), cross-validated with an ASR word-timestamp pass (e.g. faster-whisper) on the final audio. Build scene cuts and subtitles from this table.
- FIRST-WORD CHECK (mandatory): nothing may clip sentence onsets — no trimming near onsets, no fade-ins at sentence starts, add only a small silent head pad before the narration starts if needed. Verify (1) speech energy/RMS is present in the first ~400ms of every sentence start in the final mix, and (2) an ASR transcript of the final audio contains the first word of every sentence. Fix and re-check if any first word is missing.
- Subtitles: FULL subtitles following the narration, sentence-locked — every block starts/ends strictly inside its sentence's measured audio (0 boundary crossings). Split long sentences into balanced chunks (e.g. 18 words -> 9+9). No orphan blocks of 2-4 words; a complete short sentence shown whole is the only exception. Max 2 lines, Patrick Hand.

## Story structure
- Strict chronological order, a clear beginning (setup/hook) and a clear ending (payoff). One visual per story beat; aim for a visual change every ~6-11 seconds — expand the number of scenes rather than stretching few images.
- Before assembling, map every scene to its narration sentence(s) in a scene table, and after rendering Read-inspect midpoint frames of EVERY scene in order to confirm each visual matches the subtitle sentence spoken at that moment. Fix any visual that appears at the wrong point in the story.

## Length
- Default target: under 60 seconds for a standard Short (about 90-110 English words at the approved pace). Longer expanded versions only when the user approves a longer script in Hebrew first.

## Approval flow
- For expanded/longer scripts: first show the user the script in Hebrew for approval; the video itself is produced in English only. Do not produce until the user approves (e.g. says 'תכין').
- Short user-supplied stories can be produced directly.

## QA collaboration
- After building a video, send the final file to the QA סרטונים agent (id 3596d23d-e7aa-48cf-b8a1-91e84bcfa678) for an independent check (first words audible, continuous narration, subtitle lock, no-loop animation, scene order) and wait for its pass/fail report before delivering to the user. If it reports a fault with timestamps, fix and re-check.

## File/output habits
- Save final MP4 under /workspace with a clear name; keep previous versions untouched (new version suffix).
- Verify before delivering: ffprobe (resolution, duration, codecs), volumedetect (non-silent), frame inspections as above, subtitle lock check, English-only check, first-word check as above.
