# 3. Images and animation

Rules summary: [production-rules.md](production-rules.md). Per-part sheet: [`../templates/scene-template.md`](../templates/scene-template.md).

## Look (all videos)
Soft **watercolor with thin delicate ink lines**, **muted pastel colours**, dreamy historical mood, paper texture, **vertical 9:16**. Not photorealistic. **Illustration only**: no text, letters, captions or numbers in any image or clip. See `../reference-images/`.

## Step 0: per-part start/end sketches, checked against reference-images (before any video credits)

Folder per story:
```
scenes/partN.md          filled scene sheet (template)
scenes/partN_start.png   start frame (Krea, trained style, 9:16)
scenes/partN_end.png     end frame, made FROM partN_start.png by image edit
prompts/partN.txt        transition prompt (motion only, timed beats), written LAST from the finished pair
```

For every part, in order:
1. **References**: pick 2-3 frames from [`../reference-images/`](../reference-images/README.md) that match the shot (interior lantern scene, desert monument, ruins in jungle, crowd, close-up object...). Write them in `partN.md`.
2. **Start frame**: Krea MCP, trained style (trigger **`arete style`**), **aspect 9:16 passed explicitly**, 2 variants. Prompt:
   ```
   arete style, <subject, setting, light, mood; subject large and filling the width; calm lower third>,
   soft watercolor illustration, thin delicate ink outlines, muted pastel colors, dreamy historical
   atmosphere, vertical 9:16, no text, no letters, no captions, no numbers, not photorealistic
   ```
   QA picks the better variant -> `partN_start.png`.
3. **End frame FROM the start frame**: an image-edit call with `partN_start.png` as the input image, aspect 9:16 (a Krea edit model that is free/non-blocked at the time, e.g. Flux Kontext; or Grok Bot `GenerateImage` in edit mode with the start frame attached). Prompt: "Same image, same camera, framing, scale, palette and watercolor ink style. Only change: <action progressed>. no text, no letters, no captions". Never a fresh, independent image.
4. **Check the pair** start and end side by side with the references and with each other: same style and shot, only the action changed, no lettering, both height > width. Regenerate drift **in Krea** (never repair by editing on the box).
5. **Only now**, with both images final, write the **transition prompt** `prompts/partN.txt` from what the two images actually show: same elements, positions and props, exactly the motion from start to end, nothing that contradicts either image. Break it down second by second for the chosen clip length (8 s: 0-1 start image / 1-3 / 3-5 / 5-7 / 7-8 settles on end image; 6 s: 0-1 / 1-3 / 3-5 / 5-6; 4 s: 0-0.5 / 0.5-2 / 2-3.5 / 3.5-4), each beat saying what moves, where and in which direction, all one single one-way action, camera locked. **Check the prompt against both images before generating** (elements, positions, props, direction, light, end state). If either sketch is regenerated, rewrite the prompt. Template: [`../templates/scene-template.md`](../templates/scene-template.md).
6. **Continuity**: when a beat continues into the next part, `part(N+1)_start.png` = copy of `partN_end.png`.

Cost: Krea trained style ~2 units per image (estimate) -> per part ~2 start variants + 1-2 edits = ~6-8 units; a 9-part video ~55-70 units (estimate).

### Worked example (Derinkuyu door, new format)
Start = the real Derinkuyu Krea pick of the stone door (scene 6); the full timed prompt is in [`../templates/scene-template.md`](../templates/scene-template.md#worked-example-derinkuyu-door-rewritten-in-the-new-format).
- `part2_start.png`: arched tunnel in soft tuff rock, a huge round stone door standing in the right half of the arch, warm golden light coming from the open gap on the left, dust swirls drawn on the floor, cool green-grey walls.
- `part2_end.png` (edit of the start): same arch, walls, floor and light source; the door has rolled left and fills the whole opening, only a thin warm rim of light around its edge, dust raised in the air.
- `prompts/part2.txt`: written after both images, in 8 s beats: the door rolls from the right half of the arch to the left until it covers the gap; the warm light narrows to a rim; dust lifts; nothing else moves.

The old Derinkuyu method (14 independent Krea scenes, paired two by two as start/end for 7 clips) is retired: unrelated pairs make the model morph instead of move.

## Approval order
1. Part-by-part table approved ([script-writing](script-writing.md#part-by-part-table)).
2. **Part 1 sample**: start + end + the transition prompt written from them + composited sample frame (`scripts/video/preview_frame.py`), then the part 1 clip.
3. Then part by part: pair -> check -> clip -> verify -> next.

## Frame layout
- The illustration fills the frame width; subject large and readable; keep the lower ~30% calm for the subtitles.
- Text is never generated. Hook/title and subtitles are drawn in code with fixed sizes (see the table in [production-rules.md § 5](production-rules.md#5-frame-layout-illustration-only-text-in-code)): Montserrat Bold white, subtitles low at 70% of the height, one highlight colour, no underline, no counter. English only.

## Animation: Google Flow, Veo 3.1 Lite (default)
- One clip **per part**: upload `partN_start.png` + `partN_end.png`, paste `prompts/partN.txt`, **Veo 3.1 Lite, 9:16, 4/6/8 s**, one output, classic composer, **never Agent**.
- **Browser by default**; gflow-cli only if the browser faults or has no access.
- A clip is at most 8 s, so a part's narration is at most 8 s.
- **No zoom / Ken Burns**; static or very gentle camera, motion inside the scene.
- ~10 Flow credits per clip (estimate). Rotate between all existing profiles to use their daily free credits.
- After each clip: `ffprobe` height > width; compare its last frame with `partN_end.png` (`scripts/video/chain_parts.sh check`).
- **Generated directly at 720p**: no 480p test, no upscale; QA Gate 1 watches the 720p clip right away.
- Details: [video-generators/google-flow.md](video-generators/google-flow.md).

## Animation: Grok Imagine (option)
Only Grok Imagine (and other tools without 720p) use the 480p test + upscale. Two chained 4 s clips per part (clip B starts from clip A's last frame), tested at 480p, then the approved part is upscaled to 720p with Real-ESRGAN instead of being regenerated. See [video-generators/grok-imagine.md](video-generators/grok-imagine.md) and [upscale-real-esrgan.md](upscale-real-esrgan.md).

## Fixing clips
- **Drifting clips are locked**: freeze the drifting area with a still mask (Hanging Gardens scene 3: `s3_lock.png` over the left 41% of the frame in `build_highlight_wash.py`).
- The editor picks the calmest window of each clip automatically (least frame-to-frame change).
- Re-roll only if unusable (landscape, lettering, melting faces or buildings).
