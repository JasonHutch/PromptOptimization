| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
| C | MembershipCard |  |  |
| A | member number | Customer |  |
| C | Name |  |  |
| A | address | Customer |  |
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
| AS | issues | Customer | LoanItem |
| A | issued |  |  |
| AS | kept | Customer |  |
| AS | denoted |  | SubjectSection |
| AS | identified |  | LoanItem |
| AS | supported | Library |  |
| AS | searched |  | LoanItem |
| AS | updated |  | Library |
| V | valid | Membership |  |
| V | reserved | LoanItem |  |
| V | maximum of 8 |  |  |
| AG | has bar code | LoanItem |  |
| AG | consists of | Library | SubjectSection |
| AG | made up of |  | Library |
| AG | contains | SubjectSection | LoanItem |
| I | LanguageTape is a LoanItem |  |  |
| I | Book is a LoanItem |  |  | 



