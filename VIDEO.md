# Video days: Riverside clips

Read this only on a **video day** (see ROUTINE.md, "Which kind of day"). It covers finding a clip in Riverside, cutting it into a vertical reel, previewing it and publishing it. Everything in PLAYBOOK.md still applies: copy rules, names, numbers and standing notes.

## What Riverside has

Riverside (connector **Riverside**) holds Heartbeat's recorded video. Production `61d358850d6ea3000c2c157e`. Source studios:

| Studio | id | What's in it | Use it for |
|---|---|---|---|
| Case Study Interviews | `67844ca8958512f14a254907` | Murtaza interviewing customers. Hundreds of ready-cut "magic clips" (15-75s), e.g. Dewayne Williams (MAC Enterprise), Emily (10K Email Club), Kat Weaver, Allie (Level Up Ladies), Amy (VetCircle), un autre atelier | Customer story, myth vs reality, playbook tips |
| Heartbeat Tutorials | `67a43f052117ee1565e97985` | Monthly webinars: Misty/Mike with expert guests (email lists, onboarding, affiliates, safe spaces, FB ads, hiring a community manager) | Playbook / tips |
| Heartbeat Town Halls | `67a2a277ef1c852cfe14da0a` | Monthly product town halls: Murtaza, Mayhul, Nick, André demo features | Feature, shown |

Skip the other studios (Sample 1, Co-Marketing, live-event tests) and the "stinger" brand assets.

## Source rules (Clay, 2026-10-14)

- **The 7 /stories customers** (FACTS.md) are fine on video, **new angles only**: the clip must make a point we haven't posted (a tip, a decision, a mistake, a quote with a view in it). Never their headline number again as the hook. Check LOG.md and `videos-used.md` for what's already run.
- **Anyone else interviewed** (e.g. Natalia Rose / Claire Gerber) has no published story, so they can't be named. Skip them unless the clip works with no name, no community name and no numbers, and flag it.
- **Webinar guests** are outside experts, not customers. Name them only with the name they used on the webinar, never make customer or income claims about them, and flag every named guest.
- **Town halls**: shipped features only, as they work today. Never clip roadmap talk, "coming soon", pricing changes, internal numbers, or anything from the Q&A that names a customer.
- **Recordings are sources, not finished posts.** Watch for member names, emails, dashboards with revenue, and other people's faces on screen-shares. If the clip shows any, pick another moment.
- Never reuse a clip (same source edit + overlapping time range) that's in `videos-used.md`.

## Hard rules for Riverside

