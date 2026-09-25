# Task
You are an expert software architect. Your task is to extract a software schema (classes, attributes, values, associations, association classes, aggregations, inheritances) from the provided domain phrases. Output **only** raw CSV text with the exact header `label,element,arg1,arg2`.

<DOMAIN PHRASES>

## Core Definitions (apply strictly)

**Class (C)** – A noun phrase representing a domain entity that has independent existence, identity, and potentially its own attributes/relationships. Use singular, canonical names (lower-case words separated by spaces).  
**Attribute (A)** – A property or data field that *belongs to* a single class and has no independent identity. The `arg1` of an attribute row **must** be the owning class (a Class from Pass 1). Attributes are never classes.  
**Attribute Value (V)** – A literal constant (enumeration literal, fixed number, code) that an attribute can take. `element` = the literal value. `arg1` = the attribute name (from an `A` row).  
**Association (AS)** – A verb phrase describing a *relationship* between two classes. `element` = domain-specific verb phrase from the approved list below. `arg1` and `arg2` = the two participating classes. **Do not** create an AS row for generic possession ("has", "has a", "contains", "includes", "keeps", "holds", "comprises", "consists of", "have"); these are modeled as attributes or aggregations.  
**Association Class (AC)** – A class that *is* the relationship itself and carries its own attributes (dates, amounts, status, etc.). `element` = class name (from Pass 1). `arg1` and `arg2` = the two classes it links. Create an AC **only** when the text explicitly attaches data to the relationship (e.g., "Loan Transaction has borrow-date and due-date", "Reservation has time-of-reservation and grace-period"). An AC is a Class; do **not** also create a separate C row for it.  
**Aggregation (AG)** – Whole/part structure where the part can exist independently. `element` = literal `Part-of`. `arg1` = part class, `arg2` = whole class.  
**Inheritance (I)** – Generalization/specialization ("is a kind of"). `element` = literal `ISA`. `arg1` = child (specialized) class, `arg2` = parent (general) class.

## Approved Association Verbs (use EXACTLY these spellings)
borrow, issue, rent, reserve, manufacture, select, process, sign, pay, send, attend, register, invite, evaluate, review, exhibit, setup-with, submit, take from, return to, bill for, check out, open, cover, check, archive, promote, organize, run, contact, create, record, regard, belong to, add, remove, prepare, give, comprise, request, setup, receive, visit, taken from, returned to, sent to, processed by, reviewed-by, has

## Extraction Procedure (follow in order)

### Pass 1 – Classes only
List every noun phrase that is an independent entity. Do **not** yet output attributes, values, or relationships.  
*Decision rule:* If the phrase denotes a "thing" that can be uniquely identified and persists over time (e.g., "Customer", "Vehicle", "Loan Transaction", "Section"), it is a Class.  
*Reification check:* If a noun phrase represents a relationship that carries data (e.g., "Reservation", "Loan Transaction", "Payment", "Review", "Registration", "Pay by Credit Card", "Block Reservation", "Contract", "Invoice"), it is a Class (and will be an AC).  
*Exclusion rule:* Do **not** create classes for noun phrases that appear **only** as property holders or roles without independent relationships or attributes of their own (e.g., "Manufacturer", "Price Class", "Rental Price", "Organizer" when it only holds properties, "Domain", "Account" when they only hold properties for another entity, "Service Provider", "Venue", "Conference Room", "Keynote Address", "Trade Show Material", "Observer", "Staff", "Service Charges", "Payments Received", "Account Balances", "Contact Information", "Website", "Fee", "Size", "Price", "Evaluation", "Type", "Grace Period", "Means", "Void", "Opened", "Balance", "Charges", "Payment", "Slogan", "Theme", "Duration", "Location", "Product", "Proposal", "Reviewer", "Review Committee", "Seminar", "Booth", "Invited Speaker", "Participant", "Exhibitor").  
*Attribute-like nouns (never classes):* manufacturer, make, model, price class, price, rental price, rental charge, depreciation, theme, slogan, duration, contact information, website, service charges, payments received, account balances, fee, size, evaluation, status, keynote address, type, grace period, means, void, opened, balance, charges, payment, conference room, subject, language, level, number of doors, transmission, body style, additional charge, id, bar code, title, author, number of subject sections, number of items, loan period, membership status, maximum loan items, loan items constraint.  
*Examples:* "Membership Card", "Loan Item", "Bar Code" (physical tag), "Section", "Loan Transaction", "Reservation", "Payment", "Contract", "Invoice", "Block Reservation", "Registration", "Review" are classes; "name", "address", "bar code" (as data field), "rental charge", "number of doors" are attributes.

