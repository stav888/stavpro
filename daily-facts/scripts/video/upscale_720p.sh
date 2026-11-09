#!/usr/bin/env bash
# Daily Facts Arete: upscale an APPROVED low-res vertical clip (a 480p Grok Imagine test part, or a
# clip from any other generator) to 720x1280 with Real-ESRGAN, keeping exactly the same motion.
# Use it instead of regenerating at 720p (a new generation = different motion).
#
# Two back ends, same result size:
#   1. realesrgan-ncnn-vulkan (fast) if ESRGAN_BIN is set/found AND a Vulkan driver works.
#   2. esrgan_cpu.py (PyTorch on CPU, the one the box uses: it has no Vulkan driver).
# Watercolor note: illustration models smooth flat areas and can erase paper grain and soft pigment
# edges, so PAPER_MIX (default 0.25) of a plain lanczos upscale is blended back in. PAPER_MIX=0 =
# pure ESRGAN; raise to 0.35-0.4 if washes look plastic.
#
# Usage: upscale_720p.sh IN.mp4 [OUT.mp4]
# Env:   ESRGAN_MODEL anime (default, realesr-animevideov3) | general (realesr-general-x4v3, CPU path)
#        ESRGAN_WEIGHTS folder with the .pth weights (CPU path)   PYTHON  python with torch (CPU path)
#        ESRGAN_BIN  realesrgan-ncnn-vulkan binary (models/ next to it)   PAPER_MIX 0..1
set -euo pipefail
IN=${1:?usage: upscale_720p.sh IN.mp4 [OUT.mp4]}
OUT=${2:-${IN%.*}_720p.mp4}
MIX=${PAPER_MIX:-0.25}; MODEL=${ESRGAN_MODEL:-anime}
HERE=$(cd "$(dirname "$0")" && pwd)
command -v ffmpeg >/dev/null || { echo "need ffmpeg" >&2; exit 1; }
IFS=x read -r W H < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$IN")
[ "$H" -gt "$W" ] || { echo "reject: $IN is not vertical (${W}x${H})" >&2; exit 3; }

BIN=${ESRGAN_BIN:-$(command -v realesrgan-ncnn-vulkan || true)}
if [ -n "$BIN" ] && [ -x "$BIN" ]; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; mkdir "$T/a" "$T/b"
  ffmpeg -v error -i "$IN" -frames:v 1 "$T/a/probe.png"
  if "$BIN" -i "$T/a/probe.png" -o "$T/b/probe.png" -s 2 -m "$(dirname "$BIN")/models" >/dev/null 2>&1; then
    rm -f "$T"/a/* "$T"/b/*
    FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$IN")
    NAME=realesr-animevideov3; [ "$MODEL" = general ] && NAME=realesrgan-x4plus
    ffmpeg -v error -i "$IN" -fps_mode passthrough "$T/a/%06d.png"
    "$BIN" -i "$T/a" -o "$T/b" -n "$NAME" -s 2 -m "$(dirname "$BIN")/models" -f png >/dev/null 2>&1
    FIT="scale=720:1280:force_original_aspect_ratio=increase:flags=lanczos,crop=720:1280,setsar=1,format=yuv444p"
    ffmpeg -v error -y -framerate "$FPS" -i "$T/b/%06d.png" -i "$IN" -filter_complex \
      "[0:v]$FIT[e];[1:v]$FIT[s];[e][s]blend=all_expr='A*(1-$MIX)+B*$MIX',format=yuv420p[v]" \
      -map "[v]" -map 1:a? -c:v libx264 -crf 16 -preset medium -c:a copy -shortest "$OUT"
    echo "ok (ncnn-vulkan): $OUT $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$OUT")"
    exit 0
  fi
  echo "ncnn-vulkan unusable here (no Vulkan driver?), using the CPU path" >&2
fi
PAPER_MIX=$MIX "${PYTHON:-python3}" "$HERE/esrgan_cpu.py" "$IN" "$OUT" --w 720 --h 1280 --model "$MODEL"
echo "ok (cpu): $OUT $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$OUT")"
