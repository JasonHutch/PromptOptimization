| label | element | arg1 | arg2 |
|---|---|---|---|
| C | CarRentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
| C | BusinessOperation |  |  |
| C | RentalCar |  |  |
| C | PassengerCar |  |  |
| C | VehicleRental |  |  |
| C | ReservationSystem |  |  |
| C | CarMake |  |  |
| C | CarModel |  |  |
| C | PriceClass |  |  |
| C | RentalPlan |  |  |
| C | AutomaticGearChange |  |  |
| C | ManualGearChange |  |  |
| C | TwoDoors |  |  |
| C | FourDoors |  |  |
| C | Sedan |  |  |
| C | Hatchback |  |  |
| C | RentalPrice |  |  |
| C | ReservationForm |  |  |
| C | FileCabinet |  |  |
| C | Contract |  |  |
| C | BlockReservation |  |  |
| C | Invoice |  |  |
| C | RentalCharge |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | DamageRepair |  |  |
| C | RentalCarPurchase |  |  |
| C | RentalCarRepair |  |  |
| C | RentalCarMaintenance |  |  |
| C | RentalCarDisposal |  |  |
| A | number | NumberOfRentalLocations |  |
| A | number | NumberOfYears |  |
| A | number | NumberOfCars |  |
| A | number | NumberOfMakes |  |
| A | number | NumberOfModels |  |
| A | number | NumberOfPriceClasses |  |
| A | number | NumberOfRentalPlans |  |
| A | number | NumberOfDoors |  |
| AS | operate | CarRentalLocation |  |
| AS | run | BusinessOperation |  |
| AS | consider | BusinessOperation | ImprovementProposal |
| AS | find | BusinessOperation | Solution |
| AS | branch out | CarRentalCompany | VehicleRental |
| AS | use | CarRentalCompany | ReservationSystem |
| AS | have | Customer | CarMake |
| AS | rent | Customer | CarModel |
| AS | display | System | Message |
| AS | let | System | Customer |
| AS | suggest | System | CarModel |
| AS | group | CarModel | PriceClass |
| AS | make | Customer | Reservation |
| AS | process | Salesperson | Reservation |
| AS | archive | ReservationForm | FileCabinet |
| AS | require | Customer | Deposit |
| AS | void | Reservation |  |
| AS | honor | Reservation |  |
| AS | satisfy | Reservation | Request |
| AS | handle | BlockReservation | Invoice |
| AS | check out | RentalCar | Customer |
| AS | open | Invoice | Rental |
| AS | cover | Invoice | Rental |
| AS | settle | Customer | Invoice |
| AS | send | Invoice | Company |
| AS | pay | Customer | RentalCharge |
| AS | process | CreditCardProcessingCompany | RentalCharge |
| AS | keep track | BusinessOperation | RentalCarPurchase |
| AS | keep track | BusinessOperation | RentalCarRepair |
| AS | keep track | BusinessOperation | RentalCarMaintenance |
| AS | keep track | BusinessOperation | RentalCarDisposal |



