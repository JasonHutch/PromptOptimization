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
| C | Loan |  |  |
| C | Reservation |  |  |
| C | Renewal |  |  |
| C | BarCodeReader |  |  |
| AS | hasMembershipNumber | Customer | MemberNumber |
| AS | hasBarCode | LoanItem | BarCode |
| AS | isIssued | Customer | Loan |
| AS | isScanned | BarCode | BarCodeReader |
| AS | isEntered | MemberNumber |  |
| AS | isValid | MemberNumber |  |
| AS | canBeIssued | LoanItem |  |
| AS | isStamped | LoanItem |  |
| AS | isSearched | LoanItem |  |
| AS | isUpdated |  |  |


