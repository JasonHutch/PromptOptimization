| label | element | arg1 | arg2 |
|---|---|---|---|
| C | vehicle | | |
| C | car | | |
| C | manufacturer | | |
| C | make | | |
| C | model | | |
| C | location | | |
| C | customer | | |
| C | rental plan | | |
| C | reservation | | |
| C | salesperson | | |
| C | contract | | |
| C | invoice | | |
| C | credit card processing company | | |
| C | company | | |
| A | availability | car | |
| A | record type | car | |
| A | depreciation | car | |
| A | gear change | model | |
| A | doors | model | |
| A | body style | model | |
| A | price class | model | |
| A | rental price | model | |
| A | time | reservation | |
| A | period of time | reservation | |
| A | voided | reservation | |
| A | method | reservation | |
| A | opened | invoice | |
| A | rental charge | invoice | |
| A | additional charge | invoice | |
| A | checked out | rental | |
| A | returned | rental | |
| V | available | availability | |
| V | not available | availability | |
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
| AS | has | manufacturer | make |
| AS | has | make | model |
| AS | has | car | model |
| AS | has | reservation | rental plan |
| AS | select | customer | make |
| AS | select | customer | model |
| AS | make | customer | reservation |
| AS | process | salesperson | reservation |
| AS | sign | customer | contract |
| AS | has | reservation | contract |
| AS | has | reservation | rental |
| AS | cover | invoice | rental |
| AS | pay | customer | invoice |
| AS | sent to | invoice | company |
| AS | processed | credit card processing company | invoice |
| AS | checked out | car | customer |
| AS | taken from | rental | location |
| AS | returned to | rental | location |
| AC | rental | car | customer |
| I | ISA | car | vehicle |