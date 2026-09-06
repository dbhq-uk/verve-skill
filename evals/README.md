# Evals

Verve makes claims about what it will and will not do. This measures two of
them, and it is the first thing in the repository that checks the skill rather
than describing it.

`AGENTS.md` has named the two checks that matter for a while, and then admitted:
*"Neither is asserted anywhere."* This is that assertion.

## What it does not do yet

**It ships unrun.** No numbers from it appear in the README, and none should
until somebody has run it and can say when, on what model, and how many times.
`CONTRIBUTING.md` makes that a rule.

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
pip install anthropic
export ANTHROPIC_API_KEY=...
python3 evals/run.py                    # 9 cases, one call each
python3 evals/run.py --runs 3           # repeat, report the worst result
python3 evals/run.py --only audience    # one kind
python3 evals/run.py --verbose          # print every rewrite
```

Python 3.11 or newer, for `tomllib`.

Nine cases is not a benchmark. It is a floor: the things that must not break.

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

**audience** asserts that a gloss aimed at an expert goes and the numbers stay,
and separately that an apology owed to a customer is not cut in the name of
brevity. Both directions, because a guard built only against condescension
produces curtness.

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

The current `SKILL.md` and its references come to roughly 59,000 characters. It
is not known whether that helps or dilutes, and nobody has tested it.

Once this has a baseline, that becomes a run rather than an argument: cut the
references down, run the corpus again, compare. Related prior art is flint's
[DEPRECATED.md](https://github.com/V-Songbird/flint/blob/main/DEPRECATED.md),
which found newer models followed a 58-line style file more closely than the
148-line one it replaced.
