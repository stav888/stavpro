# Grok Imagine (default)

- **What:** the Grok Bot built-in `GenerateVideo` tool (Grok Imagine), image-to-video mode.
- **Input:** `image_path` = the approved still (`scenes/sceneN.jpg`, 1152x864 for Garbo). An optional `last_frame_path` pins the end frame. `duration` is 1–15 s, set to cover the scene slot. `resolution` is 480p by default.
- **Output seen on the box:** 640x480, 24 fps, ~7 s clips (`gen/sN.mp4`, inferred from the Garbo files).
- **Prompt pattern:** describe slow, continuous motion in one direction for the scene's action, and always say "locked static camera, no zoom, no pan".
- **Rules:**
  - One take per scene.
  - If a clip is short, regenerate once; never loop it.
  - Using the same image as both first and last frame makes a loop, so never do that.
- **Then:** RIFE retime to the slot (`../../scripts/video/rife_eq.py`), jolt fixes, and layout with `build.py` into 1080x1920.
- **Cost:** counts against the Grok Bot plan (about 8–10% for a ~1-minute video, measured by the user).
