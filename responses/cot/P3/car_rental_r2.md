## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | car rental company |
| 1 | rental locations |
| 1 | vehicles |
| 1 | location |
| 1 | additional charge |
| 1 | passenger cars |
| 1 | vehicle rentals |
| 1 | makes |
| 1 | cars |
| 1 | rental fleet |
| 1 | manufacturers |
| 1 | models |
| 1 | price classes |
| 1 | customer |
| 1 | rental plans |
| 1 | gear change |
| 1 | doors |
| 1 | rental prices |
| 1 | options |
| 1 | reservations |
| 1 | salespersons |
| 1 | deposit |
| 1 | contract |
| 1 | invoices |
| 1 | rentals |
| 1 | block reservation |
| 1 | credit card |
| 1 | rental charge |
| 1 | credit card processing company |
| 1 | employer |
| 2 | makes of cars |
| 2 | models of car |
| 2 | time of reservation |
| 2 | period of time |
| 2 | depreciation of the rental cars |
| 3 | operates |
| 3 | taken from |
| 3 | returned to |
| 3 | grouped into |
| 3 | select |
| 3 | rent |
| 3 | reserving |
| 3 | make |
| 3 | process |
| 3 | archive |
| 3 | sign |
| 3 | show up |
| 3 | checked out |
| 3 | opened |
| 3 | cover |
| 3 | settle |
| 3 | returned |
| 3 | sent to |
| 3 | pays by |
| 3 | processed through |
| 3 | repaired |
| 3 | keep track of |
| 3 | handled |
| 4 | available |
| 4 | rented out |
| 4 | automatic |
| 4 | manual |
| 4 | sedan |
| 4 | hatchback |
| 4 | in person |
| 4 | through the phone |
| 4 | voided |
| 4 | honored |
| 4 | purchase |
| 4 | repair |
| 4 | maintenance |
| 4 | disposal |
| 5 | a number of |
| 5 | a small number of |
| 5 | two |
| 5 | four |
| 5 | one or more |
| 6 | has several different makes of cars |
| 6 | each make may have several models |
| 6 | company has a number of different rental plans |

## Step 2: Classification reasoning

car rental company -> excluded : the enterprise itself, not a modeled entity
rental locations -> C RentalLocation : independent place where business occurs
vehicles -> C Vehicle : general asset, independent existence
location -> merged into RentalLocation : same concept as rental locations
additional charge -> A additional charge (Rental) : fee describing a rental
passenger cars -> C PassengerCar : current kind of vehicle with own scope
vehicle rentals -> merged into Vehicle concept : future kind, no new info
makes -> C Make : independent classification object
cars -> merged into Vehicle : same concept, plural form
rental fleet -> excluded : collective term, no separate info tracked
manufacturers -> A manufacturer (Make) : scalar property of a make
models -> C Model : independent object with own attributes
price classes -> A price class (Model) : grouping property of model
customer -> C Customer : independent role/person
rental plans -> C RentalPlan : independent named offering
gear change -> A gear change (Model) : property with enumerated values
doors -> A number of doors (Model) : property with enumerated values
rental prices -> merged into rental charge/plan : price info already captured
options -> excluded : refers to model attributes already listed
reservations -> C Reservation : independent tracked entity
salespersons -> C Salesperson : independent role
deposit -> A deposit (Reservation) : scalar property of reservation
contract -> C Contract : signed document, independent
invoices -> C Invoice : independent billing document
rentals -> AC Rental : occurrence of vehicle checkout, own info
block reservation -> C BlockReservation : reservation kind with own rule
credit card -> C CreditCard : payment instrument used by customer
rental charge -> A rental charge (Invoice) : scalar amount
credit card processing company -> C CreditCardProcessingCompany : external independent party
employer -> C Employer : independent billing party
makes of cars -> AS has (Vehicle, Make) : each car associated with a make
models of car -> merged into Model attributes : same X of Y concept
time of reservation -> A time (Reservation) : scalar property
period of time -> excluded : vague duration, no attribute defined
depreciation of the rental cars -> A depreciation (Vehicle) : scalar tracked value
operates -> excluded : subject (company) not modeled as class
taken from -> AS taken from (Rental, RentalLocation) : pickup location link
returned to -> AS returned to (Rental, RentalLocation) : return location link
grouped into -> reflected in A price class (Model) : no separate class needed
select -> AS select (Customer, Model) : customer chooses model
rent -> AS rent (Customer, Vehicle) : customer rents vehicle
reserving -> merged with make (reservations) : same action
make -> AS make (Customer, Reservation) : customer creates reservation
process -> AS process (Salesperson, Reservation) : staff processes reservation
archive -> AS archive (Salesperson, Reservation) : staff files reservation
sign -> AS sign (Customer, Contract) : customer signs document
show up -> excluded : intransitive, no object class
checked out -> AS checked out to (Vehicle, Customer) : vehicle given to customer
opened -> reflected in Invoice creation : covered by cover association
cover -> AS cover (Invoice, Rental) : invoice covers rentals
settle -> AS settle (Customer, Invoice) : customer pays invoice
returned -> A returned (Rental) : state of rental occurrence
sent to -> AS sent to (Invoice, Employer) : invoice billed to employer
pays by -> AS pays by (Customer, CreditCard) : payment method
processed through -> AS processed through (Invoice, CreditCardProcessingCompany) : charge processed
repaired -> reflected in A type (MaintenanceRecord) : value "repair"
keep track of -> AS keep track of (Vehicle, MaintenanceRecord) : history tracked
handled -> reflected in AS cover (Invoice, Rental) : invoices handled together
available -> V available (availability) : vehicle state
rented out -> V rented out (availability) : vehicle state
automatic -> V automatic (gear change) : model property value
manual -> V manual (gear change) : model property value
sedan -> V sedan (body style) : model property value
hatchback -> V hatchback (body style) : model property value
in person -> excluded : channel of making reservation, not tracked entity
through the phone -> excluded : same as above
voided -> A voided (Reservation) : boolean state
honored -> A honored (Reservation) : boolean state
purchase -> V purchase (type) : maintenance record life-cycle step
repair -> V repair (type) : maintenance record life-cycle step
maintenance -> V maintenance (type) : maintenance record life-cycle step
disposal -> V disposal (type) : maintenance record life-cycle step
a number of -> multiplicity : indefinite quantity of locations/plans
a small number of -> multiplicity : indefinite quantity of price classes
two -> V two (number of doors) : enumerated value
four -> V four (number of doors) : enumerated value
one or more -> multiplicity : invoice-to-rental multiplicity
has several different makes of cars -> AS has (Vehicle, Make) : duplicate of X of Y row
each make may have several models -> AS has (Make, Model) : make possesses models
company has a number of different rental plans -> reflected via RentalPlan class : company subject excluded

