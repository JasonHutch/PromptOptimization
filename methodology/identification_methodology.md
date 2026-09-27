---
title: "Optimized Methodology for Identifying Domain-Specific Phrases"
subtitle: "Team Four · CSE 4392/5320 · final version (identification prompt P4)"
---

**Evaluated against the expert solutions (F1):** library 93.7 (mean of 2 runs), NTSS 89.6, car rental 71.9. LLM: Claude (claude.ai, default tier). Baseline (P0): library 68.9 (mean of 4 runs).

This methodology extends the instructor's *Rules for identifying domain-specific phrases*. Section 5 lists every change and the observed errors that motivated it. Section 6 is the exact prompt given to the LLM.

# 1. Definition

A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

Example from the course. Sentence: "The web-based application must provide a search capability for overseas exchange programs using a variety of search criteria."

- domain-specific nouns: programs, search criteria
- domain-specific transitive verb: search for
- not domain-specific: web-based (adjective), application, capability (nouns), provide, using (verbs)

# 2. Phrase categories and rules

Use the rule number when recording a phrase.

1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories (e.g., enrollment, approval, subscription, history). List a longer noun-noun compound separately only when it names a different thing from its head noun (e.g., "room" and "room key"). An adjective in front of a listed noun does not make a new noun: "new rooms", "senior nurses" and "regular guests" are the nouns "rooms", "nurses" and "guests". Put such adjectives under rule 4 only when the text names two or more alternatives for the same noun ("senior and junior nurses" gives "senior" and "junior"); a single descriptive adjective ("late checkout") is not listed separately.
2. "X of Y" expressions, where X and Y are nouns or noun phrases (e.g., "color of car"). List every literal "\<noun\> of \<noun\>" in the text, also those whose head is a quantity or kind word (e.g., "number of seats", "kinds of rooms", "length of stay"). Only the preposition "of" counts ("gift for the guest" is not an X of Y). Do not list a group or container of Ys as X of Y ("team of players", "list of guests"), and "a number of rooms" is an indefinite quantity (rule 5), not an X of Y; never rewrite "a number of X" as "number of X". A phrase can be listed under both rule 1 and rule 2 (e.g., "date of birth").
3. Transitive verbs: action verbs performed by or on domain entities. Include passive voice and past participles (e.g., "is identified by", "is issued to") and multi-word verbs (e.g., "search for", "check in", "apply for", "assigned to").
   - Find verbs in every grammatical position: after modals and in passives ("must be confirmed", "can be transferred to", "need be approved"), in infinitives ("to deliver", "come to collect"), as gerunds ("booking rooms"), and every verb of a coordinated list ("checks, cleans and restocks" is three verbs).
   - List each verb once, whatever its voice or tense ("schedules", "is scheduled" and "scheduled" are one row). Write the verb with its particle or preposition but without its object ("cancel", not "cancel the booking").
   - A word the text uses only to describe a state an entity is in (e.g., "the room is occupied", "the account is overdue") is rule 4, not a verb.
