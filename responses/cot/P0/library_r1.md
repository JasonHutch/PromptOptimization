## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | library |
| 1 | customer |
| 1 | loan item |
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
| 1 | title |
| 1 | author(s) |
| 1 | level |
| 1 | title language |
| 2 | date of birth |
| 3 | issues (loan items to customers) |
| 3 | is issued (membership card) |
| 3 | is denoted by (classification mark) |
| 3 | is identified by (bar code) |
| 3 | borrow |
| 3 | reserved |
| 3 | renewed |
| 3 | is scanned |
| 3 | is entered |
| 3 | is read |
| 3 | is stamped |
| 3 | is issued (item) |
| 3 | searched |
| 3 | update |
| 4 | valid |
| 4 | reserved |
| 5 | maximum of 8 items |
| 5 | less than 8 |
| 5 | a number of (subject sections) |
| 5 | unique (member number) |
| 6 | has a title language and level |
| 6 | has a title, and author(s) |
| 7 | made up of (subject sections) |
| 9 | known as (customer known as member) |
| 9 | two types of loan items: language tapes and books |

## Step 2: Classification reasoning

library -> C : independent domain concept, issues items to members
customer -> merge with member : same concept renamed by "known as"
loan item -> C : independently identified by barcode
member -> C : primary actor class, absorbs "customer"
membership card -> discard : physical artifact, no independent attributes beyond member number
member number -> A of Member : scalar identifier typed via keyboard/scanner
name -> A of Member : scalar descriptive property
address -> A of Member : scalar descriptive property
date of birth -> A of Member : scalar property, "X of Y" also
subject section -> C : independently exists, has own attribute
classification mark -> A of SubjectSection : scalar identifier of a section
bar code -> A of LoanItem : scalar unique identifier
language tape -> C, subclass : specialized loan item type
book -> C, subclass : specialized loan item type
title -> A of Book : scalar descriptive property
author(s) -> A of Book : scalar descriptive property
level -> A of LanguageTape : scalar descriptive property
title language -> A of LanguageTape : scalar descriptive property
date of birth (X of Y) -> A of Member : same as above
issues (loan items to customers) -> AS issues, Library, LoanItem : library-level action on items
is issued (membership card) -> discard : card not modeled as class
is denoted by (classification mark) -> already captured as attribute, no new element
is identified by (bar code) -> already captured as attribute, no new element
borrow -> AS borrows, Member, LoanItem : core lending relationship
reserved -> AS reserves, Member, LoanItem : business action on item
renewed -> AS renews, Member, LoanItem : business action extending loan
is scanned -> discard : procedural UI/hardware detail
is entered -> discard : procedural UI detail
is read -> discard : procedural UI detail
is stamped -> discard : physical process step, not stored state
is issued (item) -> covered by AS issues/borrows : redundant with borrow
searched -> discard : generic system capability
update -> discard : generic system capability
valid -> V of attribute membershipStatus, Member : conditional state governing business rule
reserved (adj) -> V of attribute status, LoanItem : state describing item availability
maximum of 8 items -> multiplicity on borrows association : bounds Member-LoanItem loans
less than 8 -> duplicate of maximum of 8 : same business rule
a number of (subject sections) -> multiplicity on Part-of aggregation : indefinite quantity
unique (member number) -> property of attribute memberNumber, no new element
has a title language and level -> attributes titleLanguage, level of LanguageTape : possession expression
has a title, and author(s) -> attributes title, author of Book : possession expression
made up of (subject sections) -> AG Part-of, SubjectSection, Library : whole-part expression
known as (customer known as member) -> merge Customer and Member into one class : synonym relation
two types of loan items: language tapes and books -> I ISA LanguageTape/LoanItem, Book/LoanItem : generalization

## Step 3: Review

- Merged "customer" and "member" into a single class Member (synonym).
- Discarded "membership card" as a class; kept member number as an attribute of Member.
- Discarded procedural/UI verbs (scanned, entered, read, stamped, searched, update) as generic system actions, not domain state.
- Consolidated "maximum of 8 items" and "less than 8" into a single multiplicity constraint on the borrows association (0..8).
- Excluded illustrative example values "French" and "beginner" (given only as "e.g." examples, not enumerated domain values).
- Confirmed no many-to-many association requires an association class: borrows/reserves/renews link Member and LoanItem but no extra attribute of the link itself is described.
- Verified every attribute has exactly one owning class and every relationship connects listed classes.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Library | | |
| C | Member | | |
| C | LoanItem | | |
| C | LanguageTape | | |
| C | Book | | |
| C | SubjectSection | | |
| A | memberNumber | Member | |
| A | name | Member | |
| A | address | Member | |
| A | dateOfBirth | Member | |
| A | membershipStatus | Member | |
| V | valid | membershipStatus | |
| A | barcode | LoanItem | |
| A | status | LoanItem | |
| V | reserved | status | |
| A | classificationMark | SubjectSection | |
| A | titleLanguage | LanguageTape | |
| A | level | LanguageTape | |
| A | title | Book | |
| A | author | Book | |
| I | ISA | LanguageTape | LoanItem |
| I | ISA | Book | LoanItem |
| AG | Part-of | SubjectSection | Library |
| AS | issues | Library | LoanItem |
| AS | borrows | Member | LoanItem |
| AS | reserves | Member | LoanItem |
| AS | renews | Member | LoanItem |