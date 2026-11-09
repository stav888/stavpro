# Scene-by-scene production — how to describe and build each part

This guide explains **how to build the video scene by scene** from the approved part-by-part script, and above all **how to describe each scene** so sketches and clips match the Ian Xiaohei style and join cleanly.

Related docs:
- Script table + approval: [`script-writing.md`](script-writing.md)
- Narration (Chatterbox): [`narration.md`](narration.md)
- Style, pairs, RIFE: [`images-and-animation.md`](images-and-animation.md)
- Generators: [`video-generators/README.md`](video-generators/README.md) · [Grok Imagine](video-generators/grok-imagine.md) · [Google Flow](video-generators/google-flow.md) · [Krea](video-generators/krea.md) · [Hugging Face](video-generators/huggingface.md)
- Upscale (standalone, **Grok / sub-720p only**): [`upscale-real-esrgan.md`](upscale-real-esrgan.md)
- Subtitles / assemble: [`subtitles-and-build.md`](subtitles-and-build.md)
- QA / publish: [`qa.md`](qa.md) · [`publishing-buffer.md`](publishing-buffer.md)
- Continuous improvement: [`lessons-learned.md`](lessons-learned.md)

**Hard rules (always):**
- Vertical **9:16** only (e.g. 1080×1920). Never 16:9.
- Illustration **only** in stills and clips: every prompt ends with `no text, no letters, no captions`. All on-screen English text is added later by `build.py` / `preview_frame.py`.
- The name **"Xiaohei"** may appear **only inside image/video prompts**. Never in narration, subtitles, title, or YouTube metadata. The black character plays the real person of that story.
- One continuous **one-way** action per part. Locked camera. No zoom, pan, loop, reverse, or freeze >0.3 s.
- Each part ≤ **8 s** (Flow durations **4 / 6 / 8**). Narration ≈ **18–20 English words** max per part. Never stretch audio.
- **QA at every stage:** send every part clip and the final video to **QA סרטונים**, which **watches** for faults. Fix → QA again. Nothing delivered/scheduled without a QA pass. See [`qa.md`](qa.md).
- **Continuous improvement:** every production better than the last. After each video append [`lessons-learned.md`](lessons-learned.md); read it before the next story.
- **Flow = direct 720p:** Google Flow / Veo 3.1 Lite generates at **720p** with **no 480p test** and **no Real-ESRGAN upscale**. QA watches the 720p clip immediately. The 480p → upscale path is **Grok Imagine only** (and other tools whose max output is below 720p).
- **Transition prompt from the actual sketches (mandatory):** write (or rewrite) `prompts/partN.txt` **after** `scenes/partN_start.jpg` and `scenes/partN_end.jpg` exist, from what those images **actually show** — not only from the planned scene idea. Include a **timed beat breakdown** across the clip (see §1b). If a sketch is regenerated, rewrite the prompt. Check the prompt against both images before spending video credits. **Reason:** leaves the generator nothing to guess, so the clip has **no lag or glitches** (no jumps, reverse, stutter/freeze, vanishing/morphing objects, or mismatched ending).

---

## 0. Approved script table (gate before any sketches)

Present this to the user and **wait for approval** before sketches or clips ([`script-writing.md`](script-writing.md)).

**Up-front summary line (required):**
> This script = **N parts / N clips**, ~T s total (proposed length in the **~50 s – ~1.5 min** band, about **7–11 parts**). Flow estimate: **N × ~10 ≈ C credits** (Veo 3.1 Lite).

Part count = clip count = number of start+end sketch pairs.

| Part | Narration (English) | Words | Est. s | Seconds (4 / 6 / 8) | Start-frame idea | End-frame idea | Prompt (short) |
|---|---|---|---|---|---|---|---|
| 1 | … | ≤20 | ≤8 | 4 / 6 / 8 | … | … | motion only |
| 2 | … | … | … | … | … | … | … |
| … | … | … | … | … | … | … | … |
| **Total** | | | **~T s** | | **N pairs** | | **N clips** |

