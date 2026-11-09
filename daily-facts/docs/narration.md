# 2. Narration (voice)

**Narration is made FIRST**, then the edit is built around it (each clip is cut to the length of its line). Never stretch the voice to fit the pictures.

## Current voice: Kokoro TTS, `af_heart`
- Model [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Apache-2.0) via the `kokoro` Python package, `KPipeline(lang_code='a')`, voice **`af_heart`**.
- The channel voice called "S092" = af_heart at speed 0.92 (chosen 2026-10-24, replacing S088 = 0.88).
- **Since 2026-10-30: speed must be slower than 0.92** (feedback: too fast). Use `KOKORO_SPEED=0.86-0.88` and confirm on the 10 s sample.
- Delivery must sound like **storytelling, not stiff reading**: short sentences, "..." where a dramatic pause is wanted, commas for breath.
- The whole narration must sound like **one continuous story**, not disjointed segments: same voice, same speed, identical gaps.

## Steps
1. `scripts/voice/kokoro_tts_lines.py` (run in the Kokoro venv) -> `audio/lNN.wav` + `audio/lines.json` (text, duration, Kokoro word tokens).
   - each line trimmed at -45 dB, **5 ms fades**, **~150 ms silence pad** on both sides.
2. **10-second sample** (first 2-3 lines joined) -> user approval of voice and pace.
3. `scripts/voice/join_narration.py audio/l??.wav -o audio/narration.wav`
   - **0.40 s gap between lines**, internal pauses (commas, "...") capped at **~0.20 s**,
   - `loudnorm I=-16 TP=-1.5 LRA=11`, 48 kHz (Derinkuyu final: -16.16 LUFS, TP -1.46 dBTP, gaps 0.397-0.401 s; see `../examples/derinkuyu/narration_report.json`),
   - writes `narration_REPORT.json` for the QA bot.
4. **Word-by-word check against the script**: transcribe with faster-whisper and diff against `script.txt` (`scripts/subtitles/whisper_word_times.py` prints any missing/misread word per line). Regenerate a line if a word is wrong or swallowed.
5. QA bot checks the narration (pace, gaps, loudness, pronunciation) before the edit.

## Pronunciation fixes
- Regnal numbers: "II" -> "the Second" (add more to `FIX`).
- Years: Kokoro reads "1963" fine; spell out ambiguous numbers ("eighty-five meters").
- Foreign names: if Kokoro mangles one, respell it phonetically only in the TTS input (`FIX`), keep the real spelling in the subtitles.

## Legacy voices (kept for reference)
- **Pocket TTS clone** of the channel's original narrator (Petra, Oct 2026): `scripts/voice/legacy_pocket_tts_clone.py`, best of 4 seeds by ASR match and Resemblyzer speaker similarity, then `atempo=0.9`. Gated HF model, slower on CPU, retired for Kokoro.
- Edge-TTS (`en-GB-SoniaNeural`, -8% rate) narrated the Giza Short (Flow test, early Nov 2026); Google TTS / Piper / Chatterbox were tested and not used.

## No music
The approved design is narration only, no music (exception: the Alexandria test on 2026-10-24 used gentle music at the user's request). The Flow clips' own ambience is mixed very low and ducked under the voice.
