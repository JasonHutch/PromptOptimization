## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | library |
| 1 | loan item(s) |
| 1 | customer(s) |
| 1 | member |
| 1 | membership card |
| 1 | membership number |
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
| 1 | loan |
| 2 | date of birth |
| 2 | types of loan items |
| 2 | number of items on loan |
| 2 | update of records |
| 3 | issues (...to) |
| 3 | is issued |
| 3 | shows |
| 3 | kept |
| 3 | denoted by |
| 3 | identified by |
| 3 | borrow |
| 3 | reserved |
| 3 | renewed |
| 3 | extend |
| 3 | scanned |
| 3 | read |
| 3 | stamped |
| 3 | searched |
| 4 | valid |
| 4 | daily |
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

library -> class : independent entity in the domain
loan item(s) -> class : general item type, has subclasses tape/book
customer(s) -> class : concept text keeps but "member" is the name used going forward
member -> class : same concept as customer, use "member" per naming rule (first+most used check) — actually "customer" introduced first, but "member" used repeatedly afterward; keep "member" as the class name since attributes attach to member
membership card -> class : document the library issues, has its own identifying number
membership number -> attribute : identifies membership card, belongs to membership card
name -> attribute : property of member
address -> attribute : property of member
date of birth -> attribute : property of member
subject section -> class : independent entity with its own identifying mark
classification mark -> attribute : identifies subject section
bar code -> attribute : identifies loan item
language tape -> class (subclass) : kind of loan item with own attributes
title language -> attribute : property of language tape
level -> attribute : property of language tape
book -> class (subclass) : kind of loan item with own attributes
title -> attribute : property of book
author(s) -> attribute : property of book
loan -> association class : occurrence of borrowing between member and item
date of birth (X of Y) -> attribute : same as above, one row
types of loan items -> handled via inheritance rows below
number of items on loan -> attribute : derived count kept as attribute of member (current loan count)
update of records -> excluded : software/system maintenance activity, not domain entity action
issues (...to) -> association : library issues loan item to member
is issued -> association : same as "issues", merge
shows -> association : membership card shows membership number (attribute already captures this)
kept -> association : merged into attributes of member (details kept)
denoted by -> association : section denoted by classification mark (captured as attribute)
identified by -> association : loan item identified by bar code (captured as attribute)
borrow -> association : member borrows loan item
reserved -> association : member reserves loan item
renewed -> association : member renews loan
extend -> merged into "renewed" association, not separate
scanned -> excluded : describes UI/device interaction, not domain action needing separate association
read -> excluded : same reason, describes bar code reading mechanism
stamped -> excluded : minor implementation step of issuing process, not separate association
searched -> association : item is searched (library searches for item)
valid -> attribute value : boolean/status attribute "valid" of membership card
daily -> attribute value : describes update frequency, excluded as it's a system task not domain state
a number of -> multiplicity : aggregation library/subject section
two -> multiplicity : number of loan item subclasses (not separately modeled)
maximum of 8 -> multiplicity : constrains borrow association (member to loan item)
less than 8 -> multiplicity : same constraint, merge with maximum of 8
has a title language, and level -> attributes : language tape attributes (title language, level)
has a title, and author(s) -> attributes : book attributes (title, author)
made up of -> aggregation : subject section part of library
customer is known as a member -> naming decision : use "member" as class name, not inheritance
language tapes and books are two types of loan items -> inheritance : language tape and book are subclasses of loan item

## Step 3: Review

- Merged "customer" and "member" into a single class "member" (name used most/consistently in operational description).
- Excluded "scanned", "read", "stamped" as implementation/device-level actions, not distinct domain associations; the underlying facts (bar code identifies item, membership number identifies card) are captured as attributes.
- Excluded "daily update of records" and "searched" system-facility wording except kept "search" only if it names a genuine domain action; on review, "search" is a generic system facility ("the facility for an item to be searched") so excluded per domain scope filter.
- Confirmed "language tape" and "book" as subclasses of "loan item" (they have their own attributes: title language/level vs title/author), passing the kinds rule.
- Created association class "loan" for the borrow relationship between member and loan item, since a loan is an occurrence that can be renewed/reserved and the number of items on loan must be tracked (many-to-many: a member borrows many items, an item can be borrowed by many members over time).
- Added multiplicity "maximum of 8" to the borrow association (member side).
- Verified every attribute has exactly one owning class; no class used as attribute type.
- Verified every relationship connects only listed classes (library, member, membership card, subject section, loan item, language tape, book, loan).

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | library | | |
| C | member | | |
| C | membership card | | |
| C | subject section | | |
| C | loan item | | |
| C | language tape | | |
| C | book | | |
| A | name | member | |
| A | address | member | |
| A | date of birth | member | |
| A | membership number | membership card | |
| A | valid | membership card | |
| A | classification mark | subject section | |
| A | bar code | loan item | |
| A | title language | language tape | |
| A | level | language tape | |
| A | title | book | |
| A | author(s) | book | |
| I | ISA | language tape | loan item |
| I | ISA | book | loan item |
| AG | Part-of | subject section | library |
| AS | issues | library | loan item |
| AS | reserves | member | loan item |
| AC | loan | member | loan item |
| A | renew | loan | |
| A | number of items on loan | loan | |