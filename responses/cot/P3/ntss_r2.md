## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | business customers |
| 1 | trade shows |
| 1 | design |
| 1 | professional services |
| 1 | selection |
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
| 1 | invited speakers |
| 1 | selected speakers |
| 1 | observers |
| 1 | registration |
| 1 | fee |
| 1 | keynote address |
| 1 | proposals |
| 1 | evaluation |
| 1 | committee |
| 1 | reviewers |
| 1 | status |
| 1 | products |
| 1 | on site registration |
| 2 | selection of a theme |
| 2 | evaluation of proposals |
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
| 3 | attended by |
| 3 | charges |
| 3 | prepares |
| 3 | give |
| 3 | speak |
| 3 | reviewed by |
| 3 | exhibit |
| 3 | pay for |
| 3 | requested |
| 3 | rented |
| 3 | visit |
| 3 | organized by |
| 4 | pending review |
| 4 | accepted |
| 4 | rejected |
| 4 | large |
| 4 | medium |
| 4 | small |
| 5 | one or more |
| 6 | event has an organizer |
| 6 | event has contact information and possibly a website |
| 9 | trade show is regarded as an event |
| 9 | organizer can be a person or an organization |
| 9 | event organization staff, invited speakers, selected speakers, exhibitors, and observers are types of participants |

## Step 2: Classification reasoning

business customers -> C Customer : independent business entity tracked with account
trade shows -> C Trade show : independent entity, later isa event
design -> not modeled : narrative describing creation, no own attributes
professional services -> not modeled : narrative describing creation activity
selection -> not modeled : part of narrative, not tracked separately
theme -> A Trade show : scalar property from design of trade show
slogan -> A Trade show : scalar property from design of trade show
location -> A Event : scalar property, shown by CES/MacWorld examples
duration -> A Event : scalar property, shown by CES/MacWorld examples
advertisement activities -> not modeled : narrative describing promotion
creation -> not modeled : names a service activity, no own data
promotion -> not modeled : names a service activity, no own data
speakers -> not modeled : generic term, refined into invited/selected speaker
participants -> C Participant : superclass of trade show attendee roles
exhibitors -> C Exhibitor : role with own booth relationship
booths -> C Booth : independently tracked, rented, sized
conference rooms -> not modeled : activity detail of running, no data kept
seminars -> not modeled : activity detail of running, no data kept
reception -> not modeled : activity detail of running, no data kept
trade show materials -> not modeled : activity detail of running, no data kept
account -> C Account : independent record of charges/payments
service charges -> A Account : scalar value recorded on account
payments -> A Account : scalar value recorded on account
account balances -> A Account : scalar balance maintained on account
event -> C Event : independent entity with organizer, dates, domain
organizer -> C Organizer : role class, specialized into person/organization
person -> C Person : subclass of organizer
organization -> C Organization : subclass of organizer
contact information -> A Event : scalar property of event
website -> A Event : scalar property of event
domains -> C Domain : independently maintained list of predefined domains
NTSS staff -> C NTSS staff : subclass of participant, runs event
invited speakers -> C Invited speaker : subclass of participant
selected speakers -> C Selected speaker : subclass of participant
observers -> C Observer : subclass of participant
registration -> not modeled : nominalization, fee attached to trade show instead
fee -> A Trade show : registration fee differs per trade show event
keynote address -> not modeled : no scalar attribute or tracked relation given
proposals -> C Proposal : independently tracked with status, reviewed
evaluation -> not modeled : subsumed into review association
committee -> C Committee : independent group of reviewers
reviewers -> C Reviewer : independent role, part of committee
status -> A Proposal : scalar property of proposal
products -> not modeled : exhibited items, no tracked data
on site registration -> not modeled : running-activity detail, no data kept
selection of a theme -> A Trade show : attribute already captured as theme
evaluation of proposals -> AS review : reviewers evaluate/review proposals
status of a proposal -> A Proposal : attribute status owned by proposal
size of the booth -> A Booth : attribute size owned by booth
duration of the event -> A Event : attribute duration owned by event
create -> AS create : NTSS staff create event
promote -> not modeled : part of unmodeled service narrative
organize -> AS organize : organizer organizes event
run -> AS run : NTSS staff run event
contact -> not modeled : NTSS not a domain class
invite -> not modeled : subsumed in invited speaker/selected speaker roles
register -> AS register : participant registers for trade show
set up -> not modeled : running-activity detail
distribute -> not modeled : running-activity detail
record -> not modeled : implied bookkeeping on account, no new class
maintain -> not modeled : implied bookkeeping on account, no new class
belong to -> AS belong to : event belongs to domain
added -> not modeled : list-maintenance narrative, no attribute
removed -> not modeled : list-maintenance narrative, no attribute
attend -> AS attend : participant attends trade show
attended by -> AS attend : same as attend, one row
charges -> not modeled : fee already modeled as attribute
prepares -> AS prepare : NTSS staff prepare event
give -> not modeled : keynote address not modeled as class
speak -> AS speak : selected speaker speaks at trade show
reviewed by -> AS review : proposal reviewed by reviewer
exhibit -> AS exhibit : exhibitor exhibits at trade show
pay for -> AS pay for : exhibitor pays for booth
requested -> not modeled : covered by rent association
rented -> AS rent : exhibitor rents booth
visit -> AS visit : observer visits trade show
organized by -> AS organize : same as organize, one row
pending review -> V Proposal.status : enumerated status value
accepted -> V Proposal.status : enumerated status value
rejected -> V Proposal.status : enumerated status value
large -> V Booth.size : enumerated size value
medium -> V Booth.size : enumerated size value
small -> V Booth.size : enumerated size value
one or more -> multiplicity : constrains event-domain association, not separate row
event has an organizer -> AS organize : possession expresses organizer relation
event has contact information and possibly a website -> A Event : attributes contact information, website
trade show is regarded as an event -> I Trade show isa Event
organizer can be a person or an organization -> I Person isa Organizer; I Organization isa Organizer
event organization staff... are types of participants -> I NTSS staff, Invited speaker, Selected speaker, Exhibitor, Observer isa Participant

