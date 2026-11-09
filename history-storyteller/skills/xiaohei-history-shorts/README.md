# Xiaohei History Shorts skill — two options

Both versions are kept so you can choose the one that fits each video. Both use the same visual style (Ian Xiaohei, white background, wobbly black lines, Xiaohei performing the action), the same 1080x1920 format with Patrick Hand subtitles, and the same rule of no zoom, pan or loops.

| | **Current** — [`SKILL.md`](SKILL.md) | **Legacy** — [`SKILL-legacy-edge-tts.md`](SKILL-legacy-edge-tts.md) |
|---|---|---|
| Period | since Nov 2026 (approved 2026-11-07, expanded trial from 2026-11-09) | Oct 19–30, 2026 |
| Voice | Chatterbox TTS (MIT) cloned from a Kokoro `am_eric` clip (Apache-2.0): seed 7, exaggeration 0.6, cfg 0.45; backup `bm_george` | edge-tts `en-US-ChristopherNeural`, rate -5% |
| Recording method | one take **per paragraph**, joined with natural pauses; breath noise removed; no stretching; loudnorm -16 | **one single pass** over the whole script, periods written as semicolons for sharp first words; gaps normalized to ~0.4 s; loudnorm -16 |
| Script length / style | **expanded** engaging story, ~70–85 s (trial; the SEO bot reviews on 2026-11-24) | **short**, under 60 s (~90–110 words) |
| Animation smoothing | one-way image-to-video + **RIFE 4.7** retime to true 24 fps, jolt fixes, frame-splice patches | one-way image-to-video, single pass; may be slowed with setpts up to 1.35x if short; no RIFE step |
| Subtitles | sentence-locked, from faster-whisper word timestamps on the final audio | sentence-locked, from edge-tts SentenceBoundary/WordBoundary cross-checked with ASR |
| Approval flow | Hebrew script **+ one sample frame** before any full production | Hebrew script approval for expanded/long scripts; short user-supplied stories could go straight to production |
| QA | QA סרטונים must pass before delivery | same |
| Publishing | SEO bot sets metadata and slot (1–2 days apart); commit-pinned raw URL from `stav888/video-hosting`; Buffer `create_post` (category 27, public, madeForKids false, isAiGenerated true); cleanup routine after publish | not covered in the legacy skill text (in that period: Buffer upload with title, description, tags and AI label, time chosen by the bot) |

## When each fits
- **Current:** the default. Use it for stories with several beats that benefit from a fuller telling (spies, cons, inventors), and when the warmer, energetic voice matters. It costs more compute (Chatterbox on CPU plus RIFE) and needs the sample-frame approval.
- **Legacy:** use it for quick, simple stories that fit under 60 s, or as a fallback if Chatterbox or RIFE isn't available. Also use it if the 2026-11-24 review shows short scripts perform better (then combine short scripts with whichever voice the user prefers). It's lighter and faster: edge-tts is a free online TTS and has no GPU/CPU model.

To install one as a Grok Bot skill, copy the chosen file as `SKILL.md` into a skill folder. Both keep their original frontmatter.
