# Part N: <short beat name>

Copy this file to `<story>/scenes/partN.md` for every part. All generated images and clips: **vertical 9:16**, illustration only, no text.
Fill order: table -> start prompt -> start image -> end-edit prompt -> end image -> pair check -> **transition prompt LAST** (written from the two finished images) -> prompt check -> clip.

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
| One-way motion | what moves, in which direction, how fast (slow); camera locked, no zoom (planning idea; the final wording comes from the images) |
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

**Transition (fill LAST, after `partN_start.png` and `partN_end.png` both exist; motion only, timed beats):**
Look at both images and describe exactly what turns the start image into the end image, using the elements, positions and props they show. Why: a second-by-second plan that matches both images leaves the generator nothing to guess, which prevents jumps, backward motion, freezes or stutter, objects vanishing or morphing, and an ending that misses the end image (Derinkuyu clip 4: prompt "stone door rolls shut", end frame a ventilation shaft -> morph). Pick the layout for the clip length:

8 s
```
Static locked camera, no zoom, no pan. One single slow one-way action.
0-1 s: exactly the start image: <describe it as it is>; motion just begins.
1-3 s: <element> moves <where> <direction>.
3-5 s: <same element> continues <direction>, <secondary effect: light, dust, water> follows.
5-7 s: <element> nears <end position>; <effect> settles.
7-8 s: settles exactly on the end image: <describe the end image>.
Soft watercolor washes and thin ink lines stay steady. no text, no letters, no captions
```
6 s: beats 0-1 s (start image) / 1-3 s / 3-5 s / 5-6 s (settles exactly on the end image).
4 s: beats 0-0.5 s (start image) / 0.5-2 s / 2-3.5 s / 3.5-4 s (settles exactly on the end image).

Transition prompt check (before generating):
- [ ] written after both images existed (date/time after the end image)
- [ ] **elements match**: every element named is visible in the images; nothing added
- [ ] **positions match**: left/right/foreground/background as in the images
- [ ] **props match**: same objects, light source, weather as the images
- [ ] **no contradictions**: direction and end state lead exactly from the start image to the end image
- [ ] beats match the chosen clip length (4/6/8 s); first beat = start image, last beat = end image; one single one-way action, no second action or reversal
- [ ] **rewritten after any regeneration** of the start or end image (and checked again)

## QA (QA bot watches; any fault -> fix -> re-QA)
- [ ] **Gate 0 pair**: start and end side by side with the references: same style, same shot, only the action changed; no lettering; both height > width
- [ ] **Gate 0 prompt**: transition prompt passes the check above
- [ ] **Gate 1 clip** (`qa_check.py clip` + `seam`): follows the timed beats, 9:16, first/last frame match the pair, seam with part N-1 (continuous or themed), one-way motion, no glitches/distortions, no text, no frozen stretch, length covers the narration
- [ ] **Gate 2 upscale** (Grok / non-720p tools only; skip for Flow, `qa_check.py sharp`): sharper, watercolor grain kept
- [ ] QA result: PASS / faults: ...  (date, round)
- [ ] user approval (part 1 = sample)

---
### Worked example (Derinkuyu door, rewritten in the new format)
The start image is the real Derinkuyu Krea pick of the stone door (scene 6). The end image is the edit of that start (described here, since Derinkuyu was made with the old method). The transition prompt is written only after looking at both.

| Field | Value |
|---|---|
| Narration | "When danger came, massive stone doors rolled shut from the inside. Each floor could be sealed." (16 words, ~6.5 s -> 8 s clip) |
| Start frame (real pick) | arched tunnel opening in soft tuff rock; a huge round stone door, carved like a millstone, stands in the right half of the arch; warm golden light shines through the open gap on the left; dust swirls drawn on the floor; cool green-grey walls; muted rose wash at the top |
| End frame (edit of the start) | same arch, walls, floor, colours and camera; the door has rolled left and fills the whole opening; only a thin warm rim of light shows around its edge; dust raised in the air in front of it |
| One-way motion | the door rolls right -> left across the opening; light narrows; dust lifts |
| Accent colour | warm golden light from the gap |
| References | `derinkuyu-02-middle.jpg`, `derinkuyu-03-late.jpg` |

Transition prompt (8 s, written from the two images):
```
Static locked camera, no zoom, no pan. One single slow one-way action.
0-1 s: exactly the start image: arched tuff tunnel, the huge round stone door stands in the right half of the arch, warm golden light shines through the open gap on the left, dust swirls on the floor; the door just starts to move.
1-3 s: the stone door rolls slowly to the left along the floor of the arch, the gap of light on the left becomes narrower.
3-5 s: the door keeps rolling left past the middle of the arch, the golden light shrinks to a thin band, dust starts to lift from the floor in front of it.
5-7 s: the door reaches the left side of the arch and covers almost the whole opening, dust hangs in the air.
7-8 s: settles exactly on the end image: the door fills the whole arch, only a thin warm rim of light around its edge, dust drifting in front; walls and floor unchanged.
Soft watercolor washes and thin ink lines stay steady. no text, no letters, no captions
```
Prompt check: elements (arch, door, light, dust, walls) all in both images; door right -> left as the images show; light source unchanged (left gap); no lantern or people added; one action only.
