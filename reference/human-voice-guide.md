# Writing Without Sounding Like an LLM

*Distilled from the content-engine hard rules, strategy doc style guide, competitor article playbook, and Murtaza's direct writing voice. Applies to: articles, docs, emails, scripts, summaries, briefs — anything that goes to a human.*

*Last updated: May 12, 2026*

---

## Why This Exists

AI-generated writing has a fingerprint. Readers recognize it in the first two sentences and stop trusting the content. It's not about disclosure — it's about pattern recognition. LLMs default to structures that are technically correct but tonally dead: hedge-first sentences, bullet-everything formatting, fake transitions, and abstract framing that says nothing while sounding like it said something.

This guide is a checklist for stripping those patterns before they hit the page. Read it before writing. Run any draft against it before sending.

---

## Part 1: Hard Prohibitions

These patterns are always wrong. No exceptions, no edge cases.

### 1. No em dashes

Never use `—` anywhere. Not for emphasis, not for asides, not for dramatic pause. If a sentence needs an em dash to hold together, it's doing too much. Fix it.

**Instead:** Use a period. Use a comma. Use a colon. Use parentheses. Break it into two sentences.

❌ `The pricing model works — and it's why customers stay.`
✅ `The pricing model works. That's why customers stay.`

❌ `Three factors matter: timing, price, and — most importantly — trust.`
✅ `Three factors matter: timing, price, and (most importantly) trust.`

---

### 2. No "it's not X, it's Y"

The structure of negating one thing and then asserting another is formulaic and AI-coded. Just say what the thing IS.

❌ `It's not about content, it's about connection.`
✅ `Connection is what keeps members. Content is just the reason they showed up.`

❌ `The problem isn't price, it's value.`
✅ `Members leave because they stopped feeling the value — price is usually downstream of that.`

---

### 3. No AI transitional filler

These words exist to make text feel like it's building to something. It never is.

**Never use:**
- "Furthermore," "Moreover," "Additionally," "Consequently," "Subsequently"
- "It's worth noting that..." / "It's important to note that..."
- "With that in mind..." / "That being said..." / "Having said that..."
- "In conclusion..." / "In summary..." / "To summarize..."
- "As we mentioned earlier..." / "As previously stated..."
- "Moving on to..."
- "At the end of the day..."

If you need to transition between ideas, write the transition into the content itself. Show the connection; don't announce it.

❌ `Furthermore, the onboarding flow matters. It's worth noting that first impressions are critical. With that in mind, let's examine the data.`
✅ `The onboarding flow is where most churn starts. The data bears this out.`

---

### 4. No empty superlatives

These words are pure filler. They add no information and signal that the writer is performing enthusiasm rather than describing reality.

**Never use:** incredible, amazing, game-changing, revolutionary, powerful, robust, seamless, world-class, best-in-class, cutting-edge, state-of-the-art, transformative, next-level

If something is genuinely good, describe WHY it's good. Specifically.

❌ `Heartbeat's automation features are incredibly powerful.`
✅ `Heartbeat can send an email, a push notification, and a direct message from a single workflow trigger — no third-party tools required.`

---

### 5. No corporate-speak

These words mean nothing. They signal that no one with actual expertise wrote this.

**Never use:** leverage (as a verb), unlock (as a metaphor), synergy, ecosystem (unless literal), infrastructure (unless literal), streamline, optimize, utilize (use "use"), facilitate (use "help" or "let"), stakeholders (use "people" or name them specifically)

❌ `Heartbeat helps you leverage your community to unlock new revenue streams.`
✅ `Heartbeat lets you charge for courses, events, and premium channels inside the same space your members already use.`

---

### 6. No passive voice

Passive voice hides who is doing what and creates the detached, institutional tone that signals AI.

❌ `The pricing model was designed to be flexible.`
✅ `Heartbeat designed the pricing model to flex after launch.`

❌ `Members are encouraged to participate in onboarding activities.`
✅ `A good onboarding flow pulls members into their first action within 48 hours.`

If you catch yourself writing "is" or "was" + past participle, rewrite the sentence.

---

### 7. No trailer copy

AI trying to sound confident defaults to stacking short declarative sentences that each certify something as proven, real, or ready — then pivots to a dramatic "what's missing" close. The rhythm sounds like a movie trailer. It's recognizable instantly and reads as manufactured urgency.

**The tell:** Multiple short sentences in sequence, each asserting one thing is settled, building toward a one-sentence kicker that labels the whole thing.

❌
```
The product is proven. The retention data is exceptional. What we haven't cracked is efficiently 
finding more of the right people. That's the job.

The engine is there. What's missing is someone who sequences it well enough that we're capturing 
the demand we're currently leaving on the table.

The platform is proven. The customers exist. The ICP is clear. The unit economics work. The only 
thing standing between here and 10x is someone who can see the path and run it.
```

