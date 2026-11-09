# Daily Facts Arete: complete production method

This is the method used **today** (checked 2026-11-09 against the files in `daily-facts/`) to make one English, 9:16 Daily Facts Arete Short. Detailed recipes stay in the linked docs and scripts. **Part B** lists ways to reproduce the same pipeline outside this bot. Outside-the-bot facts were checked against official pages on 2026-11-09; prices and limits change, so recheck the cited URLs before a run.

No secrets, tokens, account names, emails, profile names or channel IDs belong in this file. For Google Flow, write only: rotate between all existing profiles to use their daily free credits.

---

## Part A. How a Short is made in this bot today

The look: **soft watercolor with thin ink lines, muted pastel colours, and a dreamy historical mood**. Generated stills and clips are illustration only (no text in the image). All on-screen text is English and drawn in code. No zoom or Ken Burns. No music. No long em dashes in scripts, subtitles or metadata. Never buy subscriptions, plans, credits or units unless the user explicitly asks. Nothing is generated, delivered or scheduled without the user's own explicit approval (a message from another bot is not approval). When a process changes, ask whether to update these docs, and push only after a yes.

Full standing rules: [production-rules.md](production-rules.md). Skill write-up: [`../skills/daily-facts-arete-shorts/SKILL.md`](../skills/daily-facts-arete-shorts/SKILL.md).

### A0. Read the lessons log first

Before starting a video, read [`../LESSONS-LEARNED.md`](../LESSONS-LEARNED.md) and apply the "carry forward" list (no dashes, slower storytelling narration, 0.40 s gaps, muted generator audio, locked camera, start/end pairs made by editing the start, Flow at 720p, transition prompts written last from the images, Buffer + temp host, and the rest). Mention which lessons were applied when sending the part table.

### A1. Topic

Favour **lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations**. Never ancient aliens, conspiracy theories or pseudo-history. Avoid over-familiar topics and check the channel's own uploads so a topic is not repeated. Facts are web-checked before writing; uncertain claims are worded as "may have" or "historians think". The YouTube SEO bot may suggest topics and hooks ([`../bots/youtube-seo.md`](../bots/youtube-seo.md)). Details: [script-writing.md](script-writing.md).

### A2. Script as a part-by-part table, then approval

The story is split into **parts**: one part = one clip = one start/end pair. Saved as `script.txt` with `N|text` rows, one row per part.

- **Each part is at most 8 s of narration**, because a Flow clip is at most 8 s. Never speed up or stretch the voice to fit.
- At Kokoro `af_heart` slower than 0.92, with "..." pauses, plan **about 16-18 words** per part. Treat about 20 words as the hard ceiling (a real Kokoro timing of 20 words was about 9.3 s, too long for one part).
- **Total length about 50 s to 1.5 min** (about 7-11 parts), chosen per story. Do not pad a short story. This replaced the earlier 25-40 s guideline on 2026-11-09.
- Part 1 opens with a **hook**: a question or a number, and the same words appear as on-screen text in the first second.
- Storytelling: short beats, concrete images, one surprise turn in the middle, an open question near the end.
- Write numbers as words when TTS might misread them. Regnal "II" is spoken "the Second" (see `FIX` in [`../scripts/voice/kokoro_tts_lines.py`](../scripts/voice/kokoro_tts_lines.py)); the subtitle keeps "II".
- A Hebrew translation of the script is shown for review; the English is what goes in the video.

**Before making anything** (no Krea images, no clips), send the script as a table led by one summary line:

> **N parts / N clips / ~T s / ~C Flow credits (estimate)**, e.g. `8 parts / 8 clips / ~62 s / ~80 Flow credits (estimate, Veo 3.1 Lite ~10 per clip)`

