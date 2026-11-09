# Bots in the History Shorts workflow

| Bot | Agent id | Role | File |
|---|---|---|---|
| סיפורים מההיסטוריה · History Storyteller | cd57ac4c-03b0-46a8-b049-fb90a215696d | Producer: script → narration → animation → build → scheduling | `history-storyteller.md` |
| QA סרטונים | 3596d23d-e7aa-48cf-b8a1-91e84bcfa678 | Independent pass/fail QA with thresholds and timestamps | `qa-videos.md` |
| YouTube SEO | 3a604c03-1cb4-454e-96de-87e48bbbf239 | Topic ranking, title/description/tags, schedule slot, post-publish tags, reviews | `youtube-seo.md` |
| Daily Facts Arete Style | bd551ec7-720a-4ef7-a863-9e91cc0bf76c | Sibling Shorts bot (watercolor; Kokoro voice; gflow/Veo) | `daily-facts-arete-style.md` |
| מספרת סיפורים | b4c184a5-047e-4c14-b58d-14c2b6ba6de6 | Sibling Book-to-Video bot for TAT_MIND (Pocket TTS) | `tat-mind-storyteller.md` |
| Main Bot | 292c3d9c-ab7c-4934-9587-b49cbb1f21c5 | Primary router bot | `main-bot.md` |
| Disk Saver | 2425c853-bbe7-455e-a546-c5b80c536650 | Disk audits, cleanup only with approval | `disk-saver.md` |
| פעולות / מחקר | 5163f8f4-… / caafcb77-… | Ops notes on Flow profiles / Instagram research (not used for history) | `actions-and-research-bots.md` |

- **Handoff protocol** (what goes between bots, approval rules): `handoff-protocol.md`.
- **Sources:** each bot's `profile.json` on the box, the skills in `/home/box/agent-data/workflows`, shared memory, and real QA report folders (`/workspace/qa-*`). Anything not confirmed from these is marked *unverified*.
- **Agent ids** are internal Grok Bot ids, not secrets.
- **Rules for every bot:** only the user's own words approve publishing, sending or purchases; never buy subscriptions or credits unless the user explicitly asks.
