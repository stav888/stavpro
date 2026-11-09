# Hugging Face Spaces — browser workflow

**Primary method: the Space page in the box's Chrome** (signed-in Hugging Face session, for ZeroGPU quota), operated by the bot's browser/desktop agent.

## Spaces
- **Image-to-video:** Wan 2.2 14B I2V + Lightning LoRA, https://huggingface.co/spaces/JCisHERE/wan2-2-i2v-v3
  - Inputs: input image, optional **last image**, prompt, negative prompt, duration (default 3.5 s), steps (default 6), seed / randomize, quality, scheduler, flow shift, frame multiplier, safe mode.
  - Output: 24 fps, dimensions rounded to multiples of 32. The page also has a frame-extract tool, useful for taking the last frame to chain a second clip.
- **Stills (optional):** Z-Image-Turbo, https://huggingface.co/spaces/mcp-tools/Z-Image-Turbo. It offers resolutions including 1152x864 (4:3) and 720x1280 / 1152x2048 (9:16). Xiaohei stills normally come from GenerateImage with the repo references.

## Steps (labels may change)
1. Open the Space page in box Chrome (signed in) and wait until it shows "Running".
2. Upload the start image (`scenes/sceneN.jpg`), plus a last image if you want a fixed end pose.
3. Prompt: one-direction motion, "locked static camera, no zoom, no pan". Keep the default negative prompt (it already discourages static frames and subtitles).
4. Set the duration to fit the slot (short clips are fine, since RIFE retimes them). Leave steps at 6.
5. Generate. If it's queued or the quota is exceeded, wait or stop; don't pay for compute.
6. **Download** the MP4 to `/home/box/Downloads/`, then move it to `/workspace/<story>/gen/sN.mp4`.
7. Continue with RIFE + layout.

## Limits and cost
- Free-ish: runs on ZeroGPU with a per-account daily GPU quota. Long or high-step runs use more quota.
- Queues can be long, and community Spaces can change or go offline.
- Never buy a PRO plan or paid hardware unless the user explicitly asks.

## Secondary note
The same Space tools are reachable through the Hugging Face MCP connector (`gr2_wan2_2_i2v_v3_generate_video`, `gr2_wan2_2_i2v_v3_extract_frame`, `gr1_z_image_turbo_generate`). Use it only if the user asks; the browser is the method.
