## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | business customers |
| 1 | trade shows |
| 1 | services |
| 1 | design |
| 1 | professional services |
| 1 | theme |
| 1 | slogan |
| 1 | location |
| 1 | duration |
| 1 | advertisement activities |
| 1 | creation |
| 1 | promotion |
| 1 | speakers |
| 1 | participants |
| 1 | exhibitors |
| 1 | on site registration |
| 1 | booths |
| 1 | conference rooms |
| 1 | seminars |
| 1 | reception |
| 1 | trade show materials |
| 1 | account |
| 1 | service charges |
| 1 | payments |
| 1 | account balances |
| 1 | event |
| 1 | organizer |
| 1 | person |
| 1 | organization |
| 1 | contact information |
| 1 | website |
| 1 | domains |
| 1 | NTSS staff |
| 1 | event organization staff |
| 1 | speakers (invited/selected) |
| 1 | observers |
| 1 | registration |
| 1 | fee |
| 1 | keynote address |
| 1 | proposals |
| 1 | committee of reviewers |
| 1 | reviewers |
| 1 | experts |
| 1 | products |
| 2 | selection of a theme |
| 2 | types of participants |
| 2 | evaluation of their proposals |
| 2 | committee of reviewers |
| 2 | status of a proposal |
| 2 | size of the booth |
| 2 | duration of the event |
| 3 | create |
| 3 | promote |
| 3 | organize |
| 3 | run |
| 3 | contact |
| 3 | invite |
| 3 | register |
| 3 | set up |
| 3 | distribute |
| 3 | record |
| 3 | maintain |
| 3 | belong to |
| 3 | added |
| 3 | removed |
| 3 | attend |
| 3 | charges |
| 3 | prepares |
| 3 | give |
| 3 | speak at |
| 3 | reviewed by |
| 3 | exhibit |
| 3 | pay for |
| 3 | requested |
| 3 | rented |
| 3 | visit |
| 3 | received |
| 4 | pending review |
| 4 | accepted |
| 4 | rejected |
| 4 | large |
| 4 | medium |
| 4 | small |
| 4 | invited |
| 4 | selected |
| 5 | one or more |
| 6 | has an organizer |
| 6 | has contact information |
| 9 | trade show can be regarded as an event |
| 9 | organizer can be a person or an organization |

## Step 2: Classification reasoning

business customers -> C : independent party commissioning services, "customer"
trade shows -> C : independently tracked deliverable, later ISA event
services -> excluded : too generic, covered by create/promote/organize/run verbs
design -> excluded : nominalization of "create", not a separate object
professional services -> excluded : generic, covered by attributes theme/slogan/location/duration
theme -> A : property of trade show, scalar string
slogan -> A : property of trade show, scalar string
location -> A : property of event (example venues)
duration -> A : property of event (example dates)
advertisement activities -> excluded : covered by verb "promote"
creation -> excluded : nominalization of "create"
promotion -> excluded : nominalization of "promote"
speakers -> C : independent participant role
participants -> C : superclass of speaker/exhibitor/observer/staff
exhibitors -> C : specific kind of participant, own noun -> subclass
on site registration -> excluded : example activity, no tracked attributes
booths -> C : rented physical object with size and fee
conference rooms -> excluded : example only, no further detail tracked
seminars -> excluded : example only
reception -> excluded : example only
trade show materials -> excluded : example only, object of unusable verb
account -> C : independent record with balance
service charges -> A : owned by account
payments -> A : owned by account
account balances -> A : owned by account, named "account balance"
event -> C : superclass, independent business object
organizer -> C : superclass role (person or organization)
person -> C : subclass of organizer via rule 9
organization -> C : subclass of organizer via rule 9
contact information -> A : property of event
website -> A : property of event
domains -> C : predefined list, related to event via "belong to"
NTSS staff -> C : specific kind of participant, own noun -> subclass
event organization staff -> merged with NTSS staff : same concept, first name used less than "NTSS staff"
speakers (invited/selected) -> kept as class "speaker" : general noun; invited/selected become adjective values
observers -> C : specific kind of participant, own noun -> subclass
registration -> excluded as class : no separate info besides participant/trade show link, modeled as AS "register"
fee -> A : property of trade show ("different for different trade show event")
keynote address -> excluded : not separately tracked, absorbed into AS "give"
proposals -> C : independently tracked object with status
committee of reviewers -> simplified to reviewers : committee not separately detailed
reviewers -> C : independent role reviewing proposals
experts -> merged with reviewers : same role described
products -> C : object exhibited by exhibitor
selection of a theme -> theme is A of trade show : X of Y attribute
types of participants -> realized as subclasses of participant : kind expressed as noun phrases
evaluation of their proposals -> realized via AS "review" (Reviewer, Proposal)
committee of reviewers -> see reviewers above
status of a proposal -> A "status" of proposal
size of the booth -> A "size" of booth
duration of the event -> A "duration" of event
create -> AS : Customer creates Trade Show
promote -> AS : Customer promotes Trade Show
organize -> AS : Customer organizes Trade Show
run -> AS : Customer runs Trade Show
contact -> excluded : object (NTSS as company) not modeled as class
invite -> AS : NTSS Staff invites Speaker
register -> AS : Participant registers for Trade Show
set up -> AS : NTSS Staff sets up Booth
distribute -> excluded : object (trade show materials) excluded
record -> AS : NTSS Staff records Account
maintain -> AS : NTSS Staff maintains Account
belong to -> AS : Event belongs to Domain
added -> excluded : lifecycle action on single class only, not an association
removed -> excluded : lifecycle action on single class only
attend -> AS : Participant attends Trade Show
charges -> absorbed into attribute "fee" of trade show
prepares -> AS : NTSS Staff prepares Event
give -> AS : Speaker gives Event (keynote)
speak at -> merged with "give" : same activity
reviewed by -> AS : Reviewer reviews Proposal
exhibit -> AS : Exhibitor exhibits Product
pay for -> AS : Exhibitor pays for Booth
requested -> AS : Exhibitor requests Booth
rented -> AS : Exhibitor rents Booth
visit -> excluded : trade show as object already covered by "attend"
received -> absorbed into attribute "payments" of account
pending review -> V : value of proposal status
accepted -> V : value of proposal status
rejected -> V : value of proposal status
large -> V : value of booth size
medium -> V : value of booth size
small -> V : value of booth size
invited -> V : value of speaker type attribute
selected -> V : value of speaker type attribute
one or more -> multiplicity : Event-Domain association multiplicity
has an organizer -> AS "has" : Event, Organizer
has contact information -> absorbed into attribute "contact information" of event
trade show can be regarded as an event -> I : Trade Show ISA Event
organizer can be a person or an organization -> I : Person ISA Organizer, Organization ISA Organizer

