---
applyTo: "MID/**"
---

# הוראות Copilot לעבודה בתיקיית MID

כשעובדים בתיקייה `MID/` או על קבצים מתוכה, יש לפעול לפי מסמכי התיקייה. שיח עם המשתמש בעברית; פרומפטים ופרמטרים באנגלית.

יש לקרוא תחילה:

1. סקירה וכללי ברזל: [`MID/README.md`](../../MID/README.md)
2. הוראות הסוכנים: [`MID/bots/README.md`](../../MID/bots/README.md), [`MID/bots/copilot-midjourney-producer.md`](../../MID/bots/copilot-midjourney-producer.md), [`MID/bots/copilot-midjourney-qa.md`](../../MID/bots/copilot-midjourney-qa.md)
3. מדריכים תפעוליים: [`MID/docs/`](../../MID/docs/) (כולל `workflow-step-by-step.md`, `animation-prompting-guide.md`, `post-production.md`)
4. תבניות פרומפט: [`MID/templates/`](../../MID/templates/)

כללי יסוד:

- מצלמה נעולה (`locked-off camera`). אין `push-in`, `zoom`, `dolly` או `move closer`.
- לייק רק אחרי אישור מפורש של המשתמש לאותו קליפ.
- ברירת מחדל: Start Frame בלבד, Loop כבוי, Motion Low.
- לקחים ושאלות מריצות ספציפיות נשמרים ב-[`MID/RUN-LOG.md`](../../MID/RUN-LOG.md), לא בהוראות הקבועות.
