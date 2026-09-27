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
| 1 | book |
| 1 | title language |
| 1 | level |
| 1 | title |
| 1 | author |
| 1 | loan |
| 2 | date of birth |
| 2 | number of items |
| 3 | issue / is issued |
| 3 | shows |
| 3 | denoted by |
| 3 | identified by |
| 3 | borrow |
| 3 | reserve |
| 3 | renew |
| 3 | extend |
| 3 | scanned |
| 3 | entered |
| 3 | read |
| 3 | stamped |
| 3 | searched |
| 4 | valid |
| 4 | daily |
| 5 | a number of |
| 5 | maximum of 8 |
| 5 | less than 8 |
| 6 | has a title language, and level |
| 6 | has a title, and author(s) |
| 7 | made up of |
| 9 | customer is known as a member |
| 9 | language tapes and books are two types of loan item |

## Step 2: Classification reasoning

library -> C : independent business entity, not scalar
loan item -> C : independent entity, has own id and behavior
customer -> C : independent entity with identity
member -> naming only : same concept as customer, keep name "customer"
membership card -> C : document issued to customer, tracked independently
member number -> A of membership card : identifying number printed on the card
name -> A of customer : scalar descriptive property
address -> A of customer : scalar descriptive property
date of birth -> A of customer : scalar descriptive property
subject section -> C : independent business entity of the library
classification mark -> A of subject section : identifying code of a section
bar code -> A of loan item : identifying code of an item
language tape -> C : kind of loan item with own attributes
book -> C : kind of loan item with own attributes
title language -> A of language tape : scalar property
level -> A of language tape : scalar property
title -> A of book : scalar property
author -> A of book : scalar property
loan -> AC : occurrence of borrowing, has actions performed on it
date of birth (X of Y) -> A of customer : duplicate, already listed
number of items -> A of customer : count of items currently on loan
issue / is issued -> AS : library issues membership card / loan item
shows -> merged into attribute : shown attribute already captured as member number
denoted by -> merged into attribute : already captured as classification mark
identified by -> merged into attribute : already captured as bar code
borrow -> AS : customer borrows loan item, base of loan AC
reserve -> AS : customer reserves loan item, simple association
renew -> A of loan (AC) : action performed on the loan occurrence
extend -> merged with renew : same effect as renewing the loan
scanned -> excluded : device/procedural step, not a lasting relationship
entered -> excluded : device/procedural step
read -> excluded : device/procedural step
stamped -> excluded : physical procedural step, not tracked info
searched -> excluded : generic system capability, not domain rule
valid -> A of membership card : boolean state attribute
daily -> excluded : describes software update cycle, not business data
a number of -> multiplicity : cardinality of subject sections in library
maximum of 8 -> multiplicity : upper bound on borrow association
less than 8 -> multiplicity : duplicate constraint of maximum of 8
has a title language, and level -> confirms A rows : possession expressing attributes
has a title, and author(s) -> confirms A rows : possession expressing attributes
made up of -> AG : library made up of subject sections
customer is known as a member -> naming decision : keep single class "customer"
language tapes and books are two types of loan item -> I : two subclasses of loan item

## Step 3: Review

- Kept a single class "customer" (not "member"); "is known as" is a naming statement, not inheritance.
- language tape and book pass the subclass test (each has its own attributes: title language/level vs title/author) — kept as I rows, not as values.
- "shows", "denoted by", "identified by" removed as separate associations; they only restate that member number/classification mark/bar code are attributes of the card/section/item.
- "scanned", "entered", "read", "stamped", "searched" excluded as procedural/device/system-capability steps, not lasting domain facts.
- "daily" excluded as it only qualifies a system update, not a business attribute.
- Checked customer–loan item borrow association: many-to-many (customer borrows several items over time, item borrowed by many customers over time) and extra information is kept about the occurrence (it can be renewed/extended) → modeled as association class "loan" with attribute "renew", plus its base association "borrow".
- Checked reserve association: many-to-many possible, but no extra information about the reservation occurrence is stated → kept as plain association, no association class.
- Numeric bounds ("a number of", "maximum of 8", "less than 8") treated as multiplicities of associations/aggregation, not output as separate A/V rows (no such row type in final schema).
- Every attribute assigned to exactly one class; no class used as an attribute type.

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
| A | member number | membership card | |
| A | valid | membership card | |
| A | name | customer | |
| A | address | customer | |
| A | date of birth | customer | |
| A | number of items on loan | customer | |
| A | classification mark | subject section | |
| A | bar code | loan item | |
| A | title language | language tape | |
| A | level | language tape | |
| A | title | book | |
| A | author | book | |
| AG | Part-of | subject section | library |
| I | ISA | language tape | loan item |
| I | ISA | book | loan item |
| AS | issue | library | membership card |
| AS | issue | library | loan item |
| AS | borrow | customer | loan item |
| AS | reserve | customer | loan item |
| AC | loan | customer | loan item |
| A | renew | loan | |