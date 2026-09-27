| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | Customer |  |  |
| C | BusinessModel |  |  |
| C | Service |  |  |
| C | JobMarket |  |  |
| C | LaborCost |  |  |
| C | OperatingCost |  |  |
| C | BusinessOperation |  |  |
| C | Vehicle |  |  |
| C | PassengerCar |  |  |
| C | ReservationSystem |  |  |
| C | Make |  |  |
| C | Model |  |  |
| C | PriceClass |  |  |
| C | RentalPlan |  |  |
| C | Rental |  |  |
| C | GearChange |  |  |
| C | Doors |  |  |
| C | Sedan |  |  |
| C | Hatchback |  |  |
| C | Salespersons |  |  |
| C | ReservationForm |  |  |
| C | FileCabinet |  |  |
| C | Deposit |  |  |
| C | Contract |  |  |
| C | Period |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | RentalCharge |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | DisposalInformation |  |  |
| A | numberOfRentalLocations |  |  |
| A | numberOfYears |  |  |
| A | numberOfModels |  |  |
| A | numberOfPriceClasses |  |  |
| A | numberOfCars |  |  |
| A | numberOfRentals |  |  |
| AS | operate | RentalLocation | BusinessModel |
| AS | provide | BusinessModel | Service |
| AS | boomed | BusinessModel |  |
| AS | increased | OperatingCost |  |
| AS | become | JobMarket |  |
| AS | doubled | LaborCost |  |
| AS | find |  |  |
| AS | reduce |  | OperatingCost |
| AS | described |  | BusinessOperation |
| AS | considered |  | BusinessOperation |
| AS | taken | Vehicle | RentalLocation |
| AS | returned | Vehicle | RentalLocation |
| AS | charged | Vehicle | RentalLocation |
| AS | branch |  |  |
| AS | use | ReservationSystem |  |
| AS | grouped | Model | PriceClass |
| AS | select | Customer | Make |
| AS | rented | Vehicle | Customer |
| AS | display | System | Customer |
| AS | select | Customer | Make |
| AS | suggest | System | Customer |
| AS | have | Customer | Vehicle |
| AS | available | Vehicle |  |
| AS | settled | Invoice | Customer |
| AS | sent | Invoice | Company |
| AS | paid | RentalCharge | Customer |
| AS | processed | RentalCharge | CreditCardProcessingCompany |
| AS | made | Reservation | Customer |
| AS | archived | ReservationForm | FileCabinet |
| AS | voided | Reservation | Customer |
| AS | honored | Reservation | Customer |
| AS | satisfy | Reservation | Vehicle |
| AS | handled | BlockReservation | Invoice |
| AS | opened | Invoice | Rental |
| AS | cover | Invoice | Rental |
| AS | returned | Vehicle | Rental |
| AS | checked | Vehicle | Customer |
| AS | repaired | Damage | Vehicle |
| AS | keep track |  | DisposalInformation |




