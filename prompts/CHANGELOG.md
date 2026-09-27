# Prompt versions

Every version records what changed and the hypothesis behind it. P1 versions are built only
from course materials (revised identification rules doc, Brainstorm and Classification Rules
slides, DM review checklist, assignment's association-class conditions). Later versions are
driven only by errors observed in scored runs.

## Identification
- P0 Baseline: AUM brainstorming category list + output format.
- P1 Course methodology: role, definition of domain-specific, per-category rules from the
  revised rules doc, course example, sentence-by-sentence procedure with re-scan, constraints.

## Classification
- P0 Team baseline (t1): Jason's prompt, phrases appended (original had no placeholder, so the
  notebook's replace("<DOMAIN PHRASES>") never inserted them).
- P1 Course methodology: category-to-element mapping, class-vs-attribute tests, IS-A and
  conformance tests, two association-class conditions, attribute values, review checklist,
  description as context.

## Chain of thought
- P0: Step 1 identify (ID-P1 rules) -> Step 2 classify with one-line reasons (CL-P1 rules) ->
  Step 3 checklist review -> Step 4 final model.

---
## Round 1 results (Claude, default tier; team scorer; category-aware identification)

| activity | version | library | car rental | NTSS |
|---|---|---|---|---|
| identification | P0 | 72.1 / 67.9 / 71.6 (3 runs, mean 70.5) | 49.4 / 52.4 | 71.0 |
| identification | P1 | 87.0 | 58.3 | 81.0 |
| classification | P0 | 30.4 | 44.1 | 51.4 |
| classification | P1 | 42.1 | 43.0 | 57.1 |
| CoT (final model) | P0 | 40.7 (step 1: 74.0) | 38.8 (57.9) | 68.9 (76.9) |

Run-to-run noise: identification P0 on library over 3 runs spans 67.9 to 72.1 (about 4 points).
Treat differences under ~4 points as noise.

Scorer change before scoring round 1: classification names are split on CamelCase
("LoanItem" -> "loan item"). Applied to every run, so no version gains from naming style.

## Identification P2 (from round 1 error analysis)
| error class observed in P1 | evidence | P2 rule |
|---|---|---|
| verbs in modal/passive/infinitive/coordinated positions skipped | kept; set up, added, removed, prepares, give, visit; taken from, cover, sent to | find verbs in every grammatical position |
| one verb listed twice, or with its object | "issues...to" + "is issued"; "borrow" + "borrowed"; "sign the contract" | one row per verb, no object |
| literal X-of-Y with quantity head skipped | number of subject sections, types of loan items; time of reservation, period of time | list every literal "<noun> of <noun>", only "of" |
| abstract nouns skipped | details, membership; creation, promotion, evaluation, status | include nominalizations and specific compounds |
| states/options written as verbs or nouns | rented out, voided, opened, not available, in person, by phone | states and alternatives are rule 4, one value per row |
| role adjectives merged into nouns | "invited speakers", "selected speakers" | adjective alone under rule 4 |
| background narrative treated as domain | labor cost, job market, business model, metropolitan area | scope filter: business operation only |
| evaluative adjectives | unique, famous, customer-friendly | exclude evaluative adjectives |
| generalization written without subclasses | "there are two types of loan items" | write "A and B are N types of X" |

## Classification P2 (from round 1 error analysis)
| error class observed in P1 | evidence | P2 rule |
|---|---|---|
| synonym chosen as class name cascades into every attribute/association | Member instead of Customer: ~7 FP + 7 FN on library | use the name introduced first; no second class |
| document class dropped, its number moved to the person | membership card missing, member number on Member | documents are classes; their numbers are their attributes |
| V rows for examples and limits; invented attributes | French, beginner, 8; max loan items, membership status | V only for closed lists; limits are multiplicities; no invented attributes |
| adjective-kinds made subclasses, noun-kinds made values | invited/selected speaker subclasses; plans as values | follow phrase category: adjective -> type + V, noun kind -> subclass |
| aggregation for listed activities | design, seminar, reception part-of trade show | aggregation only for wholes made of members/parts |
| no association classes produced | loan transaction, reservation, review all missed | check every association; occurrence nouns signal an association class |
| verb forms changed | send vs sent to; process vs processed by | keep the verb as written, with preposition |

## Example hygiene (applies from P2 on)
Every example in P2 prompts uses neutral domains (hotel, clinic, school). An automated check confirms no
gold phrase from any of the three answer keys appears in a prompt's examples, except those in the
instructor's own revised rules document (valid, daily, beginner, a number of, less than 8, maximum
of 8, is identified by, is issued to). Found and removed while drafting P2: "book / books" and
"has a title" (library words in identification P1). Library scores are therefore slightly
optimistic for P0/P1; car rental and NTSS are the fairer generalization tests.

