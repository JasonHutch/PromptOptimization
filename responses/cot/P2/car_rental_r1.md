## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | car rental company |
| 1 | rental locations |
| 1 | vehicles / cars |
| 1 | location |
| 1 | additional charge |
| 1 | passenger cars |
| 1 | makes |
| 1 | rental fleet |
| 1 | manufacturers |
| 1 | models |
| 1 | price classes |
| 1 | customer |
| 1 | rental plans |
| 1 | gear change |
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
| 1 | employer |
| 1 | credit card |
| 1 | rental charge |
| 1 | credit card processing company |
| 1 | damage |
| 1 | preventive maintenance |
| 2 | makes of cars |
| 2 | models of car |
| 2 | time of reservation |
| 2 | period of time |
| 2 | depreciation of the rental cars |
| 3 | operates |
| 3 | taken from |
| 3 | returned to |
| 3 | select |
| 3 | rent |
| 3 | grouped into |
| 3 | reserving |
| 3 | make (reservations) |
| 3 | process |
| 3 | archive |
| 3 | voided |
| 3 | show up |
| 3 | sign |
| 3 | honored |
| 3 | satisfy |
| 3 | checked out to |
| 3 | opened |
| 3 | cover |
| 3 | settle |
| 3 | sent to |
| 3 | pays by |
| 3 | processed through |
| 3 | repaired |
| 4 | available |
| 4 | rented out |
| 4 | automatic |
| 4 | manual |
| 4 | sedan |
| 4 | hatchback |
| 4 | in person |
| 4 | through the phone |
| 4 | purchase |
| 4 | repair |
| 4 | maintenance |
| 4 | disposal |
| 5 | a number of |
| 5 | one |
| 5 | several |
| 5 | a small number of |
| 5 | two |
| 5 | four |
| 5 | one or more |
| 6 | has several different makes of cars |
| 6 | may have several models |
| 6 | has a number of different rental plans |

## Step 2: Classification reasoning

car rental company -> C : independent business entity with a relationship to locations
rental locations -> C "rental location" : independent place object
vehicles / cars -> C "car" : same rentable object, merge synonyms, use most-used term
location -> merged into "rental location" : same concept, singular form
additional charge -> A of rental : scalar fee incurred on the rental event
passenger cars -> merged into "car" : kind differs only by scope, not own rules
makes -> C "make" : has own relationships (models, manufacturer)
rental fleet -> excluded : redundant collection of cars, no own attributes
manufacturers -> C "manufacturer" : independent supplier entity
models -> C "model" : has own attributes (gear, doors, body) and price class
price classes -> C "price class" : independent grouping entity
customer -> C : independent person
rental plans -> C "rental plan" : has own price/rules
gear change -> A of model : scalar property with enumerated values
rental prices -> A "price" of rental plan : scalar cost value
options -> excluded : covered by model's own attributes
reservations -> AC "reservation" : occurrence of customer selecting a model, has own state
salespersons -> C "salesperson" : independent role/person
reservation form -> excluded : paper artifact, duplicate of reservation
deposit -> A of reservation : scalar amount tied to a reservation
contract -> C : signed document, independent object
request -> merged into "reservation" : same concept
block reservation -> excluded : differs from reservation only by scale
invoices -> C "invoice" : independent billing document
rentals -> AC "rental" : occurrence of car checked out to customer
employer -> C : independent entity invoice can be sent to
credit card -> C : independent payment instrument
rental charge -> A of invoice : scalar money value
credit card processing company -> C : independent external entity
damage -> C "damage" : tracked event needing repair, own record
preventive maintenance -> merged into "maintenance" V : life-cycle step value
makes of cars -> possession, make is class, car relates via model : covered by has/model chain
models of car -> "model" already class, "car" already class : X of Y realized as association
time of reservation -> A "time" of reservation : scalar attribute of the reservation
period of time -> excluded : business rule constant, not a stored attribute
depreciation of the rental cars -> excluded : tax bookkeeping concept, not separately tracked here
operates -> AS operates : car rental company / rental location
taken from -> AS taken from : rental / rental location
returned to -> AS returned to : rental / rental location
select -> AS select : customer / model (base association for reservation)
rent -> AS rent : customer / car (base association for rental)
grouped into -> AS grouped into : model / price class
reserving -> merged into "select" : same action
make (reservations) -> merged into AC reservation creation : same action
process -> AS process : salesperson / reservation
archive -> AS archive : salesperson / reservation
voided -> A "voided" of reservation : boolean state of the reservation occurrence
show up -> excluded : narrative detail, not stored fact
sign -> AS sign : customer / contract
honored -> excluded : redundant with voided state
satisfy -> excluded : describes availability rule, not stored fact
checked out to -> A "checked out" of rental : boolean/date state of rental occurrence
opened -> excluded : redundant with invoice creation, not separate fact
cover -> AS cover : invoice / rental
settle -> AS settle : customer / invoice
sent to -> AS sent to : invoice / employer
pays by -> AS pays by : customer / credit card
processed through -> AS processed through : invoice / credit card processing company
repaired -> AS repaired : damage / car
available -> A "available" of car : boolean state
rented out -> merged into "available" : opposite state, same attribute
automatic -> V of gear change (model)
manual -> V of gear change (model)
sedan -> V of body type (model)
hatchback -> V of body type (model)
in person -> excluded : channel detail, no stored business rule
through the phone -> excluded : channel detail, no stored business rule
purchase -> V of type (car record)
repair -> V of type (car record)
maintenance -> V of type (car record)
disposal -> V of type (car record)
a number of / several / a small number of / one or more -> multiplicities : not output as rows
two -> V of number of doors (model)
four -> V of number of doors (model)
has several different makes of cars -> AS has : car rental company / make
may have several models -> AS has : make / model
has a number of different rental plans -> AS has : car rental company / rental plan

