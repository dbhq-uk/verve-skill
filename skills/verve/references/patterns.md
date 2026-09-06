# Pattern catalogue

Every tell has three parts: what it looks like, why it reads as machine-made,
and a *Before → After* to match in spirit. Flat word and phrase lists live in
`wordlist.md`; this file covers patterns you have to recognise rather than
grep for.

Six groups: **A** content, **B** language and structure, **C** style and
formatting, **D** assistant artefacts, **E** filler and hedging, **F**
condescension and overreach.

Groups A to E judge the writing on its own. Group F judges it against its
reader, so it needs `audience.md` alongside it.

---

## A. Content patterns

**A1. Significance inflation.** *stands as, serves as, is a testament to,
pivotal, key role, evolving landscape, indelible mark, deeply rooted.* Ordinary
facts puffed into civilisational milestones.

> Before: *was established in 1989, marking a pivotal moment in the evolution of regional statistics*
> After: *was established in 1989 to collect regional statistics independently of Spain's national office*

**A2. Notability name-drops.** *cited in The New York Times, BBC, Financial
Times; active social media presence; written by a leading expert.* Credentials
dropped in without context, doing no work.

> Before: *Her views have been cited in the NYT, BBC, FT and The Hindu. She has 500k followers.*
> After: *In a 2024 NYT interview she argued that AI regulation should focus on outcomes, not methods.*

**A3. Superficial *-ing* analyses.** *highlighting, underscoring, emphasising,
reflecting, symbolising, contributing to, fostering, showcasing.* Present
participles tacked on for fake depth.

> Before: *…resonates with the region's natural beauty, symbolising the bluebonnets, reflecting the community's deep connection to the land.*
> After: *…uses blue, green and gold; the architect chose them to reference local bluebonnets and the Gulf coast.*

**A4. Promotional / brochure language.** *nestled, vibrant, breathtaking,
must-visit, stunning, rich (figurative), boasts a, in the heart of, renowned.*

> Before: *Nestled in the breathtaking region of Gonder, Alamata stands as a vibrant town with rich cultural heritage.*
> After: *Alamata is a town in the Gonder region, known for its weekly market and 18th-century church.*

**A5. Vague attribution.** *industry reports, observers have noted, experts
argue, several sources.* No actual source behind any of it.

> Before: *Experts believe it plays a crucial role in the regional ecosystem.*
> After: *It supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.*

**A6. Formulaic "challenges and future prospects".** *Despite its… faces several
challenges… Despite these challenges… continues to thrive.*

> Before: *Despite challenges typical of urban areas, Korattur continues to thrive as part of Chennai's growth.*
> After: *Traffic worsened after 2015 when three IT parks opened; the council began a drainage project in 2022.*

**A7. Vague declaratives.** A sentence that asserts importance, depth or
structure without naming the thing. *The reasons are structural. The
implications are significant. The stakes are high. This is the deepest problem.*

Distinct from A1: A1 inflates a real fact, A7 has no fact in it at all. If the
sentence would survive being pasted into an unrelated document, it is filler.

> Before: *The implications for hiring are significant. The reasons are structural.*
> After: *Teams now interview for judgement rather than recall, because the recall half is automated.*

**A8. Telling instead of showing.** Announcing difficulty, importance or
authenticity rather than demonstrating it. *This is genuinely hard. This is what
leadership actually looks like. This actually matters.*

> Before: *Getting this right is genuinely hard. This is what real engineering discipline looks like.*
> After: *The migration took four attempts. The first three passed CI and broke in production.*

---

## B. Language and structure

**B1. AI vocabulary.** *delve, tapestry, leverage, utilise, realm, landscape,
pivotal, intricate, harness, groundbreaking, navigate, testament, robust,
holistic, foster, garner, underscore, showcase, interplay* and the rest. Full
list plus plain replacements in `wordlist.md`.

**B2. Copula avoidance.** Elaborate constructions standing in for *is*, *are*,
*has*.

> Before: *Gallery 825 serves as LAAA's exhibition space. The gallery features four rooms and boasts over 3,000 sq ft.*
> After: *Gallery 825 is LAAA's exhibition space. It has four rooms totalling 3,000 sq ft.*

