#!/usr/bin/env bash
# Grok Imagine per-part chain helpers:
#   extract-last  CLIP_A.mp4  OUT.jpg
#   join          CLIP_A.mp4  CLIP_B.mp4  OUT.mp4
#   upscale       INPUT.mp4   [OUTPUT.mp4]   # calls upscale_720p.sh
#   all           CLIP_A.mp4  CLIP_B.mp4  JOINED.mp4  [UPSCALED.mp4]
# Docs: docs/video-generators/grok-imagine.md , docs/upscale-real-esrgan.md
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
UPSCALE="$ROOT/upscale_720p.sh"

usage() {
  cat >&2 <<'U'
Usage:
  chain_and_upscale.sh extract-last CLIP_A.mp4 OUT.jpg
  chain_and_upscale.sh join         CLIP_A.mp4 CLIP_B.mp4 OUT.mp4
  chain_and_upscale.sh upscale      INPUT.mp4 [OUTPUT.mp4]
  chain_and_upscale.sh all          CLIP_A.mp4 CLIP_B.mp4 JOINED.mp4 [UPSCALED.mp4]
U
  exit 2
}

[[ $# -ge 1 ]] || usage
CMD="$1"; shift

case "$CMD" in
  extract-last)
    [[ $# -eq 2 ]] || usage
    IN="$1"; OUT="$2"
    [[ -f "$IN" ]] || { echo "Missing $IN" >&2; exit 1; }
    # Seek ~1 frame before EOF and grab one frame (works for short clips)
    ffmpeg -hide_banner -loglevel error -y -sseof -0.05 -i "$IN" -frames:v 1 -q:v 2 "$OUT"
    echo "Wrote last frame $OUT"
    ;;

  join)
    [[ $# -eq 3 ]] || usage
    A="$1"; B="$2"; OUT="$3"
    [[ -f "$A" && -f "$B" ]] || { echo "Missing A or B" >&2; exit 1; }
    TMP="$(mktemp -d "${TMPDIR:-/tmp}/chainjoin.XXXXXX")"
    trap 'rm -rf "$TMP"' EXIT
    # Re-encode both to identical params then concat demuxer (no freeze, hard cut at seam)
    FPS="$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$A")"
    for X in A B; do
      SRC="${!X}"
      ffmpeg -hide_banner -loglevel error -y -i "$SRC" \
        -an -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2,setsar=1,fps=$FPS" \
        -c:v libx264 -pix_fmt yuv420p -crf 14 -preset fast \
        "$TMP/${X}.mp4"
    done
    printf "file '%s'\nfile '%s'\n" "$TMP/A.mp4" "$TMP/B.mp4" > "$TMP/list.txt"
    ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i "$TMP/list.txt" -c copy "$OUT"
    echo "Joined -> $OUT"
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=0 "$OUT"
    ;;

  upscale)
    [[ $# -ge 1 ]] || usage
    exec "$UPSCALE" "$@"
    ;;

  all)
    [[ $# -ge 3 ]] || usage
    A="$1"; B="$2"; JOINED="$3"; UPSCALED="${4:-${JOINED%.mp4}_720p.mp4}"
    LAST="${JOINED%.mp4}_a_last.jpg"
    # extract last of A (useful when caller still needs it for regenerating B)
    "$0" extract-last "$A" "$LAST"
    "$0" join "$A" "$B" "$JOINED"
    "$0" upscale "$JOINED" "$UPSCALED"
    echo "Done: $JOINED + $UPSCALED (last frame also at $LAST)"
    ;;

  *)
    usage
    ;;
esac
