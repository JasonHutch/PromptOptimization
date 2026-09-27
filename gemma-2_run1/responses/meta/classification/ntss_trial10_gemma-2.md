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
| A | balance |  |  |
| C | Event |  |  |
| C | Organizer |  |  |
| C | Person |  |  |
| C | Organization |  |  |
| C | ContactInformation |  |  |
| C | Website |  |  |
| C | Domain |  |  |
| C | Attendee |  |  |
| C | Staff |  |  |
| C | KeynoteAddress |  |  |
| C | Proposal |  |  |
| C | Reviewer |  |  |
| A | status |  |  |
| C | Product |  |  |
| C | Service |  |  |
| C | Observer |  |  |
| AS | create | TradeShow | BusinessCustomer |
| AS | promote | TradeShow | BusinessCustomer |
| AS | organize | TradeShow | BusinessCustomer |
| AS | run | TradeShow | BusinessCustomer |
| AS | attend | Event | Attendee |
| AS | register | Event | Attendee |
| AS | charge | Registration | Attendee |
| AS | pay | Exhibitor | Booth |
| AS | invite | Speaker | TradeShow |
| AS | select | Speaker | TradeShow |
| AS | review | Proposal | Reviewer |
| AS | exhibit | Exhibitor | TradeShow |
| AS | visit | Observer | TradeShow |
| AG | has | TradeShow | Speaker |
| AG | has | TradeShow | Exhibitor |
| AG | has | TradeShow | Participant |
| AG | has | TradeShow | Observer |
| AC | Account |  |  |
| A | serviceCharges | Account |  |
| A | paymentsReceived | Account |  |
| A | balance | Account |  |
| AS | belong | Event | Domain |
| AC | Event |  |  |
| A | organizer | Event |  |
| A | contactInformation | Event |  |
| A | website | Event |  |



