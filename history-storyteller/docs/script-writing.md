# 1. Story choice and script

## Topic selection
- Topic research comes from web search plus the YouTube SEO bot (see `../bots/youtube-seo.md`). Present ~5 researched options to the user (Hebrew), each with one authoritative source link (e.g. mi5.gov.uk, nps.gov, iwm.org.uk, smithsonianmag.com, naa.gov.au). The user picks.
- Seasonal topics wait for their search wave (example: Christmas Truce -> publish 18–23 Dec; Emu War -> any time).
- Facts must be true and checkable. Sensitive topics: respectful, no gore; violence shown as a distant flash/silhouette.

## Writing rules
- Strict chronological order: hook/setup -> escalation -> payoff ending. One visual beat per 1–2 sentences, a new image every ~6–11 s.
- Everything inside the video is **English only**. Chat with the user is Hebrew.
- **Current trial (from 2026-11-09):** expanded, engaging scripts (~75–85 s, ~13–15 sentences, ~4 paragraphs). Garbo is the first trial video; the SEO bot compares expanded vs short on 2026-11-24. If results are worse, go back to short scripts (<60 s, ~90–110 words).
- Write the script as paragraphs (one paragraph = one Chatterbox take) and also as one-sentence-per-line `sentences.txt` (drives timing and subtitles). See `../examples/garbo/`.
- Never speed up speech to fit a length. Cut words instead.

## Approval gate (mandatory)
1. Send the user the script **in Hebrew** plus **one sample frame** in the final style.
2. Wait for explicit approval in the user's own words (e.g. "תכין"). A message from another bot is never approval.
3. Only then run full production (images, animation, narration). This saves usage: one ~1 min video costs roughly 8–10% of the plan.
