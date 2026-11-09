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

### Checklist before the next story
- [ ] Re-read this file (and any newer entries below).
- [ ] Script table: N parts ≤8 s each; 9:16; English-only overlays planned via `build.py`.
- [ ] Sketches: refs from `reference-images/`; large art; no text; start/end pairs only.
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
