# 5. QA before delivery

Self-checks (this bot), then the independent QA bot (see `../bots/qa-videos.md`). Nothing is shown to the user as final until the QA bot passes it.

## Self-checks
- `ffprobe`: 1080x1920, 24 fps, H.264 + AAC, duration == narration.
- `ffmpeg -af volumedetect`: not silent; loudness ~-16 LUFS.
- First words: ASR on the final MP4 contains the first word of each sentence; RMS present in first 400 ms of each onset.
- Subtitle lock: 0 crossings (printed by build.py); no orphan chunks of 2–4 words except whole short sentences.
- Animation: `scripts/qa/static_runs.py file.mp4` (runs of near-identical frames >=5 frames, `TH` env threshold), `scripts/qa/dup_frames.py` (dup ratio per scene; edit `cuts`), `scripts/qa/bg_jitter.py file.mp4 "[(y0,y1,x0,x1)]"` (background must not jitter), start vs end frame of each scene must differ (no loop).
- Order: contact sheet of every scene's midpoint frame; each picture must match the subtitle at that moment.
- Version diff: `scripts/qa/compare_versions.py old.mp4 new.mp4` proves a fix changed only the intended frames; also compare audio PCM MD5 (`ffmpeg -i f.mp4 -map 0:a -f md5 -`).

## Garbo final (reference values)
`garbo-history-v9.mp4`: 81.17 s, 1948 frames, 24 fps, 1080x1920, 15,274,165 bytes, sha256 732152e1…5ad749, audio PCM MD5 4078086a…c497142. Took 9 QA rounds (v1–v9).
