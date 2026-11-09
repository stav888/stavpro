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
