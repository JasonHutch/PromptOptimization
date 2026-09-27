| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Member | | |
| C | MembershipCard | | |
| C | MemberNumber | | |
| C | Name | | |
| C | Address | | |
| C | DateOfBirth | | |
| C | Library | | |
| C | SubjectSections | | |
| C | ClassificationMark | | |
| C | LoanItem | | |
| C | BarCode | | |
| C | LanguageTapes | | |
| C | Books | | |
| C | TitleLanguage | | |
| C | Level | | |
| C | Title | | |
| C | Author | | |
| C | Item | | |
| C | BarCodeReader | | |
| C | Membership | | |
| C | Records | | |
| A |  name | Customer | |
| A |  address | Customer | |
| A |  dateOfBirth | Customer | |
| A |  memberNumber | MembershipCard | |
| A |  subjectSections | Library | |
| A |  classificationMark | SubjectSections | |
| A |  barCode | LoanItem | |
| A |  titleLanguage | LanguageTapes | |
| A |  level | LanguageTapes | |
| A |  title | Books | |
| A |  author | Books | |
| AS | has | Library | SubjectSections |
| AS | isIssued | LoanItem | Customer |
| AS | isKept | LoanItem | Library |
| AS | isIdentified | LoanItem | BarCode |
| AS | isSearched | Records | Customer |
| AS | isUpdated | Records | Customer |
| AS | mayBorrow | Customer | LoanItem |
| AS | canBeBorrowed | LoanItem | Customer |
| AS | canBeIssued | LoanItem | Customer |
| AS | isStamped | LoanItem | Customer |


