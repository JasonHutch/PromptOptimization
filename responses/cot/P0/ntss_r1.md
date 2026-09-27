## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | NTSS |
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
| 1 | booths |
| 1 | conference rooms |
| 1 | seminars |
| 1 | reception |
| 1 | trade show materials |
| 1 | account |
| 1 | service charges |
| 1 | payments received |
| 1 | account balances |
| 1 | event |
| 1 | organizer |
| 1 | person |
| 1 | organization |
| 1 | contact information |
| 1 | website |
| 1 | domains |
| 1 | participants |
| 1 | NTSS staff |
| 1 | invited speakers |
| 1 | selected speakers |
| 1 | exhibitors |
| 1 | observers |
| 1 | registration |
| 1 | fee |
| 1 | keynote address |
| 1 | proposals |
| 1 | committee |
| 1 | reviewers |
| 1 | status |
| 1 | products or services |
| 1 | booth |
| 1 | size |
| 2 | selection of a theme |
| 2 | list of predefined domains |
| 2 | evaluation of their proposals |
| 2 | committee of reviewers |
| 2 | status of a proposal |
| 2 | size of the booth |
| 2 | duration of the event |
| 3 | create (a trade show) |
| 3 | promote |
| 3 | organize |
| 3 | run |
| 3 | contact |
| 3 | creates an account |
| 3 | inviting (speakers) |
| 3 | registering (participants and exhibitors) |
| 3 | took place in |
| 3 | belong to |
| 3 | is attended by |
| 3 | must register (to attend) |
| 3 | organized by |
| 3 | creates, prepares and runs |
| 3 | invited to give a keynote address |
| 3 | invited to speak |
| 3 | reviewed by |
| 3 | exhibit |
| 3 | pay for |
| 3 | requested |
| 3 | rented |
| 3 | visit |
| 4 | national, international |
| 4 | pending review, accepted, rejected |
| 4 | large, medium, small |
| 4 | Technology, Consumer Electronics |
| 5 | one or more (domains) |
| 6 | has an organizer |
| 6 | has contact information |
| 6 | has ... a website |
| 6 | have to pay for the booths |
| 9 | can be regarded as an event |
| 9 | can be a person or an organization |

## Step 2: Classification reasoning

NTSS -> C : service provider organization, independent entity
service provider -> discard : generic role, redundant with NTSS
business customers -> C : Customer, independent entity tracked with account
trade shows -> C : TradeShow, central independent entity
services -> discard : too generic, covered by association verbs
design -> discard : abstracted into TradeShow attributes below
professional services -> discard : too generic
theme -> A : attribute of TradeShow
slogan -> A : attribute of TradeShow
location -> A : attribute of TradeShow/Event
duration -> A : attribute of TradeShow/Event
advertisement activities -> discard : not tracked as data
booths -> C : Booth, independently requested/rented
conference rooms -> discard : detail of "running", not tracked separately
seminars -> discard : detail, not a tracked entity
reception -> discard : detail, not tracked
trade show materials -> discard : not tracked as data
account -> C : Account, independent entity with balance
service charges -> A : attribute of Account
payments received -> A : attribute of Account
account balances -> A : attribute of Account
event -> C : Event, superclass of TradeShow
organizer -> C : role class, subclassed by Person/Organization
person -> C : subclass of Organizer
organization -> C : subclass of Organizer
contact information -> A : attribute of Event
website -> A : attribute of Event
domains -> C : Domain, dynamic list of predefined values
participants -> C : Participant, superclass
NTSS staff -> C : subclass of Participant
invited speakers -> C : subclass of Participant
selected speakers -> C : subclass of Participant
exhibitors -> C : subclass of Participant
observers -> C : subclass of Participant
registration -> AC : association class between Participant and TradeShow
fee -> A : attribute of Registration
keynote address -> A : attribute of InvitedSpeaker
proposals -> C : Proposal, independent entity with status
committee -> C : Committee, aggregates Reviewers
reviewers -> C : Reviewer, subclass-like role, independent entity
status -> A : attribute of Proposal
products or services -> A : attribute of Exhibitor
booth -> C : duplicate of Booth
size -> A : attribute of Booth
selection of a theme -> A : theme is attribute of TradeShow (X of Y)
list of predefined domains -> AS : Event belongs to Domain relationship
evaluation of their proposals -> AS : Reviewer reviews Proposal
committee of reviewers -> AG : Reviewer part-of Committee
status of a proposal -> A : status attribute of Proposal
size of the booth -> A : size attribute of Booth
duration of the event -> A : duration attribute of Event
create (a trade show) -> AS : merged into NTSS manages TradeShow
promote -> AS : merged into NTSS manages TradeShow
organize -> AS : merged into NTSS manages TradeShow
run -> AS : merged into NTSS manages TradeShow
contact -> AS : Customer contacts NTSS
creates an account -> AS : NTSS creates Account
inviting (speakers) -> discard : covered by ISA InvitedSpeaker/SelectedSpeaker
registering (participants and exhibitors) -> AC : covered by Registration
took place in -> A : merged into location attribute
belong to -> AS : Event belongs to Domain
is attended by -> AC : covered by Registration (attends)
must register (to attend) -> AC : covered by Registration
organized by -> AS : Event has Organizer
creates, prepares and runs -> AS : NTSSStaff runs TradeShow
invited to give a keynote address -> A : keynoteAddress attribute
invited to speak -> AS : SelectedSpeaker submits Proposal (implied speaking role)
reviewed by -> AS : Reviewer reviews Proposal
exhibit -> A : merged into productsOrServices attribute
pay for -> AS : Exhibitor rents Booth
requested -> AS : merged into Exhibitor rents Booth
rented -> AS : merged into Exhibitor rents Booth / Booth used at TradeShow
visit -> AC : covered by Registration (Observer attends)
national, international -> V : values of Event attribute type
pending review, accepted, rejected -> V : values of Proposal attribute status
large, medium, small -> V : values of Booth attribute size
Technology, Consumer Electronics -> discard : example instances of Domain, not fixed enum since list changes
one or more (domains) -> multiplicity : Event-Domain association cardinality
has an organizer -> AS : Event has Organizer
has contact information -> A : contactInformation attribute of Event
has ... a website -> A : website attribute of Event
have to pay for the booths -> AS : Exhibitor rents Booth
can be regarded as an event -> I : TradeShow ISA Event
can be a person or an organization -> I : Person ISA Organizer, Organization ISA Organizer

