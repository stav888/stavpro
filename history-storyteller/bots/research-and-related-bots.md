# Research and related bots

## Topic research
Topic shortlists (e.g. the 5 picks of 2026-11-09: Garbo, Robert Smalls, Togo, Emu War, Christmas Truce) are produced by the producer with research help (web search / research subagents launched by the producer) plus the YouTube SEO bot. Each pick carries one authoritative source link. No dedicated standing "history research" bot was found among the user's bots; the bot named "מחקר" (caafcb77-60fd-465d-90bb-0404d13e5e70) is for the Instagram hidden-knowledge page (Pinterest pairs), not for history topics.

## Sibling bots sharing infrastructure
| Bot | Agent id | Shared pieces |
|---|---|---|
| Daily Facts Arete Style | bd551ec7-720a-4ef7-a863-9e91cc0bf76c | watercolor history Shorts; source of the Kokoro voice choice; uses `stav888/video-hosting/daily-facts-arete-style/`; `/workspace/qa-arete-*` folders show its videos also go through QA; method (Nov 2026): gflow-cli + Veo 3.1 Lite start/end frames |
| מספרת סיפורים (TAT_MIND) | b4c184a5-047e-4c14-b58d-14c2b6ba6de6 | Book-to-Video Shorts; Pocket TTS (kyutai-labs/pocket-tts, voice "mary"); uses `stav888/video-hosting/tat-mind-storyteller/` |
| APK NUMROLOGY | 292c3d9c-ab7c-4934-9587-b49cbb1f21c5 | user's primary router bot; forwards tasks to the right bot |
| Disk Saver | 2425c853-bbe7-455e-a546-c5b80c536650 | audits box disk usage, proposes cleanup (only with approval) — relevant because /workspace holds all video versions |

Usage budget note (user measurement, 2026-10-23/11-04): one ~1 min video ≈ 8–10% of the Grok Bot plan; weekly plan ≈ 4 history videos + 2–3 Daily Facts.
