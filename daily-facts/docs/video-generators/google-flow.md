# Google Flow (Veo 3.1 Lite)

[Google Flow](https://labs.google/fx/tools/flow) is the current clip generator (since Derinkuyu / Hanging Gardens, Nov 2026).

## Settings
| Setting | Value |
|---|---|
| Model | **Veo 3.1 Lite** (`veo-lite` in gflow-cli) |
| Mode | image-to-video / frames to video, **start frame + end frame** |
| Aspect | **9:16** (check the composer before every Generate; Flow may remember 16:9) |
| Resolution | 720p (the Veo Lite default; the result is 720x1280) |
| Duration | 8 s (clips come out ~7.9 s) |
| Outputs | 1 per prompt |
| Composer | classic only; never the Agent button |
| Cost | **~10 Flow credits per clip (estimate)**; 14 scenes = 7 clips = ~70 credits |

## Credits
Rotate between all existing profiles to use their daily free credits. Check the balance before each clip; when every profile is low, stop and create a one-shot routine for after the daily refresh (see `../routines.md`). A credit shortage is not a failure, and credits are never bought.

## Frame pairing
14 approved picks -> 7 clips: clip N uses `picks/s(2N-1).png` as start and `picks/s(2N).png` as end, so each clip morphs from one line's image to the next. The motion prompt describes that transition (`motion_prompts.txt`, see `../../examples/derinkuyu/motion_prompts.txt`):
```
Massive round stone door rolls shut along its groove to seal the tunnel like a vault, dust drifts,
close soft camera hold, watercolor ink lines steady, no text
```

## A. Primary: Flow web UI in the box Chrome
1. Open Chrome with a profile that still has credits, go to Flow, open/create the story's project.
2. Frames to video: upload start and end frame.
3. Veo 3.1 Lite, 9:16, 1 output. Paste the motion prompt. Generate.
4. Preview; download the MP4 to `<story>/clips/clipNN.mp4`; `ffprobe` -> 720x1280.
5. Next clip; switch profile when credits run low.

## B. Fallback: gflow-cli
[ffroliva/gflow-cli](https://github.com/ffroliva/gflow-cli) (MIT, alpha, reverse-engineered, not affiliated with Google), v0.92.1 on the box. It drives a headed Chrome on the box display with the signed-in Flow session.
```bash
gflow video i2v --profile <profile> --model veo-lite --aspect 9:16 --ui-mode classic \
  --initial-frame picks/s01.png --end-frame picks/s02.png \
  --project-name <story> --out-dir <out> --json "<motion prompt>"
```
Batch: `scripts/flow/run_clips.sh` (skips finished clips, rotates profiles, logs exit codes).
- `--resolution` is only for omni_flash; do not pass it with veo-lite (fails pre-submit).
- Exit codes we met: **6** = media download failed (the clip was generated: download it from the Flow project in the UI), **23** = UI selector drift (stop, look at Flow in the browser). Others: 3 auth, 4 rate limit, 5 content policy.
- Sign-in for a profile is done by the user in the box browser; no credentials are stored anywhere in this repo.

## Known issues
- Clips sometimes drift (faces or architecture melt between start and end frames): pick a calmer window in the edit, lock the area with a still mask, or re-roll.
- Veo adds ambience audio: kept very low and ducked under the narration.
