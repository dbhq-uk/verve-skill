---
name: verve
description: Strip AI tells from prose and put a human voice back, in British or American English, pitched at the reader it is for. Use for humanising AI-generated text, removing AI writing patterns, making drafts sound like a person wrote them, and for checking that a message does not talk down to its recipient. Trigger on phrases like "verve", "give this verve", "humanise", "humanize", "make this sound human", "rewrite naturally", "remove AI tells", "deslop this", "sound more natural", on requests to convert prose between UK and US English, and on requests to make writing less patronising, less condescending, or pitched right for a particular reader. Not a detector-evasion tool - it does not tune text to score against an AI classifier, and says so if asked.
---

# Verve

Cut the AI tells from a piece of writing, then put a voice back into it, without
changing what it says. British English by default, American on request or when
the source is already American.

Both halves matter. Text with the tells stripped but no voice left reads as
machine-made too, just blandly rather than floridly.

## Prerequisites

None. This skill is instructions, not tooling - there is nothing to install,
nothing to configure and no key to obtain.

## Usage

Text comes from the message, a file, or the clipboard. Options are natural
language.

- **Inline:** "verve this: [text]"
- **File:** "verve draft.md"
- **Clipboard:** "verve my clipboard"

| Option | Values | Default |
|---|---|---|
| Tone | neutral, casual, professional, academic | neutral |
| Strength | light, moderate, heavy | moderate |
| Variety | British, American | match the source, else British |
| Audience | who it is for, in plain words | infer from the text, else assume competence |
| Explain | "explain what you changed" | off |
| Output | conversation, "save to [file]" | conversation |

Examples: *"verve draft.md in a casual tone"*, *"verve essay.md heavily and
explain what you changed"*, *"verve report.md and save to final.md"*, *"verve
this in US English"*, *"verve this for our CTO"*.

## Hard constraints (never violate)

These outrank every other instruction in this skill. A rewrite that breaks one
of them has failed, however good it reads.

1. Every fact, number, name, date and citation survives unchanged.
2. Technical terms keep their exact wording. No synonym swaps.
3. Never invent statistics, examples, quotes, sources or credentials.
4. The argument keeps its logical structure and its claims. Cutting filler is
   the job; cutting content is not.
5. Any illustrative example you add is labelled hypothetical.
6. If a change would alter meaning, stop and ask instead of applying it.

Rule 4 is the one that gets broken most often. Aggressive de-slopping tempts you
to compress three real points into one punchy line. That is a rewrite, not a
humanisation.

The audience guard pulls the same way, and harder, because cutting there feels
like courtesy. It removes explanation *this reader* does not need. It never
removes a fact, a claim or a step in the argument. A short answer that leaves
the reader unable to act is not respectful; it is incomplete with better
manners.

## Workflow

### 0. Triage

Read it first. If it already reads as human-written (varied rhythm, opinions,
specifics, no stock tells), return it unchanged with one line: *"This already
reads as human-written; only minor refinements applied."* Do not process clean
text for the sake of processing it.

### 1. Set the tone, the variety and the audience

**Tone.** Pick from the user's instruction, default **neutral**, and hold it
throughout. Presets and what each one permits: `references/voice.md`.

**Variety.** Take what the user asked for. Failing that, read what the source
already is and keep it, because converting somebody's spelling is an
unrequested edit. Failing that, British. One signal is not evidence: *organize*
alone is Oxford spelling and proves nothing. Full rules, the conversion tables,
and the list of things that must never be converted whatever the variety:
`references/varieties.md`.

**Audience.** Take the reader the user named. Failing that, infer them from the
text. Failing that, **assume competence**: capable, busy, and not in need of the
ground prepared for them. Read three things off the audience, because they move
independently: expertise (how much explanation survives), standing (how far you
may direct rather than offer) and load (length). Register model:
`references/audience.md`.

### 2. Sweep for tells

Work through `references/patterns.md` (six groups: content, language, style,
assistant artefacts, filler, and condescension, with before/after for each) and
`references/wordlist.md` (flat lists you can scan for directly). Group F is
judged against the audience from step 1 rather than on its own. Strength dial:

