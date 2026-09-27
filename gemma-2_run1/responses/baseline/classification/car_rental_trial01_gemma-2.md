| label | element | arg1 | arg2 |
|---|---|---|---|
| C | CarRentalCompany | | |
| C | BusinessModel | | |
| C | Customer | | |
| C | VehicleRental | | |
| C | Car | | |
| A | name | CarRentalCompany | |
| A | operatingCost | BusinessModel | |
| A | businessModel | CarRentalCompany | |
| A | rentalLocations | CarRentalCompany | |
| A | customer | CarRentalCompany | |
| A | priceClasses | CarRentalCompany | |
| A | models | Car | |
| A | make | Car | |
| A | model | Car | |
| A | automatic | Car | |
| A | manual | Car | |
| A | doors | Car | |
| A | sedan | Car | |
| A | hatchback | Car | |
| A | rentalPrices | Car | |
| A | options | Car | |
| A | deposit | Customer | |
| A | creditCard | Customer | |
| A | rentalCharge | Invoice | |
| A | period | Reservation | |
| AS | operates | CarRentalCompany | BusinessModel |
| AS | provides | CarRentalCompany | VehicleRental |
| AS | rent | Customer | Car |
| AS | return | Customer | Car |
| AS | request | Customer | Reservation |
| AS | book | Customer | Reservation |
| AS | process | Company | Invoice |
| AS | settle | Customer | Invoice |
| AS | pay | Customer | Invoice |
| AC | Reservation | Customer, Car | |
| AC | Invoice | Customer, Car | |
| AC | Payment | Customer, Invoice | |
| AG | Part-Of | Car | RentalFleet |
| AG | Part-Of | RentalFleet | CarRentalCompany |


