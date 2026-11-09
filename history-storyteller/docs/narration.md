# 2. Narration (Chatterbox voice clone of Kokoro am_eric)

Approved by the user on 2026-11-07 (sample: `lustig-clean-ending-v2b-quiet-pauses.mp3`, kept on the box at `/workspace/lustig/sample/`). Earlier videos used edge-tts `en-US-ChristopherNeural` -5%; that is kept as the legacy option in `../skills/xiaohei-history-shorts/SKILL-legacy-edge-tts.md` (comparison: `../skills/xiaohei-history-shorts/README.md`).

## Why this stack
- Chatterbox TTS (Resemble AI, **MIT**) gives an energetic storyteller delivery.
- The voice timbre comes from one reference clip rendered with Kokoro-82M voice `am_eric` (**Apache-2.0**) - so the whole voice chain is commercially licensed. The user forbids LibriVox/unknown-licence reference voices and old-sounding voices.
- Backup timbre: Kokoro `bm_george` fed through Chatterbox the same way.


## Per-part length (≤ 8 s) and total runtime
- Narration is **written and checked per part** so each part fits a Flow/Veo clip: **hard max 8 seconds** at natural Chatterbox pace (~**18–20 English words** max per part).
- After each part take, **measure** the WAV; rewrite or split any part over 8 s. **Never** stretch, atempo, or speed up audio to fit.
- **Total video length** is proposed **per story** as a suitable timing between **~50 seconds and ~1.5 minutes** (about **7–11 parts** of up to 8 s each). The approval table shows the proposed total length and part count. Do not force "under 60 s" unless that length suits the story.
- The name **"Xiaohei" never appears in narration** (or anywhere in the story text). The black character plays the story's real subject; "Xiaohei" is only for image/video style prompts.

## Locked parameters
| Parameter | Value |
|---|---|
| reference clip | `k_am_eric.wav` (Kokoro `am_eric`, speed 1.0, 24 kHz) |
| seed | `torch.manual_seed(7)` before **every** take |
| exaggeration | **0.6** |
| cfg_weight | **0.45** |
| device | CPU |
| unit | **one take per paragraph** (`p1.txt`..`pN.txt`), not per sentence, not whole script. Parts map onto paragraphs/sentences so each **part ≤ 8 s** |
| join | plain concatenation, natural pauses only (~0.4–0.5 s between paragraphs) |
| time-stretch / atempo / setpts on audio | **never** (if a part is over 8 s: rewrite or split; never stretch) |
| breath noises | gated to digital silence in pauses (>=150 ms below -40 dB) |
| loudness | `loudnorm=I=-16:TP=-1.5:LRA=11`, 48 kHz |
| head pad | 0.15 s silence before first word; 30 ms fade only at the very end |

Watermark note: `resemble-perth` may lack the implicit watermarker on CPU builds; the scripts fall back to `perth.DummyWatermarker` so generation works.

## Step by step (paths relative to a project folder `<story>/audio/`)
```bash
# 0) one-time: reference voice (Kokoro env)
kokoro_venv/bin/python scripts/voice/make_kokoro_reference.py     # writes k_am_eric.wav (+ other voices)
cp k_am_eric.wav <story>/audio/

# 1) paragraphs -> p1.wav..p4.wav  (edit range(1,5) for N paragraphs)
cd <story>/audio && chatterbox_venv/bin/python ../../scripts/voice/chatterbox_paragraphs.py

# 2) join (verified: Garbo joined.wav == concat of p1..p4)
python scripts/voice/join_paragraphs.py joined.wav p1.wav p2.wav p3.wav p4.wav

# 3) breath gating + loudnorm -16 + head pad
python scripts/voice/process_narration.py joined.wav narration_norm.wav

# 4) ASR word timestamps (faster-whisper small, int8, CPU) + list of pauses >0.45 s
python scripts/voice/asr_words.py narration_norm.wav asr_words.json
```
Listen to every paragraph. If a take has a glitch, re-roll only that paragraph (same seed first; if it still fails, report to the user before changing settings). `chatterbox_full_pass.py` (single take of the whole script, `max_new_tokens` raised to 4500) is kept for comparison only.

## Checks before building video
- Each part's measured duration is **≤ 8.0 s**; total proposed length is in the **~50 s – ~1.5 min** band (or whatever the approved table said).
- Narration text never contains the word **Xiaohei**.
- ASR transcript contains the first word of every sentence.
- RMS energy present within the first ~400 ms of every sentence onset; no fade-ins at onsets.
- No pause >0.45 s inside a sentence; paragraph pauses ~0.4–0.5 s.
- Audio stays the same file through all later video versions (the QA bot compares PCM MD5 between versions).
