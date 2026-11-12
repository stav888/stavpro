# The Great Emu War

- **YouTube title:** **not found.** No Buffer title or SEO title file was found (the video has not been uploaded or scheduled). The working name in the files is “The Great Emu War” / “מלחמת האמו”.
- **Status:** In production as of the 2026-11-09 / 2026-11-12 work. Final v2 was assembled and sent to QA; nothing has been uploaded or scheduled (per the production log and the standing “no upload without approval” rule).
- **Publish / schedule time:** not scheduled
- **Final version / length:** v2, `/workspace/emu-war/final/emu_war_final_v2.mp4`, 1080×1920, 24 fps, 46.31 s (v1 ~48.9 s was kept beside it). Upscale: Lanczos (no Vulkan GPU for Real-ESRGAN).
- **Narration method:** Chatterbox am_eric, seed 7, exaggeration 0.6, cfg 0.45; one take per paragraph; p8 later re-rendered for a stronger “A”; loudnorm −16.
- **Completeness:** partial — full English narration and the clip/transition prompts are on the box; GenerateImage still/sketch prompts were not found.
- **Primary sources:** `/workspace/emu-war/prompts/`, `/workspace/emu-war/clips/*prompt*.txt`, `/workspace/emu-war/audio/p1.txt`–`p9.txt`, `/workspace/emu-war/script-proposal.md`, `/workspace/emu-war/PRODUCTION_LOG.md`.

Nothing in this file was invented. Missing prompt classes are marked **not found**.

## Script / narration

Approved English narration as recorded, one paragraph file per part (part 9 uses this revised wording, not the earlier line in the approval table):

### `p1.txt`

Source: `/workspace/emu-war/audio/p1.txt`

```
In 1932 Western Australia, the army went to war against twenty thousand emus.
```

### `p2.txt`

Source: `/workspace/emu-war/audio/p2.txt`

```
After World War One, soldier-settlers farmed tough wheat land near Campion and Walgoolan.
```

### `p3.txt`

Source: `/workspace/emu-war/audio/p3.txt`

```
About twenty thousand migrating emus smashed fences and ruined the struggling harvest.
```

### `p4.txt`

Source: `/workspace/emu-war/audio/p4.txt`

```
On November second, Major Meredith rolled out with two Lewis guns and ten thousand rounds.
```

### `p5.txt`

Source: `/workspace/emu-war/audio/p5.txt`

```
But the tall birds simply jogged through the wheat, ignoring the gunfire.
```

### `p6.txt`

Source: `/workspace/emu-war/audio/p6.txt`

```
At a Campion dam, over a thousand emus closed in — then the Lewis gun jammed.
```

### `p7.txt`

Source: `/workspace/emu-war/audio/p7.txt`

```
They mounted a gun on a truck, but the ride was too rough to fire a shot.
```

### `p8.txt`

Source: `/workspace/emu-war/audio/p8.txt`

```
A second campaign began. Meredith claimed nine hundred eighty-six kills — ten rounds each.
```

### `p9.txt`

Source: `/workspace/emu-war/audio/p9.txt`

```
Meredith said the birds faced machine guns like tanks. Parliament laughed; later, bounties worked better.
```

The Hebrew approval document and part-by-part table are in `/workspace/emu-war/script-proposal.md`. Part 9 in that table still has the earlier English line “He said they faced guns like tanks. Parliament mocked them; later, bounties worked better.” The recorded line, used in the video, is the `p9.txt` text above. The table’s Hebrew start/end columns are planning descriptions, not the GenerateImage prompts actually submitted, so they are not copied here as image prompts. The file is left in place on the box rather than pasted in full, to keep this archive focused on the prompts and the narration that was actually used.

## Per-scene image and animation prompts

Nine parts, matching the recorded narration. **Image / sketch prompts were not found** for any part (start/end stills exist as images under `/workspace/emu-war/scenes/`, but the GenerateImage text was not saved). Animation prompts below are copied verbatim from the production files. Sources are short file paths.

### Part 1

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Used wording for the continuous 8s v2 take that shipped in final v2. Source: `/workspace/emu-war/clips/part1_v2_prompt_used.txt`.

