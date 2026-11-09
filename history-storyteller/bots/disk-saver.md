# Disk Saver

- **Agent id:** `2425c853-bbe7-455e-a546-c5b80c536650`
- **Role (profile, verbatim):** "Audits disk usage on Grok Bot's computer and proposes safe cleanup for approval."

## How it works
1. Measures disk usage on the shared box.
2. Proposes what is safe to delete.
3. Deletes **only after the user approves**.

## Why it matters here
The History pipeline keeps every version, e.g. `garbo-history-v1…v9.mp4`, plus raw clips, RIFE outputs and QA artefacts under `/workspace`. Before approving a cleanup, keep:
- the final MP4 of each published video,
- `audio/` (`narration_norm.wav`, `p*.wav`),
- `scenes/`, and the timing JSON files.

Raw clips, old versions and QA arrays (`*.npy`) are the usual candidates. Text artefacts are backed up in `../examples/`.

Unverified: its routine schedule (its automations folder is empty).
