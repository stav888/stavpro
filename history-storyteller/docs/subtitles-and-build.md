# 4. Timing, subtitles, compose

## Sentence timing table
`scripts/video/sentence_timing.py` (run in the project folder) needs `audio/sentences.txt`, `audio/asr_words.json`, `audio/narration_norm.wav`:
- Aligns script words to ASR words (difflib), then snaps each sentence's first-word onset to the end of the preceding silence (< -45 dB).
- Sentence `start` = onset - 0.06 s; `end` = next sentence start. Checks the gap before each onset is silent.
- Writes `audio_timing.json` (rows + total) and `ons.json` (per-word onsets for subtitle splits).

## Build (`scripts/video/build.py OUT.mp4`)
- 1080x1920, 24 fps, H.264 crf 20, AAC 192k 48 kHz. Hard cuts at sentence starts (frame-rounded).
- Per-scene art is auto-cropped to its non-white bbox and scaled to ~1060x1150 max, centred ~y=790, white pad.
- Static overlay per scene: title at top (Patrick Hand 64, short red underline) and a `— i / N —` counter at bottom. **Edit the title string per video.**
- Subtitles: Patrick Hand 62/56/52, black, max 2 lines, 960 px wide, y=1430. Sentences <=10 words shown whole; longer split into 2–3 balanced chunks at commas or by per-sentence overrides `OV={sentence:[word indexes]}` (edit per video). Line breaks never after a/the/to/and/... Each chunk starts/ends on the frame grid **inside** its sentence; script asserts 0 boundary crossings.
- Scene mapping in this build is 1 scene per sentence row (`anim/scene{i}_r.mp4`); if a project has more scenes than sentences, extend `segs`.
- Concats clips and muxes `audio/narration_norm.wav`.
