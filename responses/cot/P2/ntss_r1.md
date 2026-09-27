## Step 1: Domain-specific phrases

| rule | phrase |
|---|---|
| 1 | business customer |
| 1 | trade show |
| 1 | service |
| 1 | design |
| 1 | theme |
| 1 | slogan |
| 1 | location |
| 1 | duration |
| 1 | advertisement |
| 1 | creation |
| 1 | promotion |
| 1 | speaker |
| 1 | participant |
| 1 | exhibitor |
| 1 | booth |
| 1 | conference room |
| 1 | seminar |
| 1 | reception |
| 1 | trade show materials |
| 1 | account |
| 1 | service charge |
| 1 | payment |
| 1 | account balance |
| 1 | event |
| 1 | organizer |
| 1 | person |
| 1 | organization |
| 1 | contact information |
| 1 | website |
| 1 | domain |
| 1 | event organization staff |
| 1 | invited speaker |
| 1 | selected speaker |
| 1 | observer |
| 1 | registration |
| 1 | fee |
| 1 | keynote address |
| 1 | proposal |
| 1 | evaluation |
| 1 | committee |
| 1 | reviewer |
| 1 | expert |
| 1 | status |
| 1 | product |
| 1 | size |
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
| 3 | belong to |
| 3 | add |
| 3 | remove |
| 3 | attended by |
| 3 | charge |
| 3 | prepare |
| 3 | give |
| 3 | speak |
| 3 | reviewed by |
| 3 | exhibit |
| 3 | pay for |
| 3 | request |
| 3 | rent |
| 3 | visit |
| 4 | pending review |
| 4 | accepted |
| 4 | rejected |
| 4 | large |
| 4 | medium |
| 4 | small |
| 5 | one or more |
| 6 | has an organizer |
| 6 | has contact information |
| 6 | has website |
| 9 | a trade show can be regarded as an event |
| 9 | organizer can be a person or an organization |

## Step 2: Classification reasoning

business customer -> class : independent business entity, tracked with account
trade show -> class : central independent business entity
service -> attribute value / dropped : too generic, replaced by specific service types (create/promote/organize/run)
design -> class : professional service activity tracked for trade show
theme -> attribute : property chosen as part of design
slogan -> attribute : property chosen as part of design
location -> attribute : property of event (also duration/venue)
duration -> attribute : property of event, "of the event"
advertisement -> class : promotion activity tracked for trade show
creation -> class : named phase/service of trade show
promotion -> class : named phase/service of trade show
speaker -> class : participant role with own attributes/rules
participant -> class : general role attending trade show
exhibitor -> class : participant kind with own attributes (booth, products)
booth -> class : rented object with size and fee
conference room -> attribute/dropped : minor detail of running activity, no own attributes; drop
seminar -> attribute/dropped : detail of running activity; drop
reception -> attribute/dropped : detail of running activity; drop
trade show materials -> attribute/dropped : detail of running activity; drop
account -> class : independent object recording charges/payments
service charge -> attribute : property of account
payment -> attribute : property of account
account balance -> attribute : property of account
event -> class : trade show is-a event, general concept
organizer -> association role : link between event and person/organization
person -> class : possible organizer type
organization -> class : possible organizer type
contact information -> attribute : property of event
website -> attribute : property of event
domain -> class : predefined domain list managed as entities
event organization staff -> class : subtype of participant (NTSS staff)
invited speaker -> class : subtype of speaker with own rule (keynote)
selected speaker -> class : subtype of speaker with own rule (proposal evaluation)
observer -> class : subtype of participant
registration -> class : occurrence of participant registering to event, has fee
fee -> attribute : property of registration
keynote address -> attribute/dropped : minor detail, not tracked separately; drop
proposal -> class : independent object reviewed with status
evaluation -> attribute/dropped : "evaluation of proposals" -> becomes review action, not separate class
committee -> class : group of reviewers assigned to review
reviewer -> class : person reviewing proposals
expert -> attribute/dropped : descriptive of reviewer, not separate concept
status -> attribute : property of proposal
product -> attribute/dropped : minor detail exhibited, not tracked with own attributes; drop
size -> attribute : property of booth
selection of a theme -> attribute : theme is attribute of design
evaluation of their proposals -> association : review relates committee/reviewer to proposal
status of a proposal -> attribute : status attribute of proposal
size of the booth -> attribute : size attribute of booth
duration of the event -> attribute : duration attribute of event
create -> association : NTSS creates trade show
promote -> association : NTSS promotes trade show
organize -> association : NTSS organizes trade show
run -> association : NTSS runs trade show / event
contact -> association : business customer contacts NTSS
invite -> association : NTSS staff invites speaker
register -> association : participant registers for trade show (registration)
set up -> attribute/dropped : detail of run activity, not separate association needed
distribute -> attribute/dropped : detail of run activity
record -> association : account records service charge/payment
maintain -> association : NTSS maintains account balance
belong to -> association : event belongs to domain
add -> attribute/dropped : lifecycle detail of domain list, not modeled as association
remove -> attribute/dropped : lifecycle detail of domain list, not modeled as association
attended by -> association : trade show attended by participant
charge -> association : registration charges fee (captured as attribute fee)
prepare -> association : NTSS staff prepares event
give -> association : invited speaker gives keynote address
speak -> association : selected speaker speaks at event
reviewed by -> association : proposal reviewed by committee/reviewer
exhibit -> association : exhibitor exhibits at trade show (implicit in exhibitor role)
pay for -> association : exhibitor pays for booth
request -> association : exhibitor requests booth
rent -> association : exhibitor rents booth
visit -> association : observer visits trade show
pending review -> attribute value : status value of proposal
accepted -> attribute value : status value of proposal
rejected -> attribute value : status value of proposal
large -> attribute value : size value of booth
medium -> attribute value : size value of booth
small -> attribute value : size value of booth
one or more -> multiplicity : event-domain relationship multiplicity
has an organizer -> association : event has organizer (person/organization)
has contact information -> attribute : contact information attribute of event
has website -> attribute : website attribute of event
a trade show can be regarded as an event -> inheritance : trade show ISA event
organizer can be a person or an organization -> association note : organizer role filled by person or organization (modeled as association, not subclass)

