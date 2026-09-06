# Design: varieties, audience, and evals

Date: 2026-09-06

Three changes, shipped as a stack of five pull requests. This document records
what was decided and why, so a later reader does not have to reconstruct the
reasoning from the diffs.

## 1. English varieties

### The problem

Verve claims British English in nine places: `README.md`, `AGENTS.md`,
`CONTRIBUTING.md`, `.claude-plugin/plugin.json` (twice), `skills/verve/README.md`,
and the `SKILL.md` frontmatter and body.

It implements it in none. No reference file mentions spelling, quotation
conventions, date formats or collective nouns. The skill asserts a variety and
then leaves the model to supply what that means from its own defaults.

So this is not a matter of adding a second mode to an existing mechanism. The
mechanism does not exist. It has to be built, and then given two values.

### The decision

A third option, **Variety**, sits alongside Tone and Strength. It takes
`British` or `American`, in plain language, the same way the other two options
are given.

`references/varieties.md` holds the substance:

- Spelling families: `-ise`/`-ize`, `-our`/`-or`, `-re`/`-er`, `-ce`/`-se`,
  doubled `l` before a suffix, and the irregulars that follow none of them
- Vocabulary pairs where the other variety would read as foreign
- Quotation mark nesting, and whether the full stop sits inside or outside
- Oxford comma stance
- Date, time, and large-number formats
- Collective nouns taking a plural verb in British and a singular in American
- Stops after courtesy titles

### The default, which is the contentious part

**Match the source. Fall back to British when the source gives no signal.**

This changes the behaviour that ships today, where everything comes back
British. The reasoning:

Hard constraint 1 says every fact, number, name, date and citation survives
unchanged. Constraint 6 says that if a change would alter meaning, stop and ask.
The spirit of both is that verve does not make edits the writer did not ask for.

Silently turning an American writer's `color` into `colour` is precisely that
kind of edit. It is small, but it is unrequested, and it is the sort of thing
that makes a tool feel like it is fighting you. A British default is right for
a British house style; it is wrong as a silent transformation applied to
somebody else's finished prose.

British remains the fallback, remains the brand, and remains this repository's
own house style. Only the silent conversion goes.

### Detection

The variety of the source is read from spelling evidence first, then vocabulary,
then punctuation convention. A single `-ize` ending is not evidence: Oxford
spelling uses `-ize` in British English. Two or more independent signals
agreeing is evidence.

Where the source is genuinely mixed, British is used and the mixing is mentioned
in one line. Verve does not stop to ask, because stopping mid-run for a
cosmetic question is a worse cost than picking a fallback and saying so.

### What does not change

The em dash ban holds in both varieties. It is a rule about a machine-writing
tell, not about British punctuation, and `varieties.md` says so plainly. Chicago
style uses em dashes freely and a reader who assumes the ban is a British quirk
will remove it the first time they set the variety to American.

## 2. The audience guard

### The problem

Verve has Tone, which controls how the writing sounds, and Strength, which
controls how much of it changes. Neither says anything about who is going to
read the result.

Without that, a whole class of failure is invisible to the skill. Explaining a
term to somebody who uses it every day is rude, because it says you did not
think they would know. Leaving the same term unexplained for a newcomer is
unhelpful. The same sentence is correct in one case and insulting in the other,
and nothing in the skill currently distinguishes them.

### The decision

A fourth option, **Audience**, given in plain language: *"for our CTO"*, *"for
a customer who has just complained"*, *"for the whole company"*.

From that description the skill reads three things:

| Axis | Question | Controls |
|---|---|---|
| Expertise | Do they already know this domain? | How much explanation survives |
| Standing | Peer, senior, report, or external? | How far you may direct rather than offer |
| Load | How busy are they, how urgent is this? | Length |

Where no audience is given, it is inferred from the text: a board memo and a
tutorial carry their own evidence. Where inference fails, **assume competence**.
That is the whole principle in two words, and it is the setting least likely to
insult somebody.

### The rules

A new group **F** in `patterns.md`, with `references/audience.md` covering the
register model in full. Ten tells:

1. Defining a term the reader uses daily
2. Restating the reader's own request back at them
3. Reasons before the answer
4. Caveats nobody asked for
5. Instructing somebody who outranks you on the subject
6. Telling them what they have just told you
7. Performed empathy
8. Grovelling, which makes the reader manage your feelings
9. Overstepping: committing on somebody's behalf, or setting deadlines for
   people who do not report to you
10. Length itself, treated as a cost imposed on a busy reader

With a flat word list: *simply, just, obviously, of course, as you know,
clearly, basically, in layman's terms, don't worry, rest assured, to be clear,
I hope this makes sense, does that make sense?*

### The tension that has to be resolved in writing

Hard constraint 4 says cutting filler is the job and cutting content is not.
The audience guard asks for brevity. Left alone, those two collide, and the
guard starts deleting substance in the name of respecting the reader.

The resolution, which goes into `audience.md` in bold: **the guard removes
explanation this particular reader does not need. It never removes a fact, a
claim, or a step in the argument.** Audience decides what counts as filler.
Constraint 4 still holds the veto.

### Scoring

No seventh dimension. The existing **Trust** dimension already asks whether the
result respects the reader's intelligence, which is this question, and it is
currently scored on feel. It gets rewritten to score against group F.

## 3. Evaluation harness

### The problem

Verve makes six claims and measures none of them. `AGENTS.md` names the two
checks that matter and then admits: *"Neither is asserted anywhere."*

### The decision

A harness in `evals/`, outside `skills/`, so the CI check that keeps the skill
free of executable code still passes.

Two assertions, on a fixed corpus:

- **Triage.** A passage that already reads as human comes back unchanged.
- **Fidelity.** A passage dense with figures, names and dates keeps every one.

### What ships, and what does not

The harness ships **unrun**. Building it costs nothing and is reversible.
Running it costs money, because there is no offline way to assert that facts
survived a rewrite: it needs real model calls.

Wiring it into CI would need an API key in a repository whose `SECURITY.md`
makes a point of having none. That claim is about the skill rather than the
repository's own CI, so it would survive, but it needs a deliberate decision
and careful wording rather than a quiet commit.

Both the first run and the CI question are left to the maintainer.

Once the harness exists, the open question of whether `SKILL.md` is too long for
newer models to follow closely becomes a run rather than a code change.

## Pull request stack

Each builds on the one above it. The three features touch `SKILL.md`'s options
table and the README, so stacking avoids conflicts and keeps each diff readable.

| PR | Contents |
|---|---|
| 1 | README dogfooding, code of conduct, CONTRIBUTING measurement rule |
| 2 | Paste-in install and audit prompts |
| 3 | English varieties |
| 4 | Audience guard |
| 5 | Evaluation harness, unrun |
