| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | LoanItem | | |
| C | Book | | |
| C | LanguageTape | | |
| C | SubjectSection | | |
| C | MembershipCard | | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | memberNumber | Member | |
| A | classificationMark | LoanItem | |
| A | barCode | LoanItem | |
| A | titleLanguage | LanguageTape | |
| A | title | Book | |
| A | author | Book | |
| A | level | Book | |
| AS | borrowed | Customer | LoanItem |
| AS | reserved | Customer | LoanItem |
| AS | renewed | Customer | LoanItem |
| AS | issued | Member | LoanItem |
| AS | kept | Member | LoanItem |
| AS | identified | BarCodeReader | LoanItem |
| AS | scanned | BarCodeReader | LoanItem |
| AS | entered | System | LoanItem |
| AS | updated | System | LoanItem |
| AC | Reservation | Customer | LoanItem |
| AG | Part-of | Book | LoanItem |
| AG | Part-of | LanguageTape | LoanItem |
| I | ISA | Member | Customer |
| I | ISA | Book | LoanItem |
| I | ISA | LanguageTape | LoanItem |



