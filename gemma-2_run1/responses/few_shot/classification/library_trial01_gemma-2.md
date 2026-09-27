| label | element | arg1 | arg2 |
|---|---|---|---|
| C | customer |  |  |
| C | member |  |  |
| C | membership card |  |  |
| C | member number |  |  |
| C | details |  |  |
| A | name | customer |  |
| A | address | customer |  |
| A | date of birth | customer |  |
| C | library |  |  |
| C | subject sections |  |  |
| A | classification mark | subject section |  |
| C | loan item |  |  |
| A | bar code | loan item |  |
| C | language tape |  |  |
| C | book |  |  |
| A | title | language tape |  |
| A | language | language tape |  |
| A | level | language tape |  |
| A | author | book |  |
| AS | may borrow | customer | loan item;  |  |
| A | maximum | customer | 8 |
| A |  | loan item | issued |
| A |  | loan item | reserved |
| A |  | loan item | renewed |
| AC | has | customer | membership; membership has a number | number |
| AC | has | loan item | bar code; bar code has a | bar code |
| AC | has | loan item | stamp; stamp has a | stamp |
| AC | has | library | subject sections; subject sections have a | classification mark |


