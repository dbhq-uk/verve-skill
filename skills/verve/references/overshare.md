# Overshare and disclosure

The audience guard asks whether this reader needs something explained. This
file asks a different question: whether the writer should be handing it over at
all.

They are not the same judgement. One is about respecting the reader, the other
about protecting the writer and whoever is not in the room. A draft can be
pitched perfectly, carry no condescension, survive every other check, and still
name another client's rate, give an excuse nobody asked for, or hand over a
negotiating position for free.

Length has nothing to do with it. F10 already covers a long message sent to a
busy reader; a one-line email can overshare.

## The two tests

Nothing is flagged unless **both** are true.

1. **They did not ask for it and do not need it to act.** If the reader asked,
   or if they need it to decide or to do something, it stays and nothing fires.
   This is the F4 caveat test run the other way round: there, a qualification
   survives if it gives the reader something to act on; here, a disclosure
   survives on the same ground.
2. **Saying it costs the writer, or somebody not in the room.** Credibility,
   negotiating position, a confidence, another person's privacy. If nothing is
   lost, it is an incidental detail, not an overshare.

Either test on its own produces noise. Test 1 alone flags every fact the reader
did not strictly require, which is most of what makes a message readable. Test
2 alone flags anything unflattering. Together they catch the thing the writer
did not notice writing.

## The floor, which is not negotiable

The check never flags:

- anything the reader needs in order to decide or act
- anything whose removal would mislead by omission
- a risk, a delay or a cost the reader is carrying
- a conflict of interest, or a disclosure a contract or a regulator requires
- a fact that is merely unflattering, because being wrong is not oversharing

One test sits behind all five: **would the reader act differently if they
knew?** If yes it is information, not an overshare, and the flag does not fire.

This is written down because the failure mode is obvious and severe. A control
that helps somebody say less sits one step from a control that helps them
conceal, and the only thing between the two is a line somebody drew on purpose.
Flagging a real risk teaches the writer to bury it, which is worse than not
having the check at all.

Hard constraint 4 backs the floor: the argument keeps its claims. Where the
floor and a pattern in group G disagree, the floor wins, every time.

## Flag, not cut

An overshare is a fact (constraint 1) or a claim (constraint 4). Removing one
is not verve's call.

**Verve never decides on its own to remove content. The user can.**

So the default is `flag`. The rewrite happens as normal, the overshare stays in
the text, and the output carries a short note naming what fired and why. An
explicit instruction in the request - *"cut the oversharing"* - makes the cuts
instead, and names each one.

That holds the constraint rather than carving a hole in it. The constraints
outrank every other instruction in the skill, and a user telling verve to
remove a sentence from their own draft is not an instruction inside the skill.
It is an edit they made.

Nothing found on disk can give that instruction. See `preferences.md`: a
`.verve.md` may set `flag` or `off`, never `cut`.

## When each pattern fires

Group F splits on whether a pattern needs a reader, and group G splits the same
way. Both tests above gate every pattern regardless: *fires on
sight* means the pattern needs no reading of the audience, not that it skips
the tests. A personal circumstance offered to somebody who has just asked after
you fails test 1, and nothing fires.

**On sight, for any reader:** G1 third-party disclosure, G2 personal
circumstances. Neither depends on who is reading, because neither is the
reader's to receive.

**Only where the reader is known, or the text is plainly outward-facing:** G3
unasked-for reasons, G4 internal detail, G5 position leakage, G6
over-answering, G7 pre-emptive confession. Each of these is fine in one
direction and costly in another. Telling a colleague on your own team which
server fell over is how work gets done; telling the client is G4.

Where no reader is known and the text gives no signal either way, the five
reader-dependent patterns stay silent. That mirrors the rule `audience.md`
already applies to F1: no reader, no confidence, no call.

An email, a letter, a proposal, a client note or anything with a salutation
addressed outside the writer's own organisation counts as plainly
outward-facing without being told.

## What the note looks like

Under the rewritten text, and only where something fired:

```
Overshare (not cut):
- You give the reason you missed Friday. He asked for the date, not the why.
- Paragraph 3 names the other client's rate.
```

One line each: what it is, and why it fired. Name the thing in the writer's own
terms rather than citing a pattern number at them.

Nothing fires, nothing is said. That is the rule the preferences lookup already
follows for a file that is not there, and it matters more here: a check that
speaks on every run gets ignored within a week, and then it is not a check.

Where the request asked for cuts, the heading is `Overshare (cut):` and the
same lines describe what was removed.

**A cut line describes what went; it never reproduces it.** *"The other client
and what you are doing for them"*, not *"the Northwind engagement"*. The note
is part of the output, so quoting the removed words back puts them straight
into the thing the user asked you to take them out of, and the cut becomes a
relocation. Name the shape, not the content.

This does not apply to `Overshare (not cut):`, where the text is still there
and naming it is how the writer finds it.

## The exit gate

The **Disclosure** gate in `SKILL.md` step 7 checks this, pass or fail on its
own like the other two.

It passes when every candidate is either left in place and listed, or removed
under an explicit request and named.

It fails when anything was removed without being named, and it fails when
something on the floor list was flagged. The second failure is the one to
watch, because it is the one that does damage: the first costs the writer a
sentence they wanted, the second costs the reader something they needed.
