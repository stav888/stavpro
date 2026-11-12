# The Great Emu War — Midjourney-adapted prompts

This file is a Midjourney Web conversion of the nine **real** animation prompts in [`emu-war.md`](emu-war.md). **`emu-war.md` is unchanged.** Midjourney has no API; the prompts below are short, concrete English meant for manual paste.

Conventions followed (from `MID/` in this repo and `.github/instructions/mid.instructions.md`):

- **Locked-off camera.** Do not use `push-in`, `zoom`, `dolly`, or `move closer`. No pan.
- **One-way motion only.** Do not use `--loop`, and do not write looping motion (`keeps turning`, `continues to tick`, reverse, ping-pong).
- Valid Midjourney video parameters used here: `--motion low` (MID default), `--raw`. `--loop` is valid in Midjourney but **must not be used** for this channel. `--end` is the End Frame control (upload the end still; see each part).
- A first clip is **5 s**. Each manual Extend adds **~4 s**. Maximum length is **21 s**. No part needs more than one extension.
- When a start still is set, Midjourney matches its aspect (these stills are 9:16; the UI often shows `--ar 171:256`). Per MID QA, **do not type `--ar`** when a Start Frame is uploaded.
- Describe **only what moves**. The start still is already frame zero.
- Style anchors stay as in the original animation prompts (Ian Xiaohei ink, white background, thin wobbly black lines, no text). Do not add photoreal / push-in language from the MID cat example — that would fight this style and the no-zoom rule.

**Original image / sketch prompts:** **not found** for every part (same as [`emu-war.md`](emu-war.md)). No new Midjourney image prompts were written. Use the existing production stills as Start and End frames.

## Frames

The nine start and end stills were copied from the box into [`emu-war-images/`](emu-war-images/) (all 18 found; all already 720×1280 and under 500 KB, copied as-is). Use the **repo** files below as Start Frame and End Frame (`--end`) in Midjourney. The original box path is noted as the source.

Part 2 v3, part 3 v2 and part 4 v2 were **clip** regenerations; no separate versioned stills were found, so these are the start/end images used for those takes.

| Part | Start Frame (in repo) | End Frame (`--end`, in repo) | Original box source |
|---|---|---|---|
| 1 | [`emu-war-images/part1_start.jpg`](emu-war-images/part1_start.jpg) | [`emu-war-images/part1_end.jpg`](emu-war-images/part1_end.jpg) | `/workspace/emu-war/scenes/part1_start.jpg` / `part1_end.jpg` |
| 2 | [`emu-war-images/part2_start.jpg`](emu-war-images/part2_start.jpg) | [`emu-war-images/part2_end.jpg`](emu-war-images/part2_end.jpg) | `/workspace/emu-war/scenes/part2_start.jpg` / `part2_end.jpg` |
| 3 | [`emu-war-images/part3_start.jpg`](emu-war-images/part3_start.jpg) | [`emu-war-images/part3_end.jpg`](emu-war-images/part3_end.jpg) | `/workspace/emu-war/scenes/part3_start.jpg` / `part3_end.jpg` |
| 4 | [`emu-war-images/part4_start.jpg`](emu-war-images/part4_start.jpg) | [`emu-war-images/part4_end.jpg`](emu-war-images/part4_end.jpg) | `/workspace/emu-war/scenes/part4_start.jpg` / `part4_end.jpg` |
| 5 | [`emu-war-images/part5_start.jpg`](emu-war-images/part5_start.jpg) | [`emu-war-images/part5_end.jpg`](emu-war-images/part5_end.jpg) | `/workspace/emu-war/scenes/part5_start.jpg` / `part5_end.jpg` |
| 6 | [`emu-war-images/part6_start.jpg`](emu-war-images/part6_start.jpg) | [`emu-war-images/part6_end.jpg`](emu-war-images/part6_end.jpg) | `/workspace/emu-war/scenes/part6_start.jpg` / `part6_end.jpg` |
| 7 | [`emu-war-images/part7_start.jpg`](emu-war-images/part7_start.jpg) | [`emu-war-images/part7_end.jpg`](emu-war-images/part7_end.jpg) | `/workspace/emu-war/scenes/part7_start.jpg` / `part7_end.jpg` |
| 8 | [`emu-war-images/part8_start.jpg`](emu-war-images/part8_start.jpg) | [`emu-war-images/part8_end.jpg`](emu-war-images/part8_end.jpg) | `/workspace/emu-war/scenes/part8_start.jpg` / `part8_end.jpg` |
| 9 | [`emu-war-images/part9_start.jpg`](emu-war-images/part9_start.jpg) | [`emu-war-images/part9_end.jpg`](emu-war-images/part9_end.jpg) | `/workspace/emu-war/scenes/part9_start.jpg` / `part9_end.jpg` |

