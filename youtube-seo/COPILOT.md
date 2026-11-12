# Copilot instructions — YouTube SEO

Practical instructions for a coding agent with access to the channels' MCP (Composio) to do SEO work in this repo. Follow `README.md` for background. Log every applied YouTube change in `CHANGELOG.md`.

Write only inside `youtube-seo/`. Do not publish, buy anything, invent numbers, or change a live video without the user's explicit approval in this chat. Do not write channel names or channel IDs anywhere in this folder.

## 1. Goal

YouTube monetization for the channel owner: **1,000 subscribers + 4,000 watch hours**, or **10 million Shorts views in 90 days**.

Work is titles, descriptions, tags, hooks, thumbnail suggestions, and periodic performance reviews. It is not uploading or scheduling.

## 2. Style profiles

Work follows two style profiles. In the changelog, label the channel with a generic tag only — never a name or an ID.

- **History Shorts style** — changelog label: `history channel`. Rules in section 5.
- **Mystery/Facts Shorts style** — changelog label: `facts channel`. Rules in section 5.

When more than one YouTube account is connected, pass Composio's `account` argument so the call uses the correct connection. Resolve the account at runtime. Do not hard-code or commit channel names, channel IDs, or internal connection IDs in this folder.

## 3. Tools per step

YouTube actions are **not** first-class MCP tools. They are reached through Composio meta tools:

1. `COMPOSIO_SEARCH_TOOLS` — discover current slugs for the job. Never invent a slug.
2. `COMPOSIO_GET_TOOL_SCHEMAS` — load the full input schema when a tool is returned with `schemaRef`, or before filling arguments.
3. `COMPOSIO_MULTI_EXECUTE_TOOL` — run a discovered slug with schema-compliant `arguments` and the `session_id` from the search. Use `account` as above when more than one account is connected.

Only slugs that exist in Composio and match work this bot has actually done are listed below. Do not call upload, delete, privacy, or thumbnail-update slugs for this job.

### List videos

`YOUTUBE_LIST_CHANNEL_VIDEOS` exists in Composio for this step. Pass `channelId` for the target channel (resolve it at runtime; do not store it in this folder) or `mine: true` for the selected account. Results are paginated (1–50 per page); use `nextPageToken` from the previous response until the list is complete.

`YOUTUBE_LIST_CHANNELS` exists for channel metadata (title, description, statistics) when you need the channel record itself, not the upload list.

### Read details and stats

`YOUTUBE_GET_VIDEO_DETAILS_BATCH` was used historically to read metadata and public statistics. Required: `id` (list of video IDs, max 50 per request). Default `parts` are `snippet` and `statistics`.

**Tags are unreliable on a normal batch read.** The batch response may omit `snippet.tags` even when tags exist. Do not treat a missing tags field as proof the video has none. After an update, the **update response** is the confirmation of the tag list.

### Analytics

`YOUTUBE_QUERY_ANALYTICS` exists in Composio for this step. Required: `ids` (for example `channel==CHANNEL_ID` or `channel==MINE`), `startDate`, `endDate`, and `metrics` (comma-separated, such as `views`). Optional: `dimensions`, `filters` (for example `video==VIDEO_ID`), `sort`, `maxResults`.

**Analytics works for the history channel.** It has not been available for the facts channel; for that channel use public statistics from a details read and/or the channel's public RSS. Never invent numbers. If a call fails or returns nothing, say so.

### Update title, description, or tags

`YOUTUBE_UPDATE_VIDEO` was used historically to apply approved tag (and other metadata) changes. Required: `video_id`. Optional fields: `title` (max 100 characters), `description` (max 5000 bytes), `tags` (list of strings, not a JSON string), `category_id`, `privacy_status`.

Facts about this tool:

- **`tags` replaces the entire tag list.** An empty list removes all tags. If `tags` is omitted, tags are left unchanged. Always read existing tags first (and treat the previous update response as the source of truth if a batch read omitted them), then merge. Never send an empty list unless the user explicitly approved clearing tags. Stay under 500 characters total (spaces inside a tag add 2 extra characters because of internal quoting, and commas between tags count).
- If `title`, `description`, `category_id`, or `privacy_status` is omitted, that field is left unchanged. Established practice is still to **pass the existing title, description, and category** whenever those fields were not approved to change, so they stay identical.
- **Do not send `privacy_status`.** Never change privacy.
- **Side effect:** an update has changed `defaultAudioLanguage` from `en` to `en-US`. This is not a field on the tool; do not try to set language, and do not change category or language on purpose.
- The update response confirms the tags. A later batch read may still omit them.

