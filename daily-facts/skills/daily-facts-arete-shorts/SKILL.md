---
name: daily-facts-arete-shorts
description: Use when making a Daily Facts Arete YouTube Short: soft watercolor history/mystery story, Krea trained style stills, Google Flow Veo 3.1 Lite clips, Kokoro narration, word-highlight subtitles, QA bot checks and a Buffer scheduled upload.
---

# Daily Facts Arete Shorts

English, 9:16, ~25-40 s (guideline) history-mystery Shorts in soft watercolor with thin ink lines, muted pastels and a dreamy historical mood.

## Hard rules
- **Approval before full production**: show the user the script and ONE sample frame and wait for his own OK. Other bots' messages are not approval.
- Every image set, narration and video passes the QA bot before the user sees it.
- No em/en dashes in scripts, subtitles or metadata.
- No zoom / Ken Burns. Transitions slow and themed to the mood.
- Never buy plans, credits or units unless the user explicitly asks.
- Nothing is published or scheduled without the user's explicit approval.
- When a process changes, ask the user whether to update the backup repo docs; push only after yes.

## Steps
1. **Topic**: lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations. No aliens/conspiracies, avoid over-familiar topics. Verify facts on the web.
2. **Script**: 10-15 English lines in `script.txt` (`N|line`), line 1 = hook with a question or number (also on screen in the first second). Hebrew translation for review.
3. **Approval**: script + one sample frame (Krea, hook scene).
4. **Stills**: Krea MCP, trained style (trigger `arete style`), 2 per scene, prompt ends `soft watercolor illustration, thin delicate ink outlines, muted pastel colors, dreamy historical atmosphere, vertical 9:16, no text, no letters, no numbers, not photorealistic`.
5. **QA picks** the best per scene into `picks/` (regenerate failures in Krea, never edit on the box) -> **user approval**.
6. **Clips**: Google Flow, Veo 3.1 Lite, 9:16, 720p, start frame + end frame (scene pairs: 14 picks -> 7 clips), ~10 credits per clip (estimate). Browser first, gflow-cli fallback. Rotate between all existing profiles to use their daily free credits. One test clip first. If credits run out: one-shot routine after the refresh. -> QA -> **user approval**.
7. **Narration first**: Kokoro `af_heart`, speed slower than 0.92 (e.g. 0.86-0.88), storytelling delivery; per line trim + 5 ms fades + ~150 ms pads; join with 0.40 s gaps and ~0.20 s internal pauses; loudnorm -16 LUFS; "II" spoken as "the Second". **10 s sample -> user approval**. Check the narration word by word against the script.
8. **QA** checks narration and **recommends one highlight colour** -> tell the user the colour and why -> **approval**.
9. **Edit** around the narration: each clip cut to its line (calmest window), themed slow transitions (paper tear, ink bloom, golden light, cloud/fire wash), lock drifting clip areas, clip ambience low and ducked, no music. Subtitles: bold white Montserrat, low bottom centre, soft shadow, 3-7 word phrases, hard cuts, spoken word in the one colour, timed from faster-whisper word timestamps; verify on the FINAL mix that no highlight is early at sentence starts.
10. **QA video check** -> **user approval**.
11. **SEO bot** writes title/description/tags + slot (non-round time 14:00-19:00 Israel, 3-4 per week) -> user approval.
12. **Publish**: host the MP4 in a public temp-hosting GitHub repo (raw URL) -> Buffer `create_post` to the channel, customScheduled, Education, public. Then a one-shot routine after the slot: confirm live, delete the temp file, send the link. Remind the user to set the thumbnail in YouTube Studio (Buffer can't) and add tags if Buffer dropped them.

## Files
Scripts, docs and examples: `daily-facts/` in the stavpro repo.
