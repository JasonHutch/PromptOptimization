| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
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
| C | TitleLanguage |  |  |
| C | Level |  |  |
| C | Title |  |  |
| C | Author |  |  |
| C | Loan |  |  |
| C | Reservation |  |  |
| C | Renewal |  |  |
| C | BarCodeReader |  |  |
| C | Records |  |  |
| A | numberOfItems |  |  |
| AS | issued | Customer,LoanItem |  |
| AS | kept | Customer,MembershipCard |  |
| AS | denoted | SubjectSection,ClassificationMark |  |
| AS | identified | LoanItem,BarCode |  |
| AS | borrowed | Customer,LoanItem |  |
| AS | reserved | LoanItem,Customer |  |
| AS | renewed | LoanItem,Customer |  |
| AS | scanned | MembershipNumber,BarCodeReader |  |
| AS | entered | MembershipNumber,System |  |
| AS | read | BarCode,BarCodeReader |  |
| AS | stamped | LoanItem,LibraryStaff |  |
| AS | searched | Customer,LibrarySystem |  |
| AS | updated | Records,LibrarySystem |  |
| A | valid | Membership |  |
| A | current | Loan |  |
| A | available | LoanItem |  |
| V | aNumberofItems |  | 8 |
| AG | membershipNumber | MembershipCard |  |
| AG | item | LoanItem |  |



