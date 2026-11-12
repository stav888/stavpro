# תבניות פרומפטים להנפשת תמונות (Animation Prompt Templates)

> תבניות עבודה מוכנות להנפשת תמונות סטילס (Image-to-Video) ב-Midjourney, מבוססות על הניסיון והתוצאות מתהליך העבודה של תמונת החתול.

---

## 1. נוסחת הזהב להנפשת תמונה (Core Prompt Formula)

```text
[תנועות מיקרו של הדמות/הנושא] + [אלמנטים דינמיים בסביבה/רקע] + [אלמנטים סטטיים מעוגנים] + [מצלמה נעולה (`locked-off camera`)] + [מילות איכות ותנועה טבעית]
```

### למה הנוסחה הזו עובדת?
1. **מונעת עיוותים (Morphing):** התמקדות במיקרו-תנועות (כגון מצמוץ, תנועת אוזניים, נשימה) מונעת מהמודל לנסות לייצר תנועות גוף רחבות שמעוותות איברים או אנטומיה.
2. **מעגנת אובייקטים (Static Anchoring):** ציון מפורש שרכיב מסוים נשאר יציב (לדוגמה `car remains completely still`) מונע מהרכב להתעוות, לזוז או לשנות צורה.
3. **שומרת על תאורה ופיזיקה אמינה:** תנועת השתקפויות או רוח קלה מייצרת תחושת חיים מיידית בלי לשבור את הפריים.

---

## 2. התבנית המלאה באנגלית

```text
The [subject] [subtle micro-movement: softly blinks / gently twitches ears / slow subtle breathing / subtle tail swish], [secondary movement], [environmental subtle motion: gentle breeze moving leaves/hair / soft light shift / ambient dust particles], [anchored static elements: e.g. background/vehicle/table remains completely still], [locked-off camera], photorealistic, ultra realistic, seamless natural motion
```

---

## 3. דוגמאות ממוקדות לפי סוג נושא

### דוגמה א': בעלי חיים (כמו בפרויקט החתול)
```text
The cat softly blinks and gently twitches its ears, subtle slow tail swish, gentle autumn breeze moving leaves slightly on the pavement, warm sunset reflections subtly shifting on the car surface, car remains completely still, locked-off camera, ultra realistic, seamless natural motion
```

### דוגמה ב': דמות אנושית (פורטרט)
```text
The person softly blinks and takes a slow subtle breath, slight natural head movement, soft strand of hair gently sways in a light breeze, warm candlelight flickering softly on the face, background remains perfectly steady, locked-off camera, photorealistic, natural seamless motion
```

### דוגמה ג': כלי רכב או אובייקט עם סביבה חיה
```text
The car stays parked and completely still, headlights gently glow with subtle atmospheric haze, rain droplets slowly sliding down the windshield, puddles on asphalt rippling slightly from falling raindrops, locked-off camera, photorealistic
```

### דוגמה ד': נוף או פנים מבנה
```text
Gentle atmospheric haze drifting across the room, sunlight rays slowly shifting angle on the wooden floor, dust motes softly floating in the light beam, curtains swaying gently by an open window, perfectly still room architecture, locked-off camera
```

---

## 4. מילות מפתח למצלמה

| פקודה | תיאור | שימוש |
|---|---|---|
| `locked-off camera` | מצלמה על חצובה ללא תזוזה | **ברירת המחדל המחייבת** — הדגש הוא על תנועה בתוך הפריים בלבד |
| `push-in` / `zoom` / `dolly` / `move closer` | התקרבות או זום | **אסורים** לפי המדיניות הקבועה. אין לבחור גם וריאציה שנראית מוגדלת |
| `subtle slow drift` / `tilt-up` / `tilt-down` | תנועת מצלמה אחרת | רק אם המשתמש ביקש זאת במפורש |

---

## 5. דגשים ופרמטרים טכניים ב-Midjourney
- Midjourney Web מוסיף אוטומטית פרמטרים של וידאו בעת שליחה:
  - יחס ממדים תואם למקור (עבור 9:16 נוצר `--ar 171:256`).
  - משך קליפ סטנדרטי: `--duration 5.2s`.
- אין צורך להקליד מילים כגון `fast`, `crazy explosion`, `running away` – תנועות מהירות גורמות לגליצ'ים ועיוותים קשים באלגוריתמי וידאו נוכחיים.

---

## 6. תבנית עבודה עם תסריט שלם (Script-to-Video Workflow)

כאשר מוגש תסריט מלא לסרטון או סדרה:
1. **חלוקה לסצנות/שוטים בודדים:** לפרק את התסריט למקטעים של 5 שניות (שוט בודד לכל מקטע).
2. **ניסוח פרומפט הנפשה ייעודי לכל מקטע:**
   - זיהוי הנושא והמיקרו-תנועה של אותה סצנה.
   - התאמת הדינמיקה הסביבתית ותנועת המצלמה המתאימה להתפתחות העלילתית.
   - שמירה על עקביות של הדמויות והאלמנטים המעוגנים לאורך כל חלקי התסריט.
3. **הצגת הפרומפטים באופן ממוספר וסדור:** המשתמש מקבל רשימה ישירה של פרומפטים להרצה שלב-אחר-שלב.
4. **תמונות לכל קטע:** לכל סצנה מכינים תמונת פתיח (Start Frame) בלבד, אלא אם המשתמש ביקש במפורש גם תמונת סיום. התמונות נוצרות ב-GPT כברירת מחדל.
5. **3 אופציות פרומפט לכל קטע:** לפני הרצת כל ג'וב מציעים למשתמש 3 אופציות פרומפט, והמשתמש בוחר אחת מהן.
6. **בחירת לייק לכל קטע:** מריצים את הג'וב, עושים QA לווריאציות (ללא גליצ'ים, עיוותים או זום), ממליצים על וריאציה, ומסמנים לייק רק אחרי שהמשתמש אישר במפורש את אותו קליפ. רק אז עוברים לקטע הבא.
7. **איחוד הקטעים:** Midjourney אינו מאחד סצנות. הקליפים שאושרו מורדים ומאוחדים לרצף אחד לפי [`../docs/post-production.md`](../docs/post-production.md).
