| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Vehicle | | |
| C | Car | | |
| C | Manufacturer | | |
| C | Make | | |
| C | Model | | |
| C | PriceClass | | |
| C | Location | | |
| C | Customer | | |
| C | RentalPlan | | |
| C | Reservation | | |
| C | Salesperson | | |
| C | Contract | | |
| C | Invoice | | |
| C | Rental | | |
| C | CreditCard | | |
| C | CreditCardProcessingCompany | | |
| C | Company | | |
| A | rental price | Model | |
| A | gear change | Model | |
| V | automatic | gear change | |
| V | manual | gear change | |
| A | doors | Model | |
| V | two | doors | |
| V | four | doors | |
| A | body style | Model | |
| V | sedan | body style | |
| V | hatchback | body style | |
| A | additional charge | Rental | |
| A | status | Car | |
| V | available | status | |
| V | not available | status | |
| V | rented out | status | |
| A | reservation status | Reservation | |
| V | voided | reservation status | |
| V | opened | reservation status | |
| A | contact method | Reservation | |
| V | in person | contact method | |
| V | by phone | contact method | |
| A | time of reservation | Reservation | |
| A | grace period | Reservation | |
| A | depreciation | Car | |
| A | plan type | RentalPlan | |
| V | daily unlimited miles plan | plan type | |
| V | weekend 10% discount plan | plan type | |
| A | activity type | Car | |
| V | purchase | activity type | |
| V | repair | activity type | |
| V | maintenance | activity type | |
| V | disposal | activity type | |
| A | reservation type | Reservation | |
| V | block reservation | reservation type | |
| I | ISA | Car | Vehicle |
| AG | Part-of | Make | Manufacturer |
| AG | Part-of | Model | Make |
| AS | belongs to | Model | PriceClass |
| AS | taken from | Vehicle | Location |
| AS | returned to | Vehicle | Location |
| AS | select | Customer | Model |
| AS | reserve | Customer | Car |
| AS | process | Salesperson | Reservation |
| AS | archive | Salesperson | Reservation |
| AS | sign | Customer | Contract |
| AS | make | Customer | Reservation |
| AS | cover | Invoice | Rental |
| AS | check out | Customer | Car |
| AS | pay | Customer | Invoice |
| AS | send | Invoice | Company |
| AS | process | CreditCardProcessingCompany | Invoice |
| AS | pay by | Customer | CreditCard |