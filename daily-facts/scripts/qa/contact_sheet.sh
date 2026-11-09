#!/bin/bash
# QA helper: N evenly spaced frames of a video in one sheet (send to the QA bot with the video).
# Usage: bash contact_sheet.sh final.mp4 out.jpg [N=12]
V=$1; O=$2; N=${3:-12}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -v error -y -i "$V" -vf "fps=$N/$D,scale=270:-2,tile=6x$(( (N+5)/6 ))" -frames:v 1 -q:v 3 "$O"
