# 7. Routines

Only **one-shot** routines are used for this channel; nothing runs on a fixed recurring schedule. Every routine is created only after the user approved the step it automates.

| Routine | When it fires | What it does | Ends with |
|---|---|---|---|
| **Flow clips after credit refresh** | the next time the Flow daily free credits are refreshed (when a run stopped because credits ran out) | runs the missing clips (`scripts/flow/run_clips.sh` skips finished ones), rotating between all existing profiles to use their daily free credits, downloads into `clips/`, checks 9:16 | a message with the clips (or the error) for QA and the user; no editing is started without approval |
| **Post-publish cleanup** | ~45-50 min after the Buffer slot | checks the Short is live on the channel, deletes the temp MP4 from the public temp-hosting repo, reminds about thumbnail + tags | the YouTube link to the user |

Rules:
- A routine never buys credits, never publishes, and never starts a new full production (since 2026-11-07 a full production needs the script + one sample frame approved first).
- If a routine fails (no credits, Flow UI drift exit 23, upload not found) it reports and stops; it does not retry blindly.
- When a process changes, ask the user whether to update this repo, and push only after he says yes.