Rules: each part ≤ **8 s** / ~**18–20 English words**; choose **4, 6 or 8 s** to cover the slot; rewrite or **split** over-length parts (never stretch audio); never put **"Xiaohei"** in narration / titles / metadata. After the table is approved → show **part 1** sample (start + end + `prompts/part1.txt` + `preview_frame.py` composite) → then produce part by part (§4).

Compact mini example (same story as §3):

> This script = **3 parts / 3 clips**, ~22 s (mini demo; a real Short is ~50 s – ~1.5 min). Flow estimate: **3 × ~10 ≈ 30 credits** (Veo 3.1 Lite).

| Part | Narration (English) | Words | Est. s | Seconds | Start-frame idea | End-frame idea | Prompt (short) |
|---|---|---|---|---|---|---|---|
| 1 | In 1932 Western Australia, soldiers rolled out with a Lewis machine gun to fight thousands of emus. | 18 | ~8 | 8 | Soldier left, gun low at side; fence + wheat | Same shot; soldier steps forward, gun raised aimed right | Step forward and raise gun to aim right |
| 2 | But the tall birds simply jogged through the wheat, ignoring the gunfire. | 13 | ~6 | 6 | Matches part 1 end; two emus enter from right | Emus jog left to mid-right; soldier still aiming | Emus jog left across wheat |
| 3 | Every burst scattered the flock. The soldiers fired thousands of rounds and barely hit any. | 15 | ~8 | 8 | Matches part 2 end; three emus mid-right | Emus scatter right/up; soldier recoils one step | Emus scatter; tiny gun recoil |

---

## 1. How to describe each scene (the template)

Fill this block **for every part** before generating that part's sketches. Save it in the part notes (or at the top of `prompts/partN.txt` as comments, with the three prompts below).

```
### Part N — <short beat title>
- Slot seconds: 4 | 6 | 8   (≤8; pick the smallest that covers measured narration)
- Narration (English, ≤~18–20 words):
  "…"
- Story beat (real event / place / year):
  …
- Setting / background:
  few objects only; pure white background; thin wobbly black hand-drawn lines; lots of white space
- Character:
  solid-black figure as <real person>, with <prop/costume>, LARGE, filling most of the frame width, clearly doing the action (not a small centred vignette)
- START frame (exact pose & positions):
  …
- END frame (same scene / camera / framing; ONLY the action's result changed):
  …
- Motion between them (one continuous one-way action + direction):
  … ; locked static camera; no zoom; no pan; no loop; no reverse
- Accent colour (one small red / orange / blue accent, like the refs):
  …
- Reference images (2–3 from reference-images/):
  - reference-images/<file>.jpg
  - …
- Continuity with part N−1:
  this part's START matches part N−1's END (same pose / prop / framing at the cut), OR hard cut to a new shot if the beat changes place
```

Then write the **three prompts** (English only; `Xiaohei` OK here; always include `no text, no letters, no captions` and **9:16**):

1. **Start-frame image prompt** — full scene description for `GenerateImage` (with the 2–3 refs).
2. **End-frame edit prompt** — edit/i2v-edit instruction applied **FROM** the start frame (same shot; only action progress).
3. **Video transition prompt** — written **after** the sketches exist (§1b): motion + **timed beats** for `prompts/partN.txt` (Flow start+end; Grok chain; Krea start+prompt), matching what the images actually show.

### Prompt skeletons

**Start-frame image prompt**
```
Ian Xiaohei illustration style, pure white background, thin wobbly black hand-drawn lines, lots of white space. Large solid-black Xiaohei as <real person> with <prop>, filling most of the frame width, <exact start pose and positions>. Few objects: <list>. Tiny <red/blue> accent on <object>. Vertical 9:16. no text, no letters, no captions.
```

**End-frame edit prompt** (image-to-image FROM start)
```
Same Ian Xiaohei scene, same white background, same camera, same framing, same scale, same objects. Only change: <exact end pose / result of the one action>. Keep large Xiaohei. Vertical 9:16. no text, no letters, no captions.
```

