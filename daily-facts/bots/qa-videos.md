# QA סרטונים (QA bot)

**Role:** independent quality check. Nothing reaches the user before QA passes it.

## What I send, per stage
| Stage | I send | QA returns |
|---|---|---|
| Stills | `qa/sNN_sheet.jpg` per scene (2 Krea variants side by side + the narration line), prompts | best variant per scene, or "regenerate sNN because ..." (re-rolls come back as `sNN_rsheet.jpg`) |
| Clips | `clips/*.mp4` + contact sheet | keep / lock area / re-roll |
| Narration | `narration.wav`, `narration_REPORT.json`, `script.txt` | word-by-word check vs the script, pace, gaps, loudness, pronunciation |
| Highlight colour | 3-4 frames from different scenes | one recommended colour + reason (I pass it to the user for approval) |
| Final video | MP4 + contact sheet + subtitle sync report + metadata draft | pass or a numbered fix list |

## Typical QA findings we fixed
- Subtitle highlight early at sentence starts -> timing from Whisper on the final mix.
- Narration too fast / too stiff -> slower Kokoro speed, storytelling punctuation.
- Gaps uneven between lines -> `join_narration.py` (0.40 s / 0.20 s).
- Final video audio too quiet (-25.5 LUFS on a partial Derinkuyu cut) -> loudnorm.
- Wooden door instead of a rolling stone door (Derinkuyu s07) -> regenerated in Krea with "no wood".
- Drifting Flow clip -> locked with a still mask.

## Rules
- QA can recommend; the user approves.
- Every new version goes back to QA, not only the changed part, when the edit changed.
