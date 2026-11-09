# Lessons learned (Daily Facts Arete)

**Rule (2026-11-09):** after every video, add a short entry here: QA faults, the user's feedback, the fixes, and later the SEO results (views, retention, CTR from the SEO bot's review). **Before starting the next video, read this file and apply the "carry forward" lessons.** Newest entry on top. No private ids or account details.

## Carry forward (current checklist for the next video)
1. No em/en dashes anywhere (script, subtitles, metadata). `make_metadata.py` asserts it; grep the subtitles too.
2. Kokoro af_heart **slower than 0.92**, storytelling punctuation ("...", short sentences), not paragraph-like reading.
3. Join narration with **0.40 s** between lines, **~0.2 s** internal pauses, loudnorm **-16 LUFS**; check every gap, QA flagged gaps of 0.58-0.67 s as too long.
4. Re-listen to line endings: a weak final syllable ("forgotten" heard as "forgot") means re-TTS that line.
5. Subtitles **low, bottom centre**, 3-7 word phrases, never crossing a sentence boundary; highlight timed from **Whisper on the final mix**, checked not early at sentence starts.
6. Transitions **slow and themed** (paper tear, ink bloom, golden light, cloud/fire wash), never quick generic dissolves.
7. **Mute generator audio** (`CLIP_AUDIO=0`); Flow ambience leaked into the narration gaps.
8. Flow clips drift/pan even when asked not to: say "static locked camera, no zoom, no pan" in every transition prompt, measure motion in QA, lock or re-roll.
9. Use start/end **pairs made by editing the start frame** (not independent scenes), so seams are real continuations.
10. Flow clips: generate **directly at 720p** and QA them right away; the 480p test + Real-ESRGAN upscale is only for Grok Imagine / tools without 720p.
11. Publish only via **Buffer** with a temporary public GitHub raw URL, delete it after publish; set thumbnail in YouTube Studio; tags may need adding after approval.

---

## Derinkuyu (published 2026-11-07, https://www.youtube.com/shorts/FbjPMiFmAzw)
Pipeline: 14 Krea scenes (trained style) -> QA picks -> 7 Flow Veo 3.1 Lite clips (scene pairs as start/end) -> Kokoro af_heart 0.92 -> ASS karaoke edit -> Buffer.

| Stage | Fault / feedback | Fix | Lesson |
|---|---|---|---|
| Narration (partial cut, user + QA) | voice liked, but delivery stiff and paragraph-like; gaps 0.8-1.1 s between lines | clearer punctuation/pacing; gaps shortened to ~0.40 s, internal pauses ~0.2 s, loudnorm -16 LUFS (approved by the user 2026-11-06) | `join_narration.py` spec; storytelling punctuation |
| Subtitles (partial cut) | placed too high, mid-screen | moved low, toward bottom centre (~10% from the bottom on the full cut, QA PASS) | subtitles low by default |
| Narration (full cut QA) | 3 gaps still long (0.58-0.67 s) | flagged for the join | check every gap in the report |
| Narration (full cut QA) | "forgotten" (line 10) weak, ASR hears "forgot"; ending felt weak | re-TTS of that line recommended | re-listen to line endings |
| Audio (full cut QA) | **source audio leaking**: Flow clip ambience audible in narration gaps (up to about -27 dB), video loudness -19 LUFS vs -16 target | mute/duck clip audio; normalise the final mix | generator audio muted by default; `qa_check.py video --narration` |
| Subtitles (full cut QA) | line 10 card showed the next sentence while "forgotten" was spoken (card crossing a sentence boundary) | split the card at the full stop | phrase cards never cross sentences |
| Picture (full cut QA) | camera pans/zooms measured in every clip (hundreds of px), not camera-locked | flagged; prompts must lock the camera | "static locked camera" in every transition prompt; measure in QA |
| Picture (Krea) | scene 7 came out as a wooden door instead of a rolling stone door | regenerated with "no wood no wooden door" | negatives in words for known mistakes |
| Flow | gflow-cli runs failed on download (exit 6) and UI drift (exit 23) on some clips | failed clips re-run separately until all 7 existed | browser first, CLI only as fallback |
| Publishing | direct YouTube uploads were being deleted (see Hanging Gardens) | published via Buffer from a temporary public GitHub raw URL, temp file deleted after publish by a one-shot routine | Buffer route |
| After publish | Buffer cannot set a thumbnail; tags may not come through | thumbnail set in YouTube Studio by the user; tags to add after his OK | remind both in the publish message |
| SEO results | early snapshot from the channel page on 2026-11-09: ~518 views | full SEO review **pending** | |

## Hanging Gardens of Babylon (published, https://www.youtube.com/shorts/IpF1nUOSWbY)
Pipeline: Krea stills -> Flow clips -> Kokoro af_heart 0.92 -> Whisper-timed word highlight + watercolor wash (`build_highlight_wash.py`).

| Stage | Fault / feedback | Fix | Lesson |
|---|---|---|---|
| Script / subtitles (user, 2026-10-30) | long em dashes look AI-written | rule: no em/en dashes anywhere; metadata script asserts it (the published subtitles still contain them) | dash check on subtitles too |
| Narration (user) | too fast | rule: Kokoro slower than 0.92 | slower speed |
| Transitions (user) | quick generic dissolves | rule: slow, mood-themed transitions (burning paper, clouds, fire, page tear) | themed transitions |
| Subtitles (QA) | highlight ran early: median -2 frames, only 48% of words within ±2 frames, ~0.2 s early at sentence starts | timing rebuilt from faster-whisper word timestamps; final check on the rendered mix (`verify_subtitle_sync.py`) | Whisper on the final mix, sentence starts checked |
| Picture (QA) | scene 3 slight left-right drift | locked with a still mask (`s3_lock.png`) | lock drifting areas |
| Audio (QA) | loudness -14 LUFS, ambience ducked to ~-35..-40 dB in gaps | accepted then; now -16 LUFS and generator audio muted | |
| Publishing | Composio YouTube uploads were deleted by YouTube within about a minute (twice), and the shared daily upload quota was often exhausted | switched to Buffer + temporary GitHub raw URL | never upload directly; Buffer only |
| SEO results | early snapshot from the channel page on 2026-11-09: ~128 views | full SEO review **pending** | |

## Template for the next entry
```
## <Title> (published YYYY-MM-DD, <link>)
Pipeline: <parts / generator / voice / editor>
| Stage | Fault / feedback | Fix | Lesson |
|---|---|---|---|
| Gate 1 clips | ... | ... | ... |
| Gate 4 full video | ... | ... | ... |
| User feedback | ... | ... | ... |
| SEO results | pending (review due <date>) | | |
```
