# Copilot Execution Playbook: Midjourney Animation

> ספר תרגולות ופקודות טכניות עבור Copilot ב-VS Code לביצוע אוטונומי של תהליך ההנפשה ב-Midjourney Web.

---

## 1. כלי הדפדפן הנדרשים (Tool Registry)

Copilot נעזר בסט כלי הדפדפן המשולב של VS Code:

| כלי | ייעוד בתהליך ההנפשה | דוגמת שימוש |
|---|---|---|
| `openBrowserPage` | ניווט לעמוד Imagine ב-Midjourney | `openBrowserPage(url: "https://www.midjourney.com/imagine")` |
| `clickElement` | לחיצה על כפתורי הוספת תמונה, מעבר לווידאו, לייק | `clickElement(selector: "button[aria-label='Add images']")` |
| `typeInPage` | הזנת פרומפט ההנפשה בשורת הפקודה | `typeInPage(text: "The cat softly blinks...", submit: true)` |
| `hoverElement` | הפעלת תצוגה מקדימה סימולטנית לכל 4 הסרטונים | `hoverElement(selector: ".prompt-subtext-area")` |
| `screenshotPage` | וידוא ויזואלי של מצב הגריד והתוצאות | `screenshotPage()` |

---

## 2. תרחיש הפעלה מלא לדוגמה (Scripted Scenario)

### א. פתיחת הממשק ווידוא סשן
```typescript
// 1. ניווט לממשק היצירה
await openBrowserPage({ url: "https://www.midjourney.com/imagine" });

// 2. וידוא שורת הפקודה פעילה
// אם קיים דף פתוח קיים ברשימת ה-attachments (לדוגמה: a1e875f5-...), ניתן להשתמש בו ישירות.
```

### ב. העלאת קובץ הסטילס ומעבר למצב וידאו
```typescript
// 1. לחיצה על כפתור צירוף תמונה
await clickElement({ selector: "button[aria-label='Add images']" });

// 2. העלאת קובץ התמונה המקומי
// בחירת הקובץ מתוך תיקיית הפרויקט או נתיב התמונה המבוקשת

// 3. לחיצה על מתג המעבר לווידאו
await clickElement({ selector: "button:has-text('Switch to video'), button[aria-label*='video']" });
```

### ג. הזנת הפרומפט והרצה
```typescript
const promptText = "The cat softly blinks and gently twitches its ears, subtle slow tail swish, gentle autumn breeze moving leaves slightly on the pavement, warm sunset reflections subtly shifting on the car surface, car remains completely still, cinematic slow push-in, ultra realistic, seamless natural motion";

await typeInPage({
  text: promptText,
  pressEnter: true
});
```

### ד. הפעלת תצוגה מקדימה (The Hover Playback Trick)
```typescript
// ריחוף ישירות מתחת לשורת הפרומפט
await hoverElement({
  selector: "div[class*='prompt-details'] + div, .image-grid-header"
});
```

### ה. סימון לייק על הווריאציה הזוכה
```typescript
// לחיצה על אייקון הלב באריח מס' 3 (אינדקס 2)
await clickElement({
  selector: ".grid-item:nth-child(3) button[aria-label*='Like'], button[aria-label='Like video (L)']"
});
```

---

## 3. פתרון בעיות נפוצות (Troubleshooting)

### בעיה 1: הדפדפן אינו מגיב או שדף חיצוני נפתח
- **גורם:** ניסיון להפעיל פקודות PowerShell שפתחו כרום חיצוני בלתי נשלט.
- **פתרון:** סגור את הפקודה החיצונית וחזור להשתמש אך ורק בכלי הדפדפן הפנימי של VS Code המחובר לסשן.

### בעיה 2: הווריאציות מציגות עיוותים אנטומיים
- **גורם:** הפרומפט הכיל מילות פעולה דינמיות מדי (כגון `running`, `jumping`, `turning around`).
- **פתרון:** חזור למיקרו-תנועות בלבד (`softly blinks`, `subtle ear twitch`, `slow tail swish`) ועגן עצמים קבועים (`remains completely still`).

### בעיה 3: הסרטונים אינם מתנגנים במקביל
- **גורם:** סמן העכבר הוצב מחוץ לאזור שמתחת לפרומפט.
- **פתרון:** מקם את העכבר ישירות בין טקסט הפרומפט לבין שורת האריחים הראשונה.