4. Adjectives, enumeration: state-describing adjectives and conditional attributes that govern business rules or domain states (e.g., valid, daily, beginner), and listed values of a property.
   - Include states and statuses even when written as participles or nouns (e.g., vacant, occupied, checked in, cancelled, overdue, approved, denied).
   - Include each item of a list of alternatives the business keeps: kinds or variants of an entity (economy or business; single, double, or suite), the ways something is done (online, at the front desk), and the life-cycle steps recorded for an asset (e.g., installation, inspection, replacement).
   - Adjectives that distinguish kinds of a role (e.g., "senior nurses", "junior nurses") are listed as the adjective alone (senior, junior); the noun goes under rule 1.
   - Nouns that name kinds of something (e.g., a named package, a room type such as "suite", a kind of item) stay under rule 1. Rule 4 holds adjectives, states, choices and life-cycle steps only.
   - If the text uses a word as an action anywhere (e.g., "a guest can be upgraded"), list it under rule 3; list it under rule 4 only when the text uses it just to describe a state.
   - One value per row.
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases that constrain domain entities (e.g., "a number of", "less than 8", "maximum of 8", "at least two", "up to 3"). Write only the quantity expression, not the noun it counts, and list each number separately ("one or two beds" gives "one" and "two"). List a number here even if it is also inside a longer phrase, but list a bound once as the bound ("maximum of 8", not also "8"). Numbers go under rule 5 only, never rule 4.
6. Possession expressions: has / have / possess statements between domain concepts. Write the whole expression (e.g., "has a color"). Write one row per possession clause, keeping everything the clause lists together ("a room has a view, and a balcony" is one row, not two). "Have to" expresses obligation, not possession.
7. "Consist of / part of" expressions (e.g., "made up of", "consists of", "is part of", "comprises", "is composed of").
8. Containment / containing expressions (e.g., "contains", "holds").
9. "X is a Y" expressions (generalization/specialization), including equivalent wording such as "is known as", "is considered a", "is a kind of" or "there are N types of X". Write the whole expression naming both sides; for "there are N types of X: A and B", write "A and B are N types of X". Both sides must be domain concepts that could be classes; a sentence that only describes someone ("the guests are frequent travelers") is not a generalization.

# 3. Domain scope filter

- Exclude general system capabilities or software infrastructure verbs (e.g., support, provide, allow) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays, suggests or stores (the system, its screens and its messages). This does not exclude the business keeping or recording information about its entities: in "the particulars of each guest must be kept", "kept" is a domain verb.
- Exclude background narrative that is not part of the business operation: the business's history, success, costs, market conditions and motives for building the system. Only the description of how the business operates is in scope.
- Exclude names of specific real-world instances used as illustrations (named firms, venues, brands, people, dates, addresses). A value given as an example for a property is different: in "color (e.g. red)", "red" is an enumeration value (rule 4).
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, popular, modern, convenient).

# 4. Procedure

1. Read the description one sentence at a time.
2. In each sentence, test every noun phrase, verb, adjective, number and relationship expression against the definition and the nine categories.
3. Keep each phrase in the wording used in the text. List a concept once even if it appears many times; singular and plural forms are the same phrase (you may write "ticket / tickets").
4. One sentence can give rows under more than one rule; list each. "There are two kinds of rooms: singles and suites" gives "two" (rule 5), "kinds of rooms" (rule 2) and "singles and suites are two kinds of rooms" (rule 9).
5. Before answering, re-scan the whole description for phrases you skipped, especially passive verbs, adjectives that express a rule or state, and quantities.
6. Then check every row and delete or move the rows that fail:
   a. Is the same concept already listed under this rule in another form (singular/plural, with an adjective in front, another form of the same verb)? Keep one row.
   b. Is it a word you took out of a longer phrase you already listed (the noun "cleaning" out of "cleaning of rooms", the adjective "late" out of "late checkout")? Delete it unless the text also uses it on its own, or it is one of two or more alternatives the text names for the same noun.
   c. Is it part of the business operation, not background narrative or the software?
   d. Is it under the right rule (kinds are nouns; states and choices are rule 4; numbers are rule 5; actions are rule 3)?

Constraints: Only list phrases that literally appear in the description. Do not add explanations. The phrase cell holds only the phrase, never a quoted sentence or a note in parentheses.

# 5. Changes from the instructor's rules

