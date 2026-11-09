# Krea

[Krea](https://www.krea.ai) is used for **every still image** (trained channel style) and was tested for clips (LTX).

## Trained style "Daily Facts Arete Watercolor"
- Trained 2026-10-24 on Krea 2 Medium from 30 frames of the channel's original videos (soft watercolor, thin ink lines, muted pastels).
- Trigger word: **`arete style`**. Training cost ~508 units (one-time, estimate).
- Generation through the **Krea MCP connector** with model `krea-2 medium-turbo` + the style; ~**2 units per image (estimate)**; 9:16 output (~720x1280).
- **Aspect 9:16 is passed explicitly on every call**; check height > width on every result.
- Per part (since 2026-11-09): 2 variants of the **start frame** -> QA pick -> `scenes/partN_start.png`; then the **end frame is an image edit FROM the start frame** (a Krea edit model that is free/non-blocked at the time, e.g. Flux Kontext, with the start frame as input and the same 9:16), so only the action changes. Never two independent images as a start/end pair.
- Before generating: pick 2-3 matching frames from `../../reference-images/` per part and check the results side by side with them (Step 0).
- URLs saved in `<story>/urls.txt`, files in `<story>/krea/`.
- Prompt template and examples: `../images-and-animation.md`, `../../examples/derinkuyu/prompts.txt`, `../../examples/olmec-heads/prompts.txt`.
- Failed image -> regenerate in Krea (never fix by editing on the box).

## Krea video (LTX) (planned / tested, Oct 2026)
LTX models take a start frame only: upload `partN_start.png` + the transition prompt and use `partN_end.png` as the check target. Clip length per part still <= 8 s of narration.

| Model | Where | Cost (estimate) |
|---|---|---|
| LTX-2 19B | Krea web app only | ~33.8 units per 5 s clip |
| LTX-2.3 22B | Krea MCP (cheapest LTX there) | ~133 units per 5 s clip |
Plan at the time: ~12 five-second clips per video (~450 units), stills ~60-80 units, about 510-530 units per video, 7-8 videos on a 5,000-unit monthly plan with ~1,000 reserved for style training. Flow's daily free credits replaced this for clips.

## Model availability
The free/blocked model list (checked on perchance.org/krea) changes over time: recheck before choosing a model, and when the user's own check disagrees, trust his.

## Budget
Never buy units or plans unless the user explicitly asks. Report the remaining balance when it gets low.
