# Video generators used for Daily Facts Arete

All costs are **estimates** from our own runs and the services' pages at the time; check the live balance before every run. Never buy plans or credits unless the user explicitly asks.

| Generator | Role | Used in | Output | Cost (estimate) | Doc |
|---|---|---|---|---|---|
| **Google Flow, Veo 3.1 Lite** | current clip source (start + end frame per clip) | Giza (first Flow test), Hanging Gardens, Derinkuyu | 720x1280, ~8 s (its ambience audio is muted in the edit) | ~10 Flow credits per clip (daily free credits) | [google-flow.md](google-flow.md) |
| **Krea** (trained style + LTX video) | all stills (always); LTX clips were planned/tested | every video (stills) | stills ~720x1280; LTX 5 s clips | ~2 units per image; LTX-2 19B ~34 units per 5 s (web app), LTX-2.3 22B ~133 units per 5 s (MCP) | [krea.md](krea.md) |
| **Grok Imagine** | image-to-video before Flow; now an option (2 x 4 s chained per part, 480p test + Real-ESRGAN 720p) | Prague v3, Petra, Alexandria | 720p, 5-6 s | uses the Grok Bot subscription (about 10% of a monthly plan per video, estimate) | [grok-imagine.md](grok-imagine.md) |

Not used for this channel: Hugging Face Wan i2v Spaces, Midjourney (considered only).

## Common rules (see also [../production-rules.md](../production-rules.md))
- **Step 0 first**: per-part `partN_start` / `partN_end` pair (end made FROM start), checked against `../../reference-images/`, before any video credits.
- One transition prompt per part, motion only.
- Flow: browser by default, gflow-cli only on browser fault / no access; Veo 3.1 Lite, 4/6/8 s, so each part's narration <= 8 s; never click Agent.
- **Flow: generate directly at 720p**; no 480p test, no upscale; QA watches the 720p clip right away.
- The 480p test + Real-ESRGAN upscale is **only for Grok Imagine and other tools that cannot output 720p**: Grok = 2 chained 4 s clips per part at 480p, QA, then upscale to 720p ([../upscale-real-esrgan.md](../upscale-real-esrgan.md)) instead of regenerating.
- Vertical **9:16** only: pass aspect 9:16 explicitly on every image and video call, classic composer, verify every still and clip (height > width), reject landscape.
- **No zoom / Ken Burns**; static or very gentle camera, motion inside the scene.
- Prompts always end with `no text` (images: `no text, no letters, no numbers`).
- **One test clip first**, then the rest after it looks right.
- Input frames are always the QA-picked, user-approved Krea stills.
