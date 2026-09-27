| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
| C | MembershipCard |  |  |
| C | MemberNumber |  |  |
| C | Details |  |  |
| A | name | Customer |  |
| A | address | Customer |  |
| A | dateOfBirth | Customer |  |
| C | Library |  |  |
| C | SubjectSection |  |  |
| A | classificationMark | SubjectSection |  |
| C | LoanItem |  |  |
| A | barCode | LoanItem |  |
| C | LanguageTape |  |  |
| C | Book |  |  |
| A | title | LanguageTape |  |
| A | language | LanguageTape |  |
| A | level | LanguageTape |  |
| A | author | Book |  |
| A | numberBorrowed | Customer |  |
| AS | canBorrow | Customer | LoanItem |
| AC | Loan | Customer |  |
| A | issued | Loan |  |
| A | reserved | Loan |  |
| A | renewed | Loan |  |
| A | valid | MembershipCard |  |
| A | current | Loan |  |
| A | daily | Record |  |
| V | memberNumber | MembershipCard |  |
| V | barCode | LoanItem |  |
| V | title | LanguageTape |  |
| V | title | Book |  |
| V | author | Book |  |



