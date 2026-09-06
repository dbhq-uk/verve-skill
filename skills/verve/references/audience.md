# Audience and register

Tone controls how the writing sounds. Strength controls how much of it changes.
Neither says anything about who is going to read it, and without that a whole
class of failure is invisible.

Explaining a term to somebody who uses it every day is rude, because it says you
did not think they would know. Leaving the same term unexplained for a newcomer
is unhelpful. The sentence is identical in both cases. Only the reader differs,
so only the reader can settle it.

## The principle

**Assume competence, not knowledge.** Where you know nothing else about the
reader, write for somebody capable and busy. That is the setting least likely to
insult anybody, and the one a reader is most likely to forgive when it is wrong.

Competence and subject knowledge are different things, and only the second
licenses cutting an explanation. A reader can be entirely capable and still not
know your system. So an unknown reader means:

- **Cut** F2, F6, F7, F8 and F10. None of those depend on what the reader knows.
  Restating their question, feeding their own words back, performing empathy,
  grovelling and padding are rude to everybody.
- **Keep** F1. You cannot tell whether a gloss is redundant without knowing
  whether they already have the term, and a definition somebody did not need
  costs them a sentence, where one they did need and did not get costs them the
  point.
- **Soften rather than cut** F5 and F9. Offer instead of directing, and do not
  commit on anyone's behalf. Both are right whoever is reading.

Once you do know the reader, F1 comes back into scope and the axes below decide
the rest.

## Reading the audience

The user describes the reader in plain language: *"for our CTO"*, *"for a
customer who has just complained"*, *"for the whole company"*, *"for someone who
has never used the product"*. From that, read three things.

| Axis | Question | What it controls |
|---|---|---|
| Expertise | Do they already know this subject? | How much explanation survives |
| Standing | Peer, senior, report, or external? | How far you may direct rather than offer |
| Load | How busy are they, how urgent is this? | Length |

They move independently, which is the point of keeping them apart. A chief
executive is high standing and high load but may have low expertise in the
specific subject: explain the domain, keep it short, and do not tell them what
to do. A junior engineer on your own team is the reverse on two of the three.

### When no audience is given

Infer it from the text. A board memo, a customer apology, a tutorial and an
internal postmortem all carry evidence of who they are for: the salutation, the
vocabulary, the amount of context assumed, what is being asked of the reader.

Where inference fails, assume competence, as above. Do not stop and ask. A
question about the reader is worth asking only when the text could not be
delivered at all without the answer, which is rare.

## What the guard removes

The ten patterns in `patterns.md` group F, judged against the audience you have
just read:

F1 explaining known terms, F2 restating the ask, F3 reasons before the answer,
F4 unrequested caveats, F5 instructing upwards, F6 telling them what they told
you, F7 performed empathy, F8 grovelling, F9 overreach, F10 length as an
imposition.

Plus these, on sight, wherever the reader has any expertise in the subject:

- simply, just, obviously, of course, clearly, naturally
- as you know, as you are aware, as I am sure you know
- basically, essentially, in layman's terms, to put it simply
- don't worry, rest assured, no need to panic
- to be clear, let me explain, let me walk you through
- I hope this makes sense, does that make sense?, hope this helps

*As you know* deserves its own note, because it fails in both directions at
once. If they do know, you have wasted their time saying so. If they do not, you
have told them they should have. There is no reader for whom it works.

## The boundary, which is not negotiable

**The guard removes explanation this reader does not need. It never removes a
fact, a claim, or a step in the argument.**

Hard constraint 4 still holds the veto. Audience decides what counts as filler;
it does not license cutting content. The failure to watch for is a rewrite that
drops a caveat which was load-bearing, or a step the reader genuinely needed,
and calls the result respectful. That is not brevity. It is an incomplete
answer with better manners.

Two tests before cutting on audience grounds:

1. Would this reader already know it? If you cannot say yes with confidence,
   keep it. This is why an unknown reader does not license cutting an
   explanation: no reader, no confidence, no cut.
2. Does removing it change what the reader would do next? If yes, keep it,
   however obvious it looks.

A caveat that names a real risk is content. A caveat that protects the writer is
F4. The test is whether it gives the reader something to act on: a condition
they could meet, a consequence they could avoid, or a limit they could work
inside. *"Results may vary depending on your configuration"* names no condition
and no consequence, so it is F4. *"This drops the table, so take a dump first"*
names both, so it stays.

## Politeness fails in two directions

The obvious failure is condescension. The other one is curtness, and a guard
built only against the first will produce it.

Brevity is not bluntness. Cutting the explanation a reader does not need is
courtesy; cutting the greeting, the thanks, or the acknowledgement that somebody
has been inconvenienced is not concision, it is coldness. A one-line reply to a
customer who has lost money reads as contempt however efficient it is.

So:

- Keep the salutation, the sign-off and the thanks. They cost a line and they
  are what makes the rest readable as a message from a person.
- Keep one apology where one is owed. Cut the second and third (F8).
- Keep acknowledgement of a real cost to the reader, once, in plain words, and
  then move to what you are doing about it. Cutting it entirely is F7's failure
  from the other side.
- Softening a refusal is not hedging. *We cannot do that* and *I am afraid we
  cannot do that* carry the same information; the second is not weaker, it is
  addressed to a person.

Where standing runs upwards or the reader is external, the balance shifts
towards warmth. Where it runs to a peer on your own team, it shifts towards
brevity. Neither ever licenses removing information.

## Length

Treat length as something the writer spends on the reader's behalf. That framing
settles most cases without a rule.

It is not a word count. Two thousand words to a reviewer who asked for detail is
correct. Two hundred to a director who asked one question is not. The measure is
whether every part is doing work *for this reader*.

Where the detail is real but this reader does not need it, the answer is to put
it somewhere they can reach rather than to delete it. A short reply that names
the file holding the long version respects the reader twice: once by being
short, and once by not throwing the work away.

## Interaction with the tone presets

The audience sets the register; the tone preset sets the surface. They are
compatible, and where they appear to conflict the audience wins on substance and
the preset wins on style.

- **Academic** keeps its hedges. A single hedge is precision there, not F4. The
  guard still cuts F1, F2, F6 and F10.
- **Casual** may keep its discourse markers (*honestly*, *look*), and they are
  not F-group tells. It does not license *obviously* or *of course*, which are
  about the reader rather than the speaker.
- **Professional** is where grovelling most often survives a rewrite, because it
  reads as courtesy. Apply F8 anyway.
- **Neutral** takes the guard as written.

## Scoring

The **Trust** dimension in `SKILL.md` scores this. It asks whether the result
respects the reader's intelligence, which is the question this file answers, and
it is scored against group F rather than on feel.

Score 10 where nothing in group F survives and the warmth appropriate to the
reader is intact. Score 5 where the text is clean of condescension but has gone
cold. Score below 5 where a reader would finish it feeling either talked down to
or brushed off.