**Video transition prompt** (`prompts/partN.txt`) — write this **after** the start/end sketches exist (see §1b). Include timed beats.
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (<D> s total):
- 0–… s: exact start-image state (list character pose/position, props, objects, background, accent colour as they appear in partN_start.jpg)
- …–… s: <what moves, where, which direction>
- …
- …–<D> s: settles exactly on the end-image state (as in partN_end.jpg)

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects in the same positions as the sketches. no text, no letters, no captions.
```

---

## 1b. Transition prompt from the actual sketches (mandatory)

> **Hard rule:** do **not** paste a prompt written only from the script idea. After `scenes/partN_start.jpg` and `scenes/partN_end.jpg` exist, **look at both images**, then write (or rewrite) `prompts/partN.txt` so it describes **exactly** the motion from the start image to the end image, naming the same elements in the same positions as they appear. If either sketch is regenerated, **rewrite the prompt**. Check the prompt against both images **before** generating. After generation, QA checks that the clip followed the prompt (including timed beats) and landed on the end image.
>
> **Why (no lag / no glitches):** planning each second with timed beats and matching the prompt to both images leaves the generator nothing to guess. That prevents jumps, backward or reversed motion, stutter or freezes, objects vanishing or morphing, and a mismatched ending — so the clip stays continuous and lands on the end sketch.

### Steps (every part)

1. Open `partN_start.jpg` and `partN_end.jpg` side by side.
2. **List what is actually in them** (do not invent):
   - Character position and pose (left/right/centre, facing which way, limbs)
   - Props / costume
   - Other objects
   - Background / setting marks
   - Accent colour (what and where)
3. Confirm end is the **same shot** as start (same camera, framing, scale, background); only the action's result changed.
4. Write the transition prompt:
   - Name the **same** elements in the **same** positions as in the images.
   - Describe **one continuous one-way** action from start pose → end pose.
   - Include a **timed beat breakdown** for the clip duration (4 / 6 / 8 s).
   - Locked camera; no zoom; no pan; no loop; no reverse; same style; `no text, no letters, no captions`.
5. **Do not** mention things that are not in the images, or that contradict them (wrong side, wrong prop, extra characters, different background).
6. Run the **prompt-check checklist** below. Only then generate.
7. If a sketch is regenerated → rewrite the prompt and re-check before generating again.

### Timed beat splits

| Clip length | Beat windows (first = exact start state; last = settles on exact end state) |
|---|---|
| **8 s** | 0–1 s · 1–3 s · 3–5 s · 5–7 s · 7–8 s |
| **6 s** | 0–1 s · 1–2.5 s · 2.5–4 s · 4–5.5 s · 5.5–6 s |
| **4 s** | 0–0.5 s · 0.5–1.5 s · 1.5–2.5 s · 2.5–3.5 s · 3.5–4 s |

Each beat says **what moves, where, and in which direction**. Every beat continues the **same** one-way action (no new subplot mid-clip).

### Timed template (`prompts/partN.txt`)

```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (<D> s total):
- 0–… s: exact start-image state — <character pose/position, props, objects, background, accent as in partN_start.jpg>
- …–… s: <what moves, where, which direction>
- …–… s: <continue same action>
- …–… s: <continue same action>
- …–<D> s: settles exactly on the end-image state — <as in partN_end.jpg>

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects in the same positions as the sketches. no text, no letters, no captions.
```

### Worked timed example — Emu War part 1 (8 s)

Assume the generated sketches show: soldier left-of-centre facing right, Lewis gun low at his side, fence left, wheat right, tiny red on gun cooling rings (start); same shot with soldier one step forward and gun at waist aimed right (end).

```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (8 s total):
- 0–1 s: exact start-image state — large black soldier left-of-centre facing right, Lewis gun held low at his side, low fence left, wheat stalks right, tiny red on gun cooling rings, pure white background
- 1–3 s: soldier begins one step forward toward the right; gun starts rising from his side
- 3–5 s: step completes; gun rises to about hip height, still aimed right
- 5–7 s: gun reaches waist height aimed right; body settles after the step
- 7–8 s: settles exactly on the end-image state — soldier one pace forward, Lewis gun at waist aimed right, same fence, wheat, red accent, same framing

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and objects in the same positions as the sketches. no text, no letters, no captions.
```

### Prompt-check checklist (before generate)

```
[ ] Looked at partN_start.jpg and partN_end.jpg (not only the script idea)
[ ] Listed character pose/position, props, objects, background, accent colour from the images
[ ] Prompt names the same elements in the same positions (no wrong side / wrong prop / extra characters)
[ ] Prompt does not mention anything absent from the images
[ ] Prompt does not contradict either image
[ ] One continuous one-way action; locked camera; no zoom; no pan; no loop; no reverse
[ ] Same Ian Xiaohei style; no text / no letters / no captions
[ ] Timed beats present for the clip length (4/6/8) and consistent with both images
[ ] First beat = exact start-image state; last beat = settles on exact end-image state
[ ] If a sketch was regenerated since the last prompt → prompt was rewritten
```

### Good vs bad transition prompts (image match)

| | Bad (contradicts / invents) | Good (matches the images) |
|---|---|---|
| Side / prop | Start sketch has soldier on the **left** with a **Lewis gun**; prompt says "cavalry on the right draw sabres" | "soldier left-of-centre raises the Lewis gun aimed right" |
| Extra cast | Only soldier + fence + wheat in both sketches; prompt adds "a crowd of farmers cheering" | Names only soldier, fence, wheat, gun (as drawn) |
| End state | End sketch shows gun at **waist**; prompt says "fires a long burst into the sky" (not in the end image) | Motion ends when pose matches the end sketch |
| Timing | One vague sentence, no beats | Timed beats 0–1 / 1–3 / 3–5 / 5–7 / 7–8 with progressive one-way action |
| Written when | Prompt written from the script **before** sketches, never updated | Prompt written **after** sketches; rewritten if a sketch changes |

---

## 2. Good vs bad scene descriptions

| | Bad | Good |
|---|---|---|
| Action | Vague feelings: "he is sad", "they are worried" | One **concrete visible** action: "raises the Lewis gun", "emus scatter left across the plain" |
| Count | Many actions in one part: walk + aim + fire + celebrate | **One** action per part; split the rest into the next parts |
| Camera | "camera pans over the field", "zoom in on the gun" | Locked static camera; motion is **in the drawing only** |
| Text | "draw the year 1932 under the title", captions in the image | Illustration only: `no text, no letters, no captions` |
| Size | Small figure floating in the middle of white space | Large figure filling most of the **width**, clearly doing the action |
| Pair | End frame reinvented as a new composition | End is the **same shot** as start; only pose/result changed |
| Continuity | Part 2 starts in a random new pose | Part 2 start matches part 1 end (or a deliberate hard cut to a new place) |
| Words | 35-word narration crammed into 8 s | ≤~18–20 words; rewrite or **split** the part |
| Name | Narration says "Xiaohei walks…" | Narration names the **real person**; "Xiaohei" only in prompts |
| Aspect | 16:9 / landscape still | Vertical **9:16** only; reject if width ≥ height |

**One-sentence rule:** if you cannot mime the part's motion with one continuous gesture of your hand, the description has too many actions — split it.

---

## 3. Worked example — three parts of the Emu War (Western Australia, 1932)

Summary line for a full Emu War script would look like:
> This script = **9 parts / 9 clips**, ~68 s. Flow estimate: **9 × ~10 ≈ 90 credits** (Veo 3.1 Lite).

Below are **parts 1–3** fully described (template + all three prompts each). Use them as the pattern for the rest of any story.

### Part 1 — Soldiers arrive with the Lewis gun
- **Slot seconds:** 8
- **Narration:** "In 1932 Western Australia, soldiers rolled out with a Lewis machine gun to fight thousands of emus." (18 words)
- **Story beat:** Campion district, Nov 1932 — Australian soldiers arrive to cull crop-raiding emus.
- **Setting:** pure white; one low fence line left; a few wheat stalks right; thin wobbly black lines.
- **Character:** large black figure as a soldier in a simple peaked cap, holding a Lewis gun; fills most of the width.
- **START:** soldier stands left-of-centre facing right; Lewis gun held low at his side; fence left; wheat right.
- **END:** same shot; soldier has stepped one pace forward and raised the Lewis gun to waist height, aimed right.
- **Motion:** one step forward + raise the gun to aim right; locked camera.
- **Accent:** tiny red on the gun's cooling jacket rings.
- **Refs:** `reference-images/lustig-01-early.jpg`, `reference-images/wojtek-01-hook.jpg`, `reference-images/first-airplane-01-early.jpg`
- **Continuity:** part 1 opener (no previous end).

**Start-frame image prompt**
```
Ian Xiaohei illustration style, pure white background, thin wobbly black hand-drawn lines, lots of white space. Large solid-black Xiaohei as an Australian soldier in a simple peaked cap, filling most of the frame width, standing left-of-centre facing right, holding a Lewis machine gun low at his side. Few objects: a low fence line on the left, a few wheat stalks on the right. Tiny red accent on the gun cooling rings. Vertical 9:16. no text, no letters, no captions.
```

**End-frame edit prompt**
```
Same Ian Xiaohei scene, same white background, same camera, same framing, same scale, same fence and wheat. Only change: the soldier has taken one step forward and raised the Lewis gun to waist height aimed to the right. Keep large Xiaohei. Vertical 9:16. no text, no letters, no captions.
```

**Video transition prompt** (`prompts/part1.txt`) — written **after** the sketches; timed beats for 8 s
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (8 s total):
- 0–1 s: exact start-image state — large black soldier left-of-centre facing right, Lewis gun held low at his side, low fence left, wheat stalks right, tiny red on gun cooling rings
- 1–3 s: soldier begins one step forward toward the right; gun starts rising from his side
- 3–5 s: step completes; gun rises to about hip height, still aimed right
- 5–7 s: gun reaches waist height aimed right; body settles after the step
- 7–8 s: settles exactly on the end-image state — soldier one pace forward, Lewis gun at waist aimed right, same fence, wheat, red accent

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same fence, wheat, gun and character. no text, no letters, no captions.
```