| Version | Change | Observed error that motivated it |
|---|---|---|
| P1 | Role, definition of domain-specific, per-category rules from the revised rules document, course example, sentence-by-sentence procedure | Baseline listed generic words and missed passive verbs, state adjectives and quantities |
| P2 | Verbs in every grammatical position; one row per verb; literal X of Y; abstract nouns; states and choices under rule 4; business-operation scope filter | Nine recurring error classes in P1 across all three descriptions (e.g. "kept", "set up", "number of subject sections", "rented out") |
| P3 | Narrowed the P2 rules that over-fired; numbers listed once; both sides of X is a Y must be domain concepts; self-verification pass | P2 raised recall but created its own false positives (e.g. "new domains", "committee of reviewers") |
| P4 | Possession clauses kept whole; one sentence can give rows under several rules; record-keeping verbs are domain verbs; example values are enumeration values; no words split out of listed phrases | Last library errors: "has a level", "types of loan items", "kept", "French", "update", "current" |

All examples in the rules use neutral domains (hotel, clinic, school), apart from those already in the instructor's rules document. An automated check confirmed that no phrase from the three expert solutions appears in the examples.

# 6. Final prompt (P4)

The text below is sent to the LLM with the business description in place of `{{DESCRIPTION}}`.

```
# Role
You are a domain modeling expert applying the Agile Unified Methodology (AUM). You are performing Step 2 of domain modeling: brainstorming the domain-specific phrases in a business description.

# Definition
A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

Example from the course. Sentence: "The web-based application must provide a search capability for overseas exchange programs using a variety of search criteria."
- domain-specific nouns: programs, search criteria
- domain-specific transitive verb: search for
- not domain-specific: web-based (adjective), application, capability (nouns), provide, using (verbs)

# Categories (use the rule number in the output)
1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories (e.g., enrollment, approval, subscription, history). List a longer noun-noun compound separately only when it names a different thing from its head noun (e.g., "room" and "room key"). An adjective in front of a listed noun does not make a new noun: "new rooms", "senior nurses" and "regular guests" are the nouns "rooms", "nurses" and "guests". Put such adjectives under rule 4 only when the text names two or more alternatives for the same noun ("senior and junior nurses" gives "senior" and "junior"); a single descriptive adjective ("late checkout") is not listed separately.
2. "X of Y" expressions, where X and Y are nouns or noun phrases (e.g., "color of car"). List every literal "<noun> of <noun>" in the text, also those whose head is a quantity or kind word (e.g., "number of seats", "kinds of rooms", "length of stay"). Only the preposition "of" counts ("gift for the guest" is not an X of Y). Do not list a group or container of Ys as X of Y ("team of players", "list of guests"), and "a number of rooms" is an indefinite quantity (rule 5), not an X of Y; never rewrite "a number of X" as "number of X". A phrase can be listed under both rule 1 and rule 2 (e.g., "date of birth").
3. Transitive verbs: action verbs performed by or on domain entities. Include passive voice and past participles (e.g., "is identified by", "is issued to") and multi-word verbs (e.g., "search for", "check in", "apply for", "assigned to").
   - Find verbs in every grammatical position: after modals and in passives ("must be confirmed", "can be transferred to", "need be approved"), in infinitives ("to deliver", "come to collect"), as gerunds ("booking rooms"), and every verb of a coordinated list ("checks, cleans and restocks" is three verbs).
   - List each verb once, whatever its voice or tense ("schedules", "is scheduled" and "scheduled" are one row). Write the verb with its particle or preposition but without its object ("cancel", not "cancel the booking").
   - A word the text uses only to describe a state an entity is in (e.g., "the room is occupied", "the account is overdue") is rule 4, not a verb.
4. Adjectives, enumeration: state-describing adjectives and conditional attributes that govern business rules or domain states (e.g., valid, daily, beginner), and listed values of a property.
   - Include states and statuses even when written as participles or nouns (e.g., vacant, occupied, checked in, cancelled, overdue, approved, denied).
   - Include each item of a list of alternatives the business keeps: kinds or variants of an entity (economy or business; single, double, or suite), the ways something is done (online, at the front desk), and the life-cycle steps recorded for an asset (e.g., installation, inspection, replacement).
   - Adjectives that distinguish kinds of a role (e.g., "senior nurses", "junior nurses") are listed as the adjective alone (senior, junior); the noun goes under rule 1.
   - Nouns that name kinds of something (e.g., a named package, a room type such as "suite", a kind of item) stay under rule 1. Rule 4 holds adjectives, states, choices and life-cycle steps only.
   - If the text uses a word as an action anywhere (e.g., "a guest can be upgraded"), list it under rule 3; list it under rule 4 only when the text uses it just to describe a state.
   - One value per row.
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases that constrain domain entities (e.g., "a number of", "less than 8", "maximum of 8", "at least two", "up to 3"). Write only the quantity expression, not the noun it counts, and list each number separately ("one or two beds" gives "one" and "two"). List a number here even if it is also inside a longer phrase, but list a bound once as the bound ("maximum of 8", not also "8"). Numbers go under rule 5 only, never rule 4.
6. Possession expressions: has / have / possess statements between domain concepts. Write the whole expression (e.g., "has a color"). Write one row per possession clause, keeping everything the clause lists together ("a room has a view, and a balcony" is one row, not two). "Have to" expresses obligation, not possession.
7. "Consist of / part of" expressions (e.g., "made up of", "consists of", "is part of", "comprises", "is composed of").
8. Containment / containing expressions (e.g., "contains", "holds").
9. "X is a Y" expressions (generalization/specialization), including equivalent wording such as "is known as", "is considered a", "is a kind of" or "there are N types of X". Write the whole expression naming both sides; for "there are N types of X: A and B", write "A and B are N types of X". Both sides must be domain concepts that could be classes; a sentence that only describes someone ("the guests are frequent travelers") is not a generalization.

# Domain scope filter
- Exclude general system capabilities or software infrastructure verbs (e.g., support, provide, allow) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays, suggests or stores (the system, its screens and its messages). This does not exclude the business keeping or recording information about its entities: in "the particulars of each guest must be kept", "kept" is a domain verb.
- Exclude background narrative that is not part of the business operation: the business's history, success, costs, market conditions and motives for building the system. Only the description of how the business operates is in scope.
- Exclude names of specific real-world instances used as illustrations (named firms, venues, brands, people, dates, addresses). A value given as an example for a property is different: in "color (e.g. red)", "red" is an enumeration value (rule 4).
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, popular, modern, convenient).

# Procedure
1. Read the description one sentence at a time.
2. In each sentence, test every noun phrase, verb, adjective, number and relationship expression against the definition and the nine categories.
3. Keep each phrase in the wording used in the text. List a concept once even if it appears many times; singular and plural forms are the same phrase (you may write "ticket / tickets").
4. One sentence can give rows under more than one rule; list each. "There are two kinds of rooms: singles and suites" gives "two" (rule 5), "kinds of rooms" (rule 2) and "singles and suites are two kinds of rooms" (rule 9).
5. Before answering, re-scan the whole description for phrases you skipped, especially passive verbs, adjectives that express a rule or state, and quantities.
6. Then check every row and delete or move the rows that fail:
   a. Is the same concept already listed under this rule in another form (singular/plural, with an adjective in front, another form of the same verb)? Keep one row.
   b. Is it a word you took out of a longer phrase you already listed (the noun "cleaning" out of "cleaning of rooms", the adjective "late" out of "late checkout")? Delete it unless the text also uses it on its own, or it is one of two or more alternatives the text names for the same noun.
   c. Is it part of the business operation, not background narrative or the software?
   d. Is it under the right rule (kinds are nouns; states and choices are rule 4; numbers are rule 5; actions are rule 3)?

# Constraints
- Only list phrases that literally appear in the description.
- Do not add explanations. The phrase cell holds only the phrase, never a quoted sentence or a note in parentheses.

# Business description
"""
{{DESCRIPTION}}
"""

# Output format
Output one markdown table with exactly the columns | rule | phrase |, one row per phrase, and nothing after it.

```