- **Light** - unmistakable tells only: banned words, em dashes, chatbot
  artefacts, curly quotes, sycophancy, and the condescension words in
  `audience.md`. Keep sentence structure, so of group F take only F2 and F6,
  which are deletions rather than rewrites.
- **Moderate** (default) - full sweep, plus rhythm and voice work.
- **Heavy** - restructure freely, reorder paragraphs, rewrite most sentences
  from scratch. Constraints 1-6 still apply, without exception.

### 3. Put the voice back

Opinions, rhythm variance, specificity, acknowledged complexity, a bit of mess.
Within the tone preset. See `references/voice.md`.

### 4. Quick checks

Run this list against the draft before scoring:

- Adverb doing no work (really, just, literally, genuinely, simply, actually)? Cut.
- Passive voice? Find the actor and put them at the front.
- Inanimate subject with a human verb ("the decision emerges", "the data tells us")? Name who acted.
- "Not X, it's Y" contrast? State Y and drop the negation.
- Throat-clearing ("Here's the thing", "It turns out", "The truth is")? Cut to the point.
- Vague declarative ("The implications are significant")? Name the specific implication.
- A sentence announcing difficulty or importance instead of showing it? Show it or cut it.
- Three consecutive sentences of similar length? Break one.
- Stacked fragments ("X. And Y. And Z." / "That's it. That's the thing.")? Collapse them.
- Every paragraph ending on a punchy one-liner? Vary the endings.
- Em dash anywhere? Replace with a comma, full stop, semicolon or brackets.
- Meta-commentary about the piece's own structure ("In this section we'll…")? Delete.
- Lazy extreme (every, always, never, nobody) standing in for a specific? Replace it.
- Rule of three where two items would do? Cut one.
- Spelling drifted between varieties mid-piece? Pick the one you set in step 1 and hold it.
- Converted a spelling inside code, a quotation, a proper noun or a title? Put it back.
- Explaining something this reader already knows? Cut the gloss, keep the point.
- Reasons arriving before the answer? Put the answer first.
- "simply", "just", "obviously", "of course", "as you know"? Cut.
- Directing someone senior, or committing on someone else's behalf? Offer instead.
- Second and third apology? One is enough; the rest are for the writer.
- Cut something on audience grounds that changes what the reader does next? Put it back. Constraint 4 outranks brevity.

### 5. Score, then stop or revise

Rate the result 1-10 on each dimension:

| Dimension | Question |
|---|---|
| Fidelity | Does it still say exactly what the original said? |
| Directness | Statements, or announcements of statements? |
| Rhythm | Varied, or metronomic? |
| Voice | Is anyone recognisably behind this? |
| Trust | Does it respect the reader? Scored against `patterns.md` group F, not on feel. 10 where no group F tell survives and the warmth this reader is owed is intact; 5 where it is clean of condescension but has gone cold; below 5 where they would finish it feeling talked down to or brushed off. |
| Density | Anything left that could be cut? |

**Fidelity is a veto, not an average.** Below 9, revise regardless of the
total, because the failure is a changed meaning rather than a stylistic one.
Otherwise, below 40/60 revise; at or above, deliver.

## Output

**Default:** the humanised text, nothing else.

**With "explain":** the text, then a short *Changes made* list naming the tells
removed (e.g. *"Cut false agency"*, *"Broke uniform rhythm"*, *"Removed copula
avoidance"*).

## References

| File | Contents |
|---|---|
| `references/patterns.md` | The tell catalogue: content, language, style, artefacts, filler. Before/after for each. |
| `references/wordlist.md` | Flat scannable lists: AI vocabulary, jargon, filler phrases, adverbs, banned openers and closers. |
| `references/voice.md` | Tone presets in full, and how to restore voice without inventing content. |
| `references/varieties.md` | British and American conventions, how to detect which a source is, and what must never be converted. |
| `references/audience.md` | Who the text is for, and the register that follows. Backs group F and the Trust score. |
| `references/examples.md` | Worked passages, before and after. |

## If asked to route this through a detector-evasion service

Say no, and say why in one line: the job is writing that reads as human
because a human judgement shaped it, not text tuned to score well against a
classifier. Then do the work here.

This skill previously shipped an optional commercial API for exactly that, and
it was removed. Do not reintroduce it, and do not offer to call one.