## Step 3: Review

- Merged "create/promote/organize/run" verbs into a single association NTSS–TradeShow ("manages") to avoid four redundant associations.
- Dropped generic/non-tracked nouns (service provider, services, design, professional services, advertisement activities, conference rooms, seminars, reception, trade show materials) as they add no attributes/relationships.
- Merged "is attended by / must register / visit" into the single Registration association class (many-to-many Participant↔TradeShow with fee attribute).
- Treated Technology/Consumer Electronics as example instances of class Domain rather than fixed attribute values, since the domain list is explicitly dynamic.
- Confirmed Registration qualifies as an association class: many-to-many (participant attends many trade shows; trade show has many participants) and carries its own data (fee).
- Verified every attribute has exactly one owning class and no class is used as an attribute type.
- Confirmed all ISA subclasses (TradeShow, Person, Organization, NTSSStaff, InvitedSpeaker, SelectedSpeaker, Exhibitor, Observer) satisfy the IS-A test.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | NTSS | | |
| C | Customer | | |
| C | Account | | |
| C | Event | | |
| C | TradeShow | | |
| C | Organizer | | |
| C | Person | | |
| C | Organization | | |
| C | Domain | | |
| C | Participant | | |
| C | NTSSStaff | | |
| C | InvitedSpeaker | | |
| C | SelectedSpeaker | | |
| C | Exhibitor | | |
| C | Observer | | |
| C | Proposal | | |
| C | Reviewer | | |
| C | Committee | | |
| C | Booth | | |
| A | serviceCharges | Account | |
| A | paymentsReceived | Account | |
| A | accountBalance | Account | |
| A | theme | TradeShow | |
| A | slogan | TradeShow | |
| A | location | Event | |
| A | duration | Event | |
| A | contactInformation | Event | |
| A | website | Event | |
| A | type | Event | |
| A | fee | Registration | |
| A | keynoteAddress | InvitedSpeaker | |
| A | status | Proposal | |
| A | productsOrServices | Exhibitor | |
| A | size | Booth | |
| V | national | type | |
| V | international | type | |
| V | pending review | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| I | ISA | TradeShow | Event |
| I | ISA | Person | Organizer |
| I | ISA | Organization | Organizer |
| I | ISA | NTSSStaff | Participant |
| I | ISA | InvitedSpeaker | Participant |
| I | ISA | SelectedSpeaker | Participant |
| I | ISA | Exhibitor | Participant |
| I | ISA | Observer | Participant |
| AS | contacts | Customer | NTSS |
| AS | creates | NTSS | Account |
| AS | has | Customer | Account |
| AS | manages | NTSS | TradeShow |
| AS | has | Event | Organizer |
| AS | belongs to | Event | Domain |
| AS | runs | NTSSStaff | TradeShow |
| AS | submits | SelectedSpeaker | Proposal |
| AS | reviews | Reviewer | Proposal |
| AS | rents | Exhibitor | Booth |
| AS | rented for | Booth | TradeShow |
| AC | Registration | Participant | TradeShow |
| AG | Part-of | Reviewer | Committee |