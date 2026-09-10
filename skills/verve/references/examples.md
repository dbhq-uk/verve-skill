# Worked examples

Full passages rather than single sentences, because most tells only show up at
length. Each notes which patterns were removed.

Every after-text below uses only what its before-text contains. That is the
rule being taught, so the examples obey it: where a fix needs a specific, the
before-text carries that specific, wrapped in the slop the fix removes. Word
counts are given deliberately. A humanisation that halves the length has
usually deleted content, not filler.

---

## 1. Blog prose, moderate strength, neutral tone

**Before** (70 words)

> Here's the thing: in today's fast-paced engineering landscape, code review
> isn't just a quality gate — it's a cultural artefact. What makes it hard is
> that the feedback becomes a signal about the team itself. Let that sink in.
> Teams that delve into review culture find that it fosters trust, improves
> velocity and builds shared ownership. The implications are significant. Not
> because the tooling is complex. Because people are complex.

**After** (61 words)

> Code review is a quality gate, but it is also part of a team's culture, and
> that is the hard part: feedback on the code reads as a signal about the team
> itself. Teams that work at their review culture find it builds trust, speeds
> them up and spreads ownership. None of that is because the tooling is
> complex. People are.

**Removed:** throat-clearing opener (D-list), *in today's* (E5), *landscape* and
*delve* and *fosters* (B1), em dash (C1), Wh- opener (B13), emphasis crutch
*let that sink in* (E3), vague declarative (A7), binary contrast (B3).

**Note:** every claim in the original survives: quality gate, cultural
artefact, feedback as a signal about the team, trust, velocity, shared
ownership, people over tooling. Trust, velocity and ownership stay as three
items because they are three claims; B7 targets forced triplets, not real
ones. And nothing appears in the after-text that the before-text does not
carry. The tells came out; the argument stayed.

---

## 2. The failure mode to avoid

Same passage, over-cut:

> Code review is about people, not tools.

Seven words, no tells, and it has thrown away six of the original's seven
claims. Run the readback against it: what makes review hard? What do teams
that work at review culture get? Neither question can be answered from the
rewrite, so the readback fails it, however clean it reads. When a rewrite
drops below roughly 70% of the original length, check whether content went
with the filler.

---

## 3. Reference prose, moderate strength, neutral tone

**Before** (59 words)

> Nestled in the breathtaking Cotswolds, Stow-on-the-Wold stands as a vibrant
> market town with a rich history dating back to its 1330 market charter.
> Its picturesque square, which serves as the heart of the town and was
> originally laid out for the annual sheep fairs, boasts numerous independent
> shops, highlighting the area's enduring appeal to visitors from across the
> globe.

**After** (42 words)

> Stow-on-the-Wold is a market town in the Cotswolds, chartered as a market in
> 1330. The square at its centre was laid out for the annual sheep fairs and
> now holds numerous independent shops. It continues to draw visitors from
> across the globe.

**Removed:** *nestled*, *breathtaking*, *vibrant*, *picturesque*, *boasts* (A4),
*stands as* and *serves as* (A1, B2), *rich history* (A1), *highlighting* (A3),
*enduring appeal* (A1).

**Note:** the charter date and the sheep fairs are in the before-text, which is
why the after-text may use them. Where a real source says only *"a rich
history dating back to the medieval period"*, the honest after keeps exactly
that: *"Stow-on-the-Wold is a market town in the Cotswolds with a history
dating back to the medieval period. Its central square holds numerous
independent shops, and the area remains popular with visitors from across the
globe."* Never fill a promotional adjective's hole with a fabricated fact, and
never let cutting the adjective take a claim with it.

---

## 4. Assistant output, light strength

**Before**

> Great question! Let's dive into how database indexing works. Here's what you
> need to know:
>
> - **B-tree indexes:** These are the most common type of index.
> - **Hash indexes:** These offer O(1) lookups for equality comparisons.
> - **Partial indexes:** These index only a subset of rows.
>
> I hope this helps! Let me know if you'd like me to elaborate on any of these.

**After**

> B-tree indexes are the most common type. Hash indexes give O(1) lookups for
> equality comparisons. Partial indexes cover only a subset of rows.

**Removed:** sycophancy (D3), signposting (D4), chatbot artefacts (D1),
inline-header bullets (C3), fragmented restatement of each heading (D5).

