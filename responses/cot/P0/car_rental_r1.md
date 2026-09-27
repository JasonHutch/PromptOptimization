## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 5 | a number of rental locations |
| 3 | taken from (location) |
| 3 | returned to (location) |
| 4 | additional charge |
| 1 | passenger cars |
| 1 | vehicle rentals |
| 2 | makes of cars |
| 1 | manufacturers |
| 6 | each make may have several models |
| 1 | models |
| 2 | price classes (of models) |
| 3 | grouped into |
| 3 | select (make and model) |
| 4 | rented out |
| 4 | available |
| 3 | suggest (similar models) |
| 1 | rental plans |
| 4 | daily unlimited miles plan |
| 4 | weekend 10% discount plan |
| 4 | automatic or manual gear change |
| 4 | two or four doors |
| 4 | sedan or hatchback |
| 1 | rental prices |
| 1 | customer |
| 3 | make reservations |
| 1 | salespersons |
| 3 | process (the reservations) |
| 1 | reservation |
| 4 | no deposit required |
| 4 | voided |
| 3 | sign (the contract) |
| 1 | contract |
| 5 | more than a given period of time |
| 4 | honored |
| 1 | block reservation |
| 5 | several cars |
| 1 | invoice |
| 1 | rentals |
| 3 | checked out to |
| 4 | opened (invoice) |
| 3 | cover (rentals) |
| 3 | settle (the invoice) |
| 3 | sent to (a company) |
| 3 | pays by (credit card) |
| 1 | credit card |
| 1 | credit card processing company |
| 3 | processed through |
| 1 | rental charge |
| 4 | available for rental |
| 1 | preventive maintenance |
| 1 | damage |
| 3 | repaired |
| 1 | purchase |
| 1 | repair |
| 1 | disposal |
| 2 | depreciation of the rental cars |

## Step 2: Classification reasoning

a number of rental locations -> C RentalLocation + multiplicity : locations are independently existing places
taken from (location) -> AS taken-from(Rental, RentalLocation) : pickup relationship between rental and location
returned to (location) -> AS returned-to(Rental, RentalLocation) : drop-off relationship between rental and location
additional charge -> A additionalCharge of Rental : scalar value describing a rental
passenger cars -> I PassengerCar ISA Vehicle : subtype of general Vehicle concept
vehicle rentals -> C Vehicle : independent rentable entity, future vehicle types implied
makes of cars -> A/C Make of Vehicle : make is a classifying entity, kept as class
manufacturers -> attribute merged into Make : manufacturer name describes Make
each make may have several models -> AG Part-of Model - Make : model belongs to a make
models -> C Model : independently tracked rentable variant
price classes (of models) -> C PriceClass : classification entity grouping models
grouped into -> AS grouped-into(Model, PriceClass) : classification relationship
select (make and model) -> AS select(Customer, Model) : customer action on model
rented out -> V rentedOut of availability(Vehicle) : state value of vehicle
available -> V available of availability(Vehicle) : state value of vehicle
suggest (similar models) -> excluded : system suggestion, not a stored domain fact
rental plans -> C RentalPlan : named plan entity with rules
daily unlimited miles plan -> V of name(RentalPlan) : example plan name value
weekend 10% discount plan -> V of name(RentalPlan) : example plan name value
automatic or manual gear change -> A transmission of Model, V automatic/manual : model property values
two or four doors -> A doorCount of Model, V two/four : model property values
sedan or hatchback -> A bodyStyle of Model, V sedan/hatchback : model property values
rental prices -> A rentalCharge of Invoice : scalar monetary value
customer -> C Customer : person entity engaging in rentals
make reservations -> AS make(Customer, Reservation) : customer creates reservation
salespersons -> C Salesperson : staff role entity
process (the reservations) -> AS process(Salesperson, Reservation) : staff action on reservation
reservation -> C Reservation : independently tracked booking record
no deposit required -> A deposit of Reservation : scalar value (may be zero)
voided -> V voided of status(Reservation) : reservation state value
sign (the contract) -> AS sign(Customer, Contract) : customer action creating contract
contract -> C Contract : legal document entity
more than a given period of time -> A gracePeriod of Reservation : numeric constraint value
honored -> V honored of status(Reservation) : reservation state value
block reservation -> I BlockReservation ISA Reservation : special reservation type for several cars
several cars -> multiplicity of BlockReservation-Vehicle : quantity constraint
invoice -> C Invoice : independently tracked billing document
rentals -> C Rental : independently tracked rental transaction
checked out to -> AS checked-out-to(Vehicle, Customer) : action creating a rental
opened (invoice) -> V opened of status(Invoice) : invoice state value
cover (rentals) -> AS cover(Invoice, Rental) : invoice covers one or more rentals
settle (the invoice) -> AS settle(Customer, Invoice) : customer action closing invoice
sent to (a company) -> AS sent-to(Invoice, Company) : invoice billed to employer
pays by (credit card) -> AS pays-by(Customer, CreditCard) : payment relationship
credit card -> C CreditCard : payment instrument entity
credit card processing company -> C CreditCardProcessingCompany : external processing entity
processed through -> AS processed-through(Invoice, CreditCardProcessingCompany) : payment processing relationship
rental charge -> A rentalCharge of Invoice : scalar monetary value (duplicate merged)
available for rental -> V available of availability(Vehicle) : duplicate state merged
preventive maintenance -> C Maintenance : trackable service record
damage -> A damage of Repair : descriptive attribute of a repair event
repaired -> AS repaired(Vehicle, Repair) : action linking vehicle to repair record
purchase -> C Purchase : trackable acquisition record
repair -> C Repair : trackable repair record
disposal -> C Disposal : trackable disposal record
depreciation of the rental cars -> A depreciation of Vehicle : scalar value tracked for tax purposes

