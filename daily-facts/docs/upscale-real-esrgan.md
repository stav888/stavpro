# Upscale an approved clip to 720p (Real-ESRGAN)

Script: [`../scripts/video/upscale_720p.sh`](../scripts/video/upscale_720p.sh) (standalone; any vertical clip from any generator: Grok Imagine 480p tests, a low-res Krea clip, an old 400x736 Grok clip, etc.).

## When
- The clip **already passed QA** (motion, watercolor look, 9:16, no text) and only needs more resolution.
- Same motion is wanted. Regenerating at 720p gives a different take, so it would need QA and approval again.

## When not
- The upscale smears the thin ink lines, turns washes plastic or adds ringing -> regenerate at the generator's native 720p and run QA again.
- The clip failed QA for motion or style: upscaling does not fix drift, morphing or jumps.

## How it works
1. Rejects anything that is not vertical (height > width).
2. Real-ESRGAN x4 with **realesr-animevideov3** (illustration video model, default) or `ESRGAN_MODEL=general` (realesr-general-x4v3) if the anime model flattens the watercolor too much.
3. Lanczos to exactly **720x1280** (cover + centre crop).
4. **Paper-texture blend**: `PAPER_MIX` (default 0.25) of a plain lanczos upscale of the source is mixed back in, so the paper grain and soft pigment edges of the Arete style survive. 0 = pure ESRGAN; 0.35-0.4 if washes look plastic.
5. x264 CRF 16, same fps, original audio kept.

Back ends:
- **CPU / PyTorch** ([`../scripts/video/esrgan_cpu.py`](../scripts/video/esrgan_cpu.py)): what the box uses, because it has no Vulkan driver. ~0.7 s per 270x480 frame on the box, so an 8 s part at 24 fps takes ~2-3 min (estimate).
- **realesrgan-ncnn-vulkan** (fast): used automatically when `ESRGAN_BIN` points to it and a Vulkan driver works; otherwise the script falls back to CPU.

```bash
ESRGAN_WEIGHTS=/path/to/weights PYTHON=/path/to/venv/bin/python \
  scripts/video/upscale_720p.sh gen/part3_480.mp4 gen/part3_720.mp4
# options: ESRGAN_MODEL=general  PAPER_MIX=0.35  ESRGAN_BIN=/path/realesrgan-ncnn-vulkan
```
Tested on the box on 2026-11-09 with a 270x480 cut of a Derinkuyu clip: 24 frames in ~17 s, output 720x1280, ink lines visibly sharper than a plain lanczos resize.

## Verify
`ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 out.mp4` -> `720,1280`. Look at a mid frame and the last frame next to the 480p source: lines sharp, washes still soft, no halos. Then a short QA sharpness check.

## Install
See [`../requirements/system-deps.md`](../requirements/system-deps.md): PyTorch (CPU) + the two `.pth` weights from the Real-ESRGAN release, or the ncnn-vulkan binary with its `models/` folder. Licence: Real-ESRGAN BSD-3-Clause; for the ncnn-vulkan build GitHub shows no SPDX licence id, so check its repo before redistributing.
