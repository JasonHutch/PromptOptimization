| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | MembershipCard | | |
| C | Library | | |
| C | SubjectSection | | |
| C | ClassificationMark | | |
| C | LoanItem | | |
| C | Barcode | | |
| C | LanguageTape | | |
| C | Book | | |
| C | Title | | |
| C | Author | | |
| C | Facility | | |
| A | memberNumber | MembershipCard | |
| A | details | Member | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | subjectSection | Library | |
| A | classificationMark | Book | |
| A | barCode | LoanItem | |
| A | titleLanguage | Book | |
| A | level | Book | |
| A | author | Book | |
| A | maximum | | |
| A | items | Library | |
| A | loan | | |
| AS | isIssued | LoanItem | Customer |
| AS | isKnown | Member | Library |
| AS | isIdentified | LoanItem | Barcode |
| AS | isMadeUp | LoanItem | SubjectSection |
| AS | areRead | LanguageTape | Customer |
| AS | isEntered | Barcode | Customer |
| AS | isScanned | Barcode | Library |
| AS | isStamped | LoanItem | Library |
| AS | canBeIssued | LoanItem | Customer |
| AS | mustSupport | Facility | Barcode |
| AC | Membership | Customer | Member |
| AC | Loan | Customer | LoanItem |
| AG | Part-Of | SubjectSection | Library |
| AG | Part-Of | Book | LoanItem |
| AG | Part-Of | LanguageTape | LoanItem |
| AG | Part-Of | Title | Book |
| AG | Part-Of | Author | Book |



