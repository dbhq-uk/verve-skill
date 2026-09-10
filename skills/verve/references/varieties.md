# English varieties

Verve writes British or American English. This file is what that means in
practice, and, more importantly, where the line sits between a variety
convention and a fact you must not touch.

## Choosing the variety

In this order:

1. **What the user asked for.** *"in US English"*, *"American spelling"*,
   *"keep it British"*. An explicit instruction settles it.
2. **What the source already is.** Read the evidence and keep it.
3. **British**, when the source gives no signal either way.

Rule 2 is the one that matters, and it follows from hard constraint 1. Turning
somebody's `color` into `colour` is an unrequested edit to finished prose. It is
small, but it is the kind of small change that makes a tool feel like it is
arguing with you, and verve does not make edits nobody asked for.

## Detecting the variety of a source

One signal is not evidence. Oxford spelling is British and uses `-ize`
throughout, so a single *organize* tells you nothing. Look for two or more
independent signals that agree, drawn from different rows of the tables below.

Strong signals, roughly in order of how much weight to give them:

- `-our` / `-or` (*colour*, *honour*, *behaviour*)
- `-re` / `-er` (*centre*, *metre*, *theatre*)
- Doubled `l` before a suffix (*travelled*, *cancelled*, *modelling*)
- `-ce` / `-se` in noun forms (*licence*, *defence*, *practice* as a noun)
- Vocabulary pairs (*autumn*, *lift*, *pavement*, *mobile*)
- Date order in running prose (*14 March 2026* against *March 14, 2026*)

Weak on its own: `-ise` / `-ize`, single `l` spellings, and the serial comma.

Where the source is genuinely mixed, use British, and say so in one line when
you deliver: *"Source mixed British and American spelling; standardised on
British."* Do not stop and ask. A cosmetic question is not worth interrupting a
run for.

## Spelling

| Family | British | American |
|---|---|---|
| `-our` / `-or` | colour, honour, favour, behaviour, labour | color, honor, favor, behavior, labor |
| `-re` / `-er` | centre, metre, theatre, fibre, litre | center, meter, theater, fiber, liter |
| `-ise` / `-ize` | organise, realise, recognise, apologise | organize, realize, recognize, apologize |
| `-yse` / `-yze` | analyse, paralyse, catalyse | analyze, paralyze, catalyze |
| `-ce` / `-se` (noun) | licence, defence, offence, pretence | license, defense, offense, pretense |
| Doubled `l` | travelled, cancelled, modelling, labelled | traveled, canceled, modeling, labeled |
| `ae` / `oe` | anaemia, paediatric, oestrogen, manoeuvre | anemia, pediatric, estrogen, maneuver |
| `-ogue` / `-og` | catalogue, dialogue, analogue | catalog, dialog, analog |

Note that British keeps the noun and verb distinct in the `-ce` / `-se` row:
*a licence* but *to license*, *a practice* but *to practise*. American uses
*license* and *practice* for both. Getting this wrong is a grammar error rather
than a variety slip, so check the part of speech before converting.

Irregulars that follow no family rule:

| British | American |
|---|---|
| programme (but *computer program*) | program |
| storey (of a building) | story |
| tyre | tire |
| kerb | curb |
| plough | plow |
| grey | gray |
| aluminium | aluminum |
| speciality | specialty |
| whilst, amongst, learnt, spelt, dreamt | while, among, learned, spelled, dreamed |

## Vocabulary

**Vocabulary conversion is off unless the user asks for it by name.** Spelling
and punctuation are conventions. A word is a choice, and swapping one is the
synonym substitution constraint 2 forbids, wearing a spelling conversion's
clothes. *CV* and *résumé* are not the same document. A *flat* and an
*apartment* are not the same thing in every market. Setting the variety to
American does not license either swap.

When the user does ask for vocabulary conversion, convert only where the other
variety would genuinely read as foreign, and never a word that names something
specific. Most words are shared, and swapping one for the sake of it costs
precision for nothing.

