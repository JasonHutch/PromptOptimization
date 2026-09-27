| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | Library | | |
| C | LoanItem | | |
| C | Book | | |
| C | LanguageTape | | |
| A | name | Customer | |
| A | memberNumber | Member | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | subjectSections | Library | |
| A | classificationMark | LoanItem | |
| A | barCode | LoanItem | |
| A | title | Book | |
| A | level | Book | |
| A | author(s) | Book | |
| AS | isIssued | Member | LoanItem |
| AS | isIdentified | LoanItem | Customer |
| AS | has | Library | SubjectSections |
| AC | Membership | Customer | |
| AC | LoanRecord | Member | LoanItem |
| AG | Part-of | LoanItem | Library |
| AG | Part-of | SubjectSection | Library |
| I | ISA | Member | Customer | 




