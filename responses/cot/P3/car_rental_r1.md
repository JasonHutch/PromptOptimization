## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | vehicles / cars |
| 1 | location |
| 1 | makes |
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
| 1 | reservation form |
| 1 | deposit |
| 1 | contract |
| 1 | request |
| 1 | block reservation |
| 1 | invoices |
| 1 | rentals |
| 1 | company (billing) |
| 1 | credit card |
| 1 | rental charge |
| 1 | credit card processing company |
| 1 | maintenance |
| 1 | damage |
| 2 | makes of cars |
| 2 | models of car |
| 2 | time of reservation |
| 2 | depreciation of the rental cars |
| 3 | taken from |
| 3 | returned to |
| 3 | select |
| 3 | rent |
| 3 | grouped into |
| 3 | make (a reservation) |
| 3 | reserving |
| 3 | process |
| 3 | archive |
| 3 | sign |
| 3 | show up |
| 3 | satisfy |
| 3 | checked out to |
| 3 | open (invoice) |
| 3 | cover |
| 3 | settle |
| 3 | sent to |
| 3 | pays |
| 3 | processed through |
| 3 | repaired |
| 3 | need |
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
| 4 | disposal |
| 5 | a small number of |
| 5 | two |
| 5 | four |
| 5 | a given period of time |
| 5 | several |
| 5 | one or more |
| 5 | a number of |
| 6 | has several different makes of cars |
| 6 | may have several models |
| 6 | has a number of different rental plans |

## Step 2: Classification reasoning

vehicles / cars -> C : independent rental asset, main class, keep name "car"
location -> C : place with independent existence
makes -> C : brand of car, tracked independently
manufacturers -> merge with makes : same concept, "make" used as class name
models -> C : car model tracked with own attributes
price classes -> C : grouping entity models belong to
customer -> C : person interacting with business, has own data
rental plans -> C : plan with its own rules, independent entity
gear change -> A : property of Model, scalar
doors -> A : property of Model, scalar
rental prices -> dropped : no clear single owner, not literal enough to assign
options -> dropped : generic reference to model properties already captured
reservations -> C : reservation record class
salespersons -> C : staff role
reservation form -> merge with reservation : same paper record, one class
deposit -> dropped : mentioned only as business rule, no attribute value stated
contract -> C : signed document, independent
request -> merge with reservation : same concept (reservation request)
block reservation -> dropped : not an enumerated kind, absorbed into reservation-car association
invoices -> C : billing document
rentals -> AC : noun naming occurrence of car-customer checkout
company (billing) -> C : party invoices can be sent to
credit card -> C : payment instrument, independent entity
rental charge -> merge with invoice : same billed amount concept
credit card processing company -> C : external party processing payment
maintenance -> V : life-cycle step value of car
damage -> C : trackable entity needing repair
makes of cars -> AS : possession, company has makes (dropped, subject is background company)
models of car -> AS : relationship Car-Model
time of reservation -> A : attribute "time" of Reservation
depreciation of the rental cars -> dropped : background tax purpose detail, not tracked attribute
taken from -> AS : Car taken from Location
returned to -> AS : Car returned to Location
select -> AS : Customer selects Make/Model
rent -> AS : Customer rents Car
grouped into -> AS : Model grouped into Price class
make (a reservation) -> AS : Customer makes Reservation
reserving -> merge with make : same action, duplicate verb form
process -> AS : Salesperson processes Reservation
archive -> AS : Salesperson archives Reservation
sign -> AS : Customer signs Contract
show up -> dropped : no clear object class, vague
satisfy -> dropped : too vague, no second class
checked out to -> AS : Car checked out to Customer, basis of Rental AC
open (invoice) -> dropped : redundant with cover, no distinct actor
cover -> AS : Invoice covers Rental
settle -> AS : Customer settles Invoice
sent to -> AS : Invoice sent to Company
pays -> AS : Customer pays by Credit card
processed through -> AS : Invoice processed through Credit card processing company
repaired -> A : boolean state attribute of Damage
need -> dropped : vague, folded into maintenance value
available -> A : boolean attribute of Car
rented out -> dropped : duplicate state of available (false)
automatic -> V : value of gear change
manual -> V : value of gear change
sedan -> V : value of body type
hatchback -> V : value of body type
in person -> dropped : not tracked as attribute, channel detail only
through the phone -> dropped : same as above
voided -> V : value/state of Reservation
honored -> V : value/state of Reservation
purchase -> V : life-cycle event value of Car
repair -> V : life-cycle event value of Car
disposal -> V : life-cycle event value of Car
a small number of -> dropped : indefinite quantity, no attribute to attach
two -> V : value of doors
four -> V : value of doors
a given period of time -> dropped : indefinite quantity, business rule only
several -> dropped : indefinite quantity, no attribute
one or more -> dropped : multiplicity implied in Invoice-Rental association, not separate row
a number of -> dropped : indefinite quantity
has several different makes of cars -> dropped : subject is the rental company itself, excluded
may have several models -> AS : Make has Model
has a number of different rental plans -> dropped : subject is rental company, excluded

## Step 3: Review

- Merged "vehicles" and "cars" into a single class "car"; merged "manufacturers" into "make".
- Merged "reservation form" and "request" into "reservation" (same record, one class).
- Merged "rental charge" into "invoice".
- Dropped verbs with no identifiable second class ("show up", "satisfy", "need", "keep track of").
- Dropped possession clauses whose subject is the rental company itself (background actor, not a modeled class).
- Dropped indefinite quantities that could not be attached to a specific attribute or multiplicity.
- Confirmed "rented out" duplicates the boolean state already captured by attribute "available"; removed.
- Verified the checked-out-to association between Car and Customer is many-to-many over time and that the text names its occurrence ("rentals") and keeps information about it (invoice coverage) — modeled as association class Rental.
- Checked every remaining AS row connects two classes present in the C/AC list.
- No class remains without attributes or relationships; Price class, Rental plan, Company, Credit card, Credit card processing company, Contract, Damage, Location, Salesperson all carry at least one relationship.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | car | | |
| C | location | | |
| C | make | | |
| C | model | | |
| C | price class | | |
| C | customer | | |
| C | rental plan | | |
| C | reservation | | |
| C | salesperson | | |
| C | contract | | |
| C | invoice | | |
| C | company | | |
| C | credit card | | |
| C | credit card processing company | | |
| C | damage | | |
| A | available | car | |
| A | life-cycle event | car | |
| A | gear change | model | |
| A | doors | model | |
| A | body type | model | |
| A | time | reservation | |
| A | voided | reservation | |
| A | honored | reservation | |
| A | repaired | damage | |
| V | purchase | life-cycle event | |
| V | repair | life-cycle event | |
| V | maintenance | life-cycle event | |
| V | disposal | life-cycle event | |
| V | automatic | gear change | |
| V | manual | gear change | |
| V | two | doors | |
| V | four | doors | |
| V | sedan | body type | |
| V | hatchback | body type | |
| AS | taken from | car | location |
| AS | returned to | car | location |
| AS | select | customer | make |
| AS | select | customer | model |
| AS | rent | customer | car |
| AS | has | make | model |
| AS | grouped into | model | price class |
| AS | make | customer | reservation |
| AS | process | salesperson | reservation |
| AS | archive | salesperson | reservation |
| AS | sign | customer | contract |
| AS | checked out to | car | customer |
| AS | cover | invoice | rental |
| AS | settle | customer | invoice |
| AS | sent to | invoice | company |
| AS | pays by | customer | credit card |
| AS | processed through | invoice | credit card processing company |
| AS | has | car | damage |
| AC | rental | car | customer |