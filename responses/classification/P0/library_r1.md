| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Library | | |
| C | LoanItem | | |
| C | Member | | |
| C | MembershipCard | | |
| C | SubjectSection | | |
| C | LanguageTape | | |
| C | Book | | |
| C | BarCodeReader | | |
| C | CurrentLoan | | |
| C | Record | | |
| A | member number | Member | |
| A | details | Member | |
| A | name | Member | |
| A | address | Member | |
| A | date of birth | Member | |
| A | classification mark | LoanItem | |
| A | bar code | LoanItem | |
| A | title language | LoanItem | |
| A | level | LanguageTape | |
| A | title | LoanItem | |
| A | author(s) | Book | |
| A | book bar code | Book | |
| A | number of subject sections | Library | |
| A | types of loan items | LoanItem | |
| A | number of items | CurrentLoan | |
| A | update of records | Record | |
| A | membership | Member | |
| V | French | title language | |
| V | beginner | level | |
| V | daily | update of records | |
| V | valid | membership | |
| V | two | types of loan items | |
| V | 8 | number of items | |
| V | less than 8 | number of items | |
| AS | issues | Library | LoanItem |
| AS | borrow | Member | LoanItem |
| AS | reserved | Member | LoanItem |
| AS | renewed | Member | CurrentLoan |
| AS | extend | Member | CurrentLoan |
| AS | scanned | BarCodeReader | LoanItem |
| AS | entered | Member | Record |
| AS | read | BarCodeReader | LoanItem |
| AS | stamped | Library | LoanItem |
| AS | searched | Member | Record |
| AS | identified | BarCodeReader | Member |
| AS | shows | MembershipCard | Member |
| AS | kept | Library | Record |
| AG | Part-of | SubjectSection | Library |
| AG | Part-of | LoanItem | Library |
| AG | Part-of | CurrentLoan | Member |
| I | ISA | LanguageTape | LoanItem |
| I | ISA | Book | LoanItem |