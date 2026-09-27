| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
| C | Business |  |  |
| C | Cost |  |  |
| C | JobMarket |  |  |
| C | LaborCost |  |  |
| C | Solution |  |  |
| C | OperatingCost |  |  |
| C | BusinessOperation |  |  |
| C | ImprovementProposal |  |  |
| C | PassengerCar |  |  |
| C | VehicleRental |  |  |
| C | ReservationSystem |  |  |
| C | Make |  |  |
| C | Model |  |  |
| C | PriceClass |  |  |
| C | Customer |  |  |
| C | RentalPlan |  |  |
| C | GearChange |  |  |
| C | RentalPrice |  |  |
| C | Salesperson |  |  |
| C | ReservationForm |  |  |
| C | FileCabinet |  |  |
| C | Deposit |  |  |
| C | Contract |  |  |
| C | Period |  |  |
| C | Reservation |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | Rental |  |  |
| C | CreditCard |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | Purchase |  |  |
| C | Disposal |  |  |
| C | Depreciation |  |  |
| A | number |  | NumberOfVehicles |
| A | number |  | NumberOfRentalLocations |
| A | number |  | NumberOfMakes |
| A | number |  | NumberOfModels |
| A | number |  | NumberOfPriceClasses |
| A | number |  | NumberOfRentalPlans |
| AS | operate | RentalLocation | Business |
| AS | is | Business | BusinessModel |
| AS | manage | Business | Costs |
| AS | control | Business | OperatingCost |
| AS | reduce | Business | OperatingCost |
| AS | find | Business | Solution |
| AS | consider | Business | ImprovementProposal |
| AS | select | Customer | Make |
| AS | display | System | Customer |
| AS | let | System | Customer |
| AS | suggest | System | Customer |
| AS | handle | Business | Invoice |
| AS | settle | Customer | Invoice |
| AS | process | CreditCardProcessingCompany | RentalCharge |
| AS | track | Business | RentalCar |
| AS | keep | Business | RentalCar |
| AS | have | Business | RentalCar |
| V | available |  | Available |
| V | rented out |  | RentedOut |
| V | active |  | Active |
| V | manual |  | Manual |
| V | automatic |  | Automatic |
| V | direct |  | Direct |
| V | given |  | Given |


