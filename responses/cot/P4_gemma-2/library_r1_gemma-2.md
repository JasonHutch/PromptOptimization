## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| literal | A library issues loan items to customers. |
| literal | Each customer is known as a member and is issued a membership card that shows a unique member number. |
| literal | Along with the membership number other details on a customer must be kept such as a name, address, and date of birth. |
| literal | The library is made up of a number of subject sections. |
| literal | Each section is denoted by a classification mark. |
| literal | A loan item is uniquely identified by a bar code. |
| literal | There are two types of loan items, language tapes, and books. |
| literal | A language tape has a title language (e.g. French), and level (e.g. beginner). |
| literal | A book has a title, and author(s). |
| literal | A customer may borrow up to a maximum of 8 items. |
| literal | An item can be borrowed, reserved or renewed to extend a current loan. |
| literal | When an item is issued the customer's membership number is scanned via a bar code reader or entered manually. |
| literal | If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually. |
| literal | If the item can be issued (e.g. not reserved) the item is stamped and then issued. |
| literal | The library must support the facility for an item to be searched and for a daily update of records. |

## Step 2: Classification ledger

| phrase | label | element | arg1 | arg2 | evidence |
|---|---|---|---|---|---|
| A library | C | Library |  |  | "A library issues loan items to customers." |
| issues loan items | V | issue | Library | LoanItem | "A library issues loan items to customers." |
| to customers | AS | to | Library | Customer | "A library issues loan items to customers." |
| Each customer | C | Customer |  |  | "Each customer is known as a member and is issued a membership card that shows a unique member number." |
| known as a member | V | be | Customer | Member | "Each customer is known as a member and is issued a membership card that shows a unique member number." |
| is issued | V | issue | Customer | MembershipCard | "Each customer is known as a member and is issued a membership card that shows a unique member number." |
| membership card | C | MembershipCard |  |  | "Each customer is known as a member and is issued a membership card that shows a unique member number." |
| shows a unique member number | V | show | MembershipCard | MemberNumber | "Each customer is known as a member and is issued a membership card that shows a unique member number." |
| Along with the membership number | C | And |  |  | "Along with the membership number other details on a customer must be kept such as a name, address, and date of birth." |
| other details | C | Detail |  |  | "Along with the membership number other details on a customer must be kept such as a name, address, and date of birth." |
| name, address, and date of birth | C | Detail |  |  | "Along with the membership number other details on a customer must be kept such as a name, address, and date of birth." |
| The library | C | Library |  |  | "The library is made up of a number of subject sections." |
| is made up | V | compose | Library | SubjectSection | "The library is made up of a number of subject sections." |
| of a number of subject sections | C | SubjectSection |  |  | "The library is made up of a number of subject sections." |
| Each section | C | SubjectSection |  |  | "Each section is denoted by a classification mark." |
| is denoted | V | denote | SubjectSection | ClassificationMark | "Each section is denoted by a classification mark." |
| by a classification mark | C | ClassificationMark |  |  | "Each section is denoted by a classification mark." |
| A loan item | C | LoanItem |  |  | "A loan item is uniquely identified by a bar code." |
| is uniquely identified | V | identify | LoanItem | BarCode | "A loan item is uniquely identified by a bar code." |
| by a bar code | C | BarCode |  |  | "A loan item is uniquely identified by a bar code." |
| There are two types | C | Type |  |  | "There are two types of loan items, language tapes, and books." |
| of loan items | C | LoanItem |  |  | "There are two types of loan items, language tapes, and books." |
| language tapes | C | LanguageTape |  |  | "There are two types of loan items, language tapes, and books." |
| and books | C | Book |  |  | "There are two types of loan items, language tapes, and books." |
| A language tape | C | LanguageTape |  |  | "A language tape has a title language (e.g. French), and level (e.g. beginner)." |
| has a title language | V | have | LanguageTape | TitleLanguage | "A language tape has a title language (e.g. French), and level (e.g. beginner)." |
| (e.g. French) | C | TitleLanguage |  |  | "A language tape has a title language (e.g. French), and level (e.g. beginner)." |
| and level | C | Level |  |  | "A language tape has a title language (e.g. French), and level (e.g. beginner)." |
| (e.g. beginner) | C | Level |  |  | "A language tape has a title language (e.g. French), and level (e.g. beginner)." |
| A book | C | Book |  |  | "A book has a title, and author(s)." |
| has a title | V | have | Book | Title | "A book has a title, and author(s)." |
| and author(s) | C | Author |  |  | "A book has a title, and author(s)." |
| A customer | C | Customer |  |  | "A customer may borrow up to a maximum of 8 items." |
| may borrow | V | borrow | Customer | LoanItem | "A customer may borrow up to a maximum of 8 items." |
| up to a maximum of 8 items | C | LoanItem |  |  | "A customer may borrow up to a maximum of 8 items." |
| An item | C | LoanItem |  |  | "An item can be borrowed, reserved or renewed to extend a current loan." |
| can be borrowed | V | beBorrowed | LoanItem |  | "An item can be borrowed, reserved or renewed to extend a current loan." |
| reserved | V | beReserved | LoanItem |  | "An item can be borrowed, reserved or renewed to extend a current loan." |
| or renewed | V | beRenewed | LoanItem |  | "An item can be borrowed, reserved or renewed to extend a current loan." |
| to extend a current loan | C | Loan |  |  | "An item can be borrowed, reserved or renewed to extend a current loan." |
| When an item is issued | C | Issue |  |  | "When an item is issued the customer's membership number is scanned via a bar code reader or entered manually." |
| the customer's membership number | C | MemberNumber |  |  | "When an item is issued the customer's membership number is scanned via a bar code reader or entered manually." |
| is scanned | V | scan | MemberNumber | BarCodeReader | "When an item is issued the customer's membership number is scanned via a bar code reader or entered manually." |
| via a bar code reader | C | BarCodeReader |  |  | "When an item is issued the customer's membership number is scanned via a bar code reader or entered manually." |
| or entered manually | C | ManualEntry |  |  | "When an item is issued the customer's membership number is scanned via a bar code reader or entered manually." |
| If the membership is still valid | C | Membership |  |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| and the number of items on loan less than 8 | C | LoanItem |  |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| the book bar code | C | BarCode |  |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| is read | V | read | BarCode |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| either via the bar code reader | C | BarCodeReader |  |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| or entered manually | C | ManualEntry |  |  | "If the membership is still valid and the number of items on loan less than 8, the book bar code is read, either via the bar code reader or entered manually." |
| If the item can be issued | C | Issue |  |  | "If the item can be issued (e.g. not reserved) the item is stamped and then issued." |
| the item is stamped | V | stamp | LoanItem |  | "If the item can be issued (e.g. not reserved) the item is stamped and then issued." |
| and then issued | V | issue | LoanItem |  | "If the item can be issued (e.g. not reserved) the item is stamped and then issued." |
| The library | C | Library |  |  | "The library must support the facility for an item to be searched and for a daily update of records." |
| must support | V | support | Library | Facility | "The library must support the facility for an item to be searched and for a daily update of records." |
| the facility | C | Facility |  |  | "The library must support the facility for an item to be searched and for a daily update of records." |
| for an item to be searched | C | Search |  |  | "The library must support the facility for an item to be searched and for a daily update of records." |
| and for a daily update of records | C | Update |  |  | "The library must support the facility for an item to be searched and for a daily update of records." |



