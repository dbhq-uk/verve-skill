# Design: what three other slop tools had that verve did not

Date: 2026-11-05

Dan asked for verve to take what is worth taking from three repositories:
[ilien-dev/quiron](https://github.com/ilien-dev/quiron),
[gabelul/slopbuster](https://github.com/gabelul/slopbuster) and
[lukstei/slop-grader](https://github.com/lukstei/slop-grader). This records
what each is, what was taken, what was refused, and what the evals said. The
reading notes are in
[`docs/research/Verve_Borrowed_Evidence_20261105`](../research/Verve_Borrowed_Evidence_20261105/Verve_Borrowed_Evidence_20261105.md).

## Licences first

**Quirón is AGPL-3.0 with an attribution term** (its `NOTICE`, read at
`9bedfd5`). Verve is MIT. Copying Quirón's text, word lists or scripts would
make verve a work based on it, and the AGPL would follow. So nothing here is
copied from it. What is taken is ideas and measured findings, written fresh,
with the primary study cited where there is one, and Quirón named where the
measurement is its own.

Slopbuster (`8215cbf`) and slop-grader (`a0cdba4`) are MIT. Nothing was copied
from them either; the few rules taken are rewritten in verve's own catalogue
form.

## What each one is

**Quirón** is a humaniser skill built around measurement: a Python meter that
compares 23 rates in a text against bands from pre-2022 human posts, a pattern
checker, and a loop that runs until two clean passes in a row. Its rules carry
measured rates from its own run (167 human dev.to posts against 90 assistant
posts on the same titles, 2026) and from published studies. Its most useful
finding is a blind-judge table: rewriting every tell out of an assistant post
left judges calling it AI 12 times in 12, and adding the writer's own notes
(what happened, names, links, opinions) was the only thing that moved them.

**Slopbuster** is a prose and code humaniser skill: about 24 text patterns, an
academic ruleset, and a tiered 0 to 10 score.

**Slop-grader** is a command-line grader that asks Jev (TypeSafe's System One
model, a paid API) one typed question per rule per line of a document. It is
why Jev came up: verve never used it.

## Taken

**The Material note** (`SKILL.md`, Output). The Quirón result above, in
verve's terms. Step 3 now records whether the source has anything of the
writer's own; when it has none and the piece will go out under the writer's
name, the rewrite says so under the text and asks the questions that would fix
it. It never answers
them (constraint 3), never fires after triage, and stays silent on reference
text, so it does not become a check that speaks on every run.

**Notes beside a draft are source** (`SKILL.md`, step 3). Quirón lets the
writer's notes overrule the draft. Verve asks instead, under constraint 6,
because picking a side on a fact is a meaning change.

**The cold read** (`SKILL.md`, step 6). A fresh agent with no context reads
the finished text and quotes the three passages most likely to read as
machine-made. Quirón measured it: on 18 held-out titles, texts its Opus judges
called AI fell from 17% to 3%, and its GPT judges moved too, so it is not the
rewriter pleasing its own kind. Verve's version asks for reasons and quotes,
never Quirón's 0 to 100 probability, because detect mode refuses numbers. It
runs at heavy strength or on request only, since it costs a second agent, and
it is skipped in embedded mode. It answers the limit step 6 already admits:
the same context wrote the draft and grades it.

**Over-correction, from measurement** (`voice.md`, `SKILL.md` step 6). Three
new items. A coined saying to close a paragraph: Quirón's judges quoted
exactly those lines as their reason. Sincerity added as voice: *honestly* was
in a third of Quirón's rewrites against a few per cent of human posts, and
Anthropic's own system prompts tell Claude to avoid *genuinely* and
*honestly*. A rule pushed to zero: Quirón cites TextPulse (a vendor working
paper, not peer reviewed) for models overshooting every property a brief
named, cutting connective openers to none where people use some, while the
one property the brief did not name, vocabulary range, did not move.

**Passive voice and connectives** (`patterns.md` C10, C4). Reinhart et al.
(2025, PNAS) found models using the agentless passive at about half the human
rate, so the passive alone is weak evidence and converting every one is
over-correction. C4 now says not to take connectives to zero, and that one
carrying a cause keeps a word of the same force (constraint 4).

**C11, process nouns as subjects** (`patterns.md`). Slopbuster asserts it;
Reinhart et al. measured nominalisations at about twice the human rate. Its
worked example also shows the failed fix (*fell after* for *resulted in*),
because swapping a cause for a sequence is the commonest way this edit breaks
constraint 4.

**D8, heading density and the summary section** (`patterns.md`). Quirón
measured about twice the headings per 1,000 words in assistant posts, and a
closing *Conclusion* or *Key takeaways* section in 62% of them against 14% of
human ones. Rewrites that fix every word leave both. Merging sections moves
text and changes none of it.

**The question answered in the next breath** (`patterns.md` A4). From
slopbuster; a small extension of the setup question A4 already had.

**Ordinary words at a machine rate** (`wordlist.md`). The 2023 marker words
are rare in 2026 output; what stands out is ordinary words at several times
the human rate. Six named from Quirón's filtered count, which builds on the
LexA index (Juzek 2026) and Kobak et al. (2025), plus *substantially* for
Claude. Needs company, and stronger in detect mode than as a reason to edit.
The under-used plain words (*very, get, able*) are weak evidence for detect
mode and are never added to a rewrite.

**Fiction** (`voice.md`). Verve had nothing. Quirón found that model stories
are already choppier than human ones, so verve's own rhythm advice pushed a
story the wrong way. The section reverses it for stories and keeps the plot,
the ending and every name as content.

**Long texts a section at a time** (`SKILL.md`, step 4). Slop-grader's whole
design rests on a model skimming long documents and missing rules. Its fix is
a paid per-line API; verve's is an instruction.

**An invented-figure check in the evals** (`evals/run.py`). The idea behind
Quirón's `factdiff.py`, written fresh: any figure or link in a rewrite that
neither the text nor the request contains fails the case. It runs on every
rewrite case. Regraded over every recorded run, it fired only on detect mode
(which numbers its list of tells, so it is exempt), on triage (held to the
exact text already), and on outputs that were already failing for printing a
tool call or commentary. Two new mutations prove it catches an appended figure
and an appended link.

## Not taken

- **Quirón's meter, bands and loop.** Scripts under `skills/` are ruled out,
  and a score is what detect mode refuses.
- **Quirón's "notes win over the draft".** Verve asks; see above.
- **Quirón's fiction rules that change the story** (open the ending, break the
  template, cut half the zingers). Those edit content. Verve names them in
  detect mode and does them only when asked.
- **Quirón's review queue for negated setups.** It found that removing a
  short "X isn't Y." setup inside the loop made rewrites read more AI. One
  vendor-adjacent measurement; A1 stays as it is until verve's own evals say
  otherwise.
- **False ranges** (slopbuster). Dropped as stale on 24 Sep, following
  Wikipedia's current guide. Slopbuster asserts it without evidence, which is
  not enough to reverse a decision made on evidence. It was briefly added and
  taken out again before the eval run.
- **Slopbuster's score, its "inject personality" advice** (invented feelings,
  "let some mess in") and **"soften causal language"**. The first is a number,
  the second breaks constraint 3, the third breaks constraint 4.
- **Slop-grader's Jev provider, or any API call.** Hard constraint 3. Its
  document scores (engagement, originality, headline delivery) are scores, and
  its tech-docs rules (magic values, missing version qualifiers) are document
  quality, not AI tells.

## Two fixes the evals forced, and one old fault they found

**The Material note over-fired.** The first draft fired on "a piece that tells
or argues", and on the first batch it fired on a 32-word technical snippet
sent with nothing but *verve this:*, in all three runs, pushing that case over
its growth limit. It now fires only when the request or the text says the
piece will go out under the writer's name, and never on a snippet, a reply,
reference text or text whose purpose nobody stated.

**Printed tool calls.** The first batch printed a fake preferences check
three times in 63 calls, against about one a batch before. All three came
from step 0, not from anything added here. Step 0 now keys on having a tool
that reads files, not on whether the model believes it can, and says that a
check written out as text lands in the user's output. The next two batches
printed none, in 126 calls.

**An old swap that broke constraint 4.** The judge flagged *pivotal* rewritten
as *decisive*, and `wordlist.md` offered exactly that swap. *Decisive* claims
the thing settled the outcome; the row now offers *important, central*.

The corpus had two faults of my own, both fixed: the Material regex was
double-escaped, so it could never match and the new guard on the voice case
could never fire, and two of the new case's claims were pinned too tightly
(the source's *it* refers back to the productivity gains, so tying them to
culture is the source's claim, not an addition).

## Evals

`claude-opus-5-5` through the CLI, three runs each, against the last recorded
run (`runs/2026-09-25-claude-opus-5-5-wikipedia-tells-run*`, 20/20).

| Batch | Substring grader | Judge (Codex): kept their meaning |
|---|---|---|
| First draft (`runs/superseded/...-first-run*`) | 18, 19, 20 of 21 once the regex was fixed | not judged |
| Trigger and step 0 fixed (`runs/superseded/...-second-run*`) | 21/21 each | 16, 17, 17 of 18 |
| Final, *pivotal* fixed (`runs/2026-11-05-...-run*`) | **21/21 each** | **18, 18, 18 of 18** |

The second batch's judge misses were the *decisive* swap and the material
case's claims. One material-only judge pass on the final runs, before the
full one, flagged *embrace* becoming *commit to* in run 3; the full pass did
not. The judge varies a little between calls, as the eval README says.

Not measured: whether the Material note, the cold read or the new tells make
a rewrite read as more human. Quirón measured that on its own skill with blind
judges; verve's evals assert only that the constraints hold and the notes fire
where they should. The cold read is never exercised by the evals, because the
CLI runs have no tools.
