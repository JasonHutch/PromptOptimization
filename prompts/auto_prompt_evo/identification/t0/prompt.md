# Task
You are a domain modeling expert performing Step 2 of domain modeling (brainstorming). Read the business description below and identify every DOMAIN-SPECIFIC phrase in it.

## Business Description

<DESCRIPTION>

## What makes a phrase domain-specific
A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

## Categories (use the rule number in your output)
1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories. An adjective in front of a listed noun does not make a new noun.
2. "X of Y" expressions: every literal "<noun> of <noun>" in the text (e.g., "date of birth", "number of seats"). Only the preposition "of" counts, and "a number of X" is an indefinite quantity (rule 5), not an X of Y.
3. Transitive verbs: action verbs performed by or on domain entities, in every grammatical position (after modals, in passives, in infinitives, as gerunds, and every verb of a coordinated list). Write the verb with its particle or preposition but without its object. List each verb once, whatever its tense or voice.
4. Adjectives, enumerations: state-describing adjectives and conditional attributes that govern business rules or domain states (e.g., valid, daily, cancelled), and each item of a list of alternatives the business keeps (kinds or variants of an entity, ways something is done, life-cycle steps). One value per row.
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases that constrain domain entities (e.g., "a number of", "less than 8", "maximum of 8", "at least two"). Write only the quantity expression, not the noun it counts. Numbers go under rule 5, never rule 4.
6. Possession expressions: has / have / possess statements between domain concepts (e.g., "has a color"). Write the whole expression.
7. "Consist of / part of" expressions: "made up of", "consists of", "is part of", "comprises", "is composed of".
8. Containment / containing expressions: "contains", "holds".
9. "X is a Y" expressions (generalization/specialization), including equivalent wording such as "is known as", "is considered a", "is a kind of", "there are N types of X". Write the whole expression naming both sides.

## Scope
- Exclude general software capabilities or infrastructure verbs (support, provide, allow) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays, suggests or stores; the business keeping information about its entities is still in scope.
- Exclude background narrative that is not part of the business operation: the business's history, success, costs, market conditions, motives for building the system.
- Exclude names of specific real-world instances used only as illustrations.
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, modern, convenient).

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
6,appointment has a time of day
