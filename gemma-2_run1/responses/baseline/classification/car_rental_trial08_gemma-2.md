| label | element | arg1 | arg2 |
|---|---|---|---|
| C | CarRentalCompany | | |
| C | Business | | |
| C | Customer | | |
| C | Invoice | | |
| C | RentalCar | | |
| C | RentalPlan | | |
| C | Reservation | | |
| A | name | Customer | CarRentalCompany |
| A | status | Invoice | CarRentalCompany |
| A | rentalLocations | CarRentalCompany | |
| A | makes | RentalCar | |
| A | models | RentalCar | |
| A | priceClass | RentalCar | |
| A | type | RentalCar | |
| A | contract | Reservation | |
| A | period | Reservation | |
| A | car | Reservation | |
| A | deposit | Reservation | |
| A | time | Reservation | |
| A | customer | Reservation | |
| A | rentalCharge | Invoice | |
| A | company | Invoice | |
| AS | operates | CarRentalCompany | |
| AS | provides | CarRentalCompany | RentalCar |
| AS | make | RentalCar | |
| AS | model | RentalCar | |
| AS | rent | Customer | RentalCar |
| AS | return | Customer | RentalCar |
| AS | pay | Customer | Invoice |
| AS | settle | Invoice | CarRentalCompany |
| AS | process | Invoice | CreditCardProcessingCompany |
| AS | request | Customer | CarRentalCompany |
| AS | block | Customer | Reservation |
| AS | has | CarRentalCompany | RentalLocation |