**B3. Negative parallelism and binary contrast.** The single most reliable tell
in current model prose. Every variant of setting up a negation to knock it down:

| Variant | Example |
|---|---|
| Not X, but Y | *It's not just a song, it's a statement.* |
| The answer/question isn't X, it's Y | *The question isn't whether, it's when.* |
| X isn't the problem. Y is. | *Technology isn't the problem. Culture is.* |
| It feels like X. It's actually Y. | *It looks like a pricing issue. It's a trust issue.* |
| Stops being X and starts being Y | *The tool stops being a helper and starts being a colleague.* |
| Not only X but also Y | *Not only faster but also cheaper.* |

**Fix:** state Y. Drop the negation entirely. *The heavy beat adds to the
aggression* beats *it's not just about the beat; it's part of the aggression*.

**B4. Negative listing.** The same move stretched over several sentences.
*Not a X. Not a Y. A Z.* / *It wasn't X. It wasn't Y. It was Z.* State Z; the
reader does not need the runway.

**B5. False agency.** Inanimate subjects given human verbs. Models reach for
this constantly because it lets them avoid naming who did anything.

| Pattern | What actually happened |
|---|---|
| *a complaint becomes a fix* | Someone read it and fixed it. |
| *the decision emerges* | Someone decided. |
| *the culture shifts* | People changed how they behave. |
| *the conversation moves toward* | Someone steered it. |
| *the data tells us* | Someone read the data and drew a conclusion. |
| *the market rewards* | Buyers paid for it. |
| *a bet lives or dies in days* | Someone shipped it or killed it. |

**Fix:** name the human. If no specific person fits, use *you* and put the
reader in the seat, subject to the tone preset (see `voice.md` - academic and
professional presets restrict second person).

**B6. Narrator from a distance.** Floating above the scene rather than standing
in it. *Nobody designed this. People tend to. This happens because. This is why.*

> Before: *Nobody designed this. Organisations tend to accumulate process over time.*
> After: *You don't sit down one morning and decide to add four approval steps. You add one, then another, after each thing goes wrong.*

Tone-dependent: fine in academic register, a tell in essays and blog posts.

**B7. Rule of three.** Forced triplets to sound comprehensive. Two items are
almost always enough.

> Before: *talks, panels and networking opportunities; innovation, inspiration and insight.*
> After: *talks and panels, plus informal networking between sessions.*

**B8. Elegant variation.** Synonym cycling driven by repetition penalties.

> Before: *The protagonist faces challenges. The main character overcomes obstacles. The central figure triumphs. The hero returns home.*
> After: *The protagonist faces challenges but eventually triumphs and returns home.*

**B9. False ranges.** *from X to Y* where X and Y sit on no real scale.

> Before: *from the Big Bang to the cosmic web, from the birth of stars to the dance of dark matter*
> After: *covers the Big Bang, star formation and current theories about dark matter*

**B10. Passive voice and subjectless fragments.** Passive hides the actor and
drains the sentence.

> Before: *No configuration file needed. The results are preserved automatically.*
> After: *You don't need a configuration file. The system preserves results automatically.*

Keep the passive where the actor is genuinely unknown or irrelevant, and in
academic register where convention expects it.

**B11. Persuasive authority tropes.** *the real question is, at its core,
fundamentally, what really matters, the heart of the matter.* Ceremony around an
ordinary point.

> Before: *The real question is whether teams can adapt. At its core, what matters is organisational readiness.*
> After: *Whether teams can adapt depends mostly on whether the organisation is ready to change its habits.*

**B12. Lazy extremes.** *every, always, never, everyone, nobody, all.* False
authority standing in for a specific claim. Replace with the actual scope.

> Before: *Everyone knows this approach never scales.*
> After: *Both teams that tried it hit the same lock contention at around 200 writers.*

**B13. Wh- opener crutch.** *What makes this hard is… Why this matters is…
How teams solve this is…* Occasional use is fine; models use it as a default
sentence shape. If two or more appear in a passage, restructure so the subject
leads.

> Before: *What makes migrations painful is the rollback path.*
> After: *The rollback path is what makes migrations painful.* Or better: *Migrations hurt because rolling one back means replaying six hours of writes.*

