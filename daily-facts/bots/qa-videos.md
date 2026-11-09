# QA סרטונים (QA bot)

**Role:** independent quality check that **actually watches** every clip, every upscale and the full video (with sound) at each stage. Nothing reaches the user and nothing is scheduled before QA passes it. Gates and checklists: [`../docs/qa.md`](../docs/qa.md).

## What I send, per stage
| Stage | I send | QA returns |
|---|---|---|
| Stills | `qa/sNN_sheet.jpg` per scene (2 Krea variants side by side + the narration line), prompts | best variant per scene, or "regenerate sNN because ..." (re-rolls come back as `sNN_rsheet.jpg`) |
| Clips (each, right after generation) | `clips/partN.mp4` + `qa_check.py clip/seam` output | seams, glitches, distortions, text, 9:16, one-way motion -> keep / lock area / re-roll |
| Upscale | 480p source + 720p result + `qa_check.py sharp` | sharpness, watercolor grain kept -> PASS / regenerate at 720p |
| Narration | `narration.wav`, `narration_REPORT.json`, `script.txt` | word-by-word check vs the script, pace, gaps, loudness, pronunciation |
| Highlight colour | 3-4 frames from different scenes | one recommended colour + reason (I pass it to the user for approval) |
| Final video | MP4 + contact sheet + `qa_check.py video` + subtitle sync report + metadata draft | audio vs script, -16 LUFS, no source audio, sync, subtitle size/position, layout, English only, no frozen animation -> pass or a numbered fix list |

## Typical QA findings we fixed
- Subtitle highlight early at sentence starts -> timing from Whisper on the final mix.
- Narration too fast / too stiff -> slower Kokoro speed, storytelling punctuation.
- Gaps uneven between lines -> `join_narration.py` (0.40 s / 0.20 s).
- Final video audio too quiet (-25.5 LUFS on a partial Derinkuyu cut) -> loudnorm.
- Wooden door instead of a rolling stone door (Derinkuyu s07) -> regenerated in Krea with "no wood".
- Drifting Flow clip -> locked with a still mask.

## Handoff per gate
- Each request names the gate (0 pairs, 1 clip, 2 upscale, 3 narration, 4 full video, 5 pre-schedule), the exact file paths on the shared box, the `scripts/qa/qa_check.py` output, the part's scene sheet (for clips) or the script (for audio), and what changed since the last QA round.
- QA answers PASS or a numbered fault list with timestamps and evidence frames/spectrograms; I fix every item and send it back for re-QA (full video again if the edit changed).
- QA findings go into `../LESSONS-LEARNED.md` after the video.

## Rules
- QA can recommend; the user approves.
- Every new version goes back to QA, not only the changed part, when the edit changed.
