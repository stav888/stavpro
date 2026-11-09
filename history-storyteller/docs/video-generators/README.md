# Image-to-video generators — options

The pipeline needs one **image-to-video** clip per scene, animated from the approved Xiaohei still. **Grok Imagine** (the built-in GenerateVideo tool) is the current default. The alternatives run on the box's signed-in Chrome sessions:
- **Google Flow** is worked **directly in Flow's web UI** in the box's Chrome (manual browser operation). The **gflow-cli MCP** is only a **fallback** when the browser route has a fault or no access.
- **Krea** runs through the **Krea MCP connector**, with krea.ai/video in the browser as the fallback (unchanged).
- **Step 0 for every option, before any video credits are spent:** prepare the start frames (and end frames where the model supports them) for every scene **according to** [`../../reference-images/`](../../reference-images/) (38 vertical 9:16 frames from 13 Shorts). Pick 2–3 relevant refs per scene (relative paths), pass them as style references / describe their style, match white background / wobbly black lines / black Xiaohei / composition / minimal accents, check each sketch side by side with those refs and the scene table, regenerate any style drift, and only then spend video credits. All sketches and clips are **vertical 9:16** (never 16:9); always pass aspect `"9:16"` explicitly and verify height > width. This follows the approval flow (script + sample frame).
- **Route failures:**
  - **Flow (browser-primary):** if the browser route has a fault or no access, fall back to the gflow-cli MCP (tell the user). Do not start with MCP when the browser works.
  - **Krea (MCP-primary):** if the MCP route doesn't work (connector or server error, auth failure, missing tool, repeated failures), the bot **offers the user a choice** to switch to manual browser operation, using the web UI steps in the Krea doc. It goes to the browser only after the user picks it.
  - A credit shortage (402 / `insufficient_balance` / no profile with credits) is not a route failure: stop and tell the user, with no buying.
- **Hugging Face** is run directly in the browser by the bot's browser/desktop agent. Its MCP route is only a secondary note.

| Option | Provider / model | Resolution | Clip length | Approx. cost | How it's run | Pros | Cons | When to use |
|---|---|---|---|---|---|---|---|---|
| [Grok Imagine](grok-imagine.md) (**default**) | xAI Grok Imagine via the Grok Bot built-in `GenerateVideo` | 480p by default (Garbo clips were 640x480, 24 fps) | 1–15 s | Grok Bot plan usage (one ~1-minute video ≈ 8–10% of the plan, user measurement) | built-in tool call, no browser | no logins, simple, proven on 13 videos | low resolution (RIFE + layout compensate); plan usage | the normal choice |
| [Google Flow](google-flow.md) | Google Veo 3.1 (Lite / Fast / Quality), Omni Flash | 720p (Veo 3.1 Lite was used) | 4 / 6 / 8 s (Omni Flash up to 10 s) | ~10 Flow credits per Veo Lite clip; each account has free daily credits | **Flow web UI in box Chrome** (classic composer, Veo 3.1 Lite 720p 9:16, start+end frames), rotating between all signed-in profiles; **gflow-cli MCP only as fallback** on browser fault / no access | high quality, start **and** end frame, 9:16 native, free daily credits | daily credit limits; UI labels can change | when quality matters or plan usage must be saved |
| [Krea](krea.md) | Krea: MiniMax H3 Max, LTX-2 19B, Seedance, Kling, Veo, Hailuo… | 480p–1080p by model | flexible per model (e.g. H3 Max 5–15 s) | **estimates, may be outdated:** H3 Max 480p 5 s ~130 credits; LTX-2 19B 512p 5 s ~34; Seedance 1.0 Pro is 720p+ only via the API (the 480p ~31 estimate likely doesn't apply) | **Krea MCP connector** (`generate_video`, `get_job`, `preflight` quote, `get_balance`); krea.ai/video in the browser as fallback | many models in one place, start/end frames + style refs on several, free cost quote | paid credits; API billing may differ from web credits | to compare models or for a hard scene |
| [Hugging Face Space](huggingface.md) | Wan 2.2 14B I2V (Lightning LoRA) Space | output rounded to multiples of 32 px | default 3.5 s (set per run) | free with ZeroGPU quota | **browser**: the Space page on huggingface.co | free, optional last frame | queue and quota limits; shorter clips; quality varies | free fallback / experiments |

## Same rules after any generator
1. One-direction, progressive motion per clip. No loop, ping-pong, reverse, freeze, zoom or pan (camera locked in the prompt).
2. RIFE 4.7 motion-equalized retime to the scene slot at true 24 fps (`../../scripts/video/rife_eq.py`), then jolt fixes. Never interpolate across a cut.
3. Layout into 1080x1920 with `../../scripts/video/build.py` (crop to art, scale, English title/underline/subtitles/counter) — see **Frame layout (mandatory)** in each generator doc; sketches are illustration-only (`no text, no letters, no captions`), large Xiaohei filling most of the width; approval samples via `../../scripts/video/preview_frame.py`.
4. QA סרטונים check before delivery.

## Spending rules (all options)
- Never buy credits, plans or subscriptions unless the user explicitly asks.
- Don't generate before the user has approved the script and the sample frame.
- Check the balance first. If it isn't enough, stop and tell the user.