---

### Part 2 — Emus appear on the plain
- **Slot seconds:** 6
- **Narration:** "But the tall birds simply jogged through the wheat, ignoring the gunfire." (13 words)
- **Story beat:** Emus keep moving through the crop; hard to hit.
- **Setting:** pure white; a short wheat row across the lower third; thin wobbly lines.
- **Character:** large black figure still as the soldier (cap + Lewis) on the left; two large emu silhouettes on the right (long necks, small heads).
- **START:** matches part 1 END — soldier left with gun at waist aiming right; two emus enter from the far right edge, mid-stride leftward.
- **END:** same shot; both emus have jogged left across the wheat to mid-right; soldier still aiming (no new pose).
- **Motion:** emus jog left across the frame only; soldier stays aimed; locked camera.
- **Accent:** tiny blue on one emu's eye dot.
- **Refs:** `reference-images/wojtek-02-middle.jpg`, `reference-images/flexible-glass-02-middle.jpg`, `reference-images/lustig-02-middle.jpg`
- **Continuity:** START = part 1 END (soldier pose/gun match).

**Start-frame image prompt**
```
Ian Xiaohei illustration style, pure white background, thin wobbly black hand-drawn lines, lots of white space. Large solid-black Xiaohei as an Australian soldier with peaked cap on the left, Lewis gun raised at waist aimed right. Two large black emu silhouettes enter from the far right edge mid-stride leftward, long necks, small heads. Few objects: a short wheat row across the lower third. Tiny blue accent on one emu eye. Vertical 9:16. no text, no letters, no captions.
```

