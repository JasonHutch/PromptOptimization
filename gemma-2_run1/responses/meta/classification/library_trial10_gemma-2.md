| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer |  |  |
| C | Member |  |  |
| C | MembershipCard |  |  |
| C | MemberNumber |  |  |
| C | Details |  |  |
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
| C | Membership |  |  |
| C | NumberOfItemsOnLoan |  |  |
| C | BookBarCode |  |  |
| C | Stamp |  |  |
| C | Update |  |  |
| A | membership_number | Customer |  |
| A | name | Customer |  |
| A | address | Customer |  |
| A | date_of_birth | Customer |  |
| A | classification_mark | SubjectSection |  |
| A | bar_code | LoanItem |  |
| A | title_language | LanguageTape |  |
| A | level | LanguageTape |  |
| A | title | Book |  |
| A | author | Book |  |
| A | maximum_loan | Customer | 8 |
| A | is_reserved | LoanItem | true/false |
| V | valid_membership | Membership |  |
| AS | issued | Customer, LoanItem |  |
| AC | LoanItem | Customer |  |
| AC | LoanItem | BarCode |  |
| A | bar_code_read | BarCodeReader |  |
| A | bar_code_entered |  |  |


