# Bots in the History Shorts workflow

| Bot | Agent id | Role | File |
|---|---|---|---|
| סיפורים מההיסטוריה · History Storyteller | cd57ac4c-03b0-46a8-b049-fb90a215696d | Producer (this bot) | `history-storyteller.md` |
| QA סרטונים | 3596d23d-e7aa-48cf-b8a1-91e84bcfa678 | Independent video QA before delivery | `qa-videos.md` |
| YouTube SEO | 3a604c03-1cb4-454e-96de-87e48bbbf239 | Titles/descriptions/tags, schedule slot, tags after publish, performance reviews | `youtube-seo.md` |
| Research (subagents) + related bots | – | Topic research; sibling video bots sharing infra | `research-and-related-bots.md` |

Handoff protocol between them: `handoff-protocol.md`.
Agent ids are internal Grok Bot ids (not secrets); they are how bots address each other with SendToAgent.
