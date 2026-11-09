# 5. QA

Every image set, narration and video passes the **QA סרטונים** bot before the user sees it (`../bots/qa-videos.md`). Never send a video to the user before QA approves.

| Stage | What goes to QA | QA checks | Output |
|---|---|---|---|
| Step 0 pairs | per part: `partN_start` variants, then start + end side by side with the 2-3 chosen reference frames + the scene sheet | style match to `reference-images/`, end frame is the same shot with only the action changed, no text/letters, subject fills the width, calm lower third, history accuracy, height > width | best start variant, "pair OK" or "regenerate partN_end because ..." |
| Clips (part 1 first, then part by part) | `clips/partN.mp4` + its `_endcheck.jpg` | 9:16, one-way motion, last frame close to `partN_end`, drift, morphing, flicker, unwanted zoom, text artefacts; Grok option: A/B seam, then 720p upscale sharpness | keep / lock area / re-roll |
| Narration | narration WAV + `_REPORT.json` + script | word-by-word vs script, pace (slower than 0.92), gaps 0.40 s / 0.20 s, -16 LUFS, pronunciation ("the Second") | pass / list of lines to redo |
| Highlight colour | 3-4 frames from different scenes | contrast with the palette | one recommended colour + reason |
| Video | final MP4 + `scripts/qa/contact_sheet.sh` sheet + `verify_subtitle_sync.py` output | sync (not early at sentence starts), subtitle position low, transitions slow and themed, no dashes, hook text in 1st second, length, loudness, end card | pass / fixes |

Self-checks before sending to QA:
- `ffprobe` every clip and the final file, PIL every still: height > width (landscape = reject).
- `grep -P "\x{2014}|\x{2013}"` on script, subtitles and metadata returns nothing.
- `verify_subtitle_sync.py` median offset near 0, max |offset| <= 2 frames.
- Loudness with `ffmpeg -af ebur128`.
