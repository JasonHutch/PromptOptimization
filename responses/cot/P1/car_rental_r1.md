## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | vehicle |
| 1 | location |
| 1 | passenger car |
| 1 | vehicle rental |
| 1 | make |
| 1 | car |
| 1 | rental fleet |
| 1 | manufacturer |
| 1 | model |
| 1 | price class |
| 1 | customer |
| 1 | rental plan |
| 1 | gear change |
| 1 | door |
| 1 | rental price |
| 1 | reservation |
| 1 | salesperson |
| 1 | deposit |
| 1 | contract |
| 1 | block reservation |
| 1 | invoice |
| 1 | rental |
| 1 | company |
| 1 | credit card |
| 1 | rental charge |
| 1 | credit card processing company |
| 1 | maintenance |
| 1 | damage |
| 1 | purchase |
| 1 | repair |
| 1 | disposal |
| 1 | depreciation |
| 2 | make of car |
| 2 | model of car |
| 2 | time of reservation |
| 2 | period of time |
| 2 | depreciation of rental cars |
| 3 | taken from |
| 3 | returned to |
| 3 | select |
| 3 | rent |
| 3 | grouped into |
| 3 | reserve |
| 3 | make (a reservation) |
| 3 | void |
| 3 | sign |
| 3 | honor |
| 3 | check out |
| 3 | open |
| 3 | cover |
| 3 | settle |
| 3 | return |
| 3 | sent to |
| 3 | pay by |
| 3 | process through |
| 3 | repair (verb) |
| 3 | keep track of |
| 3 | process (reservations) |
| 3 | archive |
| 4 | available |
| 4 | rented out |
| 4 | automatic |
| 4 | manual |
| 4 | two |
| 4 | four |
| 4 | sedan |
| 4 | hatchback |
| 4 | in person |
| 4 | through the phone |
| 4 | voided |
| 4 | checked out |
| 4 | purchase (life-cycle step) |
| 4 | repair (life-cycle step) |
| 4 | maintenance (life-cycle step) |
| 4 | disposal (life-cycle step) |
| 5 | several |
| 5 | small number of |
| 5 | a number of |
| 5 | more than |
| 5 | one |
| 5 | more (one or more) |
| 6 | has several different makes of cars |
| 6 | has several models |
| 6 | has a number of different rental plans |

## Step 2: Classification reasoning

vehicle -> C : independent concept, superclass, future vehicle types possible
location -> C : place where cars are taken/returned, independent object
passenger car -> renamed car : same concept as "car" used throughout, one class
vehicle rental -> excluded : background/future-scope narrative, not an operating concept
make -> C : identifiable manufacturer brand, has models
car -> C, ISA vehicle : car is a kind of vehicle (future other vehicle types)
rental fleet -> excluded : synonym for the set of cars, not a separate object
manufacturer -> A of make : simple descriptive property, no own behavior
model -> C : identifiable product line, has own attributes
price class -> C : groups models, referenced independently
customer -> C : independent role, party to many associations
rental plan -> C : identifiable offering with own identity
gear change -> A of model : property with two enumerated values
door -> A "number of doors" of model : property with two enumerated values
rental price -> excluded : depends on plan/model combination, not separately modeled attribute
reservation -> C : document/record created and tracked
salesperson -> C : role performing "process" action
deposit -> excluded : not required, no data to store per description
contract -> C : signed document, independent record
block reservation -> C, ISA reservation : specific kind of reservation named by noun
invoice -> C : billing document opened per checkout
rental -> AC (customer, car) : many-to-many, occurrence info (location, invoice) kept
company -> C : recipient of invoice (e.g. employer)
credit card -> C : payment instrument, independently identified
rental charge -> A of invoice : monetary amount of an invoice
credit card processing company -> C : external party processing payment
maintenance -> V of type, owner car record : life-cycle step recorded for car
damage -> merged into repair : trigger for repair, not separate stored concept
purchase -> V of type, owner car record : life-cycle step recorded for car
repair -> V of type, owner car record : life-cycle step recorded for car
disposal -> V of type, owner car record : life-cycle step recorded for car
depreciation -> A of car : property tracked for tax purposes
make of car -> AS "of" (car, make) : car belongs to a specific make/model
model of car -> AS "of" (car, model) : car is an instance of a model
time of reservation -> A "time" of reservation : timestamp property of reservation
period of time -> excluded : threshold constant for business rule, not stored data
depreciation of rental cars -> A depreciation of car : same as above
taken from -> AS "taken from" (rental, location) : pickup location of a rental occurrence
returned to -> AS "returned to" (rental, location) : return location of a rental occurrence
select -> AS "select" (customer, model) : customer chooses a model
rent -> merged into rental AC : same act represented by rental association class
grouped into -> AS "grouped into" (model, price class) : models classified into price classes
reserve -> AS "reserve" (reservation, car) : reservation holds a car
make (a reservation) -> AS "make" (customer, reservation) : customer creates reservation
void -> A "voided" boolean of reservation : true/false state of reservation
sign -> AS "sign" (customer, contract) : customer signs contract
honor -> excluded : business rule outcome, not stored data
check out -> merged into rental AC : checkout creates the rental occurrence
open -> merged into AG invoice-rental : opening invoice links it to rental
cover -> AG Part-of (rental, invoice) : invoice composed of one or more rentals
settle -> AS "settle" (customer, invoice) : customer pays off invoice
return -> merged into "returned to" : same action already modeled
sent to -> AS "sent to" (invoice, company) : invoice mailed to employer/company
pay by -> AS "pay by" (customer, credit card) : payment method used
process through -> AS "processed through" (invoice, credit card processing company)
repair (verb) -> merged into car record type : action matches life-cycle value
keep track of -> excluded : paraphrased by car record class, generic capability
process (reservations) -> AS "process" (salesperson, reservation) : salesperson handles reservation
archive -> excluded : implementation detail of manual filing, not domain rule
available -> V of availability, owner car : one of two states of a car
rented out -> V of availability, owner car : opposite state of available
automatic -> V of gear change, owner model
manual -> V of gear change, owner model
two -> V of number of doors, owner model
four -> V of number of doors, owner model
sedan -> V of body style, owner model
hatchback -> V of body style, owner model
in person -> excluded : channel of legacy manual process, not tracked state
through the phone -> excluded : channel of legacy manual process, not tracked state
voided -> A "voided" of reservation : already captured above
checked out -> merged into rental AC : state represented by rental occurrence existing
purchase (life-cycle) -> V of type, owner car record
repair (life-cycle) -> V of type, owner car record
maintenance (life-cycle) -> V of type, owner car record
disposal (life-cycle) -> V of type, owner car record
several -> multiplicity : expressed on make-model, not separate row
small number of -> multiplicity : expressed on model-price class, not separate row
a number of -> multiplicity : expressed on rental plan-customer, not separate row
more than -> multiplicity : expresses reservation void threshold, business rule only
one -> multiplicity : minimum rentals per invoice
more (one or more) -> multiplicity : rentals per invoice upper bound
has several different makes of cars -> AS "has" (make, model) : reframed as make-model ownership
has several models -> AS "has" (make, model) : duplicate of above, one association
has a number of different rental plans -> AS "available to" (rental plan, customer) : plans offered to customers