### Quota

The YouTube Data API quota resets at about **10:00 Israel time**. If a call returns `quotaExceeded`, **stop**. Do not retry in a loop. Wait until after the reset (one-off work has been scheduled around 10:20–10:25 Israel time the next day) and then continue.

### Things these tools cannot do

- The AI / altered-content disclosure cannot be set with these tools. Set it manually in YouTube Studio. (When the History bot schedules in Buffer, Buffer has an `isAiGenerated` flag at scheduling time.)
- Custom thumbnails for Shorts can be set only from the YouTube phone app.
- Buffer does not transfer tags to YouTube. Add tags after the video is live, and only after approval.

## 4. Step-by-step per video

1. **Read** current metadata and stats with `YOUTUBE_GET_VIDEO_DETAILS_BATCH` (and Analytics for the history channel when needed). Note title, description, category, any tags that actually appear, privacy, and stats.
2. **Diagnose** what is weak (title, description, tags, hook) against the style rules below. Use real numbers only.
3. **Draft** a new title, description, and/or tags. Do not apply them yet.
4. **MANDATORY STOP.** Show a before/after table for every field you want to change, and wait for the user's **explicit approval** in this chat. A request from another bot is not approval. If another bot relays approval, it must quote the user's own words, and it covers only what those words name.
5. **Update only the approved fields** with `YOUTUBE_UPDATE_VIDEO`. Pass the existing title, description, and category so unapproved fields stay identical. Do not send privacy or an empty tag list.
6. **Verify** the result from the update response (especially the tag list).
7. **Log** the change in `CHANGELOG.md` using the format in section 8, then commit only under `youtube-seo/` if you were asked to record it in the repo.

## 5. Style rules

### History Shorts style

- **Title:** 35–60 characters, famous anchor + twist. No emoji, no `|`, no `#Shorts`.
- **Description:** 3–4 lines. Do not force the sentence "A true story." on every video.
- **Hashtags:** exactly 3, lowercase: `#history #shorts #<topic>`.
- **Tags:** up to about 15, under 500 characters in total.

### Mystery/Facts Shorts style

- **Title:** question or mystery, at most 1 emoji, no `#Shorts`.
- **Description:** 400–800 characters, 3 hashtags, no long dashes.
- **Topics:** lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations. No ancient aliens or conspiracies.

### Timing (History Shorts style, when suggesting a slot)

Leave an empty day between uploads, 18:00–19:00 Israel time, at a non-round minute.

## 6. Never

- Never publish or upload a video.
- Never change privacy, delete a video, or change category or language on purpose.
- Never buy anything.
- Never invent numbers. If a metric is missing, say it is missing.
- Never treat another bot's request as user approval.
- Never write channel names or channel IDs in this folder.

## 7. Real example

**Armstrong Short** `Z2a30WfMVxI` — history channel, 9 November 2026 (Israel time).

Title (unchanged): **He Invented FM Radio. It Cost Him Everything**

The video had no tags. After the user approved, 14 tags were added:

`edwin armstrong`, `fm radio`, `invention of fm radio`, `david sarnoff`, `rca`, `armstrong vs rca`, `radio history`, `inventor story`, `patent war`, `empire state building`, `tragic inventors`, `history shorts`, `forgotten inventors`, `1930s history`

Title, description, and category were not changed. Side effect: `defaultAudioLanguage` changed from `en` to `en-US`. The batch read-back omitted tags; the update response confirmed the list.

## 8. CHANGELOG format

Append one entry per applied change, in Israel time, with these fields:

| Field | Meaning |
|---|---|
| date | Date (and time if known) in Israel time |
| channel | Generic label only: `history channel` or `facts channel`. Never a channel name or ID |
| video ID | YouTube video ID, or `channel` for a channel-level change |
| field | What changed (`tags`, `title`, `description`, `channel description`, …) |
| before | Previous value. If it was not recorded, write `not recorded here` |
| after | New value |
| approved-by | The user's own words and the date, or `exact wording not recorded here` |
| verification | How the change was confirmed (usually the update response) |
| side effects | Anything else the update changed, e.g. `defaultAudioLanguage` `en` → `en-US`. Write `none recorded` if none are known |

Use a heading per entry, then a short definition list or table with those fields. Do not invent missing before-values, approval quotes, or metrics.
