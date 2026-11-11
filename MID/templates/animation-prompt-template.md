# תבניות פרומפטים להנפשת תמונות (Animation Prompt Templates)

> תבניות עבודה מוכנות להנפשת תמונות סטילס (Image-to-Video) ב-Midjourney, מבוססות על הניסיון והתוצאות מתהליך העבודה של תמונת החתול.

---

## 1. נוסחת הזהב להנפשת תמונה (Core Prompt Formula)

```text
[תנועות מיקרו של הדמות/הנושא] + [אלמנטים דינמיים בסביבה/רקע] + [אלמנטים סטטיים מעוגנים] + [תנועת מצלמה עדינה] + [מילות איכות ותנועה טבעית]
```

### למה הנוסחה הזו עובדת?
1. **מונעת עיוותים (Morphing):** התמקדות במיקרו-תנועות (כגון מצמוץ, תנועת אוזניים, נשימה) מונעת מהמודל לנסות לייצר תנועות גוף רחבות שמעוותות איברים או אנטומיה.
2. **מעגנת אובייקטים (Static Anchoring):** ציון מפורש שרכיב מסוים נשאר יציב (לדוגמה `car remains completely still`) מונע מהרכב להתעוות, לזוז או לשנות צורה.
3. **שומרת על תאורה ופיזיקה אמינה:** תנועת השתקפויות או רוח קלה מייצרת תחושת חיים מיידית בלי לשבור את הפריים.

---

## 2. התבנית המלאה באנגלית

```text
The [subject] [subtle micro-movement: softly blinks / gently twitches ears / slow subtle breathing / subtle tail swish], [secondary movement], [environmental subtle motion: gentle breeze moving leaves/hair / soft light shift / ambient dust particles], [anchored static elements: e.g. background/vehicle/table remains completely still], [camera motion: cinematic slow push-in / subtle slow drift], photorealistic, ultra realistic, seamless natural motion
```

---

## 3. דוגמאות ממוקדות לפי סוג נושא

### דוגמה א': בעלי חיים (כמו בפרויקט החתול)
```text
The cat softly blinks and gently twitches its ears, subtle slow tail swish, gentle autumn breeze moving leaves slightly on the pavement, warm sunset reflections subtly shifting on the car surface, car remains completely still, cinematic slow push-in, ultra realistic, seamless natural motion
```

### דוגמה ב': דמות אנושית (פורטרט)
```text
The person softly blinks and takes a slow subtle breath, slight natural head movement, soft strand of hair gently sways in a light breeze, warm candlelight flickering softly on the face, background remains perfectly steady, cinematic slow push-in, photorealistic, natural seamless motion
```

### דוגמה ג': כלי רכב או אובייקט עם סביבה חיה
```text
The car stays parked and completely still, headlights gently glow with subtle atmospheric haze, rain droplets slowly sliding down the windshield, puddles on asphalt rippling slightly from falling raindrops, locked-off shot with subtle cinematic slow zoom, photorealistic
```

### דוגמה ד': נוף או פנים מבנה
```text
Gentle atmospheric haze drifting across the room, sunlight rays slowly shifting angle on the wooden floor, dust motes softly floating in the light beam, curtains swaying gently by an open window, perfectly still room architecture, smooth slow camera push-in
```

---

## 4. מילות מפתח מומלצות לתנועת מצלמה

| פקודה | תיאור | השפעה |
|---|---|---|
| `cinematic slow push-in` | התקרבות איטית ומיוצבת לכיוון הנושא | מוסיף דרמטיות בלי לייצר רעידות |
| `subtle slow drift` | תנועה מרחפת איטית מאוד | טבעי ואורגני לסצנות רגועות |
| `locked-off camera` | מצלמה על חצובה ללא תזוזה | מצוין כשהדגש הוא רק על תנועות בתוך הפריים |
| `slow tilt-up / tilt-down` | הטיה קלה מעלה או מטה | חושף הדרגתיות של פרטים בגובה (9:16) |

---

## 5. דגשים ופרמטרים טכניים ב-Midjourney
- Midjourney Web מוסיף אוטומטית פרמטרים של וידאו בעת שליחה:
  - יחס ממדים תואם למקור (עבור 9:16 נוצר `--ar 171:256`).
  - משך קליפ סטנדרטי: `--duration 5.2s`.
- אין צורך להקליד מילים כגון `fast`, `crazy explosion`, `running away` – תנועות מהירות גורמות לגליצ'ים ועיוותים קשים באלגוריתמי וידאו נוכחיים.
