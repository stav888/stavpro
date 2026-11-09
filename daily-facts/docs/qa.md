# 5. QA: staged gates (mandatory, from 2026-11-09)

**Every production goes through QA that actually watches the video** at each stage. The **QA סרטונים bot** plays every clip and the full video (frame by frame where needed, with sound), measures, and returns PASS or a numbered fault list with timestamps and evidence frames. See [`../bots/qa-videos.md`](../bots/qa-videos.md).

**Rules**
- Any fault -> fix -> **re-QA the fixed item** (and the full video again if the edit changed). Repeat until PASS.
- **Nothing is delivered to the user and nothing is scheduled on Buffer without a QA PASS** for the exact file being delivered/scheduled.
- `scripts/qa/qa_check.py` runs first as an automatic pre-check (aspect, length, frozen frames, seams, sharpness, loudness, source-audio leak). It does not replace QA watching the video; it gives QA the numbers.
- QA recommends; the user approves (approval gates are in [production-rules § 6](production-rules.md#6-approval-flow)).
- Every QA fault and its fix also goes into [`../LESSONS-LEARNED.md`](../LESSONS-LEARNED.md) when the video is done.

## Gate 0: Step 0 pairs (before any video credits)
What QA gets: per part `partN_start` variants, then start + end side by side with the 2-3 chosen reference frames + the scene sheet.
- [ ] watercolor look matches `reference-images/` (washes, thin ink lines, muted pastels, paper texture, not photorealistic)
- [ ] end frame = same shot as start, only the action changed (camera, framing, scale, palette, characters unchanged)
- [ ] no text, letters or numbers anywhere in the image
- [ ] subject large and filling the width; lower ~30% calm for subtitles
- [ ] history plausible (period clothing, architecture, props)
- [ ] height > width
Output: best start variant + "pair OK" or "regenerate partN_end because ...".

## Gate 1: every clip, right after generation (QA watches each clip)
Pre-check: `python3 scripts/qa/qa_check.py clip clips/partN.mp4 --start scenes/partN_start.png --end scenes/partN_end.png` and, from part 2 on, `qa_check.py seam clips/part(N-1).mp4 clips/partN.mp4 [--continuous]`.
- [ ] **9:16** (height > width); landscape = reject
- [ ] **continuity at the seams**: first frame matches `partN_start`, last frame matches `partN_end`; where part N+1 continues part N, part N's last frame = part N+1's first frame (`--continuous` must PASS)
- [ ] **one-way motion**: no loop, ping-pong, reverse, drift back and forth; camera locked or very gentle, **no pans or zooms** the prompt did not ask for
- [ ] **no glitches or distortions**: melting faces, hands, buildings; flicker; morphing between unrelated shapes; sudden jumps
- [ ] **no text** appearing anywhere in any frame (signs, fake letters, watermarks)
- [ ] length 4/6/8 s covers the part's narration; no frozen stretch
- [ ] Grok option: no visible seam where clip B starts from clip A's last frame
Output per clip: keep / lock the drifting area / re-roll. Only kept clips go to the user.

## Gate 2: after every upscale
Pre-check: `python3 scripts/qa/qa_check.py sharp gen/partN_480.mp4 clips/partN.mp4`.
- [ ] 720x1280, same motion and length as the approved 480p take
- [ ] **sharper**: ink lines crisp, no smearing, halos or ringing
- [ ] **watercolor survived**: paper grain and soft washes still visible, not plastic (if lost: raise `PAPER_MIX` and re-run, or try `ESRGAN_MODEL=general`)
- [ ] no new artefacts on faces or fine details (compare mid and last frame with the 480p source)
Output: PASS or "regenerate at native 720p".

## Gate 3: narration (before the edit)
- [ ] word by word against `script.txt` (faster-whisper; every word present, nothing swallowed, e.g. "forgotten" not heard as "forgot")
- [ ] pace slower than 0.92, storytelling not stiff; each part <= 8 s
- [ ] gaps 0.40 s between lines, internal pauses ~0.2 s; loudness ~-16 LUFS (`narration_REPORT.json`)
- [ ] pronunciation (regnal "II" = "the Second", names)
Output: PASS or lines to re-record. Plus one recommended highlight colour for the user's approval.

## Gate 4: full video, before anything is delivered
Pre-check: `python3 scripts/qa/qa_check.py video final/<story>_final.mp4 --narration audio/narration.wav` and `python3 scripts/qa/verify_subtitle_sync.py` (edit the file name and spot-check times), plus a contact sheet (`scripts/qa/contact_sheet.sh`). Then QA watches the whole video with sound.

Audio
- [ ] narration word by word vs the script on the **final mix**
- [ ] loudness ~-16 LUFS integrated, true peak <= -1 dBTP
- [ ] **no source audio leaking** (generator ambience, voices, music): mix inside narration pauses near silence (< -50 dBFS); generator audio is muted by default (`CLIP_AUDIO=0`)
- [ ] no clicks, cut-off first/last words

Subtitles
- [ ] **sync from Whisper on the final mix**: highlight within ~2 frames, **never early at sentence starts**, no phrase card crossing a sentence boundary
- [ ] **size and position**: Montserrat Bold white, low bottom-centre (top of the text at ~70% of the height), inside the safe area, readable on light scenes
- [ ] one highlight colour throughout; no em/en dashes; **English only**

Layout and picture
- [ ] 9:16, illustration fills the frame; hook text visible in the first second
- [ ] only code-drawn text on screen (no generator lettering)
- [ ] **no frozen animation** (no still stretch longer than a transition), no loops, no unwanted pans/zooms
- [ ] transitions slow and themed; no hard jumps between parts
- [ ] length matches the approved part table

Output: PASS (then the user sees the video) or a numbered fault list -> fix -> re-run Gate 4.

## Gate 5: before scheduling
- [ ] the file uploaded to the temp host is byte-identical to the QA-passed file (same size / checksum)
- [ ] metadata has no dashes, facts match the script
Only then the Buffer post is created ([publishing](publishing-buffer.md)).

## Self-checks before sending anything to QA
- `ffprobe` every clip and the final file, PIL every still: height > width (landscape = reject).
- `grep -P "\x{2014}|\x{2013}"` on script, subtitles and metadata returns nothing.
- `qa_check.py` results attached to the QA request.
