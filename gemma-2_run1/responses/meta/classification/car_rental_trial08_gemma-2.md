| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
| C | JobMarket |  |  |
| C | LaborCost |  |  |
| C | OperatingCost |  |  |
| C | BusinessOperation |  |  |
| C | VehicleRental |  |  |
| C | PassengerCar |  |  |
| C | ReservationSystem |  |  |
| C | Make |  |  |
| C | Model |  |  |
| C | PriceClass |  |  |
| C | RentalPlan |  |  |
| C | RentalCar |  |  |
| C | GearChange |  |  |
| C | RentalPrices |  |  |
| C | Salesperson |  |  |
| C | ReservationForm |  |  |
| C | Contract |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | Disposal |  |  |
| C | RentalCarPurchase |  |  |
| C | Depreciation |  |  |
| A | makeOf | Make | Model |
| A | priceClassOf | Model | PriceClass |
| A | carType | RentalCar | PassengerCar |
| A | planType | RentalPlan |  |
| A | gearType | RentalCar | GearChange |
| A | doors | RentalCar |  |
| A | bodyType | RentalCar |  |
| AS | reduce | OperatingCost |  |
| AS | find | Solution | OperatingCost |
| AS | branchOut |  | VehicleRental |
| AS | use | ReservationSystem |  |
| AS | select | Customer | Make |
| AS | select | Customer | Model |
| AS | display | System |  |
| AS | suggest | System | Model |
| AS | group | Model | PriceClass |
| AS | have | Customer |  |
| AS | settle | Customer | Invoice |
| AS | process | Salesperson | ReservationForm |
| AS | open | Invoice | RentalCar |
| AS | cover | Invoice | Rental |
| AS | send | Invoice | Company |
| AS | charge | Invoice | Customer |
| AS | keep | Company | RentalCar |
| AS | need | RentalCar | PreventiveMaintenance |
| AS | has | RentalCar | Damage |
| AS | want | Customer | RentalCar |



