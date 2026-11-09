# פעולות (actions bot)

**Role:** executes long or browser-heavy jobs so the producer bot stays free: generating the Flow clips in the box Chrome (or with gflow-cli as fallback), downloading results, and running assembly helpers on request.

## Handoff
- I send: the story folder, the approved per-part pairs (`scenes/partN_start.png`, `scenes/partN_end.png`) and transition prompts (`prompts/partN.txt`, duration 4/6/8 s), the exact settings (Flow web UI in the browser by default, gflow-cli only on browser fault; Veo 3.1 Lite, 9:16 set explicitly, 1 output, classic composer, never Agent), which parts to run (part 1 alone first as the sample), and "rotate between all existing profiles to use their daily free credits; never buy credits".
- It returns: `clips/partN.mp4` (checked height > width) + a short log (which parts succeeded, credits left, errors).
- If credits run out it stops and reports; a one-shot routine continues after the daily refresh.

## Rules
- It never publishes or changes the script, picks or metadata.
- Clips go to QA, then to the user, before the edit.
