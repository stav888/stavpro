# Story-to-Animation Production Workflow

This document describes the repeatable process for producing short illustrated story videos. It is intentionally project- and scene-neutral: every new story part must be built from that part's own source material.

## 1. Intake and preparation

1. Collect the complete script, intended audience, language, target duration, aspect ratio, visual references, and any platform or model requirements.
2. Break the script into ordered parts. For each part, keep its source narration, intended title, visual beat, and factual or sensitivity notes together.
3. Validate factual claims when the story is historical or documentary. Separate confirmed facts from theories and unknowns.
4. Translate or adapt text only as requested. Preserve approved wording exactly across all assets for that part.

## 2. Build each part independently

For each part, derive its title, caption, opening image, ending image, and animation prompt from that part's script and visual description. Do not carry over story details, actions, scenery, text, or prompts from another part. Reuse only global project settings that the user has approved, such as illustration style, character design, palette, aspect ratio, and text placement.

If requirements are missing or ambiguous, ask before making a consequential creative choice. Keep continuity between the two frames within the same part; do not force continuity with a different story beat.

## 3. Create and review the still images

1. Produce two 9:16 keyframes per part: an opening frame and a target ending frame. Use supplied references only for the visual traits they are intended to establish.
2. Keep the title and caption in consistent fixed positions. Use the same approved text in both frames.
3. Show both images to the user for review. If either image fails to generate, retry; if it misses a requirement, correct that frame and review it again.
4. Do not upload images to the video tool until the user approves the images and animation prompt.
5. Store approved files with consistent names, such as `images/part-XX-opening.png` and `images/part-XX-ending.png`.

## 4. Write the animation prompt

Create one English prompt per part describing only the movement from that part's opening frame to its ending frame. Include pacing, camera motion, duration, and relevant continuity constraints. Do not use another part's scene description as a prompt source.

For any visible text, include a preservation instruction: keep the exact title and caption static, sharp, readable, and unchanged throughout; do not move, animate, morph, blur, fade, cover, or distort the text.

Show the prompt to the user together with the images. Wait for approval before continuing to the video tool.

## 5. Prepare the video in Grok Imagine

After approval:

1. Open Grok Imagine and select **Video** mode.
2. Upload that part's opening image and set its role to **First frame**.
3. Upload that part's ending image and set its role to **Last frame**. Confirm the timeline order is opening → video → ending; do not leave either keyframe as **Reference**.
4. Enter the approved animation prompt. Use Grok's **Enhance prompt** action when requested, then review the resulting text for accidental changes to the story, titles, captions, or text-preservation requirements.
5. Set and verify the user's requested generation options. The current project defaults are audio on, 480p, 10 seconds, and 9:16; if the user requests different settings for a part, use those instead.
6. Confirm both frame roles, audio state, resolution, duration, aspect ratio, and prompt. Stop before submitting unless the user has explicitly approved video generation.

## 6. Quality control and file management

- Check spelling, exact approved text, visual consistency, frame order, and requested dimensions before upload.
- Verify that the animation prompt matches the current part and protects all on-screen text.
- Save source text, approved images, final prompt, generation settings, outputs, and retry notes under the project folder.
- Keep project-wide defaults separate from part-specific content so new parts can be processed without inheriting old scene details.
- If the requested image or video model is not selectable in the available tool, state that clearly; do not claim a model was used unless verified.

## Reusable animation prompt structure

```text
Animate smoothly from this part's opening image to its ending image in [approved style]. [Describe this part's action and environmental movement]. Keep [continuity details from this part] consistent. Use [pacing and camera behavior], with no [unwanted transitions or effects]. Duration: [requested duration].

Text preservation — important: Keep the exact title “[PART TITLE]” and caption “[PART CAPTION]” static, sharp, readable, and unchanged throughout. Treat them as fixed overlays: do not move, animate, morph, blur, fade, cover, or distort the text.
```
