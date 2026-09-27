## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | library |
| 1 | loan item |
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
| 1 | language tape |
| 1 | title language |
| 1 | level |
| 1 | book |
| 1 | title |
| 1 | author(s) |
| 1 | membership number |
| 1 | loan |
| 2 | date of birth |
| 2 | number of subject sections |
| 2 | number of items on loan |
| 3 | issues |
| 3 | shows |
| 3 | denoted by |
| 3 | identified by |
| 3 | borrow |
| 3 | extend |
| 3 | scanned |
| 3 | entered |
| 3 | read |
| 3 | stamped |
| 3 | issued |
| 3 | searched |
| 4 | valid |
| 4 | reserved |
| 4 | borrowed |
| 4 | renewed |
| 4 | daily |
| 5 | maximum of 8 |
| 5 | less than 8 |
| 6 | has a title language, and level |
| 6 | has a title, and author(s) |
| 7 | made up of |
| 9 | customer is known as a member |
| 9 | language tapes and books are two types of loan item |

## Step 2: Classification reasoning

library -> C : independent business entity, owns sections
loan item -> C : identified by bar code, has independent existence
customer -> C : primary business actor with attributes
member -> merge into customer : same concept, "customer" used first/most
membership card -> C : document issued to customer, holds its own number
member number -> A : identifying attribute of membership card
name -> A : attribute of customer
address -> A : attribute of customer
date of birth -> A : attribute of customer
subject section -> C : part of library, has its own attribute
classification mark -> A : identifying attribute of subject section
bar code -> A : identifying attribute of loan item
language tape -> C : subclass, specific kind of loan item
title language -> A : attribute of language tape
level -> A : attribute of language tape
book -> C : subclass, specific kind of loan item
title -> A : attribute of book
author(s) -> A : attribute of book
membership number -> merge into member number : same concept restated
loan -> AC : occurrence of borrow relation, needs status kept
date of birth (X of Y) -> A : same as above, attribute of customer
number of subject sections -> not modeled : generic quantity, covered by aggregation
number of items on loan -> not modeled : derived count, represented via loan multiplicity
issues -> covered by AC loan : issuing action is the loan occurrence itself
shows -> not separate AS : just exposes attribute member number
denoted by -> not separate AS : expresses attribute classification mark
identified by -> not separate AS : expresses attribute bar code
borrow -> AS/AC basis : core relation modeled as Loan association class
extend -> not separate AS : renew action reflected in loan status
scanned -> excluded : procedural UI/device action, not persistent relation
entered -> excluded : procedural UI/device action
read -> excluded : procedural UI/device action
stamped -> excluded : procedural/physical action, not a lasting relationship
issued -> covered by AC loan : status/occurrence of loan
searched -> excluded : generic system search facility
valid -> A/V : boolean-like attribute of membership card
reserved -> V : value of loan status attribute
borrowed -> V : value of loan status attribute
renewed -> V : value of loan status attribute
daily -> excluded : describes generic record-update facility, not domain rule
maximum of 8 -> multiplicity : bounds loan association, not separate element
less than 8 -> multiplicity : same constraint, not separate element
has a title language, and level -> A : language tape attributes (rule6 confirmed)
has a title, and author(s) -> A : book attributes (rule6 confirmed)
made up of -> AG : subject section is part of library
customer is known as a member -> naming decision : confirms merge, not separate element
language tapes and books are two types of loan item -> I : both ISA loan item

## Step 3: Review

- Merged "member" into "customer" (same concept, first name kept).
- Merged "membership number" into "member number" (same attribute, restated).
- Excluded "bar code reader", "scanned", "entered", "read", "stamped", "searched", "daily update of records" as UI/device/generic process actions, not domain relationships.
- Modeled "loan" as an association class (Loan) between Customer and Loan Item because the relation is many-to-many over time and its own state (status: borrowed/reserved/renewed) must be tracked — satisfies both association-class conditions.
- Treated "maximum of 8" / "less than 8" as a business constraint on the Loan association rather than a standalone attribute (not invented as new attribute).
- Verified every attribute has exactly one owning class, and every association/aggregation/inheritance connects only listed classes.
- Kept Membership Card as its own class (document issued to customer) rather than folding member number into Customer, per document-class rule.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | library | | |
| C | subject section | | |
| C | customer | | |
| C | membership card | | |
| C | loan item | | |
| C | book | | |
| C | language tape | | |
| AC | loan | customer | loan item |
| A | classification mark | subject section | |
| A | name | customer | |
| A | address | customer | |
| A | date of birth | customer | |
| A | member number | membership card | |
| A | valid | membership card | |
| A | bar code | loan item | |
| A | title | book | |
| A | author(s) | book | |
| A | title language | language tape | |
| A | level | language tape | |
| A | status | loan | |
| V | reserved | status | |
| V | borrowed | status | |
| V | renewed | status | |
| AG | Part-of | subject section | library |
| AS | issued to | membership card | customer |
| I | ISA | book | loan item |
| I | ISA | language tape | loan item |