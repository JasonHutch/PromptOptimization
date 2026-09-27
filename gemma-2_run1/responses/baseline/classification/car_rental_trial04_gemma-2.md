| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation | | |
| C | BusinessModel | | |
| C | CustomerService | | |
| C | LaborCost | | |
| C | OperatingCost | | |
| C | RentalFleet | | |
| C | Make | | |
| C | Model | | |
| C | PriceClass | | |
| C | RentalPlan | | |
| C | DailyUnlimitedMilesPlan | | |
| C | Weekend10PercentDiscountPlan | | |
| C | AutomaticGearChange | | |
| C | ManualGearChange | | |
| C | TwoOrFourDoors | | |
| C | Sedan | | |
| C | Hatchback | | |
| C | RentalCar | | |
| C | PreventiveMaintenance | | |
| C | RentalCarPurchase | | |
| C | Repair | | |
| C | Maintenance | | |
| C | DisposalInformation | | |
| C | RentalCar | | |
| A | number_of_locations | RentalLocation | |
| A | color | RentalCar | |
| AS | boomed | RentalLocation | RentalCar |
| AS | run | BusinessModel | RentalLocation |
| AS | find | CustomerService | Customer |
| AS | described | RentalCar | Make |
| AS | grouped | RentalCar | PriceClass |
| AS | select | Customer | RentalCar |
| AS | display | System | RentalCar |
| AS | suggest | System | Customer |
| AS | have | RentalLocation | RentalCar |
| AS | available | RentalCar | Customer |
| AS | make | RentalCar | Make |
| AS | model | RentalCar | Model |
| AS | settle | Customer | RentalCar |
| AS | sent | Invoice | Customer |
| AS | pay | Customer | Invoice |
| AS | processed | Invoice | System |
| AS | keep_track_of | System | RentalCar |
| C | Invoice | | |
| C | System | | |
| A | number | RentalLocation | |
| A | several | RentalCar | |
| A | several | RentalPlan | |
| A | 10% | Weekend10PercentDiscountPlan | |
| A | company_has | BusinessModel | |
| A | company_has | CustomerService | |
| A | company_may_have | RentalFleet | |
| A | system_should_display | System | RentalCar |
| A | system_should_suggest | System | RentalCar |
| A | company_has | RentalLocation | |
| A | company_finds | RentalCar | |
| A | company_wants | RentalCar | |
| A | company | BusinessModel | |
| AS | consist_of | RentalFleet | RentalCar |
| AS | returned_to | RentalCar | RentalLocation |
| AS | returned_to | RentalCar | Customer |
| AS | consist_of | RentalCar | Make |