## How to paste (Midjourney Web)

1. Imagine → add the **Start Frame** still → Switch to video.
2. Set **End Frame** (`--end`) to that part’s `partN_end.jpg` where the plan says to use it. Leave **Loop off**. Motion **Low**.
3. Paste the prompt, including `--motion low --raw`. Do not add `--loop`. Do not add `--ar`.
4. For a 9 s part: run the **opening** prompt first (5 s). After a clean take, **Extend manually** once (~+4 s → ~9 s), replace the prefilled text with the **extend** prompt, Loop off, Motion Low, and keep `--end` aimed at the same end still if the plan says so. Split prompts follow the MID rule: the first 5 s is not packed, and the extend continues the same one-way action.

## Narration length vs 5 s or 9 s

Measured from `/workspace/emu-war/audio/part_timing.json` (final v2). “Speech” is last word minus first word in that part. Every part is ≤ 8 s, so at most one Extend is needed.

| Part | Speech | Part slot | 5 s clip? | Plan |
|---|---:|---:|---|---|
| 1 | 5.36 s | 5.58 s | No — speech is longer than 5 s | One Extend (**9 s**) |
| 2 | 5.32 s | 5.72 s | No | One Extend (**9 s**) |
| 3 | 4.44 s | 4.82 s | Yes | **5 s** only |
| 4 | 4.50 s | 4.97 s | Yes | **5 s** only |
| 5 | 3.62 s | 3.89 s | Yes | **5 s** only |
| 6 | 5.42 s | 5.62 s | No | One Extend (**9 s**) |
| 7 | 3.70 s | 4.06 s | Yes | **5 s** only |
| 8 | 4.82 s | 5.21 s | Speech fits 5 s; the part slot is 0.21 s over | **5 s** is enough for the words; use one Extend (**9 s**) only if you want the full slot |
| 9 | 6.04 s | 6.44 s | No | One Extend (**9 s**) |

## Part 1

- **Narration:** In 1932 Western Australia, the army went to war against twenty thousand emus.
- **Length plan:** 9 s (5 s + one Extend). Speech 5.36 s.
- **Start Frame:** [`emu-war-images/part1_start.jpg`](emu-war-images/part1_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part1_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part1_end.jpg`](emu-war-images/part1_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part1_end.jpg`)

<p><img src="emu-war-images/part1_start.jpg" width="180" alt="part 1 start"> <img src="emu-war-images/part1_end.jpg" width="180" alt="part 1 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/clips/part1_v2_prompt_used.txt` (final v2 wording, also in [`emu-war.md`](emu-war.md)). Converted below; not used verbatim because Midjourney wants a short motion prompt and a 5 s + 4 s split.

Set Start and End frames. Loop off. Opening job has no end-state settle packed into the first 5 s; the third emu should already be in by the end of the opening, and the Extend only settles (soldier front foot slightly lifted). Midjourney “no new objects on Extend” is respected: both extra emus enter in the opening.

**Opening prompt (5 s) — paste:**

