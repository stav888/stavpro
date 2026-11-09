# System dependencies

| What | Version used | Install |
|---|---|---|
| ffmpeg / ffprobe (libx264, aac, loudnorm) | 7.1.5 (Debian 13) | `sudo apt-get install -y ffmpeg` |
| Python | 3.11 (TTS), 3.12 (Kokoro), 3.13 (video/QA) | `uv python install 3.11 3.12 3.13` |
| uv | any recent | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| git + gh CLI | gh logged in as the repo owner (scopes: repo) | `gh auth login` |
| Font: Patrick Hand (OFL) | Regular | Google Fonts: https://fonts.google.com/specimen/Patrick+Hand -> set `PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf` |
| Real-ESRGAN ncnn-vulkan | latest portable | [releases](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases); keep `models/` beside the binary; `export REALESRGAN_BIN=/path/realesrgan-ncnn-vulkan`. Standalone guide: [`../docs/upscale-real-esrgan.md`](../docs/upscale-real-esrgan.md) |

## Model weights (download, never commit)
| Model | Source | Licence | Used for |
|---|---|---|---|
| Chatterbox TTS | HF `ResembleAI/chatterbox` (auto-downloaded by `ChatterboxTTS.from_pretrained`) | MIT | narration |
| Kokoro-82M (voice `am_eric`) | HF `hexgrad/Kokoro-82M` | Apache-2.0 | 1 reference clip for Chatterbox cloning |
| faster-whisper `small` | HF `Systran/faster-whisper-small` (auto) | MIT | word timestamps / first-word QA |
| RIFE 4.7 `rife47.pth` | HF `jasonot/mycomfyui` file `rife47.pth` -> `export RIFE47_WEIGHTS=/path/rife47.pth` | MIT (RIFE) | 24 fps one-way retime, jolt fixes |
| RIFE arch code | `git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation /tmp/cfi` (commit 26545cc2dd95bc3d27f056016300673bdeee78f5) -> `export CFI_RIFE_DIR=/tmp/cfi/vfi_models/rife` | MIT | `rife_arch.IFNet` |
| Real-ESRGAN `realesr-animevideov3` | bundled with ncnn-vulkan `models/` (or [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) weights) | **BSD-3-Clause** (Real-ESRGAN) | Local 480p→720×1280 upscale (`scripts/video/upscale_720p.sh`); see [`../docs/upscale-real-esrgan.md`](../docs/upscale-real-esrgan.md) |

Download RIFE weights: `hf download jasonot/mycomfyui rife47.pth --local-dir ./weights`
