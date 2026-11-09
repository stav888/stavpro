# YouTube SEO (titles, descriptions, tags)

**Role:** SEO and growth bot for the channel, goal: monetization. Writes titles, descriptions, tags, hashtags and hooks, suggests topics and slots, and reviews performance every few days.

## Handoff
- I send: topic, final script, video length, the hook line, and any facts that must be in the description.
- It returns: title, description, tags, hashtags, and a suggested non-round slot 14:00-19:00 Israel time.
- I check: no em/en dashes, title <= 100 chars, tags <= 500 chars total, facts match the script; save with `scripts/metadata/make_metadata.py`.
- The user approves the metadata before scheduling.

## After publishing
- Buffer sometimes drops tags; the SEO bot adds them after the user's OK.
- It runs periodic performance reviews (views, retention, CTR) and suggests title/description fixes for weak videos; changes to a live video also need the user's OK.

## Channel guidelines it helped set (approved 2026-11-02)
Topics (lost places, geographic mysteries, near-miss technology, battles, forgotten civilizations; no aliens/conspiracies), 3-4 Shorts a week, hook text in the first second, 25-40 s (length later changed to about 50 s - 1.5 min on 2026-11-09, see `../docs/production-rules.md`).
