# Google Flow (Veo) — browser workflow

**Primary method: the web UI in the box's Chrome**, operated by the bot's browser/desktop agent with the already signed-in profiles.
- Site: https://flow.google.com (Google Labs Flow, also reachable via https://labs.google/fx/tools/flow).
- Method used before (Daily Facts videos): **Veo 3.1 Lite, 720p, 9:16, a start frame and an end frame per clip, ~10 Flow credits per clip.**

## Daily free credits: rotate between profiles
- Each Flow account in the box's Chrome has **50 free credits per day**, and each account refreshes at its own time.
- **Rotate between all existing Chrome profiles** to use every account's daily free credits before anything else.
  - Check a profile's balance in Flow's account menu.
  - Generate until it is low, then switch to the next profile.
  - Log which clip came from which profile in the project notes on the box.
- Profile names, account names and refresh times are deliberately **not** written here.

## Steps in the web UI (labels may change; follow what the page shows)
1. Open Chrome with the next profile in the rotation. Go to flow.google.com and open or create a project for the story.
2. Check the credit balance (account menu). If it's under ~10, switch profiles.
3. Choose **image-to-video / frames to video** and **upload the start frame** (`scenes/sceneN.jpg`). For a controlled end pose, also **upload an end frame** (e.g. a variant of the same still with the action completed).
4. Settings: **model Veo 3.1 Lite** (cheapest; Fast/Quality cost more), **aspect 9:16**, **720p**, and a duration covering the scene slot (4 / 6 / 8 s).
5. Prompt: slow one-direction motion for the scene's action, "static locked camera, no zoom, no pan", no text.
6. Click **Generate** (one clip, count 1), wait, and preview.
7. **Download** the MP4. It lands in `/home/box/Downloads/`. Move it to `/workspace/<story>/gen/sN.mp4`.
8. Continue with RIFE + layout (see `README.md`).

## Rules
- **Never click Flow's "Agent" button.**
- Never buy credits or subscriptions unless the user explicitly asks.
- Spend credits **only on Veo video clips** for approved scenes.
- No re-runs "just to compare" without a reason.
- Never type passwords. If a profile is signed out, follow the `sign-in` skill and ask the user.

## Secondary note: CLI/MCP (not the method)
[ffroliva/gflow-cli](https://github.com/ffroliva/gflow-cli) (MIT, alpha, reverse-engineered, not affiliated with Google) is installed on the box at `/home/box/.local/bin/gflow-cli` (v0.92.1, source `/workspace/gflow-cli`).
- Example: `gflow video i2v --initial-frame start.png --end-frame end.png --model veo-lite --aspect 9:16 --duration 8 --profile <profile> "prompt" --out-dir ./gen`
- Balance: `gflow credits user --profile <profile>` / `gflow credits list`
- MCP server: `gflow mcp run` (stdio, add `--no-spend` to hide the spending tools) or `gflow serve --port 8000`.
- Use only if the user asks for it. The browser stays the primary route.
