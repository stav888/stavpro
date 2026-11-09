# 7. Routines (scheduled follow-ups)

Pattern used for every scheduled Short (Grok Bot "routines" skill):
1. **Post-publication cleanup routine** – one-shot, set for shortly after `dueAt` (e.g. +30–60 min):
   - Check via Buffer that the post status is `sent` and get the YouTube URL/ID.
   - If sent: `git rm` the MP4 in `stav888/video-hosting/history-storyteller/<project>/`, add `.gitkeep`, commit `cleanup: remove <project> after Buffer publish`, push (no force). If not sent: do not delete, report to the user.
   - Tell the SEO bot the video ID so it can add tags and track performance.
2. **SEO performance reviews** live in the YouTube SEO bot (every ~3 days; trial comparison expanded vs short scripts on 2026-11-24).
3. Routines never publish new content, buy anything, or change YouTube metadata without the user's approval (tag addition was approved as part of the standing SEO flow).

Note: the exact routine definitions are stored in Grok Bot's internal routine store, not as files; this page documents their behaviour.
