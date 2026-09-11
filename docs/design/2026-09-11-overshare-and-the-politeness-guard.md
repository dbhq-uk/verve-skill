# Design: the overshare check, and the politeness guard it sits next to

Date: 2026-09-11

Two pieces of work in one document, because the second is what reading the
first exposed.

1. A new **overshare check** - group G - which asks whether the writer should
   be handing something over at all.
2. Four fixes to the existing **politeness check** - group F and
   `references/audience.md` - which is two-sided in doctrine and one-sided in
   structure.

## 1. The overshare check

### The problem

Group F asks *does this reader need this explained?* Nothing in verve asks
*should the writer be saying this at all?*

They are different questions. Group F is about respecting the reader; overshare
is about protecting the writer, and the person not in the room. A draft can
pass every existing check, be pitched perfectly, carry no condescension, and
still name another client's rate, give an excuse nobody asked for, or hand over
a negotiating position for free.

The gap is not length. F10 already covers a long message sent to a busy reader,
and the `E` group covers padding. A one-line email can overshare. That is why
this is a new group rather than an extension of an existing one.

### The principle, and two tests

Nothing is flagged unless **both** tests pass.

1. **Did they ask for it, or do they need it to act?** If yes, it stays and
   nothing fires. This is the F4 caveat test run the other way round: there,
   a qualification survives if it gives the reader something to act on; here,
   a disclosure survives on the same ground.
2. **Does saying it cost the writer, or somebody not in the room?**
   Credibility, negotiating position, a confidence, another person's privacy.
   If nothing is lost, it is an incidental detail, not an overshare.

Either test alone produces noise. Test 1 alone flags every fact the reader did
not strictly require. Test 2 alone flags anything unflattering. Together they
catch the thing the writer did not notice writing.

### The floor, which is not negotiable

The check never flags:

- anything the reader needs in order to decide or act
- anything whose removal would mislead by omission
- a risk, a delay or a cost the reader is carrying
- a conflict of interest, or a disclosure a contract or a regulator requires
- a fact that is merely unflattering - being wrong is not oversharing

One test sits behind all five: **would the reader act differently if they
knew?** If yes it is information, not an overshare, and the flag does not fire.

This goes in `references/overshare.md` in the position `audience.md` gives its
own boundary section, and for the same reason. A control that helps you say
less sits one step from a control that helps you conceal, and the difference
between them is a sentence somebody has to write down.

### The seven patterns

Group G in `patterns.md`, in the house format: what it looks like, why it is an
overshare, and a *Before → After*.

Both tests gate every pattern below, without exception. "Fires on sight" means
the pattern needs no reading of the audience, not that it skips the tests: a
personal circumstance offered to somebody who asked after you fails test 1, and
nothing fires.

**These fire on sight. No reader needed, because they are wrong in front of
anybody.**

**G1. Third-party disclosure.** Another client named, a colleague's private
remark, what somebody else is paying.

> Before: *I can start on the 6th, once the Northwind engagement wraps up.*
> After: *I can start on the 6th.*

The date is the fact the reader needs. Who else is buying your time is not.

**G2. Personal circumstances.** Health, money, family, mood, where you were.

> Before: *Sorry for the slow reply, I have been dealing with a family illness.*
> After: *Sorry for the slow reply.*

The apology is owed and stays - cutting it would be F11. The reason is not the
reader's business. Note the line test 1 draws: *"I am away next week"* is
operational and stays, because the reader plans around it.

**These need a reader - known, or the text plainly outward-facing.**

**G3. Unasked-for reasons and excuses.** The apology is owed; the reason is the
writer's problem.

> Before: *Sorry, I missed Friday - the spec landed late and I had two other deadlines that week.*
> After: *Sorry, I missed Friday.*

**G4. Internal detail.** How the sausage was made: who was off sick, which
system fell over, that you forgot.

> Before: *The report is late - the build server died on Tuesday and Sam was on leave.*
> After: *The report is late.*

The floor governs the exception. Where the cause tells the reader it will
happen again, the cause is a risk they are carrying and it stays.

**G5. Position leakage.** Your availability is thin, you need the work, your
fallback price, how much the deadline is hurting.