## Step 3: Review

- Dropped "conference room", "seminar", "reception", "trade show materials", "keynote address", "product", "expert", "evaluation" (as class) since they have no independent attributes/relationships beyond narrative detail.
- Dropped "add"/"remove" domain and "set up"/"distribute" as separate associations; these are narrative process detail not modeled as relationships.
- Merged "creation", "promotion", "organize", "run" phases: kept as classes only where they carry distinct attributes (design); promotion/organization/running collapsed into associations between NTSS and trade show rather than separate empty classes — removed "promotion", "creation" as classes (no attributes), kept as association verbs (promote/organize).
- "service" (generic) dropped; NTSS's four activities represented as associations (create, promote, organize, run) between customer/NTSS and trade show, not as classes.
- "organizer" modeled as association role between Event and Person/Organization (not itself a class) since it has no separate attributes.
- Checked create/register associations: registration is many-to-many-like occurrence with its own attribute (fee) and status implicitly tied to participant+event → kept as association class Registration(Participant, Event) with attribute fee.
- Checked review association: many proposals reviewed by many reviewers/committee, with status kept on proposal not on association, so no association class needed; kept as plain association (reviewed by).
- Verified invited speaker / selected speaker / exhibitor / observer / event organization staff are legitimate subclasses of participant, each with own rules (keynote invite, proposal evaluation, booth rental, visit).
- Verified booth request/rental: many exhibitors rent many booths over event duration; no additional info about the occurrence itself beyond size/fee already on Booth, so no association class, kept as plain association.
- Ensured every attribute belongs to exactly one class (theme, slogan under Design; duration, location, contact information, website under Event; size, fee under Booth/Registration; status under Proposal).
- Confirmed trade show ISA event passes IS-A and conformance tests.

## Final domain model

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | business customer | | |
| C | trade show | | |
| C | design | | |
| C | event | | |
| C | person | | |
| C | organization | | |
| C | domain | | |
| C | account | | |
| C | participant | | |
| C | event organization staff | | |
| C | speaker | | |
| C | invited speaker | | |
| C | selected speaker | | |
| C | exhibitor | | |
| C | observer | | |
| C | booth | | |
| C | proposal | | |
| C | committee | | |
| C | reviewer | | |
| A | theme | design | |
| A | slogan | design | |
| A | duration | event | |
| A | location | event | |
| A | contact information | event | |
| A | website | event | |
| A | service charge | account | |
| A | payment | account | |
| A | account balance | account | |
| A | size | booth | |
| A | fee | booth | |
| A | status | proposal | |
| V | pending review | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| I | ISA | trade show | event |
| I | ISA | event organization staff | participant |
| I | ISA | speaker | participant |
| I | ISA | invited speaker | speaker |
| I | ISA | selected speaker | speaker |
| I | ISA | exhibitor | participant |
| I | ISA | observer | participant |
| AS | contact | business customer | NTSS |
| AS | create | business customer | design |
| AS | promote | business customer | trade show |
| AS | organize | business customer | trade show |
| AS | run | event organization staff | event |
| AS | has | business customer | account |
| AS | maintain | account | business customer |
| AS | has an organizer | event | person |
| AS | has an organizer | event | organization |
| AS | belong to | event | domain |
| AS | attended by | trade show | participant |
| AS | register | participant | trade show |
| AC | registration | participant | trade show |
| A | fee | registration | |
| AS | prepare | event organization staff | event |
| AS | give | invited speaker | event |
| AS | speak | selected speaker | event |
| AS | reviewed by | proposal | reviewer |
| AS | reviewed by | proposal | committee |
| AS | pay for | exhibitor | booth |
| AS | request | exhibitor | booth |
| AS | rent | exhibitor | booth |
| AS | visit | observer | trade show |