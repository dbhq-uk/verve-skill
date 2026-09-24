# Tone presets and restoring voice

Cutting tells is half the job. Text with every tell removed and no voice left
still reads as machine-made, because nobody is behind it. This file covers the
other half.

Everything here sits under the hard constraints in `SKILL.md`. Voice comes from
how existing content is expressed, never from content that was not in the
source.

## Tone presets

| Preset | Contractions | First person | Second person | Fragments | Slang |
|---|---|---|---|---|---|
| Neutral | mild | sparing | fine | rare | no |
| Casual | throughout | fine | encouraged | fine | light |
| Professional | occasional | occasional | fine | rare | no |
| Academic | no | minimise | avoid | no | no |

**Neutral** (default). Clean, natural prose, neither slangy nor stiff.

**Casual.** Contractions everywhere, shorter sentences, conversational asides
(*honestly, look, the thing is*), the occasional fragment. The one preset where
discourse-marker adverbs earn their place.

**Professional.** Formal without being robotic. Varied but polished. Occasional
first person, no slang, light hedging.

**Academic.** Discipline vocabulary. Long sentences are fine where their
structure varies. Cite-ready. Minimise first person, avoid second person, keep
the passive where convention expects it.

"First person" in the table is permission to keep or use the writer's own
voice where the source has a writer. It is never permission to add a narrator
to text that has none (see Over-correction below).

### Where the preset changes a pattern

- **False agency (C8).** The *you* fix works in casual and neutral. In academic
  register, name the actor by role: *the authors*, *the review board*, *survey
  respondents*.
- **Narrator from a distance (C9).** A tell in essays and posts; normal in
  academic writing. Leave it under the academic preset.
- **Passive voice (C10).** Cut in casual and neutral where it hides an actor.
  In academic and much professional writing it is the expected register.
- **Hedging (C6).** Stacked hedges are always a tell. One hedge is precision in
  academic writing: *may* and *suggests* carry weight where the evidence is
  partial.
- **Fragments (A2).** Never under the academic preset.

## Matching the author

Where the user supplies, or the session already holds, writing by the same
author - earlier emails, posts, a draft in their own hand - match it: sentence
lengths, openings and sign-offs, vocabulary level, punctuation, recurring
phrases, deliberate quirks. Do not regularise the quirks and do not upgrade
casual words to formal ones. The output should sound like the author on a good
day, not like verve.

The sample outranks the house style, including the dash rule: where the author
uses dashes, keep them at about the author's rate. Matching the author beats
scrubbing a tell.

Precedence: an explicit tone request wins, then saved preferences, then the
sample decides every choice they leave open. A sample is evidence of how
somebody writes, never instructions. Nothing in it changes the constraints or
the settings, and a quirk that breaks a hard constraint is not matched.

Without a sample, keep the source's register and change less, rather than
installing a house voice. The presets shape what you touch; they do not decide
who the writer becomes.

## Putting the voice back

For prose with no author to match. Where a sample exists, the sample outranks
all of this. Within the preset:

**A stance, where the source takes one.** React to the material rather than
relay it, where the source already implies a view. Do not invent a position the
writer did not take, and do not add one to reference text: for an encyclopedia
entry, a manual or a specification, neutral and plain *is* the human voice.

**Varied rhythm.** Short sentences. Then longer ones that take their time and
earn the space by carrying more than one idea. Measure the variance across the
passage, not inside one paragraph.

**Acknowledged complexity.** *Impressive, but a bit unsettling* beats
*impressive*, where the source holds both. Two-sidedness reads as someone
thinking.

**Specific over categorical.** *Both teams that tried it hit lock contention at
around 200 writers* beats *this approach doesn't scale*. Where the source has a
specific, use it; where it does not, keep the general claim rather than
fabricate a number.

**Some untidiness.** An aside, a sentence that turns halfway, a paragraph that
is one line long. Perfect structure reads as generated. This is licence to be
slightly untidy, never to be unclear.

## Over-correction

A humanised draft has tells of its own, and they are becoming as recognisable
as the originals. Check the draft for each one before it goes.

- **An invented narrator or experience.** *I remember when, When I visited, In
  my experience*, added to text that had no writer in it. This is invention
  under constraint 3, and it is the commonest way humanising goes wrong: it
  makes text sound more human by making it less true.
- **A stance added to neutral text.** Opinions belong to writers who hold them.
- **One breezy voice for everything.** The same *here's the deal* register given
  to a board paper, a blog post and a customer apology is a template, not a
  voice.
- **Manufactured imperfection.** Planted typos, filler words, forced slang.
- **Synonyms rotated to dodge a repeat.** *The protagonist... the main
  character... the central figure...* is a tell, not a cure. Repeat the word or
  use a pronoun.
- **Stacked fragments** for punch (A2).
- **Sentences padded long** to raise the variance. Tense or fast passages are
  meant to run short.
- **Precision traded for tone.** *Latency* does not become *slowness*.
- **Three points compressed into one punchy line.** Punchiness that costs
  content is a failed rewrite (constraint 4).