## Step 3: Model audits

| audit | result |
|---|---|
| source-span fidelity | pass |
| duplicate aliases | pass |
| class/attribute ownership | pass |
| relationship endpoints | pass |
| inheritance tests | pass |
| association-class conditions | pass |

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Library |  |  |
| C | Customer |  |  |
| C | MembershipCard |  |  |
| C | MemberNumber |  |  |
| C | SubjectSection |  |  |
| C | ClassificationMark |  |  |
| C | LoanItem |  |  |
| C | BarCode |  |  |
| C | LanguageTape |  |  |
| C | TitleLanguage |  |  |
| C | Level |  |  |
| C | Book |  |  |
| C | Author |  |  |
| V | issue | Library | LoanItem |
| AS | to | Library | Customer |
| V | be | Customer | Member |
| V | issue | Customer | MembershipCard |
| V | show | MembershipCard | MemberNumber |
| C | Detail |  |  |
| V | compose | Library | SubjectSection |
| V | denote | SubjectSection | ClassificationMark |
| V | identify | LoanItem | BarCode |
| C | Type |  |  |
| V | have | LanguageTape | TitleLanguage |
| V | have | LanguageTape | Level |
| V | have | Book | Title |
| V | have | Book | Author |
| V | borrow | Customer | LoanItem |
| V | beBorrowed | LoanItem |  |
| V | beReserved | LoanItem |  |
| V | beRenewed | LoanItem |  |
| V | scan | MemberNumber | BarCodeReader |
| V | read | BarCode |  |
| V | stamp | LoanItem |  |
| V | issue | LoanItem |  |
| V | support | Library | Facility |
| C | Search |  |  |
| C | Update |  |  |



