# Bots in the History Shorts workflow

| Bot | Agent id | Role | File |
|---|---|---|---|
| סיפורים מההיסטוריה · History Storyteller | cd57ac4c-03b0-46a8-b049-fb90a215696d | Producer: script → narration → animation → build → scheduling | `history-storyteller.md` |
| QA סרטונים | 3596d23d-e7aa-48cf-b8a1-91e84bcfa678 | Independent pass/fail QA with thresholds and timestamps | `qa-videos.md` |
| YouTube SEO | 3a604c03-1cb4-454e-96de-87e48bbbf239 | Topic ranking, title/description/tags, schedule slot, post-publish tags, reviews | `youtube-seo.md` |

- **Handoff protocol** (what goes between bots, approval rules): `handoff-protocol.md`.
- **Sources:** each bot's `profile.json` on the box, the skills in `/home/box/agent-data/workflows`, shared memory, and real QA report folders (`/workspace/qa-*`). Anything not confirmed from these is marked *unverified*.
- **Agent ids** are internal Grok Bot ids, not secrets.
- **Rules for every bot:** only the user's own words approve publishing, sending or purchases; never buy subscriptions or credits unless the user explicitly asks.
