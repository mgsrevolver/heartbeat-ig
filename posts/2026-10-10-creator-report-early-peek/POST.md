# IG carousel post: Creator Economy Report early peek

Clay's 7-slide cut (2026-10-10), from slides 1-5, 8 and 12 of the full set. Images: `slide-01.jpg` to `slide-07.jpg` (1080×1350 JPEG, 4:5, all under 300 KB). Account: @join.heartbeat. **POSTED 2026-10-10 by Clay's go via Windsor, media id 17912751375542982.**

| # | Slide |
|---|---|
| 1 | Cover: "We asked community builders 27 questions." |
| 2 | 6 in 10 have an audience under 5,000 |
| 3 | Word of mouth & email lists bring in nearly 2x the members of all social combined |
| 4 | 2 in 3 run it solo, 56% under 5 hrs/week |
| 5 | 73% expect revenue to grow, 0 expect it to shrink |
| 6 | 3 in 4 want to run on fewer tools |
| 7 | CTA: report coming + survey open until Oct 16 for Heartbeat admins |

## Caption

```
We're surveying community builders for our first Creator Economy Report, & the early answers are already good 👀

A few that stopped us:
→ 6 in 10 have an audience under 5,000
→ word of mouth beats every social platform for new members
→ 2 in 3 run their community completely solo
→ 3 in 4 want to run it all on fewer tools
→ & not one person expects revenue to shrink next year

Full report drops soon. Follow along so you don't miss it 💛

Run a community on Heartbeat? Check your inbox. The survey's open until Oct 16 🧡

#communitybuilding #creatoreconomy #onlinecommunity #membershipsite #communitymanager
```

## Posting via Windsor

- Account: connector `instagram`, account `17841480374143685` (join.heartbeat), connected 2026-10-10.
- Images: marketing-site PR #137 (https://github.com/heartbeat-chat/heartbeat-marketing-site/pull/137) hosts them at `https://www.heartbeat.chat/images/social/creator-report-2026-teaser/slide-01.jpg` to `slide-07.jpg`. Live only after merge + deploy. curl each one for a 200 `image/jpeg` before posting.
- Call: `execute_action(connector="instagram", account="17841480374143685", action="create_carousel_post", params={image_urls:[...7 in order], caption:<above>})`. This **publishes immediately**. Run it only on Clay's explicit "post it".

## Scheduled follow-ups (approved by Clay 2026-10-10, local scheduled tasks via Windsor)

| When (ET) | Task | Asset | Hosted by |
|---|---|---|---|
| Sat 10/10 8pm | `ig-post-reel-guess-the-stat` | `reels/reel-a-guess-the-stat.mp4` (24s) | PR #138 |
| Sun 10/11 noon | `ig-post-quote-carousel` | `reels/quote-carousel/slide-01..07.jpg` | PR #138 |
| Sun 10/11 8pm | `ig-post-reel-typical-builder` | `reels/reel-b-typical-builder.mp4` (17s) | PR #138 |

Each task checks its URLs return 200 before posting and skips if they don't. Tasks live in ~/.claude/scheduled-tasks/ and only run while the Claude app is open. Build: `python3 build_reels.py`.
