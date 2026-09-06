# Worked examples

Full passages rather than single sentences, because most tells only show up at
length. Each notes which patterns were removed.

Word counts are given deliberately. A humanisation that halves the length has
usually deleted content, not filler.

---

## 1. Blog prose, moderate strength, neutral tone

**Before** (86 words)

> Here's the thing: in today's fast-paced engineering landscape, code review
> isn't just a quality gate — it's a cultural artefact. What makes it hard is
> that the feedback becomes a signal about the team itself. Let that sink in.
> Teams that delve into review culture find that it fosters trust, improves
> velocity and builds shared ownership. The implications are significant. Not
> because the tooling is complex. Because people are complex.

**After** (84 words)

> Code review is a quality gate, but it also tells you what a team is like.
> The difficulty is that people read feedback on their code as feedback on
> them, so the tone of a review carries further than its content. Teams that
> take review culture seriously tend to trust each other more and ship faster,
> partly because ownership stops being one person's problem. That is mostly a
> people problem rather than a tooling one.

**Removed:** throat-clearing opener (D-list), *in today's* (E5), *landscape* and
*delve* and *fosters* (B1), em dash (C1), Wh- opener (B13), emphasis crutch
*let that sink in* (E3), rule of three (B7), vague declarative (A7), binary
contrast (B3), false agency in *the feedback becomes a signal* (B5).

**Note:** length is preserved. Every claim in the original survives: quality
gate, cultural signal, difficulty of feedback, trust, velocity, shared
ownership, people over tooling. The tells came out; the argument stayed.

---

## 2. The failure mode to avoid

Same passage, over-cut:

> Code review is about people, not tools.

Nine words, no tells, and it has thrown away six of the original's seven
claims. This scores 10 on Density and 2 on Fidelity, which is a fail, because
Fidelity is a veto. When a rewrite drops below roughly 70% of the original
length, check whether content went with the filler.

---

## 3. Reference prose, moderate strength, neutral tone

**Before** (52 words)

> Nestled in the breathtaking Cotswolds, Stow-on-the-Wold stands as a vibrant
> market town with a rich history dating back to the medieval period.
> Its picturesque square, which serves as the heart of the town, boasts
> numerous independent shops, highlighting the area's enduring appeal to
> visitors from across the globe.

**After** (48 words)

> Stow-on-the-Wold is a market town in the Cotswolds, chartered as a market in
> 1330. The square at its centre was built for the annual sheep fairs and now
> holds mostly independent shops. It remains one of the more visited towns in
> the area.

**Removed:** *nestled*, *breathtaking*, *vibrant*, *picturesque*, *boasts* (A4),
*stands as* and *serves as* (A1, B2), *rich history* (A1), *highlighting* (A3),
*visitors from across the globe* (A4).

**Note:** *chartered as a market in 1330* and *built for the annual sheep fairs*
would be inventions if the source did not contain them. Shown here as what the
after-text looks like when the source *does* have those specifics. Where it
doesn't, the correct after is *"Stow-on-the-Wold is a market town in the
Cotswolds. Its central square holds mostly independent shops."* Never fill a
promotional adjective's hole with a fabricated fact.

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

> Postgres has three index types worth knowing. B-trees are the default and
> handle ranges and ordering. Hash indexes give O(1) equality lookups but
> nothing else. Partial indexes cover a subset of rows, which keeps them small
> when most queries only touch recent data.

**Removed:** sycophancy (D3), signposting (D4), chatbot artefacts (D1),
inline-header bullets (C3), fragmented restatement of each heading (D5).

**Note:** light strength normally preserves sentence structure. Here the
structure *was* the tell, so converting the list to prose is in scope even at
light. The technical content, including *O(1)*, is untouched under constraint 2.

---

## 5. Casual tone, heavy strength

**Before** (61 words)

> It is important to note that the migration process was fraught with
> challenges. Despite these obstacles, the team persevered and ultimately
> succeeded in delivering a robust solution. The project stands as a testament
> to what cross-functional collaboration can achieve. Moving forward, the
> future looks bright for the platform.

**After** (57 words)

> The migration was a mess. Four attempts, and the first three passed CI before
> falling over in production. The team got there in the end, and the thing that
> made the difference was having someone from ops in the room from day one
> rather than at the review. The platform is on a better footing now.

**Removed:** *it is important to note* (E1), formulaic challenges-then-triumph
arc (A6), *robust* and *testament* (A1, B1), *cross-functional* (B14),
*moving forward* (jargon), generic positive conclusion (E4).

**Note:** *four attempts*, *passed CI*, *someone from ops* are only legitimate
if the source contained them. Heavy strength licenses restructuring, never
invention. If the source really is that vague, the honest after-text is
*"The migration was a mess, and the team got there in the end. Having ops
involved early was what made the difference."* Shorter, still specific about
what it does know, and silent about what it doesn't.

---

## 6. Audience guard, moderate strength

**Audience:** the VP of Engineering, who ran the platform team for six years.
She asked one question: whether to approve the extra Redis nodes.

**Before** (118 words)

> Thanks so much for your question about the Redis scaling request! I completely
> understand that budget decisions like this can be difficult, and I want you to
> know your caution here is very reasonable.
>
> By way of background, Redis is an in-memory data store, which means it keeps
> data in RAM rather than on disk. This makes it very fast, but it also means
> capacity is limited by available memory.
>
> Basically, we're running out of memory. You need to approve the three
> additional nodes by Friday so that Infrastructure can provision them next
> week, and I'll get Finance to sign off the spend at the same time.
>
> I hope this makes sense! Let me know if you have any questions.

**After** (44 words)

> Yes, worth approving. We are at 87% memory on the primary cluster and hit
> evictions twice last week.
>
> Three nodes covers us to roughly 2x current volume. Infrastructure can
> provision next week if the decision lands by Friday. Finance has not been
> asked yet.

**Removed:** sycophancy (D3), performed empathy (F7), a definition of Redis for
somebody who ran the platform team (F1), *basically* and *I hope this makes
sense* (condescension list), *you need to approve* aimed upwards (F5), the
commitment made on Finance's behalf (F9), chatbot closer (D1).

**Note:** the before-text is 118 words and contains one fact. The after-text is
44 and contains five, three of which were never in the original and could only
be added because the writer knew them. If you do not have the numbers, do not
invent them: constraint 3 has no exceptions, and the honest version is *"Yes,
worth approving. We are close to the memory ceiling and saw evictions last
week."*

Two things deliberately kept. *Yes, worth approving* leads, because she asked a
question and the answer is the first thing she should read (F3). *Finance has
not been asked yet* stays, because it changes what she does next, and cutting it
for brevity would be constraint 4 broken in the guard's name.
