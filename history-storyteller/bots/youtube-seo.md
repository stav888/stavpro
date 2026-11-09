# YouTube SEO

- **Agent id:** `3a604c03-1cb4-454e-96de-87e48bbbf239`
- **Role (for History Storyteller):** SEO and growth for **Smart History Knowledge**, aiming at YouTube monetization (1,000 subscribers + 4,000 watch hours, or 10M Shorts views in 90 days).
- **Profile rules that apply here (from its profile):**
  - For every video: a click-worthy title, a keyword-rich description, niche tags, hook and thumbnail suggestions.
  - A performance check every 3 days.
  - Never publish or change anything on YouTube without explicit approval; never buy anything.
  - Inspiration sources: AgriciDaniel/claude-youtube and sergebulaev/youtube-skills.

## Inputs
- **From the producer:**
  - Topic candidates with sources.
  - The final English script, topic and length.
  - The date and time of the last scheduled post.
  - After publish: the YouTube video ID, and whether it's an expanded-trial video.
- **From YouTube or YouTube Analytics:** real view, CTR and retention data, for reviews only.

## Step by step
1. **Topic ranking:** judges search demand (evergreen vs seasonal), hook strength, and fit with the channel's best performers. Recommends which story to make now and which to hold for its season.
2. **Metadata**, using the `youtube-video-seo` skill and the playbooks in `/home/box/repos/ytseo`:
   - Primary keyword + 3–5 secondary ones; checks real YouTube search suggestions when possible.
   - **Title:** 3–5 options, keyword first, curiosity twist, under ~60 characters; recommends one. Channel pattern: *"He Did X. Then Y"* (e.g. "He Invented FM Radio. It Cost Him Everything").
   - **Description:** first two lines are hook + keyword, then a 2–4 line summary, then 3 hashtags (always `#history #shorts` + one topic tag).
   - **Tags:** 10–15, specific → broad (e.g. Garbo: juan pujol garcia … world war 2).
   - Plus a first-3-seconds hook suggestion and a thumbnail brief.
3. **Scheduling slot:**
   - Max one video per channel per day, 1–2 days after the previous one.
   - Evening Israel time at non-round minutes (examples: 18:43, 18:47, 18:52).
   - Seasonal topics are held for their wave (Christmas Truce → 18–23 Dec, suggested 22 Dec 18:37).
4. **After publish:**
   - Adds the tags through the **YouTube API** (Buffer can't set tags).
   - May correct `defaultAudioLanguage` to `en-US`. Armstrong had 0 tags, got 14, and its language changed from en to en-US.
   - These two edits are part of the standing flow the user set. Any other YouTube change needs explicit approval.
5. **Performance review, every ~3 days** (`youtube-performance-review` skill):
   - Last ~30 days: views, impressions CTR, average view duration / % viewed, subscribers gained.
   - Compared with the channel median.
   - Low CTR → title/thumbnail fixes. Low retention → hook or structure changes for the next videos.
   - Reports progress toward monetization. Proposes changes only.
6. **Trial review on 2026-11-24:** expanded scripts (Garbo onward, with 3–7 days of data) vs the earlier short scripts. If expanded performs worse, the producer goes back to short scripts.

## Tools, connectors, skills
- **Skills:** `youtube-video-seo`, `youtube-performance-review`.
- **Repos:** [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube) and [sergebulaev/youtube-skills](https://github.com/sergebulaev/youtube-skills), cloned at `/home/box/repos/ytseo`.
- **Data and writes:** a YouTube / YouTube Analytics connection for data and tag writes. The exact connector isn't recorded in its profile (unverified). WebSearch for keyword checks.

## Outputs
A Hebrew message with:
- the recommendation and its reasons;
- title options plus the pick, the description, hashtags and tags (copy-paste ready);
- the slot in Israel time;
- for reviews: a per-video table, flagged videos with fixes, and monetization progress.

## Rules
- Never publish or change anything on YouTube without the user's explicit approval (except the standing post-publish tag and language step).
- Never buy anything. Never invent numbers: if there's no data connection, it says so.

## Real example (paraphrased, 2026-11-09)
- **Producer → SEO:** "The user is choosing between the Emu War and the Christmas Truce. Which one, when, and with what working title?"
- **SEO → producer:**
  - Emu War now: it's searched all year and has an absurd hook ("an army with machine guns vs birds, and the birds won").
  - Christmas Truce in December, when searches jump in the two weeks before Christmas.
  - Slots: Emu War Sat 14 Nov 18:52, Christmas Truce Tue 22 Dec 18:37.
  - Working titles: "Australia Declared War on Emus. The Emus Won" / "In 1914, Enemies Stopped the War for Christmas".
  - Expanded-vs-short review booked for 24 Nov; asked to be sent the IDs of the expanded videos.
- **Producer → user:** the same recommendation in Hebrew. It also corrected the bird name: the SEO bot had written "יענים" (ostriches), but the story is about emus.
