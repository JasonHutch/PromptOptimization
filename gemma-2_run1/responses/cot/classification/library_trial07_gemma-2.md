| label | element | arg1 | arg2 |
|---|---|---|---|
| C | customer |  |  |
| C | member |  |  |
| C | membership card |  |  |
| C | member number |  |  |
| A | name | customer |  |
| A | address | customer |  |
| A | date of birth | customer |  |
| C | library |  |  |
| C | subject section |  |  |
| A | classification mark | subject section |  |
| C | loan item |  |  |
| A | bar code | loan item |  |
| C | language tape |  |  |
| C | book |  |  |
| A | title | language tape |  |
| A | language | language tape |  |
| A | level | language tape |  |
| A | author | book |  |
| A | of loan | customer |  |
| AS | issued | customer | loan item |
| AS | scanned | membership card | bar code reader |
| AS | entered | membership number |  |
| AS | supported | library | item searching |
| AS | searched | customer | item |
| V | valid | membership | true/false |
| V | reserved | item | true/false |
| A | number | customer | 8 |
| AG | has membership number | membership card | member number |
| AG | is made up of | library | subject section |
| AG | contains | subject section | classification mark |
| I | is a type of | loan item | language tape |
| I | is a type of | loan item | book |



