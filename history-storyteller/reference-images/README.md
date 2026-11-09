# Reference images — what the videos look like

All images in this folder are frames/stills from **our own** finished productions (generated for this channel), downscaled to 540x960 JPG (the contact sheet and source still are wider). Total under 0.5 MB.

## Style rules these images show
- **Canvas:** 9:16, 1080x1920, pure white background, no textures, no gradients. The camera never moves: no zoom, pan or Ken Burns. Scenes change with hard cuts.
- **Line art:** thin, slightly wobbly black hand-drawn lines and lots of empty white space. Colour only as tiny accents (a red dot or dashed line, an orange bulb or flame, a soft sun glow).
- **Xiaohei:** solid-black bean-shaped character with white dot eyes, thin stick legs and a blank expression. He **performs the key action** of the sentence (holds the guidebook, writes the reports, watches the landing through binoculars, pours the water). He is never decoration. Props such as a hat or headphones may be added for the role.
- **Other people:** simple white line-drawn figures (officers, businessmen) with minimal detail. No gore: a bomb is a distant glow on the horizon (image 10).
- **Layout (from `scripts/video/build.py`):**
  - Title at top in Patrick Hand ~64 px, all caps, with a short red underline.
  - Art large in the middle band (auto-cropped to its content, up to ~1060x1150 px, centred around y≈790).
  - Subtitle at y≈1430 in Patrick Hand 52–62 px, black, max 2 lines, locked to the spoken sentence.
  - Small grey counter `— i / N —` at the bottom.
- **No text inside the generated art.** All text is added in the compose step.

## The images
| File | What it shows |
|---|---|
| `01-garbo-final-frame-scene1.jpg` | Garbo v9, scene 1/14, the hook. Xiaohei as Pujol in a hat, holding up a document in a sketched street. Title, red underline, 2-line subtitle and counter all visible. |
| `02-garbo-final-frame-scene9.jpg` | Garbo scene 9/14. Xiaohei and officer Tomás Harris at a desk under a board of imaginary agents linked by red dashed lines (the only colour). |
| `03-garbo-final-frame-scene12.jpg` | Garbo scene 12/14. Wide landscape: Xiaohei in front of a tank and troops in the Calais area. Small figures, lots of white space. |
| `04-garbo-contact-sheet-all-scenes.jpg` | Midpoint frame of all 14 Garbo scenes in story order. This is the sheet used to check that each picture matches the sentence spoken at that moment and the order is chronological. |
| `05-garbo-source-still-before-layout.jpg` | The raw generated still (1152x864 landscape) for scene 10, Normandy landing, before animation and before it is placed in the 9:16 layout. Shows what to ask the image model for. |
| `06-garbo-approval-sample-frame.jpg` | The single sample frame shown to the user with the Hebrew script for approval before full production (Pujol inventing his agent network). No title or subtitles yet. |
| `07-lustig-final-frame.jpg` | "The Man Who Sold the Eiffel Tower", scene 2/11. Xiaohei as Lustig reading a newspaper, with an orange idea bulb as the accent. |
| `08-armstrong-final-frame.jpg` | "The Man Who Invented FM", scene 4/10. A white line-drawn executive orders Xiaohei (Armstrong) out, carrying a box of equipment. |
| `09-wojtek-final-frame.jpg` | "Wojtek — The Soldier Bear", scene 4/8. Xiaohei leads the bear up the gangway to a ship. This is an older, smaller title style (before the larger title was adopted). |
| `10-yamaguchi-final-frame.jpg` | "Survived Two Atomic Bombs", scene 2/6. A sensitive moment shown respectfully: distant glow, a small figure, no graphic detail. |
| `11-stanley-meyer-final-frame.jpg` | "The Car That Ran on Water?", scene 2/10. Big close-up of Xiaohei pouring water into the "fuel cell". Shows the BIG-art framing the user asked for. |

## Original style source (linked, not copied)
The look is based on **Ian Xiaohei Illustrations** by Ian ([helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations), MIT; see its [NOTICE.md](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/NOTICE.md), which asks for attribution to Ian). Its 16:9 example images are passed as `reference_image_paths` to every image generation. Browse them in [`ian-xiaohei-illustrations/assets/examples/`](https://github.com/helloianneo/ian-xiaohei-illustrations/tree/main/ian-xiaohei-illustrations/assets/examples), for example:

![Ian Xiaohei example: minimum loop](https://raw.githubusercontent.com/helloianneo/ian-xiaohei-illustrations/main/ian-xiaohei-illustrations/assets/examples/02-minimum-loop.png)

Differences from Ian's original: we use a vertical 9:16 layout instead of 16:9, English-only text (added in compose, never in the art), history scenes instead of article metaphors, and animated one-way motion.