```
The soldier stays at the same place on the left with only a slight weight shift, one emu already on the right shifts in place, a second emu walks in from the right edge and stops on the right, then a third emu walks in from the right edge and stops in a row, white gaps between the three emus, none of them cross or pass through the soldier, fence on the far left stays fixed and visible, tiny red muzzle ring stays constant, no muzzle flash, one-way motion only, no freeze, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

**Extend prompt (~4 s) — paste:**

```
The three emus already on the right stand in a stable row with slight head bobs and feather ruffle, the soldier stays at the same left place with a small weight shift and a slight lift of his front foot, red muzzle ring stays constant, fence stays fixed and visible, no new emus, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 2

- **Narration:** After World War One, soldier-settlers farmed tough wheat land near Campion and Walgoolan.
- **Length plan:** 9 s (5 s + one Extend). Speech 5.32 s.
- **Start Frame:** [`emu-war-images/part2_start.jpg`](emu-war-images/part2_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part2_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part2_end.jpg`](emu-war-images/part2_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part2_end.jpg`)

<p><img src="emu-war-images/part2_start.jpg" width="180" alt="part 2 start"> <img src="emu-war-images/part2_end.jpg" width="180" alt="part 2 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part2.txt`.

**Opening prompt (5 s) — paste:**

```
The farmer stays at the same left place and slowly begins to kneel beside the wheat, wheat heads start to droop, tiny orange sun stays fixed in the upper right, no new characters, one-way motion only, no freeze, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

**Extend prompt (~4 s) — paste:**

```
The farmer finishes kneeling and crouches beside the drooping wheat at the same left place, wheat tips droop a little more, orange sun stays fixed, slight living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 3

- **Narration:** About twenty thousand migrating emus smashed fences and ruined the struggling harvest.
- **Length plan:** **5 s** only (speech 4.44 s; slot 4.82 s).
- **Start Frame:** [`emu-war-images/part3_start.jpg`](emu-war-images/part3_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part3_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part3_end.jpg`](emu-war-images/part3_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part3_end.jpg`)

<p><img src="emu-war-images/part3_start.jpg" width="180" alt="part 3 start"> <img src="emu-war-images/part3_end.jpg" width="180" alt="part 3 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part3_v2.txt`.

**Prompt (5 s) — paste:**

