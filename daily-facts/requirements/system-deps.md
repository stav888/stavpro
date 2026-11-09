# System dependencies

| Tool | Version on the box (2026-11-09) | Used for | Install |
|---|---|---|---|
| FFmpeg (with libass, libx264) | 7.1.5 | decode/encode, `xfade`, `ass` subtitles, `loudnorm`, `ebur128`, `sidechaincompress`, frame grabs | `sudo apt-get install -y ffmpeg` |
| Python | 3.11 (system), 3.12 (Kokoro venv) | all scripts | `uv` / apt |
| uv | latest | venvs | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| espeak-ng (optional) | not installed on the box | misaki can use it for out-of-vocabulary words; the pipeline ran without it | `sudo apt-get install -y espeak-ng` |
| gh (GitHub CLI) | 2.103.0 | push the MP4 to the public temp-hosting repo for Buffer, delete it after publish, this backup | `sudo apt-get install -y gh` then `gh auth login` (interactive, never store tokens in files) |
| gflow-cli | 0.92.1 | Flow fallback only (headed Chrome on the box display) | `uv tool install gflow-cli` |
| Real-ESRGAN weights `realesr-animevideov3.pth`, `realesr-general-x4v3.pth` | release v0.2.5.0 | `scripts/video/upscale_720p.sh` CPU path (`esrgan_cpu.py`, PyTorch from the Kokoro venv works) | download from https://github.com/xinntao/Real-ESRGAN/releases, set `ESRGAN_WEIGHTS` |
| realesrgan-ncnn-vulkan (optional) | portable binary | fast upscale path, needs a working Vulkan driver (the box has none, so it falls back to CPU) | https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/releases, keep `models/` next to it, set `ESRGAN_BIN` |
| Google Chrome | box browser | Flow web UI (primary), Krea web app (LTX clips) | preinstalled |
| Montserrat (variable TTF) | Google Fonts | subtitles in `build_highlight_wash.py` (env `MONTSERRAT_TTF`) | fonts.google.com/specimen/Montserrat |
| DejaVu Sans | Debian fonts | ASS subtitles in `build_flow_xfade_ass.py` | `fonts-dejavu-core` |

## Models (downloaded on first run)
| Model | Size | Licence | Where |
|---|---|---|---|
| hexgrad/Kokoro-82M, voice `af_heart` | ~330 MB | Apache-2.0 | `KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')` |
| Systran/faster-whisper-small.en | ~480 MB | MIT | per-line word times (`whisper_word_times.py`) |
| Systran/faster-whisper-medium.en | ~1.5 GB | MIT | final sync check on the rendered video (`verify_subtitle_sync.py`) |
| kyutai/pocket-tts (legacy, gated) | - | see model card | old voice clone only |

## Services (no install, connectors or web apps)
- **Krea** (MCP connector + web app): trained style "Daily Facts Arete Watercolor" (trigger `arete style`), images; LTX video in the web app.
- **Google Flow** (labs.google/fx/tools/flow): Veo 3.1 Lite clips.
- **Grok Imagine** (Grok Bot `GenerateVideo` / Grok Chat): image-to-video in the earlier videos.
- **Buffer** (MCP connector): scheduled YouTube upload.
- The Flow path needs no upscaler (720p clips are scaled to 1080x1920 with lanczos in the editor). Real-ESRGAN is only for approved low-res clips from Grok Imagine or other tools without 720p output (480p tests, see `../docs/upscale-real-esrgan.md`).
