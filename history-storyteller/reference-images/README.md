# Reference images — what the videos look like

All 38 images in this folder are frames from **13 of our own finished history Shorts** (12 videos with 3 frames each plus 2 from Garbo). Each video has a hook/early frame, a middle action frame and an ending/late frame, so the style can be compared across stories. **Every file is vertical 9:16 at 540×960 JPG** taken from the final MP4s — never 16:9 / landscape. Total about 1.4 MB. File names follow `<video>-NN-<role>.jpg`.

**For new sketches (Step 0):** always build start/end frames **according to** these references (pick 2–3 per scene, match the look, check side by side). Sketches must be vertical 9:16, **illustration only** (`no text, no letters, no captions`), with large Xiaohei filling most of the width — not a small centred vignette. Compose the approval sample with `preview_frame.py`; never ask the generator to draw the title/underline/caption.

## Style rules these images show
- **Canvas:** **vertical 9:16 only** (final Shorts 1080×1920; these refs 540×960), pure white background, no textures, no gradients. Never 16:9. The camera never moves: no zoom, pan or Ken Burns. Scenes change with hard cuts.
- **Line art:** thin, slightly wobbly black hand-drawn lines and lots of empty white space. Colour only as tiny accents (a red dot or dashed line, an orange bulb or flame, a soft sun glow).
- **Xiaohei:** solid-black bean-shaped character with white dot eyes, thin stick legs and a blank expression. He **performs the key action** of the sentence (holds the guidebook, writes the reports, watches the landing through binoculars, pours the water). He is never decoration. Props such as a hat or headphones may be added for the role.
- **Other people:** simple white line-drawn figures (officers, businessmen) with minimal detail. No gore: a bomb is a distant glow on the horizon (`yamaguchi-01-early.jpg`).
- **Layout (from `../scripts/video/build.py`) — see Frame layout below:**
  - Title English UPPERCASE at `(540,115)` in Patrick Hand 64, red underline x=400–680 (280 px, 6 px) at y=165.
  - Art large in the middle band (auto-cropped to content, up to 1060×1150, centred around y≈790, between y=200–1400).
  - English subtitle at y=1430 in Patrick Hand 62 (fallback 56/52), max 2 lines, 960 px, locked to speech.
  - Grey counter `— i / N —` at y=1835 (32 px).
- **No text inside the generated art.** All on-screen text is English and is added in the compose step (`build.py` / `preview_frame.py`).

## Frame layout (mandatory)

**All on-screen text in the video is English only** (title, subtitles, page counter). Never put Hebrew or any other language on the frame.

Generated stills and clips (sketches **and** video) contain the **illustration only**:
- **No title, no underline, no caption, no page counter, no letters of any kind.**
- Every image/video prompt must say: `no text, no letters, no captions`.
- Any lettering baked into a still or clip is a **reject** — regenerate it. Text is added afterwards by [`../scripts/video/build.py`](../scripts/video/build.py) (or [`../scripts/video/preview_frame.py`](../scripts/video/preview_frame.py) for the approval sample).

**Drawing size (fill the screen):**
- Make the scene fill nearly the whole **width** of the image. The Xiaohei character must be large and clearly doing the action — not a small vignette centred in the middle.
- `build.py` crops each clip to the drawing's bounding box (pixels darker than 200, plus a 14 px margin) and scales it to fit a **1060×1150** box, centred at about **y=790** and kept between **y=200** and **y=1400** of the 1080×1920 frame. A wide, well-filled drawing therefore ends up filling most of the screen; a small centred drawing stays small.

**Overlay layout on the 1080×1920 canvas** (Patrick Hand, `PatrickHand-Regular.ttf`, env `PATRICK_HAND_TTF`):

