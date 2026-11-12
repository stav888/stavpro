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

## Other notes

- Buffer post IDs, tags, and full descriptions stay in `examples/*/buffer_metadata.md` and are not repeated here.
- Lustig includes a clearly labeled **unused 16:9 Vox-style experiment** found in `/workspace/vox-pipeline/prompts/`. That is not the scheduled Xiaohei Short.
- No account names, emails, tokens, or secrets are included.