## Step 3: Review

- Merged "vehicles", "cars", "passenger cars" into one class "car".
- Merged "location" and "rental locations" into one class "rental location".
- Merged "request" into "reservation"; merged "rented out" into the "available" attribute; merged "honored" into "voided" state; merged "preventive maintenance" into the "maintenance" value.
- Removed "rental fleet", "reservation form", "options", "block reservation", "period of time", "depreciation of the rental cars", channel adjectives ("in person", "through the phone") and "opened"/"satisfy"/"show up" as redundant, non-stored, or software/narrative detail.
- Confirmed "reservation" and "rental" each satisfy both association-class conditions (many-to-many customer/model and customer/car, plus own tracked state: voided/deposit/time, checked out/additional charge) — modeled as AC, not as plain C.
- Added a new class "car record" to hold the life-cycle values (purchase, repair, maintenance, disposal) since these values describe an object's own history, not the car itself.
- Verified every attribute has exactly one owning class and every association connects two classes/ACs listed in the model.
- Checked "make", "model", "price class" are not subclasses of each other (they differ by role, not by kind), so no inheritance rows are created — no "X is a Y" phrase was found in the text.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | car rental company | | |
| C | rental location | | |
| C | car | | |
| C | make | | |
| C | manufacturer | | |
| C | model | | |
| C | price class | | |
| C | customer | | |
| C | rental plan | | |
| C | salesperson | | |
| C | invoice | | |
| C | employer | | |
| C | credit card | | |
| C | credit card processing company | | |
| C | contract | | |
| C | damage | | |
| C | car record | | |
| A | additional charge | rental | |
| A | available | car | |
| A | gear change | model | |
| A | number of doors | model | |
| A | body type | model | |
| A | price | rental plan | |
| A | price | price class | |
| A | rental charge | invoice | |
| A | time | reservation | |
| A | deposit | reservation | |
| A | voided | reservation | |
| A | checked out | rental | |
| A | type | car record | |
| V | automatic | gear change |
| V | manual | gear change |
| V | two | number of doors |
| V | four | number of doors |
| V | sedan | body type |
| V | hatchback | body type |
| V | purchase | type |
| V | repair | type |
| V | maintenance | type |
| V | disposal | type |
| AS | operates | car rental company | rental location |
| AS | has | car rental company | make |
| AS | has | car rental company | rental plan |
| AS | has | make | model |
| AS | from | make | manufacturer |
| AS | grouped into | model | price class |
| AS | has | model | car |
| AS | select | customer | model |
| AS | rent | customer | car |
| AS | taken from | rental | rental location |
| AS | returned to | rental | rental location |
| AS | process | salesperson | reservation |
| AS | archive | salesperson | reservation |
| AS | sign | customer | contract |
| AS | cover | invoice | rental |
| AS | settle | customer | invoice |
| AS | sent to | invoice | employer |
| AS | pays by | customer | credit card |
| AS | processed through | invoice | credit card processing company |
| AS | repaired | damage | car |
| AS | has | car | car record |
| AC | reservation | customer | model |
| AC | rental | customer | car |