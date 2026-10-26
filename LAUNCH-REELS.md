# Launch reels: Tue Oct 27 to Thu Oct 29, 2026

The "Heartbeat IG: launch reels" routine reads this file. It posts one reel a day for the Creator Economy Report launch. Clay approved these three reels and captions in Cortex on 2026-10-26 ("schedule the reels... these should temporarily override the other IG workflow"), so no preview email and no reply are needed for them. Only the posts listed here are approved. Nothing else may be published from this file.

| Date (ET) | n | Slug | Reel |
|---|---|---|---|
| Tue 2026-10-27 | 1 | `2026-10-27-report-first-member` | The first member matters most |
| Wed 2026-10-28 | 2 | `2026-10-28-report-small-communities` | Small communities, real money |
| Thu 2026-10-29 | 3 | `2026-10-29-report-live-time` | Members pay for people |

Steps:

0. Check the date and time in ET (`TZ=America/New_York date`). If today isn't in the table, or it's outside 08:45-10:59 ET, stop and do nothing.

1. Duplicate check: if LOG.md has a `posted` row for today's slug, or Gmail has a sent `[cortex-ig] posted <slug>` email, stop. Never post a reel twice. If a Windsor call errors or times out, read the account's latest media (Windsor `get_data`, connector `instagram`) before you retry.
2. Use the files already in `posts/<slug>/`: `media/reel.mp4`, `media/reel-cover.jpg` and `caption.txt`. Do **not** re-render, re-edit, recut or rewrite anything, the caption included. Use `caption.txt` exactly as written.
3. Build the URLs from the sha of the commit on `main` that contains the post (`git log -1 --format=%H origin/main -- posts/<slug>`): `https://cdn.jsdelivr.net/gh/mgsrevolver/heartbeat-ig@<sha>/posts/<slug>/media/reel.mp4` and `.../reel-cover.jpg`. Run `bash tools/check_media.sh` on both, with the usual retry rule.
4. Publish with Windsor `create_video_post {video_url, caption, cover_url, share_to_feed:true}`. Keep the media id.
5. Email Clay (`send_message`, to clay@heartbeat.chat only) with subject `IG posted: Creator Economy Report reel <n>/3`. In the body, put `[cortex-ig] posted <slug>`, the media id and a link to https://www.instagram.com/join.heartbeat/. If anything failed, use the subject `IG error: Creator Economy Report reel <n>/3` and give the reason. Do not retry later in the day.
6. Add a LOG.md row with pillar `Proof in numbers / Report launch` and format `Reel (code-rendered, ~30s), cover: report stat card`, then commit and `git push origin HEAD:main` (on rejection, `git pull --rebase origin main` and push again).

Never post more than today's one reel. Never post on any other date.

