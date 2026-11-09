#!/bin/bash
# Fallback path: generate one Veo 3.1 Lite clip per start/end frame pair with gflow-cli.
# Primary path is the Flow web UI in the box Chrome (see docs/video-generators/google-flow.md).
#
# Usage: STORY_DIR=/workspace/arete/<story> PROFILES="<profile list>" bash run_clips.sh
#   picks/sNN.png         locked Krea picks, 2 per clip (odd = start frame, even = end frame)
#   motion_prompts.txt    "NN|prompt" per clip
# Profiles: rotate between all existing profiles to use their daily free credits.
# Each clip costs ~10 Flow credits (estimate). Skips clips that already exist, so a re-run after
# a credit refresh only does the missing ones.
set -u
D=${STORY_DIR:?set STORY_DIR}
N=${N_CLIPS:-7}
export GFLOW_CLI_HOME=${GFLOW_CLI_HOME:-/workspace/gflow/home}
OUT=${GFLOW_CLI_OUTPUT_DIR:-/workspace/gflow/out}; export GFLOW_CLI_OUTPUT_DIR=$OUT
export GFLOW_CLI_UI_MODE=classic
read -r -a P <<< "${PROFILES:?set PROFILES (space separated, all existing profiles)}"
mkdir -p "$D/clips" "$D/flow"
pi=0
for n in $(seq 1 $N); do
  NN=$(printf %02d $n); a=$(printf %02d $((2*n-1))); b=$(printf %02d $((2*n)))
  [ -s "$D/clips/clip$NN.mp4" ] && continue
  prompt=$(grep "^$NN|" "$D/motion_prompts.txt" | cut -d'|' -f2-)
  gflow video i2v --profile "${P[$pi]}" --model veo-lite --aspect 9:16 --ui-mode classic \
    --initial-frame "$D/picks/s$a.png" --end-frame "$D/picks/s$b.png" \
    --project-name "$(basename "$D")" --out-dir "$OUT" --json "$prompt" > "$D/flow/clip$NN.log" 2>&1
  rc=$?
  echo "clip$NN exit $rc profile#$pi" >> "$D/flow/summary.txt"
  # non-zero exit: 3 auth, 4 rate limit, 6 network/download (clip may exist in the Flow project: download it in the UI), 23 UI drift (stop, check Flow). Move to the next profile.
  if [ $rc -ne 0 ]; then pi=$(( (pi+1) % ${#P[@]} )); [ $rc -eq 23 ] && break; fi
done
# Downloaded MP4s land in $OUT; move each into $D/clips/clipNN.mp4 and check height > width with ffprobe.