> Before: *I have capacity from next week and the pipeline is quiet, so I can be flexible on rate.*
> After: *I have capacity from next week.*

**G6. Over-answering.** Answering the question they did not ask alongside the
one they did. Scope, a figure, or a capability nobody costed, volunteered.

> Before, replying to *"can you take the Azure piece?"*: *Yes. I could also take the identity workstream and the reporting if that helps.*
> After: *Yes.*

**G7. Pre-emptive confession.** Flagging something that is not yet a problem
and that the writer can still absorb.

> Before: *This should be fine, though I have had weeks where things slip.*
> After: *This should be fine.*

The floor governs this one hardest. Where the slip is real and dated, the
reader needs it, and it stays.

**A note the group needs, in its own preamble.** Every *After* line above shows
what an explicitly requested cut produces. The default is `flag`, so on a
normal run the *Before* text is what ships and the *After* is what the note
describes. The catalogue is not a licence to cut. `patterns.md` already carries
a version of this warning for groups A to F; group G needs its own, because
here the material at risk is a fact rather than a flourish.

### Flag, not cut

An overshare is a fact (hard constraint 1) or a claim (hard constraint 4).
Cutting one breaks a veto that `AGENTS.md` calls non-negotiable, and the step 6
fidelity readback would score the cut as a failure - correctly.

So the resolution is a line, not an exception:

**Verve never decides on its own to remove content. The user can.**

Default behaviour is `flag`. The output is the humanised text, then, **only
where something fired**, a short block - one line each, naming what it is and
why:

```
Overshare (not cut):
- You give the reason you missed Friday. He asked for the date, not the why.
- Paragraph 3 names the other client's rate.
```

Nothing fires, nothing is said. That is the rule the preferences lookup already
follows for a missing file.

An explicit instruction - *"verve this and cut the oversharing"* - makes the
cuts and names them under `Overshare (cut):` instead.

This holds the constraint intact rather than carving it out. The constraints
outrank "every other instruction in this skill" [from `SKILL.md`], and a user
telling verve to remove a sentence from their own draft is not an instruction
inside the skill. It is an edit they made.

### The preferences key, deliberately crippled

A fifth option joins the four in the `SKILL.md` usage table, where the values
are what a request may ask for:

| Option | Values | Default |
|---|---|---|
| Overshare | flag, cut, off | flag |

A fifth key joins the four in `references/preferences.md`, where they are not:

| Key | Values | Default |
|---|---|---|
| Overshare | flag, off | flag |

**`cut` is valid from the request only, and never from a file.** A `.verve.md`
arrives with any repository you clone. `AGENTS.md` rule 1b exists so that a
file on disk cannot steer the skill on a machine that merely opened it, and
this is the first setting where the stake is the removal of facts rather than a
change of tone. A file that says `Overshare: cut` gets read as `flag`, and the
run says in one line which value it ignored - the behaviour `preferences.md`
already specifies for a file that asks for something it may not have.

### What it does to step 6

The fidelity readback would score every requested cut as an omission. So step 6
gains one rule:

> Content removed under an explicit instruction from the user is a deliberate
> removal. Record it, list it in the output, and exclude it from the readback.
> Content removed without one is an omission and fails, exactly as now.

The distinction is the instruction, and it has to be an instruction in the
request. Nothing else changes about the readback.

### The third exit gate

Step 7 gains **Disclosure**, alongside Fidelity and Audience fit, and pass or
fail on its own like the other two. No total, for the reason step 7 already
gives.

Disclosure passes when every candidate is either left in place and listed, or
cut under an explicit request and named. It fails when anything was removed
without being named, and it fails when something on the floor list was flagged.
The second failure is the one to watch: a guard that flags a real risk is
training the writer to bury it.

## 2. Four fixes to the politeness guard

### 2.1 The guard is one-sided in structure

**The finding.** `audience.md` is explicit that politeness fails in two
directions, and that curtness is the failure a condescension guard will
actively produce. The exit gate checks both: audience fit passes only when
"the warmth this reader is owed is intact: the greeting, the thanks, the one
apology where one is owed" [from `SKILL.md` step 7].

