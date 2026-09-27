| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
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
| C | RentalPrice |  |  |
| C | Reservation |  |  |
| C | Salesperson |  |  |
| C | ReservationForm |  |  |
| C | Deposit |  |  |
| C | Contract |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | CreditCard |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | RentalCarPurchase |  |  |
| C | DisposalInformation |  |  |
| A | number |  |  |
| A | percentage |  |  |
| A | period |  |  |
| V | 10 |  |  |
| AS | operates | RentalLocation | BusinessModel |
| AS | finds | RentalCar | RentalPlan |
| AS | reduce | OperatingCost |  |
| AS | described | BusinessOperation |  |
| AS | branch |  | ReservationSystem |
| AS | use | ReservationSystem |  |
| AS | have | Customer | Make |
| AS | select | Customer | Model |
| AS | display | System | Customer |
| AS | let | System | Customer |
| AS | suggest | System | Customer |
| AS | make | Customer | Model |
| AS | have | Customer | BlockReservation |
| AS | settle | Customer | Invoice |
| AS | send | Invoice | Company |
| AS | process | CreditCard | RentalCharge |
| AS | keep track | Company | RentalCar |
| AC | Rental |  |  |
| AC | Rental |  |  |
| AC | Rental |  |  |
| I | Car | Vehicle |



