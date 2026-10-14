# heartbeat-ig

Daily organic Instagram for **@join.heartbeat**, run by a Claude Code cloud routine.

1. Once a day the routine drafts one post. Days alternate: a video clip cut from Heartbeat's Riverside recordings, then a carousel, rendered reel or single image from public Heartbeat material, product news and creator-economy observations.
2. It emails Clay a preview at clay@heartbeat.chat. Subject starts with `IG draft:`.
3. Clay replies in that thread, in plain words:
   - **approve** ("post it", "yes", "go") → it posts as-is
   - **edits + approve** ("change slide 2 to X, then post") → it applies the edits and posts, no second round
   - **feedback only** ("try a different hook") → it revises and sends a new preview
   - **decline** ("skip", "no") → nothing is posted
4. Daily cadence (ET): draft at 9:00, reply check at 10:00, post at 11:00 if Clay approved by then, otherwise skip the day. It replies in the thread when the post is live. Schedule: `0 9-11 * * *` America/New_York (routines can't run more than hourly; an optional sibling routine at `30 10 * * *` adds a 10:30 check).

Nothing is ever posted without Clay's approving reply in that exact thread.

## Files

| Path | What |
|---|---|
| `ROUTINE.md` | Step-by-step procedure the routine follows every run. **The routine prompt just says "follow ROUTINE.md"**, so edit this file to change behaviour. |
| `VIDEO.md` | Video-day procedure: find, cut and publish a Riverside clip |
| `videos-used.md` | Ledger of Riverside clips already drafted |
| `PLAYBOOK.md` | Content pillars, formats, brand, copy rules, standing notes from Clay |
| `FACTS.md` | Approved numbers, publishable customer stories, public URLs |
| `LOG.md` | One row per post: date, pillar, format, status, link |
| `posts/<date>-<slug>/` | Each post: `post.json` state, `src/` HTML, `media/` JPEG/MP4 |
| `tools/` | `render.py` (HTML → JPEG), `reel.py` (scenes → MP4), `check_media.sh`, `brand.css` |
| `examples/` | Working carousel + reel templates to copy |
| `brand/`, `fonts/` | Logo files and the two brand fonts (OFL) |

## Setup (one time)

1. **Give the Claude GitHub App this repo.** github.com → Settings → Applications → Installed GitHub Apps → Claude → Configure → Repository access → add `heartbeat-ig`. That is why it was missing from the routine's repo dropdown.
2. **Make this repo public.** Instagram fetches media from a public URL, and previews embed the same URLs. Media is served through jsDelivr from this repo, which only works for public repos. Nothing secret lives here.
3. The routine needs the Gmail, Windsor.ai and Riverside connectors at claude.ai/customize/connectors, each attached to the routine. Windsor publishes stills; Riverside cuts and publishes the video-day clips (`VIDEO.md`), which needs Instagram connected inside each Riverside source studio.

Local test: `python3 tools/render.py examples/carousel/src/*.html --out /tmp/out` and `python3 tools/reel.py examples/reel/reel.json`.
