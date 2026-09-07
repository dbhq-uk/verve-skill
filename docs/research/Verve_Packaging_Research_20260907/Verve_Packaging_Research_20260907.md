# The wrapper is not the problem: sepia is a skill too, and so is the 44k-star category leader - verve missed the January wave and has had no distribution at all

*standard · 6 angles · 9 sources (8 opened, 0 via Bright Data) · 3 disconfirming searches · premise of the request falsified*

**Question:** Is verve's 4-star / sepia's 2,374-star gap explained by packaging - "same product, wrong wrapper", verve as a Claude skill versus sepia as a standalone tool anyone can run? What should verve do?
**Scope:** What sepia ships, how it spread, and what the de-AI-writing category rewards. In: GitHub, aggregators, the Chinese-language ecosystem. Out: building anything; detector-evasion tools.

---

## Answer

The premise is wrong. Sepia is not a standalone tool: its own README describes "a portable Agent Skill: any agent that speaks the standard can load it", installed with `npx skills add Nanako0129/sepia` - the same Skills CLI and the same wrapper verve already ships [1]. The category leader, blader/humanizer at 44,842 stars, is also literally "Agent skill that removes signs of AI-generated writing from text" [6][7]. The gap is explained by timing and distribution, not packaging: the category's gold rush happened in one week of January 2026 (three repos created 11-19 Jan now hold 16.8k-44.8k stars each [7]), verve launched 29 July with no push, and sepia launched 28 August but caught GitHub Trending with a research hook and a novel fiction angle [3][4].

---

## Findings

### Finding 1: Sepia ships the same wrapper verve already has - an Agent Skill plus native plugins

**Confidence: Strong** - sepia's own repository, corroborated by the GitHub registry record and the skill directories that indexed it.

Sepia is plain markdown under the Agent Skills standard: one canonical `SKILL.md` with reference files, installed via `npx skills add Nanako0129/sepia -g` on "77+ agents", with native plugin packaging for Claude Code, Codex, Grok Build and Antigravity [1]. There is no binary, no CLI of its own, no API - the README says outright "the skill is plain markdown under the Agent Skills standard" [1]. Verve's install story is nearly identical: Claude Code plugin, `npx skills add dbhq-uk/verve-skill`, Codex installer. The claim that verve is "packaged as a Claude skill instead of a thing anyone can run" while sepia is a runnable tool does not survive contact with either repository. What sepia does have that verve lacks is two more native platforms (Grok Build, Antigravity), five slash-command operation entries (`/sepia-write`, `/sepia-review`, `/sepia-refactor`, `/sepia-recreate`, `/sepia-hemingway`), and READMEs in English, Simplified and Traditional Chinese [1].

### Finding 2: Sepia spread through GitHub Trending and the aggregator flywheel, not a launch post

**Confidence: Moderate** - two dated aggregator records and an absence of any launch thread; absence is hard to prove.

The repo was created 28 August 2026 [7]. The Daily Commit featured it on 29 August at "1,430+ GitHub stars" [3]; RepoFOMO's new-repos list recorded "+125% 7-day growth, +1,321 ★ this week, ★ 2,375 total" at 10 days old [4]. Pickup then cascaded through Telegram repo channels, Russian and Korean posts, and the skill directories (skills-hub.ai, skillsllm.com) that index by GitHub topic. Hacker News has no thread on it at all - Algolia returns zero results for the repo or its author [5]. The author has 199 followers [2], so this was not an influencer launch either. The two Chinese AI-Twitter posts about de-AI skills that surfaced in the disconfirming pass both predate sepia (their tweet IDs decode to 19 January and 14 February 2026), which is evidence for the category being hot, not for anyone sparking sepia. What plausibly got it onto Trending in the first place: a citable research base ("Based on StoryScope, arXiv:2604.03136" with the 93.2% macro-F1 stat that every aggregator quoted verbatim [1][3]), a genuinely new layer (narrative architecture for fiction, when every rival edits surface style), and the bilingual READMEs opening the Chinese-speaking market.

### Finding 3: The de-AI category's star gold rush was January 2026, and skills won it

**Confidence: Strong** - GitHub's own creation dates and star counts, plus multiple independent Chinese-language roundups.

blader/humanizer (created 18 Jan 2026): 44,842 stars. hardikpandya/stop-slop (11 Jan): 16,884. op7418/Humanizer-zh (19 Jan): 16,835. All three are skills or prompt packs, not standalone tools [6][7]. Late entrants do far worse regardless of quality: devswha/patina (24 Feb) has 348 stars, sepia (28 Aug) has ~2,390 - the best late-entry result, and still an order of magnitude below the January winners [7]. The category is also crowded and hottest in the Chinese-speaking ecosystem: there are published top-ten roundups of 去AI味 skills (cnblogs, wangruofeng007.com), an sspai feature, and a stack of competing Chinese-language repos. Verve, created 29 July [7], entered six months after the wave with an org-account author, no launch post anywhere findable, no research citations, and a repo description that anchors it to two platforms ("Claude Code and Codex skill…") when its install story already covers every agent the Skills CLI reaches [1].

### Finding 4: The 44.8k leader wins on four things verve can copy without copying its content

**Confidence: Strong** - blader/humanizer's own README and skill files, read in full, compared against verve's `skills/verve/` tree.

blader/humanizer's README does work verve's does not [6]. Four transferable moves, none of which require taking its patterns:

