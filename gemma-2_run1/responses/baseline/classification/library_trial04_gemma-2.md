| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | Library | | |
| C | LoanItem | | |
| C | MembershipCard | | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | memberNumber | Member | |
| A | subjectSections | Library | |
| A | classificationMark | LoanItem | |
| A | barCode | LoanItem | |
| A | titleLanguage | LoanItem | |
| A | level | LoanItem | |
| A | title | LoanItem | |
| A | author | LoanItem | |
| A | numberItemsOnLoan | Customer | |
| A | bookBarCode | LoanItem | |
| A | records | Library | |
| AS | has | Customer | MembershipCard |
| AS | has | Member | MembershipCard |
| AS | isIssued | Library | LoanItem |
| AS | kept | Library | LoanItem |
| AS | isIdentified | Library | LoanItem |
| AS | mayBorrow | Customer | LoanItem |
| AS | canBeIssued | Library | LoanItem |
| AS | isScanned | BarCodeReader | LoanItem |
| AS | isEntered | System | LoanItem |
| AS | isStillValid | MembershipCard | |
| AS | isRead | System | LoanItem |
| AS | isStamped | System | LoanItem |
| AS | mustSupport | System | BarCodeReader |
| AS | isSearched | System | LoanItem |
| AC | Membership | Customer | Library |
| AG | Part-of | LoanItem | Library |
| I | ISA | LanguageTape | LoanItem |
| I | ISA | Book | LoanItem |




