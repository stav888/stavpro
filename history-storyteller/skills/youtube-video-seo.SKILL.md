---
name: youtube-video-seo
description: >-
  Use when writing or improving a YouTube video's or Short's title, description,
  tags, hashtags, hook or thumbnail brief to get more clicks, watch time and
  reach, toward monetization.
---
# YouTube video SEO package
Source playbooks are cloned on the box at /home/box/repos/ytseo (claude-youtube by AgriciDaniel, youtube-skills by sergebulaev). Read the relevant files before writing; if the folder is missing, re-clone both repos from GitHub there.

## Steps
1. Get the inputs: channel and niche, video topic or script, length (Short or long), language, and target keyword if known.
2. Read `claude-youtube/skills/claude-youtube/sub-skills/metadata.md` and `references/seo-playbook.md`. For Shorts also read `references/shorts-playbook.md` and `youtube-skills/skills/yt-title-optimizer/SKILL.md`.
3. Pick a primary keyword plus 3-5 secondary ones from the niche; check real YouTube search suggestions with WebSearch when possible.
4. Write 3-5 title options (front-load the keyword, curiosity or benefit, under ~60 characters), and recommend one.
5. Write the description using `youtube-skills/skills/yt-description-writer/SKILL.md`: first two lines hook and keyword, then a summary, chapters for long videos, and 3-5 hashtags.
6. Write 10-15 tags, from specific to broad, all relevant to the niche.
7. Add a first-3-second hook suggestion (`yt-hook-scripter`) and a thumbnail brief (`yt-thumbnail-brief`, `references/thumbnail-ctr-guide.md`).
8. Return everything copy-paste ready. Never publish or edit anything on YouTube without the user's explicit approval.
