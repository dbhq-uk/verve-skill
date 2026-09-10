# Evals

Verve makes claims about what it will and will not do. This measures four of
them, and it is the only thing in the repository that checks the skill rather
than describing it. Until September 2026 `AGENTS.md` named the two checks that
matter and then admitted that neither was asserted anywhere. This is that
assertion, with variety and audience added since.

The reasoning behind the corpus, and behind the variety and audience features it
checks, is recorded in
[`docs/design/2026-09-06-varieties-audience-and-evals.md`](../docs/design/2026-09-06-varieties-audience-and-evals.md).

## The first run

**9/9, on 8 September 2026, on `claude-opus-5`, once.**

Read that with its method attached, because the method is not the one `run.py`
describes.

There was no `ANTHROPIC_API_KEY` to hand, so `call_model` never ran. The nine
rewrites were produced by `claude-opus-5` in a Claude Code session, given the
system prompt `build_system_prompt()` assembles (67,526 characters) and the same
case prompts, then graded by `check()` through `grade.py`. The outputs are in
`runs/2026-09-08-claude-opus-5.json` and the grading is repeatable:

```bash
python3 evals/grade.py evals/runs/2026-09-08-claude-opus-5.json --allow-missing
```

`--allow-missing` is there because the corpus has been strengthened since that
run was recorded (2026-09-10: unlisted-content assertions, `must_match`, and a
clean-prose conversion case the run predates). The recorded outputs pass the
strengthened assertions; the flag only skips, loudly, the case that did not
exist yet. Never use it on a fresh run, where a missing case is a missing
test.

Four things about that run are worth knowing before leaning on the number.

**The assertions were withheld until after the outputs were written.** Only the
`id`, `kind`, `request` and `text` fields were read while rewriting. Had the
`must_survive` and `must_go` lists been visible first, the run would have been
teaching to the test and the result worth nothing.

**One run, not three.** `--runs 3` exists because a single pass can get lucky,
and this was a single pass.

**Nine cases in one session, not nine independent calls.** Each rewrite could
in principle have been shaped by the ones before it. The API harness does not
have that problem and this run did.

**It is one model.** Verve runs anywhere the Skills CLI reaches, and nothing
here says how it behaves on any of them.

So this is a floor under a floor: it says the instructions can produce output
that holds, not that they reliably will. The honest next step is a paid run of
`run.py --runs 3`, and the number above should be replaced by it rather than
sitting alongside it.

### What the substrings missed, and a second model caught

The day after that run, an adversarial review by a different model (Codex, read-only,
briefed to break the repository) read the nine outputs against their sources and
found that `fidelity-figures-and-names` had passed every assertion while changing
two claims. The source says Eustat *stands as a testament to the Basque Country's
commitment to independent data*; the output said it *was founded in 1989 to
produce data on the Basque Country independently*, which turns evidence of a
commitment into a founding purpose. The source says its work *underscores the
vital role that regional statistical bodies play*; the output said *its figures
are used in policy, which is the main argument for having regional statistical
bodies at all*, which is an opinion the source never offered.

Every listed figure and name survived. `max_loss` was satisfied. The check had
nothing to say, because it checks for deletion and this was distortion, exactly
as the limits section below warns. The output in `runs/` is the corrected one,
and the point of recording the original here is that it is the clearest evidence
in this repository of why a green run is not a fidelity guarantee.

Two things changed in the harness as a result. A triage case now fails if the
output contains anything beyond the input and the one permitted line, where
before it only checked that the input was present somewhere. And fidelity cases
carry `max_gain` as well as `max_loss`, because a rewrite that drops unlisted
claims and pads the result back over the length floor was passing.

## What it still does not do

**It is not wired into CI**, beyond a dry run that costs nothing. Measuring for
real needs an API key, and `SECURITY.md` makes a point of this project having no
credentials. That claim is about the skill rather than about the repository's
own CI, so it would survive a secret being added, but that is a decision to take
deliberately rather than in passing.

## Why it needs a model

There is no offline way to assert that a fact survived a rewrite. Something has
to do the rewrite. That is the whole reason verve had no tests before now, and
the reason this directory exists rather than a unit test somewhere.

## Running it

```bash
python3 evals/run.py --dry-run          # validates the corpus, calls nothing
python3 evals/mutate.py                 # checks the checker, calls nothing
pip install anthropic
export ANTHROPIC_API_KEY=...
python3 evals/run.py                    # 10 cases, one call each
python3 evals/run.py --runs 3           # repeat, report the worst result
python3 evals/run.py --only audience    # one kind
python3 evals/run.py --verbose          # print every rewrite

python3 evals/grade.py evals/runs/FILE.json   # grade outputs produced elsewhere
```

Python 3.11 or newer, for `tomllib`.

Ten cases is not a benchmark. It is a floor: the things that must not break.

## The four kinds

**triage** gives it prose that already reads as human and asserts it comes back
unchanged. A skill that always rewrites has lost the property that makes it safe
to point at anything, and the damage is invisible because the output still looks
like work.

**fidelity** gives it a passage thick with figures, names, dates and identifiers
and asserts every one survives. This is the failure that matters most, and a
wordlist edit can introduce it quietly.

**variety** asserts that an American source stays American, and that conversion
never reaches code, identifiers or proper nouns. `background-color` is not a
spelling and the World Health Organization keeps its `z`.