**B14. Hyphenated word-pair overuse.** *cross-functional, data-driven,
decision-making, client-facing, end-to-end, real-time, long-term, third-party,
well-known, high-quality.* Models hyphenate these with perfect consistency;
people do not.

---

## C. Style and formatting

**C1. Em dashes.** Used far more by models than by people. Replace with commas,
full stops, semicolons or brackets.

**C2. Boldface emphasis.** Mechanical inline bolding of key terms. Strip unless
the source genuinely uses bold for UI labels or defined terms.

**C3. Inline-header vertical lists.** Bullets shaped `- **Foo:** …`. Convert to
prose unless a real list is warranted.

**C4. Title Case Headings.** Use sentence case: *## Strategic negotiations and
global partnerships*.

**C5. Emojis in headings and bullets.** 🚀 💡 ✅ - remove unless the source
document genuinely uses them.

**C6. Curly quotes.** Replace typographic quotes with straight ones unless the
source is typeset prose where curly is correct.

**C7. Dramatic fragmentation.** Stacked fragments performing profundity.
*[Noun]. That's it. That's the [thing]. X. And Y. And Z.*

A single fragment for emphasis is good writing and `voice.md` asks for one
occasionally. Stacking them is the tell. One per few hundred words reads as a
choice; three in a row reads as a template.

> Before: *Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff.*
> After: *You get two of speed, quality and cost. Everyone picks cost and regrets it.*

---

## D. Assistant artefacts

**D1. Chatbot artefacts.** *I hope this helps! Of course! Certainly! You're
absolutely right! Let me know if you'd like… Here's an overview of…* Strip
entirely.

**D2. Knowledge-cutoff disclaimers.** *As of my last update, while specific
details are limited, based on available information.*

**D3. Sycophancy.** *Great question! That's an excellent point!* Delete.

**D4. Signposting.** *Let's dive in, let's explore, let's break this down,
here's what you need to know, without further ado.* Do the thing instead.

> Before: *Let's dive into how caching works in Next.js. Here's what you need to know.*
> After: *Next.js caches data at several layers: request memoisation, the data cache, and the router cache.*

**D5. Fragmented headers.** A heading followed by a one-line paragraph that
restates the heading.

> Before: *## Performance* / *Speed matters.* / *When users hit a slow page they leave.*
> After: *## Performance* / *When users hit a slow page they leave.*

**D6. Meta-commentary.** The piece narrating its own structure instead of
having one. *The rest of this essay explains… In this section, we'll… Let me
walk you through… As we'll see… But that's another post.* Also the stock asides:
*Plot twist: / Spoiler: / Hint: / X is a feature, not a bug.*

Delete them. A piece that moves does not need to announce that it is moving.

**D7. Rhetorical setups.** Questions and prompts that announce insight rather
than deliver it. *What if [reframe]? Here's what I mean: Think about it: And
that's okay.* Make the point; let the reader draw the conclusion.

---

## E. Filler and hedging

**E1. Filler phrases.** *in order to* → *to*, *due to the fact that* →
*because*, *has the ability to* → *can*, *it is important to note that* →
delete. Full table in `wordlist.md`.

**E2. Excessive hedging.** *It could potentially possibly be argued that the
policy might have some effect.* → *The policy may affect outcomes.*

**E3. Emphasis crutches.** Phrases that assert weight without adding any.
*Full stop. Period. Let that sink in. Make no mistake. This matters because.
Here's why that matters.* Delete; if the point carries weight, it carries it.

**E4. Generic positive conclusions.** *The future looks bright. Exciting times
lie ahead. A major step in the right direction.* Replace with a concrete next
thing, or simply end on the last real point.

**E5. Banned openers and closers.** *In today's world, in conclusion, in
summary, at the end of the day, having said that, needless to say, it goes
without saying, when it comes to.* Full list in `wordlist.md`.

**E6. Dead adverbs.** *really, just, literally, genuinely, honestly, simply,
actually, truly, deeply, fundamentally, inherently, interestingly, importantly,
crucially.* These add emphasis without adding meaning.

Cut them by default, with one exception: the casual tone preset allows
*honestly*, *look* and similar as genuine discourse markers, where they mark a
shift in stance rather than decorate an adjective. *Honestly, I'd skip it* is a
person talking. *This is genuinely important* is padding.

