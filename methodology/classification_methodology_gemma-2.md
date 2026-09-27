---
title: "Saif classification methodology"
subtitle: "Evidence-first AUM Step 3 classification with association-class audit"
---

# Objective

Classify the identified phrases into classes, attributes, values, associations, aggregations, inheritance, and association classes using only evidence in the business description. The assignment target is F1 >= 0.97 on all three domains.

# Procedure

1. Treat the phrase table as the candidate set and the description as evidence. Do not invent concepts or synonyms.
2. Create a concept ledger: canonical name, source phrase(s), likely kind, owning class, and evidence sentence.
3. Resolve duplicate names before creating relationships. Prefer the first name introduced when the description gives aliases.
4. Apply the class/attribute tests:
   - independent business object, document, role, or place -> class;
   - scalar property, state, identifier, or quantity owned by one object -> attribute;
   - class names never appear as attribute owners or values.
5. Map relationship phrases:
   - transitive verb -> association;
   - explicit part/whole -> aggregation;
   - `X is a Y` -> inheritance only when both are domain concepts and the IS-A/conformance tests pass;
   - possession/containment -> association, aggregation, or attribute based on the sentence's semantics.
6. Map closed lists and states to an explicitly named attribute plus value rows. Numeric bounds are multiplicities unless the description clearly treats them as stored values.
7. For every candidate association, perform the association-class gate:
   - Is the relationship many-to-many?
   - Is information about the relationship occurrence, rather than either endpoint, maintained?
   Emit `AS`, `AC`, and occurrence attributes only when both answers are yes.
8. Run a graph audit:
   - every relationship endpoint is a `C` or `AC`;
   - every `A` has one owner;
   - every `V` has one attribute owner;
   - every `AC` has a matching `AS` and at least one occurrence attribute;
   - no association class is duplicated as a plain `C`.
9. Emit one table and nothing else.

# Output contract

Use exactly:

| label | element | arg1 | arg2 |
|---|---|---|---|

Labels are `C`, `A`, `V`, `AS`, `AC`, `AG`, and `I`. Use lower-case source wording, with blank arguments where the label does not need them.
