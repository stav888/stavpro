# Google Flow (Veo): web UI in box Chrome (primary)

**Primary method: work directly in Flow's web UI** (https://flow.google.com) in the box's **Chrome browser** (manual browser operation by the bot's browser/desktop agent). No gflow-cli MCP for the normal path.

**Fallback only:** the [gflow-cli](https://github.com/ffroliva/gflow-cli) MCP server (below) — use it **only** when the browser route has a **fault** or **no access** (Chrome won't open, Flow won't load, login/session broken and can't be fixed in-browser, downloads fail repeatedly, or the page is unusable). Do **not** start with MCP when the browser works.

- Method used before (Daily Facts videos): **Veo 3.1 Lite, 720p, 9:16, a start frame and an end frame per clip, ~10 Flow credits per clip.**
- gflow-cli on the box (fallback tooling):
  - Installed: v0.92.1 at `/home/box/.local/bin/gflow` (also available as `gflow-cli`). Source and docs: `/workspace/gflow-cli` (`docs/MCP.md`, `docs/CONFIGURATION.md`).
  - Licence MIT, alpha, reverse-engineered. Not affiliated with Google.


> ## 🖼️ Step 0: sketch the frames first (ACCORDING TO the reference images), then spend video credits
> Before **any** video generation, prepare the stills for **every scene** **according to** the style references in [`../../reference-images/`](../../reference-images/) (38 vertical 9:16 frames from 13 of our Shorts):
> 1. **Pick 2–3 relevant reference images per scene** from `reference-images/` (link them by relative path in the scene notes, e.g. `../../reference-images/lustig-02-middle.jpg`). Prefer refs whose action, props or composition match the beat.
> 2. Make the **start frame** for each scene, and an **end frame** where the model supports one (all Veo models in Flow accept start + end frames). Use free image generation only: the built-in `GenerateImage` (or another free image tool), **passing those 2–3 refs as style references / describing their style in the image prompt**. Match: pure white background, thin wobbly black lines, black Xiaohei character doing the action, character size and composition, and minimal colour accents **as in the chosen references**. Every sketch is **vertical 9:16** (e.g. 1080×1920 or 540×960) — **never 16:9**. Save as `scenes/sceneN.jpg` and `scenes/sceneN_end.jpg`.
> 3. **Check** each sketch **side by side** with the chosen references and the **scene table** (scene → sentence numbers, see [images-and-animation](../images-and-animation.md)): Xiaohei ink look, matching characters across scenes, illustration only (no baked-in title/underline/caption), large Xiaohei filling most of the width (not a small centred vignette), height > width. The end frame is the same shot with the action completed (same camera, no zoom or pan). **Regenerate any sketch that drifts in style** from the references — fix now, while it's free.
> 4. **Only then** spend video credits, one clip per approved scene.
>
> This follows the existing approval flow ([script-writing § Approval gate](../script-writing.md#approval-gate-mandatory)): the user approves the script plus a sample frame before full production. The full set of frames is prepared and checked against the references before any paid clip.

> ## ⚠️ Aspect ratio 9:16 is mandatory
> Flow will happily make landscape if you let it. Prevent that:
> - **Manual web UI (primary):** pick **9:16** in the composer **before** every generation and confirm the UI shows 9:16 (Flow may remember the last-used 16:9). Prefer the **classic** composer — never Agent. Flow's agentic UI treats aspect as a soft hint and can return landscape.
> - For sketches made with the built-in `GenerateImage` or any other tool, request **9:16 / 1080×1920** explicitly in the prompt or size fields.
> - **Fallback MCP:** always pass **`aspect: "9:16"` explicitly** on every `gflow_generate_image` **and** `gflow_generate_video` call (the image tool defaults to `"1:1"`). Always pass **`ui_mode: "classic"`**, and set **`GFLOW_CLI_UI_MODE=classic`** in the MCP server / daemon env, so a non-classic arm **aborts before spending credits**. CLI: always pass `--aspect 9:16` (and prefer `--ui-mode classic`).
> - After generating, verify every still/clip with `ffprobe` or PIL that **height > width** (e.g. 1080×1920 or 720×1280). Reject and regenerate anything landscape before going on.

## Frame layout (mandatory)

**All on-screen text in the video is English only** (title, subtitles, page counter). Never put Hebrew or any other language on the frame.

Generated stills and clips (sketches **and** video) contain the **illustration only**:
- **No title, no underline, no caption, no page counter, no letters of any kind.**
- Every image/video prompt must say: `no text, no letters, no captions`.
- Any lettering baked into a still or clip is a **reject** — regenerate it. Text is added afterwards by [`../../scripts/video/build.py`](../../scripts/video/build.py) (or [`../../scripts/video/preview_frame.py`](../../scripts/video/preview_frame.py) for the approval sample).

**Drawing size (fill the screen):**
- Make the scene fill nearly the whole **width** of the image. The Xiaohei character must be large and clearly doing the action — not a small vignette centred in the middle.
- `build.py` crops each clip to the drawing's bounding box (pixels darker than 200, plus a 14 px margin) and scales it to fit a **1060×1150** box, centred at about **y=790** and kept between **y=200** and **y=1400** of the 1080×1920 frame. A wide, well-filled drawing therefore ends up filling most of the screen; a small centred drawing stays small.

**Overlay layout on the 1080×1920 canvas** (Patrick Hand, `PatrickHand-Regular.ttf`, env `PATRICK_HAND_TTF`):

| Element | Spec |
|---|---|
| Title | English, **UPPERCASE**, 64 px, colour `(20,20,20)`, centred at `(540,115)` |
| Red underline | from **x=400 to x=680** (280 px ≈ 26% of width), **6 px** thick, at **y=165**, colour `(225,55,40)` |
| Subtitles | English, **62 px** (fallback 56 then 52 only if a line won't fit), max line width **960 px**, max **2 lines**, line spacing **70 px**, first line top at **y=1430**, colour `(12,12,12)`, centred |
| Page counter | `— i / N —`, 32 px, grey `(130,130,130)`, at **y=1835** |

At the 540×960 preview / reference size these are half: title 32 px, underline 140 px long and 3 px thick at y≈82, subtitles 31 px.

**Sample-frame approval:** build the approval sample by compositing the generated illustration with these overlays (`build.py`'s static overlay plus one subtitle chunk), **never** by asking the image generator to draw text. Helper: [`../../scripts/video/preview_frame.py`](../../scripts/video/preview_frame.py):

```bash
PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf \
  python ../../scripts/video/preview_frame.py scenes/scene1.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

## 1. Primary: manual web UI in box Chrome

Labels may change; follow what the page shows. Use the **classic** composer only.

1. Open Chrome with the next profile in the rotation and go to flow.google.com. Open or create the story's project.
2. Check the credit balance in the account menu. If it's under ~10, switch profiles.
3. Choose image-to-video / frames to video. Upload the **start frame** (`scenes/sceneN.jpg`), and the **end frame** if there is one.
4. Choose **Veo 3.1 Lite**, **9:16**, **720p**, and a duration of 4/6/8 s. One output.
5. Confirm the composer shows **9:16** before Generate (Flow may remember the last-used 16:9). Prefer classic; **never click Agent**.
6. Use the same prompt pattern (one-direction motion, locked camera, no text, no letters, no captions). Click Generate, then preview.
7. Download the MP4. It lands in `/home/box/Downloads/`; move it to `/workspace/<story>/gen/sN.mp4`. Verify with `ffprobe` that height > width; reject landscape.

## 2. Daily free credits: rotate between profiles

- Each Flow account in the box's Chrome has **50 free credits per day**, and each account refreshes at its own time.
- **Rotate between all existing Chrome profiles** to use every account's daily free credits:
  1. Check the balance in the account menu (or, on the MCP fallback, `gflow_get_credits(all_profiles=true)`).
  2. Pick a profile with ≥ ~10 credits.
  3. Generate on that profile.
  4. When it runs low, move to the next profile.
- Work one clip at a time on a given profile when sharing the same Chrome window; different profiles can be used in turn across the day.
- Log which clip came from which profile in the project notes on the box.
- Profile names, account names, emails and refresh times are deliberately **not** written here.

## 3. Rules

- **Never click Flow's "Agent" button.** Stay in the **classic** composer. If an account's composer is agent-only, skip that profile.
- Never buy credits or subscriptions unless the user explicitly asks.
- Spend credits **only on Veo video clips** for approved scenes (no image generation in Flow for paid sketches when free tools cover Step 0, no re-runs "just to compare").
- A credit shortage is not a browser fault: if every profile's balance is too low, stop and tell the user. Don't buy credits and don't switch routes to get around it.
- Never commit cookies, `.env`, profile directories, or (on the MCP path) `GFLOW_DAEMON_TOKEN`.

## 4. Fallback: gflow-cli MCP

Use this **only** when the primary browser route has a **fault** or **no access** (Chrome/Flow won't open or load, session/login broken beyond an in-browser fix, repeated download failures, or the page is unusable). Tell the user you're falling back to MCP. Do **not** use MCP as the default when the browser works.

gflow-cli drives Flow in a **headed** real Chrome using the signed-in browser profiles: typed tool calls, JSON results with file paths, and errors with a `retryable` flag.

### Start the MCP server
| Mode | Command | Use |
|---|---|---|
| Read-only (safe) | `gflow mcp run --no-spend` (or `GFLOW_MCP_NO_SPEND=1`) | Checking balances, profiles and models. The spending tools `gflow_generate_video` / `gflow_generate_image` are **not registered at all**. |
| Generation | `gflow mcp run` (stdio; `--profile <profile>` pins a default profile) | Only after the user approved the script and the sample frames, and only as fallback |
| HTTP daemon | `gflow serve --port 8000 --host 127.0.0.1 [--profile <profile>] [--no-spend]` → endpoint `http://127.0.0.1:8000/mcp` | When several scripts or clients share one warm server. Keep it on loopback. A non-loopback host needs `GFLOW_DAEMON_TOKEN`, which is never committed. |

stdio client config:
```json
{ "mcpServers": { "gflow-cli": { "command": "gflow", "args": ["mcp", "run", "--no-spend"] } } }
```
Remove `--no-spend` only for an approved generation session.

Browser notes for the MCP driver:
- Set `GFLOW_CLI_UI_MODE=classic` in the server environment (and pass `ui_mode: "classic"` on every generate call) so a non-classic arm aborts before credits are spent.
- Generation needs a **headed** Chrome. `GFLOW_CLI_HEADLESS` defaults to `false`, and that's required because reCAPTCHA rejects headless.
- The window opens off-screen by default (`GFLOW_CLI_BROWSER_WINDOW_POSITION=-30000,-30000`). Set a position to watch it on the box desktop.
- Profiles are gflow's saved Chrome sessions. List them with `gflow auth list`. One-time sign-in is `gflow auth login --browser chrome`, done interactively by the user, never with typed passwords.

### Tools for this pipeline (from `docs/MCP.md`)
| Tool | Spends? | What we use it for |
|---|---|---|
| `gflow_auth_status(profile)` | no | Fast check that a profile's Flow session is alive before a run |
| `gflow_get_credits(profile, all_profiles, refresh)` | no | Balance per profile. `all_profiles=true` reads every saved profile and returns `total_credits`. |
| `gflow_list_models()` | no | Model aliases and max durations (Veo 3.1: 4/6/8 s) |
| `gflow_generate_video(...)` | **yes, credits** | Image-to-video with start and end frames (below) |
| `gflow_download_media(media_id, out_dir, profile)` | no | Recovers a clip that was generated and billed but whose download failed |
| `gflow_list_projects(profile, limit, offset)` | no | Recent generations from the local catalog |
| `gflow_upscale_video(media_id, scale, ...)` | free (measured once) | Optional 1080p export. Not needed, since RIFE + layout handle sizing. |

Image-to-video call for one scene:
```json
{
  "name": "gflow_generate_video",
  "arguments": {
    "mode": "i2v",
    "initial_frame": "/workspace/<story>/scenes/sceneN.jpg",
    "end_frame": "/workspace/<story>/scenes/sceneN_end.jpg",
    "prompt": "<slow one-direction motion for the scene>, static locked camera, no zoom, no pan, no text, no letters, no captions",
    "model": "veo_lite",
    "aspect": "9:16",
    "duration": 8,
    "count": 1,
    "profile": "<profile>",
    "project": "<flow project id for this story, optional>",
    "ui_mode": "classic",
    "output": "<story>/sN.mp4",
    "wait": true
  }
}
```
Image sketch call (free still; always force 9:16 + classic):
```json
{
  "name": "gflow_generate_image",
  "arguments": {
    "prompt": "Ian Xiaohei style ink illustration, pure white background, thin wobbly black lines, LARGE black Xiaohei character <action> filling most of the frame width (not a small centred vignette), minimal colour accents, no text, no letters, no captions, vertical 9:16",
    "model": "nano2",
    "aspect": "9:16",
    "count": 1,
    "reference_images": [
      "/path/to/history-storyteller/reference-images/<ref-a>.jpg",
      "/path/to/history-storyteller/reference-images/<ref-b>.jpg"
    ],
    "ui_mode": "classic",
    "profile": "<profile>",
    "output": "<story>/scenes/sceneN.jpg",
    "wait": true
  }
}
```
- Always set `aspect: "9:16"` — the tool default is `"1:1"`.
- Always set `ui_mode: "classic"` (and `GFLOW_CLI_UI_MODE=classic` on the server). Agentic treats aspect as a soft hint and can return landscape.
- Pass 2–3 `reference-images/` JPGs as `reference_images` so the sketch matches our Shorts style.

- `initial_frame` and `end_frame` take local file paths (or a Flow image UUID). Each is uploaded into the Flow project under a run-unique name.
- **`model: veo_lite`** is Veo 3.1 Lite, the cheapest; it's also the default for i2v when `model` is omitted. Its output is 720p, the Daily Facts setting.
  - Do **not** pass `resolution` with Veo: it is only supported on `omni_flash`, and on other models the job is refused before submit.
- `duration` is 4, 6 or 8 for Veo 3.1. Pick the value that covers the scene slot; RIFE retimes it exactly afterwards.
- `count` is always 1, because count multiplies the cost.
- `wait=true` keeps the call open for minutes, so raise the client's tool timeout. Alternatively, use `wait=false`, which returns a `task_id`; poll `tasks/get` and check `result.isError`.
- **Downloads:**
  - MCP `output` must sit inside gflow's output directory, `GFLOW_CLI_OUTPUT_DIR`. On the box the default is `/home/box/Downloads/gflow-cli/`.
  - The reply gives the file path. Copy the file to `/workspace/<story>/gen/sN.mp4`.
  - If the download failed but the clip was made, the reply has `flow_media_id`. Call `gflow_download_media` with it (free) and **do not regenerate**.
- Error handling:
  - Follow the envelope's `retryable` flag; re-run at most once.
  - A `retryable: false` timeout after submit may already be billed, so check the Flow project before retrying.
  - Upload refused by Flow's one-time "rights to use this image" dialog: the user must accept it once by hand. gflow won't click it.
- With MCP: keep `ui_mode` on `classic`/`auto` (video has only a classic driver; `agentic` is refused). Don't use the `gflow_instructions_*` (Agent-Mode) tools. If an account's composer turns out to be agent-only, i2v is refused before anything is clicked — skip that profile.
- Run with `--no-spend` whenever no generation is intended.
- Rotate profiles the same way as in §2 (`gflow_get_credits(all_profiles=true)`, pass `profile` on each call).

### CLI equivalent (one-off checks)
- `gflow video i2v --initial-frame start.png --end-frame end.png --model veo-lite --aspect 9:16 --ui-mode classic --duration 8 --profile <profile> "prompt" --out-dir ./gen`
- `gflow image t2i --aspect 9:16 --ui-mode classic --profile <profile> "prompt" --out-dir ./scenes`
- `gflow credits list` / `gflow credits user --profile <profile>` (free)

After any route: RIFE retime + `build.py` layout (see [README](README.md)).