## Step 3: Review

- Merged "event organization staff" into "NTSS staff" (same role, one name kept).
- Merged "experts" into "reviewers" (same concept described twice).
- Dropped "committee" as a separate class; reviewers modeled directly.
- Excluded generic/system phrases (services, design, professional services, on site registration, conference rooms, seminars, reception, trade show materials) — no attributes or relationships to justify classes, per "class with no attributes/relationships probably not needed."
- Excluded NTSS (the company) as a class since it represents the system/business itself, not a tracked domain object; "contact" and "distribute" verbs dropped because their object classes were excluded.
- Excluded "added"/"removed" for domain list maintenance — these are single-class lifecycle actions, not associations between two classes.
- Kept "invited"/"selected" as attribute values of a "speaker type" attribute (per rule 4), not subclasses, even though they have different follow-on activities — those activities (give, review) are still modeled as associations from the general Speaker/Proposal classes.
- Checked "register" (Participant–Trade Show) for association-class conditions: many-to-many is plausible, but no distinct information about a registration occurrence is stated (the fee belongs to the trade show, not to each registration) — kept as plain association, no AC.
- Checked "belong to" (Event–Domain) for association-class conditions: many-to-many but no extra information about the link itself — kept as plain association.
- Verified every attribute has exactly one owning class and every association connects two listed classes.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | business customer | | |
| C | trade show | | |
| C | event | | |
| C | organizer | | |
| C | person | | |
| C | organization | | |
| C | domain | | |
| C | account | | |
| C | participant | | |
| C | NTSS staff | | |
| C | speaker | | |
| C | exhibitor | | |
| C | observer | | |
| C | proposal | | |
| C | reviewer | | |
| C | product | | |
| C | booth | | |
| A | theme | trade show | |
| A | slogan | trade show | |
| A | fee | trade show | |
| A | location | event | |
| A | duration | event | |
| A | contact information | event | |
| A | website | event | |
| A | service charges | account | |
| A | payments | account | |
| A | account balance | account | |
| A | speaker type | speaker | |
| A | status | proposal | |
| A | size | booth | |
| V | invited | speaker type | |
| V | selected | speaker type | |
| V | pending review | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| I | ISA | trade show | event |
| I | ISA | person | organizer |
| I | ISA | organization | organizer |
| I | ISA | NTSS staff | participant |
| I | ISA | speaker | participant |
| I | ISA | exhibitor | participant |
| I | ISA | observer | participant |
| AS | has | event | organizer |
| AS | belong to | event | domain |
| AS | has | business customer | account |
| AS | create | business customer | trade show |
| AS | promote | business customer | trade show |
| AS | organize | business customer | trade show |
| AS | run | business customer | trade show |
| AS | attend | participant | trade show |
| AS | register | participant | trade show |
| AS | invite | NTSS staff | speaker |
| AS | give | speaker | event |
| AS | review | reviewer | proposal |
| AS | exhibit | exhibitor | product |
| AS | request | exhibitor | booth |
| AS | rent | exhibitor | booth |
| AS | pay for | exhibitor | booth |
| AS | record | NTSS staff | account |
| AS | maintain | NTSS staff | account |
| AS | prepare | NTSS staff | event |
| AS | set up | NTSS staff | booth |