| label | element | arg1 | arg2 |
|---|---|---|---|
| C | TradeShow |  |  |
| C | BusinessCustomer |  |  |
| C | Service |  |  |
| C | Design |  |  |
| C | Theme |  |  |
| C | Slogan |  |  |
| C | Location |  |  |
| C | Duration |  |  |
| C | Advertisement |  |  |
| C | Activity |  |  |
| C | Speaker |  |  |
| C | Participant |  |  |
| C | Exhibitor |  |  |
| C | Registration |  |  |
| C | Booth |  |  |
| C | ConferenceRoom |  |  |
| C | Seminar |  |  |
| C | Reception |  |  |
| C | TradeShowMaterial |  |  |
| C | Account |  |  |
| C | ServiceCharge |  |  |
| C | Payment |  |  |
| C | AccountBalance |  |  |
| C | Event |  |  |
| C | Organizer |  |  |
| C | Person |  |  |
| C | Organization |  |  |
| C | ContactInformation |  |  |
| C | Website |  |  |
| C | Domain |  |  |
| C | Attendee |  |  |
| C | Staff |  |  |
| C | Proposal |  |  |
| C | Reviewer |  |  |
| C | Expert |  |  |
| C | Status |  |  |
| C | Product |  |  |
| C | Service |  |  |
| C | Observer |  |  |
| A | pendingReview | Status |  |
| A | accepted | Status |  |
| A | rejected | Status |  |
| A | large | BoothSize |  |
| A | medium | BoothSize |  |
| A | small | BoothSize |  |
| AS | hasAccount | BusinessCustomer | Account |
| AS | consistsOf | TradeShow | Activity |
| AS | contains | Event | Domain |
| AS | attend | Attendee | TradeShow |
| AS | register | Participant | TradeShow |
| AS | charge | TradeShow | RegistrationFee |
| AS | prepare | Staff | TradeShow |
| AS | invite | Staff | Speaker |
| AS | select | Staff | Speaker |
| AS | review | Reviewer | Proposal |
| AS | exhibit | Exhibitor | TradeShow |
| AS | pay | Exhibitor | Booth |
| AS | rent | Exhibitor | Booth |
| AS | visit | Observer | TradeShow |
| AC | TradeShow |  |  |
| AC | Event |  |  |



