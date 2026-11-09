# 3. Images and animation

## Style reference
Repo: https://github.com/helloianneo/ian-xiaohei-illustrations (MIT, Ian). Clone it into `<story>/refs/` and pass example images from `assets/examples/` as `reference_image_paths` to every image generation.
- Pure white background, thin wobbly black hand-drawn lines, lots of white space, tiny red/orange/blue accents only.
- Xiaohei: solid black character, white dot eyes, thin legs, blank face. He **performs** the key action of each scene.
- No readable text in images. Regenerate once if text/garbled letters or style drift appear.

## Stills

## Step 0 — sketches according to `reference-images/` (before any video credits)
Before spending image-to-video credits (Flow, Krea, or otherwise):
1. From [`../reference-images/`](../reference-images/) (38 vertical **9:16** frames from 13 Shorts), pick **2–3 relevant refs per scene** and note them by relative path.
2. Generate the start frame (and end frame where the model supports one) with free `GenerateImage`, passing those refs as style references / describing their style. Match white background, wobbly black lines, black Xiaohei doing the action, character size/composition, minimal colour accents. **Always request 9:16 / 1080×1920 — never 16:9.**
3. Check each sketch side by side with the chosen refs and the scene table; regenerate any style drift. Verify height > width.
4. Only then run image-to-video.

- Tool: Grok Bot `GenerateImage` with [`../reference-images/`](../reference-images/) (and/or Ian Xiaohei examples) as `reference_image_paths`. For Flow/Krea sketches, output **vertical 9:16** (e.g. 1080×1920). Older Grok Imagine Garbo stills were 1152×864 JPG per scene (`scenes/sceneN.jpg`) — that landscape size is **not** the target for new Flow/Krea sketches.
- One still per story beat, mapped in a scene table (scene -> sentence numbers). Garbo: 14 scenes = 14 sentence rows in `sentences.txt` (one scene per sentence).

## Image-to-video
> Options: Grok Imagine is the default. Google Flow (Veo) runs via the gflow-cli MCP server on the browser; Krea runs via the Krea MCP connector (browser fallback); Hugging Face Spaces are run directly in the browser; see [`video-generators/`](video-generators/README.md) for the comparison, **Step 0 (sketches according to reference-images)**, and the mandatory **9:16** aspect rules.

- Tool: Grok Bot `GenerateVideo` (Grok Imagine) image-to-video, `image_path=scenes/sceneN.jpg`. Result for Garbo: 640x480, 24 fps, ~7 s (`gen/sN.mp4`).
- One take per scene that covers the whole narration slot (duration = ceil(slot), max 15 s).
- Prompt for slow, continuous, **one-direction** progressive motion, and always state a locked static camera: no zoom, no pan, no push-in.
- Forbidden: loops, ping-pong, reverse, `stream_loop`, freeze/hold >0.3 s, Ken Burns. If a clip is short: regenerate once; never loop it.

## Retime to 24 fps with RIFE (smooth motion the user asked for)
`scripts/video/rife_eq.py <scene numbers>` reads `gen/sN.mp4` and `audio_timing.json`, then writes `anim/sceneN_r.mp4` with exactly slot+3 frames:
- Motion-equalized one-way retime: cumulative frame-difference curve (85%) blended with linear (15%). Positions between source frames are synthesized with RIFE 4.7 (`IFNet(arch_ver="4.7")`, scales `[8,4,2,1]`).
- Never interpolate across a cut, and never between scenes.
- Env: `CFI_RIFE_DIR` (ComfyUI-Frame-Interpolation `vfi_models/rife`), `RIFE47_WEIGHTS` (rife47.pth). See `../requirements/system-deps.md`.

## Fixes
- `jolt_fix.py anim/sceneN_r.mp4 ...`: phase-correlation finds single-frame jolts (shift >0.4 px that returns next frame) and replaces them with RIFE midpoints of the neighbours. Keeps `_prejolt.mp4` backup.
- `fix_frames.py in.mp4 out.mp4 <unused> n1 n2 ...`: replace listed frames with RIFE midpoint of n-1/n+1.
- Late fixes are done by **frame splicing on decoded final frames** (replace only the bad frame range, keep everything else bit-identical) to avoid regressions elsewhere. Small moving details (medals, a dot) were fixed with opaque composites and feathered round masks; a figure mask was built per frame over a clean static background. These were one-off inline scripts, not saved as reusable files.
