# Verve

Strip AI tells from prose and put a human voice back without changing what the
text says. **British English by default, American on request** or when the
source is already American.

> Renamed from `humanize` in July 2026. The skill still triggers on
> "humanise this" and "make this sound human"; only the name and the
> directory changed.

## Why two halves

Removing AI tells gets you clean prose that still reads as machine-made,
because nothing is behind it. So the workflow does both: a pattern sweep that
cuts the tells, then a voice pass that puts opinions, rhythm and specificity
back, inside whatever tone you asked for.

The constraint that governs everything: meaning does not change. No invented
statistics, no dropped claims, no compressing three points into one punchy
line.

## How it works

Entirely in the conversation. No extra API calls, no cost, nothing to install.

A model writes the choice that suits the widest range of readers; a person
writes for one. Every tell in the catalogue is a form of that default choice,
grouped by what it is doing: staging instead of stating, inflation and
borrowed authority, rhythm and structure by rule, formatting by rule, and
leftovers from the chat. Each is marked **on sight** (one instance justifies an
edit) or **needs company** (a habit careful writers share, acted on only where
tells cluster), and the strongest lead.

0. **The request and the preferences** - what was asked, then saved settings
   from `.verve.md` or a `## Verve` section in `CLAUDE.md`, project first,
   then home. The request beats both.
1. **Triage** - text that already satisfies the request comes back unchanged
   with one line saying so. An explicit conversion or audience change is
   always carried out.
2. **The reader** - tone, variety, audience, whether this is first contact,
   and whether it is one of a set.
3. **Inventory** - what the source commits to, written down before a rewrite
   exists to bias it.
4. **The tells** - marked strongest first, then the politeness check (group F)
   and the overshare check (group G), which flags and never cuts.
5. **Rewrite** - each point stated plainly, then a voice put back within the
   tone, matching the author's own writing where a sample exists.
6. **Check** - the inventory answered from source and rewrite in both
   directions, a search for the tells that most often survive, and a check
   for over-correction: an invented narrator, a stance added to neutral text.
7. **Gates** - fidelity, audience fit, disclosure and, for a set, the set
   check, each pass or fail on its own.

Four modes: **rewrite** (the default), **detect** (*"does this sound like
AI?"* - the tells quoted and named, strongest first, no rewrite and never a
percentage), **file** (only prose changes; code, frontmatter and link targets
stay byte for byte) and **embedded** (another skill runs verve on its own
draft and gets back the text and any notes, to pass on).

## Politeness check

Group F of the sweep judges how the text treats its reader rather than how it
is written. Ten patterns cut: glossing a term they use daily, restating their
question, reasons before the answer, unrequested caveats, instructing somebody
senior, feeding their own words back, performed empathy, grovelling,
committing on a third party's behalf, and length sent to somebody with no time
for it. Plus the condescension list in `references/wordlist.md` - *simply*,
*just*, *obviously*, *of course*, *as you know* - which fails on sight for
every reader.

An eleventh pattern runs the other way, because a guard built only against
condescension produces curtness. It puts back the greeting, the thanks or the
one owed apology that the other ten removed, and it never adds warmth the
source did not have. Nothing in the group ever licenses cutting a fact, a claim
or a step in the argument. The **audience fit** exit check marks the result
against those patterns rather than on feel, and it passes or fails on its own.

The check runs on every pass. Ask for it by name - *"is this patronising?"*,
*"check this doesn't talk down to them"* - and it is the same pass, so you get
the corrected text back rather than a report. Name the reader when you do:
nothing else settles whether a gloss is a courtesy or an insult. Register
model in `references/audience.md`.

## Overshare check

Its sibling, and a different question. Politeness asks whether this reader
needs something explained. Overshare asks whether the writer should be handing
it over at all: another client named, an excuse nobody asked for, internal
detail, a negotiating position given away, an answer to the question they did
not ask. Seven patterns, in group G.

