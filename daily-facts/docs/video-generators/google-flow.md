# Google Flow (Veo 3.1 Lite)

[Google Flow](https://labs.google/fx/tools/flow) is the current clip generator (since Derinkuyu / Hanging Gardens, Nov 2026).

## Settings
| Setting | Value |
|---|---|
| Model | **Veo 3.1 Lite** (`veo-lite` in gflow-cli) |
| Mode | image-to-video / frames to video, **start frame + end frame** |
| Aspect | **9:16, set explicitly on every generation** (Flow may remember 16:9); verify height > width after each clip |
| Resolution | **720p directly** (the Veo Lite default; the result is 720x1280). No 480p test, no upscale: QA Gate 1 watches the 720p clip right away |
| Duration | **4, 6 or 8 s** (8 s is the hard max; pick the shortest that covers the part's narration). 8 s clips come out ~7.9 s |
| Outputs | 1 per prompt |
| Composer | classic only; never the Agent button |
| Cost | **~10 Flow credits per clip (estimate)**; a 9-part video = 9 clips = ~90 credits (estimate) |

## Credits
Rotate between all existing profiles to use their daily free credits. Check the balance before each clip; when every profile is low, stop and create a one-shot routine for after the daily refresh (see `../routines.md`). A credit shortage is not a failure, and credits are never bought.

## Inputs per part (Step 0 first)
Every part N has one matched pair made before any credits are spent (see `../images-and-animation.md`):
`scenes/partN_start.png` (Krea, trained style) and `scenes/partN_end.png` (image edit FROM the start frame), plus `prompts/partN.txt` with the motion only. Never feed two independent stills.
A part's narration is at most 8 s (~18-20 words max, plan ~16-18 at our Kokoro pace); a longer beat becomes two parts and part N+1 starts from part N's end frame.

Old method (Derinkuyu, retired): 14 independent scene picks paired two by two (`s01`+`s02` -> clip 1). Kept in `../../examples/derinkuyu/` for reference.

## A. Default: Flow web UI in the box Chrome
1. Open Chrome with a profile that still has credits (rotate between all existing profiles to use their daily free credits), go to Flow, open/create the story's project.
2. Frames to video: upload `partN_start.png` as start and `partN_end.png` as end.
3. Paste `prompts/partN.txt`. Model **Veo 3.1 Lite**, **9:16** (check it is selected), 4/6/8 s, 1 output. Classic composer; **never click Agent**.
4. Generate, preview, download to `<story>/clips/partN.mp4`.
5. Verify: `ffprobe` height > width (720x1280); landscape = reject and redo. Compare the last frame with `partN_end.png` (`scripts/video/chain_parts.sh check clips/partN.mp4 scenes/partN_end.png`).
6. Part 1 is the sample: stop after it for approval. Then continue part by part.

## B. Fallback only: gflow-cli
Use it **only if the browser faults or has no access** (Flow does not load, session broken and not fixable in the browser, downloads fail repeatedly).

[ffroliva/gflow-cli](https://github.com/ffroliva/gflow-cli) (MIT, alpha, reverse-engineered, not affiliated with Google), v0.92.1 on the box. It drives a headed Chrome on the box display with the signed-in Flow session.
```bash
gflow video i2v --profile <profile> --model veo-lite --aspect 9:16 --ui-mode classic \
  --initial-frame scenes/part1_start.png --end-frame scenes/part1_end.png --duration 8 \
  --project-name <story> --out-dir <out> --json "<motion prompt>"
```
Batch: `scripts/flow/run_clips.sh` (part pairs, skips finished clips, rotates profiles, logs exit codes, rejects landscape). Always `--aspect 9:16` and `--ui-mode classic` (or `GFLOW_CLI_UI_MODE=classic`) so a non-classic composer aborts before spending credits.
- `--resolution` is only for omni_flash; do not pass it with veo-lite (fails pre-submit).
- Exit codes we met: **6** = media download failed (the clip was generated: download it from the Flow project in the UI), **23** = UI selector drift (stop, look at Flow in the browser). Others: 3 auth, 4 rate limit, 5 content policy.
- Sign-in for a profile is done by the user in the box browser; no credentials are stored anywhere in this repo.

## Known issues
- Clips sometimes drift (faces or architecture melt between start and end frames): pick a calmer window in the edit, lock the area with a still mask, or re-roll.
- Veo adds ambience audio: muted in the edit (`CLIP_AUDIO=0`); QA Gate 4 checks that none leaks into the narration pauses.