---

## F. Condescension and overreach

These are tells about the reader rather than about the writing. They only
resolve once you know who is going to read the result, so `audience.md` carries
the register model and this group carries the patterns. Where no audience is
known, assume competence.

**F1. Explaining a term the reader uses daily.** A gloss on a word the recipient
works with every day. The gloss is not wrong; it is the assumption behind it
that gives offence.

> Before: *We should look at the CAC, or customer acquisition cost, which is what it costs to win one new customer.* (to the head of growth)
> After: *CAC is up 40% since the channel mix changed.*

**F2. Restating the ask.** Opening by repeating what the reader just asked for,
which tells them only that you can read.

> Before: *You asked whether we should move the deploy to Thursday. To answer your question about moving the deploy to Thursday: yes.*
> After: *Yes, move it to Thursday.*

**F3. Reasons before the answer.** Making somebody read the working before they
get the result. In a reply to a question, the answer is the first thing.

> Before: *Because the pool never refills and every request holds its own connection, and given the 20-connection ceiling, the gateway will fail again under the same load.*
> After: *It will fail again under the same load. The pool never refills, and each request holds its own connection against a ceiling of 20.*

**F4. Unrequested caveats.** Qualifications nobody asked for, added to protect
the writer rather than to inform the reader.

> Before: *Roll back `dep-4471`. Of course, every environment differs, and you should verify this in staging first, and results may vary depending on your configuration.*
> After: *Roll back `dep-4471`.*

Distinct from E2: hedging weakens a claim, F4 keeps the claim and bolts a
disclaimer to it.

**F5. Instructing upwards.** Directing somebody who has more standing on the
subject than the writer does. Offer, and leave the decision where it belongs.

> Before: *You need to escalate this to the board before Friday.*
> After: *This looks like a board matter, and Friday is the last meeting before quarter end.*

**F6. Telling them what they told you.** Feeding a person's own information back
as though it were news.

> Before: *As you mentioned, the outage started at 02:14. Given that it started at 02:14, the window is just under two hours.*
> After: *That puts the window at 1h 45m.*

**F7. Performed empathy.** Stated feeling standing in for action. The reader
wanted the problem dealt with, not acknowledged.

> Before: *I completely understand how frustrating this must be, and I want you to know we hear you.*
> After: *Your invoice was wrong. We have refunded the £240 and it should reach you by Thursday.*

**F8. Grovelling.** Apology stacked past the point of usefulness, which leaves
the reader managing the writer's feelings on top of their own problem.

> Before: *I'm so sorry, this is entirely my fault, I should have caught it much earlier and I completely understand if you've lost confidence in us.*
> After: *Sorry, I missed this. It is fixed, and the check that would have caught it now runs on every deploy.*

One apology, then the fix. The second apology is for the writer.

**F9. Overreach.** Committing on somebody's behalf, assuming authority the
writer does not have, or setting deadlines for people who do not report to them.

> Before: *Design will have the mocks to you by Wednesday and Legal will sign off the same week.*
> After: *I have asked Design for mocks by Wednesday. Legal has not been approached yet.*

**F10. Length as an imposition.** A long message where a short one would do,
sent to somebody with no time to read it. Every word is a cost the writer has
chosen to pass to the reader.

This one is measured against the audience rather than against a word count. Two
thousand words to a reviewer who asked for detail is right; two hundred to a
director who asked one question is not.

> Before: eleven paragraphs and three headings, in reply to *"which deploy do I roll back?"*
> After: *`dep-4471`, gateway, deployed 01:52 by `a.novak`. Full timeline in `INCIDENT-2026-03-14.md`.*

---

## Rhythm (applies throughout)

- Mix short sentences (3-7 words) with long ones (20-30). Aim for high variance,
  measured across the passage rather than within a single paragraph.
- Vary paragraph length. Some one sentence, some five.
- One deliberate fragment now and then. Not three in a row (see C7).
- Do not start consecutive paragraphs the same way.
- Do not end every paragraph on a punchy one-liner. That rhythm is itself a tell.
- Turn list-shaped prose into flowing sentences unless a list is genuinely
  clearer.
