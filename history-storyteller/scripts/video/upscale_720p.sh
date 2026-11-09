#!/usr/bin/env bash
# Upscale any vertical Shorts clip to 720x1280 with Real-ESRGAN (realesr-animevideov3).
# Works for clips from any generator (Grok Imagine, Flow, Krea, Hugging Face).
# Usage:
#   ./scripts/video/upscale_720p.sh INPUT.mp4 [OUTPUT.mp4]
# Env:
#   REALESRGAN_BIN   path to realesrgan-ncnn-vulkan (default: realesrgan-ncnn-vulkan on PATH)
#   REALESRGAN_MODEL model name (default: realesr-animevideov3)
#   REALESRGAN_SCALE internal ESRGAN scale 2|3|4 (default: 2); result is then scaled to 720x1280
# Docs: docs/upscale-real-esrgan.md
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 INPUT.mp4 [OUTPUT.mp4]" >&2
  exit 2
fi

IN="$1"
OUT="${2:-${IN%.mp4}_720p.mp4}"
BIN="${REALESRGAN_BIN:-realesrgan-ncnn-vulkan}"
MODEL="${REALESRGAN_MODEL:-realesr-animevideov3}"
SCALE="${REALESRGAN_SCALE:-2}"

if [[ ! -f "$IN" ]]; then
  echo "Input not found: $IN" >&2
  exit 1
fi
if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  echo "ffmpeg/ffprobe required" >&2
  exit 1
fi
if ! command -v "$BIN" >/dev/null 2>&1 && [[ ! -x "$BIN" ]]; then
  echo "Real-ESRGAN binary not found: $BIN" >&2
  echo "Install: see docs/upscale-real-esrgan.md and requirements/system-deps.md" >&2
  exit 1
fi

TMP="$(mktemp -d "${TMPDIR:-/tmp}/upscale720.XXXXXX")"
cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

mkdir -p "$TMP/in" "$TMP/out"

# Preserve source fps for reassemble
FPS="$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$IN")"
HAS_AUDIO="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$IN" | head -1 || true)"

echo "Extracting frames from $IN (fps=$FPS) ..."
ffmpeg -hide_banner -loglevel error -y -i "$IN" -vsync 0 -qscale:v 2 "$TMP/in/frame_%08d.png"

N="$(find "$TMP/in" -name 'frame_*.png' | wc -l | tr -d ' ')"
if [[ "$N" -lt 1 ]]; then
  echo "No frames extracted" >&2
  exit 1
fi
echo "Upscaling $N frames with $BIN -n $MODEL -s $SCALE ..."
"$BIN" -i "$TMP/in" -o "$TMP/out" -n "$MODEL" -s "$SCALE" -f png

# Reassemble at 720x1280; keep audio if present
echo "Assembling $OUT at 720x1280 ..."
if [[ -n "$HAS_AUDIO" ]]; then
  ffmpeg -hide_banner -loglevel error -y \
    -framerate "$FPS" -i "$TMP/out/frame_%08d.png" -i "$IN" \
    -map 0:v:0 -map 1:a:0? \
    -vf "scale=720:1280:flags=lanczos,setsar=1" \
    -c:v libx264 -pix_fmt yuv420p -crf 16 -preset medium \
    -c:a aac -b:a 192k -shortest \
    "$OUT"
else
  ffmpeg -hide_banner -loglevel error -y \
    -framerate "$FPS" -i "$TMP/out/frame_%08d.png" \
    -vf "scale=720:1280:flags=lanczos,setsar=1" \
    -c:v libx264 -pix_fmt yuv420p -crf 16 -preset medium \
    -an \
    "$OUT"
fi

ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate \
  -of default=noprint_wrappers=1 "$OUT"
echo "Wrote $OUT"
