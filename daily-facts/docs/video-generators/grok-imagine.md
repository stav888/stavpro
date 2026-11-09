# Grok Imagine

Used for image-to-video **before Flow** (Oct 2026): Prague v3, Petra, Alexandria.

## How it was used
1. **Bot-generated** (Grok Bot `GenerateVideo`): each approved Krea still (flat, front-facing composition works best) animated to a 720p, 5-6 s clip with a gentle one-direction motion prompt. The user liked this result (Prague v3).
2. **User-animated** (to save bot usage): I place the approved stills in scene order in a new, unanimated Grok Imagine canvas named for the video, in one vertical column with scene labels, and write one detailed animation prompt per scene that the user copies; he animates them himself and sends back the clips, and I assemble them.

## Settings
- Input: the approved Krea still, 9:16. Output 720p, 5-6 s; trimmed to the line length (an older rule capped every scene at 3 s; the narration-first edit now sets the length).
- No zoom; static camera with gentle in-scene motion; `no text`.

## Cost (estimate)
Uses the Grok Bot subscription: a full video with bot-made clips used about 10% of a monthly plan, which is why the pipeline moved to Flow's free daily credits.

## Per-part chained workflow (option, from 2026-11-09)
Use when Flow credits are out or a part needs Grok's motion. Inputs are the same Step 0 pair (`partN_start.png`, `partN_end.png`) and transition prompt.

1. **Clip A, 4 s, 480p, 9:16** from `scenes/partN_start.png`. Prompt: the first half of the motion toward the end state + `static locked camera, no zoom, no pan, soft watercolor and thin ink lines stay steady, no text, no letters, no captions`. Save `gen/partN_a.mp4`.
2. **Last frame of A**: `scripts/video/chain_parts.sh last gen/partN_a.mp4 gen/partN_a_last.png`.
3. **Clip B, 4 s, 480p, 9:16** from `gen/partN_a_last.png`: continue the same one-way motion to the end state. Save `gen/partN_b.mp4`.
4. `partN_end.png` is the **check target only** (never a separate i2v start, which would leave a jump at 4 s).
5. **Join**: `scripts/video/chain_parts.sh join gen/partN_a.mp4 gen/partN_b.mp4 gen/partN_480.mp4` (drops B's duplicate first frame), then `chain_parts.sh check gen/partN_480.mp4 scenes/partN_end.png`.
6. **QA at 480p**: seam continuity, watercolor look kept, no drift, 9:16, no text.
7. After QA passes, **upscale instead of regenerating**: `scripts/video/upscale_720p.sh gen/partN_480.mp4 clips/partN.mp4` (Real-ESRGAN, 720x1280, paper-texture blend; [guide](../upscale-real-esrgan.md)). Regenerate at 720p only if the upscale smears the ink lines.

Cost (estimate): two short 480p generations per part on the Grok Bot plan; cheaper than one 720p take and the 480p test can be thrown away without much loss.
