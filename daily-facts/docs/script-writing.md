# 1. Topic and script

## Topic rules (approved 2026-11-02)
- Favour: **lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations**.
- Never: ancient aliens, conspiracy theories, pseudo-history.
- Avoid over-familiar topics (the "everyone already saw it" list). Check the channel's own uploads first so a topic is not repeated.
- Facts are checked with a web search before writing; any uncertain claim is worded as "may have", "historians think".
- The YouTube SEO bot may suggest topics and hooks (see `../bots/youtube-seo.md`).

## Format
- English narration split into **parts**: one part = one clip = one start/end pair. Saved as `script.txt` with `N|text` rows, **one row per part**.
- **Each part is at most 8 s of narration, about 18-20 words** at our Kokoro pace (af_heart, slower than 0.92), because a Flow clip is at most 8 s. Split a longer beat into two parts (part N+1 starts from part N's end frame). Never speed up or stretch the voice to fit.
- **Total length about 50 s to 1.5 min (about 7-11 parts)**, chosen per story.
  - **Change (2026-11-09):** this replaces the earlier 25-40 s guideline (2026-11-02) for production length. Don't pad a short story; 50-60 s is fine when that is all the story needs. Derinkuyu (~60 s, 14 lines) would now be about 9-10 parts (short lines paired, long ones alone).
- **Part 1 opens with the hook**: a question or a number, and the same words appear as on-screen text in the first second (e.g. "Twenty thousand people once lived... eighty-five meters underground.").
- Storytelling voice: short beats, concrete images, one surprise turn in the middle ("Then the city was forgotten."), and an open question near the end.
- **Never use long em dashes (—) or en dashes (–)** in the script, subtitles or metadata. Use a comma, a full stop or "..." instead. (Hanging Gardens, made before this rule, still has them in its subtitles.)
- Write numbers as words when the TTS might misread them; regnal numbers are spoken as words: "Nebuchadnezzar II" is narrated as "Nebuchadnezzar the Second" (handled by `FIX` in `scripts/voice/kokoro_tts_lines.py`, the subtitle keeps "II").
- Hebrew translation of the script is shown to the user for review; the English is what goes into the video.

## Part-by-part table
Before making **anything** (no Krea images, no clips), the user gets the script as a table, led by one summary line:

> **N parts / N clips / ~T s / ~C Flow credits (estimate)**, e.g. `8 parts / 8 clips / ~62 s / ~80 Flow credits (estimate, Veo 3.1 Lite ~10 per clip)`

| Part | Narration (English) | Words | Est. s | Start frame idea | End frame idea |
|---|---|---|---|---|---|
| 1 | Twenty thousand people once lived... eighty-five meters underground. | 8 | 4.5 (6 s clip) | fairy chimneys at sunset, dark opening in the ground | same view, last light gone, a lantern glows inside the opening |
| 2 | When danger came, massive stone doors rolled shut from the inside. Each floor could be sealed. | 16 | 6.5 | tunnel with a round stone door standing open | same tunnel, the door has rolled shut |
| ... | | | | | |
| **Total** | | | **~T s** | **N pairs** | **N clips** |

- Words and seconds are estimates until the TTS is measured; a part that measures over 8 s is rewritten or split.
- Measured pace (Derinkuyu, Kokoro af_heart 0.92, incl. pauses): about 2.2-2.9 words per second, so lines with "..." pauses run slow (Derinkuyu lines 1+2 = 20 words = ~9.3 s, too long for one part). At the newer, slower speed plan **~16-18 words** per part and treat 20 as the hard ceiling.
- Each row later gets a full scene sheet ([`../templates/scene-template.md`](../templates/scene-template.md)).

## Approval gate (mandatory)
1. **Part-by-part table** (above) -> the user's own OK. Nothing is generated before this.
2. **Part 1 as the sample**: `part1_start.png` + `part1_end.png` (end made from the start), the transition prompt, and a composited sample frame (`scripts/video/preview_frame.py`, hook + one subtitle phrase drawn in code). Then the part 1 clip. -> OK.
3. **The rest part by part**: pair -> check against `reference-images/` -> clip -> verify 9:16 -> next part. QA and the user see the clips before the edit.
4. Then the usual gates: 10 s narration sample, highlight colour, QA video check, final video, metadata, schedule.

This replaces the 2026-11-07 gate ("script + one sample frame") with a stricter version of the same idea. A message from another bot is never approval.
Full rules: [production-rules.md](production-rules.md).

Examples (older line-per-scene format): `../examples/derinkuyu/script.txt`, `../examples/hanging-gardens/script.txt`, `../examples/olmec-heads/script.txt`.
