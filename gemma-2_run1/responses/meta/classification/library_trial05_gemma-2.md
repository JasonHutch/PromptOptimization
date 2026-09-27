| label | element | arg1 | arg2 |
|---|---|---|---|
| C | member |  |  |
| C | membership card |  |  |
| C | member number |  |  |
| C | name |  |  |
| A | name |  | member |
| C | address |  |  |
| A | address |  | member |
| C | date of birth |  |  |
| A | date of birth |  | member |
| C | library |  |  |
| C | subject section |  |  |
| C | classification mark |  |  |
| C | loan item |  |  |
| C | bar code |  |  |
| C | language tape |  |  |
| C | book |  |  |
| C | title |  |  |
| A | title |  | language tape |
| A | title |  | book |
| C | author |  |  |
| A | author |  | book |
| C | customer |  |  |
| A | number of items |  | customer |
| AS | issues | customer | loan item |
| AS | is known as | member | customer |
| AS | is made up of | library | subject section |
| AS | denoted by | subject section | classification mark |
| AS | identified by | loan item | bar code |
| AS | has | loan item | title |
| AS | has | loan item | author |
| AS | is | book | loan item |
| AS | is | language tape | loan item |
| AS | borrowed | customer | loan item |
| AS | reserved | loan item |  |
| AS | renewed | loan item |  |
| AS | issued | customer | loan item |
| AS | scanned | bar code reader | membership card |
| AS | entered | membership number |  |
| AS | read | bar code reader | bar code |
| AS | stamped | item |  |
| AS | supported | library | searching |
| V | valid |  | membership |
| V | reserved |  | loan item |
| A | up to 8 |  | customer |
|  |  |  |  |
|  |  |  |  |




