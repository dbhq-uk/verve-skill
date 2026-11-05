# What quiron, slopbuster and slop-grader have that verve does not

Date: 2026-11-05. Level: standard. Decision record: [`docs/design/2026-11-05-measured-evidence.md`](../../design/2026-11-05-measured-evidence.md).

## Sources read

| Repository | Commit | Licence | What was read |
|---|---|---|---|
| [ilien-dev/quiron](https://github.com/ilien-dev/quiron) | `9bedfd5` | AGPL-3.0-only plus a 7(b) attribution term (`NOTICE`) | `README.md`, `SKILL.md`, `references/patterns.md`, `word-choice.md`, `fiction.md`, `sources.md`, parts of `numbers.md` |
| [gabelul/slopbuster](https://github.com/gabelul/slopbuster) | `8215cbf` | MIT | `README.md`, `SKILL.md`, `scoring.md`, `rules/text-*.md`, `rules/academic.md`, `guides/*.md`; code rules skimmed |
| [lukstei/slop-grader](https://github.com/lukstei/slop-grader) | `a0cdba4` | MIT | `README.md`, `rules/no-ai-slop.md`, `rules/article-scores.md`, `rules/tech-docs.md` headings |

Because of Quirón's licence, no text, word list or code from it is reproduced here or in the skill. Findings are restated, with the primary study named where Quirón cites one.

## Quirón: findings that bear on verve

How well each is supported: **published** means a peer-reviewed study Quirón cites; **Quirón-measured** means its own run on 167 human dev.to posts and 90 assistant posts on the same titles (2026), with blind Claude and GPT judges; **vendor** means TextPulse working papers, self-published and not peer reviewed.

| Finding | Support | Verve before | Taken |
|---|---|---|---|
| Rewriting every tell out of an assistant post left blind judges calling it AI 12 of 12; adding the writer's own notes brought it to 3 of 12 | Quirón-measured, one round on 12 titles, later rounds weaker (18 of 32 still judged AI) | Nothing on asking for the writer's material | Material note |
| A fresh-context cold read, acted on once, cut texts judged AI from 17% to 3% on 18 held-out titles; GPT judges moved too | Quirón-measured | Step 6 admitted the self-grading limit, no remedy | Cold read, reasons only, heavy or on request |
| Models told what humans do overshoot every named property; the unnamed one (vocabulary range) does not move | Vendor (TextPulse) and published (Reinhart et al. 2025, PNAS) | Over-correction list without this | Over-correction items |
| Models use the agentless passive at about half the human rate; nominalisations about 2x; participial clauses about 5x | Published (Reinhart et al. 2025) | C10 cut passive in casual and neutral; B3 covered riders | C10 evidence, C11 |
| Assistant posts: about 2x headings per 1,000 words; closing summary section in 62% against 14% | Quirón-measured | D6 stock headings only | D8 |
| *honestly* in 33% of Quirón's rewrites against 2% to 5% of human posts; Anthropic system prompts tell Claude to avoid *genuinely*, *honestly*, *straightforward* | Quirón-measured, and Anthropic's published system prompts | Dead adverbs list | Over-correction item |
| 2023 marker words rare in 2026 output; ordinary words at several times the human rate now separate | Quirón-measured over LexA (Juzek 2026), Kobak et al. 2025 | Era table only | New wordlist section |
| Model stories are choppier than human ones, so blog rhythm advice backfires in fiction | Quirón-measured on WritingPrompts | No fiction guidance | Fiction section |
| Every rewriter slipped in small invented specifics; a figure-and-link diff caught them | Quirón-measured | Readback in prose only, no eval check | Eval check in `run.py` |
| Rewriting a human post made it read slightly more AI (Opus 6.0 to 7.5) | Quirón-measured, not significant (p = 0.056) | Triage already guards this | Nothing new; supports triage |
| Removing short negated setups inside the loop made rewrites read more AI | Quirón-measured | A1 on sight | Not taken; one measurement |

## Slopbuster: gaps against verve

From a separate read of slopbuster against verve's catalogue. Verve already covers nearly all of its 24 text patterns, usually more carefully, and it has nothing like groups F and G, the readback or triage. Every structural rule in it is asserted rather than measured; it cites studies only for vocabulary.

- **Process nouns as subjects** (`rules/academic.md` rules 25, 29, 46, 47): taken as C11, with Reinhart et al. as the evidence.
- **A question answered in the next breath** (`rules/text-structure.md`): taken into A4.
- **False ranges** (`rules/text-language.md`): not taken. Verve dropped it as stale on 24 Sep following Wikipedia.
- **Restating participial closers, per-section academic conventions, forced symmetry, scare quotes, a rhythm test**: small or covered; not taken this round.
- **Rejected**: the 0 to 10 score, detector-evasion framing, injected personality and feelings, "soften causal language" (changes claim strength).

## Slop-grader

A CLI that grades each line against each rule through Jev (TypeSafe's System One model, a paid API) or OpenRouter. Its rule questions are a compact restatement of tells verve already has (binary contrast, throat-clearing, puffery, weasel attribution, synonym cycling, decorative closers). Its document rules are scores. Its one idea verve could use offline is the reason it exists: a single model pass skims long documents. Taken as the instruction to mark long pieces a section at a time.
