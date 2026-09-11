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

0. **The request and the preferences** - what was asked, then saved settings
   from `.verve.md` or a `## Verve` section in `CLAUDE.md`, project first,
   then home. The request beats both.
1. **Triage** - returns text that already satisfies the request unchanged
   rather than mangling it. An explicit conversion or audience change is
   always carried out.
2. **Tone, variety and audience** - neutral / casual / professional / academic,
   British or American, and the reader it is pitched at, all held throughout.
3. **Pattern sweep** - seven groups of tells (content, language, style,
   assistant artefacts, filler, condescension, overshare) with before/after for
   each. The last two are the politeness check and the overshare check, below.
   Every substantive cut names what goes with it first.
4. **Voice pass** - opinions, rhythm variance, specificity, within the tone,
   matching the author's own writing where a sample exists.
5. **Quick checks** - a pre-flight list run against the draft.
6. **Fidelity readback** - a claim inventory built before the rewrite,
   answered from source and rewrite and compared, in both directions.
7. **Exit checks** - fidelity, audience fit and disclosure, each pass or fail
   on its own.

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
| Output | conversation, save to file | conversation |

`Overshare: cut` is the one value a saved preferences file may not set, because
a `.verve.md` arrives with any repository you clone and nothing found on disk
gets to authorise dropping a fact from your draft.

## Structure

```
verve/
├── SKILL.md                    # Workflow, constraints, quick checks, exit gates
└── references/
    ├── patterns.md             # The tell catalogue, before/after for each
    ├── wordlist.md             # Flat scannable word and phrase lists
    ├── voice.md                # Tone presets and restoring voice
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

Route your text through a detector-evasion service. An optional commercial API
for that shipped with earlier versions and was removed in July 2026: the point
is prose a human judgement shaped, not text tuned to score well against a
classifier.
