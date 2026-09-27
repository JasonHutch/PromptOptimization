## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| literal | "car rental company" |
| literal | "rental locations" |
| literal | "passenger cars" |
| literal | "makes of cars" |
| literal | "models" |
| literal | "price classes" |
| literal | "rental plans" |
| literal | "daily unlimited miles plan" |
| literal | "weekend 10% discount plan" |
| literal | "automatic or manual gear change" |
| literal | "two or four doors" |
| literal | "sedan or hatchback" |
| literal | "reservation form" |
| literal | "file cabinet" |
| literal | "block reservation" |
| literal | "invoices" |
| literal | "credit card processing company" |
| literal | "preventive maintenance" |
| literal | "damage" |
| literal | "rental car purchase" |
| literal | "repair" |
| literal | "maintenance" |
| literal | "disposal information" |
| literal | "depreciation" |

## Step 2: Classification ledger

| phrase | label | element | arg1 | arg2 | evidence |
|---|---|---|---|---|---|
| car rental company | C | Company |  |  | "A car rental company operates a number of rental locations throughout the metropolitan area." |
| rental locations | C | Location |  |  | "A car rental company operates a number of rental locations throughout the metropolitan area." |
| passenger cars | C | VehicleType |  |  | "Although the company is, at present, concerned only with passenger cars, it may branch out into other forms of vehicle rentals in the future" |
| makes of cars | C | CarMake |  |  | "The company has several different makes of cars in its rental fleet, from different manufacturers." |
| models | C | CarModel |  |  | "Each make may have several models." |
| price classes | C | PriceClass |  |  | "The models are grouped into a small number of price classes." |
| rental plans | C | RentalPlan |  |  | "The company has a number of different rental plans available to customers." |
| daily unlimited miles plan | C | RentalPlan |  |  | "For example, there is a 'daily unlimited miles plan'" |
| weekend 10% discount plan | C | RentalPlan |  |  | "and a 'weekend 10% discount plan'." |
| automatic or manual gear change | A | CarFeature |  |  | "The company finds it important to have information available on the models of car, such as automatic or manual gear change" |
| two or four doors | A | CarFeature |  |  | "two or four doors" |
| sedan or hatchback | A | CarFeature |  |  | "and sedan or hatchback." |
| reservation form | C | ReservationForm |  |  | "The salespersons process the reservations manually using a reservation form" |
| file cabinet | C | Storage |  |  | "and archive them in the file cabinet." |
| block reservation | C | ReservationType |  |  | "Sometimes a customer wishes to make a block reservation for several cars" |
| invoices | C | Invoice |  |  | "As soon as a car is checked out to a customer, an invoice is opened." |
| credit card processing company | C | PaymentProcessor |  |  | "When the customer pays by a credit card, the rental charge will be processed through a credit card processing company." |
| preventive maintenance | V | MaintenanceType |  |  | "Rental cars need frequent preventive maintenance" |
| damage | V | CarDamage |  |  | "and, in addition, any damage to a car has to be repaired as soon as possible." |
| rental car purchase | V | CarAcquisition |  |  | "The company wants to keep track of the rental car purchase" |
| repair | V | CarRepair |  |  | "and, in addition, any damage to a car has to be repaired as soon as possible." |
| maintenance | V | CarMaintenance |  |  | "Rental cars need frequent preventive maintenance" |
| disposal information | V | CarDisposal |  |  | "and disposal information for business and tax purposes" |
| depreciation | V | CarValueChange |  |  | "e.g., depreciation of the rental cars." |



## Step 3: Model audits

| audit | result |
|---|---|
| source-span fidelity | pass |
| duplicate aliases | pass |
| class/attribute ownership | pass |
| relationship endpoints | pass |
| inheritance tests | pass |
| association-class conditions | pass |

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Company |  | CarRentalCompany |
| C | Location |  | RentalLocation |
| C | VehicleType |  | PassengerCar |
| C | CarMake |  | Toyota |
| C | CarModel |  | Corolla |
| C | PriceClass |  | Economy |
| C | RentalPlan |  | DailyUnlimitedMiles |
| A | CarFeature |  | AutomaticGear |
| A | CarFeature |  | TwoDoors |
| C | ReservationForm |  | RentalForm |
| C | Storage |  | FileCabinet |
| C | ReservationType |  | BlockReservation |
| C | Invoice |  | RentalInvoice |
| C | PaymentProcessor |  | CreditCardProcessor |
| V | MaintenanceType |  | PreventiveMaintenance |
| V | CarDamage |  | Damage |
| V | CarAcquisition |  | Purchase |
| V | CarRepair |  | Repair |
| V | CarMaintenance |  | Maintenance |
| V | CarDisposal |  | Disposal |
| V | CarValueChange |  | Depreciation |



