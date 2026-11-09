# 4. Subtitles and edit

## Order
narration (final, approved) -> word timestamps -> **highlight colour recommendation from QA -> user approval** -> edit -> QA video check.

## Timeline (narration-first, one clip per part)
- Each part's narration (<= 8 s) is laid on its own clip (`clips/partN.mp4`, 4/6/8 s); the part's slot = `LEAD + narration + TAIL`, and the clip is trimmed to that window (never looped or stretched).
- Each scene = `LEAD 0.25 s + line duration + TAIL 0.35 s` (capped at clip length minus the transition).
- The clip is **cut to its line**: the editor scans each Flow clip and takes the window with the least motion jitter (`build_highlight_wash.py`), or retimes the 8 s pair-clip to the two lines it covers (`build_flow_xfade_ass.py`, Derinkuyu).
- First second: the hook line is on screen as text immediately (question or number), drawn in code (Montserrat Bold white, top at y=300, see [production-rules § 5](production-rules.md#5-frame-layout-illustration-only-text-in-code)).
- The approval sample frame for part 1 is composited with `scripts/video/preview_frame.py` (same fonts and positions as the editor), never generator-drawn text.

## Transitions
- **Slow and themed to the mood**, never quick generic dissolves: watercolor paper tearing in two, ink bloom, brush wipe, golden light (fire / sunrise), cloud or burning-paper wash.
- Scripts: `scripts/video/transition_paper_tear.py`, `scripts/video/transition_ink_bloom.py` (ink / brush / golden), and the watercolor-wash with paper texture built into `build_highlight_wash.py`.
- Paper-colour fade in at the start (10 frames) and out at the end (14 frames).

## Subtitles (style since 2026-10-30)
- **Bold white sans-serif** (Montserrat Bold), **bottom centre, placed low** (about 70% of the height or lower; never covering the main subject), soft black shadow, thin dark stroke, **no box**.
- **3-7 word phrases with hard cuts** (no fades, no pop animation).
- The **currently spoken word is highlighted in ONE bright colour for the whole video**, chosen with the QA bot to contrast with that video's images (Hanging Gardens: cyan `#2EF2FF`; Derinkuyu: cyan via ASS `\k` karaoke). Tell the user in writing which colour and why, and get approval before the edit.
- **Word timing comes from faster-whisper word timestamps** (`scripts/subtitles/whisper_word_times.py`), aligned to the script words; Kokoro tokens are only the fallback.
- **Final check on the FINAL mixed audio**: `scripts/qa/verify_subtitle_sync.py` re-transcribes the rendered MP4 and reports the offset per highlighted word. Target |offset| <= 2 frames at 24 fps, and **never early at sentence starts** (the first word of each line is checked explicitly).
- No em dashes in subtitles.

## Audio mix
- **Narration only. Generator audio is muted** (`CLIP_AUDIO=0`, the default in both editors since 2026-11-09): QA found Flow ambience leaking into the narration gaps on Derinkuyu. `CLIP_AUDIO>0` restores the old ducked ambience only if the user asks for it.
- Final `loudnorm` I=-16 LUFS, TP -1.5 (Hanging Gardens was mixed at -14). QA Gate 4 checks loudness and leaks with `scripts/qa/qa_check.py video --narration`.
- No music.

## Render
- 1080x1920, 24 fps, H.264 CRF 17-18, AAC 192k, `+faststart` (Derinkuyu was rendered at 720x1280 straight from the 720p Flow clips).
- Thumbnail: a clean frame or a Krea pick with the hook text, 1080x1920 JPG, set by the user in YouTube Studio.
