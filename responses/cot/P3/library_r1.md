## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | library |
| 1 | customer |
| 1 | member |
| 1 | membership card |
| 1 | member number |
| 1 | name |
| 1 | address |
| 1 | date of birth |
| 1 | subject section |
| 1 | classification mark |
| 1 | bar code |
| 1 | loan item |
| 1 | language tape |
| 1 | book |
| 1 | title language |
| 1 | level |
| 1 | title |
| 1 | author |
| 1 | loan |
| 1 | records |
| 1 | update |
| 2 | date of birth |
| 2 | number of items on loan |
| 2 | update of records |
| 3 | issue / issued (to) |
| 3 | shows |
| 3 | kept |
| 3 | denoted by |
| 3 | identified by |
| 3 | borrow |
| 3 | reserve / reserved |
| 3 | renew / renewed |
| 3 | extend |
| 3 | scanned |
| 3 | entered |
| 3 | read |
| 3 | stamped |
| 3 | search for |
| 4 | valid |
| 4 | daily |
| 5 | a number of |
| 5 | two |
| 5 | maximum of 8 |
| 5 | less than 8 |
| 6 | a language tape has a title language, and level |
| 6 | a book has a title, and author(s) |
| 7 | library is made up of subject sections |
| 9 | customer is known as a member |
| 9 | language tapes and books are two types of loan items |

## Step 2: Classification reasoning

library -> class : independent business entity, holds sections and processes loans
customer -> class : independent entity with kept personal details
member -> alias of customer : same entity, "known as" not a differing subclass
membership card -> class : document issued to customer, holds identifying number
member number -> attribute of membership card : identifying number of a document
name -> attribute of customer : scalar personal detail
address -> attribute of customer : scalar personal detail
date of birth -> attribute of customer : scalar personal detail (also rule 2)
subject section -> class : independent part of the library
classification mark -> attribute of subject section : identifying code
bar code -> attribute of loan item : identifying code
loan item -> class : independent object customers borrow
language tape -> subclass (class + I) : kind of loan item with its own attributes
book -> subclass (class + I) : kind of loan item with its own attributes
title language -> attribute of language tape : scalar property
level -> attribute of language tape : scalar property
title -> attribute of book : scalar property
author -> attribute of book : scalar property
loan -> association class : occurrence of borrowing, subject of renew action
records -> excluded : vague, refers to system data, not a domain entity
update -> excluded : software/batch process, infrastructure
date of birth -> attribute of customer : duplicate of rule-1 entry, one row kept
number of items on loan -> not modeled : counts current loans, no multiplicity label available
update of records -> excluded : software batch process, not domain concept
issue / issued (to) -> merged : "issue" of item = "borrow"; "issue" of card = association issued to
shows -> dropped : intra-class link already captured as attribute of card
kept -> dropped : maps to attributes already listed (name, address, dob)
denoted by -> dropped : maps to attribute classification mark
identified by -> dropped : maps to attribute bar code
borrow -> association : customer borrows loan item, root of loan association class
reserve / reserved -> association : customer reserves loan item
renew / renewed -> attribute of loan : action performed on the loan occurrence
extend -> dropped : same action as renew, not separate
scanned -> dropped : bar-code-reader/UI process step, infrastructure
entered -> dropped : manual data entry, infrastructure/UI
read -> dropped : bar-code-reader/UI process step, infrastructure
stamped -> dropped : physical clerical step, no second class involved
search for -> association : library searches for a loan item
valid -> attribute value (boolean attribute valid) of membership card : membership status
daily -> dropped : describes a system batch job, infrastructure
a number of -> dropped : indefinite quantity, no multiplicity label available
two -> dropped : cardinality already expressed via the two subclasses
maximum of 8 -> not modeled : numeric bound, no multiplicity label in schema
less than 8 -> not modeled : duplicate bound of "maximum of 8"
a language tape has a title language, and level -> attributes of language tape : possession gives scalar properties
a book has a title, and author(s) -> attributes of book : possession gives scalar properties
library is made up of subject sections -> aggregation : whole/part relationship, section part of library
customer is known as a member -> alias, not inheritance : same entity, no distinguishing attributes
language tapes and books are two types of loan items -> inheritance : subclasses with their own attributes

## Step 3: Review

- Kept "customer" as the single class name (not "member"); confirmed no separate attributes/relations distinguish "member," so no inheritance created for it.
- Confirmed "language tape" and "book" each have distinct attributes and are correctly modeled as subclasses (C + I), not enumerated values.
- Merged "issue" (of loan item) into the "borrow" association/association-class, and kept a separate "issued to" association for the membership card, avoiding duplicate associations for the same lending act.
- Dropped "shows," "kept," "denoted by," "identified by" as verbs since they only restate attribute ownership already captured.
- Dropped process/UI steps (scanned, entered, read, stamped) and infrastructure/background items (bar code reader, records, update, daily) as non-domain or already covered.
- Recognized "loan" as an association class (many customers ↔ many items over time) since "renew" acts on the borrowing occurrence itself; added attribute "renew" to it.
- Numeric bounds ("maximum of 8," "less than 8," "a number of," "two") are business rules but have no corresponding label in the schema, so they are not represented as separate rows.
- Verified every attribute has exactly one owning class, every association connects two listed classes, and the association class has its matching AS row and an attribute.

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
| A | name | customer | |
| A | address | customer | |
| A | date of birth | customer | |
| A | member number | membership card | |
| A | valid | membership card | |
| A | classification mark | subject section | |
| A | bar code | loan item | |
| A | title language | language tape | |
| A | level | language tape | |
| A | title | book | |
| A | author | book | |
| A | renew | loan | |
| AS | issued to | membership card | customer |
| AS | borrow | customer | loan item |
| AS | reserve | customer | loan item |
| AS | search for | library | loan item |
| AC | loan | customer | loan item |
| AG | Part-of | subject section | library |
| I | ISA | language tape | loan item |
| I | ISA | book | loan item |