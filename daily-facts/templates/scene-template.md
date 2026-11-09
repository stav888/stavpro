# Part N: <short beat name>

Copy this file to `<story>/scenes/partN.md` for every part. All generated images and clips: **vertical 9:16**, illustration only, no text.

| Field | Value |
|---|---|
| Part / clip | N of TOTAL |
| Narration (English, <= ~18-20 words, <= 8 s) | "<exact line(s) from script.txt>" |
| Words / est. seconds | <words> / <s> (measured after TTS: <s>) |
| Beat | what the viewer must understand in this part |
| Setting | place, era, time of day, light |
| Characters and props | who/what is in frame, clothing, key objects (period-correct) |
| Start frame (`partN_start.png`) | exact composition: subject position, scale, camera height, what is happening at t=0 |
| End frame (`partN_end.png`) | the SAME shot after the action: only these things changed: ... |
| One-way motion | what moves, in which direction, how fast (slow); camera locked, no zoom |
| Accent colour | the one warmer/brighter accent in the muted palette (e.g. lantern amber, sunset rose, teal water) |
| References used | `reference-images/<file>.jpg`, `reference-images/<file>.jpg` (2-3) |
| Continuity | start = end of part N-1? (yes/no, what carries over: light, props, palette) |
| Transition to next part | themed, slow: paper tear / ink bloom / golden light / cloud or fire wash |
| Clip settings | Flow Veo 3.1 Lite, 9:16, 4/6/8 s, **720p directly** (no test, no upscale); or Grok Imagine 2 x 4 s chained, 480p test + upscale (non-720p tools only) |

## Prompts

**Start frame (Krea, trained style, aspect 9:16):**
```
arete style, <subject, setting, light, mood, composition filling the width, calm lower third>,
soft watercolor illustration, thin delicate ink outlines, muted pastel colors, dreamy historical
atmosphere, vertical 9:16, no text, no letters, no captions, no numbers, not photorealistic
```

**End frame (image edit FROM partN_start.png, aspect 9:16):**
```
Same image, same camera, framing, scale, palette and watercolor ink style. Only change: <the action
has progressed: ...>. Keep everything else identical. no text, no letters, no captions
```

**Transition (motion only, for the video model):**
```
Slow continuous one-direction motion: <what moves from the start state to the end state>. Static
locked camera, no zoom, no pan, no loop, no reverse. Soft watercolor and thin ink lines stay steady.
no text, no letters, no captions
```

## QA (QA bot watches; any fault -> fix -> re-QA)
- [ ] **Gate 0 pair**: start and end side by side with the references: same style, same shot, only the action changed; no lettering; both height > width
- [ ] **Gate 1 clip** (`qa_check.py clip` + `seam`): 9:16, first/last frame match the pair, seam with part N-1 (continuous or themed), one-way motion, no glitches/distortions, no text, no frozen stretch, length covers the narration
- [ ] **Gate 2 upscale** (Grok / non-720p tools only; skip for Flow, `qa_check.py sharp`): sharper, watercolor grain kept
- [ ] QA result: PASS / faults: ...  (date, round)
- [ ] user approval (part 1 = sample)

---
### Worked example (Derinkuyu, rewritten in the new part format)
| Field | Value |
|---|---|
| Narration | "When danger came, massive stone doors rolled shut from the inside. Each floor could be sealed." (16 words, ~6.5 s) |
| Start frame | narrow tuff tunnel, huge round millstone door standing open in its side groove, lantern on the floor, cool grey stone |
| End frame | same shot, the stone disc has rolled across and seals the tunnel, a little dust in the air |
| One-way motion | the disc rolls left to right along its groove and stops; dust drifts down; camera locked |
| Accent colour | lantern amber |
| References | `derinkuyu-02-middle.jpg`, `derinkuyu-03-late.jpg` |
| Transition prompt | Slow continuous one-direction motion: the massive round stone door rolls from left to right along its carved groove until it seals the tunnel, dust drifts down. Static locked camera, no zoom, no pan, no loop. no text, no letters, no captions |