## Step 3: Review

- Removed "car rental company" as a class; it is the business itself, not a domain object to model.
- Merged "cars", "vehicle rentals", "location" into Vehicle/RentalLocation to avoid duplicate classes.
- Dropped "rental fleet", "options", "period of time", "in person"/"through the phone" as they add no separate attribute or class.
- Confirmed BlockReservation qualifies as a subclass (own rule: covers several vehicles, invoices handled together), not just a value.
- Confirmed PassengerCar qualifies as a subclass of Vehicle (system must later support other vehicle kinds; passenger car has the current business rules).
- Checked Rental (Customer x Vehicle checkout) against association-class rules: many customers rent many vehicles over time (many-to-many across time), and occurrence-specific data (additional charge, checked out, returned) must be kept → confirmed as AC, not output as C.
- Checked Invoice–Rental: one invoice covers many rentals but a rental belongs to one invoice → ordinary association, no association class needed.
- Verified every attribute has exactly one owning class and no class is used as an attribute type.
- Verified every AS/AC/I connects only to classes listed as C or AC.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation | | |
| C | Vehicle | | |
| C | PassengerCar | | |
| C | Make | | |
| C | Model | | |
| C | RentalPlan | | |
| C | Customer | | |
| C | Reservation | | |
| C | BlockReservation | | |
| C | Invoice | | |
| C | CreditCard | | |
| C | CreditCardProcessingCompany | | |
| C | Salesperson | | |
| C | Contract | | |
| C | MaintenanceRecord | | |
| C | Employer | | |
| AC | Rental | Customer | Vehicle |
| A | availability | Vehicle | |
| V | available | availability | |
| V | rented out | availability | |
| A | depreciation | Vehicle | |
| A | manufacturer | Make | |
| A | price class | Model | |
| A | gear change | Model | |
| V | automatic | gear change | |
| V | manual | gear change | |
| A | number of doors | Model | |
| V | two | number of doors | |
| V | four | number of doors | |
| A | body style | Model | |
| V | sedan | body style | |
| V | hatchback | body style | |
| A | time | Reservation | |
| A | deposit | Reservation | |
| A | voided | Reservation | |
| A | honored | Reservation | |
| A | rental charge | Invoice | |
| A | settled | Invoice | |
| A | type | MaintenanceRecord | |
| V | purchase | type | |
| V | repair | type | |
| V | maintenance | type | |
| V | disposal | type | |
| A | additional charge | Rental | |
| A | checked out | Rental | |
| A | returned | Rental | |
| AS | taken from | Rental | RentalLocation |
| AS | returned to | Rental | RentalLocation |
| AS | select | Customer | Model |
| AS | rent | Customer | Vehicle |
| AS | make | Customer | Reservation |
| AS | process | Salesperson | Reservation |
| AS | archive | Salesperson | Reservation |
| AS | sign | Customer | Contract |
| AS | checked out to | Vehicle | Customer |
| AS | cover | Invoice | Rental |
| AS | settle | Customer | Invoice |
| AS | sent to | Invoice | Employer |
| AS | pays by | Customer | CreditCard |
| AS | processed through | Invoice | CreditCardProcessingCompany |
| AS | has | Vehicle | Make |
| AS | has | Make | Model |
| AS | has | Rental | RentalPlan |
| AS | keep track of | Vehicle | MaintenanceRecord |
| AS | covers | BlockReservation | Vehicle |
| I | ISA | PassengerCar | Vehicle |
| I | ISA | BlockReservation | Reservation |