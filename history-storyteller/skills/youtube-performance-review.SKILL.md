---
name: youtube-performance-review
description: >-
  Use for a periodic (e.g. every 3 days) review of a YouTube channel's recent
  videos: views, CTR, watch time, retention, and suggested title, description
  and tag fixes for underperformers.
---
# YouTube performance review
Playbooks are cloned on the box at /home/box/repos/ytseo; re-clone claude-youtube (AgriciDaniel) and youtube-skills (sergebulaev) there if missing.

## Steps
1. Read `claude-youtube/skills/claude-youtube/sub-skills/analyze.md`, `references/analytics-guide.md`, `references/algorithm-guide.md` and `references/monetization-guide.md`.
2. Pull real data for videos from the last ~30 days through a connected YouTube or YouTube Analytics connector: views, impressions CTR, average view duration and percentage viewed, subscribers gained. If no connector is connected, say so and ask to connect one; never invent numbers.
3. Compare each video to the channel median. Flag videos with low CTR (fix title or thumbnail) and low retention (fix the hook or the structure for the next videos).
4. For each flagged video, write improved title, description and tags with the youtube-video-seo skill.
5. Report progress toward monetization (1,000 subscribers plus 4,000 watch hours in 12 months, or 10M Shorts views in 90 days) and the change since the last review.
6. Propose changes only; apply them on YouTube only after the user explicitly approves.
