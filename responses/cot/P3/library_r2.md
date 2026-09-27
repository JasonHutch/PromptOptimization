## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | library |
| 1 | loan item |
| 1 | customer |
| 1 | member |
| 1 | membership card |
| 1 | member number |
| 1 | membership number |
| 1 | name |
| 1 | address |
| 1 | date of birth |
| 1 | subject section |
| 1 | classification mark |
| 1 | bar code |
| 1 | language tape |
| 1 | book |
| 1 | title language |
| 1 | level |
| 1 | title |
| 1 | author |
| 1 | loan |
| 1 | bar code reader |
| 1 | records |
| 2 | date of birth |
| 2 | number of items on loan |
| 2 | update of records |
| 3 | issues |
| 3 | is issued (issued to) |
| 3 | shows |
| 3 | kept |
| 3 | denoted by |
| 3 | identified by |
| 3 | borrow |
| 3 | reserved |
| 3 | renewed |
| 3 | scanned |
| 3 | entered |
| 3 | read |
| 3 | stamped |
| 3 | searched |
| 4 | valid |
| 4 | daily |
| 4 | French |
| 4 | beginner |
| 5 | a number of |
| 5 | two |
| 5 | maximum of 8 |
| 5 | less than 8 |
| 6 | has a title language, and level |
| 6 | has a title, and author(s) |
| 7 | made up of |
| 9 | customer is known as a member |
| 9 | language tapes and books are two types of loan items |

## Step 2: Classification reasoning

library -> C : independent operating entity of the domain
loan item -> C : superclass, has own attribute bar code and subtypes
customer -> C : independent person tracked by library, keeps their own data
member -> merged into customer : alias introduced by "known as", same concept
membership card -> C : document issued to customer, holds its own number
member number -> merged with membership number : same concept, different wording
membership number -> A of membership card : identifying number belongs to the document
name -> A of customer : scalar property of customer
address -> A of customer : scalar property of customer
date of birth -> A of customer : scalar property of customer
subject section -> C : independent organizational unit of library
classification mark -> A of subject section : identifies a section
bar code -> A of loan item : identifying code of the item
language tape -> C, I to loan item : kind with its own attributes title language/level
book -> C, I to loan item : kind with its own attributes title/author
title language -> A of language tape : scalar property
level -> A of language tape : scalar property
title -> A of book : scalar property
author -> A of book : scalar property
loan -> AC : occurrence of borrow with its own state/actions
bar code reader -> discard : input device, software/infra detail
records -> discard : vague, generic system data
date of birth -> A of customer : same as rule-1 decision
number of items on loan -> discard : duplicate, expressed as multiplicity max 8
update of records -> discard : generic batch processing, not domain rule
issues -> merged into borrow : same fact as customer borrowing item
is issued (issued to) -> AS : membership card issued to customer
shows -> discard : duplicate, membership number already attribute of card
kept -> discard : just states attributes are recorded
denoted by -> discard : duplicate, classification mark already attribute
identified by -> discard : duplicate, bar code already attribute
borrow -> AS : core association between customer and loan item
reserved -> V of status : one of the states of a loan occurrence
renewed -> V of status : one of the states of a loan occurrence
scanned -> discard : data-entry/device detail, not domain rule
entered -> discard : data-entry detail
read -> discard : data-entry detail
stamped -> A of loan : action recorded on the loan occurrence
searched -> discard : generic system search capability
valid -> A of membership card : boolean state of the card
daily -> discard : part of discarded "update of records"
French -> discard : example value only, not enumerated list
beginner -> discard : example value only, not enumerated list
a number of -> multiplicity : indefinite quantity on library/section aggregation
two -> discard : just introduces the two subtypes, no separate value
maximum of 8 -> multiplicity : bound on customer-loan item association
less than 8 -> duplicate of maximum of 8 : same business rule
has a title language, and level -> possession realized as attributes of language tape
has a title, and author(s) -> possession realized as attributes of book
made up of -> AG : subject section part of library
customer is known as a member -> alias, not inheritance : same concept, no new class
language tapes and books are two types of loan items -> I : both are kinds of loan item

## Step 3: Review

- Merged "member number" and "membership number" into a single attribute "membership number" of membership card (kept name used most).
- Kept "customer" as the class name (used most and throughout) rather than "member"; no separate class or inheritance created for "member".
- Removed "bar code reader", "records"/"update of records", "searched", "scanned", "entered", "read", "daily" as software/data-entry/infra details, not real business classes or rules.
- Removed "shows", "kept", "denoted by", "identified by" as duplicates already captured by attributes (membership number, classification mark, bar code).
- Removed "French" and "beginner" as example values, not enumerated lists; kept "title language" and "level" as plain attributes.
- Merged "issues" with "borrow" into one association; created association class "loan" for the customer–loan item borrow relationship since it is many-to-many over time and carries its own state (status) and action (stamped).
- Modeled "borrowed/reserved/renewed" as values of a "status" attribute of the loan association class, not as separate classes.
- Modeled "maximum of 8" / "less than 8" as the same multiplicity constraint on the borrow association; dropped "number of items on loan" as a duplicate of this constraint.
- Verified every association, aggregation and inheritance row connects only to classes listed as C or AC.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | library | | |
| C | customer | | |
| C | membership card | | |
| C | subject section | | |
| C | loan item | | |
| C | language tape | | |
| C | book | | |
| A | membership number | membership card | |
| A | valid | membership card | |
| A | name | customer | |
| A | address | customer | |
| A | date of birth | customer | |
| A | classification mark | subject section | |
| A | bar code | loan item | |
| A | title language | language tape | |
| A | level | language tape | |
| A | title | book | |
| A | author | book | |
| A | status | loan | |
| A | stamped | loan | |
| V | borrowed | status | |
| V | reserved | status | |
| V | renewed | status | |
| AS | issued to | membership card | customer |
| AS | borrow | customer | loan item |
| AC | loan | customer | loan item |
| AG | Part-of | subject section | library |
| I | ISA | language tape | loan item |
| I | ISA | book | loan item |