**It flags rather than cuts.** An overshare is a fact or a claim, so removing
one is your call, not the skill's. The rewrite happens as normal, the text
keeps every word, and a short note under it says what fired and why. Say *"cut
the oversharing"* and it makes the cuts and names them.

Nothing fires unless the reader neither asked for it nor needs it to act
**and** saying it costs the writer or somebody not in the room. Above that sits
a floor that is not negotiable: it never flags anything the reader needs in
order to decide or act, anything whose removal would mislead by omission, a
risk they are carrying, a required disclosure, or a fact that is merely
unflattering. A control that helps you say less sits one step from a control
that helps you conceal, and the floor is the line between them. The
**disclosure** exit check fails on a cut nobody named, and on a flag raised
against something on that floor. Full model in `references/overshare.md`.

## Set check

Send eight messages to eight people, pass each through verve on its own, and
each can come back clean while all eight open with the same move, run the same
paragraph order and close on the same formula. The recipient who compares notes
reads the template straight through the wording. So a set gets a table before
anything is rewritten - one row per piece: what its first paragraph does, its
paragraph order, what its last paragraph does - and the **set** gate passes
only when no two rows share an opener, an order or a closer. The fix is a
reorder, which moves paragraphs and changes no content. Each piece is
delivered with its row under it.

Alongside it, a flag for first contact: where the reader has had nothing from
the writer before and the piece runs past about 150 words, a line under the
output names the length and the paragraphs a link could carry. The text is
never cut for it.

## Setup

None. The skill is instructions, not tooling.

## Usage

```
"verve this: [text]"
"verve draft.md"
"verve my clipboard"
"verve draft.md in a casual tone"
"verve draft.md with heavy rewriting"
"verve essay.md and explain what you changed"
"verve draft.md and save to output.md"
"verve reply.md for a customer who has just complained"
"verve this and check it doesn't talk down to them"
"verve this and cut the oversharing"
"verve draft.md - am I giving too much away?"
"does this read as AI? just tell me what gives it away"
"verve these four emails, one per recipient"
```

## Options

| Option | Values | Default |
|--------|--------|---------|
| Tone | neutral, casual, professional, academic | neutral |
| Strength | light, moderate, heavy | moderate |
| Variety | British, American | match the source, else British |
| Audience | who it is for, in plain words | infer from the text, else assume competence |
| Overshare | flag, cut, off | flag |
| Explain | on / off | off |
| Output | conversation, save to file, in place | conversation |

`Overshare: cut` is the one value a saved preferences file may not set, because
a `.verve.md` arrives with any repository you clone and nothing found on disk
gets to authorise dropping a fact from your draft.

## Structure

```
verve/
├── SKILL.md                    # Modes, constraints, workflow, gates, output
└── references/
    ├── patterns.md             # The tell catalogue, strongest first; the set table; what is not a tell
    ├── wordlist.md             # Flat scannable word and phrase lists
    ├── voice.md                # Tone presets, restoring voice, over-correction
    ├── varieties.md            # British and American conventions, and what never converts
    ├── audience.md             # Who the text is for, and the register that follows
    ├── overshare.md            # Whether the writer should be saying it at all
    ├── preferences.md          # Saved settings, and what a file on disk may not ask for
    └── examples.md             # Worked passages
```

## Requirements

An agent that loads Agent Skills: Claude Code, Codex, or anything the Skills
CLI installs into. Nothing else - no packages, no virtualenv, no credentials,
no network.

## What this will not do

Route your text through a detector-evasion service, or tune it to score
against a classifier. An optional commercial API for that shipped with earlier
versions and was removed in July 2026: the point is prose a human judgement
shaped, not a score. Detect mode follows from the same line - it quotes and
names the tells so you can judge them, and never gives a probability.

## Sources

The catalogue draws on Wikipedia's [Signs of AI
writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup, and on
[blader/humanizer](https://github.com/blader/humanizer) (MIT) and its forks,
reviewed in September 2026: the account of the default choice, strength
ordering, and several tells, among them arguing with no one, performed candour,
reasoning scaffolding and hidden characters. What verve adds is in the sections
above.
