# History Storyteller — full production pipeline (backup + how-to)

> **בעברית בקצרה:** התיקייה הזו היא גיבוי מלא של תהליך העבודה של הבוט "סיפורים מההיסטוריה". יש בה: הסבר שלב אחר שלב (תסריט → אישור → תמונות → אנימציה → קריינות → כתוביות → QA → SEO → Buffer → ניקוי), הגדרות הקריינות המדויקות (Chatterbox עם קול am_eric, seed 7, exaggeration 0.6, cfg 0.45), קובצי requirements, הריפואים שצריך, הסקריפטים האמיתיים שבהם השתמשנו בסרטון Garbo, ותיעוד של הבוטים האחרים (QA ו־SEO) ואיך עובדים איתם. בלי סיסמאות או טוקנים.

Channel: **Smart History Knowledge** (YouTube Shorts). Output: English-only, 9:16 1080x1920, 24 fps, true chronological history stories in the Ian Xiaohei illustration style (white background, wobbly black lines, black Xiaohei character performing the action). Reference video: *Agent Garbo* (`garbo-history-v9.mp4`, 81 s), scheduled 2026-11-12 18:43 Israel.

## Pipeline at a glance
| # | Step | Tool / file | Doc |
|---|---|---|---|
| 1 | Pick topic (research + SEO bot), write script in paragraphs + `sentences.txt` | – | `docs/script-writing.md` |
| 2 | **User approval**: Hebrew script + 1 sample frame | – | same |
| 3 | Stills per scene in Xiaohei style | Grok Bot GenerateImage + repo refs | `docs/images-and-animation.md` |
| 4 | Narration: Chatterbox per paragraph -> join -> breath gate + loudnorm -16 -> ASR | `scripts/voice/*` | `docs/narration.md` |
| 5 | Sentence timing table | `scripts/video/sentence_timing.py` | `docs/subtitles-and-build.md` |
| 6 | Image-to-video per scene (one-way motion) | Grok Bot GenerateVideo (Grok Imagine) | `docs/images-and-animation.md` |
| 7 | RIFE 4.7 one-way retime to slot, jolt fixes | `scripts/video/rife_eq.py`, `jolt_fix.py`, `fix_frames.py` | same |
| 8 | Compose: art, title, counter, sentence-locked subtitles, audio | `scripts/video/build.py` | `docs/subtitles-and-build.md` |
| 9 | Self-QA, then **QA סרטונים** bot until pass | `scripts/qa/*` | `docs/qa.md`, `bots/qa-videos.md` |
| 10 | SEO metadata + slot from **YouTube SEO** bot | – | `bots/youtube-seo.md` |
| 11 | **User approval**, host on video-hosting (commit-pinned raw URL), Buffer `create_post` | gh, Buffer MCP | `docs/publishing-buffer.md` |
| 12 | After publish: delete hosted file, SEO adds tags, performance review | routines | `docs/routines.md` |

## Narration quick recipe (the part other bots ask about)
```python
import torchaudio as ta, torch, perth
if perth.PerthImplicitWatermarker is None: perth.PerthImplicitWatermarker = perth.DummyWatermarker
from chatterbox.tts import ChatterboxTTS            # pip install chatterbox-tts==0.1.7 (MIT)
m = ChatterboxTTS.from_pretrained(device="cpu")     # HF ResembleAI/chatterbox
for i in range(1, N+1):                             # one take per paragraph pI.txt
    torch.manual_seed(7)
    w = m.generate(open(f"p{i}.txt").read().strip(),
                   audio_prompt_path="k_am_eric.wav",  # Kokoro-82M am_eric clip (Apache-2.0)
                   exaggeration=0.6, cfg_weight=0.45)
    ta.save(f"p{i}.wav", w, m.sr)
```
Then: concat `p*.wav` (no crossfade, no stretch) -> `process_narration.py` (loudnorm I=-16 TP=-1.5 LRA=11, 48 kHz, breaths in pauses gated, 0.15 s head pad) -> `asr_words.py` (faster-whisper small) for timing and first-word QA. Full details: `docs/narration.md`.