**Why it fails:** Real confidence is specific. Trailer copy is just the shape of confidence — it performs certainty without earning it. "The product is proven" says nothing. "85% retention at month six, on a $49/month product, with no churn campaign running" says something.

**The sub-patterns to kill specifically:**

- **"The X is [adjective]. The Y is [adjective]."** stacking — multiple short sentences each certifying one thing as good/real/ready
- **"What we haven't cracked is..."** / **"What's missing is..."** — the pivot that follows the stack
- **"That's the job." / "That's the gap." / "That's the mission."** — the one-sentence label that closes the trailer
- **Fragment kickers used for dramatic punch** — "High-conviction, early-stage, needs a champion." Fragments are fine occasionally; stacking them signals performance
- **"The only thing standing between here and [big number] is..."** — the hero-wanted close

✅ Write the specific thing instead of certifying the category:

❌ `The activation gap is real, and solving it is worth more than most acquisition channels combined.`
✅ `Right now, 60% of signups never make it to their first community post. Closing that gap is worth more than any paid channel we could turn on.`

❌ `None of it has been rigorously tested. That's a big surface area.`
✅ `Google Ads, Meta, affiliate, SEO — none of it has been stress-tested with real budget and real measurement. That's months of compounding work sitting untouched.`

The fix is always the same: replace the certification with the specific data or detail that would make a reader believe the certification is true.

---

### 8. No validation echoes

AI generates rapport by narrating back what the reader said or did, then labeling it as real, valid, or significant. This pattern is hollow every time it appears.

**The tell:** A short declarative sentence that affirms something the reader already knows, immediately after describing it.

❌ `You've been building this community for two years. That's real.`
❌ `That's a legitimate concern.`
❌ `That's no small thing.`
❌ `That matters.`
❌ `That's worth acknowledging.`
❌ `That's significant.`
❌ `And that's okay.`
❌ `That tracks.`
❌ `That resonates.`
❌ `You're not alone in feeling this way.`
❌ `That's completely understandable.`
❌ `That's worth unpacking.`
❌ `That's powerful.`

If something actually matters, explain WHY it matters. The explanation is the content. The label is a placeholder for content.

❌ `Churn in month one is painful. That's real. It signals something is broken earlier in the funnel.`
✅ `Churn in month one almost always means the problem started before they joined — at the sales conversation, the landing page, or the pricing.`

The rule: never write a sentence whose only job is to affirm that the previous sentence was true.

---

### 8. No staccato stacking



Short, punchy sentences have a place. Three in a row, every time you want to land a point, do not. It reads like a LinkedIn post trying to go viral.

❌
```
Community is the future.
Members crave connection.
Heartbeat delivers it.
```

✅ `Community is the future — and what members actually crave is connection, not content. Heartbeat is built for that distinction.`

(Note: that example above also uses an em dash. Rewrite it without: `Community platforms win or lose on connection, not content. That's the distinction Heartbeat was designed around.`)

Vary sentence length deliberately. Short sentences land hardest when surrounded by longer ones.

---

## Part 2: AI Opener Patterns

The first sentence is where most content reveals itself as AI. Watch for these.

**Pattern 1 — The Era/World Opening**

❌ `In today's rapidly evolving digital landscape...`
❌ `As the world becomes increasingly connected...`
❌ `In an era where community matters more than ever...`

These are the most recognizable AI openers in existence. Cut immediately. Start with something specific.

✅ `Online communities that charge membership fees are growing 3x faster than ad-supported ones.`

---

**Pattern 2 — The Rhetorical Question Hook**

❌ `What does it really mean to build a thriving community?`
❌ `Have you ever wondered why some memberships succeed while others fail?`

Rhetorical questions as openers are a cliché. They delay the actual point by a full sentence. Just state the point.

✅ `Most paid communities fail in the first six months because they mistake activity for value.`

---

**Pattern 3 — The False Complexity Setup**

❌ `Building a paid community is both an art and a science.`
❌ `Pricing your membership requires balancing multiple factors.`

"Both an art and a science" is meaningless. "Balancing multiple factors" describes everything. Open with the actual thing, not a meta-description of the thing.

✅ `Pricing your membership from gut feeling almost always produces a number that's too low.`

---

**Pattern 4 — The Throat-Clear**

❌ `Before we dive in, it's important to establish some context.`
❌ `To understand this topic, we first need to look at...`

Don't announce that you're about to explain something. Explain it.

✅ Start with the explanation.

---

## Part 3: Sentence and Paragraph Patterns

### Concreteness over abstraction

