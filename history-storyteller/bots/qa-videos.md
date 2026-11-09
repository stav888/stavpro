# QA סרטונים (video QA bot)

- **Agent id:** `3596d23d-e7aa-48cf-b8a1-91e84bcfa678`
- **Role:** an independent pass/fail check of every Short before it reaches the user. It is read-only: it never fixes or publishes anything.
- **Profile (verbatim, Hebrew):** בודק איכות (QA) לסרטוני ה־Shorts של ערוץ Smart History Knowledge לפני פרסום. בודק שמע: שכל מילה ראשונה בכל משפט/קטע נשמעת מלאה ולא חתוכה, שהקריינות רציפה והמשכית ולא נשמעת כמו קטעים נפרדים, שאין שתיקות ארוכות או קפיצות עוצמה במעברים. בודק כתוביות: נעולות למשפט הנאמר, בלי חציית גבולות ובלי שורות יתומות קצרות. בודק אנימציה בצפייה בפריימים/בסרטון: תנועה חד־כיוונית מתקדמת בלי לולאה, בלי פינג־פונג, בלי הקפאה ובלי זום, ושהתמונה מתאימה למשפט הנאמר באותו רגע ובסדר כרונולוגי. מחזיר דוח קצר בעברית: עבר/לא עבר לכל בדיקה, עם זמנים מדויקים של תקלות אם נמצאו. לא מתקן ולא מפרסם בעצמו — רק בודק ומדווח.

## Inputs (from the producer, via SendToAgent)
- Absolute box path of the final MP4.
- Version number and the list of changes since the last version.
- The previous version's path, for the regression diff.
- Sometimes the sentence list or timing table.

## Step by step (as seen in its report folders `/workspace/qa-<project>-vN/`)
1. **Format:** ffprobe (resolution, fps, codecs, duration). Loudness: integrated LUFS, true peak, clipping.
2. **Audio extraction:** 16 kHz WAV, then ASR with **faster-whisper small and base**, word timestamps.
3. **First words, per sentence:**
   - "low onset" = first non-zero sample after digital silence.
   - "strong onset" = first 5 ms window with RMS ≥ -25 dB (also checked at -20 dB).
   - RMS is measured over 0–50, 50–100 and 0–400 ms.
   - ASR word confidence is checked for the first word.
4. **Pauses:**
   - `silencedetect` at -35/-40/-50 dB, measuring gaps between and inside sentences.
   - Between-sentence pauses should be ~0.42–0.45 s.
   - A pause inside a sentence much longer than a comma (Wojtek v5: 1.08 s) is a **fail**.
5. **Loudness jumps:** per-sentence RMS should stay in a narrow band (e.g. -18.5…-20.7 dB). Audio MD5 is compared with the previous version: it must be identical if the audio wasn't meant to change.
6. **Subtitles:**
   - Changes in the caption band are detected per frame (crop around y 1050–1550, threshold of 1% mean difference).
   - Each change is compared with the sentence onsets; deviation must be ≤ ~0.07 s.
   - No crossing sentence boundaries, no blank caption inside a sentence, no short orphans.
7. **Animation:**
   - `freezedetect` -60/-50 dB, d=0.5 s: no freezes.
   - Motion difference per 0.5 s: no "dead" half-seconds.
   - Montage at 1 fps and 3 fps: order and match to the subtitles.
   - Duplicate/static frame runs, ping-pong/loop detection, single-frame jolts.
   - Zoom check with SIFT + RANSAC scale between the first and last frame of each scene (must be 0%: no zoom).
   - Seams at splices, using zoomed crops (e.g. `s4dot_zoom.png`, `medals_zoom.png` in qa-garbo-v5/v8).
8. **Regression diff:** per-frame difference against the previous version (e.g. `cmp.py` → `cmp.json`, with the caption band masked). Changes must fall only in the intended frame range.
9. **Report:** a short Hebrew report with ✅/❌ per area and exact timestamps or frame numbers for every fault, ending with a narrow fix suggestion.

## Thresholds (from real reports)
| Check | Pass |
|---|---|
| First-word attack | strong onset ≤ 50–80 ms after the low onset; no missing or cut first word in ASR |
| Between-sentence pause | ~0.4–0.45 s, consistent |
| Pause inside a sentence | none clearly longer than a comma pause (~0.3–0.6 s); 1.08 s failed |
| Loudness | ~-16 LUFS integrated, true peak ≤ -1.0 dBTP, no clipping |
| Subtitle change vs onset | ≤ ~0.07 s; 0 boundary crossings |
| Freeze | freezedetect finds 0 events ≥ 0.5 s |
| Zoom (History) | none (SIFT scale ≈ 0) |
| Audio between versions | identical MD5 unless audio was changed on purpose |

## Output format (real example, translated and shortened: Wojtek v5)
> ffprobe 39.30 s, 1080x1920, integrated -16.13 LUFS, no clipping.
> First words, 8 sentences: all strong onsets within 0–55 ms → ✅. Pauses between sentences 0.42–0.45 s → ✅. Subtitles: changes within ~0.07 s of the onsets → ✅. Animation: 0 freezes, minimum motion 0.0053 → ✅.
> **New fault:** a 1.08 s silence *inside* sentence 8 ("died" … "In 1963"), ~2.4× the normal pause. ASR splits it into two sentences → ❌.
> **Verdict: FAIL, not approved for delivery.** Narrow fix: re-make or edit only sentence 8, so the pause becomes a ~0.3–0.4 s comma, without touching the "He" onset; then re-check sentence 8 only.

The producer fixed it (v6), and QA passed. Garbo went through v1–v9 the same way.

## Rules
- Read-only: it never edits, re-renders, uploads or publishes.
- Verdicts are information for the producer, not user approval.
- Never invent measurements. Every fault has a timestamp.

## Recreate
Create a Grok Bot named "QA סרטונים" with the profile above, and install `../requirements/requirements-video.txt` plus ffmpeg on the box. Give it `../docs/qa.md`, `../scripts/qa/`, and the thresholds table above.
