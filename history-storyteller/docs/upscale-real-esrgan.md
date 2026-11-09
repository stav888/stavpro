# Real-ESRGAN upscale to 720×1280 (standalone)

Use this on **approved vertical clips whose native output is below 720p** — primarily **Grok Imagine**, and other tools (some Krea / HF models) with max output under 720p — when you want 720p without regenerating the motion.

> **Not for Google Flow.** Veo 3.1 Lite already generates at **720p**. Flow has **no 480p test** and **no Real-ESRGAN step**; QA watches the 720p clip immediately ([`video-generators/google-flow.md`](video-generators/google-flow.md)).

Licence: **Real-ESRGAN** is **BSD-3-Clause** ([xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)). The portable `realesrgan-ncnn-vulkan` binary is MIT ([xinntao/Real-ESRGAN-ncnn-vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan)); we list Real-ESRGAN (BSD-3) in the base-repos table.

## When to use
- A 480p (or other sub-720) clip **already passed QA** (motion, style, 9:16, no text) and you want sharper delivery frames.
- You want the **same motion**, only higher resolution.

## When **not** to use / regenerate instead
- Upscale looks soft, mushy, ringing, or breaks line art → **regenerate** at the generator's native 720p (or Flow/Krea equivalent), then full QA again.
- The clip failed motion/style QA → fix the take first; upscaling will not fix jumps, loops, or style drift.
- Do **not** regenerate at 720p just to “match” an approved 480p take — a new generation is different motion. Prefer local upscale first.

## Model choice
- **Default for Xiaohei / illustration Shorts:** `realesr-animevideov3` (anime/illustration video model).
- Avoid general photo models (`realesrgan-x4plus`) for these drawings unless testing.

## Install
See also [`../requirements/system-deps.md`](../requirements/system-deps.md).

**Preferred (portable Vulkan binary, no Python GPU stack):**
```bash
# Example Linux: download the latest realesrgan-ncnn-vulkan release zip from
# https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases
# unzip somewhere permanent, ensure the `models/` folder sits next to the binary.
export REALESRGAN_BIN=/path/to/realesrgan-ncnn-vulkan
# binary must be on PATH, or set REALESRGAN_BIN every run
```

**Python alternative (optional):**
```bash
pip install realesrgan basicsr
# then use xinntao's inference_realesrgan_video.py with -n realesr-animevideov3
# The shell helper below expects the ncnn-vulkan binary by default.
```

Needs: `ffmpeg` / `ffprobe` (already in system-deps).

## Standalone script
[`../scripts/video/upscale_720p.sh`](../scripts/video/upscale_720p.sh) — input any MP4 → **720×1280** MP4. Keeps audio if present; preserves source fps; scales after ESRGAN so the canvas is exactly 720×1280.

```bash
# From a story folder or with absolute paths:
./scripts/video/upscale_720p.sh gen/part3.mp4 gen/part3_720p.mp4

# Or via the chain helper's upscale subcommand (same script):
./scripts/video/chain_and_upscale.sh upscale gen/part3.mp4 gen/part3_720p.mp4

# Env overrides:
REALESRGAN_BIN=/path/realesrgan-ncnn-vulkan \
REALESRGAN_MODEL=realesr-animevideov3 \
REALESRGAN_SCALE=2 \
  ./scripts/video/upscale_720p.sh clip_480.mp4 clip_720.mp4
```

`REALESRGAN_SCALE` is the internal ESRGAN factor (2/3/4, default 2). Frames are then `scale=720:1280` so the deliverable size is fixed.

## Verify
```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,codec_name \
  -of default=noprint_wrappers=1 clip_720.mp4
# expect: width=720  height=1280
```
Visual: open a mid frame and the last frame; line art should stay sharp (not smeared). If soft/broken → regenerate at native 720p + full QA.

## After upscale
**QA stage 2** — send the 720p file to **QA סרטונים** for a short **sharpness** check ([`qa.md`](qa.md)). Then continue: RIFE 24 fps retime (`scripts/video/rife_eq.py`), jolt fixes, `build.py` into 1080×1920, **QA stage 3** on the full video.

## Grok Imagine chain
For Grok's two×4 s chain, join first, QA the 480p join, then upscale — see [`video-generators/grok-imagine.md`](video-generators/grok-imagine.md) § Per-part chained workflow. `chain_and_upscale.sh` calls this upscale script.