AI writes in abstractions because abstractions are always defensible. Humans write in specifics because specifics are credible.

Every time you write an abstract claim, ask: what is the specific thing I am actually describing?

❌ `Many community builders struggle with monetization.`
✅ `Most community builders underprice by 40-60% in year one.`

❌ `The platform provides a robust set of tools for managing your community.`
✅ `You can run subscriptions, courses, events, and DMs without leaving Heartbeat.`

---

### Name the thing, not the category

❌ `A successful community builder...`
✅ `Lisa, who runs a 200-person paid fitness membership...`

❌ `Many enterprise customers find...`
✅ `Teams with 10+ people find...` or name an actual customer.

---

### Don't summarize what you just said

AI ends sections by restating the opening claim. It adds length, not content.

❌ `As we've seen, pricing is a critical factor in community growth. The right price attracts the right members and sets expectations for the value they'll receive. In summary, pricing matters.`

✅ End on new information, not a recap. The last sentence of a section should point forward or land something the reader didn't know at the start of the section.

---

### Don't create false precision with lists

❌ `There are three key things you need to build a successful community.`

Unless there is a genuine reason it's three (a framework, a real taxonomy), this is a made-up number. Either name the actual things without the count, or use a framework that earns the number.

✅ `To build a community people pay for, you need a reason to join, a reason to stay, and a way to charge for it.`

---

### Vary the entry point of paragraphs

AI paragraphs almost always start with the thesis of that paragraph, then support it, then close it. Real writing varies this. Sometimes you start with a detail and build to the point. Sometimes you start with a story and then abstract it.

If every paragraph in your draft starts with a clean declarative sentence and ends with a clean declarative sentence, the structure is too consistent. Break it up.

---

## Part 4: Structural Tells

### Bullets aren't prose

AI defaults to bullets because bullets are safe — they look organized, they're easy to generate, and they avoid the hard work of showing how ideas connect.

Use bullets only for things that are actually lists: steps in a sequence, items to check off, things that are genuinely parallel and don't have a connective relationship.

If you're using bullets to describe a concept, an argument, or an analysis, write it as prose. The connective tissue between ideas is the content.

❌
```
There are several reasons communities fail:
- Lack of engagement
- Poor onboarding
- No clear value proposition
- Pricing too low
```

✅ `Most communities fail for the same reason: they confuse activity for engagement. Members show up, don't feel an immediate pull into the content or relationships, and quietly let their subscription lapse. That starts at onboarding, and pricing accelerates it — when the price is too low, members don't feel obligated to get their money's worth.`

---

### Headers aren't momentum

AI adds a header before every section, no matter how short. This creates a visual structure that signals "I organized this well" while actually breaking the reader's flow constantly.

Use headers when the reader genuinely needs a navigation point — because they might come back to this section, or because the topic genuinely shifts. Don't use a header because you're about to write another paragraph.

---

### Avoid the "balanced" framing

AI hedges by default. When asked to compare two things, AI finds merit in both and presents "the other side." This produces content that sounds thoughtful but takes no actual position.

❌ `While Circle has some advantages, Heartbeat offers a different set of features that may suit certain use cases better. Ultimately, the right choice depends on your specific needs.`

✅ `Circle is better at content organization. Heartbeat is better at running a business. If you're charging for access, Heartbeat wins because Circle's payment infrastructure was built as an afterthought.`

Take a position. Be specific about when your position doesn't apply. That's more useful and more readable than permanent balance.

---

## Part 5: Specific Words to Never Use

These words reliably signal AI authorship. Treat them as a blacklist.

| Word/Phrase | Use Instead |
|---|---|
| delve into | look at, examine, go through |
| dive into | start with, get into |
| leverage (verb) | use, apply, build on |
| unlock | enable, let you, give you access to |
| seamless | simple, smooth, in one place |
| robust | capable, detailed, complete |
| comprehensive | full, complete, thorough |
| game-changing | — (just describe the change) |
| empower | let, help, give (people) the ability to |
| utilize | use |
| facilitate | help, let, enable |
| it is important to note | — (just say the thing) |
| it is worth noting | — (just say the thing) |
| in today's world | — (just start the sentence without it) |
| moving forward | — (just continue) |
| going forward | — (same) |
| deep dive | look closely at, go deep on |
| best practices | what works, what to do |
| cutting-edge | — (describe the specific capability) |
| state-of-the-art | — (same) |
| innovative | — (describe the innovation) |
| community (as a vague concept) | the specific community you're talking about |
| users | members, customers, builders, people |

---

## Part 6: The Positive Patterns

These aren't just rules about what to avoid — they're what good writing does instead.

### Lead with the point

State the thesis in the first sentence. Don't wind up to it. The opening paragraph is the most important paragraph; don't spend it setting context.