**Note:** light strength normally preserves sentence structure. Here the
structure *was* the tell, so converting the list to prose is in scope even at
light. Every technical claim, including *O(1)*, is exactly the source's, and
nothing has been added to dress the prose up: an answer this thin stays thin,
because filling it out would be invention.

---

## 5. Casual tone, heavy strength

**Before** (91 words)

> It is important to note that the migration process was fraught with
> challenges. The team made a total of four attempts, and the first three of
> these passed CI only to subsequently fail in production. Despite these
> obstacles, the team persevered and ultimately succeeded, in no small part due
> to the fact that an ops engineer was embedded from day one rather than being
> consulted only at the review stage. The project stands as a testament to what
> cross-functional collaboration can achieve. Moving forward, the future looks
> bright for the platform.

**After** (56 words)

> The migration was a mess. Four attempts, and the first three passed CI before
> falling over in production. The team got there in the end, and the thing that
> made the difference was having an ops engineer in the room from day one
> rather than at the review. Things look good for the platform from
> here.

**Removed:** *it is important to note* (E1), *due to the fact that* (E1),
formulaic challenges-then-triumph arc (A6), *testament* (A1, B1),
*moving forward* (jargon), *subsequently*, generic positive conclusion (E4)
folded into a plain final sentence.

**Note:** the attempts, the CI failures and the ops engineer are all in the
before-text; heavy strength licenses restructuring, never invention. The
*testament to cross-functional collaboration* sentence survives as the ops
sentence, which is the same claim made concretely. If the source really is
vague - *"the process was fraught with challenges, but the team persevered
and ultimately delivered a robust solution, a testament to what
cross-functional collaboration can achieve"* - the honest after-text is *"The
migration was difficult, but the team got there and delivered something
reliable. It shows what collaboration across teams can do."* Every claim in
that source kept, nothing specific conjured to decorate it.

---

## 6. Audience guard, moderate strength

**Audience:** the VP of Engineering, who ran the platform team for six years.
She asked one question: whether to approve the extra Redis nodes.

**Before** (155 words)

> Thanks so much for your question about the Redis scaling request! I completely
> understand that budget decisions like this can be difficult, and I want you to
> know your caution here is very reasonable.
>
> By way of background, Redis is an in-memory data store, which means it keeps
> data in RAM rather than on disk. This makes it very fast, but it also means
> capacity is limited by available memory.
>
> Basically, we're running out of memory - we are currently at 87% on the
> primary cluster and have experienced evictions on two occasions in the past
> week. You need to approve the three additional nodes by Friday so that
> Infrastructure can provision them next week; our estimate is that three nodes
> would give us headroom to roughly 2x current volume. I'll get Finance to sign
> off the spend at the same time.
>
> I hope this makes sense! Let me know if you have any questions.

**After** (57 words)

> Yes, worth approving. We are at 87% memory on the primary Redis cluster and
> have hit evictions twice in the past week.
>
> Three additional nodes should cover us to roughly 2x current volume.
> Infrastructure can provision next week if the decision lands by Friday, and
> I'll get Finance to sign off the spend at the same time.

**Removed:** sycophancy (D3), performed empathy (F7), a definition of Redis for
somebody who ran the platform team (F1), *basically* and *I hope this makes
sense* (condescension list), *you need to approve* aimed upwards, recast so the
deadline and the decision survive without the command (F5), chatbot closer
(D1).

**Note:** every figure, estimate and modality in the after-text is in the
before-text - *should cover* stays an estimate because the source said
*estimate* and *would*. The audience guard removed the Redis gloss, which is
explanation this reader does not need; it removed no fact of the request
itself. If the source lacks the numbers, the honest version keeps everything
she acts on: *"Yes, worth approving. We are running out of memory, and
Infrastructure can provision the three additional nodes next week if the
decision lands by Friday. I'll get Finance to sign off the spend at the same
time."*

Two things deliberately kept. *Yes, worth approving* leads, because she asked a
question and the answer is the first thing she should read (F3). *I'll get
Finance to sign off the spend* stays, because it is the writer's own
undertaking rather than a promise made on Finance's behalf - F9 removes
invented commitments, not real ones - and cutting it would change what she
does next, which is constraint 4 broken in the guard's name.