## Step 3: Review

- Merged "manufacturer" into Make as descriptive concept rather than separate class (no independent tracking needed).
- Removed "suggest similar models" as a system-suggestion capability, not a stored domain fact.
- Merged duplicate "rental prices"/"rental charge" into single attribute rentalCharge of Invoice.
- Merged duplicate "available"/"available for rental" into a single attribute availability of Vehicle.
- Kept Purchase, Repair, Maintenance, Disposal as separate classes since each is a distinct tracked business/tax record type; associated each to Vehicle.
- Verified BlockReservation and PassengerCar inheritance pass IS-A and conformance tests (both are proper specializations).
- Removed ReservationForm and file cabinet from the model as they are implementation/manual-process artifacts, not domain concepts to persist in the target system.
- Confirmed every attribute has exactly one owning class and every relationship connects only listed classes.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation | | |
| C | Vehicle | | |
| I | ISA | PassengerCar | Vehicle |
| C | Make | | |
| C | Model | | |
| C | PriceClass | | |
| C | RentalPlan | | |
| C | Customer | | |
| C | Salesperson | | |
| C | Reservation | | |
| I | ISA | BlockReservation | Reservation |
| C | Rental | | |
| C | Invoice | | |
| C | Contract | | |
| C | CreditCard | | |
| C | CreditCardProcessingCompany | | |
| C | Company | | |
| C | Purchase | | |
| C | Repair | | |
| C | Maintenance | | |
| C | Disposal | | |
| A | additionalCharge | Rental | |
| A | deposit | Reservation | |
| A | gracePeriod | Reservation | |
| A | status | Reservation | |
| A | status | Invoice | |
| A | rentalCharge | Invoice | |
| A | transmission | Model | |
| A | doorCount | Model | |
| A | bodyStyle | Model | |
| A | name | RentalPlan | |
| A | discount | RentalPlan | |
| A | availability | Vehicle | |
| A | depreciation | Vehicle | |
| A | damage | Repair | |
| V | available | availability | |
| V | rentedOut | availability | |
| V | automatic | transmission | |
| V | manual | transmission | |
| V | two | doorCount | |
| V | four | doorCount | |
| V | sedan | bodyStyle | |
| V | hatchback | bodyStyle | |
| V | daily unlimited miles plan | name | |
| V | weekend 10% discount plan | name | |
| V | voided | status (Reservation) | |
| V | honored | status (Reservation) | |
| V | opened | status (Invoice) | |
| AS | taken-from | Rental | RentalLocation |
| AS | returned-to | Rental | RentalLocation |
| AS | select | Customer | Model |
| AS | grouped-into | Model | PriceClass |
| AS | make | Customer | Reservation |
| AS | process | Salesperson | Reservation |
| AS | sign | Customer | Contract |
| AS | reserve | Reservation | Vehicle |
| AS | checked-out-to | Vehicle | Customer |
| AS | cover | Invoice | Rental |
| AS | settle | Customer | Invoice |
| AS | sent-to | Invoice | Company |
| AS | pays-by | Customer | CreditCard |
| AS | processed-through | Invoice | CreditCardProcessingCompany |
| AS | uses | Rental | RentalPlan |
| AS | undergoes | Vehicle | Maintenance |
| AS | repaired | Vehicle | Repair |
| AS | has | Vehicle | Purchase |
| AS | has | Vehicle | Disposal |
| AG | Part-of | Model | Make |