| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| C | Member | | |
| A | membershipCard | Member | |
| A | memberNumber | Member | |
| C | Library | | |
| A | subjectSections | Library | |
| A | classificationMark | Library | |
| C | LoanItem | | |
| A | barCode | LoanItem | |
| C | LanguageTape | LoanItem | |
| A | title | LanguageTape | |
| A | level | LanguageTape | |
| C | Book | LoanItem | |
| A | title | Book | |
| A | author | Book | |
| C | Membership | | |
| A | customer | Membership | |
| C | BarCodeReader | | |
| C | Records | | |
| AS | issued | Customer | LoanItem |
| AS | kept | LoanItem | Library |
| AS | denoted | LoanItem | Records |
| AS | identified | LoanItem | BarCodeReader |
| AS | borrowed | Customer | LoanItem |
| AS | reserved | Customer | LoanItem |
| AS | renewed | Customer | LoanItem |
| AS | scanned | BarCodeReader | LoanItem |
| AS | entered | Records | LoanItem |
| AS | read | BarCodeReader | LoanItem |
| AS | stamped | LoanItem | Library |
| AC | Membership | Customer | |
| AC | LoanRecord | Customer | LoanItem |
| AG | Part-of | LanguageTape | LoanItem |
| AG | Part-of | Book | LoanItem |
| I | ISA | LanguageTape | LoanItem |
| I | ISA | Book | LoanItem |
| I | ISA | LoanItem | LibraryItem |



