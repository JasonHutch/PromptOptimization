| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation | | |
| C | BusinessModel | | |
| C | CustomerService | | |
| C | Business | | |
| C | JobMarket | | |
| A | name | Business | |
| A | laborCost | Business | |
| A | operatingCost | Business | |
| A | rentalLocations | Business | |
| A | improvementProposals | Business | |
| C | PassengerCar | | |
| C | VehicleRental | | |
| C | ReservationSystem | | |
| C | RentalFleet | | |
| C | Manufacturer | | |
| C | Model | | |
| C | Toyota | Manufacturer | |
| C | Corolla | Model | Toyota |
| C | Camry | Model | Toyota |
| C | PriceClass | | |
| C | Make | | |
| C | RentalPlan | | |
| C | DailyUnlimitedMilesPlan | RentalPlan | |
| C | Weekend10PercentDiscountPlan | RentalPlan | |
| C | Car | PassengerCar | |
| A | automaticGearChange | Car | |
| A | manualGearChange | Car | |
| A | doors | Car | |
| C | Sedan | Car | |
| C | Hatchback | Car | |
| C | Salesperson | | |
| C | ReservationForm | | |
| C | FileCabinet | | |
| C | Contract | | |
| C | Invoice | | |
| C | CreditCardProcessingCompany | | |
| C | PreventiveMaintenance | | |
| C | Damage | | |
| C | Depreciation | | |
| AS | operates | Business | RentalLocation |
| AS | includes | BusinessModel | Business |
| AS | provides | Business | CustomerService |
| AS | operatesIn | Business | JobMarket |
| AS | incurs | Business | laborCost |
| AS | incurs | Business | operatingCost |
| AS | implements | Business | improvementProposals |
| AS | offers | Business | VehicleRental |
| AS | manages | Business | RentalFleet |
| AS | produces | Manufacturer | Model |
| AS | belongsTo | Model | Manufacturer |
| AS | groupedInto | Model | PriceClass |
| AS | selectedBy | Customer | Car |
| AS | processedBy | Business | CreditCardProcessingCompany |
| AS | undergoes | Car | PreventiveMaintenance |
| AS | subjectTo | Car | Damage |
| AS | experiences | Car | Depreciation |
| AG | Part-Of | RentalLocation | Business |
| AG | Part-Of | VehicleRental | Business |
| AG | Part-Of | RentalFleet | Business |
| AG | Part-Of | Model | Manufacturer |
| AG | Part-Of | Car | RentalFleet |
| AG | Part-Of | Invoice | Business |


