# Bots in the Daily Facts Arete workflow

| Bot | Role | Gets from me | Gives back |
|---|---|---|---|
| **Daily Facts Arete** (this bot) | producer: topic, script, Krea stills, narration, edit, publishing via Buffer | - | - |
| [QA סרטונים](qa-videos.md) | quality gate for images, clips, narration, highlight colour and final video | files + what to check | pass / picks / fix list |
| [YouTube SEO](youtube-seo.md) | titles, descriptions, tags, hooks, slots, performance reviews | final video summary + script | metadata + suggested slot |
| [פעולות](actions.md) | runs heavy browser/desktop jobs: Flow clips, downloads, assembly helpers | picks + motion prompts + exact settings | clips / files + logs |
| [Main Bot](main-bot.md) | router: passes the user's requests and other bots' messages to the right bot | - | relayed requests |

How handoffs work: [handoff-protocol.md](handoff-protocol.md).
