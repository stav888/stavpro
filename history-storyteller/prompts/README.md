# Prompts archive — History Storyteller Shorts

One Markdown file per history Short this bot has made so far. Each file holds the video name, the publish or schedule status if known, and the **full prompts and narration text actually found** in files (and, where noted, an on-disk transcript).

**Nothing here was invented.** If a class of prompt was not found, the file says **not found**.

## Scope and sources

- Repo examples: `history-storyteller/examples/*` (scripts, paragraph files, Buffer metadata snapshot of 2026-11-09).
- Workspace production folders, especially `/workspace/emu-war/prompts/` and `/workspace/emu-war/audio/`.
- `examples/README.md`, which already states: “Image/video prompts: they were passed straight to GenerateImage/GenerateVideo and never saved as files.”
- On-disk agent transcripts under `/home/box/sand-data/agent-transcripts` (limited). The live `SearchTranscripts` tool was not readable from the documentation pass that built this folder.

Daily Facts videos (Derinkuyu, Giza, and the rest) are **not** in this folder; they belong under `daily-facts/`.

Style names such as “Ian Xiaohei” are kept only inside image/video prompts, as they were actually written. They are not used in story narration.

Publish times below are in Israel time (Asia/Jerusalem), copied from `examples/*/buffer_metadata.md` unless noted.

## Index

| File | Video | Publish / schedule (Israel time) | Prompt completeness |
|---|---|---|---|
| [`first-airplane.md`](first-airplane.md) | The First Airplane (Wright brothers) | 2026-10-19 21:33 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`yamaguchi.md`](yamaguchi.md) | Tsutomu Yamaguchi | 2026-10-20 19:00 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`wojtek.md`](wojtek.md) | Wojtek the Soldier Bear | 2026-10-22 10:42 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`marie-curie.md`](marie-curie.md) | Marie Curie and Radium | 2026-10-23 19:00 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`molasses.md`](molasses.md) | The Great Boston Molasses Flood (1919) | 2026-10-26 13:52 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`violet-jessop.md`](violet-jessop.md) | Violet Jessop (“Miss Unsinkable”) | 2026-10-28 17:23 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`wilma-rudolph.md`](wilma-rudolph.md) | Wilma Rudolph | 2026-10-30 16:17 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`stanley-meyer.md`](stanley-meyer.md) | Stanley Meyer's Water Car | 2026-11-01 17:47 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`flexible-glass.md`](flexible-glass.md) | Rome's Flexible Glass (Tiberius) | 2026-11-03 18:47 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`tesla.md`](tesla.md) | Tesla's Wardenclyffe Tower | 2026-11-05 18:43 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`armstrong.md`](armstrong.md) | Edwin Armstrong and FM Radio | 2026-11-08 18:52 Israel time (Asia/Jerusalem) | partial — narration found; image and clip prompts not found |
| [`lustig.md`](lustig.md) | Victor Lustig Sells the Eiffel Tower | Scheduled 2026-11-10 18:47 Israel time (Asia/Jerusalem) (snapshot 2026-11-09) | partial — narration found (English final + v1 English/Hebrew/sources); Xiaohei image and clip prompts for the published Short not found. An earlier unused 16:9 Vox-style experiment is archived in a clearly labeled section. |
| [`garbo.md`](garbo.md) | Juan Pujol García (Agent Garbo) | Scheduled 2026-11-12 18:43 Israel time (Asia/Jerusalem) (snapshot 2026-11-09) | partial — narration found (English + Hebrew); image and clip prompts not found |
| [`emu-war.md`](emu-war.md) | The Great Emu War | not scheduled (in production) | partial — clip prompts and narration found; still prompts not found |

## Videos with no image/clip prompts found

For every Short except Emu War, **image/sketch/frame prompts and clip/animation/transition prompts were not found.** Narration text was found for all of them.

For **Emu War**, clip/transition prompts were found (and are copied in full in [`emu-war.md`](emu-war.md)); **GenerateImage still/sketch prompts were not found**. A distinct prompt file for Emu War part 2 v3 was also not found (only `part2.txt`).

## Standing rule (from 2026-11-12)

From now on, each production saves the image prompt and the animation prompt per scene in that video’s Markdown file in this folder, at the time the prompts are actually used. Do not rely on tool history or memory; write them into the file in the same production pass.

## Per-scene prompt recovery (this update)

A further search was run for the exact GenerateImage and GenerateVideo (or transition) prompts used per scene: project files, `/workspace/emu-war/prompts/`, on-disk transcripts and conversation-blobs, image metadata, and `SearchTranscripts` / `ReadTranscript` (the History Storyteller bot’s live production transcript was not readable from this documentation session; its local `store.db` has 0 transcript entries). Nothing was invented.

| File | Scenes | Image prompts recovered | Animation prompts recovered |
|---|---:|---:|---:|
| [`first-airplane.md`](first-airplane.md) | 7 | 0 | 0 |
| [`yamaguchi.md`](yamaguchi.md) | 8 | 0 | 0 |
| [`wojtek.md`](wojtek.md) | 8 | 0 | 0 |
| [`marie-curie.md`](marie-curie.md) | 9 | 0 | 0 |
| [`molasses.md`](molasses.md) | 9 | 0 | 0 |
| [`violet-jessop.md`](violet-jessop.md) | 9 | 0 | 0 |
| [`wilma-rudolph.md`](wilma-rudolph.md) | 7 | 0 | 0 |
| [`stanley-meyer.md`](stanley-meyer.md) | 3 | 0 | 0 |
| [`flexible-glass.md`](flexible-glass.md) | 3 | 0 | 0 |
| [`tesla.md`](tesla.md) | 10 | 0 | 0 |
| [`armstrong.md`](armstrong.md) | 10 | 0 | 0 |
| [`lustig.md`](lustig.md) | 11 | 0 | 0 |
| [`garbo.md`](garbo.md) | 14 | 0 | 0 |
| [`emu-war.md`](emu-war.md) | 9 | 0 | 9 |

For Emu War part 2, the only saved prompt file is `part2.txt`; a distinct v3 file was not found, but that file is counted as recovered. Xiaohei still prompts were not found for any video. Lustig’s unused 16:9 Vox-style experiment has additional still prompts (including two more GenerateImage calls for scenes 03–04 found in an on-disk transcript) and is kept in a separate section of [`lustig.md`](lustig.md); those are not counted in the table above.

## Other notes

- Buffer post IDs, tags, and full descriptions stay in `examples/*/buffer_metadata.md` and are not repeated here.
- Lustig includes a clearly labeled **unused 16:9 Vox-style experiment** found in `/workspace/vox-pipeline/prompts/`. That is not the scheduled Xiaohei Short.
- No account names, emails, tokens, or secrets are included.