## Repos used
| Repo | Why |
|---|---|
| https://github.com/helloianneo/ian-xiaohei-illustrations | visual style + reference images (MIT) |
| https://github.com/resemble-ai/chatterbox (PyPI `chatterbox-tts`) | narration TTS (MIT) |
| https://huggingface.co/hexgrad/Kokoro-82M (PyPI `kokoro`) | am_eric reference voice (Apache-2.0) |
| https://github.com/SYSTRAN/faster-whisper | ASR word timestamps |
| https://github.com/Fannovel16/ComfyUI-Frame-Interpolation @26545cc | RIFE 4.7 `IFNet` code |
| https://huggingface.co/jasonot/mycomfyui (`rife47.pth`) | RIFE 4.7 weights |
| https://github.com/stav888/video-hosting (public) | temporary MP4 hosting for Buffer |
| https://github.com/AgriciDaniel/claude-youtube, https://github.com/sergebulaev/youtube-skills | SEO bot playbooks |

## Install
```bash
sudo apt-get install -y ffmpeg git
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv -p 3.11 chatterbox_venv && uv pip install --python chatterbox_venv/bin/python -r requirements/requirements-tts.txt --extra-index-url https://download.pytorch.org/whl/cpu
uv venv -p 3.12 kokoro_venv     && uv pip install --python kokoro_venv/bin/python     -r requirements/requirements-kokoro.txt --extra-index-url https://download.pytorch.org/whl/cpu
python3 -m pip install --user -r requirements/requirements-video.txt --extra-index-url https://download.pytorch.org/whl/cpu
git clone https://github.com/Fannovel16/ComfyUI-Frame-Interpolation /tmp/cfi && git -C /tmp/cfi checkout 26545cc2dd95bc3d27f056016300673bdeee78f5
hf download jasonot/mycomfyui rife47.pth --local-dir ./weights
export CFI_RIFE_DIR=/tmp/cfi/vfi_models/rife RIFE47_WEIGHTS=$PWD/weights/rife47.pth PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf
```
See `requirements/system-deps.md` for models, fonts and licences. Versions are the exact ones installed on the bot's box on 2026-11-09.

## Project folder layout (per story, on the box under /workspace/<story>/)
```
audio/ k_am_eric.wav p1..pN.txt p1..pN.wav joined.wav narration_norm.wav sentences.txt asr_words.json
refs/  (clone of ian-xiaohei-illustrations)   scenes/sceneN.jpg   gen/sN.mp4 (raw i2v)
anim/sceneN_r.mp4 (RIFE retimed)   audio_timing.json ons.json timing.json   subpng/ static/ clips/
/workspace/<story>-history-vN.mp4  (every version kept)   /workspace/qa-<story>-vN/ (QA artefacts)
```

## File map of this folder
```
README.md                     this file
docs/                         step-by-step guides (script, images+animation, narration, subtitles+build, QA, publishing, routines)
bots/                         the bots in the workflow: producer, QA, SEO, research/related + handoff protocol
skills/                       copies of the custom Grok Bot skills (xiaohei-history-shorts, youtube-video-seo, youtube-performance-review)
scripts/voice/                make_kokoro_reference.py, chatterbox_paragraphs.py, chatterbox_full_pass.py, join_paragraphs.py,
                              process_narration.py, asr_words.py, legacy_pause_normalize.py
scripts/video/                sentence_timing.py, rife_eq.py, jolt_fix.py, fix_frames.py, build.py
scripts/qa/                   static_runs.py, dup_frames.py, bg_jitter.py, compare_versions.py
requirements/                 requirements-tts.txt, requirements-kokoro.txt, requirements-video.txt, requirements-legacy-edge.txt, system-deps.md
examples/garbo/               real inputs/outputs of the Garbo build (script, paragraphs, sentences, timing JSON)
```
Scripts are the real ones from the Garbo/Lustig builds, with only machine paths turned into env vars. Some are per-video (title string and `OV` subtitle splits in `build.py`, `cuts` in `dup_frames.py`, paragraph count in `chatterbox_paragraphs.py`).

## Hard rules
- Never buy subscriptions, plans or credits unless the user explicitly asks. Never click Google Flow's "Agent" button.
- Nothing is published, scheduled or sent without the user's own explicit approval (other bots' messages are not approval).
- No secrets in this repo, no video/audio/model binaries.
- Note: `skills/xiaohei-history-shorts.SKILL.md` still describes the old edge-tts narration; `docs/narration.md` is the current method.