## Step 3: Review

- Merged "passenger car", "car" into a single class **car**; removed "rental fleet" and "vehicle rental" as non-operational narrative.
- Removed **deposit** (explicitly not required, no data kept) and **option** concept (folded into model attributes: gear change, doors, body style are the "options" referenced later).
- Combined "rent", "check out" and "open (invoice)" into a single association class **rental** (customer–car), since renting is many-to-many and occurrence data (location, invoice link) must be kept.
- Converted purchase/repair/maintenance/disposal into a single class **car record** with an enumerated `type` attribute, instead of four separate classes, matching the "life-cycle steps" pattern; merged **damage** into this concept.
- Removed **manufacturer** and **company** and **rental price**/**option** as standalone classes where they reduced to attributes or were unsupported by relationships; kept manufacturer as an attribute of make.
- Removed channel phrases ("in person", "through the phone"), "honor", "archive", "keep track of" as business-rule/implementation narrative, not stored domain data.
- Verified every association connects two classes/AC present in the model; no class is used as an attribute type; every class has at least one attribute or relationship.
- Confirmed **rental** (customer↔car) qualifies as an association class (many-to-many + occurrence data: location, invoice) and **block reservation** qualifies as a subclass (specific named kind), not an attribute value.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | location | | |
| C | vehicle | | |
| C | car | | |
| I | ISA | car | vehicle |
| C | make | | |
| A | manufacturer | make | |
| C | model | | |
| A | gear change | model | |
| V | automatic | gear change | |
| V | manual | gear change | |
| A | number of doors | model | |
| V | two | number of doors | |
| V | four | number of doors | |
| A | body style | model | |
| V | sedan | body style | |
| V | hatchback | body style | |
| A | availability | car | |
| V | available | availability | |
| V | rented out | availability | |
| A | depreciation | car | |
| C | price class | | |
| C | customer | | |
| C | rental plan | | |
| C | reservation | | |
| A | time | reservation | |
| A | voided | reservation | |
| C | block reservation | | |
| I | ISA | block reservation | reservation |
| C | salesperson | | |
| C | contract | | |
| C | invoice | | |
| A | rental charge | invoice | |
| AC | rental | customer | car |
| C | company | | |
| C | credit card | | |
| C | credit card processing company | | |
| C | car record | | |
| A | type | car record | |
| V | purchase | type | |
| V | repair | type | |
| V | maintenance | type | |
| V | disposal | type | |
| AS | of | car | model |
| AS | has | make | model |
| AS | grouped into | model | price class |
| AS | select | customer | model |
| AS | make | customer | reservation |
| AS | reserve | reservation | car |
| AS | available to | rental plan | customer |
| AS | sign | customer | contract |
| AS | process | salesperson | reservation |
| AS | settle | customer | invoice |
| AS | sent to | invoice | company |
| AS | pay by | customer | credit card |
| AS | processed through | invoice | credit card processing company |
| AS | taken from | rental | location |
| AS | returned to | rental | location |
| AS | of | car record | car |
| AG | Part-of | rental | invoice |