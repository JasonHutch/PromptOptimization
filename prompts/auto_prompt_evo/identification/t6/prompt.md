```markdown
# Task
You are a domain modeling expert performing Step 2 of domain modeling (brainstorming). Read the business description below and identify every DOMAIN-SPECIFIC phrase in it.

## Business Description

<DESCRIPTION>

## What makes a phrase domain-specific
A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

## Categories (use the rule number in your output)
1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories. An adjective in front of a listed noun does not make a new noun — list the base noun separately and the adjective under rule 4 if it qualifies. Named plan names or product names that are variants of an entity go under rule 1, not rule 4.
2. "X of Y" expressions: every literal "<noun> of <noun>" in the text (e.g., "date of birth", "number of seats"). Only the preposition "of" counts, and "a number of X" is an indefinite quantity (rule 5), not an X of Y. Also capture "types of X", "forms of X", "kinds of X" as rule 2 expressions. Capture bare "types of" or "kinds of" without the noun if that is how the text reads.
3. Transitive verbs: action verbs performed by or on domain entities, in every grammatical position (after modals, in passives, in infinitives, as gerunds, and every verb of a coordinated list). Write the verb with its particle or preposition but without its object. List each verb once, whatever its tense or voice. Include verbs like "show", "keep", "extend", "read", "identify", "cover", "belong to", "involve", "visit", "give", "prepare", "add", "remove", "sign", "make", "honor", "settle", "open", "void", "branch out into", "group into", "sent to", "checked out", "stamped", "scanned", "searched", "reserved", "renewed", "issued", "denoted".
4. Adjectives, enumerations: state-describing adjectives and conditional attributes that govern business rules or domain states (e.g., valid, daily, cancelled), and each item of a list of alternatives the business keeps (kinds or variants of an entity, ways something is done, life-cycle steps). One value per row. Include specific named values such as language names (e.g., French), channel names (e.g., in person, by phone), and lifecycle states (e.g., pending, opened, available, not available). Named lifecycle states should be listed as they appear in the text — do NOT add qualifiers (e.g., write "pending" not "pending review" if the state name is just "pending"). Named plan names or product names that are variants of an entity go under rule 1, not rule 4. Lifecycle nouns tracked as domain entities (purchase, repair, maintenance, disposal) go under rule 1 ONLY if the text treats them as tracked entities; if the text lists them as lifecycle states or categories, put them under rule 4.
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases that constrain domain entities (e.g., "a number of", "less than 8", "maximum of 8", "at least two", "each", "one or more", "several", "two", "four"). Write only the quantity expression, not the noun it counts. Numbers go under rule 5, never rule 4.
6. Possession expressions: has / have / possess statements between domain concepts (e.g., "has a color"). Write the whole expression. Keep these SHORT — write only "X has Y" without elaboration. Do NOT duplicate rule 2 or rule 1 content here unnecessarily; only capture the most important has/have relationships that are not already expressed by rule 2. When the text uses "has" generically without specifying a particular property, write just "has" as the phrase. Prefer a single short "has" over multiple redundant ones. When the text uses "has" to introduce a specific named property that is not captured elsewhere (e.g., "has a title language", "has a title and author(s)"), capture those specific short forms.
7. "Consist of / part of" expressions: "made up of", "consists of", "is part of", "comprises", "is composed of", "involves", "including". Write only the expression keyword, not the full sentence, unless the full phrase is needed for clarity.
8. Containment / containing expressions: "contains", "holds".
9. "X is a Y" expressions (generalization/specialization), including equivalent wording such as "is known as", "is considered a", "is a kind of", "there are N types of X", "can be regarded as". Write the whole expression naming both sides. If the text uses "can be regarded as" without naming both sides in that exact phrase, write just "can be regarded as". Do NOT duplicate a rule 9 expression with slight rewording — write it once in the most natural form from the text.

## Scope
- Exclude general software capabilities or infrastructure verbs (support, provide, allow, suggest, display, store) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays or suggests; the business keeping information about its entities is still in scope.
- Exclude background narrative that is not part of the business operation: the business's history, success, costs, market conditions, motives for building the system.
- Exclude names of specific real-world instances used only as illustrations (e.g., a specific city name used as an example). Exception: named domain values that define a category or state (e.g., "French" as a language value) ARE in scope under rule 4 or rule 1.
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, modern, convenient, famous).

## Critical extraction rules

### Verbs (Rule 3)
Be thorough. Extract ALL action verbs that domain entities perform or undergo, including verbs in passive voice and gerund form. Do NOT omit verbs just because they appear in passive or gerund form — "scanned", "stamped", "searched", "reserved", "renewed", "issued", "denoted", "identified", "sent to", "checked out", "processed", "visited", "prepared", "attended", "invited", "selected", "requested", "rented", "reviewed", "distributed", "exhibited", "registered", "recorded", "maintained", "created", "promoted", "organized", "run", "shown", "kept", "entered", "returned to", "taken from", "cover", "archive", "reserving", "prepares", "attended by", "reviewed by", "added", "removed" are all valid rule 3 verbs. Write each verb once in its base or most natural form from the text. Do NOT invent verb phrases not in the text (e.g., do not write "keep track of" if the text only says "keep"; do not write "kept track of" unless those exact words appear).

### Nouns (Rule 1)
Extract ALL domain nouns including abstract ones: records, details, membership, current loan, update, creation, promotion, design, services, products, evaluation, review, options, transmission, other forms of vehicle, doors, additional charge, rental price, payments received, organization staff, committee, status, fee, advertisement, location, company, rentals, bar code reader, book bar code, title language. Do not omit nouns just because they seem simple or short. When a compound noun appears (e.g., "book bar code", "title language", "organization staff", "payments received", "account balance"), list it as a single noun phrase under rule 1. When the text uses a short form and a long form of the same noun (e.g., "items" and "loan items"), list the most specific compound form. Also extract abstract process nouns like "evaluation", "review", "registration", "creation", "promotion", "design" when the business tracks them. Extract "location" and "company" as rule 1 nouns when they appear as domain concepts.

### Rule 2 — "X of Y"
Capture every literal "noun of noun" phrase in the text. Also capture "update of records", "time of reservation", "model of car", "status of a proposal", "committee of reviewers", "depreciation of the rental cars", "number of subject sections", "selection of a theme", "selection of a slogan", "evaluation of their proposals", "duration of the event", "size of the booth" etc. Do NOT capture "a number of X" here (that is rule 5). When the text says "makes of car" or "models of car", capture those exact forms. Capture "types of" or "kinds of" even without a following noun if that is how the text reads. Do NOT invent rule 2 phrases that do not literally appear in the text.

### Rule 4 — Enumerations and states
- Each item in a list of alternatives gets its own row.
- Named lifecycle states: write them EXACTLY as they appear in the text. If the text says "pending" write "pending"; if it says "pending review" write "pending review". Do NOT add words that are not in the state name itself.
- Include: available, not available, rented out, voided, opened, invited, selected, pending, accepted, rejected, automatic, manual, in person, by phone, on site, national, international, daily, valid, beginner, French, large, medium, small, sedan, hatchback, two doors, four doors.
- Do NOT put numbers here; numbers go under rule 5.
- When the text lists items like "purchase, repair, maintenance, disposal" as lifecycle categories or states of a vehicle, put them under rule 4. If the text treats them as tracked domain entities with their own properties, put them under rule 1.
- Named plan names or product names that are variants of an entity go under rule 1 (e.g., "daily unlimited miles plan", "weekend savings plan" are rule 1 nouns).
- When the text says "invited and/or selected" as a combined state, list "invited and/or selected" as a single row unless the text also lists them separately.
- When the text lists "invited" and "selected" as separate states, list each separately.

### Rule 5 — Quantities
Capture ALL quantity words and phrases: "each", "several", "one or more", "a number of", "two", "four", "maximum of 8", "less than 8", "up to a maximum of 8". Write only the quantity expression. Numbers like "two" and "four" go here, not under rule 4. The word "each" always goes under rule 5. "A number of" is always rule 5, never rule 2.

### Rule 6 — Possession
Do NOT over-generate. Only write the most semantically important has/have relationships that are not already captured by rule 2. When the text uses "has" generically (e.g., "an event has ..."), a single entry "has" is sufficient rather than enumerating every property. Do not write one for every property already captured under rules 1 and 2. Prefer brevity. When the text uses "has" to introduce a specific named property that is not captured elsewhere (e.g., "has a title language", "has a title and author(s)"), capture those specific short forms. Do NOT write "X has Y" if Y is already captured as a rule 2 "Y of X" phrase.

### Rule 7
Write the keyword expression only (e.g., "made up of", "involves", "including") not the full sentence.

### Rule 9 — Generalization
Write each generalization once in the most natural form from the text. Do not write the same relationship twice with different wording. When the text groups multiple subtypes together (e.g., "X and Y are two types of Z"), write that as a single row. When the text uses "can be regarded as" without naming both sides explicitly in that phrase, write just "can be regarded as" as the phrase. When the text names both sides (e.g., "customer is known as a member"), write the full expression.

### Avoiding duplication across rules
- A phrase captured under rule 2 ("size of the booth") need not also appear under rule 6.
- A noun captured under rule 1 need not be repeated under rule 6 as a possession expression unless the relationship itself is the key fact.
- Singular and plural are the same phrase — list each concept once using the form that appears in the text.
- If a verb appears in both active and passive forms, list it once.
- Do not split a compound noun into parts and list both; list the compound as it appears.
- Do not list a noun under both rule 1 and rule 4.
- Do not list a verb under both rule 3 and rule 4 (e.g., "borrowed" as a state goes under rule 4 only if it is a lifecycle state; as an action verb it goes under rule 3).
- Do not list "rented out" under both rule 3 and rule 4; if it is a lifecycle state, put it under rule 4 only.

### Common mistakes to avoid
- DO NOT classify named plan names (e.g., "daily unlimited miles plan", "weekend savings plan") under rule 4; they are rule 1 nouns.
- DO NOT add qualifiers to lifecycle state names that do not appear in the text (e.g., write "pending" not "pending review" unless the text literally says "pending review").
- DO capture "each" and bare number words ("two", "four") under rule 5.
- DO capture abstract nouns like "evaluation", "review", "current loan", "payments received", "organization staff", "committee", "status", "fee", "advertisement", "membership", "details", "options", "rentals", "location", "company", "bar code reader", "book bar code", "title language", "transmission", "other forms of vehicle" under rule 1 when they appear.
- DO capture "shows" / "show", "visit", "cover", "sent to", "checked out", "denoted", "stamped", "scanned", "searched", "identified", "reserved", "renewed", "issued", "prepared", "attended", "invited", "selected", "requested", "rented", "distributed", "exhibited", "kept", "entered", "returned to", "taken from", "pay", "give", "prepares", "archive", "reserving", "attended by", "reviewed by", "added", "removed" as rule 3 verbs when they appear in the text.
- DO capture "can be regarded as" as a rule 9 expression (write just "can be regarded as" if the text does not name both sides in that phrase).
- When the text uses "has" generically to introduce properties of an entity, a single short rule 6 entry "has" is preferred over many specific "X has Y" entries.
- For rule 2, capture "number of subject sections", "makes of car", "model of car", "update of records", "status of a proposal", "committee of reviewers", "depreciation of the rental cars", "types of", "size of the booth", "duration of the event" etc. exactly as they appear.
- DO capture compound nouns like "title language", "book bar code", "organization staff", "payments received", "account balance" as single rule 1 entries.
- DO capture "involves" and "including" as rule 7 keywords when they appear.
- DO NOT generate rule 2 entries for phrases that do not literally appear in the text.
- DO NOT generate rule 3 entries for verbs that do not appear in the text (e.g., do not invent "keep track of" if the text says "keep"; do not invent "kept track of" unless those exact words appear).
- DO NOT generate rule 1 entries for nouns that do not appear in the text.
- For rule 4, when the text says "invited and/or selected" treat that as a single combined state value unless the text also lists them separately.
- For rule 9, when the text says "can be regarded as" without naming both sides in that exact phrase, write just "can be regarded as".
- DO capture "other forms of vehicle" or similar "other forms of X" phrases as rule 1 nouns when they appear.
- DO capture "location" as a rule 1 noun when the text uses it as a domain concept (e.g., rental location).
- DO capture "company" as a rule 1 noun when the text uses it as a domain concept (e.g., credit card processing company).
- For rule 3, "returned to" and "taken from" are valid verb+preposition forms when they appear in the text.
- DO capture "payments received" as a rule 1 compound noun when it appears.
- DO capture "each" under rule 5 whenever it appears in the text.
- DO NOT list "rented out" under rule 3 if it is used as a lifecycle state; put it under rule 4 only.
- DO NOT over-generate rule 2 entries for phrases like "number of rental locations", "number of rental plans", "number of price classes", "forms of vehicle rentals" unless those exact phrases appear verbatim in the text.
- DO NOT over-generate rule 6 entries; prefer a single "has" entry when the text uses "has" generically.
- DO capture "