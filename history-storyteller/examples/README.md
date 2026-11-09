# Examples — real text artifacts from finished Shorts

Text only: scripts, paragraph/sentence files, timing tables, subtitle chunks, and the Buffer metadata as posted. No media and no secrets. Every folder has a `buffer_metadata.md` (title, description, publish time, flags) read from Buffer on 2026-11-09.

| Folder | Topic | Final file / length | Narration | Script style | Published (Israel) |
|---|---|---|---|---|---|
| `first-airplane/` | Wright brothers, the first airplane (first channel video) | sketch-2 v6, 130.0 s | edge-tts `en-US-ChristopherNeural` -5%, 7 segment files `seg1..7` (no generator script on the box, so the voice is from the channel notes) | expanded (7 segments) | 2026-10-19 21:33 |
| `yamaguchi/` | Tsutomu Yamaguchi survived two atomic bombs | v2, 48.0 s | edge-tts ChristopherNeural -5%, per-sentence files (`make_tts.py`) | short | 2026-10-20 19:00 |
| `wojtek/` | Wojtek the soldier bear | v6, 38.6 s | edge-tts ChristopherNeural -5%; v1 per sentence, final rebuilt as continuous narration with edited pauses | short | 2026-10-22 10:42 |
| `marie-curie/` | Marie Curie and radium | v2, 49.9 s | edge-tts ChristopherNeural -5%, **single pass with semicolons** (`script_tts_semicolons.txt`) | short | 2026-10-23 19:00 |
| `molasses/` | Great Boston Molasses Flood, 1919 | v1, 47.3 s | edge-tts, single pass with semicolons | short | 2026-10-26 13:52 |
| `violet-jessop/` | "Miss Unsinkable" Violet Jessop | v3, 51.2 s | edge-tts, single pass with semicolons | short | 2026-10-28 17:23 |
| `wilma-rudolph/` | Wilma Rudolph | v5, 49.2 s | edge-tts, single pass with semicolons | short | 2026-10-30 16:17 |
| `stanley-meyer/` | Stanley Meyer's "water car" | v2, 53.9 s | **Chatterbox** am_eric, seed 7, exaggeration 0.75, cfg 0.4, **3 paragraphs** (`p1..p3`) | short | 2026-11-01 17:47 |
| `flexible-glass/` | Tiberius and the unbreakable glass | v3, 42.1 s | Chatterbox am_eric, seed 7, 0.75 / 0.4, 3 paragraphs | short | 2026-11-03 18:47 |
| `tesla/` | Tesla's Wardenclyffe tower | v3, 45.3 s | Chatterbox am_eric, seed 7, 0.75 / 0.4, single full pass | short | 2026-11-05 18:43 |
| `armstrong/` | Edwin Armstrong and FM radio | v3, 52.6 s | Chatterbox am_eric, seed 7, 0.75 / 0.4, single full pass | short | 2026-11-08 18:52 |
| `lustig/` | Victor Lustig sells the Eiffel Tower | v8, 51.6 s | Chatterbox am_eric, seed 7, **0.6 / 0.45** (approved setting), single full pass (`gen7f.py`) | short (v1 script with Hebrew + sources included) | scheduled 2026-11-10 18:47 |
| `garbo/` | Agent Garbo, the D-Day double agent | v9, 81.2 s | Chatterbox am_eric, seed 7, 0.6 / 0.45, **4 paragraphs** joined naturally (current standard) | **expanded (trial)** | scheduled 2026-11-12 18:43 |

How the voice evolved:
1. Edge-tts (Oct 19–30): first per-sentence files, then one single pass with semicolons for sharper first words.
2. Chatterbox clone of Kokoro am_eric at 0.75 / 0.4 (Nov 1–8).
3. Approved setting 0.6 / 0.45 from 2026-11-07 (Lustig, Garbo), recorded per paragraph from Garbo on.

## File types
| File | Meaning |
|---|---|
| `script_en.txt`, `script_final_en.txt`, `script_en_expanded.txt` | final English narration script |
| `script_he_expanded.txt`, `script_v1_en_he_sources.md` | Hebrew script shown to the user for approval (+ sources and caveats for Lustig) |
| `p1.txt..pN.txt`, `seg*.txt` | one TTS take per file (paragraph / segment) |
| `script_tts_semicolons.txt` | edge-tts input, with periods replaced by semicolons (displayed subtitles keep normal punctuation) |
| `sentences.txt` | one sentence per line: the timing and subtitle units |
| `audio_timing.json` | sentence table: start / onset / end / speech_end and first-word checks |
| `subtitle_chunks_timing.json`, `timing.json`, `subtitle_timing.csv`, `subtitle_splits.json` | subtitle chunks and scene cuts per sentence |
| `ons.json` | per-word onsets used for subtitle splits |
| `self_check_first_words.txt` | first-word RMS and ASR self-check (Marie Curie) |
| `build_notes.md` | build notes (Lustig) |
| `buffer_metadata.md` | title, description, time, privacy, category and flags as stored in Buffer |

## Not available
- **Image/video prompts:** they were passed straight to GenerateImage/GenerateVideo and never saved as files.
- **Tag lists:** only Garbo's tag list is saved. For the other videos the SEO bot added tags via the YouTube API, and those lists aren't on the box.
- **Hebrew scripts:** they exist as files only for Garbo and Lustig.
- **AI flag on sent posts:** Buffer shows `isAiGenerated: false` on the sent posts (the field is `true` on the two scheduled ones). Whether the AI label was applied in YouTube Studio for those videos is not verified here.