Nothing produces that result. Group F is ten patterns all pointing the same
way. Step 5's quick checks have *"Second and third apology? One is enough"* -
the condescension direction - and nothing checking that the first survived.

So the sweep can only make text colder, and the gate is asked to catch a
failure the sweep is structurally biased towards creating. It is the same shape
as the bug the whole fidelity readback exists to catch: a rewrite that reads as
correct because of what it dropped.

**The fix.** Group F is renamed *condescension, overreach and curtness*, and
gains an eleventh pattern.

**F11. Warmth stripped.** The greeting, the thanks, or the one owed apology
removed in the name of concision.

> Source: *Thanks for flagging this, and sorry. We have refunded the £240 and it should reach you by Thursday.*
> After an over-aggressive sweep: *Refunded. £240, Thursday.*
> Correct: the source line, restored.

The framing matters and has to survive into the catalogue. **F11 restores
warmth the rewrite removed. It never adds warmth the source did not have** -
that would be inventing content, which hard constraint 3 forbids without
exception. F11 is a fidelity check wearing a register hat.

One line joins step 5: *"Greeting, thanks, or the one apology that was owed -
still there? Put it back."*

Cost is about fifteen lines, and it makes an existing gate checkable.

### 2.2 SKILL.md and audience.md disagree about the condescension list

**The finding.** `audience.md` heads its condescension word list with "Plus
these, on sight, **wherever the reader has any expertise in the subject**".
`SKILL.md`'s light-strength rule fires "the condescension words in
`audience.md`" with no such condition.

They cannot both be right, and the unknown-reader default makes it worse:
"assume competence, **not knowledge**" [from `audience.md`] draws exactly the
distinction the gate depends on. Unknown reader means unknown expertise, so by
`audience.md` the list does not fire, and by `SKILL.md` it does.

**The fix.** The list becomes ungated, with one exception, and moves to
`wordlist.md` under a new `## Condescension` heading - which is where the
skill's own organising principle puts a flat scannable list, and which makes
`SKILL.md`'s light-strength sentence true as written.

Ungated, because every line on it is about the writer's posture rather than the
reader's knowledge. `audience.md`'s own argument for *as you know* generalises:
if they do know, you wasted their time; if they do not, you told them they
should have. There is no reader for whom it works.

The exception is the four simplification markers - *basically, essentially, in
layman's terms, to put it simply* - which stay gated on expertise, because
simplifying is a service to a newcomer and an insult to an expert.

`audience.md` keeps the *as you know* note and points at `wordlist.md` for the
list itself.

### 2.3 Light strength skips F8

**The finding.** Light takes "only F2 and F6, which are deletions rather than
rewrites" [from `SKILL.md` step 3]. But `audience.md` names five patterns as
reader-independent - F2, F6, F7, F8 and F10 - and F8's fix is a pure deletion:
keep the first apology, cut the second and third.

So light strength, which already cuts sycophancy by name, leaves grovelling in
place. The two are the same reflex pointed at different people.

**The fix.** Light takes F2, F6 and F8. F7 and F10 stay out, because their
fixes are rewrites and light keeps sentence structure - that part of the rule
is right and stays.

### 2.4 "Politeness" exists only in the READMEs

**The finding.** `README.md`, `skills/verve/README.md` and `plugin.json` all
call it the politeness check, as of 2026-09-08. `SKILL.md` and `references/`
never use the word - they say *audience fit* and *condescension*. A user
reading the README and a contributor reading the skill are discussing the same
control under two names, and a second reader-facing control is about to land
next to it.

**The fix.** Settle the vocabulary in both directions.

- **The politeness check** is group F plus `audience.md`, gated by
  **Audience fit**, which becomes "Audience fit (the politeness check)" in
  step 7. The gate name does not change, so the corpus assertions do not move.
- **The overshare check** is group G plus `overshare.md`, gated by
  **Disclosure**.
- The `SKILL.md` frontmatter description gains the overshare triggers:
  *oversharing*, *am I saying too much*, *should I be telling them this*.

## Files touched

