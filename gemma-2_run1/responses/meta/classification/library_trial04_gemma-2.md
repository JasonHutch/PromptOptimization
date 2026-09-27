| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
| C | MembershipCard |  |  |
| C | MemberNumber |  |  |
| C | Name |  |  |
| A | name | Customer |  |
| C | Address |  |  |
| A | address | Customer |  |
| C | DateOfBirth |  |  |
| A | dateOfBirth | Customer |  |
| C | Library |  |  |
| C | SubjectSection |  |  |
| C | ClassificationMark |  |  |
| C | LoanItem |  |  |
| C | BarCode |  |  |
| C | LanguageTape |  |  |
| C | Book |  |  |
| A | title | LanguageTape |  |
| A | language | LanguageTape |  |
| A | level | LanguageTape |  |
| A | title | Book |  |
| A | author | Book |  |
| A | barCode | LoanItem |  |
| AS | issued | Customer | LoanItem |
| A | issued | LoanItem |  |
| A | reserved | LoanItem |  |
| A | renewed | LoanItem |  |
| A | searched | Library |  |
| A | updated | Record |  |
| A | number | LoanItem |  |
| A | maximum |  | 8 |
| A | valid | Membership |  |
| V | current | LoanItem |  |
| V | daily | Record |  |
| A | scanned | BarCode |  |
| A | entered | BarCode |  |
| A | read | BarCode |  |
| AC | Borrow | Customer | LoanItem |
| V | number | Borrow |  |



