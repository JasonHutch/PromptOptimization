---
title: "Saif identification methodology"
subtitle: "Coverage-first phrase extraction for AUM Step 2"
---

# Objective

Extract every domain-specific phrase that appears literally in the business description while excluding generic software language and background narrative. The assignment target is F1 >= 0.97 on library, car rental, and NTSS.

# Procedure

1. Read the description sentence by sentence and preserve the original wording.
2. Build a private inventory of noun phrases, `X of Y` phrases, transitive verbs, states/enumerations, quantities, possession clauses, part/whole expressions, containment expressions, and generalization expressions.
3. Apply the domain-scope filter: retain only concepts the business tracks, acts on, or constrains; remove UI, storage, generic system capability, marketing, and illustrative proper names.
4. Normalize only grammatical variants. Keep one row for a repeated concept, but do not merge different phrases merely because they are synonyms.
5. Run a coverage audit against the source:
   - nouns in every sentence, including abstract nouns and documents;
   - passive, modal, infinitive, gerund, and coordinated verbs;
   - state words versus action verbs;
   - literal `of` expressions;
   - each item in a closed enumeration;
   - each quantity or bound;
   - possession and relationship expressions.
6. Run a precision audit: reject generic words, adjectives with no domain state/kind/value, narrative claims, and nouns already contained in a longer phrase unless they name a separate object.
7. Emit only the required two-column table. Do not add explanations or inferred phrases.

# Output contract

Use exactly:

| rule | phrase |
|---|---|

Rules 1–9 follow the instructor's identification rules. A phrase may appear under more than one rule when the source warrants it. Every phrase must be a literal span of the description, apart from singular/plural or tense normalization.

# Error controls added in this version

- A source-span audit reduces false negatives from passive verbs, quantities, and coordinated lists.
- A separate state/action decision prevents state adjectives from being emitted as verbs.
- A literal-span check prevents answer-key leakage and invented synonyms.
- A final table-only contract makes the output safe for the existing scorer.
