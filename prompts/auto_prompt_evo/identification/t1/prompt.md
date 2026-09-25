# Task
You are a domain modeling expert performing Step 2 of domain modeling (brainstorming). Read the business description below and identify every DOMAIN-SPECIFIC phrase in it.

## Business Description

<DESCRIPTION>

## What makes a phrase domain-specific
A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

## Categories (use the rule number in your output)
1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories. An adjective in front of a listed noun does not make a new noun — list the base noun separately and the adjective under rule 4 if it qualifies.
2. "X of Y" expressions: every literal "<noun> of <noun>" in the text (e.g., "date of birth", "number of seats"). Only the preposition "of" counts, and "a number of X" is an indefinite quantity (rule 5), not an X of Y. Also capture "types of X", "forms of X", "kinds of X" as rule 2 expressions.
3. Transitive verbs: action verbs performed by or on domain entities, in every grammatical position (after modals, in passives, in infinitives, as gerunds, and every verb of a coordinated list). Write the verb with its particle or preposition but without its object. List each verb once, whatever its tense or voice. Include verbs like "show", "keep", "extend", "read", "identify", "cover", "belong to", "involve", "visit", "give", "prepare", "add", "remove".
4. Adjectives, enumerations: state-describing adjectives and conditional attributes that govern business rules or domain states (e.g., valid, daily, cancelled), and each item of a list of alternatives the business keeps (kinds or variants of an entity, ways something is done, life-cycle steps). One value per row. Include specific named values such as language names (e.g., French), channel names (e.g., in person, by phone), and lifecycle states (e.g., pending, opened).
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases that constrain domain entities (e.g., "a number of", "less than 8", "maximum of 8", "at least two", "each", "one or more", "several"). Write only the quantity expression, not the noun it counts. Numbers go under rule 5, never rule 4.
6. Possession expressions: has / have / possess statements between domain concepts (e.g., "has a color"). Write the whole expression. Keep these SHORT — write only "X has Y" without elaboration. Do NOT duplicate rule 2 or rule 1 content here unnecessarily; only capture the most important has/have relationships.
7. "Consist of / part of" expressions: "made up of", "consists of", "is part of", "comprises", "is composed of", "involves", "including". Write only the expression keyword, not the full sentence, unless the full phrase is needed for clarity.
8. Containment / containing expressions: "contains", "holds".
9. "X is a Y" expressions (generalization/specialization), including equivalent wording such as "is known as", "is considered a", "is a kind of", "there are N types of X", "can be regarded as". Write the whole expression naming both sides.

## Scope
- Exclude general software capabilities or infrastructure verbs (support, provide, allow, suggest, display, store) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays or suggests; the business keeping information about its entities is still in scope.
- Exclude background narrative that is not part of the business operation: the business's history, success, costs, market conditions, motives for building the system.
- Exclude names of specific real-world instances used only as illustrations (e.g., a specific city name used as an example).
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, modern, convenient, famous).

## Critical extraction rules
- **Verbs**: Be thorough. Extract ALL action verbs that domain entities perform or undergo, including: show, keep, extend, read, identify, cover, belong to, visit, give, prepare, add, remove, involve, include, denote, honor, settle, open, void, branch out into.
- **Nouns**: Extract ALL domain nouns including abstract ones: records, details, membership, current loan, update, creation, promotion, design, services, products, evaluation, review, options, transmission, other forms.
- **Rule 4 enumerations**: Each item in a list of alternatives gets its own row. Named states like "pending" (not just "pending review"), "opened", "in person", "by phone", "invited", "selected" each get their own row.
- **Rule 5 quantities**: Capture ALL quantity words: "each", "several", "one or more", "a number of", "two", "four", plus compound expressions like "maximum of 8".
- **Rule 7**: Write the keyword expression only (e.g., "made up of", "involves", "including") not the full sentence.
- **Rule 6**: Do NOT over-generate. Only write the most semantically important has/have relationships. Do not write one for every property already captured under rules 1 and 2.
- **Avoid duplication across rules**: A phrase captured under rule 2 ("size of the booth") need not also appear under rule 6. A noun captured under rule 1 need not be repeated under rule 6 as a possession expression unless the relationship itself is the key fact.
- **Singular/plural**: List each concept once; singular and plural are the same phrase. Use the form that appears in the text.

# Output
Output **raw CSV text** with exactly this header row, followed by one row per phrase. Output nothing else after the data rows.

rule,phrase

## Rules
- Copy each phrase verbatim from the description, in the wording the description uses.
- List each concept once, even if the description repeats it; singular and plural are the same phrase.
- One phrase per row. Do not merge several phrases into one row.
- Do not invent phrases that do not appear in the description.
- No prose, no explanation, no markdown, no code fences. CSV text only.

## Example
For the sentence "A clinic schedules appointments for patients. Each appointment has a time of day. An appointment can be cancelled online or at the desk.", the rows include:

rule,phrase
1,clinic
1,appointment
1,patient
2,time of day
3,schedules
4,cancelled
4,online
4,at the desk
5,each
6,appointment has a time of day