- **Never modify an existing edit or recording.** Always `editing_clone_edit` first and work only on the clone. (The magic clips are Murtaza's library.)
- **Publish only through `social_upload_create` to Instagram, only in the publish slot, only with Clay's approval in that thread** (same rule as ROUTINE.md). Never post to YouTube, TikTok, Facebook, LinkedIn or X, even if they're connected.
- Never call `social_cancel_upload`, `social_disconnect_social_account`, `social_connect_social_account`, anything under `hosting_*` (podcasts), webinar or scheduling tools, `editing_set_brand`, or `media_*` deletes.
- Never request `includePreviewUrl` on a recording. That link is a studio-wide credential.
- A video post is one `upload_create` call, ever. If it errors or times out, don't retry: call `social_list_uploads` for that studio and today, and email Clay `[cortex-ig] error <slug>` if it's unclear.

## Make the clip (draft slot)

1. **Find candidates.** Cheapest first:
   - `platform_list_edits` (limit 200, page with offset) and scan titles for short magic clips (duration 15,000-75,000 ms) that fit today's idea. Or `platform_get_project(projectId)` for one interview's clips.
   - `search_riverside(searchTerm=<topic>, filters=[{entity:"TAKE", field:null, value:null}], nextSearchAfter=null)` to find a spoken moment in long recordings (webinars, town halls). It finds the recording; for a long recording, `platform_list_edits` the project to find an existing edit to clone. Use `editing_create_edit_from_recording` only if no edit exists.
   - Skip anything in `videos-used.md`.
2. **Read before you choose.** `editing_read_aligned_transcript(editId)` on the candidate (read-only). Pick a moment that stands alone: a hook in the first sentence, one idea, a payoff. 15-45s is the target; 60s max. Don't keep a question without its answer.
3. **Clone it.** `editing_clone_edit(sourceEditId, title="IG <slug>")`. Use the returned `editId` and `revision` from here on.
4. **Make it vertical.** `editing_read_timeline_in_range(editId, startTime 0, endTime ~5s)` and check `settings.canvas`. The case-study magic clips are usually 9:16 already (canvas 360x640): if so, **leave the layout alone**. Only if it's not 9:16, run `editing_batch` with `[{type:"update_aspect_ratio", params:{ratio:"9:16"}}]`, then `editing_apply_smart_layout(style:"FullScreen")`.
   **Then check who's on screen in every scene.** In the 10/14 test, FullScreen put Murtaza (the interviewer) on screen for the whole clip. Read the scenes in the timeline; for any scene showing the wrong person, `editing_batch` with `assign_track_to_tile {sceneId, tileId:"fullscreen", trackId:<featured speaker's track>}`. The featured speaker should fill the frame while they talk.
5. **Trim.** `editing_read_aligned_transcript(editId, detail:"words", startMs, endMs)` around your moment, then `editing_resolve_transcript_selection` with a `boundary_range` (first and last words) and `intent:"keep"`. When `readyToApply` is true, run `editing_cut_time_ranges` with its payload unchanged. Then `editing_remove_pauses(thresholdMs: 700)` for pace.
6. **Captions on** (most people watch muted). `editing_get_captions_presets(studioId)`: use the brand default from `brandCaptionsList` if there is one, else a bold built-in. Then `editing_set_captions(editId, presetId, studioId, show:true, style:{contentPerSegment:"lines_2"})`. Keep captions clear of the bottom 340px (IG UI), e.g. `position:{x:0.5, y:0.68}`.
7. **Name the speaker** where allowed: `editing_add_lower_third(name, title, startMs: 500, durationMs: 4000)`, e.g. "Dewayne Williams" / "MAC Enterprise".
7b. **Append the stinger (always, Clay 2026-10-14).** Every video ends on Heartbeat's 3-second CTA stinger, **at the end, never the start**. Riverside's magic clips don't actually include it: their `stinger-…` track is empty. Pick by the clip's primary brightness: **light (white) stinger** for a bright clip, **dark (black) stinger** for a dark one. You can't see frames, so judge from what you know (studio background, lighting cues in the transcript, the source project) and default to light, the brand-kit outro. Name the choice in the email's Flags: "Stinger: light. Reply 'dark stinger' to swap."
   - Vertical (9:16) files in the Riverside media library: light `6ab28675edb60e4ca8113b10` (`stinger-light-cta-1080x1920.mp4`), dark `6ab286751fc500861c4e434e` (`stinger-dark-cta-1080x1920.mp4`). The 16:9 versions (light `6ab2869ec699fbe8b0ad2c4e`, dark `6ab2869e9c6acb8c61d18a66`) are for landscape edits only. Never use the "stinger light/dark 1920x1080" *recordings*.
   - Do it **after** all trims and pause removal: `platform_get_edit` for `duration` (the playable end), then `editing_insert_media_as_scene(editId, assetId, startMs:<duration>, durationMs:3000, sceneName:"Stinger")`. Duration should grow by exactly 3000.
   - Any later trim (Clay's edits) must cut before the stinger, not through it. If you re-cut the end, check the stinger is still the last 3s.
8. **Cover.** Render a 1080x1920 cover with `tools/render.py` (hook text, brand fonts; PLAYBOOK cover rules apply). You can't grab a frame from Riverside, so for a person use their photo from their public story page or directory listing, or go type-led. JPEG under 2 MB, saved as `posts/<slug>/media/reel-cover.jpg`. Upload it to Riverside: `media_create_media_upload` → `curl -T` the file to the returned URL → `media_finalize_media_upload`. Keep the `mediaId` as `thumbnailMediaId`. If the upload fails, fall back to `thumbnailOffset` (ms of a strong frame) and say so in Flags.
9. **Check it.** `editing_read_aligned_transcript(editId)` once more: the kept text must read as a complete thought, start on the hook and end on the payoff. Fix it before sending. Also confirm nothing plays before the first spoken word (no stinger or empty scene at the start) and that `duration` = last word's `playableEndMs` + 3000 (the stinger). Then `platform_get_edit(editId)` for `riversideUrl` and `duration`.
10. Add a row to `videos-used.md`: date, slug, source edit id, source title, kept range (ms), clone edit id.

## Preview email (video)

Same as ROUTINE.md step 2.8, with:
- Subject: `IG draft: <short title> · <pillar> · Video`.
- Media block: the cover image inline, a **"Watch the cut in Riverside"** link to the clone's `riversideUrl`, the duration, and the full kept transcript in a light box (so Clay can approve from his phone without opening Riverside).
- Flags: every named person, the source recording, anything from a town hall, and "Riverside may add a watermark if the plan requires one."
- State line `format` is `"video"` and it also carries `"riverside":{"editId","studioId","thumbnailMediaId"|null,"thumbnailOffset"|null,"durationMs"}`. `files` is `[]` and `cover` is `"reel-cover.jpg"`.

**Edits from Clay** ("start at 'the first thing'", "cut the last line", "different clip") are made on the same clone (or a new clone for a different clip), then a `revised`/`ready` reply with the new transcript.

## Publish (publish slot, approved only)

1. `social_get_connected_platforms(studioId)` for the clip's studio and find the Instagram account for join.heartbeat (`username: join.heartbeat`). Riverside connects social accounts **per studio**. As of 2026-10-14 Instagram (platformAccountId `39109532062027442`) is connected in **Case Study Interviews** and **Heartbeat Town Halls**, not yet Tutorials. Publish through the clip's own studio. If the clip's studio has no Instagram, publish with the Town Halls `studioId` (`67a2a277ef1c852cfe14da0a`) and that `platformAccountId`, passing the clip's edit id as usual. If Riverside rejects that (a studio/clip mismatch error), nothing was posted: reply `[cortex-ig] error <slug>` with the exact error and "Connect Instagram in the <clip's studio> studio in Riverside, then reply approve again." Then stop.
2. Duplicate check: `social_list_uploads(studioId, productionId, from=<today 00:00 ET>, platform:"INSTAGRAM")` for the studio you're publishing through. If an upload of this editId exists, don't publish again; go to step 4 with that uploadId.
3. `social_upload_create`:
   ```
   platform: "Instagram", studioId, platformAccountId,
   clipId: <clone editId>,
   composeSettings: {quality:"1080p", normalizeGain:true, showWatermark:false},
   instagramData: {caption, shareToFeed:true, thumbnailOffset?: <ms>},
   thumbnailMediaId?: <mediaId>
   ```
   (Use exactly one of `thumbnailMediaId` or `instagramData.thumbnailOffset`.) Keep the `uploadId`. The clip renders first, which takes minutes.
4. Poll `social_get_upload_status(uploadId)` every 60s for up to 12 minutes. A bare `sleep 60` is blocked in the cloud sandbox: run `sleep 60; echo done` with `run_in_background: true` and check status when it finishes. (First live post, 10/14: a 27s clip went PENDING → COMPLETED in about 2 minutes.)
   - `COMPLETED` → reply `[cortex-ig] posted <slug>` with the uploadId, the final caption and the post link `https://www.instagram.com/reel/<externalId>/` (externalId is the shortcode).
   - `FAILED` (terminal) → reply `[cortex-ig] error <slug>` with Riverside's `reason`. Never re-publish on your own.
   - Still `PENDING` → reply `[cortex-ig] publishing <slug>` ("Rendering in Riverside; I'll confirm on the next run.") with the state line plus `"uploadId"`. The next run checks it (ROUTINE.md step 1).
5. LOG.md row: Format `Video (<n>s), source: <source title>`, link = uploadId until it's live, then the post link.