**audience** asserts that a gloss aimed at an expert goes and the numbers,
node count and provisioning week stay, and separately that an apology owed to
a customer survives in some wording and a *should* does not harden into a
promise. Both directions, because a guard built only against condescension
produces curtness. These cases used to assert much less than their `why`
claimed: a two-line output with no apology and no node count passed both,
which is what the 2026-09-10 strengthening and `evals/mutate.py` exist to
prevent recurring.

## How a case is written

Every case says what must be true of the output, never what the output should
be. There is no single correct rewrite, so asserting one would turn this into a
style opinion with a test runner attached.

That means the assertions are substring checks: this survived, that did not. It
is a blunt instrument, and deliberately so. A check that tried to judge whether
the prose got *better* would be a second opinion about writing, which is exactly
what verve already is.

Four things stop a blunt check being a useless one.

`must_survive` is **case-sensitive**, because constraint 2 protects exact
wording. `gateway.pool.perrequest` is a different key from
`gateway.pool.perRequest`, and a check that accepted it would assert the
opposite of the rule it exists to defend. Ordinary vocabulary goes in
`must_survive_any_case` instead, since a word legitimately changes case when a
rewrite moves it to the front of a sentence.

`must_go` is case-insensitive, because a banned phrase is banned in any casing.
Both directions err towards failing.

`must_match` holds case-insensitive regular expressions that must each match.
It is for content whose wording legitimately varies: an apology can be *sorry*
or *apologise*, *primary cluster* can be recast as *primary Redis cluster*, a
modality check wants *should* somewhere near its deadline. It is a smoke
check, not a semantic one - *"we are not sorry"* matches an apology pattern -
so the criterion it approximates stays written in the case's `why`, and a
green match is not a substitute for reading the output.

Any case that is not a triage case **fails automatically if the input comes back
whole**. Without that, a case asserting only `must_survive` passes on a verbatim
no-op: every fact trivially survives text nobody touched. That hole was real and
both fidelity cases sat in it.

`max_loss` puts a floor under how much a rewrite may cut. `must_survive` is a
whitelist, so it cannot notice content that was never listed going missing.
A case with `max_loss = 0.5` fails a rewrite that drops more than half the
words, whatever survived from the list.

### Known limits of substring checking

Negation and attribution are invisible to it. *"It is false that 83% of requests
failed"* contains `83%` and passes a case asserting that figure survived, even
though the meaning is inverted. So does a sentence that moves a number onto the
wrong subject.

Nothing in a substring harness fixes that. Catching it needs a judge reading for
meaning, which is a different tool. Treat the fidelity cases as protection
against *deletion*, not against *distortion*, and do not let a green run stand in
for reading the output.

### The mutation suite, which checks the checker

`evals/mutate.py` takes recorded outputs that pass, damages each one in a way
the corpus claims to care about - apology removed, *should* hardened to
*will*, the node count dropped, a triage passage re-cased, commentary appended
- and asserts the grader fails the damaged version with the expected failure.
Every one of those mutation classes was demonstrated to pass the harness on
2026-09-10, before the assertions they now exercise existed; the suite exists
so that cannot quietly become true again. Run it after any change to
`corpus.toml` or `run.py`. It is offline and free.

`evals/mutations.toml` also records the *semantic* mutation classes - figures
swapped between subjects, a condition inverted into a consequence - that no
substring assertion can see. `mutate.py` lists them without pretending to
check them; they are what the reading pass is for.

Each case carries a `why`. It is printed on failure, because six months from now
the useful thing is not that `fidelity-dense-technical` failed, it is what that
case was put there to protect.

## Adding one

Add a `[[case]]` to `corpus.toml`. Give it an id, a kind, the request, the text,
at least one assertion, and a `why` that says what breaks in the real world if
this case fails. Run `--dry-run` to check it loads.

Prefer a case that would have caught a bug somebody actually hit. A case that
asserts something obvious passes forever and tells you nothing.

## What it does not cover

Preferences. `run.py` sends a prompt and reads the reply, so it cannot test that
verve finds `.verve.md`, prefers the project copy over the personal one, or
declines to act on prose in a preferences file that is not one of the recognised
keys. That last one is the part worth testing, because it is the boundary that
stops a cloned repository steering the skill.

Testing it means running a real agent in a temporary directory rather than
calling the API, which is a different and larger harness. Until that exists,
those rules are checked by reading them. Do not mistake a green run for coverage
of `references/preferences.md`.

## One deliberate difference from a real session

`run.py` inlines every reference file into the system prompt. A real session
reads them on demand.

That removes retrieval as a variable, so a failure here is the instructions
failing rather than the model choosing not to open a file. It makes this a floor
rather than a simulation: passing does not prove a real session behaves the
same way, but failing proves something is wrong with the instructions
themselves.

## The question waiting on this

As of 2026-09-10 `SKILL.md` and its references come to 79,474 characters, up from 67,526 at the first run. It is not
known whether that helps or dilutes, and nobody has tested it.

Once this has a baseline, that becomes a run rather than an argument: cut the
references down, run the corpus again, compare. Related prior art is flint's
[DEPRECATED.md](https://github.com/V-Songbird/flint/blob/main/DEPRECATED.md),
which found newer models followed a 58-line style file more closely than the
148-line one it replaced.