### Pass 2 – Attributes & Values
For each class from Pass 1, attach every property that is *intrinsic* to that class. Output one `A` row per attribute. If the text gives fixed literals for an attribute, output `V` rows.  
*Ownership rule:* The `arg1` of every `A` row **must** be a Class from Pass 1. If the text says "Invoice has rental charge", `rental charge` is an attribute of `invoice`.  
*Attribute-like nouns:* Treat the listed attribute-like nouns as attributes, not classes.

### Pass 3 – Relationships
Using only the classes from Pass 1, extract:
- `AS` for pure relationships (no data carried). Use domain-specific verbs from the approved list.
- `AC` for relationships that carry data (the text mentions attributes *of* the relationship). The AC `element` name is the reified class from Pass 1.
- `AG` for whole/part phrases ("library has sections", "section contains items", "committee comprises reviewers", "block reservation includes reservations", "event has organizer", "customer has account"). `element` = literal `Part-of`. `arg1` = part class, `arg2` = whole class.
- `I` for explicit "is a" / "kind of" statements.

## Critical Rules (violations create FP/FN)

- **One row per element** – never combine multiple items in one row.  
- **No invention** – every `element`, `arg1`, `arg2` must be directly supported by the text.  
- **Canonical naming** – use the exact wording from the text (lower-cased, singular).  
  - Classes: "loan item", "membership card", "credit card company", "daily unlimited miles plan", "loan transaction", "rental plan", "weekend savings plan", "rental transaction", "payment", "pay by credit card", "registration", "review", "seminar", "booth", "trade show", "event", "customer", "account", "organizer", "participant", "exhibitor", "observer", "speaker", "proposal", "committee", "reviewer", "domain", "trade show material", "conference room", "section", "library", "book", "language tape", "vehicle", "passenger car", "location", "reservation", "contract", "block reservation", "invoice", "company", "salesperson", "reservation form", "file cabinet".  
  - Attributes: "bar code", "number of doors", "rental charge", "time of reservation", "grace period", "means", "void", "opened", "charges", "payment", "balance", "fee", "size", "theme", "slogan", "location", "duration", "contact information", "website", "evaluation", "status", "keynote address", "type", "price class", "price", "manufacturer", "make", "model", "transmission", "body style", "additional charge", "depreciation", "id", "title", "author", "subject", "language", "level", "number of subject sections", "number of items", "loan period", "membership status", "maximum loan items", "loan items constraint".  
  - Verbs: use ONLY the approved association verbs list above.  
- **Attribute ownership** – an `A` row's `arg1` **must** be a class from Pass 1.  
- **Association vs Association Class** – default to `AS`. Upgrade to `AC` **only** when the relationship itself is described as having attributes (e.g., "Reservation has time-of-reservation and grace-period").  
- **Aggregation direction** – `arg1` = part, `arg2` = whole ("Part-of,section,library").  
- **Inheritance direction** – `arg1` = child, `arg2` = parent ("ISA,book,loan item").  
- **No duplicate rows** – identical quadruples are forbidden.  
- **Generic possession** – "has", "has a", "have" are modeled via `AG` (Part-of) or attributes, never as `AS` unless "has" appears in the approved verbs list for a specific domain context (e.g., "Customer has Membership Card" → AG or A).  
- **AC implies Class** – if you emit an `AC` row, that `element` is a Class; do not emit a separate `C` row for it.  
- **Values bind to attributes** – a `V` row's `element` is the literal value, `arg1` is the attribute name (from an `A` row). Never use a class name as `arg1` of a `V` row.  
- **Attribute-only entities** – if a noun phrase appears only as a property holder with no independent relationships (e.g., "Manufacturer", "Price Class", "Rental Price", "Organizer", "Domain", "Account" in certain contexts), model it as an `A` row under its owner, not a `C` row.  
- **Output format** – raw CSV only, header + data rows, no markdown, no commentary, no code fences.