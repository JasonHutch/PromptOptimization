| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
| C | MembershipCard |  |  |
| A | member number | Customer |  |
| C | Name |  |  |
| C | Address |  |  |
| A | date of birth | Customer |  |
| C | Library |  |  |
| C | SubjectSection |  |  |
| A | classification mark | SubjectSection |  |
| C | LoanItem |  |  |
| A | bar code | LoanItem |  |
| C | LanguageTape |  |  |
| C | Book |  |  |
| A | title | LanguageTape |  |
| A | language | LanguageTape |  |
| A | level | LanguageTape |  |
| A | author | Book |  |
| A | number of items | Customer |  |
| AS | borrow | Customer | LoanItem |
| A | reserved | LoanItem |  |
| AS | issue | Customer | LoanItem |
| A | stamped | LoanItem |  |
| AS | search |  | LoanItem |
| AS | update |  | Record |
| C | Record |  |  |
| A | valid | MembershipCard |  |
| V | 8 |  |  |
| AG | has | Library | SubjectSection |
| AG | holds | SubjectSection | LoanItem |
| I | LanguageTape is a LoanItem |  |  |
| I | Book is a LoanItem |  |  |