## Chain of thought P1
Built with scripts/build_cot.py from identification P2 + classification P2. Scaffold changes:
re-scan all verbs (not only passive); check every association for association-class status.

## Target change
Optimization goal lowered from F1 = 97% (assignment PDF) to F1 = 90% per the instructor.
Status against 90% after round 1: identification P1 library 87.0 and NTSS 81.0 are within reach;
car rental identification (58.3) and all classification scores (42-57) are not yet.

---
## Round 2 results (mean F1 over all runs so far; n = number of runs)

| activity | version | library | car rental | NTSS |
|---|---|---|---|---|
| identification | P0 | 68.9 (n=4) | 52.0 (n=3) | 71.2 (n=2) |
| identification | P1 | 88.7 (n=2) | 60.0 (n=2) | 80.8 (n=2) |
| identification | P2 | 87.7 | 63.8 | 79.8 |
| classification | P2 | 70.6 | 45.5 | 61.0 |
| CoT (final model) | P1 | 63.0 (step 1: 83.5) | 40.0 (71.1) | 61.3 (88.6) |

Library is still below 90 -> step 6 -> back to step 3.

Identification P2 finding: recall rose as designed (NTSS R 84 -> 97, car rental 73 -> 78) but
precision fell (NTSS P 78 -> 68), so F1 was flat. Several new false positives were caused by
P2 rules over-firing: this is the precision/recall trade-off of adding inclusion rules.
Classification P2: library +28.5 (42.1 -> 70.6), confirming the naming-cascade hypothesis.

## Identification P3 (precision-focused; from round 2 error analysis)
| error class observed in P2 | evidence | P3 rule |
|---|---|---|
| compound rule over-fired on adjective + noun | invited speakers, new domains, outdated domains, international trade shows | only noun-noun compounds naming a different thing; adjectives never make a new noun |
| literal X-of-Y over-fired on groups/containers | committee of reviewers, list of predefined domains | exclude groups/containers |
| "a number of X" rewritten as X of Y | number of rental locations, number of different makes | "a number of" is a quantifier (rule 5) |
| nouns naming kinds pushed into rule 4 | language tapes, books, sedan, hatchback, named plans | kinds stay nouns; rule 4 = adjectives, states, choices, life-cycle steps |
| action words moved to rule 4 | reserved (text also says "can be reserved") | used as an action anywhere -> rule 3 |
| number listed twice | 8 and maximum of 8; two/four under rules 4 and 5 | list the bound once; numbers only under rule 5 |
| descriptions treated as generalization | "speakers are famous figures", "reviewers who are experts" | both sides of X is a Y must be domain concepts |
| notes inside the phrase cell | "includes (Promoting a trade show includes ...)" | phrase only |
| (technique) | | added a self-verification pass: dedupe, scope, rule check before answering |

## Classification P3 (from round 2 error analysis)
| error class observed in P2 | evidence | P3 rule |
|---|---|---|
| association class emitted without its association, and also as a class | AC loan + C loan, no AS borrow | output AS + AC + its attributes; never also C |
| AC attributes missing | borrow / renew / reserve of the loan occurrence | one attribute per action performed on an occurrence |
| kinds rule misfired both ways | sedan/hatchback subclasses; invited/selected speaker subclasses | subclass only if the kind has something of its own (course inheritance criterion); adjective kinds are always values |
| association attached to a subclass the sentence doesn't name | "Vehicles can be taken from..." -> taken from(car, location) | connect to the class the sentence names |
| (review) | | checklist checks every I row and every AC row |