```
The farmer stays locked behind the fence on the left with only slight breath, emus enter only from the right edge and walk left toward a fence gap, never through or behind the farmer, the group grows from one emu to three distinct emus, a gap opens in the fence, wheat flattens, tiny blue eye accents stay visible, continuous living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 4

- **Narration:** On November second, Major Meredith rolled out with two Lewis guns and ten thousand rounds.
- **Length plan:** **5 s** only (speech 4.50 s; slot 4.97 s).
- **Start Frame:** [`emu-war-images/part4_start.jpg`](emu-war-images/part4_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part4_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part4_end.jpg`](emu-war-images/part4_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part4_end.jpg`)

<p><img src="emu-war-images/part4_start.jpg" width="180" alt="part 4 start"> <img src="emu-war-images/part4_end.jpg" width="180" alt="part 4 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part4_v2.txt`.

**Prompt (5 s) — paste:**

```
Meredith stays at the same left place, the Lewis gun rises slowly from low at his side to waist height aimed right, a tiny red ring on the muzzle stays clearly visible and constant, no muzzle flash, fence on the left and wheat on the right stay fixed, slight breath, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 5

- **Narration:** But the tall birds simply jogged through the wheat, ignoring the gunfire.
- **Length plan:** **5 s** only (speech 3.62 s; slot 3.89 s).
- **Start Frame:** [`emu-war-images/part5_start.jpg`](emu-war-images/part5_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part5_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part5_end.jpg`](emu-war-images/part5_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part5_end.jpg`)

<p><img src="emu-war-images/part5_start.jpg" width="180" alt="part 5 start"> <img src="emu-war-images/part5_end.jpg" width="180" alt="part 5 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part5.txt`.

**Prompt (5 s) — paste:**

```
The soldier stays at the same left place aiming right, the two emus jog left from the right edge and stop mid-right, never crossing the soldier, red muzzle ring stays constant, blue eye accents stay, slight living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 6

- **Narration:** At a Campion dam, over a thousand emus closed in — then the Lewis gun jammed.
- **Length plan:** 9 s (5 s + one Extend). Speech 5.42 s.
- **Start Frame:** [`emu-war-images/part6_start.jpg`](emu-war-images/part6_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part6_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part6_end.jpg`](emu-war-images/part6_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part6_end.jpg`)

<p><img src="emu-war-images/part6_start.jpg" width="180" alt="part 6 start"> <img src="emu-war-images/part6_end.jpg" width="180" alt="part 6 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part6.txt`.

**Opening prompt (5 s) — paste:**

```
The soldier stays at the same left place, the clustered emus on the right begin to scatter right and up, staying on the right half and never crossing the soldier, the gun tip starts to tilt into a jammed pose, red muzzle ring stays constant, living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

**Extend prompt (~4 s) — paste:**

```
The emus finish scattering to the right and stay on the right half, the gun settles in the jammed tilt, the soldier stays at the same left place, red muzzle ring stays constant, slight living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 7

- **Narration:** They mounted a gun on a truck, but the ride was too rough to fire a shot.
- **Length plan:** **5 s** only (speech 3.70 s; slot 4.06 s).
- **Start Frame:** [`emu-war-images/part7_start.jpg`](emu-war-images/part7_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part7_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part7_end.jpg`](emu-war-images/part7_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part7_end.jpg`)

<p><img src="emu-war-images/part7_start.jpg" width="180" alt="part 7 start"> <img src="emu-war-images/part7_end.jpg" width="180" alt="part 7 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part7.txt`.

**Prompt (5 s) — paste:**

```
The truck tilts and bounces one way as if on a rough ride, the soldier on the bed wobbles but stays on the truck, emus move farther right as they escape, red muzzle ring stays constant, no reverse bounce, no loop, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 8

- **Narration:** A second campaign began. Meredith claimed nine hundred eighty-six kills — ten rounds each.
- **Length plan:** **5 s** covers the spoken words (4.82 s). The part slot is 5.21 s, so one Extend (9 s) is optional if you want that extra tail.
- **Start Frame:** [`emu-war-images/part8_start.jpg`](emu-war-images/part8_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part8_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part8_end.jpg`](emu-war-images/part8_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part8_end.jpg`)

<p><img src="emu-war-images/part8_start.jpg" width="180" alt="part 8 start"> <img src="emu-war-images/part8_end.jpg" width="180" alt="part 8 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part8.txt`.

**Prompt (5 s) — paste:**

```
Meredith stays at the same left place, he raises a blank paper and points, the gun stays low, a red ring on the muzzle stays constant if visible, the small background emus shrink or grow fewer, slight living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

## Part 9

- **Narration:** Meredith said the birds faced machine guns like tanks. Parliament laughed; later, bounties worked better.
- **Length plan:** 9 s (5 s + one Extend). Speech 6.04 s.
- **Start Frame:** [`emu-war-images/part9_start.jpg`](emu-war-images/part9_start.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part9_start.jpg`)
- **End Frame (`--end`):** [`emu-war-images/part9_end.jpg`](emu-war-images/part9_end.jpg) (in this repo; source on the box: `/workspace/emu-war/scenes/part9_end.jpg`)

<p><img src="emu-war-images/part9_start.jpg" width="180" alt="part 9 start"> <img src="emu-war-images/part9_end.jpg" width="180" alt="part 9 end"></p>
- **Original image prompt:** **not found.**
- **Original animation prompt (source only):** `/workspace/emu-war/prompts/part9.txt`.
- **Grok animation prompt (v2 used in final):** used in `emu_war_final_v3.mp4`. Source: `/workspace/emu-war/prompts/part9_v2.txt`.

