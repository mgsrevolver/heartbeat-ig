# Instagram playbook: @join.heartbeat

**Who we're talking to:** people who run, or want to run, a paid online community. That means coaches, consultants, educators, creators, experts and niche organisers. They want members who stay, income that grows, and less tool sprawl.

**What a good post does:** teaches or shows something concrete in the first second, makes a community builder feel seen, and makes Heartbeat look like the obvious home for their community. Get creative. Variety beats a template.

## Standing notes from Clay

Newest first. The routine adds these when Clay's reply contains a standing instruction.

- 2026-10-22: On vertical video, captions always go in the lower third (larger type) so they never cover the speaker's face(s). Attribution/lower third, the Heartbeat logo and any other overlays go in the top third. Clay may also speed clips to 1.25x and trim a trailing half-thought word.
- 2026-10-19: **Vary covers; nothing is banned.** Gradient covers are fine, and video posts don't need an image-led cover (type-led is fine). The goal is a profile grid that doesn't look samey. Before choosing slide 1, check the last 3 covers in LOG.md (Format column) and don't repeat a style; never two gradient covers in a row. Supersedes the 10/13 note below, which said the gradient was never the default and carousels open on imagery. Imagery is still a good default for carousels (photo collage, community logo grid, screenshot, phone mockup, one strong photo); example: `posts/2026-10-13-paid-community-for-that/src/slide-01.html`.
- 2026-10-16: **Never put captions, lower thirds, citations or any text over someone's face on video.** Clay hand-placed the Amy/VetCircle edit in the Riverside editor: captions at y=0.948 (bottom edge of the 9:16 frame; the `y 0.85` I used still landed mid-frame, so check the real position by reading `settings.captions.position` on the clone and don't trust the value you set), and her name / community lower third also placed away from her face. Use captions y≈0.95 as the default and verify the lower third position in the editor timeline. Supersedes the `y:0.68` hint in VIDEO.md step 6.
- 2026-10-14: **Cover quotes are neutral or positive, and clean.** The first video's cover used DeWayne's "Why are you telling all about business on social media?" Clay pulled it: a skeptical line, and the spoken grammar reads as wrong on a cover. Pick the line that states the takeaway (e.g. "Our mission is to provide information with integrity and transparency"), lightly cleaned (drop filler words, never change meaning), and open the caption on the same positive note. Questions, doubts, and garbled grammar can stay in the video, never on the cover or as the caption hook.
- 2026-10-14: **Every other day is a video day.** Alternate a Riverside clip (customer interviews, webinars, town halls; procedure in `VIDEO.md`) with a still post (carousel, rendered reel or image). Clips from the 7 /stories interviews are OK on video, **new angles only**: a point we haven't posted, never the same headline number as the hook.
- 2026-10-14: **Pause customer stories from the 7 on heartbeat.chat/stories** (applies to still posts; video clips of them are OK with a new angle, see the note above). (Emily, Kat, Allie/Level Up Ladies, etc. are exhausted). A specific case study or glow-up is OK only if it is NOT one of those 7. Find a new one and send it for review; if no public source exists, ask Clay for a lead instead of drafting.
- 2026-10-14: **Featured directory community posts are OK, with rough/rounded/directional size or numbers allowed.** Clay suggested this as the next idea after pausing customer stories.
- 2026-10-13 (superseded by 10/19 on covers): **The gradient is never the default slide 1.** A pink-to-orange gradient cover on every carousel makes the profile grid look samey. Use it as slide 1 only for data, survey or drier non-visual posts (a big number, a stat roundup, a hot take), and even then only occasionally. The gradient is fine on later slides (a stat beat, the CTA). Every other post opens on imagery: a photo collage, a grid of community logos, a screenshot, a phone mockup or one strong photo. Before choosing slide 1, check the last 3 covers in LOG.md (noted in the Format column) and don't repeat a style, and never post two gradient covers in a row. Example of an image-led cover: `posts/2026-10-13-paid-community-for-that/src/slide-01.html` (photo mosaic with niche tags, cream band with the hook).
- 2026-10-13: **Every community slide gets a picture of that community.** First-party (their logo or cover art from the directory listing) first. Otherwise a relevant royalty-free photo. Unsplash blocks bots, so search Openverse instead: `https://api.openverse.org/v1/images/?q=<terms>&license=cc0&source=stocksnap,rawpixel`. Those are CC0, so no credit is needed on-slide. Record each photo's source URL in `posts/<slug>/CREDITS.md`. Avoid photos with military or agency insignia, needles or medical procedures, readable name badges, or faces that look staged.

