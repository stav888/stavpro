# 1. Topic and script

## Topic rules (approved 2026-11-02)
- Favour: **lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations**.
- Never: ancient aliens, conspiracy theories, pseudo-history.
- Avoid over-familiar topics (the "everyone already saw it" list). Check the channel's own uploads first so a topic is not repeated.
- Facts are checked with a web search before writing; any uncertain claim is worded as "may have", "historians think".
- The YouTube SEO bot may suggest topics and hooks (see `../bots/youtube-seo.md`).

## Format
- English narration, **10-15 lines**, one sentence (or two short ones) per line, saved as `script.txt` with `N|line` rows.
- Target length **25-40 s** (guideline). Derinkuyu ran ~60 s with 14 lines; Hanging Gardens ~66 s with 15 lines. Shorter is better for retention.
- **Line 1 is the hook**: a question or a number, and the same words appear as on-screen text in the first second (e.g. "Twenty thousand people once lived... eighty-five meters underground.").
- Storytelling voice: short beats, concrete images, one surprise turn in the middle ("Then the city was forgotten."), and an open question near the end.
- One scene per line (14 lines = 14 scenes = 7 Flow clips when every clip uses a start + end frame pair).
- **Never use long em dashes (—) or en dashes (–)** in the script, subtitles or metadata. Use a comma, a full stop or "..." instead. (Hanging Gardens, made before this rule, still has them in its subtitles.)
- Write numbers as words when the TTS might misread them; regnal numbers are spoken as words: "Nebuchadnezzar II" is narrated as "Nebuchadnezzar the Second" (handled by `FIX` in `scripts/voice/kokoro_tts_lines.py`, the subtitle keeps "II").
- Hebrew translation of the script is shown to the user for review; the English is what goes into the video.

## Approval gate (mandatory, since 2026-11-07)
Before ANY full production the user gets:
1. the script (English + Hebrew), and
2. **one sample frame** (a single Krea image in the Arete style for the hook scene),

and production starts only after the user's own explicit OK. A message from another bot is not approval.
Further approvals follow at every stage (see the pipeline table in `../README.md`).

Examples: `../examples/derinkuyu/script.txt`, `../examples/hanging-gardens/script.txt`, `../examples/olmec-heads/script.txt`.
