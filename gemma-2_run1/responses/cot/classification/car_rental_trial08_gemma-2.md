| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation |  |  |
| C | BusinessModel |  |  |
| C | CustomerService |  |  |
| C | Business |  |  |
| C | Costs |  |  |
| C | JobMarket |  |  |
| C | LaborCost |  |  |
| C | Solution |  |  |
| C | OperatingCost |  |  |
| C | BusinessOperation |  |  |
| C | ImprovementProposal |  |  |
| C | Vehicle |  |  |
| C | PassengerCar |  |  |
| C | VehicleRental |  |  |
| C | ReservationSystem |  |  |
| C | Make |  |  |
| C | Model |  |  |
| C | PriceClass |  |  |
| C | RentalPlan |  |  |
| C | Customer |  |  |
| C | Reservation |  |  |
| C | Invoice |  |  |
| C | RentalCharge |  |  |
| C | CreditCardProcessingCompany |  |  |
| C | PreventiveMaintenance |  |  |
| C | Damage |  |  |
| C | Repair |  |  |
| C | Purchase |  |  |
| C | Disposal |  |  |
| C | Depreciation |  |  |
| A | NumberOfRentalLocations |  |  |
| A | NumberOfYears |  |  |
| A | NumberOfEmployees |  |  |
| A | NumberOfCars |  |  |
| A | NumberOfMakes |  |  |
| A | NumberOfModels |  |  |
| A | NumberOfPriceClasses |  |  |
| A | NumberOfRentalPlans |  |  |
| A | NumberOfDoors |  |  |
| A | NumberOfRentals |  |  |
| AS | operate | Business | RentalLocation |
| AS | provide | Business | CustomerService |
| AS | track | Business |  |
| AS | increase | Costs |  |
| AS | find | Business | Solution |
| AS | reduce | Business | OperatingCost |
| AS | describe | Business | BusinessOperation |
| AS | consider | Business | ImprovementProposal |
| AS | take | Vehicle | RentalLocation |
| AS | return | Vehicle | RentalLocation |
| AS | branch | Business | VehicleRental |
| AS | use | Business | ReservationSystem |
| AS | have | Customer | Make |
| AS | select | Customer | Model |
| AS | display | System | Customer |
| AS | let | System | Customer |
| AS | suggest | System | Customer |
| AS | have | Customer | RentalPlan |
| AS | make | Customer | Reservation |
| AS | rent | Customer | Vehicle |
| AS | find | Business | RentalPlan |
| AS | have | Business | RentalPlan |
The table must not contain any of the following:

*  UI/system/storage concepts
*  Merged aliases