| Element | Spec |
|---|---|
| Title | English, **UPPERCASE**, 64 px, colour `(20,20,20)`, centred at `(540,115)` |
| Red underline | from **x=400 to x=680** (280 px ≈ 26% of width), **6 px** thick, at **y=165**, colour `(225,55,40)` |
| Subtitles | English, **62 px** (fallback 56 then 52 only if a line won't fit), max line width **960 px**, max **2 lines**, line spacing **70 px**, first line top at **y=1430**, colour `(12,12,12)`, centred |
| Page counter | `— i / N —`, 32 px, grey `(130,130,130)`, at **y=1835** |

At the 540×960 preview / reference size these are half: title 32 px, underline 140 px long and 3 px thick at y≈82, subtitles 31 px.

**Sample-frame approval:** build the approval sample by compositing the generated illustration with these overlays (`build.py`'s static overlay plus one subtitle chunk), **never** by asking the image generator to draw text. Helper: [`../scripts/video/preview_frame.py`](../scripts/video/preview_frame.py):

```bash
PATRICK_HAND_TTF=/path/PatrickHand-Regular.ttf \
  python ../scripts/video/preview_frame.py scenes/scene1.jpg \
    --title "THE ENGLISH TITLE" \
    --subtitle "One English subtitle chunk." \
    --i 1 --n 14 -o sample_frame.png
```

## The images
| File | Video | What it shows |
|---|---|---|
| `garbo-01-hook.jpg` | Agent Garbo — The Spy Who Invented Spies (final v9, expanded script) | scene 1/14. Xiaohei as Pujol, in a hat, holds up a document in a sketched street (hook). |
| `garbo-02-middle.jpg` | Garbo | scene 7/14 middle action: Germans study a map of an imaginary spy ring (left) while Xiaohei alone writes the reports under a lamp (right). |
| `lustig-01-early.jpg` | The Man Who Sold the Eiffel Tower (v8) | "He forged official stationery": Xiaohei in a bowler hat stamps papers. |
| `lustig-02-middle.jpg` | Lustig | "He hinted that he was a corrupt official": a whisper across a café table to a dealer. |
| `lustig-03-ending.jpg` | Lustig | "he was too embarrassed to go to the police": the victim holds his face by an empty doorway. |
| `armstrong-01-hook.jpg` | The Man Who Invented FM (v3) | "a radio signal free of static": Xiaohei with a glowing tube radio and sound waves. |
| `armstrong-02-middle.jpg` | Armstrong | "he had Armstrong's equipment removed": an angry executive points and Xiaohei carries out a box. |
| `armstrong-03-ending.jpg` | Armstrong | "in the end she won or settled every case": Xiaohei holds up a sealed document among many radios. |
| `wojtek-01-hook.jpg` | Wojtek — The Soldier Bear (v6) | "In Iran in 1942, Polish soldiers found an orphaned brown bear cub": Xiaohei in a helmet with a tiny cub. |
| `wojtek-02-middle.jpg` | Wojtek | "the army officially enlisted him as a soldier": Xiaohei leads the bear up a gangway to a ship. |
| `wojtek-03-middle.jpg` | Wojtek | "Private Wojtek got a service number, a pay book…": the bear reads his pay book next to Xiaohei. |
| `yamaguchi-01-early.jpg` | Survived Two Atomic Bombs (v2) | "…in Hiroshima, when the first atomic bomb fell": a distant glow on the horizon and a small figure, shown respectfully with no graphic detail. |
| `yamaguchi-02-middle.jpg` | Yamaguchi | "The next morning, bandaged, he took a train home — to Nagasaki": Xiaohei in bandages at a train window. |
| `yamaguchi-03-ending.jpg` | Yamaguchi | "He lived to the age of 93": an old Xiaohei with a cane by a tree; a quiet ending. |
| `stanley-meyer-01-hook.jpg` | The Car That Ran on Water? (v2) | "named Stanley Meyer built a small dune buggy": Xiaohei in a garage with the buggy and water jugs. |
| `stanley-meyer-02-middle.jpg` | Stanley Meyer | "In 1996, expert witnesses examined his fuel cell for an Ohio court": two experts watch Xiaohei. |
| `stanley-meyer-03-ending.jpg` | Stanley Meyer | "Still, to this day, some people believe his…": Xiaohei puzzled beside the covered buggy. |
| `tesla-01-hook.jpg` | Tesla's Lost Tower (v3) | "a giant tower on Long Island, New York": a small Xiaohei working under Wardenclyffe tower. |
| `tesla-02-middle.jpg` | Tesla | "It was paid for by J.P. Morgan": a top-hatted Morgan hands Xiaohei a money bag. |
| `tesla-03-ending.jpg` | Tesla | "Tesla's tower never powered the world": Xiaohei with a model in a puddle beneath the faded tower. |
| `flexible-glass-01-hook.jpg` | The Glass That Couldn't Break (v3) | "a glassmaker came to the palace of the Roman emperor Tiberius": a small Xiaohei on palace steps before the emperor. |
| `flexible-glass-02-middle.jpg` | Flexible glass | "The glassmaker took out a small hammer": Xiaohei hammers a dented glass bowl on an anvil. |
| `flexible-glass-03-ending.jpg` | Flexible glass | "To this day, no one knows if this glass ever really existed": scholars around a candle-lit table. |
| `first-airplane-01-early.jpg` | The First Airplane (Sketch 2 v6, first channel video) | "But bicycles taught them the secret: an unstable machine": Xiaohei riding a bicycle. |
| `first-airplane-02-middle.jpg` | First airplane | "Only after control worked did they add a light [engine]": two Xiaoheis fit an engine. |
| `first-airplane-03-late.jpg` | First airplane | "…metres — shorter than a modern passenger jet": Xiaohei watching the Wright Flyer in the air. |
| `curie-01-early.jpg` | Marie Curie — The Glow of Radium (v2) | "She heard of mysterious rays coming from uranium…": Xiaohei leaning over a glowing sample. |
| `curie-02-middle.jpg` | Curie | "In 1903, Marie became the first woman ever to win a Nobel Prize": a medal handed to Xiaohei on a podium. |
| `curie-03-ending.jpg` | Curie | "The glow she loved harmed her…": Xiaohei over a glowing chest of notebooks. |
| `violet-jessop-01-hook.jpg` | Miss Unsinkable 1911–1916 (v3) | "the Olympic, the largest ship in the world": a tiny Xiaohei on the deck of a huge liner. |
| `violet-jessop-02-middle.jpg` | Violet Jessop | "sent into lifeboat sixteen with a baby in her arms": Xiaohei in a lifeboat with the sinking ship behind. |
| `violet-jessop-03-ending.jpg` | Violet Jessop | "people called her Miss Unsinkable": Xiaohei at a ship's rail with a life ring. |
| `wilma-rudolph-01-hook.jpg` | The Fastest Woman 1940–1960 (v5) | "In 1940, in a small Tennessee town, Wilma Rudolph was born": a row of Xiaohei siblings, red sun accent. |
| `wilma-rudolph-02-middle.jpg` | Wilma Rudolph | "until at twelve, she took it [the brace] off and played basketball": orange ball as the only colour. |
| `wilma-rudolph-03-late.jpg` | Wilma Rudolph | "In 1960, in Rome, she won three gold medals": Xiaohei with medals in front of the Colosseum. |
| `molasses-01-hook.jpg` | The Great Molasses Flood — 1919 (v1) | "On a bright winter day in 1919, a giant tank stood over Boston's harbor": Xiaohei under the tank. |
| `molasses-02-middle.jpg` | Molasses flood | "A brown wave twenty-five feet high raced through the…": Xiaohei runs from the brown wave (brown is the scene's one colour). |
| `molasses-03-ending.jpg` | Molasses flood | "And for decades, on hot days, the streets still smelled sweet": Xiaohei in a hot street, orange sun. |

**Per-video count:** Garbo 2; Lustig, Armstrong, Wojtek, Yamaguchi, Stanley Meyer, Tesla, Flexible glass, First airplane, Marie Curie, Violet Jessop, Wilma Rudolph and Molasses 3 each.

Note: the first airplane, Wojtek, Yamaguchi, Curie, Violet, Wilma and Molasses videos use the older small title style. Newer videos (Lustig, Armstrong, Meyer, Tesla, Flexible glass, Garbo) use the larger all-caps title with a red underline, which is the current standard.

## Original style source (linked, not copied)
The look is based on **Ian Xiaohei Illustrations** by Ian ([helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations), MIT; see its [NOTICE.md](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/NOTICE.md), which asks for attribution to Ian). Its 16:9 example images are passed as `reference_image_paths` to every image generation. Browse them in [`ian-xiaohei-illustrations/assets/examples/`](https://github.com/helloianneo/ian-xiaohei-illustrations/tree/main/ian-xiaohei-illustrations/assets/examples), for example:

![Ian Xiaohei example: minimum loop](https://raw.githubusercontent.com/helloianneo/ian-xiaohei-illustrations/main/ian-xiaohei-illustrations/assets/examples/02-minimum-loop.png)

Differences from Ian's original: we use a vertical 9:16 layout instead of 16:9, English-only text (added in compose, never in the art), history scenes instead of article metaphors, and animated one-way motion.
