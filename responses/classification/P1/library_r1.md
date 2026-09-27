| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Library | | |
| C | Member | | |
| C | SubjectSection | | |
| C | LoanItem | | |
| C | LanguageTape | | |
| C | Book | | |
| A | memberNumber | Member | |
| A | name | Member | |
| A | address | Member | |
| A | dateOfBirth | Member | |
| A | membershipStatus | Member | |
| V | valid | membershipStatus | |
| A | maxLoanItems | Member | |
| V | 8 | maxLoanItems | |
| A | classificationMark | SubjectSection | |
| A | barCode | LoanItem | |
| A | titleLanguage | LanguageTape | |
| V | French | titleLanguage | |
| A | level | LanguageTape | |
| V | beginner | level | |
| A | title | Book | |
| A | author | Book | |
| I | ISA | LanguageTape | LoanItem |
| I | ISA | Book | LoanItem |
| AG | Part-of | SubjectSection | Library |
| AS | issues | Library | LoanItem |
| AS | borrow | Member | LoanItem |
| AS | reserve | Member | LoanItem |
| AS | renew | Member | LoanItem |
| AS | search | Library | LoanItem |