Known cap (not fixed, by design): car rental attribute names chosen by the expert that do not appear
in the text (transmission, means, body style, number of doors, status). Fixing them would require
putting answer-key names into the prompt.

## Chain of thought P2
Composed from identification P3 + classification P3. build_cot.py now copies the identification
procedure (including the P3 self-verification pass) instead of a fixed summary paragraph.

---
## Round 3 results (single run per cell)

| activity | version | library | car rental | NTSS |
|---|---|---|---|---|
| identification | P3 | 89.9 (P 92.5 R 87.5) | 74.5 | 85.4 |
| classification | P3 | 69.1 | 50.4 | 64.7 |
| CoT (final model) | P2 | 69.1 (step 1: 88.0) | 32.6 (75.3) | 55.6 (86.7) |

Identification P3 hypothesis confirmed on car rental (+10.7) and NTSS (+5.6), both beyond the
+/-3.9 noise threshold; library +2.2 is within noise. Precision recovered (NTSS 68 -> 83) with most
of P2's recall kept. Library is 0.1 below 90 on one sample: not decidable without repeat runs.

## Classification ceiling (why classification stops at P3)
Team scorer with --no-args (arguments ignored): library 80.0, car rental 67.7, NTSS 67.7 vs the
official 69.1 / 50.4 / 64.7. On library the remaining misses are expert modeling choices the text
does not support:
- borrow(customer, book) and AC loan transaction(customer, book); the text says customers borrow "items"
- loan item.title; the text says "a book has a title"
- book.subject and hold(section, loan item); neither appears in the text
- membership card.id; the text says "a unique member number"
A model faithful to the description cannot reach 90 on library classification without being given
these choices, which would leak the answer key. Classification best: P3 on the three-domain mean.

## Identification P4 (library-driven, from round 3 error analysis)
| error class observed in P3 | evidence (library) | P4 rule |
|---|---|---|
| possession clause split into pieces | "has a level", "has author(s)" | one row per possession clause, items kept together |
| X-of-Y inside another rule's sentence skipped | "types of loan items" (inside the generalization) | one sentence can give rows under several rules |
| record-keeping verb dropped by the software filter | "kept" (missed in P1, P2 and P3) | the business keeping information is a domain verb |
| example value dropped as a "named instance" | "French" from "(e.g. French)" | property example values are rule 4 |
| words pulled out of listed phrases | "update" (update of records), "current" (current loan) | delete unless used alone or one of named alternatives |
| rule conflict introduced in P4 draft, resolved | | adjectives go to rule 4 only when the text names alternatives for the same noun |

## Chain of thought P3
Composed from identification P4 + classification P3 (2,899 words). Note: CoT P2 fell on car rental
(40.0 -> 32.6) and NTSS (61.3 -> 55.6) while its step 1 stayed level with standalone identification;
the drop is in classification inside the long combined prompt.

---
## Round 4 results (means; n = runs)

| activity | version | library | car rental | NTSS |
|---|---|---|---|---|
| identification | P4 | **93.7** (n=2: 95.5, 91.9) | 71.9 | 89.6 |
| classification | P3 | 70.8 (n=3: 67.9, 69.1, 75.5) | 47.2 (n=2) | 64.3 (n=2) |
| CoT (final model) | P3 | 63.7 (n=2; step 1: 91.4, 94.4) | 31.9 | 68.9 |

Step 6: library identification F1 >= 90 on both runs -> library goal met.
Steps 7-8: NTSS 89.6 (single run, 0.4 below, inside +/-3.9 noise); car rental 71.9.

## Decision: stop at identification P4, classification P3, CoT P3
- NTSS: 4 misses are key-convention items (involves/including as part-of, "each"); most of the 15
  extras are genuine domain phrases the NTSS key does not list (status of a proposal, evaluation of
  proposals, "an organizer can be a person or an organization").
