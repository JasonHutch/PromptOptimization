# Task
You are a domain modeling expert. Read the business description below and identify every DOMAIN-SPECIFIC phrase in it. Output ONLY raw CSV text with the header `rule,phrase` and one phrase per row. No markdown, no tables, no code fences, no commentary — just the CSV.

## Business Description

<DESCRIPTION>

## What makes a phrase domain-specific
A phrase is DOMAIN-SPECIFIC if the application domain must keep detail about it, track it, or apply business rules to it, or if its meaning would change in a different domain. Words that would appear in almost any software description (system, application, user, information, data, facility, capability, message) are NOT domain-specific.

## Categories (use the rule number in your output)
1. Nouns / noun phrases: the things, people, roles, documents and places of the business, and their properties. Include abstract nouns and nominalizations the business tracks, such as processes, states and histories.
2. "X of Y" expressions: every literal "<noun> of <noun>" in the text. Only the preposition "of" counts. Also capture "types of X", "forms of X", "kinds of X", "types of" or "kinds of" alone if that is how the text reads. "A number of X" is rule 5, not rule 2.
3. Transitive verbs: action verbs performed by or on domain entities, in every grammatical position (after modals, in passives, in infinitives, as gerunds, and every verb of a coordinated list). Write the verb with its particle or preposition but without its object. List each verb once in its base or most natural form from the text.
4. Adjectives, enumerations: state-describing adjectives and conditional attributes that govern business rules or domain states, and each item of a list of alternatives the business keeps. One value per row.
5. Numeric, quantity: numbers, cardinal bounds and indefinite quantity phrases (e.g., "a number of", "less than 8", "maximum of 8", "at least two", "each", "one or more", "several", "two", "four"). Write only the quantity expression.
6. Possession expressions: has / have / possess statements between domain concepts. Keep SHORT. When the text uses "has" generically, write just "has". Only capture specific named properties not already expressed by rule 2 (e.g., "has a title language", "has a title and author(s)").
7. "Consist of / part of" expressions: write only the keyword (e.g., "made up of", "involves", "including").
8. Containment expressions: "contains", "holds".
9. "X is a Y" expressions (generalization/specialization), including "is known as", "is considered a", "is a kind of", "can be regarded as". Write the whole expression naming both sides. If the text uses "can be regarded as" without naming both sides in that exact phrase, write just "can be regarded as".

## Critical Rules

### Rule 1 — Nouns
- Extract ALL domain nouns including abstract ones: records, details, membership, current loan, status, fee, advertisement, location, company, evaluation, review, registration, creation, promotion, design, committee, proposal, account balance, payments received, organization staff, bar code reader, book bar code, title language, other forms of vehicle, transmission, options, additional charge, rental charge, rental price, rental fleet, rental plan, reservation form, file cabinet, block reservation, contract, invoice, deposit, damage, depreciation, salesperson, credit card processing company, keynote address, reviewer, seminar, reception, conference room, booth, trade show materials, account, service charge, service provider, business customer, NTSS.
- When a compound noun appears (e.g., "book bar code", "title language", "organization staff", "payments received", "account balance", "rental location", "rental plan", "rental charge", "credit card processing company"), list it as a single noun phrase.
- When the text uses a short form and a long form of the same noun (e.g., "items" and "loan items"), list the most specific compound form.
- Extract abstract process nouns like "evaluation", "review", "registration", "creation", "promotion", "design" when the business tracks them.
- Named plan names or product names that are variants of an entity go under rule 1 (e.g., "daily unlimited miles plan", "weekend savings plan").
- Do NOT list a noun under both rule 1 and rule 4.
- An adjective in front of a listed noun does not make a new noun — list the base noun separately and the adjective under rule 4 if it qualifies.

### Rule 2 — "X of Y"
- Capture EVERY literal "noun of noun" phrase in the text exactly as it appears.
- Also capture "types of", "kinds of", "forms of" even without a following noun if that is how the text reads.
- Capture: "number of subject sections", "makes of car", "model of car", "update of records", "status of a proposal", "committee of reviewers", "depreciation of the rental cars", "size of the booth", "duration of the event", "selection of a theme", "selection of a slogan", "evaluation of their proposals", "time of reservation", "period of time", "number of items", "types of loan items", "types of participants", "types of".
- Do NOT invent rule 2 phrases that do not literally appear in the text.
- "A number of X" is rule 5, never rule 2.