**A full before/after in the README.** The Lisbon example runs six paragraphs of AI travel-blog prose against six of the rewrite, with a note saying which facts the writer supplied so the rewrite could use them [6]. It is the single most persuasive artefact in the repo: a reader decides in thirty seconds whether the tool works. Verve has six worked examples of comparable quality in `skills/verve/references/examples.md`, and *none of them appear in the README* - they are buried where only an installed agent reads them. This is the cheapest high-value fix available.

**One causal account that generates every rule.** Humanizer opens with a theory: a model "writes whatever is most likely to come next… the choice that fits the widest range of readers and subjects. A person chooses for one reader and one subject", and then states that every tell it hunts is a form of that default choice [6]. Twenty-five patterns hang off one sentence. Verve's patterns.md has six lettered groups (A-F) and no spine - and the irony is that verve's audience guard *is* the "one reader" half of that theory, already built and better developed than humanizer's, just never stated as the reason the tool exists.

**Patterns numbered by strength, with weak-alone guards.** Humanizer numbers 1-25 by strength and frequency: "the first five justify an edit on a single sighting", while others are "marked weak alone… count only when several tells share a passage, because a careful writer may use any one of them on purpose" [6]. That is both a false-positive guard and a citable handle. Verve's groups are unnumbered and carry no severity ranking - a grep for weak-alone or false-positive language in `patterns.md` returns one unrelated line. Verve's triage step gets some of this benefit, but at whole-document rather than per-pattern resolution.

**A named external authority.** Humanizer's pattern list is sourced to Wikipedia's "Signs of AI writing" and WikiProject AI Cleanup [6]; sepia's to arXiv [1]. Both winners point at an evidence base outside themselves. Verve cites stop-slop in acknowledgements only.

Two smaller ones worth noting: voice matching from a pasted sample ("include 2-3 paragraphs of your own writing" and it follows your rhythm, word choice and quirks [6]) is a real feature gap - verve has tone, variety and audience but no way to say *sound like me*, and `.verve.md` is the obvious home for it. And humanizer's release notes state a pattern count on every entry, which advertises maintenance at a glance.

What not to copy: the 25 patterns themselves (verve's catalogue is larger and its condescension group has no equivalent there), and the vocabulary list. Verve's differentiators - audience pitch, British English, the voice pass, the anti-detector-evasion stance - are things neither leader has.

---

## So What

On this evidence, rebuilding verve as a standalone CLI would be effort spent falsifying a premise that is already falsified - every winner in this category is a skill. What verve is missing is not a wrapper but (a) any distribution event at all, and (b) the shareable hooks the aggregator flywheel feeds on. The moves that follow, cheapest first:

1. **Fix the discovery surface now.** Description should lead with the category term and the 77+-agent reach, not "Claude Code and Codex". Topics should add the tags the skill directories and roundups index on: `humanizer`, `ai-writing`, `llm`, `writing-tools`, `developer-tools`. Done in this session.
2. **Give the README the hooks aggregators quote.** Sepia's description was reprinted verbatim by every aggregator. Verve's British-English default, the audience guard, and the removed-the-paid-detector-evasion story are genuinely distinctive; they need to be in the first two lines, not paragraph four. Done in this session.
3. **Distribution is the actual gap, and it is a human act.** A Show HN, a post where the category audience lives (r/ClaudeAI, X, and - where demand demonstrably is - the Chinese-speaking community), or a PR adding verve to the roundup lists. Sepia proves a 199-follower unknown can 500x verve's stars in a fortnight with no launch thread, purely on hooks plus trending. This is Daniel's call on venue and voice, and the one thing this session cannot do for them.
4. **An evidence base is the durable differentiator.** Sepia's arXiv grounding is what every reprint quoted. Verve's equivalent is honest eval numbers from the corpus that already exists in `evals/` - run it, publish the numbers, and cite the prose-relevant public research (Measuring AI Slop, Reinhart et al.) where it genuinely applies. Do not manufacture a research veneer; the repo's own no-unrun-numbers rule is right.

Second-order point no source states: the January winners won on being first, sepia won on being different. Verve can only take the second path, and its differences (audience pitch, British English, both-halves rewrite, the anti-detector-evasion stance) are real but currently invisible at every point where discovery happens.

## Limitations

Sepia's precise trending trigger is inferred from dated aggregator snapshots; star-history granularity was not retrieved, and a deleted launch post somewhere unindexed cannot be ruled out. Star counts are a proxy for users; none of these repos publish install counts, so "sepia has more users than verve" is likely but unproven. The Chinese-ecosystem heat rests on roundup pages read at SERP level plus competitor repos verified via the GitHub API; the roundup pages themselves were not opened. All counts are as of 2026-09-07 and this field moves weekly.

## Bibliography

[1] Nanako0129 (2026). "sepia - De-AI writing skill". GitHub. https://github.com/Nanako0129/sepia
[2] Nanako0129 (2026). "Nanako0129 (Nyanako) profile". GitHub. https://github.com/Nanako0129
[3] The Daily Commit (2026). "Nanako0129/sepia". thedailycommit.in. https://thedailycommit.in/story/2026-08-29/08-github-nanako0129-sepia
[4] RepoFOMO (2026). "Top 50 New GitHub Repositories (Under 4 Weeks Old)". repofomo.com. https://repofomo.com/trending/new/
[5] HN Algolia (2026). "Search: sepia de-AI - no results". hn.algolia.com. https://hn.algolia.com/api/v1/search?query=sepia+de-AI
[6] blader (2026). "humanizer - Agent skill that removes signs of AI-generated writing from text". GitHub. https://github.com/blader/humanizer
[7] GitHub API (2026). "Repository metadata: star counts and creation dates for de-AI category repos". api.github.com. https://api.github.com/repos/blader/humanizer
