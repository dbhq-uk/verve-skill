<div align="center">

<img src="assets/logo.svg" alt="verve skill for Claude Code, by DBHQ" width="420">

# verve

**Is anyone recognisably behind this writing?**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-blueviolet)](https://code.claude.com/docs/en/plugins)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-lightgrey)]()

A free, open-source tool by [DBHQ](https://dbhq.uk)

</div>

---

verve cuts the AI tells out of a piece of writing and puts a voice back into it, without changing what it says. **British English by default, American on request** or when the draft is already American.

## What it looks like

A model writes the most likely next sentence, which is the one that suits the widest range of readers and subjects at once. A person writes for one reader and one subject. Every tell verve hunts is a version of that difference, and the voice pass is what puts the one reader back.

**Before** (70 words)

> Here's the thing: in today's fast-paced engineering landscape, code review isn't just a quality gate — it's a cultural artefact. What makes it hard is that the feedback becomes a signal about the team itself. Let that sink in. Teams that delve into review culture find that it fosters trust, improves velocity and builds shared ownership. The implications are significant. Not because the tooling is complex. Because people are complex.

**After** (61 words)

> Code review is a quality gate, but it is also part of a team's culture, and that is the hard part: feedback on the code reads as a signal about the team itself. Teams that work at their review culture find it builds trust, speeds them up and spreads ownership. None of that is because the tooling is complex. People are.

Nine words shorter, all seven of the original's claims survive, and nothing appears in the after that the before does not carry. Out came the throat-clearing opener, *in today's*, *landscape*, *delve*, *fosters*, the em dash, *let that sink in*, and the not-X-but-Y contrast at both ends.

Five more, including the failure mode where a rewrite cuts content along with the filler, are in [`references/examples.md`](skills/verve/references/examples.md).

## What makes it different

**It does both halves.** Most de-slopping tools only subtract. Strip the tells and stop, and you get clean prose that still reads as machine-made - just blandly rather than floridly, because nothing is behind it. So the pattern sweep is followed by a voice pass: opinions, rhythm variance, specificity, acknowledged complexity, a bit of mess.

Meaning holds the veto. Every fact, number, name, date and citation survives unchanged; technical terms keep their exact wording; nothing is invented. Before delivery the rewrite passes three gates, each pass or fail on its own: a fidelity readback in both directions, an audience-fit check, and a disclosure check. There is no total for good rhythm to buy a changed meaning back with. Aggressive rewriting tempts a model to compress three real points into one punchy line. That is the failure this guards against.

**It knows who the writing is for.** Explaining a term to someone who uses it daily is rude, because it says you did not think they would know. Leaving it unexplained for a newcomer is unhelpful. Same sentence, different reader, and nothing but the reader can settle it. So verve takes an audience in plain words (*"for our CTO"*, *"for a customer who has just complained"*) and reads three things off it: how much explanation survives, how far you may direct rather than offer, and how long the thing should be. Say nothing and it infers the reader from the text, then falls back to assuming competence.

**There is a politeness check, and it runs both ways.** Ten patterns are judged against that reader on every pass: glossing a term they use daily, restating their question, reasons before the answer, caveats nobody asked for, instructions aimed at somebody senior, feeding their own words back, performed empathy, the second and third apology, committing on a third party's behalf, and length sent to somebody with no time to read it. With them goes a list that fails on sight for every reader: *simply*, *just*, *obviously*, *of course*, *as you know*. An eleventh pattern runs the other way, because a guard built only against condescension turns everything curt - it puts back the greeting, the thanks or the one owed apology that the other ten took out, and it never adds warmth the source did not have. None of it ever licenses cutting a fact. The result is the **audience fit** gate, marked against those patterns rather than on feel: it passes only where no condescension pattern survives and the warmth this reader is owed is intact, and it fails where the reader would finish feeling either talked down to or brushed off.

**And a second check, asking the opposite question: are you giving too much away?** Politeness asks whether the reader needs something explained. Overshare asks whether you should be handing it over at all - another client named, an excuse nobody asked for, which of your systems fell over, a negotiating position volunteered, an answer to the question they did not ask. Seven patterns, and it **flags rather than cuts**, because an overshare is a fact and removing a fact from your draft is your call, not the tool's. The text comes back whole with a short note under it saying what fired and why; say *"cut the oversharing"* and it makes the cuts and names each one. Nothing fires unless the reader neither asked for it nor needs it to act *and* saying it costs you or somebody not in the room. Above that sits a floor that does not move: it never flags anything the reader needs in order to decide or act, anything whose removal would mislead by omission, a risk they are carrying, a disclosure a contract or a regulator requires, or a fact that is merely unflattering - because being wrong is not oversharing. A control that helps you say less sits one step from a control that helps you conceal, and that floor is the line between them.

Triage comes early, and leaving your text alone is a valid result. Writing that already satisfies the request comes back unchanged, with one line saying so - though an explicit ask, a variety conversion or an audience change, is always carried out however clean the prose is. A tool that processes clean prose for the sake of processing it makes writing worse.

**Nothing to pay, and nothing held back.** The whole skill is the conversation itself - no API key, no per-word billing, no network round trip, no paid tier holding the good half back. Earlier versions shipped an optional commercial detector-evasion API. It was removed in July 2026: writing that reads as human should come from a judgement about the writing, not from a service that tunes text to score against a classifier.

**British English by default, and it will not quietly convert yours.** If you write for a UK audience and are tired of drafts drifting into American spelling, that is the default and it holds throughout. Ask for American and you get American. Hand it a draft that is already American and it keeps it that way, because silently turning somebody's `color` into `colour` is the sort of unrequested edit verve exists to avoid.

## Install

### As a Claude Code plugin (recommended)

```
/plugin marketplace add dbhq-uk/marketplace
/plugin install verve@dbhq
```

### Any agent (Cursor, Copilot, Windsurf, Gemini, Cline and more)

```bash
npx skills add dbhq-uk/verve-skill
```

The [skills.sh](https://skills.sh) CLI installs into whichever agent directories it finds, so this works outside Claude Code and Codex too.

### Local install (Claude Code or Codex)

```bash
git clone https://github.com/dbhq-uk/verve-skill.git
cd verve-skill
./install.sh          # Claude Code: symlinks into ~/.claude/skills (edits are live)
./install-codex.sh    # Codex: installs into ~/.codex/skills
```

[`install.sh`](install.sh) and [`install-codex.sh`](install-codex.sh) are the same install two ways. `SKILL.md` names its references by relative path, so nothing needs rewriting: the Claude Code installer symlinks the whole skill directory and every edit is live, while the Codex installer copies `SKILL.md` and symlinks `references/`, so re-run it after editing `SKILL.md`. Neither will delete a `verve` directory it did not create.

### Let the agent do it

For an agent none of the above covers, paste [`prompts/install.md`](prompts/install.md) into a session. It finds the skills directory, fetches the eight files, puts them in the right layout and asks before overwriting anything already there.

**Nothing to install beyond that.** No packages, no virtualenv, no credentials, no network. The skill is instructions and reference material, not tooling.

## Usage

Ask in any session. Text comes from the message, a file, or the clipboard, and the options are plain language.

```
"verve this: [text]"
"verve draft.md"
"verve my clipboard"
"verve draft.md in a casual tone"
"verve draft.md with heavy rewriting"
"verve essay.md and explain what you changed"
"verve draft.md and save to output.md"
"verve draft.md in US English"
"verve this for our CTO, she has two minutes"
"verve reply.md for a customer who has just complained"
"verve this and check it doesn't talk down to them"
"verve draft.md - am I giving too much away?"
"verve this and cut the oversharing"
```

| Option | Values | Default |
|---|---|---|
| Tone | neutral, casual, professional, academic | neutral |
| Strength | light, moderate, heavy | moderate |
| Variety | British, American | match the source, else British |
| Audience | who it is for, in plain words | infer from the text, else assume competence |
| Overshare | flag, cut, off | flag |
| Explain | on / off | off |
| Output | conversation, save to file | conversation |

**Set them once instead of repeating them.** Put a `.verve.md` in your project, or a `## Verve` section in the `CLAUDE.md` you already have:

```markdown
# Verve

Variety: British
Tone: professional
Audience: engineers on my own team, who know the stack

## Never change
- serialize, normalize, tokenizer
- Ministry of Defence
```

verve looks in the project first, then your home directory, and the request still beats both. **Never change** is the part worth having: it is the fidelity constraint made extensible, so the house spellings and product names a rewrite keeps getting wrong survive every pass. Full rules, including what a file on disk is *not* allowed to ask for, in [`references/preferences.md`](skills/verve/references/preferences.md).

**Audience** is the other one to know. Give it a reader and verve cuts what that reader does not need: glosses on terms they use daily, the ask restated back at them, reasons before the answer, caveats nobody requested, instructions aimed at someone senior, performed empathy, and the second and third apology. It works the other way too, because brevity is not bluntness. A one-line reply to a customer who has lost money reads as contempt however efficient it is, so the greeting, the thanks and one genuine apology stay. What it never cuts is a fact, a claim or a step in the argument, whatever the reader knows.

That is the politeness check, and it runs on every pass whether you ask for it or not. Ask for it by name - *"is this patronising?"*, *"check this doesn't talk down to them"* - and it is the same pass, so what comes back is the corrected text rather than a report. Name the reader when you do, because nothing else settles whether a gloss is a courtesy or an insult. The register model behind it, and the two tests applied before anything is cut on audience grounds, are in [`references/audience.md`](skills/verve/references/audience.md).

**Overshare** is its sibling, and the only setting that leaves your text alone by design. It runs on every pass too, names what you are giving away that nobody asked for, and changes nothing until you say *"cut the oversharing"*. Set it to `off` in a project where it does not earn its place. `cut` is the one value a saved file may **not** set: a `.verve.md` arrives with any repository you clone, and nothing found on disk gets to authorise dropping a fact from your draft. The two tests, the floor and the patterns are in [`references/overshare.md`](skills/verve/references/overshare.md).

**Variety** picks the English. Ask for it by name and that settles it. Say nothing and verve reads what the draft already is and keeps it, falling back to British when the draft gives no signal either way. Code, quotations, proper nouns, titles and standards text are never converted whichever variety you choose: `background-color` stays `background-color`, and the World Health Organization keeps its `z`.

**Strength** is the dial worth knowing. *Light* touches only the unmistakable tells - banned words, em dashes, chatbot artefacts, sycophancy - and leaves sentence structure alone. *Moderate*, the default, adds rhythm and voice work. *Heavy* restructures freely and rewrites most sentences from scratch. The meaning constraints hold at every level, without exception.

## How it works

0. **The request and the preferences** - what was asked, then saved settings and never-change terms, project first, then home
1. **Triage** - text that already satisfies the request is returned unchanged rather than mangled; an explicit conversion or audience change is always carried out
2. **Tone, variety and audience** - one of four tone presets, British or American, and the reader it is pitched at, all held throughout
3. **Pattern sweep** - seven groups of tells (content, language, style, assistant artefacts, filler, condescension, overshare), each with before/after. The condescension group is the politeness check, judged against the reader set in step 2 rather than on its own; the overshare group is the disclosure check, and it flags rather than cuts. Every substantive cut names what goes with it before it is made
4. **Voice pass** - put opinions, rhythm and specificity back, inside the tone, matching the author's own writing where a sample exists
5. **Quick checks** - a pre-flight list run against the draft
6. **Fidelity readback** - a claim inventory built before the rewrite, answered from source and rewrite and compared, in both directions
7. **Exit checks** - fidelity, audience fit and disclosure, each pass or fail on its own, no total to trade against

## Audit a whole repository

The skill rewrites one piece at a time. To find out which pieces are worth rewriting, paste [`prompts/audit.md`](prompts/audit.md) into a session sitting in any repository.

It is read-only by design. It works out which files are actually prose, sets aside the licences and generated references and the specimens quoted as evidence, scores what is left by tells per hundred words, and hands back a table ordered worst first, plus the files it thinks you should leave alone. Nothing is rewritten. You decide what gets a run.

## What this will not do

Route your text through a detector-evasion service. Verve shipped with an optional [Undetectable AI](https://undetectable.ai) engine until July 2026, and it was removed rather than kept as a switch nobody had to flip.

It contradicted the free, read-every-line argument the rest of the skill is built on. It also aimed at the wrong target. A classifier score is not the goal; prose a person would be happy to put their name to is. Those two come apart the moment you optimise for the score, and when they do the score wins and the writing loses.

## Development

Want to hack on the skill or run it from source with live edits? See [`docs/dev-setup.md`](docs/dev-setup.md).

[`CONTRIBUTING.md`](CONTRIBUTING.md) covers working on it, and [`AGENTS.md`](AGENTS.md) is for an AI agent doing so. The skill itself is [`skills/verve/SKILL.md`](skills/verve/SKILL.md).

[`evals/`](evals/) holds a fixed corpus that checks the skill rather than describing it: triage leaves human prose alone, every figure and identifier survives a rewrite, a variety conversion never reaches code or proper nouns, and the audience guard cuts the gloss without cutting the apology. The assertions are substring and pattern checks - they catch deletion, not distortion, and a green run is not a substitute for reading the output. A mutation suite ([`evals/mutate.py`](evals/mutate.py)) checks the checker: damaged outputs must fail, and every damage class it applies once passed the harness undetected. Run both after changing anything under `skills/`.

It has been run once: **9/9, on 8 September 2026, on `claude-opus-5`**, against the corpus as it stood that day; the corpus has been strengthened since and the recorded outputs pass the stronger assertions too. That number comes with conditions worth reading before you trust it - one run rather than three, one model, and produced in an agent session rather than through the API harness, though graded by the same assertions. [`evals/README.md`](evals/README.md) states all of it, and the outputs are committed in [`evals/runs/`](evals/runs/) so the grading can be repeated.

## History

Renamed from `humanize` in July 2026. The skill still triggers on *"humanise this"* and *"make this sound human"*; only the name and the directory changed.

## Licence

[MIT](LICENSE) © 2026 DBHQ Consulting Ltd