## Step 3: Review

- Excluded NTSS as a class (singleton service-provider/system, not a tracked domain object); its staff role kept as "NTSS staff".
- Merged "attended by" into "attend" and "organized by" into "organize" (same association, different voice).
- Dropped narrative-only phrases with no attributes or relationships (design, selection, professional services, advertisement activities, creation, promotion, conference rooms, seminars, reception, trade show materials, on site registration, keynote address, products, registration) per "class/attribute with no data" rule.
- Moved "fee" to Trade show (not Event) since the text ties fee variance specifically to "different trade show event".
- Checked Reviewer–Proposal and Event–Domain associations against association-class conditions: neither needs extra relationship-specific data, so no association class created.
- Added AG for Reviewer part-of Committee (committee is a group whose members are reviewer objects).
- Verified every I row: Trade show/Event, Person/Organizer, Organization/Organizer, and the five participant subclasses each carry distinct relationships (organize, exhibit, review-target, rent, visit, speak), so kept as subclasses rather than attribute values.
- Confirmed every attribute has exactly one owning class and every association connects only classes listed as C.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Account | | |
| C | Trade show | | |
| C | Event | | |
| C | Organizer | | |
| C | Person | | |
| C | Organization | | |
| C | Domain | | |
| C | Participant | | |
| C | NTSS staff | | |
| C | Invited speaker | | |
| C | Selected speaker | | |
| C | Exhibitor | | |
| C | Observer | | |
| C | Proposal | | |
| C | Reviewer | | |
| C | Committee | | |
| C | Booth | | |
| A | service charges | Account | |
| A | payments | Account | |
| A | balance | Account | |
| A | theme | Trade show | |
| A | slogan | Trade show | |
| A | fee | Trade show | |
| A | location | Event | |
| A | duration | Event | |
| A | contact information | Event | |
| A | website | Event | |
| A | status | Proposal | |
| A | size | Booth | |
| V | pending review | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| AS | has | Customer | Account |
| AS | organize | Organizer | Event |
| AS | belong to | Event | Domain |
| AS | create | NTSS staff | Event |
| AS | prepare | NTSS staff | Event |
| AS | run | NTSS staff | Event |
| AS | register | Participant | Trade show |
| AS | attend | Participant | Trade show |
| AS | review | Reviewer | Proposal |
| AS | pay for | Exhibitor | Booth |
| AS | rent | Exhibitor | Booth |
| AS | visit | Observer | Trade show |
| AS | speak | Selected speaker | Trade show |
| AS | exhibit | Exhibitor | Trade show |
| AG | Part-of | Reviewer | Committee |
| I | ISA | Trade show | Event |
| I | ISA | Person | Organizer |
| I | ISA | Organization | Organizer |
| I | ISA | NTSS staff | Participant |
| I | ISA | Invited speaker | Participant |
| I | ISA | Selected speaker | Participant |
| I | ISA | Exhibitor | Participant |
| I | ISA | Observer | Participant |