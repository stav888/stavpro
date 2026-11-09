# 6. Hosting, Buffer scheduling, after publish

Nothing is scheduled or published without the user's explicit approval in their own words.

## 1. SEO + time from the YouTube SEO bot
Send it the final script, topic, length and the date of the last scheduled video. It returns title, description (hook lines + summary + 3 hashtags e.g. `#history #shorts #ww2`), 10–15 tags, and the exact publish slot. Rules: max one video per channel per day, 1–2 days apart, odd non-round minutes (e.g. 18:43, 18:52), Israel time.

## 2. Host the MP4 (public repo)
Repo: https://github.com/stav888/video-hosting (public). Layout: one folder per bot, one subfolder per project, e.g. `history-storyteller/garbo/garbo.mp4`.
```bash
gh repo clone stav888/video-hosting && cd video-hosting
mkdir -p history-storyteller/<project> && cp /workspace/<final>.mp4 history-storyteller/<project>/<project>.mp4
git add . && git commit -m "Add <story> history Short (vN)" && git push
SHA=$(git rev-parse HEAD)
URL=https://raw.githubusercontent.com/stav888/video-hosting/$SHA/history-storyteller/<project>/<project>.mp4
curl -sI "$URL" | head -1            # must be 200
curl -sL "$URL" | sha256sum          # must equal local sha256
```
Always use the **commit-pinned** raw URL (not `main`), so later cleanup commits can't break a pending post.

## 3. Buffer `create_post` (Buffer MCP connector)
Channel: Smart History Knowledge (YouTube). Fields used:
- `text` = description; `assets` = video URL above; `dueAt` = SEO slot in UTC (`2026-11-12T16:43Z` = 18:43 Israel).
- `metadata.youtube`: `title`, `categoryId: "27"` (Education), `privacy: "public"`, `madeForKids: false`, `isAiGenerated: true`.
- Buffer cannot set YouTube tags. The SEO bot adds tags through the YouTube API after the video is live.
- The YouTube "altered or synthetic content" label must also be confirmed manually by the user in YouTube Studio.
Verify the post status is `scheduled` and report the time to the user in Israel time.

## 4. After publish
- SEO bot: adds tags (and `defaultAudioLanguage` en-US), logs the video ID for performance reviews.
- Delete the MP4 from video-hosting with a commit `cleanup: remove <project> after Buffer publish`, keep the folder with a `.gitkeep`. Never force-push.
- Example (Armstrong): published 2026-11-08 18:52 Israel, hosted file removed in commit b2c21f5.
