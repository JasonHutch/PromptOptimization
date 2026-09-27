| label | element | arg1 | arg2 |
|---|---|---|---|
| C | NTSS | | |
| C | BusinessCustomer | | |
| C | TradeShow | | |
| C | Event | | |
| C | Design | | |
| C | Account | | |
| C | Person | | |
| C | Organization | | |
| C | Domain | | |
| C | Participant | | |
| C | NTSSStaff | | |
| C | Speaker | | |
| C | InvitedSpeaker | | |
| C | SelectedSpeaker | | |
| C | Exhibitor | | |
| C | Observer | | |
| C | Booth | | |
| C | ConferenceRoom | | |
| C | Seminar | | |
| C | Reception | | |
| C | TradeShowMaterial | | |
| C | Proposal | | |
| C | Committee | | |
| C | Reviewer | | |
| AC | Registration | Participant | TradeShow |
| A | theme | Design | |
| A | slogan | Design | |
| A | location | Event | |
| A | duration | Event | |
| A | advertisement | TradeShow | |
| A | contactInformation | Event | |
| A | website | Event | |
| A | serviceCharges | Account | |
| A | paymentsReceived | Account | |
| A | balance | Account | |
| A | fee | Registration | |
| A | keynoteAddress | InvitedSpeaker | |
| A | evaluation | Proposal | |
| A | status | Proposal | |
| A | size | Booth | |
| A | scope | TradeShow | |
| V | national | scope | |
| V | international | scope | |
| V | pending | status | |
| V | accepted | status | |
| V | rejected | status | |
| V | large | size | |
| V | medium | size | |
| V | small | size | |
| I | ISA | TradeShow | Event |
| I | ISA | NTSSStaff | Participant |
| I | ISA | Speaker | Participant |
| I | ISA | Exhibitor | Participant |
| I | ISA | Observer | Participant |
| I | ISA | InvitedSpeaker | Speaker |
| I | ISA | SelectedSpeaker | Speaker |
| AG | Part-of | Design | TradeShow |
| AG | Part-of | ConferenceRoom | TradeShow |
| AG | Part-of | Seminar | TradeShow |
| AG | Part-of | Reception | TradeShow |
| AG | Part-of | TradeShowMaterial | TradeShow |
| AG | Part-of | Reviewer | Committee |
| AS | create | NTSS | TradeShow |
| AS | promote | NTSS | TradeShow |
| AS | organize | NTSS | TradeShow |
| AS | run | NTSS | TradeShow |
| AS | contact | BusinessCustomer | NTSS |
| AS | invite | NTSS | Speaker |
| AS | register | Participant | TradeShow |
| AS | setUp | NTSSStaff | Booth |
| AS | setUp | NTSSStaff | ConferenceRoom |
| AS | distribute | NTSSStaff | TradeShowMaterial |
| AS | have | BusinessCustomer | Account |
| AS | record | NTSS | Account |
| AS | belongTo | Event | Domain |
| AS | add | NTSS | Domain |
| AS | remove | NTSS | Domain |
| AS | attend | Participant | TradeShow |
| AS | prepare | NTSSStaff | Event |
| AS | give | InvitedSpeaker | Event |
| AS | review | Reviewer | Proposal |
| AS | exhibit | Exhibitor | TradeShow |
| AS | pay | Exhibitor | Booth |
| AS | request | Exhibitor | Booth |
| AS | rent | Exhibitor | Booth |
| AS | visit | Observer | TradeShow |
| AS | organize | Person | Event |
| AS | organize | Organization | Event |