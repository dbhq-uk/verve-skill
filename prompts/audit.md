Audit the prose in this repository for AI tells. Report only. Change nothing.

That last part is the contract for this whole job. You are surveying, not editing. Do not rewrite a file, do not fix a tell, and do not open a pull request, however obvious the fix looks. At the end I decide which files get a verve run, and that run is a separate job.

## What to judge against

If the verve skill is installed, read its catalogue and use it: `SKILL.md`, then `references/patterns.md` and `references/wordlist.md`. If it is not installed, fetch these two and work from them:

- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/patterns.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/wordlist.md

Work from that catalogue rather than your own sense of what sounds artificial. A named tell with a worked example is checkable; a feeling is not.

## First, find the prose

Prose is text written to be read by a person, where the voice matters. Look for it in READMEs, `docs/`, contributing and security policies, changelog entries that describe things in sentences, marketing and landing copy, blog posts, and long comment blocks that explain a decision rather than a line of code.

Then throw out everything that is not prose, and say what you set aside. Repositories are full of text that looks auditable and is not:

- Licences, and any file whose wording is legally fixed
- Generated API references, schema dumps, and anything with a "do not edit" header
- Vendored or third-party files you did not write
- Changelogs that are lists of commit subjects
- Configuration tables, command references, and option matrices, where terseness is correct and voice would be noise
- Test fixtures, and any file that quotes bad writing deliberately

That last one matters more than it sounds. A document about AI slop quotes AI slop as evidence. Those are specimens, not violations, and a blockquote is usually the signal. Counting them is the fastest way to make this whole audit useless.

## Then judge each file

For every file that survived, give me:

- The tells you actually found, named from the catalogue, with the line number and the phrase
- How dense they are: tells per hundred words, not a raw count, so a long file is not punished for being long
- The three worst instances, quoted

Judge fidelity risk too, because it decides whether a verve run is safe to make heavy. A file thick with figures, names, dates and quoted commands has a lot to lose in a rewrite. A file of general argument has little. Say which each one is.

Do not flag a word from the wordlist on sight. Nothing there is banned outright: the tell is density and reflexive use, and one deliberate use of the right word is fine. If you cannot say what the sentence would look like without it, it is not a finding.

## Report

Order it worst first, by density, in one table: file, words, tells per hundred words, fidelity risk, and the single worst tell in it.

Then, under the table, three short lists.

**Worth a run.** The files where a verve pass would clearly help, with the strength I should ask for and why. Say `light` where the file is dense with facts and only needs the unmistakable tells removed, and `moderate` or `heavy` where the writing itself is the problem.

**Leave alone.** The files that already read as human-written. Name them explicitly. A survey that finds fault everywhere is not a survey, and verve's own first step is deciding to do nothing.

**Not prose.** What you set aside, and in a few words each, why.

Finish with the one file you would fix first, and the reason it is that one rather than the one at the top of the table. Density is not the same as importance: a README with a moderate score is read a thousand times more often than an internal note with a terrible one.

## Limits

Read-only, as above. Do not install anything, do not add a dependency, and do not touch source code, tests or CI. If the repository has uncommitted changes, that is fine, because you are not writing to it, but say so if you notice, in case I did not mean to leave them there.
