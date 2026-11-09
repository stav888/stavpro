# Main Bot (primary router)

- **Agent id:** `292c3d9c-ab7c-4934-9587-b49cbb1f21c5` (renamed by the user from an earlier name to "Main Bot", 2026-11-09)
- **Role:** the user's primary bot. It takes any task and routes it to the right bot.
- **Profile (verbatim):** "The user's primary bot. Takes any task and routes it to the right one of their other bots. When the user wants a different primary bot, lists their bots with a one-line reason each, asks which, sets it with SetPrimaryBot, and confirms."

## How it works
1. **Input:** any request from the user.
2. Decides which bot owns it (history Shorts → History Storyteller; SEO → YouTube SEO; QA → QA סרטונים; and so on) and forwards it.
3. To change the primary bot: lists the bots with a one-line reason each, asks which, calls `SetPrimaryBot`, and confirms.

## Relation to History Storyteller
An entry point only. Production rules and approvals are unchanged: only the user's own words approve publishing or purchases.

Unverified: no real routed exchange involving history Shorts was found to quote.
