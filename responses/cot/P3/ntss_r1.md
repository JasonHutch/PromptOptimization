## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | business customers |
| 1 | trade shows |
| 1 | services |
| 1 | design |
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
| 1 | booths |
| 1 | conference rooms |
| 1 | seminars |
| 1 | reception |
| 1 | trade show materials |
| 1 | on site registration |
| 1 | account |
| 1 | service charges |
| 1 | payments |
| 1 | account balances |
| 1 | organizer |
| 1 | contact information |
| 1 | website |
| 1 | predefined domains |
| 1 | event organization staff |
| 1 | invited speakers |
| 1 | selected speakers |
| 1 | observers |
| 1 | NTSS staff |
| 1 | registration |
| 1 | fee |
| 1 | keynote address |
| 1 | evaluation |
| 1 | proposals |
| 1 | committee |
| 1 | reviewers |
| 1 | products |
| 1 | event |
| 2 | selection of a theme |
| 2 | evaluation of their proposals |
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
| 3 | receive |
| 3 | belong to |
| 3 | add |
| 3 | remove |
| 3 | attend |
| 3 | charge |
| 3 | prepare |
| 3 | give |
| 3 | speak at |
| 3 | review |
| 3 | exhibit |
| 3 | pay for |
| 3 | request |
| 3 | rent |
| 3 | visit |
| 3 | organized by |
| 4 | new |
| 4 | outdated |
| 4 | person |
| 4 | organization |
| 4 | pending review |
| 4 | accepted |
| 4 | rejected |
| 4 | large |
| 4 | medium |
| 4 | small |
| 5 | one or more |
| 6 | has an organizer |
| 6 | has contact information and possibly a website |
| 9 | a trade show can be regarded as an event |
| 9 | event organization staff, invited speakers, selected speakers, exhibitors and observers are types of participants |

## Step 2: Classification reasoning

business customers -> C Customer : independently existing party tracked by an account
trade shows -> C TradeShow : independently existing thing, later shown as Event subclass
services -> dropped : generic term, covered by create/promote/organize/run verbs
design -> dropped : not scalar, captured by theme/slogan/location/duration attributes
theme -> A of TradeShow : scalar descriptive property chosen for the show
slogan -> A of TradeShow : scalar descriptive property chosen for the show
location -> A of TradeShow : scalar property of the show
duration -> A of TradeShow : scalar property of the show
advertisement activities -> dropped : no further tracked detail, covered by verb promote
creation -> dropped : nominalization of verb create, already captured
promotion -> dropped : nominalization of verb promote, already captured
speakers -> superclass Participant subtype, split into invited/selected below
participants -> C Participant : superclass for all attendee kinds
exhibitors -> C Exhibitor : ISA Participant, has own rules (booth rental)
booths -> C Booth : independently existing rented object
conference rooms -> dropped : no attributes/relations given
seminars -> dropped : no attributes/relations given
reception -> dropped : no attributes/relations given
trade show materials -> dropped : no attributes/relations given
on site registration -> dropped : narrative activity, not tracked entity
account -> C Account : independently existing record per customer
service charges -> A of Account : scalar monetary amount
payments -> A of Account : scalar monetary amount
account balances -> A of Account : scalar monetary amount
organizer -> C Organizer : independently existing person/organization
contact information -> A of Event : scalar descriptive property
website -> A of Event : scalar descriptive property
predefined domains -> C Domain : independently existing, added/removed over time
event organization staff -> C NTSS staff : ISA Participant, runs the event
invited speakers -> C InvitedSpeaker : ISA Participant, own rule (keynote by fame)
selected speakers -> C SelectedSpeaker : ISA Participant, own rule (proposal evaluation)
observers -> C Observer : ISA Participant, no extra detail but distinct kind
NTSS staff -> C NTSS staff : ISA Participant (see above)
registration -> AC Registration : occurrence of many-to-many attend relationship
fee -> A of Registration : scalar amount charged per registration
keynote address -> A of InvitedSpeaker : scalar topic property
evaluation -> dropped : process captured by review association
proposals -> C Proposal : independently existing document with status
committee -> C Committee : whole made up of reviewers
reviewers -> C Reviewer : independently existing expert entity
products -> dropped : no further tracked attributes/relations
event -> C Event : superclass, has organizer/contact info/domains
selection of a theme -> A theme of TradeShow : attribute, already captured
evaluation of their proposals -> AS has : SelectedSpeaker has Proposal
status of a proposal -> A status of Proposal : scalar attribute
size of the booth -> A size of Booth : scalar attribute
duration of the event -> A duration of TradeShow : already captured
create -> AS creates : NTSS staff creates Event
promote -> AS promotes : NTSS staff promotes Event
organize -> AS organizes : NTSS staff organizes Event
run -> AS runs : NTSS staff runs Event
contact -> dropped : company itself not modeled as singleton class
invite -> dropped : captured by subclass naming (invited/selected speaker)
register -> AS registers : Participant registers Event, becomes AC
set up -> dropped : narrative detail of running, no tracked entity
distribute -> dropped : narrative detail of running, no tracked entity
record -> dropped : generic bookkeeping verb, captured by Account attributes
maintain -> dropped : generic bookkeeping verb, captured by Account attributes
receive -> dropped : captured by Account payments attribute
belong to -> AS belongs to : Event belongs to Domain
add -> AS adds : NTSS staff adds Domain
remove -> AS removes : NTSS staff removes Domain
attend -> merged with register : same participation relationship
charge -> merged into Registration fee attribute
prepare -> AS prepares : NTSS staff prepares Event
give -> merged into keynote address attribute : action produces attribute value
speak at -> dropped : covered by SelectedSpeaker participation
review -> AS reviews : Reviewer reviews Proposal
exhibit -> dropped : no tracked object, products not a class
pay for -> merged into rents : booth payment tied to rental
request -> merged into rents : booth request/rental treated as one association
rent -> AS rents : Exhibitor rents Booth
visit -> dropped : same as observer participation, covered by register
organized by -> merged into has : Event has Organizer
new -> dropped : transient descriptor before add, not stored state
outdated -> dropped : transient descriptor before remove, not stored state
person -> V of Organizer.type : enumerated value of organizer kind
organization -> V of Organizer.type : enumerated value of organizer kind
pending review -> V of Proposal.status : enumerated status value
accepted -> V of Proposal.status : enumerated status value
rejected -> V of Proposal.status : enumerated status value
large -> V of Booth.size : enumerated size value
medium -> V of Booth.size : enumerated size value
small -> V of Booth.size : enumerated size value
one or more -> dropped : multiplicity, no dedicated column in final table
has an organizer -> AS has : Event has Organizer
has contact information and possibly a website -> merged into Event attributes contact information, website
a trade show can be regarded as an event -> I : TradeShow ISA Event
event organization staff, invited speakers, selected speakers, exhibitors and observers are types of participants -> I rows : each ISA Participant

