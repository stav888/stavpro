# 3. Images and animation

## Look (all videos)
Soft **watercolor with thin delicate ink lines**, **muted pastel colours**, dreamy historical mood, paper texture, **vertical 9:16**. Not photorealistic. No text in any image. See `../reference-images/`.

## 3a. Stills: Krea, trained style "Daily Facts Arete Watercolor"
- Every still comes from the trained Krea style (trigger word **`arete style`**), trained on 30 frames of the channel's original videos on Krea 2 Medium. Generated through the **Krea MCP connector** (model `krea-2 medium-turbo` with the style attached), saved to `<story>/krea/sNN_v1.png`, `sNN_v2.png`, with the Krea URLs in `urls.txt`.
- **2 images per scene**. Prompt pattern (from `../examples/derinkuyu/prompts.txt`):
  ```
  arete style, <scene: subject, setting, light, mood>, soft watercolor illustration, thin delicate ink outlines,
  muted pastel colors, dreamy historical atmosphere, vertical 9:16, no text, no letters, no numbers, not photorealistic
  ```
  Add negatives in words when needed ("no wood no wooden door", "underground depth not a surface map").
- Do not make sketches fresh in Grok Imagine or other generators: the trained style keeps the channel look consistent.
- **If an image fails QA, regenerate it in Krea**; do not repair it with crops or colour grading on the box (too costly in usage).
- Cost: ~2 Krea units per image (estimate), so ~56-60 units for 14 scenes x 2.

## 3b. QA pick and approval
- The QA bot gets per-scene contact sheets (`<story>/qa/sNN_sheet.jpg`, both variants side by side + the line text) and picks the best, or asks for a regeneration (`sNN_rsheet.jpg` = regenerated round).
- Picks are copied to `<story>/picks/sNN.png`.
- **User approval** of all picks before any paid animation.

## 3c. Animation (current): Google Flow, Veo 3.1 Lite
- One clip per **pair of scenes**: odd pick = start frame, even pick = end frame (14 scenes -> 7 clips).
- **Veo 3.1 Lite, 720p, 9:16**, 8 s, one output, classic composer.
- Motion prompt per clip (`motion_prompts.txt`, `NN|prompt`): slow, gentle, one direction, "watercolor", "no text". Example: `Massive round stone door rolls shut along its groove to seal the tunnel like a vault, dust drifts, close soft camera hold, watercolor ink lines steady, no text`.
- **No zoom / Ken Burns** (rule since 2026-10-24): static or very gentle camera, motion inside the scene.
- ~10 Flow credits per clip (estimate). Daily free credits: rotate between all existing profiles to use their daily free credits.
- **One test clip first**, show it, then the rest (avoid wasting credits).
- **User approval** of the clips.
- Details and fallbacks: `video-generators/google-flow.md`.

## 3d. Fixing clips
- **Drifting clips are locked**: if part of a clip drifts or morphs badly, freeze that area with a still mask (Hanging Gardens scene 3: `s3_lock.png` blended over the left 41% of the frame in `build_highlight_wash.py`).
- The editor picks the calmest window of each 8 s clip automatically (least frame-to-frame change).
- Re-roll a clip in Flow only if it is unusable (wrong aspect, text appears, faces melt).

## Earlier animation routes (used before Flow)
- **Grok Imagine** (Grok Bot `GenerateVideo`, or the user animating in Grok Chat with per-scene prompts I write): Prague v3, Petra, Alexandria. See `video-generators/grok-imagine.md`.
- **Krea video (LTX)**: planned as the main clip source in Oct 2026; see `video-generators/krea.md`.