```
Slow continuous one-direction motion matching the actual start and end sketches. The soldier stays at the same horizontal place on the left (same x); only a small weight shift and a slight lift of his front foot toward the end pose. Do NOT walk him across the frame. Do NOT move him right then left. All new motion is the emus entering from the RIGHT EDGE only.

What the sketches show:
- Start: large solid-black Australian Army officer left-of-centre facing right, peaked cap, white eyes, thin stick limbs; Lewis gun held aimed right with a constant tiny red ring near the muzzle; ONE tall black emu on the right facing left; low post-and-rail fence always on the far left; sparse ground scribbles; pure white background.
- End: same soldier at the SAME left x with a slight weight shift / front foot slightly lifted; SAME gun and constant red muzzle ring; THREE clearly separate black emu silhouettes in a row on the right (white gaps between them); same fence left; same framing.

Timed beats (8 s total, ONE continuous clip):
- 0–1 s: motion starts immediately — tiny living motion / weight shift on the soldier; the single emu may shift slightly in place; NO freeze hold; fence fully visible; red muzzle ring constant
- 1–3 s: a SECOND emu walks in from the RIGHT EDGE of the frame and stops fully to the RIGHT of the soldier and to the right of the first emu; NEVER crosses, overlaps, or passes behind/through the soldier; fence stays fixed and visible; red ring constant; no muzzle flash
- 3–5 s: a THIRD emu walks in from the RIGHT EDGE and joins the row on the right; three emus remain clearly separate with white space between bodies; soldier stays at same x with only slight weight shift; fence fixed; red ring constant
- 5–7 s: three clearly separate emu silhouettes stand in a stable row on the right facing the soldier; no merging into one blob; soldier small living motion only at same x
- 7–8 s: settles on the end-image state with only slight living motion (no frozen hold) — soldier same left x, front foot slightly lifted, Lewis aimed right, constant red muzzle ring, three separate emus on the right, fence still fully visible left

Hard rules: static locked camera, no zoom, no pan, no camera movement, no loop, no reverse, no ping-pong. Fence stays fixed and always visible the whole time. Red muzzle ring stays constant; no muzzle flash. Emus only on the right half; never enter through or behind the soldier. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines. no text, no letters, no captions.

---
Delivered take used GenerateVideo try2 wording (same rules, stronger living-motion / red / separation emphasis). Approach: ONE continuous 8s clip, image_path=part1_start.jpg, last_frame_path=part1_end.jpg, duration=8, resolution=480p, aspect_ratio=9:16.
```

Other animation prompt versions found for this part (not the final v2 take):

**Canonical `prompts/part1.txt` (continuous 8s rules).** Source: `/workspace/emu-war/prompts/part1.txt`.

```
ONE continuous clip. Ian Xiaohei ink style. Pure white background. Locked static camera, no zoom, no pan, no loop, no reverse, no ping-pong.

CRITICAL — SOLDIER LOCKED IN PLACE: keep the soldier at the exact same left x the whole time. ONLY subtle breathing / tiny weight shift. NO lean left or right, NO lunge, NO step, NO walk cycle, NO body slide. His silhouette x must stay fixed.

CRITICAL — RED MUZZLE RING: a tiny bright red ring on the Lewis gun muzzle tip must stay clearly visible and constant in EVERY frame from first to last. Never blink off. No muzzle flash.

CRITICAL — LIVING MOTION THROUGH THE END: keep light living motion the whole time, especially 6.5–7.5 s — emu head bobs, slight feather ruffle, tiny soldier breath. NEVER freeze or near-freeze.

CRITICAL — fence on the far left stays fixed and fully visible every frame.
CRITICAL — emus only on the right half; enter only from the RIGHT EDGE; never cross/overlap the soldier; keep three distinct emu heads (bodies may lightly touch).

Start: soldier left locked, peaked cap, Lewis aimed right with constant red muzzle ring, ONE emu right, fence left.
End: same soldier SAME locked left x (only subtle breath / tiny weight shift), SAME constant red ring, THREE emu heads in a row on the right, same fence.

Timed beats:
- 0–1 s: motion starts immediately — subtle breath only; one emu slight living motion; red ring ON; fence ON; no hold
- 1–3 s: second emu walks in from RIGHT EDGE; soldier LOCKED; red ring ON
- 3–5 s: third emu walks in from RIGHT EDGE; three distinct heads; soldier LOCKED; red ring ON
- 5–7 s: three emu heads stable on the right with light head-bobs / feather ruffle; soldier LOCKED with only breath; red ring ON; NO lean, NO morph rewrite of pose/gun
- 7–8 s: continue light living motion into the end state (no freeze) — soldier still LOCKED same x, red ring ON, three emu heads, fence ON

no text, no letters, no captions.
```

**Earlier Clip A plan (not used in final v2).** Source: `/workspace/emu-war/clips/part1_a_prompt.txt`.

