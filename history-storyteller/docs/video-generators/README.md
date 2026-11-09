# Image-to-video generators — options

The pipeline needs one **image-to-video** clip per scene, animated from the approved Xiaohei still. **Grok Imagine** (the built-in GenerateVideo tool) is the current default. The three alternatives below are run **in the browser**: the box's Chrome with signed-in sessions, operated by the bot's browser/desktop agent. Their CLI/MCP routes exist but are only secondary notes.

| Option | Provider / model | Resolution | Clip length | Approx. cost | How it's run | Pros | Cons | When to use |
|---|---|---|---|---|---|---|---|---|
| [Grok Imagine](grok-imagine.md) (**default**) | xAI Grok Imagine via the Grok Bot built-in `GenerateVideo` | 480p by default (Garbo clips were 640x480, 24 fps) | 1–15 s | Grok Bot plan usage (one ~1-minute video ≈ 8–10% of the plan, user measurement) | built-in tool call, no browser | no logins, simple, proven on 13 videos | low resolution (RIFE + layout compensate); plan usage | the normal choice |
| [Google Flow](google-flow.md) | Google Veo 3.1 (Lite / Fast / Quality), Omni Flash | 720p (Veo 3.1 Lite was used) | 4 / 6 / 8 s (Omni Flash up to 10 s) | ~10 Flow credits per Veo Lite clip; each account has free daily credits | **browser**: flow.google.com in box Chrome, rotating between all signed-in profiles | high quality, start **and** end frame, 9:16 native, free daily credits | daily credit limits, manual rotation, UI changes | when quality matters or plan usage must be saved |
| [Krea](krea.md) | Krea: MiniMax H3 Max, LTX-2 19B, Seedance, Kling, Veo, Hailuo… | 480p–1080p by model | flexible per model (e.g. H3 Max 5–15 s) | **estimates, may be outdated:** H3 Max 480p 5 s ~130 credits; LTX-2 19B 512p 5 s ~34; Seedance 1.0 480p 4 s ~31 | **browser**: krea.ai/video in box Chrome | many models in one place, start/end frames on several | paid credits; costs vary per model | to compare models or for a hard scene |
| [Hugging Face Space](huggingface.md) | Wan 2.2 14B I2V (Lightning LoRA) Space | output rounded to multiples of 32 px | default 3.5 s (set per run) | free with ZeroGPU quota | **browser**: the Space page on huggingface.co | free, optional last frame | queue and quota limits; shorter clips; quality varies | free fallback / experiments |

## Same rules after any generator
1. One-direction, progressive motion per clip. No loop, ping-pong, reverse, freeze, zoom or pan (camera locked in the prompt).
2. RIFE 4.7 motion-equalized retime to the scene slot at true 24 fps (`../../scripts/video/rife_eq.py`), then jolt fixes. Never interpolate across a cut.
3. Layout into 1080x1920 with `../../scripts/video/build.py` (crop to art, scale, title, subtitles).
4. QA סרטונים check before delivery.

## Spending rules (all options)
- Never buy credits, plans or subscriptions unless the user explicitly asks.
- Don't generate before the user has approved the script and the sample frame.
- Check the balance first. If it isn't enough, stop and tell the user.
