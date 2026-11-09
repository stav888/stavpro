# Video generators used for Daily Facts Arete

All costs are **estimates** from our own runs and the services' pages at the time; check the live balance before every run. Never buy plans or credits unless the user explicitly asks.

| Generator | Role | Used in | Output | Cost (estimate) | Doc |
|---|---|---|---|---|---|
| **Google Flow, Veo 3.1 Lite** | current clip source (start + end frame per clip) | Giza (first Flow test), Hanging Gardens, Derinkuyu | 720x1280, ~8 s, with ambience audio | ~10 Flow credits per clip (daily free credits) | [google-flow.md](google-flow.md) |
| **Krea** (trained style + LTX video) | all stills (always); LTX clips were planned/tested | every video (stills) | stills ~720x1280; LTX 5 s clips | ~2 units per image; LTX-2 19B ~34 units per 5 s (web app), LTX-2.3 22B ~133 units per 5 s (MCP) | [krea.md](krea.md) |
| **Grok Imagine** | image-to-video before Flow | Prague v3, Petra, Alexandria | 720p, 5-6 s | uses the Grok Bot subscription (about 10% of a monthly plan per video, estimate) | [grok-imagine.md](grok-imagine.md) |

Not used for this channel: Hugging Face Wan i2v Spaces, Midjourney (considered only).

## Common rules
- Vertical **9:16** only; verify every clip with `ffprobe` (height > width).
- **No zoom / Ken Burns**; static or very gentle camera, motion inside the scene.
- Prompts always end with `no text` (images: `no text, no letters, no numbers`).
- **One test clip first**, then the rest after it looks right.
- Input frames are always the QA-picked, user-approved Krea stills.