```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (8 s total, Grok chain 2×4 s):

Clip A (0–4 s) — from part1_start.jpg:
- 0–1 s: exact start-image state — large solid-black Australian Army officer left-of-centre facing right, peaked cap, white dot eyes, thin stick limbs; Lewis gun held in both hands aimed right with tiny red accent near the muzzle; one tall black emu silhouette on the right facing left (long neck, small head); low post-and-rail fence on the far left behind the soldier; sparse ground scribble lines; pure white background
- 1–2 s: soldier begins one step toward the right; body shifts slightly forward; gun stays aimed right
- 2–3 s: step continues; a second emu silhouette starts to appear on the far right behind the first
- 3–4 s: soldier mid-step; two emus visible on the right; motion continues toward the end state (no reverse, no freeze)

```

**Earlier Clip A wording actually submitted (not used in final v2).** Source: `/workspace/emu-war/clips/part1_a_prompt_used.txt`.

```
Slow continuous one-direction motion matching the start sketch. Timed beats (4 s):
- 0–1 s: exact start state — large solid-black Australian Army officer left-of-centre facing right, peaked cap, white dot eyes, thin stick limbs; Lewis gun held in both hands aimed right with tiny red accent near the muzzle; one tall black emu silhouette on the right facing left; low post-and-rail fence on the far left; sparse ground scribbles; pure white background
- 1–2 s: soldier begins one step toward the right; body shifts slightly forward; gun stays aimed right
- 2–3 s: step continues; a second emu silhouette starts to appear on the far right behind the first
- 3–4 s: soldier mid-step; two emus visible on the right; motion continues forward (no reverse, no freeze)

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects. no text, no letters, no captions.
```

**Earlier Clip B wording actually submitted (not used in final v2).** Source: `/workspace/emu-war/clips/part1_b_prompt_used.txt`.

```
IMPORTANT: begin exactly on this image and change it only slowly. Continue one continuous one-way motion toward the end state.

From the current frame: large solid-black Australian Army officer mid-stride facing right, peaked cap, white eyes, Lewis gun aimed right with tiny red near muzzle; two black emu silhouettes (one near/behind soldier, one on the right); sparse ground lines; pure white background.

Timed beats (4 s):
- 0–1 s: keep the same composition; soldier continues the same step slightly further right; third emu begins to appear on the far right; restore/keep a low fence on the far left if missing
- 1–2 s: three emu silhouettes form a row filling the right side, facing the soldier; soldier keeps stepping right
- 2–3 s: soldier finishes the step (right leg forward); body settles; gun still aimed right with red muzzle accent; fence left
- 3–4 s: settles on end state — soldier one pace right mid-stride, Lewis aimed right, three black emus filling the right, low fence left, same white background

No sudden jump, no morphing faces, no vanishing limbs, no new unrelated objects. Static locked camera, no zoom, no pan, no loop, no reverse. Same Ian Xiaohei ink style, thin wobbly black lines. no text, no letters, no captions.
```

**Part 1 v3 3s tail-retry prompt (not used in final v2).** Source: `/workspace/emu-war/prompts/part1_tail3s.txt`.

```
Continue ONE continuous 3-second clip from this exact mid frame to the end sketch. Ian Xiaohei ink style. Pure white background. Locked static camera, no zoom, no pan, no loop, no reverse.

CRITICAL — SOLDIER LOCKED IN PLACE at the same left x as this start frame. ONLY subtle breathing / tiny weight shift. NO lean left or right, NO lunge, NO step, NO walk, NO body slide.

CRITICAL — RED MUZZLE RING on the Lewis gun tip stays clearly visible and constant in EVERY frame. Never blink off. No muzzle flash.

CRITICAL — keep light living motion the whole 3 seconds: emu head bobs, slight feather ruffle, tiny soldier breath. NEVER freeze or near-freeze, especially not in the last 1.5 s.

CRITICAL — fence far left stays fixed and fully visible. Three distinct emu heads already on the right stay on the right (bodies may lightly touch); do not merge heads; do not add a walk cycle.

From this frame (already ~3 emus on the right, soldier left with gun + red ring, fence left) to the end sketch (same locked soldier x, three emu heads, same fence, same red ring).

Timed beats (3 s):
- 0–1 s: continue immediately with light living motion; soldier LOCKED; red ring ON; emu heads bob slightly
- 1–2 s: feather ruffle / head bobs; soldier LOCKED breath only; red ring ON; no morph of gun/pose
- 2–3 s: settle toward end image with continued micro-motion (no freeze); soldier LOCKED same x; red ring ON; three distinct emu heads; fence ON

no text, no letters, no captions.
```

