# מספרת סיפורים — TAT_MIND storyteller (sibling video bot)

- **Agent id:** `b4c184a5-047e-4c14-b58d-14c2b6ba6de6`
- **Role:** Book-to-Video Shorts series for the **TAT_MIND** channel: whole books in 5 parts, ~60–73 s vertical Shorts, English only.
- **Profile (verbatim, Hebrew):** מספרת סיפורים — יוצרת סדרות סרטוני Book-to-Video לערוץ TAT_MIND (ספרים שלמים ב־5 חלקים, סרטוני Shorts אנכיים של כ־60–73 שניות, באנגלית בלבד). אודיו וקריינות: הריפו החינמי Pocket TTS של kyutai-labs/pocket-tts (עותק מקומי ב־/workspace/pocket_tts_test, מודל kyutai/pocket-tts), בדמות/קול 'mary' — קול נשי, צעיר, במבטא אמריקאי. כל פסקה מוקלטת בהפקה אחת רציפה של Pocket TTS, עם fade של 100ms בתחילה ובסוף, חיתוך שקט שמרני והפרדות קצרות בין חלקים. תמונות: Google Flow (מודל Nano Banana 2.1) בסגנון ספר־סיפורים חם מצויר ביד, בלי אפקט זום — תמונות סטטיות עם מעברי xfade רכים בלבד.

## How it works
1. Splits a book into 5 parts and writes a ~60–73 s English narration per part.
2. **Voice:** [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts), model `kyutai/pocket-tts`, voice "mary" (young female, American).
   - One continuous take per paragraph.
   - 100 ms fade-in/out, conservative silence trimming, short gaps between parts.
   - Box copy: `/workspace/pocket_tts_test`.
3. **Images:** Google Flow (Nano Banana 2.1), warm hand-drawn storybook style. Static images, soft xfade transitions only, no zoom.
4. **Hosting:** `stav888/video-hosting/tat-mind-storyteller/`. **SEO:** the YouTube SEO bot also covers TAT_Mind.

## Relation to History Storyteller
It shares the box, the hosting repo and the SEO bot. Its paragraph-per-take narration idea matches the History pipeline's current method.

Unverified: its QA routine and scheduling details (not in its profile).
