# Lessons learned — continuous improvement

> **Rule:** every production should be **better than the last**. After each video, append a short entry below (QA faults, user feedback, what was fixed, SEO performance once known). **Before starting the next video**, read this log and apply its lessons to prompts, timing, sketches, audio, and layout.

Related: [`qa.md`](qa.md) · [`scene-by-scene-production.md`](scene-by-scene-production.md) · [`../README.md`](../README.md)

---

## 2026-11-09 — pipeline rules from recent feedback (seed)

Sources: user feedback on frames/layout, Flow/Grok process decisions, Garbo QA rounds, contact-sheet checks.

| Lesson | What went wrong / what we learned | Apply next time |
|---|---|---|
| **16:9 aspect** | Generators (esp. Flow) happily return landscape if aspect is left to a default or Agent mode soft-hints it. | Always pass **9:16** explicitly; classic composer only; verify **height > width** with ffprobe/PIL; reject and regenerate landscape. |
| **Generator drawing text** | Image tools baked title/captions into the still; underline came out short and subtitle size wrong when the generator drew them. | Stills/clips = **illustration only** (`no text, no letters, no captions`). All English text is composited later by `build.py` / `preview_frame.py` with locked sizes (title 64; underline x=400–680 / 6 px; subtitles 62). |
| **Art too small** | Xiaohei sat as a small centred vignette; after bbox crop it stayed tiny on the 1080×1920 canvas. | Prompt for a **large** figure filling most of the **width**; scene spread across the frame, not a mid-frame miniature. |
| **Independent stills vs start/end pairs** | Making a separate still per frame broke start→end i2v (jump between unrelated compositions). | **One matched pair per part:** `partN_start` + `partN_end` (end FROM start); one transition prompt; never independent stills of every frame. |
| **8 s Flow limit** | Flow/Veo start→end is max **8 s** (4/6/8 only). Longer narration forced stretch or bad cuts. | Write narration ≤~18–20 words / ≤8 s per part; rewrite or **split**; next start matches previous end; never stretch audio. |
| **Regenerate vs upscale** | Re-running at 720p after a good 480p take produced **different motion**, not the same take sharper. | QA at **480p** → upscale approved clip with Real-ESRGAN to **720×1280**; regenerate 720p only if upscale is soft/broken, then full QA again. |
| **Garbo contact sheet** | Midpoint frames must match the spoken line; order mistakes and frozen/looped motion failed QA (Garbo took v1–v9). | After render, inspect a **contact sheet of every part's midpoint**; confirm visual ↔ subtitle; no loop/freeze/zoom; send full video to QA סרטונים until pass. |
| **Prompt vs actual sketches** | A transition prompt written only from the script idea can contradict the generated start/end (wrong side, wrong prop, extra characters) or lack timing, so the clip drifts. | Write / rewrite `prompts/partN.txt` **after** the sketches exist, from what the images show; include **timed beats**; check against both images before generate; rewrite if a sketch changes; QA compares clip timing to the beats ([`scene-by-scene-production.md`](scene-by-scene-production.md) §1b). |

### Checklist before the next story
- [ ] Re-read this file (and any newer entries below).
- [ ] Script table: N parts ≤8 s each; 9:16; English-only overlays planned via `build.py`.
- [ ] Sketches: refs from `reference-images/`; large art; no text; start/end pairs only.
- [ ] Transition prompts: written **after** sketches from the actual images + timed beats; prompt-check before generate.
- [ ] Clips: Flow ≤8 s or Grok 2×4 s chain; 480p QA → upscale; QA at every stage ([`qa.md`](qa.md)).
- [ ] After delivery: append a new dated entry (faults, fixes, SEO when known).

---

## Template for new entries

```
## YYYY-MM-DD — <story slug> (vN)

- **QA faults:** …
- **User feedback:** …
- **Fixed by:** …
- **SEO / performance (when known):** views, CTR, retention notes from YouTube SEO bot …
- **Carry forward:** 1–3 concrete rules for the next video
```

## 2026-11-09 — emu-war (full Short)

- **QA faults (part 1):** ping-pong when end sketch x ≈ start x but prompt asked for a walk; chain Clip B with end-pin reversed motion; fence fade; emu through soldier; red muzzle blinks; holds.
- **User feedback:** prefer continuous Grok 8s start→end; max 3 versions then pick best and finish whole script; Grok only (no Flow).
- **Fixed by:** rewrite motion to match actual sketch delta (locked x + emus from right edge); single continuous GenerateVideo; numeric gates (x range, red min, diff spikes); Lanczos upscale when Vulkan ESRGAN unavailable.
- **SEO / performance (when known):** —
- **Carry forward:**
  1. End-sketch character x must equal start x + intended move; otherwise prompt only the drawn delta.
  2. Prefer one continuous Grok clip (start + last_frame) over A/B chain when ≤8–15 s.
  3. Crowds/animals enter from frame edge only; keep fixed props + constant accents; living motion through the end (no freeze).

## 2026-11-09 — emu-war (final_v2 after full-video QA FAIL)

- **QA faults:** multi-sentence subtitle cards (parts 8–9); cards 0.41–0.91 s early vs first word; weak “A” + mid pauses >0.6 s; holds from freeze+setpts stretch (parts 2/3/4/6/8/9); part4 red zero ~26%; part1 at version cap with end morph.
- **User feedback:** fix cheapest-first (subs → audio → retime → regen); part1 stays v2; max 3 versions; do not upload/schedule.
- **Fixed by:** sentence-split cards word-synced via ASR; re-render p8 + cap ASR gaps to ~0.35 s; hold-drop retime then setpts; regen part3/part4 v2 + part2 v3 (last); Lanczos upscale; keep v1 final beside v2.
- **SEO / performance (when known):** —
- **Carry forward:**
  1. Subtitle cards = one sentence each; start ≤2 frames from ASR first-word onset.
  2. Cap narration word-gaps to ~0.35 s after join; verify every first phoneme is audible.
  3. Drop hold frames before setpts; only spend a version slot when living seconds cannot cover the narration slot.
