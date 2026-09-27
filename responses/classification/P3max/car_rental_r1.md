| label | element | arg1 | arg2 |
|---|---|---|---|
| C | vehicle | | |
| A | available | vehicle | |
| A | purchase | vehicle | |
| A | disposal | vehicle | |
| A | depreciation | vehicle | |
| C | car | | |
| I | ISA | car | vehicle |
| C | make | | |
| A | name | make | |
| C | manufacturer | | |
| A | name | manufacturer | |
| C | model | | |
| A | name | model | |
| A | gear change | model | |
| V | automatic | gear change | |
| V | manual | gear change | |
| A | doors | model | |
| V | two | doors | |
| V | four | doors | |
| A | body style | model | |
| V | sedan | body style | |
| V | hatchback | body style | |
| A | rental price | model | |
| C | price class | | |
| A | name | price class | |
| C | location | | |
| A | name | location | |
| C | customer | | |
| A | name | customer | |
| C | rental plan | | |
| A | name | rental plan | |
| V | daily unlimited miles plan | name | |
| V | weekend 10% discount plan | name | |
| C | reservation | | |
| A | time of reservation | reservation | |
| A | period of time | reservation | |
| A | voided | reservation | |
| A | reservation mode | reservation | |
| V | in person | reservation mode | |
| V | by phone | reservation mode | |
| A | archive | reservation | |
| C | block reservation | | |
| I | ISA | block reservation | reservation |
| C | reservation form | | |
| C | salesperson | | |
| A | name | salesperson | |
| C | contract | | |
| A | sign | contract | |
| C | rental | | |
| A | checked out | rental | |
| A | returned to | rental | |
| A | additional charge | rental | |
| A | rental charge | rental | |
| C | invoice | | |
| A | opened | invoice | |
| A | sent to | invoice | |
| C | company | | |
| A | name | company | |
| C | credit card | | |
| A | number | credit card | |
| C | credit card processing company | | |
| A | name | credit card processing company | |
| C | maintenance | | |
| A | date | maintenance | |
| C | repair | | |
| A | date | repair | |
| AS | has | manufacturer | make |
| AS | has | make | model |
| AG | Part-of | model | price class |
| AS | is of | car | model |
| AS | taken from | car | location |
| AS | returned to | car | location |
| AS | select | customer | model |
| AS | make | customer | reservation |
| AS | reserving | reservation | car |
| AS | applies | reservation | rental plan |
| AS | process | salesperson | reservation |
| AS | uses | salesperson | reservation form |
| AS | sign | customer | contract |
| AS | cover | invoice | rental |
| AS | checked out | rental | car |
| AS | has | customer | rental |
| AS | pay | customer | invoice |
| AS | sent to | invoice | company |
| AS | processed | credit card | credit card processing company |
| AS | pays by | customer | credit card |
| AS | needs | car | maintenance |
| AS | has | car | repair |