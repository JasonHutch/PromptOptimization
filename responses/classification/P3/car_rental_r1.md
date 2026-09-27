| label | element | arg1 | arg2 |
|---|---|---|---|
| C | vehicle | | |
| C | car | | |
| C | location | | |
| C | make | | |
| C | model | | |
| C | customer | | |
| C | salesperson | | |
| C | rental plan | | |
| C | contract | | |
| C | block reservation | | |
| C | invoice | | |
| C | credit card | | |
| C | company | | |
| C | credit card processing company | | |
| A | gear change | model | |
| A | doors | model | |
| A | body style | model | |
| A | rental price | model | |
| A | price class | model | |
| A | availability | car | |
| A | record type | car | |
| A | voided | reservation | |
| A | time | reservation | |
| A | method | reservation | |
| A | period of time | reservation | |
| A | additional charge | rental | |
| A | opened | invoice | |
| A | rental charge | invoice | |
| V | available | availability | |
| V | rented out | availability | |
| V | purchase | record type | |
| V | repair | record type | |
| V | maintenance | record type | |
| V | disposal | record type | |
| V | automatic | gear change | |
| V | manual | gear change | |
| V | two | doors | |
| V | four | doors | |
| V | sedan | body style | |
| V | hatchback | body style | |
| V | in person | method | |
| V | by phone | method | |
| AS | taken from | vehicle | location |
| AS | returned to | vehicle | location |
| AS | select | customer | make |
| AS | select | customer | model |
| AS | process | salesperson | reservation |
| AS | archive | salesperson | reservation |
| AS | sign | customer | contract |
| AS | cover | invoice | rental |
| AS | checked out | car | customer |
| AS | pay | customer | invoice |
| AS | sent to | invoice | company |
| AS | processed | invoice | credit card processing company |
| AS | paid by | invoice | credit card |
| AS | make | customer | reservation |
| AC | reservation | customer | model |
| AC | rental | customer | car |
| AG | Part-of | model | make |
| I | ISA | car | vehicle |
| I | ISA | block reservation | reservation |