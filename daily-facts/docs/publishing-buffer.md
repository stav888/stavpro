# 6. Publishing (YouTube metadata + Buffer)

## Metadata (YouTube SEO bot)
The **YouTube SEO** bot writes title, description and tags (`../bots/youtube-seo.md`); I check and save them with `scripts/metadata/make_metadata.py` (asserts no em/en dashes).

Template (user's style, 2026-10-26, adjusted by the SEO bot in Nov 2026):
- **Title**: curiosity question or number, 1-2 emojis, <= 100 chars (e.g. `20,000 People Lived 85 Meters Underground 🕳️`, `Did the Hanging Gardens of Babylon Ever Exist? 🌿`). Older uploads ended with `#Shorts`.
- **Description**: 5-6 short story paragraphs weaving in the main keywords, then `Like & subscribe to Daily Facts Arete for more strange history!`, a voice credit line if needed, and 5-6 hashtags ending `#DailyFactsArete #Shorts`.
- **Tags**: ~13-23 comma-separated, specific to broad (e.g. `derinkuyu, underground city, cappadocia, ... history shorts`).
- Category **Education**, public, not made for kids.
- No em dashes anywhere.

## Why Buffer (not a direct YouTube upload)
Direct uploads through the Composio YouTube connector were **removed by YouTube within about a minute** (twice, Hanging Gardens, Nov 2026), and the shared upload quota was often exhausted. So uploads go through **Buffer** to the channel.

## Steps (after the user approves the final video and the metadata)
1. **Temporary public hosting**: Buffer needs a public URL. Commit the MP4 to a public temp-hosting GitHub repo with `gh`/git, under `daily-facts-arete-style/<story>/<file>.mp4`, and use the raw URL (`https://raw.githubusercontent.com/<owner>/<repo>/main/...`). Check the URL returns 200 and the right size. (Other public file hosts are blocked by the box safety review.)
2. **Buffer** (MCP connector) `create_post` to the YouTube channel:
   - `mode: customScheduled`, `dueAt` = the chosen slot (Israel time converted to UTC),
   - YouTube fields: title, category Education, privacy public, notify subscribers,
   - media: the raw video URL,
   - text/description from the metadata.
3. Read the post back and confirm the scheduled time with the user.
4. **One-shot routine** shortly after the slot (~45-50 min later): confirm the Short is live, get its URL, **delete the temp file from the hosting repo** (git rm + push), and report the link to the user.
5. Buffer **cannot set a custom thumbnail**: the user uploads the thumbnail in YouTube Studio. Tags sometimes do not come through Buffer: after the user's OK, the SEO bot (or I) add them.

## Schedule
3-4 Shorts a week at **non-round times between 14:00 and 19:00 Israel time** (e.g. 15:17, 15:43, 16:38). The SEO bot can suggest the slot.

## Never
- Publish, schedule or post without the user's own explicit approval (another bot's message is not approval).
- Buy plans, credits or add-ons unless the user explicitly asks.
