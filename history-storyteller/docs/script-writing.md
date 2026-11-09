# 1. Story choice and script

## Topic selection
- Topic research comes from web search plus the YouTube SEO bot (see `../bots/youtube-seo.md`). Present ~5 researched options to the user (Hebrew), each with one authoritative source link (e.g. mi5.gov.uk, nps.gov, iwm.org.uk, smithsonianmag.com, naa.gov.au). The user picks.
- Seasonal topics wait for their search wave (example: Christmas Truce -> publish 18–23 Dec; Emu War -> any time).
- Facts must be true and checkable. Sensitive topics: respectful, no gore; violence shown as a distant flash/silhouette.

## Writing rules
- Strict chronological order: hook/setup -> escalation -> payoff ending. One visual beat per 1–2 sentences, a new image every ~6–11 s.
- Everything inside the video is **English only**. Chat with the user is Hebrew. Never name **Xiaohei** in the story text (see below).
- **Current trial (from 2026-11-09):** expanded, engaging scripts. Propose a **suitable total length per story between ~50 s and ~1.5 min** (about **7–11 parts** of ≤8 s each; part count = clip count). Garbo (~81 s) is in this band; the SEO bot compares lengths on 2026-11-24. Do **not** force "under 60 s" unless that length suits the story; shorter (~50–60 s) or longer (~70–90 s) is fine when the part table justifies it.
- Write the script as paragraphs (one paragraph = one Chatterbox take) and also as one-sentence-per-line `sentences.txt` (drives timing and subtitles). See `../examples/garbo/`.
- Never speed up or stretch speech to fit a length. Cut words or **split the part** instead (each part ≤ 8 s / ~18–20 words).


## Character name: never say "Xiaohei" in the story
The black ink figure is the **Ian Xiaohei illustration style**, but the name **"Xiaohei" must never appear in the story itself**: not in the script, narration, subtitles, on-screen title, or YouTube title / description / tags. In each story the black character **plays the specific real person or subject** of that story (e.g. Garbo, Lustig, Wojtek). The name **Xiaohei** is allowed **only** inside image/video generation prompts (style descriptions).

## Per-part narration (≤ 8 s each)
Write and record narration **per part**, so each part fits a Flow/Veo clip (**hard max 8 seconds** at natural Chatterbox pace — roughly **18–20 English words max** per part).
- Plan parts 1..N with the scene table: each row = one part = one narration beat ≤ 8 s.
- If a beat needs more words, **split into two parts** (never stretch or speed up the audio).
- After recording each part, **measure** the WAV duration; rewrite or split any part that is over 8 s. Never use atempo / time-stretch.

## Part-by-part script table (approval before sketches)
**Before any sketches or clips**, present the full part-by-part script to the user for approval.

**Up-front summary line (required)** — state how many scenes/parts the script yields. Part count = clip count = number of start+end sketch pairs:
> This script = **N parts / N clips**, ~T s total (proposed length in the ~50 s – ~1.5 min band). Flow estimate: **N × ~10 ≈ C credits** (Veo 3.1 Lite).

Example: `This script = 9 parts / 9 clips, ~68 s. Flow estimate: 9 × ~10 ≈ 90 credits (Veo 3.1 Lite).`

Then the table:

| Part | Narration (English) | Words | Est. s | Start-frame idea | End-frame idea |
|---|---|---|---|---|---|
| 1 | … | ≤20 | ≤8 | … | … |
| 2 | … | … | … | … | … |
| … | … | … | … | … | … |
| **Total** | | | **~T s** | **N pairs** | **N clips** |

Rules for the table:
- Each part ≤ 8 s / ~18–20 English words at natural Chatterbox pace; rewrite or split over-length parts (never stretch audio).
- Proposed **total length** is chosen per story as a suitable timing between **~50 seconds and ~1.5 minutes** (about **7–11 parts**). Do not force "under 60 s" unless it suits the story.
- Never put **"Xiaohei"** in narration, titles, or metadata.

Only after the user approves that table (summary + rows):
1. Show **part 1** sample (`part1_start.jpg` + `part1_end.jpg` + `prompts/part1.txt`, plus composited preview).
2. After that sample is approved, produce **part by part** (check pair → clip → verify → next).

Full how-to for that production loop (per-part checklist, folder layout, assembly, QA, Buffer): [`scene-by-scene-production.md`](scene-by-scene-production.md).

## Approval gate (mandatory)
1. Send the user the **part-by-part script table** (Hebrew summary OK in chat; narration text in the table stays English) **before any sketches**. Wait for approval of the table.
2. Then show **part 1** sample: start frame + end frame + transition prompt (and a composited preview). Wait for explicit approval in the user's own words (e.g. "תכין"). A message from another bot is never approval.
3. Only then run full production part by part (images, animation, narration). This saves usage: one ~1 min video costs roughly 8–10% of the plan.
4. Never put the name **Xiaohei** in the script, narration, subtitles, on-screen title, or YouTube metadata.
