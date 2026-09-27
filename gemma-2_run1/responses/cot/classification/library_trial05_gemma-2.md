| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Member |  |  |
| C | Customer |  |  |
| C | MembershipCard |  |  |
| C | MembershipNumber |  |  |
| C | Name |  |  |
| C | Address |  |  |
| C | DateOfBirth |  |  |
| C | Library |  |  |
| C | SubjectSection |  |  |
| C | ClassificationMark |  |  |
| C | LoanItem |  |  |
| C | BarCode |  |  |
| C | LanguageTape |  |  |
| C | Book |  |  |
| C | Title |  |  |
| C | Author |  |  |
| C | Loan |  |  |
| C | Reservation |  |  |
| C | Renewal |  |  |
| C | BarCodeReader |  |  |
| C | Record |  |  |
| A | NumberOfItems |  |  |
| AS | issued | Member, LoanItem |  |
| AS | scanned | BarCode,  |  |
| AS | entered | MembershipNumber, BarCode |  |
| AS | kept | Customer, MembershipCard |  |
| AS | denoted | SubjectSection, ClassificationMark |  |
| AS | identified | LoanItem, BarCode |  |
| AS | borrowed | Member, LoanItem |  |
| AS | reserved | LoanItem,  |  |
| AS | renewed | LoanItem,  |  |
| AS | stamped | LoanItem,  |  |
| AS | searched | Record,  |  |
| AS | updated | Record,  |  |
| V | valid |  |  |
| V | maximum |  |  |
| V | current |  |  |
| A | aNumber |  |  |