**End-frame edit prompt**
```
Same Ian Xiaohei scene, same white background, same camera, same framing, same scale, same soldier pose and wheat. Only change: both emus have jogged left to the mid-right of the frame, still mid-stride. Keep large Xiaohei and emus. Vertical 9:16. no text, no letters, no captions.
```

**Video transition prompt** (`prompts/part2.txt`) — written **after** the sketches; timed beats for 6 s
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (6 s total):
- 0–1 s: exact start-image state — soldier left with Lewis at waist aimed right; two emus enter from far right edge mid-stride leftward; wheat row lower third; tiny blue on one emu eye
- 1–2.5 s: both emus continue jogging left across the wheat
- 2.5–4 s: emus reach the right-centre of the frame; soldier stays aimed (no new pose)
- 4–5.5 s: emus settle into mid-right mid-stride
- 5.5–6 s: settles exactly on the end-image state — emus mid-right mid-stride; soldier still aimed; same wheat and blue accent

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and wheat. no text, no letters, no captions.
```

---

### Part 3 — Emus scatter; gun misses
- **Slot seconds:** 8
- **Narration:** "Every burst scattered the flock. The soldiers fired thousands of rounds and barely hit any." (15 words)
- **Story beat:** Gunfire scatters the flock; cull fails.
- **Setting:** pure white; wheat row lower third; a few tiny dashed "tracer" lines (drawn ink, not text).
- **Character:** large soldier left with Lewis; three emu silhouettes bursting apart to the right and up.
- **START:** matches part 2 END — soldier aimed; two emus mid-right; a third emu just behind them.
- **END:** same shot; the three emus have scattered — one further right, one higher, one exiting top-right; soldier recoils one small step as the gun kicks.
- **Motion:** emus scatter outward/right/up in one burst; tiny gun recoil; locked camera.
- **Accent:** tiny red flash at the Lewis muzzle.
- **Refs:** `reference-images/yamaguchi-02-middle.jpg`, `reference-images/molasses-02-middle.jpg`, `reference-images/stanley-meyer-02-middle.jpg`
- **Continuity:** START = part 2 END (soldier + emu positions match).

**Start-frame image prompt**
```
Ian Xiaohei illustration style, pure white background, thin wobbly black hand-drawn lines, lots of white space. Large solid-black Xiaohei as an Australian soldier on the left with Lewis gun aimed right. Three large black emu silhouettes clustered mid-right, long necks. Few objects: wheat row across the lower third. Tiny red accent at the gun muzzle. Vertical 9:16. no text, no letters, no captions.
```

**End-frame edit prompt**
```
Same Ian Xiaohei scene, same white background, same camera, same framing, same scale, same wheat. Only change: the three emus have scattered — one farther right, one higher, one exiting top-right — and the soldier has recoiled one small step from the gun kick. Keep large Xiaohei. Vertical 9:16. no text, no letters, no captions.
```

**Video transition prompt** (`prompts/part3.txt`) — written **after** the sketches; timed beats for 8 s
```
Slow continuous one-direction motion matching the actual start and end sketches.