## Step 3: Review

- Dropped "Committee of reviewers" as an X-of-Y noun phrase but kept it as an aggregation (Reviewer part-of Committee), matching the "team of players" pattern.
- Merged create/organize/promote/run/prepare all under NTSS staff as subject, avoiding a redundant NTSS company class (single instance, not otherwise related).
- Confirmed Registration qualifies as an association class: many-to-many (participant attends many events, event has many participants) and it carries its own attribute (fee).
- Verified Organizer, Proposal, Booth, Domain, Committee, Reviewer, Account all have at least one attribute or relationship, so they are kept as classes.
- Removed classes with no attributes/relationships (conference rooms, seminars, reception, trade show materials, on-site registration, products, design, selection, evaluation).
- Confirmed person/organization and size values (large/medium/small) and status values are enumerations (V), not subclasses, since no extra attributes/rules are attached to them individually.
- Confirmed every I row's subclass has its own rule (staff runs event, invited speaker gives keynote by fame, selected speaker has proposal, exhibitor rents booth) satisfying the subclass test; Observer kept as subclass since it is explicitly listed as a distinct participant type even without extra rules, to preserve the participant taxonomy given in the text.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Account | | |
| C | Event | | |
| C | TradeShow | | |
| C | Organizer | | |
| C | Domain | | |
| C | Participant | | |
| C | NTSS staff | | |
| C | InvitedSpeaker | | |
| C | SelectedSpeaker | | |
| C | Exhibitor | | |
| C | Observer | | |
| C | Proposal | | |
| C | Reviewer | | |
| C | Committee | | |
| C | Booth | | |
| A | service charges | Account | |
| A | payments | Account | |
| A | account balance | Account | |
| A | contact information | Event | |
| A | website | Event | |
| A | theme | TradeShow | |
| A | slogan | TradeShow | |
| A | location | TradeShow | |
| A | duration | TradeShow | |
| A | type | Organizer | |
| A | status | Proposal | |
| A | size | Booth | |
| A | keynote address | InvitedSpeaker | |
| A | fee | Registration | |
| V | person | type | |
| V | organization | type | |
| V | pending review | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| AS | has | Customer | Account |
| AS | has | Event | Organizer |
| AS | belongs to | Event | Domain |
| AS | adds | NTSS staff | Domain |
| AS | removes | NTSS staff | Domain |
| AS | creates | NTSS staff | Event |
| AS | promotes | NTSS staff | Event |
| AS | organizes | NTSS staff | Event |
| AS | runs | NTSS staff | Event |
| AS | prepares | NTSS staff | Event |
| AS | registers | Participant | Event |
| AS | has | SelectedSpeaker | Proposal |
| AS | reviews | Reviewer | Proposal |
| AS | rents | Exhibitor | Booth |
| AC | Registration | Participant | Event |
| AG | Part-of | Reviewer | Committee |
| I | ISA | TradeShow | Event |
| I | ISA | NTSS staff | Participant |
| I | ISA | InvitedSpeaker | Participant |
| I | ISA | SelectedSpeaker | Participant |
| I | ISA | Exhibitor | Participant |
| I | ISA | Observer | Participant |