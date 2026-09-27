| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | MembershipCard | | |
| C | Library | | |
| C | SubjectSections | | |
| C | ClassificationMark | | |
| C | LoanItem | | |
| C | BarCodeReader | | |
| C | Records | | |
| A | memberNumber | MembershipCard | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | itemNumber | LoanItem | |
| A | barCode | LoanItem | |
| A | titleLanguage | LoanItem | |
| A | level | LoanItem | |
| A | title | LoanItem | |
| A | author | LoanItem | |
| A | classificationMark | SubjectSections | |
| A | subject | SubjectSections | |
| A | records | Records | |
| AS | isIssued | Member | MembershipCard |
| AS | isKept | LoanItem | Library |
| AS | isIdentified | LoanItem | BarCode |
| AS | has | Customer | MembershipCard |
| AS | areRead | BarCodeReader | BarCode |
| AS | isScanned | BarCodeReader | BarCode |
| AS | isEntered | Records | BarCode |
| AS | canBeIssued | LoanItem | Customer |
| AS | isStamped | LoanItem | Records |
| AS | isSupported | Library | SubjectSections |
| AC | LoanRecord |  customer, member, loanItem, dateOfIssue, dueDate | Customer |
| AG | Part-of | BarCode | LoanItem |