### Part 2

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Only saved part 2 prompt file. Final v2 used part 2 v3; a distinct v3 prompt file was not found. Source: `/workspace/emu-war/prompts/part2.txt`.

```
Slow continuous one-direction motion matching the actual start and end sketches. Ian Xiaohei ink style, pure white background. Locked static camera, no zoom, no pan, no loop, no reverse.

The farmer stays at the same left x. Motion: he slowly kneels / crouches down beside the wheat (toward the end pose). Wheat heads droop a little more. Tiny orange sun stays fixed upper right. No new characters.

Start: large black settler-farmer left with peaked cap standing beside wheat stalks; orange sun upper right; white bg.
End: same farmer same left x kneeling/crouching, touching drooping wheat; same sun.

Timed beats (6 s):
- 0–1 s: exact start; light living motion begins immediately (no freeze); sun and wheat visible
- 1–3 s: farmer begins to bend knees / lower body; wheat tips start to droop; same x
- 3–5 s: continues kneeling down toward end pose; wheat droops more; living motion
- 5–6 s: settles on end pose with slight living motion (no freeze) — kneeling farmer, drooping wheat, sun fixed

no text, no letters, no captions.
```

### Part 3

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 3 v2, used in final v2. Source: `/workspace/emu-war/prompts/part3_v2.txt`.

```
ONE continuous 6s clip from the actual start and end sketches. Ian Xiaohei ink, pure white background. Locked static camera, no zoom, no pan, no loop, no reverse.

Farmer LOCKED at same left x behind the fence — only subtle breath. Emus enter ONLY from the RIGHT EDGE and walk left toward a fence gap; never through/behind the farmer. Grow 1→3 distinct emus. Tiny blue eye accents CONSTANT every frame. Fence develops a broken gap; wheat flattens. CONTINUOUS living motion the whole time — emu head bobs, steps, feather ruffle. NEVER freeze or near-freeze, especially not in the last 2 seconds.

Timed beats (6 s):
- 0–1 s: exact start living immediately (no hold); 1 emu right; fence intact; blue eyes ON
- 1–2.5 s: second emu walks in from RIGHT EDGE; farmer locked; continuous motion
- 2.5–4 s: third emu from RIGHT EDGE; fence gap opens; wheat tramples; keep moving
- 4–5.5 s: three emus settle mid-right with ongoing head bobs / weight shifts; NO freeze
- 5.5–6 s: living settle on end image (still micro-motion, no freeze)

no text, no letters, no captions.
```

Other animation prompt versions found for this part (not the final v2 take):

**Part 3 v1 (not used in final v2).** Source: `/workspace/emu-war/prompts/part3.txt`.

```
ONE continuous 6s clip. Ian Xiaohei style, pure white background. Locked static camera, no zoom, no pan, no loop, no reverse.

CRITICAL — farmer LOCKED at same left x behind the fence. ONLY subtle breath. NO walk.

CRITICAL — emus enter ONLY from the RIGHT EDGE, walk left toward the fence gap, never through/behind the farmer. Grow from 1 to 3 distinct emus. Tiny blue eye accents stay visible.

Fence gains a broken gap; wheat gets trampled flatter. Light living motion to the end; no freeze.

Start: farmer left behind intact fence; one emu on the right; blue eye; wheat.
End: same farmer same left x; broken fence gap; three emus mid-right; blue eyes; flatter wheat.

Beats: 0–1s start living; 1–3s second emu from right edge; 3–5s third emu from right + fence gap opens; 5–6s living settle on end.
no text, no letters, no captions.
```

### Part 4

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 4 v2, used in final v2. Source: `/workspace/emu-war/prompts/part4_v2.txt`.

```
ONE continuous 6s clip matching the actual start and end sketches. Ian Xiaohei ink, pure white background. Locked static camera, no zoom, no pan, no loop, no reverse.

Meredith LOCKED at same left x. ONLY motion: slowly raise the Lewis gun from low at his side up to waist height aimed right. Tiny RED ring on the muzzle/cooling tip must stay clearly visible and CONSTANT in EVERY frame — never blink off, no muzzle flash. Fence left and wheat right stay fixed. CONTINUOUS living motion throughout (micro breath + smooth gun raise). NEVER freeze or near-freeze.

Timed beats (6 s):
- 0–1 s: exact start; living motion begins immediately; red ring ON and bright
- 1–3 s: gun rises smoothly from side toward hip; red ON; no morph jolts
- 3–5 s: gun continues to waist aim-right; red ON; farmer/soldier locked x
- 5–6 s: living settle on end pose with red still ON (no freeze, slight breath)

no text, no letters, no captions.
```