| File | Change |
|---|---|
| `skills/verve/references/overshare.md` | New. Principle, two tests, the floor, the reader-dependency rule |
| `skills/verve/references/patterns.md` | Six groups become seven. Group F renamed and gains F11. New group G, G1-G7, with its own preamble |
| `skills/verve/references/audience.md` | Condescension list moves out to `wordlist.md`; F11 joins the guard's pattern list; the politeness check is named |
| `skills/verve/references/wordlist.md` | New `## Condescension` section, ungated but for the four simplification markers |
| `skills/verve/references/preferences.md` | Fifth key, and the `cut`-from-request-only rule tied to rule 1b |
| `skills/verve/SKILL.md` | Frontmatter triggers; options table row; constraint note on explicit removal; step 3 seven groups and F8 at light; step 5 two new checks; step 6 carve-out; step 7 third gate; Output block; references table |
| `skills/verve/README.md`, `README.md` | Describe the overshare check; correct the politeness description |
| `.claude-plugin/plugin.json` | Description and keywords; version 2.2.0 to 2.3.0 |
| `AGENTS.md` | A conventions bullet for group G, matching the audience guard bullet |
| `evals/corpus.toml` | A fifth case type: overshare flags without cutting, and the floor holds |

## One rule the implementation added

Writing the corpus outputs turned up a hole this document did not have. The
`Overshare (cut):` note names what was removed, and the note is part of the
output, so a note reading *"the Northwind engagement"* puts the client's name
straight back into the text the user asked to have it taken out of. The cut
becomes a relocation, and the `must_go` assertion on that case catches it.

So: **a cut line describes what went and never reproduces it.** *"The other
client and what you are doing for them"*, not the name. This does not apply to
`Overshare (not cut):`, where the text is still there and naming it is how the
writer finds it. The rule is in `overshare.md` and in the `SKILL.md` Output
section.

## Verification

`bash -n install.sh install-codex.sh`, `claude plugin validate .` and
`python3 evals/run.py --dry-run` are the static gates, and `python3
evals/mutate.py` after touching the corpus.

`references/` and `SKILL.md` both change, so **the real corpus run is
required**, not optional [from `AGENTS.md`].

The new corpus cases must assert both directions, because only one of them is
the interesting failure:

- a draft carrying an overshare comes back **with the text intact** and the
  flag raised - a case that passes by cutting has failed
- a draft whose disclosure is load-bearing comes back with **no flag** - the
  floor holding
- an explicit *"cut the oversharing"* removes it, names it, and the readback
  still passes

Worth saying as plainly as the readback document said it: the third case is the
one substring assertions can check, and the second is the one that matters
most. A green run shows the change broke nothing the harness can see. It does
not show that the floor holds.

There is a second limitation specific to this group, and it is recorded in
`corpus.toml` and `evals/README.md` as well as here. Verve's note is part of
the output, so a `must_survive` string matches whether it sits in the body or
only in the note. The assertions cannot tell those apart. The cut case is
written so the note may not echo what it removed, which catches the worst
version of the problem, but the general case needs a reader.

### The run

Done on 2026-09-11, with no API key, by the route
[`2026-09-08-fidelity-readback.md`](2026-09-08-fidelity-readback.md) used: the
thirteen rewrites were produced in an agent session against the edited skill
and graded by the same assertions.

```
python3 evals/grade.py evals/runs/2026-09-11-claude-opus-5-overshare.json
13/13 passed
```

`bash -n`, `claude plugin validate .`, `python3 evals/run.py --dry-run` and
`python3 evals/mutate.py` (8/8 automated mutations caught) all pass. The
outputs are committed so the grading can be repeated.

The same caveat as last time, and it is not a formality: the session that
produced those rewrites is the session that designed the rules they were graded
against. A green run shows the harness saw nothing break. The case for the
floor rests on the reasoning above.

## What this does not do

It does not give verve a view on whether a disclosure is wise. It reports that
one is there, on a test the user can read, and leaves the call with the person
whose reputation is attached to the text.

It does not touch length. F10 and the audience load axis already own that, and
folding volume into disclosure was considered and dropped: they pull in
different directions, one serving the reader's time and the other the writer's
interests, and a control doing both would be arguing with itself.
