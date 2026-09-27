| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
| C | JobMarket |  |  |
| C | LaborCost |  |  |
| C | OperatingCost |  |  |
| C | BusinessOperation |  |  |
| C | PassengerCar |  |  |
| C | VehicleRental |  |  |
| C | ReservationSystem |  |  |
| C | RentalFleet |  |  |
| C | Make |  |  |
| C | Model |  |  |
| C | PriceClass |  |  |
| C | RentalPlan |  |  |
| C | GearChange |  |  |
| C | RentalPrice |  |  |
| C | ReservationForm |  |  |
| C | FileCabinet |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | RentalCarPurchase |  |  |
| C | Depreciation |  |  |
| A | Number | number of rental locations |  |
| A | Number | number of years |  |
| A | Number | number of makes |  |
| A | Number | number of models |  |
| A | Number | number of price classes |  |
| A | Number | number of rental plans |  |
| A | Number | number of cars |  |
| A | Number | number of rentals |  |
| AS | operate | RentalLocation |  |
| AS | operate | BusinessModel |  |
| AS | operate | CustomerService |  |
| AS | track | OperatingCost |  |
| AS | reduce | OperatingCost |  |
| AS | consider | ImprovementProposal |  |
| AS | branchOut | BusinessModel | VehicleRental |
| AS | use | ReservationSystem |  |
| AS | have | Make | Model |
| AS | select | Customer | Make |
| AS | display | Message |  |
| AS | suggest | System | Make |
| AS | find | Customer | RentalPlan |
| AS | make | Customer | Reservation |
| AS | process | Salesperson | Reservation |
| AS | archive | Reservation | FileCabinet |
| AS | void | Reservation |  |
| AS | honor | Reservation | RentalCar |
| AS | make | Customer | BlockReservation |
| AS | handle | Invoice | Rental |
| AS | open | Invoice | Rental |
| AS | cover | Invoice | Rental |
| AS | settle | Customer | Invoice |
| AS | send | Invoice | Company |
| AS | process | CreditCardProcessingCompany | RentalCharge |
| AS | keep | Company | RentalCarPurchase |
| AS | track | Company | RentalCarMaintenance |
| AS | dispose | Company | RentalCar |



