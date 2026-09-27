---
title: "Optimized Methodology for Classifying Domain-Specific Phrases"
subtitle: "Team Four · CSE 4392/5320 · final version (classification prompt P3)"
---

**Evaluated against the expert solutions (F1):** library 70.8 (mean of 3 runs), NTSS 64.3 (mean of 2 runs), car rental 47.2 (mean of 2 runs). LLM: Claude (claude.ai, default tier). Baseline (P0, the team's t1 prompt): library 30.4.

This methodology extends the course's *Classification Rules* (Step 3 of AUM domain modeling), the assignment's association-class conditions and the domain model review checklist. Section 3 lists every change and its evidence; Section 4 explains why iteration stopped below 90%. Section 5 is the exact prompt.

# 1. Inputs

1. The business description (context only).
2. The brainstormed domain-specific phrases. Each has a rule number giving its phrase category:
   1 noun/noun phrase, 2 "X of Y", 3 transitive verb, 4 adjective/enumeration, 5 numeric/quantity,
   6 possession, 7 consist of/part of, 8 containment, 9 "X is a Y".

# 2. Classification rules

| phrase category | classify as |
|---|---|
| 1 noun / noun phrase | class or attribute (see the class-vs-attribute tests) |
| 2 "X of Y" | X is an attribute of Y, or X is part of Y, or X is a role in an association |
| 3 transitive verb | association relationship between the subject's class and the object's class |
| 4 adjective, enumeration | attribute value |
| 5 numeric, quantity | attribute value, or a multiplicity |
| 6 possession (has/have) | aggregation, association, or attribute |
| 7 consist of / part of | aggregation relationship |
| 8 containment | association or aggregation |
| 9 "X is a Y" | inheritance |

## Naming

- Name every element with the words of the description, in lower case with spaces (e.g., "order line", "date of arrival"). Do not invent synonyms.
- When the description gives two names for one concept (e.g., "each client is known as a patron"), use the name introduced first and used most, and do not create a second class.
- A property you create to hold listed values may be given a plain noun name (e.g., "category", "grade", "kind").

## Class or attribute?

- An object has an independent existence in the application domain; an attribute does not. "Number of seats" is an attribute because it cannot exist without a car, airplane or classroom.
- Attributes describe objects or store their state, and are scalar types (int, double, string, char, boolean). Classes are not scalar.
- You can type an attribute value on a keyboard; you cannot type an object. Objects are created by invoking a constructor.
- Every attribute belongs to exactly one class. Never use a class as an attribute type; relate the two classes instead.
- Documents and cards the business hands out, signs or mails (e.g., a ticket, a permit, a receipt) are classes. Their identifying numbers are attributes of the document, not of its holder.
- Do not invent attributes that are not in the phrases or the description.

## Attribute values

- When adjectives or enumeration values describe the same property (e.g., "red, green" describe color), output the property as an attribute (A) of its class and each value as an attribute value (V) of that attribute. Name the attribute after the property even if the text only states the values.
- Output V rows only for a closed list of alternatives the description states ("A or B", "X, Y, or Z", a list of statuses). A value given only as an example ("e.g. red") is not a V row. A numeric limit (e.g., "a maximum of 5") is a multiplicity, not an attribute or value.
- A state that is simply true or false for an object (e.g., paid, cancelled, overdue) is a boolean attribute named by the state.

## Kinds of a concept: attribute value or subclass?

- Create subclasses only when the description gives a kind something of its own that the general class does not have: its own attributes, relationships or business rules (e.g., a discount, a fee, an action only that kind performs). Output each as C plus an I row to the general class.
- Kinds that differ only by name or by a value (e.g., "single" and "double" rooms, "red" and "blue" cars) are values (V) of an attribute of the general class, not subclasses.
- Kinds named by an adjective (rule 4, e.g., "senior" and "junior" nurses) are always values of a type attribute, never subclasses.

## Relationships

- Inheritance (I): one concept is a generalization of the other. Check both tests: IS-A (every instance of the subclass is an instance of the superclass) and conformance (the superclass's relationships also hold for the subclass). A car is not an engine.
- Aggregation (AG): one object is part of another (an engine is part of a car). Use it for a whole made of members or parts: "made up of", "a team of players", "a batch of orders". A list of steps that make up an activity is not aggregation unless the parts are objects belonging to the whole.
- Association (AS): any other application-specific relationship, usually named by a domain-specific transitive verb (e.g., faculty teach course, user has account). Name it with the verb as the description writes it, including its preposition (e.g., "assigned to", "approved by", "has"), and list the subject class then the object class. Both classes must be classes you output. Connect it to the class the sentence names: when the sentence names the general concept (e.g., "equipment can be leased"), use the general class, not one of its subclasses.

## Association classes
Create an association class (AC) from an association between two classes only when BOTH hold:

1. The association is many-to-many (a student may enroll in many courses and a course has many students), and
2. Information about the association itself, not about either class, must be kept (e.g., the grade of a student in a course).
Name the association class with the noun form of the association (enroll -> Enrollment), or with the noun the description already uses for it. List its two participating classes.
Check every association against both conditions; do not skip this. Strong signals of an association class:

- the description has a noun for one occurrence of the relationship (e.g., an enrollment, a booking, a subscription, an appointment), or
- other verbs act on the occurrence rather than on either class (e.g., an appointment is rescheduled or cancelled).
The information kept about an occurrence (e.g., the dates of the actions performed on it, its state) are attributes of the association class.
Output an association class as three things: the association (AS row) it belongs to, the association class (AC row) with its two participating classes, and its attributes (A rows owned by the association class), including one attribute for each action the description performs on an occurrence, named by that action (e.g., "reschedule"). Never output the association class also as a C row.

## Review checklist (apply before you answer)

- The model contains only application-domain concepts: no user-interface, database, software-system, design-pattern or storage classes.
- Every class shows its important attributes; a class with no attributes and no relationships probably is not needed.
- No class is used as an attribute; no operations are shown.
- Two phrases that name the same concept become one element.
- Every relationship connects classes that you listed as C or AC.
- Every I row passes the kinds rule: if the subclass differs from its siblings only by a value, or its name is an adjective plus the superclass name, replace it with a type attribute and V rows.
- Every AC row has its matching AS row and at least one attribute, and is not also a C row.

## Output labels

| label | meaning | element | arg1 | arg2 |
|---|---|---|---|---|
| C | class | class name | | |
| A | attribute | attribute name | owning class | |
| V | attribute value | the value | owning attribute | |
| AS | association | verb | subject class | object class |
| AC | association class | class name | participating class | participating class |
| AG | aggregation | Part-of | part class | whole class |
| I | inheritance | ISA | subclass | superclass |

One row per element, in a table with the columns label, element, arg1, arg2.

# 3. Changes from the course rules

| Version | Change | Observed error that motivated it |
|---|---|---|
| P1 | Category-to-element mapping table, class-vs-attribute tests, IS-A and conformance tests, the two association-class conditions, review checklist, description as context | Team baseline guessed relationships without the description; 40 false positives on library |
| P2 | Naming rule (use the first name for a concept); documents are classes; attribute values only for closed lists; stricter aggregation; mandatory association-class check | "Each customer is known as a member": the class was named Member and every attribute and association on it missed (library 42.1 to 70.6) |
| P3 | Association class output with its association and attributes, never as a plain class; subclasses only when a kind has something of its own; relationships attach to the class the sentence names | Association class emitted without its association; sedan/hatchback made subclasses; associations attached to a subclass the sentence did not name |

# 4. Why classification stops below 90%

Scored with the team scorer's no-arguments mode, P3 reaches 80.0 on library and 67.7 on car rental and NTSS, against the official 69.1, 50.4 and 64.7 for the same runs. The remaining library misses are modeling choices that the description does not support:

| Expert solution | What the description says |
|---|---|
| borrow(customer, book) | "A customer may borrow up to a maximum of 8 items" |
| loan item.title | "A book has a title" |
| book.subject | not mentioned |
| hold(section, loan item) | not mentioned |
| membership card.id | "a unique member number" |

Reaching 90% would require putting these choices into the prompt, which would leak the answer key.

# 5. Final prompt (P3)

The text below is sent to the LLM with the business description and the phrase list in place of `{{DESCRIPTION}}` and `{{PHRASES}}`.

```
# Role
You are a domain modeling expert applying the Agile Unified Methodology (AUM). You are performing Step 3 of domain modeling: classifying the brainstormed domain-specific phrases into classes, attributes, attribute values and relationships.

# Inputs
1. The business description (context only).
2. The brainstormed domain-specific phrases. Each has a rule number giving its phrase category:
   1 noun/noun phrase, 2 "X of Y", 3 transitive verb, 4 adjective/enumeration, 5 numeric/quantity,
   6 possession, 7 consist of/part of, 8 containment, 9 "X is a Y".

# Classification rules (apply by phrase category)
| phrase category | classify as |
|---|---|
| 1 noun / noun phrase | class or attribute (see the class-vs-attribute tests) |
| 2 "X of Y" | X is an attribute of Y, or X is part of Y, or X is a role in an association |
| 3 transitive verb | association relationship between the subject's class and the object's class |
| 4 adjective, enumeration | attribute value |
| 5 numeric, quantity | attribute value, or a multiplicity |
| 6 possession (has/have) | aggregation, association, or attribute |
| 7 consist of / part of | aggregation relationship |
| 8 containment | association or aggregation |
| 9 "X is a Y" | inheritance |

## Naming
- Name every element with the words of the description, in lower case with spaces (e.g., "order line", "date of arrival"). Do not invent synonyms.
- When the description gives two names for one concept (e.g., "each client is known as a patron"), use the name introduced first and used most, and do not create a second class.
- A property you create to hold listed values may be given a plain noun name (e.g., "category", "grade", "kind").

## Class or attribute?
- An object has an independent existence in the application domain; an attribute does not. "Number of seats" is an attribute because it cannot exist without a car, airplane or classroom.
- Attributes describe objects or store their state, and are scalar types (int, double, string, char, boolean). Classes are not scalar.
- You can type an attribute value on a keyboard; you cannot type an object. Objects are created by invoking a constructor.
- Every attribute belongs to exactly one class. Never use a class as an attribute type; relate the two classes instead.
- Documents and cards the business hands out, signs or mails (e.g., a ticket, a permit, a receipt) are classes. Their identifying numbers are attributes of the document, not of its holder.
- Do not invent attributes that are not in the phrases or the description.

## Attribute values
- When adjectives or enumeration values describe the same property (e.g., "red, green" describe color), output the property as an attribute (A) of its class and each value as an attribute value (V) of that attribute. Name the attribute after the property even if the text only states the values.
- Output V rows only for a closed list of alternatives the description states ("A or B", "X, Y, or Z", a list of statuses). A value given only as an example ("e.g. red") is not a V row. A numeric limit (e.g., "a maximum of 5") is a multiplicity, not an attribute or value.
- A state that is simply true or false for an object (e.g., paid, cancelled, overdue) is a boolean attribute named by the state.

## Kinds of a concept: attribute value or subclass?
- Create subclasses only when the description gives a kind something of its own that the general class does not have: its own attributes, relationships or business rules (e.g., a discount, a fee, an action only that kind performs). Output each as C plus an I row to the general class.
- Kinds that differ only by name or by a value (e.g., "single" and "double" rooms, "red" and "blue" cars) are values (V) of an attribute of the general class, not subclasses.
- Kinds named by an adjective (rule 4, e.g., "senior" and "junior" nurses) are always values of a type attribute, never subclasses.

## Relationships
- Inheritance (I): one concept is a generalization of the other. Check both tests: IS-A (every instance of the subclass is an instance of the superclass) and conformance (the superclass's relationships also hold for the subclass). A car is not an engine.
- Aggregation (AG): one object is part of another (an engine is part of a car). Use it for a whole made of members or parts: "made up of", "a team of players", "a batch of orders". A list of steps that make up an activity is not aggregation unless the parts are objects belonging to the whole.
- Association (AS): any other application-specific relationship, usually named by a domain-specific transitive verb (e.g., faculty teach course, user has account). Name it with the verb as the description writes it, including its preposition (e.g., "assigned to", "approved by", "has"), and list the subject class then the object class. Both classes must be classes you output. Connect it to the class the sentence names: when the sentence names the general concept (e.g., "equipment can be leased"), use the general class, not one of its subclasses.

## Association classes
Create an association class (AC) from an association between two classes only when BOTH hold:
1. The association is many-to-many (a student may enroll in many courses and a course has many students), and
2. Information about the association itself, not about either class, must be kept (e.g., the grade of a student in a course).
Name the association class with the noun form of the association (enroll -> Enrollment), or with the noun the description already uses for it. List its two participating classes.
Check every association against both conditions; do not skip this. Strong signals of an association class:
- the description has a noun for one occurrence of the relationship (e.g., an enrollment, a booking, a subscription, an appointment), or
- other verbs act on the occurrence rather than on either class (e.g., an appointment is rescheduled or cancelled).
The information kept about an occurrence (e.g., the dates of the actions performed on it, its state) are attributes of the association class.
Output an association class as three things: the association (AS row) it belongs to, the association class (AC row) with its two participating classes, and its attributes (A rows owned by the association class), including one attribute for each action the description performs on an occurrence, named by that action (e.g., "reschedule"). Never output the association class also as a C row.

## Review checklist (apply before you answer)
- The model contains only application-domain concepts: no user-interface, database, software-system, design-pattern or storage classes.
- Every class shows its important attributes; a class with no attributes and no relationships probably is not needed.
- No class is used as an attribute; no operations are shown.
- Two phrases that name the same concept become one element.
- Every relationship connects classes that you listed as C or AC.
- Every I row passes the kinds rule: if the subclass differs from its siblings only by a value, or its name is an adjective plus the superclass name, replace it with a type attribute and V rows.
- Every AC row has its matching AS row and at least one attribute, and is not also a C row.

# Output
Output one markdown table with exactly these columns and nothing after it.

| label | element | arg1 | arg2 |
|---|---|---|---|

| label | meaning | element | arg1 | arg2 |
|---|---|---|---|---|
| C | class | class name | | |
| A | attribute | attribute name | owning class | |
| V | attribute value | the value | owning attribute | |
| AS | association | verb | subject class | object class |
| AC | association class | class name | participating class | participating class |
| AG | aggregation | Part-of | part class | whole class |
| I | inheritance | ISA | subclass | superclass |

One row per element. Use the wording of the phrases and the description. No prose, no code fences.

# Business description
"""
{{DESCRIPTION}}
"""

# Domain-specific phrases
{{PHRASES}}

```