### Rule 3 — Verbs
- Be thorough. Extract ALL action verbs that domain entities perform or undergo, including verbs in passive voice and gerund form.
- Valid verbs include: issues/issued, shows, kept, denoted, borrow/borrowed, reserved, renewed, extend, scanned, entered, read, stamped, searched, identified, taken from, returned to, branch out into, group into, select, rent, process/processed, archive, void, honor, make, check out/checked out, open, settle, send to/sent to, pay, repair, sign, reserve, cover, reserving, create/creates, promote/promoting, organize/organizing, run/running/runs, contact, design, invite/inviting, register/registering, set up/setting up, distribute/distributing, record, maintain, attend/attended by, exhibit, request/requested, rent/rented, review/reviewed by, give, add/added, remove/removed, belong to, charge, prepare/prepares, visit, satisfy, handle, show up.
- Write each verb once in its base or most natural form from the text (e.g., "issues" or "issued" — pick the form closest to the text).
- Do NOT invent verb phrases not in the text.
- Do NOT list "rented out" under rule 3 if it is used as a lifecycle state; put it under rule 4 only.

### Rule 4 — Adjectives / Enumerations / States
- Each item in a list of alternatives gets its own row.
- Named lifecycle states: write them EXACTLY as they appear in the text. If the text says "pending" write "pending"; if it says "pending review" write "pending review". Do NOT add words not in the state name.
- Include: available, not available, rented out, voided, opened, invited, selected, pending, accepted, rejected, automatic, manual, in person, by phone, on site, national, international, daily, valid, beginner, French, large, medium, small, sedan, hatchback, two doors, four doors, purchase, repair, maintenance, disposal (when listed as lifecycle states/categories).
- When the text says "invited and/or selected" as a combined state, list "invited and/or selected" as a single row.
- When the text lists "invited" and "selected" as separate states, list each separately.
- Do NOT put numbers here; numbers go under rule 5.
- Named plan names or product names that are variants of an entity go under rule 1, not rule 4.
- Lifecycle nouns (purchase, repair, maintenance, disposal) go under rule 4 when the text lists them as lifecycle states or categories; go under rule 1 only if the text treats them as tracked entities with their own properties.

### Rule 5 — Quantities
- Capture ALL quantity words and phrases: "each", "several", "one or more", "a number of", "two", "four", "maximum of 8", "less than 8", "up to a maximum of 8", "a small number of".
- Write only the quantity expression, not the noun it counts.
- Numbers like "two" and "four" go here, not under rule 4.
- "Each" always goes under rule 5.
- "A number of" is always rule 5, never rule 2.

### Rule 6 — Possession
- Do NOT over-generate. Only write the most semantically important has/have relationships not already captured by rule 2.
- When the text uses "has" generically (e.g., "an event has ..."), a single entry "has" is sufficient.
- When the text uses "has" to introduce a specific named property not captured elsewhere (e.g., "has a title language", "has a title and author(s)"), capture those specific short forms.
- Do NOT write "X has Y" if Y is already captured as a rule 2 "Y of X" phrase.
- Prefer brevity; prefer a single "has" over multiple redundant entries.

### Rule 7
- Write the keyword expression only (e.g., "made up of", "involves", "including") not the full sentence.

### Rule 9 — Generalization
- Write each generalization once in the most natural form from the text.
- Do not write the same relationship twice with different wording.
- When the text uses "can be regarded as" without naming both sides explicitly in that phrase, write just "can be regarded as".
- When the text names both sides (e.g., "customer is known as a member"), write the full expression.

## Scope
- Exclude general software capabilities or infrastructure verbs (support, provide, allow, suggest, display, store) unless they are a domain-specific action performed by or on a domain entity.
- Exclude what the software itself displays or suggests; the business keeping information about its entities is still in scope.
- Exclude background narrative not part of the business operation: history, success, costs, market conditions, motives.
- Exclude names of specific real-world instances used only as illustrations (e.g., a specific city name used as an example). Exception: named domain values that define a category or state (e.g., "French" as a language value) ARE in scope under rule 4 or rule 1.
- Exclude purely evaluative adjectives that do not define a state, kind or value (e.g., excellent, modern, convenient, famous).

## Avoiding duplication across rules
- A phrase captured under rule 2 ("size of the booth") need not also appear under rule 6.
- A noun captured under rule 1 need not be repeated under rule 6 as a possession expression unless the relationship itself is the key fact.
- Singular and plural are the same phrase — list each concept once using the form that appears in the text.
- If a verb appears in both active and passive forms, list it once.
- Do not split a compound noun into parts and list both; list the compound as it appears.
- Do not list a noun under both rule 1 and rule 4.
- Do not list a verb under both rule 3 and rule 4.

## Output format
Output ONLY raw CSV with header `rule,phrase`. One row per phrase. No markdown, no tables, no code fences, no explanations.

Example output:
rule,phrase
1,loan item
1,member
2,number of items
3,borrow
4,valid
5,each
6,has a title and author(s)
7,made up of
9,customer is known as a member