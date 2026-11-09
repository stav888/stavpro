# Examples

## Published Shorts (links checked 2026-11-09 with YouTube oEmbed)
| Video | Link | Pipeline generation | Files here |
|---|---|---|---|
| 20,000 People Lived 85 Meters Underground 🕳️ (Derinkuyu) | https://www.youtube.com/shorts/FbjPMiFmAzw | current: Krea stills -> Flow Veo 3.1 Lite pairs -> Kokoro -> ASS karaoke -> Buffer | [`derinkuyu/`](derinkuyu/): script, Krea prompts, Flow motion prompts, narration QA report |
| Did the Hanging Gardens of Babylon Ever Exist? 🌿 | https://www.youtube.com/shorts/IpF1nUOSWbY | Krea stills -> Flow clips -> Kokoro -> Whisper-timed highlight + watercolor wash (`build_highlight_wash.py`) | [`hanging-gardens/`](hanging-gardens/): script, final metadata |
| How Did a Whole City Vanish Inside a Cliff? Petra's Mystery 😱 | https://www.youtube.com/shorts/JjFwSP6t6k8 | earlier pipeline: Krea trained-style stills, clips made before the switch to Flow (Grok Imagine era) | [`petra/`](petra/): script |
| Was Cleopatra Closer to the Moon Landing Than the Pyramids? 🤯 (Great Pyramid of Giza) | https://www.youtube.com/shorts/Wvbv_iAVoMg | earlier Flow test: watercolor stills + Flow frame clips with themed pigment-bloom / ink-wash transitions, edge-tts narration and a serif title card (before the Kokoro and highlight-subtitle rules) | [`giza/`](giza/): script, per-scene image + motion prompt plan |

Channel: https://www.youtube.com/@Daily_Facts_Arete

## In progress (not published)
- **Olmec heads** ([`olmec-heads/`](olmec-heads/)): 15-line script + Krea prompts; Krea stills made and QA-picked, waiting for the next approval steps.

No video or audio binaries are stored here (repo stays small); watch the published links instead.