| British | American |
|---|---|
| autumn | fall |
| lift | elevator |
| pavement | sidewalk |
| flat | apartment |
| mobile | cell phone |
| CV | résumé |
| holiday | vacation |
| post | mail |
| queue | line |
| timetable | schedule |
| maths | math |
| full stop | period |

## Punctuation and formatting

| | British | American |
|---|---|---|
| Quotation marks | Single outer, double inner | Double outer, single inner |
| Stop against a closing quote | Outside, unless the quoted text is a full sentence | Inside, almost always |
| Serial comma | Usually omitted | Usually kept |
| Courtesy titles | Mr, Mrs, Dr, St (no stop) | Mr., Mrs., Dr., St. |
| Dates in prose | 14 March 2026 | March 14, 2026 |
| All-numeric dates | Never produce one: `03/04/2026` is 4 March in one variety and 3 April in the other. Write the month out. An ISO `2026-03-14` already in the source stays exactly as it is |
| Time | 14:00, or 2pm | 2:00 p.m. |
| Billion | Modern British follows American: a thousand million |
| Collective nouns | Plural verb where the members act: *the team are arguing* | Singular verb: *the team is arguing* |

The serial comma row is a preference, not a rule, in either variety. Where
dropping it creates ambiguity, keep it, whichever variety you are writing.

**On dates.** Constraint 1 itself carries the exception: a date's value
survives, its written format may follow the variety, and verve never produces
a new all-numeric date. This file does not get to widen that. Applying it:
`03/04/2026` is 3 April in British order and 4 March in American, and a reader
cannot tell which was meant, so when converting a date in running prose, write
the month out. An ISO `YYYY-MM-DD` already in the source is unambiguous and
stays exactly as it is - and so does any other all-numeric date whose order
you cannot determine. Leave it rather than guess.

## What the variety does not change

**The em dash ban holds in both.** It is a rule about a machine-writing tell,
not a British convention. Chicago style uses em dashes freely and correctly, so
a reader setting the variety to American may reasonably assume the ban was a
British quirk and put them back. It was not. Models overuse the em dash in every
variety, and `patterns.md` C1 applies unchanged.

Also unchanged by the variety: the curly quote rule (C6), which is about
typographic artefacts rather than nationality; every tell in `patterns.md`; every
list in `wordlist.md`; the tone presets; and the exit checks.

## What must never be converted

This is the fidelity risk in this feature, and it outranks every table above.
Hard constraint 2 says technical terms keep their exact wording. Applied here:

**Code, and anything inside it.** `background-color`, `initialize()`,
`--optimize`, `color: red`, `analyzer`. A CSS property is an identifier, not a
spelling. Converting one breaks the code, and it is the single worst thing this
feature could do.

**Quoted material.** Anything inside quotation marks that somebody actually
said or wrote. A British writer quoting an American keeps the American's
spelling, and the reverse. Changing a quotation is a fidelity failure.

**Proper nouns, always.** The World Health Organization keeps its `z`. So do
the Department of Labor, the US Department of Defense, Pearl Harbor, the World
Trade Center and Labor Day. On the other side, the Labour Party, the Ministry of
Defence and the Barbican Centre keep their British forms in American prose.
Names are names in every variety.

**Titles and citations.** A book, paper, film or article title is quoted exactly
as published, including its spelling. So is a journal name and a URL.

**Legal and standards text.** Wording from a licence, a contract, a
specification or a standard is fixed. Leave it.

**Domain terms with a settled form.** Where a field has standardised on one
spelling, that spelling is the term. In computing, `serialize`, `normalize` and
`tokenizer` are frequently the term of art even in British writing.

When you cannot tell whether something is a convention or a term, treat it as a
term and leave it alone. Constraint 6 applies: if a change might alter meaning,
do not make it.
