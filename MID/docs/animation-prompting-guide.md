# מדריך ניסוח פרומפטים להנפשה (Animation Prompting Guide)

> עקרונות הנדסת פרומפטים מותאמים למנוע הווידאו של Midjourney להנפשת תמונות סטילס (Image-to-Video).

---

## 1. ההבדל בין פרומפט תמונה לפרומפט הנפשה

בפרומפט תמונה (Text-to-Image), המודל יוצר את כל הקומפוזיציה, התאורה והנושא מאפס.  
לעומת זאת, בהנפשת תמונה קיימת (Image-to-Video):
- **תמונת הסטילס היא פריים האפס (t=0):** המודל כבר רואה את הדמות, הצבעים, התאורה והרקע.
- **תפקיד הפרומפט:** לתאר **רק את וקטורי התנועה (Motion Vectors)** ואת השינוי לאורך הזמן (במהלך 5.2 שניות), ולא לתאר מחדש את המראה של האובייקט.

---

## 2. חמשת עקרונות הברזל להנפשה נקייה וללא עיוותים

### א. תנועות מיקרו במקום תנועות מאקרו (Micro-Movements)
- ❌ **לא טוב:** `cat walks towards the camera and jumps on the car`  
  *תוצאה:* עיוות אנטומי קשה, כפות רגליים נעלמות, טקסטורות נמרחות.
- ✅ **מצוין:** `cat softly blinks and gently twitches its ears, subtle slow tail swish`  
  *תוצאה:* תנועה חיה, אורגנית וטבעית לחלוטין שנשארת נאמנה לתמונה המקורית.

### ב. תנועתיות סביבתית משלימה (Environmental Motion)
הסביבה מייצרת תחושת זמן שעובר ומרחב חי בלי להעמיס על הדמות הראשית:
- עלים נעים קלות ברוח הסתיו (`gentle autumn breeze moving leaves slightly on the pavement`).
- תנודות אור והשתקפויות (`warm sunset reflections subtly shifting on the car surface`).
- עשן עדין, חלקיקי אבק או גשם קל.

### ג. עיגון סטטי (Static Anchoring)
מודלי וידאו נוטים "להזיז" גם חפצים שאמורים להיות קבועים אם לא מגדירים להם אחרת.  
ציון מפורש של אלמנטים נייחים מונע עיוותים:
- `car remains completely still`
- `background architecture stays locked`
- `table and room furniture remain perfectly steady`

### ד. תנועת מצלמה יחידה ורציפה (Single Camera Motion)
- בחר **סוג תנועת מצלמה אחד** לכל קליפ:
  - `cinematic slow push-in` (התקרבות קולנועית רציפה – המומלצת ביותר לקטעי פורטרט).
  - `subtle slow drift` (צידוד עדין מאוד).
  - `locked-off tripod shot` (מצלמה מקובעת לחלוטין ללא תנועה עצמית).
- הימנע משילוב מספר תנועות מצלמה במקביל (כגון "zoom in while rotating and panning") שגורמות לסחרחורת וטשטוש.

### ה. מילות איכות ותנועה רציפה (Quality & Motion Anchors)
- `seamless natural motion`
- `ultra realistic`
- `photorealistic`
- `fluid physics`

---

## 3. ניתוח מקרה הבוחן: החתול ליד המכונית

### תמונת המקור:
- חתול ג'ינג'י/פסים יושב ליד רכב בשעת שקיעה, תאורה זהובה על הכביש ועלי שלכת פזורים.

### הפרומפט שנוסח ויושם:
```text
The cat softly blinks and gently twitches its ears, subtle slow tail swish, gentle autumn breeze moving leaves slightly on the pavement, warm sunset reflections subtly shifting on the car surface, car remains completely still, cinematic slow push-in, ultra realistic, seamless natural motion
```

### פירוק מרכיבי הפרומפט:
1. **מיקרו-תנועות החתול:** מצמוץ רך, תנועת אוזניים קלה, נפנוף איטי ועדין בזנב.
2. **אלמנטים סביבתיים:** רוח סתיו מזיזה קלות את העלים על המדרכה, השתקפויות שקיעה חמה נעות בעדינות על גוף הרכב.
3. **עיגון סטטי:** הרכב נשאר דומם ויציב לחלוטין.
4. **תנועת מצלמה:** התקרבות קולנועית איטית (Push-in).
5. **איכות:** מציאותי במיוחד, תנועה טבעית וחלקה.

**התוצאה:** 4 סרטונים מרהיבים, כאשר וריאציה מס' 3 הפיקה תנועת זנב ואוזניים מושלמת והתקרבות נקייה לחלוטין.