Timed beats (8 s total):
- 0–1 s: exact start-image state — soldier left aimed right; three emus clustered mid-right; wheat lower third; tiny red at muzzle
- 1–3 s: emus begin to burst apart — one right, one up, one toward top-right; muzzle red holds
- 3–5 s: scatter continues; soldier starts a small recoil step from the gun kick
- 5–7 s: emus near their end positions; soldier finishes the small step back
- 7–8 s: settles exactly on the end-image state — one emu farther right, one higher, one exiting top-right; soldier one small step recoiled; same wheat and red muzzle accent

Every beat continues the same one-way action. Static locked camera, no zoom, no pan, no camera movement, no loop, no reverse. Keep the same Ian Xiaohei ink style, pure white background, thin wobbly black lines, same characters and wheat. no text, no letters, no captions.
```

*(Continue the same template for parts 4…N of whatever story you are producing.)*

---

## 4. Per-part production order

Do this **after** the user has approved the part-by-part script table ([`script-writing.md`](script-writing.md)). Show **part 1** (start + end + prompt + composited preview) for approval before spending video credits. Then for each part **in order**:

1. **Record & measure narration** for that part: Chatterbox cloned from **am_eric**, **seed 7**, **exaggeration 0.6**, **cfg_weight 0.45**, one take per paragraph (`audio/pN.txt` → `pN.wav`). **No stretch / atempo / speed-up.** If measured > slot (or >8 s), rewrite or split. Details: [`narration.md`](narration.md).
2. **Describe the scene** with the template above (including continuity with part N−1).
3. **Make the sketch pair according to reference images:**
   - Pick 2–3 refs from [`../reference-images/`](../reference-images/).
   - Generate `scenes/partN_start.jpg` (9:16, illustration only, large character).
   - Generate `scenes/partN_end.jpg` **FROM** the start (edit / image-to-image). Same shot; only action progress.
   - Check pair side by side vs refs; regenerate drift; verify height > width.
4. **Write / rewrite `prompts/partN.txt` from the actual sketches** (§1b): look at `partN_start.jpg` + `partN_end.jpg`, list what they show, write a motion prompt with **timed beats** that match those images (not only the script idea). Run the prompt-check checklist. If a sketch is regenerated later, rewrite the prompt before generating.
5. **Generate the clip** for that part only:
   - **Flow (browser-primary):** upload start + end, paste prompt, Veo 3.1 Lite **720p**, **9:16**, duration 4|6|8 s (≤8). **No 480p test. No Real-ESRGAN upscale.** MCP only on browser fault / no access.
   - **Grok Imagine (default):** two chained **4 s** clips at **480p** (clip A from start → last frame → clip B continuing); end sketch = check target only; join → **QA stage 1** → `scripts/video/upscale_720p.sh` (or `chain_and_upscale.sh`) to **720×1280** → **QA stage 2** sharpness. Do **not** regenerate at 720p unless upscale is soft. (Same 480p→upscale pattern for any other tool whose max output is below 720p.)
   - **Krea (MCP-primary):** start + prompt (start/end models when available); end sketch = check target for start-only models. Browser fallback only after user choice. If output is already ≥720p, skip upscale; if below 720p, use the Grok-style 480p→upscale path.
   - **HF Wan:** start (+ optional last image) + prompt in the Space browser UI; treat sub-720p output like Grok (QA then upscale).
6. **Self-verify the clip**, then **QA stage 1** — send the part clip **and** `prompts/partN.txt` to **QA סרטונים** (watches the video): 9:16; no baked-in text; one-way motion; locked camera; no loop/zoom; last frame matches end sketch; **clip followed the prompt** (elements/positions); **timing matches the timed beats**; seam/continuity (Grok A→B); no glitches/distortions/extra limbs. **Flow:** QA watches the **720p** clip immediately. **Grok:** QA watches the **480p** join before upscale.
7. **Upscale only if needed** (Grok / sub-720p): after stage-1 pass → Real-ESRGAN → **QA stage 2** sharpness. **Skip for Flow 720p.**
8. **RIFE** to true 24 fps continuous motion (`scripts/video/rife_eq.py`), then jolt fixes if needed. Never interpolate across a cut.
9. **Retime** the part to its narration slot (motion-equalized one-way).
10. Only then move to **part N+1** (do not advance on a failed QA without a fix + re-pass, unless the user explicitly allows drafting ahead).

Credit shortage (Flow / Krea) → stop and tell the user. Never buy plans or credits unless the user explicitly asks.

---

## 5. Assembly (after all parts)

1. **Order clips** by part number: `anim/scene1_r.mp4` … `anim/sceneN_r.mp4` (or `anim/partN_r.mp4`).
2. **Join narration:** `audio/p1.wav` … `pN.wav` with natural pauses ([`../scripts/voice/join_paragraphs.py`](../scripts/voice/join_paragraphs.py)) → breath gate + **loudnorm I=-16** ([`process_narration.py`](../scripts/voice/process_narration.py)) → ASR ([`asr_words.py`](../scripts/voice/asr_words.py)) → [`sentence_timing.py`](../scripts/video/sentence_timing.py). Never stretch audio.
3. **`scripts/video/build.py`** composites every part into final **1080×1920**:
   - Art cropped to drawing bbox and scaled into the 1060×1150 box.
   - English UPPERCASE title + red underline (x=400–680, 6 px).
   - English sentence-locked subtitles synced per sentence (Patrick Hand 62 / 56 / 52; 0 boundary crossings).
   - Page counter `— i / N —` where **N = number of parts**.
4. Mux `audio/narration_norm.wav`; export `/workspace/<story>-history-vK.mp4`.

Details: [`subtitles-and-build.md`](subtitles-and-build.md), [`narration.md`](narration.md).

## 5b. Final QA → SEO → Buffer → lessons

1. Self-QA scripts, then **QA stage 3:** send the final file to the **QA סרטונים** bot (it **watches** the full video) and wait for pass ([`qa.md`](qa.md), [`../bots/qa-videos.md`](../bots/qa-videos.md)). Checks: audio (first words, pauses, no stretch, loudness), subtitle sync/size, title+underline layout, English only, animation never frozen, fit to script. Fail → fix → QA again. **Nothing delivered or scheduled without this pass.**
2. **YouTube SEO** bot sets title / description / tags / schedule (no "Xiaohei" in metadata) ([`../bots/youtube-seo.md`](../bots/youtube-seo.md)).
3. Only after the **user's own words** approve: host on `stav888/video-hosting` (commit-pinned raw URL) → Buffer `create_post` on Smart History Knowledge (category 27, public, madeForKids false, isAiGenerated true).
4. After publish: cleanup hosted file; SEO adds tags.
5. **Continuous improvement:** append a short entry to [`lessons-learned.md`](lessons-learned.md) (QA faults, user feedback, fixes; SEO performance when known). Read that log before the next video.

Details: [`publishing-buffer.md`](publishing-buffer.md).

---

## 6. Folder layout & file names (per story on the box)

```
/workspace/<story>/
  audio/
    p1.txt … pN.txt          # one narration paragraph per part
    p1.wav … pN.wav
    joined.wav  narration_norm.wav
    sentences.txt  asr_words.json
  scenes/
    part1_start.jpg  part1_end.jpg
    part2_start.jpg  part2_end.jpg
    …
    partN_start.jpg  partN_end.jpg
  prompts/
    part1.txt … partN.txt    # video transition prompts
  gen/
    partN_a.mp4  partN_b.mp4 # Grok chain only
    partN.mp4                # joined / Flow / Krea / HF take
    partN_720p.mp4           # optional after upscale
    partN_a_last.jpg         # Grok chain bridge frame
  anim/
    sceneN_r.mp4             # RIFE-retimed part (legacy name)
    partN_r.mp4              # preferred RIFE-retimed name for new builds
  refs/                      # optional clone of ian-xiaohei-illustrations
  audio_timing.json  timing.json  ons.json
  subpng/  static/  clips/