Other animation prompt versions found for this part (not the final v2 take):

**Part 4 v1 (not used in final v2).** Source: `/workspace/emu-war/prompts/part4.txt`.

```
ONE continuous 6s clip. Ian Xiaohei, white bg. Locked camera, no zoom, no pan, no loop, no reverse.
Meredith LOCKED at same left x. ONLY motion: raise Lewis gun from low at side up to waist aim-right. Tiny red muzzle/cooling ring CONSTANT every frame. Fence and wheat fixed. Living motion; no freeze.
Start: gun low at side. End: gun at waist aimed right. Same x.
Beats: 0–1s start living red ON; 1–3s gun begins rising; 3–5s rises to waist; 5–6s living settle end, red ON.
no text, no letters, no captions.
```

### Part 5

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 5 v1, used in final v2 (retime only). Source: `/workspace/emu-war/prompts/part5.txt`.

```
ONE continuous 6s. Ian Xiaohei, white bg. Locked camera, no zoom/pan/loop/reverse.
Soldier LOCKED same left x aiming right; red muzzle ring CONSTANT. Emus jog left from right edge to mid-right only — never through soldier. Blue eye accents stay. Living motion; no freeze.
Start: 2 emus at far right. End: 2 emus mid-right. Soldier same x.
Beats: 0–1 living; 1–4 emus jog left; 4–6 living settle.
no text, no letters, no captions.
```

### Part 6

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 6 v1, used in final v2 (hold-drop retime). Source: `/workspace/emu-war/prompts/part6.txt`.

```
ONE continuous 6s. Ian Xiaohei, white bg. Locked camera, no zoom/pan/loop/reverse.
Soldier LOCKED same left x. Red muzzle CONSTANT. Emus scatter right/up from cluster — stay on right half, never through soldier. Gun tilts to jammed pose. Living motion; no freeze.
Start: aimed, 3 emus clustered. End: gun jammed tilt, emus scattered right.
Beats: 0–1 living; 1–3 scatter begins + gun tip tilts; 3–5 scatter finishes; 5–6 living settle.
no text, no letters, no captions.
```

### Part 7

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 7 v1, used in final v2 (retime). Source: `/workspace/emu-war/prompts/part7.txt`.

```
ONE continuous 6s. Ian Xiaohei, white bg. Locked camera, no zoom/pan/loop/reverse.
Truck tilts/bounces one way as if rough ride; soldier on bed wobbles but stays on truck; red muzzle CONSTANT; emus move farther right escaping. Living motion; no freeze; no reverse bounce loop.
Start: truck level, soldier steady, emus mid-far right. End: truck tilted, soldier off-balance, emus farther right.
Beats: 0–1 living; 1–3 truck begins tilt; 3–5 tilt peaks + soldier wobbles; 5–6 living settle.
no text, no letters, no captions.
```

### Part 8

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 8 v1, used in final v2 (hold-drop retime). Source: `/workspace/emu-war/prompts/part8.txt`.

```
ONE continuous 6s. Ian Xiaohei, white bg. Locked camera, no zoom/pan/loop/reverse.
Meredith LOCKED same left x. Raises blank paper and points; gun stays low with red ring CONSTANT if visible. Background emus shrink/fewer. Living motion; no freeze.
Start: gun low, 2 small emus. End: paper up, pointing, fewer emus.
Beats: 0–1 living; 1–4 raise paper/point; 4–6 living settle.
no text, no letters, no captions.
```

### Part 9

- **Image / sketch prompt:** **not found.** No GenerateImage / still-sketch prompt was saved for this scene, and none was found in the transcripts or project files searched for this update.

- **Animation / clip prompt (used in final v2):** Part 9 v1, used in final v2 (hold-drop retime). Source: `/workspace/emu-war/prompts/part9.txt`.

```
ONE continuous 8s. Ian Xiaohei, white bg. Locked camera, no zoom/pan/loop/reverse.
Meredith LOCKED same left x. Lowers gun; emu stands firm; small farmer+blank bounty token appears bottom-right; red ring CONSTANT; parliament outline fixed. Living motion throughout especially 6.5–7.5s; no freeze.
Start: pointing at tank-like emu. End: gun lowered, bounty token, farmer icon, emu firm.
Beats: 0–2 living point; 2–5 lower gun; 5–7 bounty/farmer appear with living motion; 7–8 living settle.
no text, no letters, no captions.
```