- 2026-10-12: **Never share low numbers. We want to appear bigger.** Lead with the biggest figure ($27M+ paid out, 37,000+ communities, 750,000+ members). Don't publish the small milestone counts (1,100+ past $1K, 400+ past $10K). For $100K earners, say "dozens of creators have earned over $100K", not "50+". Small numbers about *a creator's* starting point are fine as story ("every community starts at zero").

- 2026-10-12: **No Creator Economy Report survey content** (stats, quotes, "take the survey") until Clay says the survey is closed. Three survey posts already ran 10/10-10/11. Once he says it's closed, the published report becomes a pillar.
- 2026-10-12: Default to one post a day. Reels and carousels over single images.

## Pillars (rotate; don't repeat the last two)

| Pillar | What it looks like | Where to get it |
|---|---|---|
| **Featured community** | One community from the directory: who it's for, what makes it unusual, one detail from its listing. Carousel with their listing screenshot, or a 10s reel scrolling it. | Live listings at heartbeat.chat/directory (FACTS.md) |
| **Unusual use cases** | "You can run a paid community for *that*?" Vets, care-home managers, container garden designers, Payback-points collectors, worship singers. Roundups of 4-6 niches work well. | Directory, customer stories |
| **Customer story** | One number + one decision that got them there. Hook on the number. | heartbeat.chat/stories (FACTS.md) |
| **Feature, shown** | A real Heartbeat feature, old or new, in use: screenshot, GIF or screen recording. Explain what happens, flatly. No hype. | heartbeat.chat/features + /feature/<slug>, /branded-app, /pricing; Slack product channels (read only) for things that already launched publicly |
| **Tool demo** | Screen-record the pricing calculator answering a real question ("what should a fitness coach charge?"). | heartbeat.chat/tools/membership-pricing-calculator |
| **Proof in numbers** | Platform-scale stats framed around the creator ("50+ creators have passed $100K"). | FACTS.md only |
| **Playbook / tips** | 5-7 slide how-to from a Heartbeat guide or /for page, ending on "full guide on heartbeat.chat". | heartbeat.chat/blog, /for, /compare |
| **Creator-economy observation** | A fresh trend, stat or news item from the last ~2 weeks, plus our take for community builders. Cite the source in the email (and on-slide if it's a stat). | WebSearch / WebFetch |
| **Myth vs reality / hot take** | A belief community builders hold, and what actually happens. | Stories, guides, observations |

Format mix: half the days are Riverside video clips (see VIDEO.md). The other half: mostly carousels and rendered reels, with the odd single image. Try new formats too: "guess the number" reels, before/after, POV, tier lists, "things nobody tells you", screenshot teardowns.

## Carousel mechanics (ideas, not a rotation)

Source: a @yoursocialteam carousel (10/7) on "swipe-mechanic" carousel types. It got 9.4K likes, 12.7K shares and 10.1K comments, but most comments came from a "comment DROPS" keyword CTA, so don't credit the mechanic alone. Treat these as tricks to apply to any pillar when the content suits it. All are plain 1080x1350 HTML slides through `tools/render.py`; no animation tooling needed. Check the last 3 formats in LOG.md and don't use the same mechanic twice in a row. Slide 1 follows the cover note (vary, don't repeat).

| Mechanic | What the swipe does | How to build it | Good for |
|---|---|---|---|
| **Traveling icon** | One object (a heart, a coin, a cursor, a community avatar) slides across slide edges, so each swipe moves it along and the text lands where it stops | Lay out one wide canvas (1080 x N slides) in one HTML, then render each slide as the same canvas shifted by `-1080 * i`. Objects cross the seam on purpose | Step-by-step journeys: "from 0 members to first $1K", how a member moves from signup to paying |
| **Swipe to zoom in** | The same image or phone screenshot gets bigger each slide until one detail fills the frame | Same asset on every slide, `transform: scale()` grows per slide, final slide is the detail with a one-line caption | Feature, shown: zoom from the whole community app into the one setting or number that matters |
| **Swipe to reveal** | A photo or screenshot starts pixelated or blurred and sharpens each slide; the clear version is the last slide | Pixelate in the browser with a canvas (`imageSmoothingEnabled=false`, draw small then scale up) at 4 to 5 steps. "Hold the dots and swipe to reveal" line at the bottom | Featured community (reveal the listing), guess-the-number, "what a $X community looks like" |
| **Walking through slides** | A reusable template: intro, one fact per slide over a consistent background, a proof screenshot, a CTA slide | Fixed background photo, one line per slide, one `.shot` frame for the proof screenshot. Close on the comment-keyword CTA | Intros of our own account, featured community profiles, "who we help" |
| **Comment-keyword CTA** | Ends on "Comment WORD and we'll send you X" | Caption CTA only. Needs a DM automation behind it (SetSmart has comment-trigger tools), so propose it to Clay, don't promise a send the routine can't make | Playbook posts that map to a guide on heartbeat.chat |

Rules for these: true content first (the mechanic never replaces a real number, listing or screenshot), reveal and zoom must end on something worth the swipe, and keep the same copy rules and numbers rules as every other post.

## Sources the routine can use (cloud)

- Public site: heartbeat.chat (directory, stories, features, pricing, tools, blog, /for, /compare). Screenshot or screen-record with headless Chromium at 1080 wide or a 430px mobile viewport, device scale 2.
- Community landing/join pages linked from directory listings (public pages only, never member-only content).
- Heartbeat Help Center articles have feature screenshots and GIFs, but the site blocks bots. Try WebFetch once, and skip it if blocked.
- Slack connector, **read only**. Look for shipped features and wins, and use only what is already public. Never send or react.
- Windsor `get_data` on connector `instagram_public` / `instagram` for our own past posts' reach and engagement. Lean into what worked.
- No internal databases (HubSpot, PostHog, Stripe) in the cloud. Numbers come from FACTS.md or a cited public page.

## Brand

- Colours: cream `#FFF7F0` background, ink `#1F1418`, logo gradient `#F91E87 → #FD8467 → #FFBA54` (left to right). Night `#0A0D12` for contrast posts.
- Type: Inter (bold/extra-bold headlines, regular body) + Instrument Serif italic for the emphasis word and big numbers. Both are in `fonts/`, wired up via `{{BRAND}}`.
- Every feed slide and reel ends with the wordmark (`brand/heartbeat-wordmark-black.svg` on light, `-white` on dark/gradient). Never recreate the logo in text.
- Components in `tools/brand.css`: `.pill .big .head em .sub .card .split .list .li .quote .shot .phone .cta .foot .reel-foot`.
- Reels: 1080x1920. Keep text out of the top 220px and the bottom 340px (IG UI). Hook on screen in the first second. 7-30s. Hard cuts or 0.2s fades. Hold the payoff beat longer.
- Carousels: 3-10 slides, 1080x1350. Slide 1 is the hook and only the hook. Slide 1 is often image-led, but a gradient (`body.dark`) or type-led slide 1 is fine too; vary it (see Standing notes, 10/19). Last slide is a soft CTA (follow, save, or "heartbeat.chat").
- Screenshots go in `.shot` (rounded, shadowed) or `.phone` frames on the cream background. Crop to the interesting part. Blur or crop out member names, faces and emails unless they belong to the featured community's public listing.

## Copy rules (check every caption and slide)

1. **No em dashes.** None. Use commas or periods.
2. No "it's not X, it's Y". No "Here's the thing". No corporate filler ("unlock", "elevate", "seamless", "game-changing", "robust", "powerful").
3. Name the noun. "$27M+ paid out to creators" beats "real results". See `reference/concreteness-rule.md`.
4. Community-first framing: "build a community people will pay for". **Never** "turn your community into a business" or "monetize your audience".
5. Numbers: only from FACTS.md (rounded floors like 50+, never exact) or a public source you cite. **Never** Heartbeat's own revenue, ARR, funding or customer counts beyond FACTS.md. "37,000+ communities **created**", never "running" or "active".
6. Names: customers with a published story (FACTS.md) and communities with a live directory listing can be named. Anyone else stays anonymous. Survey/interview quotes are always unattributed. Flag every named person or community in the preview email.
7. Competitors: we can compare honestly, but never mock or name-and-shame. If a competitor is named, flag it.
8. No promises of income ("make $10K/month"). Say what real creators did, as fact.
9. Features: describe only what exists today, as it works today. Don't preannounce anything from Slack that isn't public.
10. Voice: warm, direct, a little playful. `&` is fine. Emojis in moderation, 💛 🧡 are house favourites. `→` for caption lists.

**Caption shape:** a hook line under ~125 chars (it's all that shows before "more"). Then 2-6 short lines, then one CTA ("Follow for more", "Save this for later", "Comment GUIDE and we'll send it", or "heartbeat.chat"). Then 3-6 relevant hashtags (#communitybuilding #onlinecommunity #creatoreconomy #membershipsite #coachingbusiness, plus niche tags). Max 2,200 chars.