```

Final delivery: `/workspace/<story>-history-vN.mp4` (keep prior versions).

---

## 7. Per-part checklist

Copy for each part:

```
[ ] Part N described with the full template (incl. continuity)
[ ] Narration English, ≤~18–20 words; measured ≤ slot (≤8 s)
[ ] 2–3 reference-images/ chosen and noted
[ ] scenes/partN_start.jpg — 9:16, illustration only, large character
[ ] scenes/partN_end.jpg — FROM start; same shot; only action progress
[ ] Pair checked vs refs (style, size, no text, height > width)
[ ] prompts/partN.txt written **after** sketches from what the images show (not only the idea)
[ ] Prompt-check checklist passed (same elements/positions; timed beats; first=start / last=end)
[ ] Clip generated (Flow ≤8 s @720p direct / Grok 2×4 s @480p / Krea / HF)
[ ] Self-verify (9:16, no text, one-way, matches end, continuity, beats)
[ ] **QA stage 1** — QA סרטונים watched the part clip vs prompt+beats and passed (Flow: 720p; Grok: 480p join)
[ ] Grok / sub-720p only: upscale_720p.sh → **QA stage 2** sharpness pass (skip for Flow 720p)
[ ] RIFE 24 fps + retime to slot
[ ] Ready for part N+1 (next start matches this end, if continuous)
```

After all parts: build overlays → loudnorm −16 → **QA stage 3** (full video watched) → SEO → user approval → Buffer → append [`lessons-learned.md`](lessons-learned.md).
