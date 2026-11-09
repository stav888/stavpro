#!/bin/bash
# FALLBACK ONLY: generate one Veo 3.1 Lite clip per part with gflow-cli. The default path is the
# Flow web UI in the box Chrome (docs/video-generators/google-flow.md); use this only if the
# browser faults or has no access.
#
# Usage: STORY_DIR=/workspace/arete/<story> PROFILES="<all existing profiles>" PARTS="1 2 3" bash run_clips.sh
#   scenes/partN_start.png + scenes/partN_end.png   matched pair (end made FROM start), approved
#   prompts/partN.txt                                transition prompt (motion only)
#   prompts/partN.dur  (optional)                    4, 6 or 8 (default 8; Veo max is 8 s)
# Profiles: rotate between all existing profiles to use their daily free credits.
# Clips are generated directly at 720p (Veo 3.1 Lite default, 720x1280): no 480p test and no
# upscale for Flow; QA Gate 1 watches each 720p clip right away (scripts/qa/qa_check.py clip ...).
# ~10 Flow credits per clip (estimate). Existing clips are skipped, so a re-run after the daily
# credit refresh only does the missing parts. Part 1 is the approval sample: run PARTS="1" first.
set -u
D=${STORY_DIR:?set STORY_DIR}
PARTS=${PARTS:?set PARTS, e.g. \"1\" for the sample, then \"2 3 4 ...\"}
export GFLOW_CLI_HOME=${GFLOW_CLI_HOME:-/workspace/gflow/home}
OUT=${GFLOW_CLI_OUTPUT_DIR:-/workspace/gflow/out}; export GFLOW_CLI_OUTPUT_DIR=$OUT
export GFLOW_CLI_UI_MODE=classic           # abort before spending credits if not the classic composer
read -r -a P <<< "${PROFILES:?set PROFILES (space separated, all existing profiles)}"
mkdir -p "$D/clips" "$D/flow"
vert(){ IFS=x read -r w h < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$1"); [ "$h" -gt "$w" ]; }
pi=0
for n in $PARTS; do
  [ -s "$D/clips/part$n.mp4" ] && continue
  S="$D/scenes/part${n}_start.png"; E="$D/scenes/part${n}_end.png"
  for f in "$S" "$E"; do vert "$f" || { echo "part$n: $f is not 9:16, fix the sketch first" >&2; exit 3; }; done
  dur=$(cat "$D/prompts/part$n.dur" 2>/dev/null || echo 8)
  gflow video i2v --profile "${P[$pi]}" --model veo-lite --aspect 9:16 --ui-mode classic --duration "$dur" \
    --initial-frame "$S" --end-frame "$E" --project-name "$(basename "$D")" --out-dir "$OUT" --json \
    "$(cat "$D/prompts/part$n.txt")" > "$D/flow/part$n.log" 2>&1
  rc=$?
  echo "part$n exit $rc profile#$pi" >> "$D/flow/summary.txt"
  # exit codes: 3 auth, 4 rate limit, 6 network/download (the clip may exist in the Flow project:
  # download it in the UI), 23 UI drift (stop and look at Flow in the browser). Move to the next profile.
  if [ $rc -ne 0 ]; then pi=$(( (pi+1) % ${#P[@]} )); [ $rc -eq 23 ] && break; continue; fi
  # gflow writes the MP4 into $OUT: move the newest file to clips/partN.mp4 and reject landscape
  f=$(ls -t "$OUT"/*.mp4 2>/dev/null | head -1)
  if [ -n "$f" ]; then mv "$f" "$D/clips/part$n.mp4"; vert "$D/clips/part$n.mp4" || { echo "part$n: landscape clip, rejected" >&2; mv "$D/clips/part$n.mp4" "$D/flow/part${n}_REJECTED_landscape.mp4"; }; fi
done