```
ONE continuous 8s clip matching the actual start and end sketches. Ian Xiaohei ink style. Pure white background. Locked static camera, no zoom, no pan, no loop, no reverse, no ping-pong.

CRITICAL — LIVING MOTION THROUGH THE END: every figure keeps light living motion in EVERY second, including 0–1 s and 6.5–8 s. Emu head bobs, slight feather ruffle, weight shift foot to foot. Meredith subtle breath / tiny weight shift. Never freeze or near-freeze. No hold over 0.4 s.

CRITICAL — Meredith LOCKED at the same left x the whole time. ONLY motion: he starts with his right arm pointing at the emu, then slowly lowers that pointing arm down to his side (one-way, never points again). Tiny RED ring on the Lewis-gun muzzle/cooling tip stays clearly visible and CONSTANT in EVERY frame — never blink off, no muzzle flash.

CRITICAL — the tall emu stays on the RIGHT, standing firm, facing left. It does not walk away or cross Meredith. Keep continuous head-bobs / weight shifts so it is never static. Parliament building outline stays fixed in the mid background between them.

Start (from the actual start sketch): large solid-black officer on the left with peaked cap, white dot eyes, thin stick legs; right arm pointing at the tall emu; Lewis gun held low in the other hand with a tiny red muzzle ring; tall black emu standing on the right facing left; thin-line parliament building with dome in the mid gap; sparse ground scribbles; pure white background.

End (from the actual end sketch): SAME Meredith at the SAME left x, pointing arm now lowered at his side, gun still in the other hand with the SAME constant red muzzle ring; SAME emu standing firm on the right with living micro-motion; SAME fixed parliament outline; a SMALL solid-black farmer with a wide hat and pitchfork appears at the BOTTOM RIGHT, and a BLANK circular bounty token (two concentric circles, no letters) appears beside him. Farmer and token arrive with light living motion, not a pop-in freeze.

Timed beats (8 s):
- 0–1 s: exact start living immediately — Meredith still pointing, slight breath; emu slight head bob; red ring ON; parliament fixed; NO hold
- 1–3 s: Meredith begins slowly lowering the pointing arm; emu weight-shifts and head-bobs; red ON; no morph jolts
- 3–5 s: arm continues down toward his side; gun stays in the other hand, slightly lowered; emu still living; red ON
- 5–7 s: small farmer with pitchfork and blank bounty circle appear at the bottom right; Meredith's arm is down; emu stands firm with ongoing head bobs; red ON; all figures keep living motion
- 7–8 s: living settle on the end state — keep micro-motion to the last frame (emu head bob, farmer tiny weight shift, Meredith breath). NO freeze. Red ring still ON. Parliament still fixed.

no text, no letters, no captions.
```

The original 8 s beats put the small farmer and blank bounty token in the second half (5–7 s). MID Extend rules say no **new** objects on Extend. Those two elements are already in `part9_end.jpg`. The split below keeps pointing and the gun-lowering in the opening, and lets the end-frame token and farmer arrive on the Extend, which is how the original beats were timed. Alternatively, set `--end` on the opening 5 s job so those elements appear earlier, and use the Extend only for living settle with no new objects.

**Opening prompt (5 s) — paste:**

```
Meredith stays at the same left place, still pointing at the tall emu, then slowly begins to lower the gun, the emu stands firm, the parliament outline stays fixed, red muzzle ring stays constant, living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```

**Extend prompt (~4 s) — paste:**

```
Meredith finishes lowering the gun at the same left place, the emu stands firm, a small farmer and a blank bounty token appear at the bottom right as in the end frame, parliament outline stays fixed, red muzzle ring stays constant, living motion, no freeze, one-way motion only, locked-off camera, Ian Xiaohei ink style, pure white background, thin wobbly black lines, no text, no letters, no captions --motion low --raw
```