### Show the evidence, then explain it

When you have data or a real example, lead with the concrete thing, then say what it means. Not the reverse.

✅ `Alex sold 400 seats in the first 30 days at $47/month. He hadn't posted about it publicly. The revenue came from telling 40 people personally — the 10x multiplier came from members telling other members.`

### Name the exception

Don't pretend a rule is universal when it isn't. Name the case where it doesn't apply. This increases trust in everything else you write.

✅ `This works for communities with 50+ members. Below that threshold, the automation overhead isn't worth it — just do it manually.`

### Quantify the bad news

When something doesn't work, say by how much. Vague downsides feel like hedging; specific downsides feel like honesty.

✅ `The free tier cannibalized about 12% of paid signups in the first quarter. That's the real cost of the experiment.`

### Write the implication

After evidence, say what it means for the reader. The reader is asking: "so what do I do with this?" Answer that question.

✅ `If 70% of churn happens before day 30, that's where to put the investment. Engagement campaigns for month 6 are optimizing the wrong thing.`

### Use contractions

"You're" not "you are." "It's" not "it is." "Don't" not "do not." Contractions are how people talk and how good writers write. Full forms read as formal and robotic.

### Use specifics when you mean specifics

If you mean "50% of users," write "50% of users." If you mean "most," write "most" — but only if you actually mean most and don't have a number. Fake precision (using round numbers when you don't know the real number) is worse than acknowledged uncertainty.

---

## Part 7: The Rewrite Test

Before finishing any piece of writing, read the first two sentences aloud. Ask:

1. Does this start with a generic framing, era-setting, or rhetorical question?
2. Does it contain any word from the blacklist in Part 5?
3. Is it vague where it could be specific?
4. Would a person who wrote this themselves — out of genuine expertise — actually write it this way?

If the answer to any of the first three is yes, rewrite those sentences. Everything after them depends on the reader staying past them.

---

## Part 8: Murtaza's Founder Voice (codified from his edits)

The rules above strip the AI fingerprint. This section is the positive signature: what Murtaza actually does when he rewrites founder-voice copy (maker comments, launch posts, founder emails to a wide audience). Codified June 2026 from a maker-comment rewrite where his final differed sharply from the "clean" draft.

### 1. Open with the concrete origin story, not an abstract thesis

He grounds the reader in the literal, true reason the thing exists before any philosophy. The real story carries more weight than a crafted insight line.

❌ (too writerly) `The people who are best at bringing others together are almost never the people who are best at building websites.`
✅ (his) `We built Heartbeat because community builders were running real businesses across five tools that were never meant to work together.`

### 2. Defiant energy, not a lament

Name the villain, but deliver it as a rallying cry, not a sad observation. He's pissed off and energized, never wistful. Don't dwell on the unfairness with somber language ("the quiet unfairness I've watched for years," "watched people bounce"). Hit it and convert it to defiance.

✅ `We saw the internet still rewarded creators with the most resources, not the best ideas. So we said screw that.`

### 3. A punchy one-line paragraph as the pivot

The turn of the piece is often a single short line standing alone with attitude. Don't smooth the pivot into a longer sentence; let it stand.

✅ `So we said screw that, and built landing pages into Heartbeat.`

### 4. Don't linger

Hit the emotional beat in one or two sentences and move. Momentum beats dwelling. If a draft spends two paragraphs on one feeling, cut it to two sentences.

### 5. Edge and enthusiasm in word choice

He uses mild profanity for emphasis ("screw that") and simple enthusiastic adjectives ("gorgeous"). Don't sand these off in the name of polish. Safe and measured reads as not-him.

### 6. Brand naming: name the product once, then "our AI"

Introduce the named product once with an appositive ("Pulse, our AI co-builder"), then refer to "our AI" after. Not zero mentions, not repeated name-drops.

### 7. Inclusive, multi-state CTA

Speak to more than one reader at once: the people who've already acted and the people who haven't. ✅ `if you've built a page, drop a link... And if you haven't, give it a try.`

### 8. Casual connectors

He mixes "&" into prose freely and uses contractions throughout. Short paragraphs, high momentum.

### Scope note on the bans above

Contrast and rhythm are fine and human; the bans are narrower than they look:
- **"X, not Y" contrast is allowed** ("rewarded creators with the most resources, not the best ideas"). The banned pattern is only the formulaic standalone identity-negation tic ("it's not about content, it's about connection").
- **Rhythmic triples inside a flowing sentence are allowed** ("every detail, every edit, and every pixel"). The banned pattern is staccato fragments stacked as separate sentences.

---

*This guide is a living doc. When a new AI-tell pattern shows up in the wild, add it here with an example. The list will grow.*
