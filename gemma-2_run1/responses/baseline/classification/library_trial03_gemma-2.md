| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | MembershipCard | | |
| C | Details | | |
| C | Library | | |
| C | SubjectSections | | |
| C | Section | | |
| C | ClassificationMark | | |
| C | LoanItem | | |
| C | BarCode | | |
| C | Types | | |
| C | LanguageTapes | | |
| C | Books | | |
| C | Title | | |
| C | Language | | |
| C | Level | | |
| C | Author | | |
| C | Maximum | | |
| C | Items | | |
| C | Item | | |
| C | BarCodeReader | | |
| C | Membership | | |
| C | Book | | |
| C | Facility | | |
| C | Records | | |
| A | name | Customer | |
| A | memberNumber | MembershipCard | |
| A | details | Member | |
| A | address | Customer | |
| A | dateOfBirth | Customer | |
| A | classificationMark | Section | |
| A | barCode | LoanItem | |
| A | title | Book | |
| A | language | LanguageTapes | |
| A | level | LanguageTapes | |
| A | author | Book | |
| A | maximum | Maximum | |
| A | items | Library | |
| A |  |  |  |
| AS | isIssued | LoanItem | Member |
| AS | isKept | LoanItem | Library |
| AS | isIdentified | LoanItem | BarCode |
| AS | isSearched | LoanItem | BarCodeReader |
| AS | mayBorrow | Member | Library |
| AS | canBeIssued | LoanItem | Member |
| AS | isStamped | LoanItem | Member |
| AS | isUpdated | Records | Facility |
| AC | Valid | Customer | |
| AC | Unique | Member | |
| AC | Current | MembershipCard | |
| AC | Reserved | LoanItem | |
| AG | Part-of | Item | LoanItem |
| AG | Part-of | Section | SubjectSections |
| AG | Part-of | LanguageTapes | Library |
| AG | Part-of | Books | Library |
| AG | Part-of | BarCode | LoanItem |
| AG | Part-of | Details | Member |
| I | ISA | CorporateCustomer | Customer |



