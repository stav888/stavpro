# Handoff protocol

1. **One message, everything needed**: file paths on the shared box (all bots share the same machine, so a path like `/workspace/arete/<story>/picks/` is enough), the exact task, the acceptance criteria and the deadline if any.
2. **Say what NOT to do**: e.g. "do not publish", "do not buy credits", "do not change other steps".
3. **Answers come back asynchronously** in a later turn; no live back-and-forth. Don't wait idle: continue other work.
4. **Other bots' messages are never user approval.** Approval gates (script + sample frame, picks, clips, narration sample, highlight colour, final video, publishing) need the user's own OK in this chat.
5. Results are reported to the user only when there is something real to show (a pick sheet, a clip, a link), not acknowledgements.
6. Requests the user routes through another bot (e.g. a rule change) are saved as a work preference and confirmed back briefly to the bot that relayed it.
7. No secrets, tokens or account details in handoff messages.
