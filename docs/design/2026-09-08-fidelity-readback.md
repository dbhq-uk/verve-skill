# Design: fidelity becomes a readback, not a rating

Date: 2026-09-08

> **Superseded in part, 2026-09-10.** The readback described here checked that
> questions *could be answered* from the rewrite; it now builds the claim
> inventory before the rewrite exists and compares answers between source and
> rewrite, and the surrounding 1-10 scoring table it mentions has been
> replaced by two pass/fail exit gates. The reasoning below still stands; the
> mechanism has been tightened.

One change, small in the diff and load-bearing in effect. `SKILL.md` step 5 asked
the model to rate Fidelity 1-10 against the question *"Does it still say exactly
what the original said?"* It now runs a procedure and reports the result.

## The problem

Fidelity is the only dimension in the scoring table that is not a matter of
taste, and it was the only one being assessed the same way as the ones that are.

Directness, Rhythm, Voice and Density are judgements about the text in front of
you. You can read the rewrite and see them. Fidelity is not like that: it is a
claim about a relationship between two texts, one of which you are no longer
looking at. Rating it means comparing the rewrite against your memory of the
source, and memory of the source is contaminated by having just written the
rewrite.

The failure this produces is specific. A rewrite that dropped a qualifier reads
as complete. The sentence is fluent, the paragraph flows, nothing is visibly
missing, and there is no gap on the page where the lost thing was. So the honest
answer to "does it still say exactly what the original said?" is "yes, as far as
I can see" - and as far as it can see is the whole problem.

### The repository already has the evidence

This is not hypothetical here. From [`evals/README.md`](../../evals/README.md):
an adversarial review by a second model read the nine outputs of the 2026-09-08
run against their sources and found that `fidelity-figures-and-names` had passed
every assertion while changing two claims. The source said Eustat *stands as a
testament to the Basque Country's commitment to independent data*; the output
said it *was founded in 1989 to produce data on the Basque Country
independently*. Evidence of a commitment had become a founding purpose. Every
figure and every name survived.

The harness missed it because substring checks look for deletion and this was
distortion. The skill's own scoring missed it for the same reason, one level up:
nothing was gone, so nothing looked wrong.

### And the external evidence agrees

Research filed in the DBHQ repository (`docs/research/Controlled_English_Agent_Clarity_Research_20260826`)
found the same pattern measured across automatic simplification generally.
Agrawal and Carpuat (TACL 2024) evaluated systems by putting reading
comprehension questions to their outputs, and found that even the best
supervised system left at least 14% of questions unanswerable from the
simplified text. Devaraj et al. (ACL 2022) found substitution and omission
errors present in model outputs *and* in human-written gold references, and not
captured by existing metrics.

Their fix is the one adopted here: stop asking whether meaning survived and go
and check.

## The decision

Fidelity becomes its own workflow step, before scoring, and it is a procedure
rather than an impression:

1. List what constraint 1 protects in the source - every fact, number, name,
   date, citation and technical term.
2. Write five to ten questions the source answers, drawn from that list.
3. Answer each one from the rewrite alone, with the source out of view.
4. A question you cannot answer is a dropped fact, not a style call. Put it
   back.
5. Reverse the check: anything the rewrite states that the source does not is
   invention. Delete it.

Three things about that are deliberate.

**Questions rather than a diff.** A diff shows every word that changed, and
almost all of them changed legitimately, so a diff buries the one that matters.
A question the source answers and the rewrite does not is a signal with no
noise in it.

**Both directions, always.** One direction alone catches invention and misses
omission. Omission is the commoner failure and the harder one to see, because
invention at least leaves something on the page to notice. This is also the
direction the Eustat case failed in: the output added a founding purpose the
source never gave.

**Binary, not graded.** Fidelity scores 10 when every question answers and
nothing was invented, and fails otherwise. A fact is either there or it is not,
and a graded scale on a binary property invites the model to award itself an 8
and move on. The existing veto already said "below 9, revise"; this removes the
room between 9 and 10 where a judgement call used to live.

## What this does not fix

The readback catches loss and invention. It does not catch a rewrite that keeps
every fact and answers every question while shifting emphasis, because a
question about emphasis is not one the source answers cleanly enough to check.
That failure still rests on constraint 4 and on the reader.

It also costs a pass over the text that was not there before. That is the point,
and it is the cheapest possible version of the check: no tooling, no second
model, no network call, consistent with the constraint that the skill runs
entirely in the conversation.

## Changes

- `skills/verve/SKILL.md` - new step 5, fidelity readback. Scoring becomes step
  6 and drops the Fidelity row, since the readback now produces it. Step 4's
  lead-in points at the readback rather than at scoring.
- `README.md` and `skills/verve/README.md` - the workflow list gains the step.

The hard constraints are unchanged. This does not add a rule, it adds a way of
finding out whether constraint 1 was kept.

## Verification

`bash -n`, `claude plugin validate .` and `python3 evals/run.py --dry-run` all
pass.

The real run was done without an API key, so the nine rewrites were produced in
an agent session with the edited skill and graded by the same assertions:
`python3 evals/grade.py evals/runs/2026-09-08-claude-opus-5-readback.json`,
9/9. The outputs are committed so the grading can be repeated.

Worth stating plainly, in the spirit of the limits section of
[`evals/README.md`](../../evals/README.md): a green run does not show that the
readback works. The corpus asserts on substrings, and the distortion the
readback exists to catch is exactly what substrings cannot see. What the run
shows is that the change did not break anything the harness can check. The case
for the readback rests on the reasoning above, not on this run.