- Car rental: ~20 of 33 extras are domain-specific phrases the key omits, e.g. "rent" (the core verb
  of a car rental company), repair, deposit, damage, keep track of, settle. Fixing every fixable item
  (plans and sedan/hatchback as rule 4 instead of 1; voided/opened as rule 3 instead of 4) would reach
  about 80. Reaching 90 would require suppressing real domain phrases to match a sparse key.
- Classification: capped by expert modeling choices absent from the text (see classification ceiling).
A further round would be fitting the prompt to annotation conventions, not improving the method.

---
## Research-driven round: what the literature suggests, and what we tested

Sources reviewed:
- Chen et al., "Automated Domain Modeling with Large Language Models: A Comparative Study", MODELS 2023.
  Best LLM F1: classes 0.76, attributes 0.61, relationships 0.34. Main failures: missed elements (low
  recall) and relationships. Suggests generating several models and aggregating them.
- Yang et al., "Multi-step Iterative Automated Domain Modeling with LLMs", MODELS-C 2024: multi-step
  extraction + self-reflection improved class F1 by 22.71% and relationship F1 by 75.18% over one step.
- Chen et al., "Accurate and Consistent Graph Model Generation from Text with LLMs" (AbsCon), 2025:
  element-level majority voting raises precision but lowers recall, often giving lower F1 than a single
  run; adding structural constraints recovers recall; gains plateau at about 5 candidates; larger
  models are consistently better.
- Few-shot demonstrations are recommended for teaching annotation-specific choices.

Context for our numbers: classification P3 library 70.8 already exceeds the published single-model
baselines (which are 0.34-0.76 per element type).

### Experiment: element-level self-consistency (voting), tested offline on existing repeated runs
scripts/vote.py keeps a phrase when at least k of n runs list it (verbs vote together regardless of
auxiliaries: "issues" = "is issued").

| cell | single-run F1 | voting F1 |
|---|---|---|
| identification P4 library (n=2) | 93.7 | k=1 91.5, k=2 88.5 |
| identification P1 NTSS (n=2) | 80.8 | k=1 77.4, k=2 80.5 |
| identification P1 car rental (n=2) | 60.0 | k=1 58.3, k=2 60.4 |
| identification P0 library (n=4) | 68.9 | k=2 67.9, k=3 68.0, k=4 67.4 |

Result: no F1 gain. Voting trades recall for precision one-for-one, as AbsCon reported for plain
majority voting. It cannot remove car rental's systematic false positives (e.g. "rent"), which the model
lists in every run. Not adopted.

### Experiment: model capability (in progress)
identification-P4max and classification-P3max: identical text to the final prompts, run on the most
capable tier. Hypothesis from both papers: larger models are better with the same prompt.

### Considered, not run without instructor approval: leave-one-out few-shot
Showing annotated examples from the other two descriptions (e.g. library + car rental expert phrases when
evaluating NTSS) would teach the experts' conventions. It is standard held-out practice, but the
assignment says expert solutions must not be prompt inputs, so it needs the instructor's sign-off.

### Result: model capability (same prompts, most capable tier; single runs, tier_applied = complex)
| cell | default F1 (P / R) | most capable F1 (P / R) |
|---|---|---|
| identification P4 library | 93.7 (94.5 / 92.9) | 92.3 (88.5 / 96.4) |
| identification P4 NTSS | 89.6 (84.5 / 95.3) | 83.7 (74.5 / 95.3) |
| identification P4 car rental | 71.9 (62.5 / 84.6) | 71.9 (58.8 / 92.3) |
| classification P3 library | 70.8 (71.3 / 70.4) | 63.2 (60.0 / 66.7) |
| classification P3 car rental | 47.2 (48.2 / 46.2) | 37.7 (33.0 / 43.9) |
| classification P3 NTSS | 64.3 (56.1 / 75.4) | 62.3 (50.5 / 81.4) |

Hypothesis rejected. Precision fell in 6 of 6 cells and recall rose or held in 5 of 6: the stronger model
is more thorough and lists more genuine domain elements, which the sparser expert keys count as false
positives. This independently confirms that the remaining gap is annotation convention, not model error.
Not adopted; final prompts stay on the default tier.

Deck: noise thresholds are now measured per activity (identification 8, classification 8, CoT 14 points).
