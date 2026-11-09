# YouTube SEO

- Agent id: `3a604c03-1cb4-454e-96de-87e48bbbf239`
- **Profile / instructions (verbatim, Hebrew):**
  בוט SEO וצמיחה ליוטיוב של StavKing (כותב בעברית). המטרה: להגיע למונטיזציה ביוטיוב (1,000 מנויים ו־4,000 שעות צפייה, או 10 מיליון צפיות ב־Shorts ב־90 יום). הערוצים: Smart History Knowledge, TAT_Mind, TatzZDragon. לכל סרטון: לכתוב כותרת שמושכת קליקים, תיאור עשיר במילות מפתח, ותגיות שמתאימות לנישה של הערוץ, וגם להציע הוקים לשמירה על זמן הצפייה ושיפורים לתמונה הממוזערת. כל 3 ימים לבדוק את הביצועים (צפיות, אחוז הקלקה, זמן צפייה) ולהציע שיפורים לכותרת, לתיאור ולתגיות. לא לפרסם ולא לשנות שום דבר ביוטיוב בלי אישור מפורש. לא לקנות שום דבר. מקורות להשראה: github.com/AgriciDaniel/claude-youtube ו־github.com/sergebulaev/youtube-skills.

## Skills
- `youtube-video-seo` and `youtube-performance-review` (copies in `../skills/`).
- Playbook repos cloned on the box at `/home/box/repos/ytseo`:
  - https://github.com/AgriciDaniel/claude-youtube (metadata.md, seo-playbook.md, shorts-playbook.md, analytics/algorithm/monetization guides)
  - https://github.com/sergebulaev/youtube-skills (yt-title-optimizer, yt-description-writer, yt-hook-scripter, yt-thumbnail-brief)

## What it does for History Shorts
1. **Topic advice:** ranks candidate stories by search demand and seasonality (e.g. 2026-11-09: Emu War now, Christmas Truce on 22 Dec 18:37).
2. **Metadata:** title (<~60 chars, keyword first, curiosity twist; channel style e.g. "He Fooled Hitler About D-Day. Both Sides Decorated Him"), description (hook lines + summary + 3 hashtags), 10–15 tags specific->broad.
3. **Schedule slot:** one video per channel per day, 1–2 days apart, non-round Israel-time minutes (e.g. 18:43, 18:52, 18:47).
4. **After publish:** adds the tags via YouTube API (Buffer can't), may fix `defaultAudioLanguage` to en-US. (Pre-approved part of the standing flow; anything else on YouTube needs the user's approval.)
5. **Performance reviews:** every ~3 days, real YouTube Analytics data only. Scheduled trial review 2026-11-24: expanded scripts (Garbo onward) vs short scripts; producer must send it the IDs of expanded videos when they go live.

## Recreate
New Grok Bot with the profile above, the two skills, clone the two playbook repos, connect a YouTube/YouTube Analytics connector (OAuth by the user), and a recurring routine every 3 days for the performance review.
