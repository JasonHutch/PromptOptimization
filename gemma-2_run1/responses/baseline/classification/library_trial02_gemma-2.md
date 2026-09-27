| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| A | name | Customer | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| C | Member | | |
| A | memberNumber | Member | |
| C | MembershipCard | | |
| C | Library | | |
| A | subjectSections | Library | |
| C | SubjectSection | | |
| A | classificationMark | SubjectSection | |
| C | LoanItem | | |
| A | barCode | LoanItem | |
| C | Book | | |
| A | titleLanguage | Book | |
| A | level | Book | |
| A | title | Book | |
| A | author(s) | Book | |
| C | LanguageTape | | |
| A | title | LanguageTape | |
| A | level | LanguageTape | |
| C | BarCodeReader | | |
| C | Facility | | |
| A | records | Facility | |
| AS | issued | Customer, LoanItem | |
| AS | kept | Facility, LoanItem | |
| AS | denoted | LoanItem, SubjectSection | |
| AS | identified | BarCodeReader, LoanItem | |
| AS | borrowed | Customer, LoanItem | |
| AS | reserved | Customer, LoanItem | |
| AS | renewed | Customer, LoanItem | |
| AS | scanned | BarCodeReader, LoanItem | |
| AS | entered | Customer, MembershipCard | |
| AS | searched | BarCodeReader, LoanItem | |
| C | Membership | | |
| A | numberOfItemsOnLoan | Membership | |
| C | BookBarCode | | |
| AC | Loan | Customer, LoanItem | |
| AG | Part-of | LoanItem, Book | |
| AG | Part-of | LoanItem, LanguageTape | |
| AG | Part-of | Book, SubjectSection | |



