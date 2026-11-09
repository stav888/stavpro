# פעולות (actions bot)

**Role:** executes long or browser-heavy jobs so the producer bot stays free: generating the Flow clips in the box Chrome (or with gflow-cli as fallback), downloading results, and running assembly helpers on request.

## Handoff
- I send: the story folder, the locked picks (`picks/sNN.png`), `motion_prompts.txt`, the exact settings (Veo 3.1 Lite, 9:16, start + end frame, 1 output, classic composer, no Agent), the clip pairing (14 images -> 7 clips), and "rotate between all existing profiles to use their daily free credits; never buy credits".
- It returns: `clips/clipNN.mp4` + a short log (which clips succeeded, credits left, errors).
- If credits run out it stops and reports; a one-shot routine continues after the daily refresh.

## Rules
- It never publishes or changes the script, picks or metadata.
- Clips go to QA, then to the user, before the edit.
