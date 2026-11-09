# Krea — browser workflow

**Primary method: the web UI in the box's Chrome** (signed-in Krea session), operated by the bot's browser/desktop agent.
- Site: https://www.krea.ai/video

## Models worth trying for this style
These are shown in Krea's model list. The input fields are from Krea's model schemas, read on 2026-11-09.

| Model | Start frame | End frame | Resolution | Duration | 9:16 |
|---|---|---|---|---|---|
| MiniMax H3 Max | yes | yes | 480p / 768p / 1080p | 5–15 s | yes |
| LTX-2 19B (Lightricks) | yes | – | 512p / 768p | default 5 s | yes (default 9:16); generates audio by default, so turn it off |
| Seedance 1.0 Pro (ByteDance) | yes | yes | 720p / 1080p | default 5 s | yes |

Others in the list include Kling 2.5–4, Seedance 2/2.5, Veo 3.1, Hailuo, Runway Gen-4, Luma Ray 2 and Grok Imagine.

**Clip length is flexible:** choose per scene what looks right for the narration slot. RIFE retimes it to the exact slot afterwards.

## Approximate costs (estimates from the user; may be outdated)
| Model | Setting | ~Credits |
|---|---|---|
| MiniMax H3 Max | 480p, 5 s | ~130 |
| LTX-2 19B | 512p, 5 s | ~34 |
| Seedance 1.0 | 480p, 4 s | ~31 |

Check the cost shown in the UI before generating.

## Steps in the web UI (labels may change)
1. Open krea.ai/video in box Chrome and confirm the workspace balance.
2. Pick the model, then **upload the start image** (`scenes/sceneN.jpg`), plus an **end image** if the model supports it.
3. Set **aspect 9:16**, resolution and duration. Turn off audio if offered (we add our own narration).
4. Prompt: one-direction motion, "locked static camera, no zoom, no pan", no text.
5. Generate one clip, preview it, and **download** the MP4 to `/home/box/Downloads/`. Move it to `/workspace/<story>/gen/sN.mp4`.
6. Continue with RIFE + layout.

## Rules
- No buying credits, plans or compute packs unless the user explicitly asks.
- If the balance is short, stop and tell the user. Don't switch to another model on your own.

## Secondary note
A Krea MCP connector (`generate_video`, `list_models`, `get_model_schema`, `get_balance`) is connected to the bot. It is not the method; use it only if the user asks. Its `preflight` mode returns a cost quote without charging.
