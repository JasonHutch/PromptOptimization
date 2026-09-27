| label | element | arg1 | arg2 |
|---|---|---|---|
| C | customer |  |  |
| C | member |  |  |
| C | membership card |  |  |
| C | member number |  |  |
| C | details |  |  |
| C | name |  |  |
| C | address |  |  |
| C | date of birth |  |  |
| C | library |  |  |
| C | subject section |  |  |
| C | classification mark |  |  |
| C | loan item |  |  |
| C | bar code |  |  |
| C | language tape |  |  |
| C | book |  |  |
| C | title |  |  |
| C | author |  |  |
| C | item |  |  |
| C | loan |  |  |
| C | reservation |  |  |
| C | renewal |  |  |
| C | barcode reader |  |  |
| A | number of items on loan |  | 8 |
| AS | issued | customer | loan item |
| AS | kept | library | loan item |
| AS | denoted | subject section | classification mark |
| AS | identified | loan item | bar code |
| AS | borrowed | customer | loan item |
| AS | reserved | customer | loan item |
| AS | renewed | customer | loan item |
| AS | scanned | barcode reader | bar code |
| AS | entered | user | bar code |
| AS | read | barcode reader | bar code |
| AS | supported | library | search |
| AS | searched | user | loan item |
| AS | updated | system | record |
| V | valid |  |  |
| V | issued |  |  |
| V | reserved |  |  |
| V | current |  |  |
| V | daily |  |  |
| AG | contains | library | subject section |
| AG | has | customer | name |
| AG | has | customer | address |
| AG | has | customer | date of birth |
| AG | has | language tape | title |
| AG | has | language tape | level |
| AG | has | book | title |
| AG | has | book | author |
| I | book is a loan item |  |  |
| I | language tape is a loan item |  |  |




