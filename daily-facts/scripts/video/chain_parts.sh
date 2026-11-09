#!/usr/bin/env bash
# Grok Imagine option: build one ~8 s part from two chained 4 s clips.
#   last  CLIP_A.mp4 OUT.png          -> last frame of clip A (the start image for clip B)
#   join  CLIP_A.mp4 CLIP_B.mp4 OUT   -> A + B as one continuous clip (B's first frame, which repeats
#                                        A's last frame, is dropped so there is no stutter)
#   check PART.mp4 partN_end.png      -> side-by-side of the part's last frame and the end sketch
# All inputs must be vertical (height > width); anything else is rejected.
set -euo pipefail
vert(){ IFS=x read -r w h < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$1"); [ "$h" -gt "$w" ] || { echo "reject: $1 is ${w}x${h}, not 9:16" >&2; exit 3; }; }
case "${1:-}" in
  last)  vert "$2"; ffmpeg -v error -y -sseof -0.25 -i "$2" -update 1 -q:v 1 "$3"; echo "$3";;
  join)  vert "$2"; vert "$3"
         FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$2")
         ffmpeg -v error -y -i "$2" -i "$3" -filter_complex \
           "[0:v]fps=$FPS,setsar=1[a];[1:v]fps=$FPS,setsar=1,trim=start_frame=1,setpts=PTS-STARTPTS[b];[a][b]scale2ref=flags=lanczos[b2][a2];[a2][b2]concat=n=2:v=1:a=0[v]" \
           -map "[v]" -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$4"
         echo "$4 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$4") s";;
  check) vert "$2"; T=$(mktemp --suffix=.png); ffmpeg -v error -y -sseof -0.1 -i "$2" -update 1 "$T"
         ffmpeg -v error -y -i "$T" -i "$3" -filter_complex "[0]scale=-2:720[a];[1]scale=-2:720[b];[a][b]hstack" "${2%.*}_endcheck.jpg"
         rm -f "$T"; echo "${2%.*}_endcheck.jpg";;
  *) echo "usage: chain_parts.sh last A.mp4 out.png | join A.mp4 B.mp4 out.mp4 | check part.mp4 partN_end.png" >&2; exit 2;;
esac