Columns: Part, Narration (English), Words, Est. s, Start frame idea, End frame idea. Words and seconds are estimates until TTS is measured; a part that measures over 8 s is rewritten or split (part N+1 then starts from part N's end frame).

**Approval gate:** (1) the part-by-part table, (2) part 1 as the sample (pair + prompt + composited sample frame + clip), (3) the rest part by part, then the later gates in A10-A14. This replaced the 2026-11-07 "script + one sample frame" gate.

Examples of older line-per-scene scripts: [`../examples/derinkuyu/script.txt`](../examples/derinkuyu/script.txt), [`../examples/hanging-gardens/script.txt`](../examples/hanging-gardens/script.txt).

### A3. Scene sheet per part

Every part gets a filled [`../templates/scene-template.md`](../templates/scene-template.md): beat, setting, characters and props, exact start and end frames, the one-way motion, accent colour, 2-3 references from [`../reference-images/`](../reference-images/README.md), continuity with the previous part, and the three prompts (start, end-edit, transition). Fill order: table -> start prompt -> start image -> end-edit prompt -> end image -> pair check -> **transition prompt last** -> prompt check -> clip.

### A4. Step 0: sketches, before any video credits

For every part, stills are made and checked against our own reference frames **before spending a video credit**. Details: [images-and-animation.md](images-and-animation.md), [video-generators/krea.md](video-generators/krea.md).

1. Pick **2-3 matching references** (same kind of shot, light or subject) and write them on the scene sheet.
2. **Start frame** in Krea (MCP), trained style trigger **`arete style`**, **aspect 9:16 passed explicitly**, 2 variants. Prompt pattern (always ends with no-text wording):

   ```
   arete style, <subject, setting, light, mood; subject large and filling the width; calm lower third>,
   soft watercolor illustration, thin delicate ink outlines, muted pastel colors, dreamy historical
   atmosphere, vertical 9:16, no text, no letters, no captions, no numbers, not photorealistic
   ```

   QA picks the better variant -> `scenes/partN_start.png`.
3. **End frame FROM the start frame**: an image-edit call with `partN_start.png` as the input (a Krea edit model that is free or non-blocked at the time, for example Flux Kontext; or an equivalent edit tool), aspect 9:16. Only the action has progressed. Never a fresh independent image. Save as `scenes/partN_end.png`.
4. Check the pair **side by side** with the references and with each other: watercolor washes, thin ink outlines, muted pastels, paper texture, no photorealism, no text, both height > width, same shot with only the action changed. Regenerate drift in Krea, never by editing on the box.
5. Continuity: when a beat continues, `part(N+1)_start.png` is a copy of `partN_end.png`.

Krea still cost is an estimate from our runs (about 2 units per image; a 9-part video roughly 55-70 units). Recheck the live balance. Never buy units unless asked.

The old Derinkuyu method (14 independent Krea scenes paired two by two) is retired: unrelated pairs make the model morph instead of move.

### A5. Transition prompt, written only after both images exist

Write `prompts/partN.txt` **only after** both `partN_start.png` and `partN_end.png` exist, by looking at the two images: the same elements, positions and props they actually show, and exactly the motion that turns the start into the end. Nothing in the prompt may contradict the images. If either sketch is regenerated, rewrite the prompt and check it again.

Break the clip down in **second-by-second beats**. The first beat is exactly the start image, the last beat settles exactly on the end image, and every beat in between says what moves, where, and in which direction, all continuing **one single one-way action** (no second action, no reversal, no unasked camera move). Always include "static locked camera, no zoom, no pan".

| Clip | Beats |
|---|---|
| 8 s | 0-1 s exactly the start image (motion just begins) / 1-3 s / 3-5 s / 5-7 s / 7-8 s settles exactly on the end image |
| 6 s | 0-1 s exactly the start image / 1-3 s / 3-5 s / 5-6 s settles exactly on the end image |
| 4 s | 0-0.5 s exactly the start image / 0.5-2 s / 2-3.5 s / 3.5-4 s settles exactly on the end image |

**Why:** planning every second and matching the prompt to the start and end images leaves the generator nothing to guess. A vague or mismatched prompt is what causes lag and glitches: jumps, backward motion, freezes or stutter, objects vanishing or morphing, and an ending that does not match the end image. Example: Derinkuyu clip 4 asked for "a stone door rolls shut" while its end frame was a ventilation shaft, so the model invented a path between two unrelated images and morphed.

**Check the prompt against both images** (elements, positions, props, direction, light, end state) before generating. This is QA Gate 0, together with the pair check. Template wording: [`../templates/scene-template.md`](../templates/scene-template.md).

### A6. Part 1 sample clip, then approval

Only after the prompt check: generate the part 1 clip (A7), run QA Gate 1, and build a composited sample frame with [`../scripts/video/preview_frame.py`](../scripts/video/preview_frame.py) (hook + one subtitle phrase drawn in code, never generator-drawn text). Send the pair, the prompt, the sample frame and the clip for **user approval of the part 1 sample**. Then continue part by part.

### A7. Clips: Google Flow, Veo 3.1 Lite, 720p, 9:16 (default)

Details: [video-generators/google-flow.md](video-generators/google-flow.md).

| Setting | Value used today |
|---|---|
| Tool | Flow **web UI in the box browser** by default |
| Model | **Veo 3.1 Lite** |
| Mode | Frames to video: **start frame + end frame** |
| Aspect | **9:16, set explicitly on every call** (Flow may remember 16:9); verify height > width after each clip |
| Resolution | **720p directly** (720x1280). No 480p test, no upscale. QA Gate 1 watches the 720p clip right away |
| Duration | **4, 6 or 8 s** (pick the shortest that covers the part's narration; 8 s is the hard max; 8 s clips often come out about 7.9 s) |
| Outputs | 1 per prompt |
| Composer | classic only; **never click the Agent button** |
| Cost | **about 10 Flow credits per clip (estimate)** |

Credits: rotate between all existing profiles to use their daily free credits. Check the balance before each clip. When every profile is low, stop and create a one-shot routine for after the daily refresh ([routines.md](routines.md)). A credit shortage is not a failure, and credits are never bought.

**gflow-cli is fallback only**, if the browser faults or has no access (Flow will not load, the session is broken, or downloads fail repeatedly). Batch helper: [`../scripts/flow/run_clips.sh`](../scripts/flow/run_clips.sh). Do not pass `--resolution` with Veo Lite (it fails pre-submit). Always pass 9:16 and classic composer mode. Official Flow credit costs, fetched 2026-11-09, are in Part B.

After each clip: `ffprobe` height > width (landscape = reject and redo); compare the last frame with `partN_end.png` (`scripts/video/chain_parts.sh check`). Flow often adds ambience audio; it is muted later (`CLIP_AUDIO=0`).

### A8. Optional path: Grok Imagine (only when Flow is not used)

Used when Flow credits are out, or a part needs this motion path. This 480p test + upscale path is **only for Grok Imagine and other tools that cannot output 720p**. Never used for Flow. Details: [video-generators/grok-imagine.md](video-generators/grok-imagine.md), [upscale-real-esrgan.md](upscale-real-esrgan.md).

Per part, two **chained 4 s clips at 480p, 9:16**:

1. Clip A (4 s) from `partN_start.png`, using the first half of the timed-beat prompt (re-timed to 4 s).
2. Take the last frame of A (`scripts/video/chain_parts.sh last`).
3. Clip B (4 s) from that last frame, continuing the **same one-way action** toward the end state.
4. `partN_end.png` is the **check target only**, never a second i2v start (that would jump at 4 s).
5. Join with [`../scripts/video/chain_parts.sh`](../scripts/video/chain_parts.sh) `join`, then `check` against the end image.
6. QA the 480p join (seam, watercolor, no drift, 9:16, no text).
7. After QA passes, **upscale instead of regenerating**: [`../scripts/video/upscale_720p.sh`](../scripts/video/upscale_720p.sh) (Real-ESRGAN on CPU, default model `realesr-animevideov3`, Lanczos to exactly 720x1280, **`PAPER_MIX` default 0.25** of a plain Lanczos upscale mixed back in so watercolor grain survives). Implementation: [`../scripts/video/esrgan_cpu.py`](../scripts/video/esrgan_cpu.py). Then QA Gate 2 (sharpness and grain). Regenerate at native 720p only if the upscale smears the ink lines.

### A9. Per-clip QA (and later gates)

Staged QA that **actually watches** the video is mandatory. The QA bot plays every clip and the full video. [`../scripts/qa/qa_check.py`](../scripts/qa/qa_check.py) is the automatic pre-check only. **Any fault -> fix -> re-QA.** Nothing is delivered or scheduled without a QA PASS on that exact file. Checklists: [qa.md](qa.md).

| Gate | When | What is checked |
|---|---|---|
| 0 | Before video credits | Pair vs references; end = same shot as start; no text; 9:16; prompt written from the images, timed beats, one-way action |
| 1 | Right after each clip (Flow: at 720p as generated) | 9:16; first/last frame vs the pair; seam vs the previous part; follows the timed beats; one-way motion, no unasked pan or zoom; no glitches, morphing, jumps, or text in frames; length covers the narration; no frozen stretch (`ffmpeg freezedetect` in `qa_check.py clip`) |
| 2 | After every upscale (non-720p tools only; **skip for Flow**) | 720x1280, same motion; sharper ink lines; watercolor grain kept (`qa_check.py sharp`) |
| 3 | Narration, before the edit | Word by word vs the script; each part <= 8 s; gaps and loudness; one recommended highlight colour |
| 4 | Full video, before delivery | See A12 |
| 5 | Before scheduling | Hosted file is byte-identical to the QA-passed file; metadata has no dashes |

User approval of all clips comes after Gate 1 (and Gate 2 if used).

### A10. Narration first (then the edit is built around it)

Never stretch the voice to fit the pictures. Details: [narration.md](narration.md).

1. [`../scripts/voice/kokoro_tts_lines.py`](../scripts/voice/kokoro_tts_lines.py) in the Kokoro venv: model [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), `KPipeline(lang_code='a')`, voice **`af_heart`**, **speed slower than 0.92** (default in the script: `KOKORO_SPEED=0.88`, confirm on the sample; 0.86-0.88 is the usual range). Storytelling punctuation, not stiff reading. Each line is trimmed at -45 dB, with 5 ms fades and about 150 ms pads, written to `audio/lNN.wav` + `audio/lines.json`.
2. Measure each part's WAV. A part over 8 s is rewritten or split, never sped up.
3. **10 s narration sample** (first 2-3 lines joined) -> user approval of voice and pace.
4. [`../scripts/voice/join_narration.py`](../scripts/voice/join_narration.py): **0.40 s gaps** between lines, internal pauses capped at **about 0.20 s**, `loudnorm I=-16 TP=-1.5 LRA=11`, 48 kHz. Writes `narration_REPORT.json`.
5. Word-by-word check against `script.txt` with [`../scripts/subtitles/whisper_word_times.py`](../scripts/subtitles/whisper_word_times.py) (faster-whisper). Re-TTS a swallowed or wrong word (for example "forgotten" heard as "forgot").
6. QA Gate 3, and QA **recommends one highlight colour**. Tell the user the colour and why, and get approval **before the edit**.

No music. Generator audio is muted in the edit.

### A11. Subtitles and assembly

Details: [subtitles-and-build.md](subtitles-and-build.md). Current editor: [`../scripts/video/build_highlight_wash.py`](../scripts/video/build_highlight_wash.py). The Derinkuyu editor, kept for that video's 7 pair-clips, is [`../scripts/video/build_flow_xfade_ass.py`](../scripts/video/build_flow_xfade_ass.py) (xfade, ASS karaoke). Themed transition helpers: [`../scripts/video/transition_paper_tear.py`](../scripts/video/transition_paper_tear.py), [`../scripts/video/transition_ink_bloom.py`](../scripts/video/transition_ink_bloom.py).

- Each part's slot is `LEAD 0.25 s + narration + TAIL 0.35 s` (capped at clip length minus the transition). The clip is trimmed to that window, never looped or stretched. The editor can pick the calmest window of the clip.
- First second: hook text drawn in code (Montserrat Bold, white, 76 px at 1080x1920, centred, top at y=300).
- Subtitles: Montserrat Bold, white, 84 px, **low bottom-centre** (top of the text at y=1344, 70% of the height), 3-7 word phrases, hard cuts, soft black shadow, thin dark stroke, no box. **English only**. No dashes.
- The spoken word is highlighted in **one** approved colour for the whole video.
- Word timing comes from faster-whisper on the script alignment; the **final check is Whisper on the final mixed audio** ([`../scripts/qa/verify_subtitle_sync.py`](../scripts/qa/verify_subtitle_sync.py)). Target: highlight within about 2 frames at 24 fps, and **never early at sentence starts**.
- Transitions are **slow and themed** (paper tear, ink bloom, golden light, cloud or burning-paper wash), never quick generic dissolves. The Derinkuyu editor uses a short xfade between pair-clips; new videos prefer the watercolor / themed helpers.
- Audio: `CLIP_AUDIO=0` (default). Final `loudnorm` I=-16 LUFS, TP -1.5.
- Drifting areas can be locked with a still mask (Hanging Gardens scene 3).
- Render: 1080x1920, 24 fps, H.264 CRF 17-18, AAC 192k, `+faststart` (Derinkuyu was rendered at 720x1280 from the 720p Flow clips).

### A12. Full-video QA, then user approval

Pre-check: `python3 scripts/qa/qa_check.py video final/<story>_final.mp4 --narration audio/narration.wav` (aspect, `freezedetect`, ebur128 loudness, source-audio leak in narration pauses) plus `verify_subtitle_sync.py` and a contact sheet ([`../scripts/qa/contact_sheet.sh`](../scripts/qa/contact_sheet.sh)). Then QA watches the whole video with sound.

Must pass: narration vs script on the final mix; about -16 LUFS, true peak <= -1 dBTP; no generator audio leaking; Whisper-timed highlights, low bottom-centre subtitles, English only, no dashes; 9:16; hook in the first second; only code-drawn text; no frozen animation; slow themed transitions; length matches the approved table. Any fault -> fix -> re-run Gate 4. Only then the user sees the video for approval.

### A13. SEO metadata, then approval

The YouTube SEO bot writes title, description and tags; save them with [`../scripts/metadata/make_metadata.py`](../scripts/metadata/make_metadata.py) (asserts no em or en dashes). Style notes: [publishing-buffer.md](publishing-buffer.md). Category Education, public, not made for kids. The SEO bot can also suggest the schedule slot.

### A14. Publish via Buffer, with a temporary public GitHub host

Direct YouTube uploads through other connectors were removed by YouTube within about a minute (Hanging Gardens). The route today:

1. QA Gate 5: the file to host is the QA-passed file (same size and `sha256sum`).
2. Commit the MP4 to a **public temp-hosting GitHub repo** and use the raw URL. Check the URL returns 200 and the right size.
3. Buffer MCP `create_post`, `mode: customScheduled`, `dueAt` = the chosen slot (Israel time converted to UTC), Education, public, media = the raw URL, text from the approved metadata.
4. Read the post back and confirm the scheduled time with the user.
5. **Schedule** 3-4 Shorts a week at **non-round times between 14:00 and 19:00 Israel time** (for example 15:17, 15:43, 16:38).
6. A one-shot routine about 45-50 minutes after the slot: confirm the Short is live, **delete the temp file** from the hosting repo, and send the link.
7. Buffer cannot set a custom thumbnail, and tags sometimes do not come through. After the user's OK, the **thumbnail and tags are set in YouTube Studio**.

### A15. Lessons-learned entry

After every video, add a short entry to [`../LESSONS-LEARNED.md`](../LESSONS-LEARNED.md) (QA faults, the user's feedback, the fixes) and update "carry forward". When the SEO review arrives, add the results (until then: pending).

### A16. Scripts and dependencies (paths)

| Step | Path |
|---|---|
| Kokoro lines | `scripts/voice/kokoro_tts_lines.py` |
| Join + loudnorm | `scripts/voice/join_narration.py` |
| Word times | `scripts/subtitles/whisper_word_times.py` |
| Sample frame | `scripts/video/preview_frame.py` |
| Current editor | `scripts/video/build_highlight_wash.py` |
| Derinkuyu xfade editor | `scripts/video/build_flow_xfade_ass.py` |
| Themed transitions | `scripts/video/transition_paper_tear.py`, `scripts/video/transition_ink_bloom.py` |
| Chain 2 x 4 s / end-frame check | `scripts/video/chain_parts.sh` |
| Real-ESRGAN 720p | `scripts/video/upscale_720p.sh`, `scripts/video/esrgan_cpu.py` |
| Flow CLI fallback | `scripts/flow/run_clips.sh` |
| QA pre-checks | `scripts/qa/qa_check.py`, `scripts/qa/verify_subtitle_sync.py`, `scripts/qa/contact_sheet.sh` |
| Metadata | `scripts/metadata/make_metadata.py` |
| Install / models | `requirements/system-deps.md`, `requirements/requirements-kokoro.txt`, `requirements/requirements-video.txt`, `requirements/requirements-flow.txt` |

Install overview is in [`../README.md`](../README.md). Font: Montserrat (Google Fonts, OFL). Video I/O: FFmpeg with libass, loudnorm, freezedetect, xfade.

---

## Part B. Alternatives outside the bot

The creative method in Part A does not change: part table, Step 0 pairs, timed-beat prompts, staged QA, Kokoro, Whisper-timed subtitles, ffmpeg assembly, Buffer + temp host. What can change is **which engine makes the stills or the clips**. The options below can replace or sit beside a step. Costs are official list prices or our labelled estimates; they change. Never buy plans or credits unless the user explicitly asks.

Facts below were checked on official pages on 2026-11-09. Anything not clearly stated there is marked **uncertain**.

### B1. grok.com / the Grok app (Grok Imagine)

**Covers:** stills (optional) and, mainly, **image-to-video clips** (Part A7 / A8).

Official xAI news states that **Grok Imagine Video 1.5** is generally available on the Imagine API, and that **Video 1.5 Fast** is on [grok.com/imagine](https://grok.com/imagine) and the iOS and Android apps. The same post gives a speed example of **6-second, 720p** clips in about 25 seconds, and shows an image-to-video API call with a start image, duration and resolution. Source: [https://x.ai/news/grok-imagine-video-1-5](https://x.ai/news/grok-imagine-video-1-5).

**How it fits:** this is the same family of tool used in earlier Arete videos (Prague v3, Petra, Alexandria) and in the chained 2 x 4 s option (A8). On the website or app you can upload a 9:16 start still and a motion prompt, download the clip, then continue the ffmpeg / Kokoro / Whisper / Buffer path locally.

**How it differs from today's in-bot path:**

- In this bot, the documented Grok path still generates **two chained 4 s clips at 480p**, then upscales with Real-ESRGAN. That reflects the **bot tool path used today**, not a documented 480p cap on the consumer product (the official news page itself cites 720p).
- Official API docs (B2) describe 1-15 s clips, 480p / 720p / 1080p, 9:16, and start+last-frame pinning on `grok-imagine-video-1.5`. **Uncertain:** whether the grok.com / app UI exposes the same duration range, resolution picker, and start+end (last-frame) controls. Those UI limits were not clearly listed on the news page checked.
- Consumer quotas and plan limits for Imagine on grok.com / the apps were **not clearly documented** on the pages checked (**uncertain**).
- Generated audio should still be muted in our edit.

### B2. xAI API (image and video endpoints)

**Covers:** stills (A4) and clips (A7 / A8), programmatically.

Official docs (fetched 2026-11-09):

- Imagine overview: [https://docs.x.ai/developers/model-capabilities/imagine](https://docs.x.ai/developers/model-capabilities/imagine)
- Video overview: [https://docs.x.ai/developers/model-capabilities/video/overview](https://docs.x.ai/developers/model-capabilities/video/overview)
- Image generation (aspect ratios include **9:16**): [https://docs.x.ai/developers/model-capabilities/images/generation](https://docs.x.ai/developers/model-capabilities/images/generation)
- REST: `POST https://api.x.ai/v1/images/generations`, `POST https://api.x.ai/v1/images/edits`, `POST https://api.x.ai/v1/videos/generations` (async; poll by `request_id`)
- Pricing: [https://docs.x.ai/developers/pricing](https://docs.x.ai/developers/pricing)

**Official capabilities (video overview and model pages):**

| Model | Duration | Resolution | Aspect | Start + end frames |
|---|---|---|---|---|
| `grok-imagine-video-1.5` | 1-15 s | 480p, 720p, 1080p (native 1080p) | includes 9:16 (i2v follows the input still) | **Yes** (`image` + `last_frame`; optional mid keyframes) |
| `grok-imagine-video-1.5-lite` | 1-15 s | 480p, 720p, 1080p (1080p upscaled from 720p) | includes 9:16 | **No** (i2v start image only) |
| `grok-imagine-video` | 1-15 s | 480p, 720p | includes 9:16 | **No** (edit / extend instead) |

Image model `grok-imagine-image-2.0`: text-to-image and edits with up to 5 reference images, aspect including 9:16, resolution 1K (default) and 2K.

**Official list prices** on the pricing page (USD, subject to change): `grok-imagine-image` $0.02 / image; `grok-imagine-image-2.0` $0.04 / image; `grok-imagine-video` $0.050 / sec; `grok-imagine-video-1.5` $0.080 / sec; `grok-imagine-video-1.5-lite` $0.020 / sec. The video overview says per-second prices by resolution are on the Models page, but the model pages fetched the same day showed only those single per-second rates. **Uncertain:** any extra resolution surcharge beyond that flat rate.

**How it differs:** a single 8 s 720p clip with a real end frame can be requested on `grok-imagine-video-1.5`, so the 2 x 4 s 480p + Real-ESRGAN chain is optional, not required. This is paid API usage, not Flow's daily free credits. Rate limit listed for 1.5: 10 requests per second. Image URLs are temporary; download promptly.

### B3. Google Flow / Veo, including the Gemini API and Vertex / Gemini Enterprise

**Covers:** clips (A7), and optionally stills inside Flow (Nano Banana models). This is already the default clip engine.

**Flow web (same as Part A, also usable in an ordinary browser):** [https://labs.google/fx/tools/flow](https://labs.google/fx/tools/flow). Official feature matrix: [https://support.google.com/flow/answer/16352836](https://support.google.com/flow/answer/16352836). Official credits: [https://support.google.com/flow/answer/16526234](https://support.google.com/flow/answer/16526234).

From those pages (2026-11-09):

- **Veo 3.1 Lite**: 720p; lengths **4, 6 or 8 s**; text-to-video, frames-to-video (first, or **first and last**), both aspect ratios (Flow's Shorts path is 9:16); no video-to-video edit and no extend on Lite.
- Credit cost **per generation** for Lite, 4/6/8 s, 720p: **10 credits** for "all other users", **5 credits** for Google AI Ultra subscribers. This matches our working estimate of about 10 credits per clip.
- With or without a subscription, **50 Google Flow credits per day**; unused daily credits do not roll over. The daily refresh is triggered by the first generation of the day. Paid plans add extra monthly credits (listed on the credits page).
- Non-subscribers may be unable to generate **videos** during peak hours (officially about 2 PM to 5 PM UTC); images and the Flow Agent may still work. Our method still never clicks Agent.
- Veo 3.1 Fast, Veo 3.1 Quality, and Omni Flash 1.1 are scheduled to retire on **5 December 2026**; Flow recommends Omni Flash 1.2 or Veo 3.1 Lite going forward. Our current method already uses Lite.

**Gemini API:** official video page [https://ai.google.dev/gemini-api/docs/video](https://ai.google.dev/gemini-api/docs/video) (redirects to [https://aistudio.google.com/docs/video](https://aistudio.google.com/docs/video)) states that **Veo 3.1 Preview** model IDs (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`, `veo-3.1-lite-generate-preview`) in the Gemini API were **shut down on 22 October 2026**. The documented replacement on that API is **Gemini Omni Flash** (`gemini-omni-1.2-flash`): [https://aistudio.google.com/docs/omni](https://aistudio.google.com/docs/omni). Official Omni facts:

- 9:16 or 16:9; default resolution 720p; also 360p, and 1080p / 4K as upscaled outputs.
- Duration any whole second from **3 to 15 s** (default 10 s).
- **First and last frame interpolation is supported**, for durations **3 to 10 s** (not above 10 s).
- Up to 6 reference images; native audio; conversational edit and extend (extend 3-10 s per turn, up to 30 s total).
- Official pricing ([https://ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing)): Omni 1.2 Flash video is on the **paid** tier (free tier "not available"). Output video $12.00 / 1M tokens, billed at 5,792 tokens per second of 720p, which the same page equates to about **$0.07 / s** at 720p (about $0.023 / s at 360p, $0.104 / s at 1080p, $0.209 / s at 4K).

**Vertex / Gemini Enterprise Agent Platform:** Veo 3.1 remains listed, including first and last frames, 9:16 and 16:9, lengths 4/6/8 s, 720p (and higher on some IDs): [https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate), [https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames). **Uncertain:** one Lite model table on the 3.1-generate page has conflicting wording about image input; recheck that page before relying on Lite i2v there. Pay-as-you-go vs fixed quota also differs by listing; read the live model card.

**How it differs:** Flow in a normal browser is the same engine as Part A, minus this bot's profile rotation and QA scripts (you would still run the scripts locally). The Gemini API path today is Omni Flash, not Veo Lite preview. Omni allows 3-10 s (not only 4/6/8) for start+end, and up to 15 s without an end frame, and it is paid token billing rather than 10 daily-credit generations. Enterprise Veo can still look like Flow's 4/6/8 s + first/last + 9:16, under a Cloud project.

### B4. Krea

**Covers:** **every still** in Part A (trained style + end-frame edit), and a tested but not default clip path (LTX).

Product: [https://www.krea.ai](https://www.krea.ai). Image user guide (9:16 called out for vertical / stories): [https://www.krea.ai/docs/user-guide/features/krea-image](https://www.krea.ai/docs/user-guide/features/krea-image). Official video API example, LTX-2.3 22B: [https://www.krea.ai/docs/api-reference/video/ltx-23-22b](https://www.krea.ai/docs/api-reference/video/ltx-23-22b). FLUX 3 Max video (start_image, end_image, 9:16, 720p or 1080p, duration 5-20 s): [https://www.krea.ai/docs/api-reference/video/flux-3-max](https://www.krea.ai/docs/api-reference/video/flux-3-max).

**How it fits:** outside the bot, use the Krea web app or API with the same `arete style` trigger and 9:16 stills, then edit the start frame into the end frame. For clips, official LTX-2.3 22B parameters include `start_image`, `end_image`, aspect **16:9 or 9:16**, and durations **5, 10, 15 or 20 s**. Official API USD prices for that model (no LoRA) start at $0.1798 for 5 s, $0.3579 for 10 s, and rise with duration.

**How it differs:** our in-bot clip default is Flow (about 10 free daily credits per 4/6/8 s Lite clip), not Krea LTX. Earlier in-bot LTX tests used a **start frame only**, with the end frame as a check target, at our own unit-cost estimates (see [video-generators/krea.md](video-generators/krea.md)). The public API now documents an `end_image` field. Unit costs inside the Krea app / MCP are **our estimates**, not an official public unit table (**uncertain** if they have changed). The free or blocked model list changes; recheck before choosing an edit model. Krea video lengths are not limited to 4/6/8 s.

### B5. Higgsfield

**Covers:** clips (A7 / A8), and potentially stills, via one API that hosts many models.

Official catalog: [https://docs.higgsfield.ai/docs/models/video-generation](https://docs.higgsfield.ai/docs/models/video-generation). A close match for our start+end method is **Wan 3.0 image-to-video**: [https://docs.higgsfield.ai/docs/models/wan-3/image-to-video](https://docs.higgsfield.ai/docs/models/wan-3/image-to-video). Official parameters: required `image_url` (first frame), optional `end_image_url` (last frame), duration **2-30 s** (default 5), resolution **480p / 720p / 1080p**, aspect including **9:16**, optional audio. Official list price for Wan 3.0: from **$0.050 / s** ([https://open.higgsfield.ai/pricing](https://open.higgsfield.ai/pricing)); discounted tiers are also listed. The exact charge for one 8 s 720p 9:16 clip with an end frame should be read from the live page (**uncertain** at the per-option level).

**How it differs:** paid per second, not Flow credits. Clip length can be longer than 8 s (our narration cap would still be 8 s per part unless we split). Several other catalog models also advertise first/last frames (for example Kling variants). We have **not** used Higgsfield on this channel, so motion quality on watercolor ink stills is untested (**uncertain**).

### B6. Hugging Face (Spaces, Inference Providers, model repos)

**Covers:** stills and clips, plus the same Kokoro, Whisper and Real-ESRGAN models we already run locally.

Official pieces:

- Inference Providers, text-to-video (example model `Wan-AI/Wan2.2-TI2V-5B`, billed through a provider such as fal): [https://huggingface.co/docs/inference-providers/tasks/text-to-video](https://huggingface.co/docs/inference-providers/tasks/text-to-video)
- Official Wan 2.2 Space (TI2V-5B): [https://huggingface.co/spaces/Wan-AI/Wan-2.2-5B](https://huggingface.co/spaces/Wan-AI/Wan-2.2-5B) (announced in the Wan2.2 README)
- Wan 2.2 I2V weights: [https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)
- Wan 2.1 first-last-frame weights: [https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)
- LTX-2: [https://huggingface.co/Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)
- Spaces as API endpoints: [https://huggingface.co/docs/hub/main/en/spaces-api-endpoints](https://huggingface.co/docs/hub/main/en/spaces-api-endpoints)

**How it fits:** a Space or Inference Provider can generate a 9:16 i2v clip from `partN_start.png`; for a true end frame, prefer a model that documents first-and-last conditioning (Wan 2.1 FLF2V, LTX-2 in Diffusers, or a Space that wraps them). Then run our local narration, subtitles, QA and Buffer steps.

**How it differs:** Wan 2.2 official I2V is **start image only** (aspect follows the input image; 480P and 720P). First+last frame is documented on **Wan 2.1 FLF2V-14B-720P**, with official examples at `1280*720` (portrait 9:16 is **not shown** in those examples: **uncertain**). Provider pricing and Space queues vary; this folder has not used HF Wan Spaces for the channel (see [video-generators/README.md](video-generators/README.md)). A Space may also inject its own watermark or length limits; check the live Space card.

### B7. Local open-source models

**Covers:** stills, clips, narration, subtitles, upscale and assembly, all on a machine you control. The box we use for this bot has no GPU suitable for the large video models; those need a local NVIDIA (or similar) GPU, or a rented one. Kokoro, faster-whisper, Real-ESRGAN (CPU) and ffmpeg already run here.

**Wan 2.2** ([https://github.com/Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2), Apache-2.0): I2V-A14B supports 480P and 720P, aspect follows the input image (so a 9:16 start still should stay vertical). TI2V-5B is documented as 720P at 24 fps and can run on a consumer 4090-class GPU (about 24 GB); the README describes generating a **5-second 720P** video with that 5B model. Official I2V takes a **single** `--image` (no end frame in the 2.2 README). Default I2V-A14B duration in seconds is **not clearly stated** in that README (**uncertain**). Heavy VRAM for the 14B I2V model (the README mentions about 80 GB without offload).

**Wan 2.1 FLF2V** ([https://github.com/Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1), weights [Wan2.1-FLF2V-14B-720P](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)): official `--task flf2v-14B --first_frame ... --last_frame ... --size 1280*720`. This is the closest open-source match to Flow's start+end pair. 9:16 support is **uncertain** (examples are 1280*720).

**LTX-2 / LTX-Video** ([https://github.com/Lightricks/LTX-2](https://github.com/Lightricks/LTX-2), [https://huggingface.co/Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)): open weights, local PyTorch or Diffusers. Official tips: width and height divisible by 32; frame count `8n+1` (121 frames at 24 fps is about 5 s). Official Diffusers docs show **first and last frame** conditioning (`index=0` and `index=-1`). A 1080p-class example canvas of 1088x1920 appears in those docs (near 9:16). Practical 8 s 9:16 720p performance depends on the GPU (**uncertain** until measured).

**HunyuanVideo 1.5** ([https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5), [https://huggingface.co/tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5)): official T2V and **I2V** at **480p and 720p**, optional super-resolution toward 1080p, default `--video_length 121` frames. Diffusers examples use 24 fps (about 5 s). `--aspect_ratio` exists and defaults to **16:9**; an official list that includes 9:16 was **not** in the README (**uncertain**). Official I2V is a start image plus prompt; first+last frame is **not described** there (**uncertain** / likely unsupported without a community extension). Licence: Tencent Hunyuan Community (not Apache). Minimum GPU memory stated as 14 GB with offloading.

**FLUX / SDXL for stills (A4):** Black Forest Labs official help ([https://help.bfl.ai/articles/8916739058-what-aspect-ratios-and-output-dimensions-are-supported](https://help.bfl.ai/articles/8916739058-what-aspect-ratios-and-output-dimensions-are-supported)) documents **FLUX.2** with arbitrary sizes including an example **portrait 9:16** at 1088x1920, and **FLUX.1 Kontext** edits at about 1 MP with `aspect_ratio` in the range 3:7 to 7:3 (9:16 sits inside that range). Kontext is already named in our Krea end-frame step. SDXL (Stability open weights) can render 9:16 if you set vertical dimensions (typically multiples of 64 or 8, depending on the pipeline). None of these, by themselves, are the trained `arete style`; you would still prompt for soft watercolor, thin ink lines and muted pastels, and compare against `reference-images/`, or train / apply a style LoRA. Photoreal default models will drift unless constrained.

**Kokoro, Whisper, Real-ESRGAN, ffmpeg** are already the local tools in Part A. Official sources: [https://github.com/hexgrad/kokoro](https://github.com/hexgrad/kokoro), [https://huggingface.co/hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Apache-2.0); [https://github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) (MIT, from OpenAI Whisper); [https://github.com/xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) (BSD-3-Clause); [https://ffmpeg.org](https://ffmpeg.org) / [https://github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg). These do not change when you swap the clip engine.

### Comparison table (clip engines, 2026-11-09)

"Yes / No" is from official docs unless marked uncertain. Costs are official list figures or our labelled estimates, and they change.

| Engine | Pipeline step | 9:16 | Native 720p | Start + end frames | Clip length | Cost model (official or estimate) | Notes |
|---|---|---|---|---|---|---|---|
| **Google Flow, Veo 3.1 Lite** (default) | Clips | Yes (both ratios; set explicitly) | Yes, 720p | Yes (frames to video, first and last) | 4 / 6 / 8 s | 10 credits / generation for non-Ultra, 5 for Ultra; 50 daily credits | Browser first; never Agent; gflow-cli only on fault |
| **Gemini Omni 1.2 Flash** (Gemini API) | Clips | Yes (9:16 / 16:9) | Yes (default 720p; 1080p/4K upscaled) | Yes, for 3-10 s | 3-15 s (start+end max 10 s) | Paid tier; about $0.07 / s at 720p (official effective rate) | Veo 3.1 Preview IDs on this API shut down 22 Oct 2026 |
| **Vertex / Gemini Enterprise Veo 3.1** | Clips | Yes (9:16 / 16:9) | Yes (720p; higher on some IDs) | Yes, on the first-and-last-frame guide | 4 / 6 / 8 s | Cloud project quotas / pricing; recheck the live card | Lite image-input wording conflicts on one page (**uncertain**) |
| **Grok Imagine, grok.com / app** | Clips (optional stills) | Likely, if the still is 9:16 (**UI not fully documented**) | Official news cites 720p | **Uncertain** in the consumer UI | Official news example: 6 s; full range **uncertain** | Plan / quota **uncertain** | In-bot path still uses 2 x 4 s at 480p + Real-ESRGAN |
| **xAI API `grok-imagine-video-1.5`** | Clips | Yes (i2v follows the still) | Yes, plus 480p and 1080p | Yes | 1-15 s | $0.080 / s (official list; resolution surcharge **uncertain**) | Best API match for our pair method |
| **xAI API `grok-imagine-video-1.5-lite`** | Clips | Yes | Yes (1080p upscaled from 720p) | No | 1-15 s | $0.020 / s | Cheaper; no last frame |
| **Krea LTX-2.3 22B API** | Clips | Yes (16:9 / 9:16) | Not named as a resolution enum on that schema | Yes (`start_image` + `end_image`) | 5 / 10 / 15 / 20 s | From $0.1798 / 5 s (official API USD) | Stills remain our default Krea use |
| **Krea FLUX 3 Max video API** | Clips | Yes | Yes (720p default, 1080p) | Yes | 5-20 s | See Krea pricing on that page | Not used on this channel yet |
| **Higgsfield Wan 3.0 i2v** | Clips | Yes | Yes (480p / 720p / 1080p) | Yes (`end_image_url`) | 2-30 s | From $0.050 / s list | Untested on Arete stills |
| **HF Inference / Wan 2.2 Space** | Clips | Follows input still (official for Wan 2.2 I2V) | 480P / 720P | Wan 2.2: no; use Wan 2.1 FLF2V or LTX-2 for pairs | Often about 5 s; confirm per Space | Provider or Space queue | Not used for this channel so far |
| **Local Wan 2.2 I2V** | Clips | Follows input still | 480P / 720P | No (start only) | 5 s documented for TI2V-5B; I2V-A14B length **uncertain** | GPU time / electricity | 14B model is VRAM-heavy |
| **Local Wan 2.1 FLF2V** | Clips | **Uncertain** (examples 1280x720) | 720P | Yes | Not clearly restated here; confirm on a run | GPU time | Closest open start+end match |
| **Local LTX-2** | Clips | Practical if size is 8n? no: size /32; 1088x1920 appears in docs | Multi-stage; can target 720p/1080p | Yes (Diffusers first+last conditions) | Frame count 8n+1 (e.g. about 5 s at 121 frames / 24 fps) | GPU time | Open weights |
| **Local HunyuanVideo 1.5** | Clips | **Uncertain** (flag exists, default 16:9) | 480p / 720p, optional SR | Official I2V is start only | Default 121 frames (about 5 s at 24 fps in examples) | GPU time | Community licence |

Stills, voice, timing, upscale and assembly can stay on Krea or FLUX/SDXL, Kokoro, faster-whisper, Real-ESRGAN and ffmpeg regardless of the clip engine.

### Official sources (checked 2026-11-09)

- Flow features: https://support.google.com/flow/answer/16352836
- Flow credits: https://support.google.com/flow/answer/16526234
- Flow product: https://labs.google/fx/tools/flow
- Gemini API video (Veo Preview shutdown): https://ai.google.dev/gemini-api/docs/video
- Gemini Omni Flash: https://aistudio.google.com/docs/omni
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini Enterprise Veo 3.1: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate
- First and last frames (Enterprise): https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames
- xAI Imagine overview: https://docs.x.ai/developers/model-capabilities/imagine
- xAI video overview: https://docs.x.ai/developers/model-capabilities/video/overview
- xAI image generation: https://docs.x.ai/developers/model-capabilities/images/generation
- xAI pricing: https://docs.x.ai/developers/pricing
- Grok Imagine Video 1.5 news: https://x.ai/news/grok-imagine-video-1-5
- Krea image guide: https://www.krea.ai/docs/user-guide/features/krea-image
- Krea LTX-2.3 22B: https://www.krea.ai/docs/api-reference/video/ltx-23-22b
- Krea FLUX 3 Max video: https://www.krea.ai/docs/api-reference/video/flux-3-max
- Higgsfield video catalog: https://docs.higgsfield.ai/docs/models/video-generation
- Higgsfield Wan 3.0 i2v: https://docs.higgsfield.ai/docs/models/wan-3/image-to-video
- Higgsfield pricing: https://open.higgsfield.ai/pricing
- HF text-to-video inference: https://huggingface.co/docs/inference-providers/tasks/text-to-video
- HF Spaces as APIs: https://huggingface.co/docs/hub/main/en/spaces-api-endpoints
- Wan 2.2: https://github.com/Wan-Video/Wan2.2
- Wan 2.1 (FLF2V): https://github.com/Wan-Video/Wan2.1
- LTX-2: https://github.com/Lightricks/LTX-2 and https://huggingface.co/Lightricks/LTX-2
- LTX-2 Diffusers (first/last frame): https://huggingface.co/docs/diffusers/api/pipelines/ltx2
- HunyuanVideo 1.5: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 and https://huggingface.co/tencent/HunyuanVideo-1.5
- FLUX aspect ratios: https://help.bfl.ai/articles/8916739058-what-aspect-ratios-and-output-dimensions-are-supported
- Kokoro: https://github.com/hexgrad/kokoro and https://huggingface.co/hexgrad/Kokoro-82M
- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- Real-ESRGAN: https://github.com/xinntao/Real-ESRGAN
- FFmpeg: https://ffmpeg.org

### Items marked uncertain or unverified

1. **grok.com / Grok app UI limits** (max duration, resolution picker, start+end frame controls, plan quotas) are not clearly listed on the official news page, which only confirms Video 1.5 Fast on those clients and a 6 s / 720p speed example.
2. **xAI API prices by resolution** (different $/s at 480p vs 720p vs 1080p) were not present on the pricing and model pages fetched; those pages showed one rate per model. Treat a resolution surcharge as unverified unless the live Models page shows it.
3. **Whether any non-preview Veo ID remains on the consumer Gemini API** after the 22 October 2026 Preview shutdown, versus Omni Flash plus Enterprise / Vertex only, should be rechecked on the live docs.
4. **Gemini Enterprise `veo-3.1-lite-generate-001` image / i2v support** has conflicting official wording on one model card versus the first-and-last-frame guide.
5. **Flow "Lower Priority" Lite credit cost** (who can use it is documented; the exact credit number was not clearly captured from the help table as fetched).
6. **Wan 2.2 I2V-A14B default duration** in seconds is not clearly stated in the official README (5 s is stated for TI2V-5B).
7. **Wan 2.1 FLF2V at 9:16**: official examples use 1280x720 only.
8. **HunyuanVideo 1.5 9:16 support** and **first+last frame support** are not documented in the official README (I2V is start + prompt; aspect flag defaults to 16:9).
9. **Local LTX-2 runtime** for a full 8 s 9:16 720p part on a given GPU was not measured here.
10. **Krea app / MCP unit prices** remain our own estimates; only the public API USD table for LTX-2.3 22B (and similar) is official. The live free/blocked model list changes.
11. **Higgsfield exact price** for one 8 s 720p 9:16 Wan 3.0 clip with an end frame (the page lists "from $0.050 / s" plus discount tiers). Motion quality on Arete watercolor stills is untested.
12. **In-bot Grok 480p-then-upscale** is the current bot-tool path, not a documented consumer-product maximum of 480p.
13. **HF Space length, watermark and queue limits** depend on the live Space and were not re-verified run-by-run for this doc.
14. **Buffer dropping YouTube tags** is from our own publishes, not an official Buffer guarantee.

If a process in Part A changes, ask whether to update this file, and push only after a yes.
