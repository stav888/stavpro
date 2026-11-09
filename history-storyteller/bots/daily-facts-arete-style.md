# Daily Facts Arete Style (sibling video bot)

- **Agent id:** `bd551ec7-720a-4ef7-a863-9e91cc0bf76c`
- **Role:** vertical 9:16 history-mystery Shorts in a "Daily Facts Arete" look. Not part of the History Storyteller pipeline, but it shares the box, the hosting repo and (likely) the QA bot.
- **Profile (verbatim, Hebrew):** יוצר סרטוני YouTube Shorts אנכיים (9:16) בסגנון Daily Facts Arete: איורי watercolor עדינים עם קווי דיו דקים, צבעים פסטליים מושתקים, אווירה היסטורית-חלומית. נושאים של מסתורי היסטוריה, אירועים עתיקים, פירמידות, הרי געש וכו'. מעברי אנימציה רכים בסגנון מברשת צבע / watercolor dissolve, זום איטי עדין (Ken Burns). קריינות דרמטית באנגלית, כתוביות, טקסט על המסך. אורך ~30-60 שניות. מיועד לערוץ בסגנון Daily Facts Arete.

## How it works (from memory notes and box folders)
- **Style:** watercolor + thin ink, muted pastels, soft watercolor-dissolve transitions, slow Ken Burns zoom (allowed here, unlike History). English narration, subtitles, on-screen text, ~30–60 s.
- **Voice:** a Kokoro male voice. It's the reason the History bot first picked Kokoro (memory, 2026-10-30).
- **Video method from 2026-11-04 (memory):**
  - `gflow-cli` on the box with **Veo 3.1 Lite**, 720p 9:16. Each clip uses a start and an end image and costs 10 Flow credits.
  - 14–20 images, i.e. 7–10 clips, per video. Assembled with narration, subtitles and crossfades.
  - Uses about 7–10% of the Grok Bot plan per video.
- **Hosting:** `stav888/video-hosting/daily-facts-arete-style/`, removed after publish (commit "cleanup: remove temp derinkuyu after Buffer publish").
- **Upload metadata:** `/workspace/arete/*/yt_meta.md`, `/workspace/arete/derinkuyu/up/meta.json`.
- **QA:** reports in `/workspace/qa-arete-*/report-he.md` use the same format as QA סרטונים (e.g. dancing1518 v4: video ✅, audio ❌ because true peak was -0.2 dBTP vs the -1.0 target).
- **Weekly plan (memory):** 2–3 Daily Facts videos + 4 history videos.

## Rules (shared)
Only the user approves publishing. No purchases. Never click Google Flow's "Agent" button.

Unverified: its full skill set and its exact SEO hand-off (no skill file of its own was found in `/home/box/agent-data/workflows`).
