# Task
You are an expert software architect. Your task is to extract a software schema (classes, attributes, values, associations, association classes, aggregations, inheritances) from the provided domain phrases. Output **only** raw CSV text with the exact header `label,element,arg1,arg2`.

<DOMAIN PHRASES>

## Core Definitions (apply strictly)

**Class (C)** – A noun phrase representing a domain entity that has independent existence, identity, and potentially its own attributes/relationships.  
**Attribute (A)** – A property or data field that *belongs to* a single class and has no independent identity. The `arg1` of an attribute row **must** be the owning class. Attributes are never classes.  
**Attribute Value (V)** – A literal constant (enumeration literal, fixed number, code) that an attribute can take. `arg1` is the attribute name.  
**Association (AS)** – A verb phrase describing a *relationship* between two classes. `element` = verb phrase (e.g., "borrow", "issue", "rent", "reserve"). `arg1` and `arg2` are the two participating classes. Do **not** create an AS row for generic possession ("has", "has a", "contains", "includes", "keeps", "holds", "comprises", "consists of"); these are modeled as attributes or aggregations.  
**Association Class (AC)** – A class that *is* the relationship itself and carries its own attributes (dates, amounts, status, etc.). `element` = class name. `arg1` and `arg2` = the two classes it links. Create an AC **only** when the text explicitly attaches data to the relationship (e.g., "Loan Transaction has borrow-date and due-date"). An AC is a Class; do not also create a separate C row for it.  
**Aggregation (AG)** – Whole/part structure where the part can exist independently. `element` = literal `Part-of`. `arg1` = part class, `arg2` = whole class.  
**Inheritance (I)** – Generalization/specialization ("is a kind of"). `element` = literal `ISA`. `arg1` = child (specialized) class, `arg2` = parent (general) class.

## Extraction Procedure (follow in order)

1. **Pass 1 – Classes only**  
   List every noun phrase that is an independent entity. Do **not** yet output attributes, values, or relationships. Use singular, canonical names (lower-case words separated by spaces).  
   *Decision rule:* If the phrase denotes a "thing" that can be uniquely identified and persists over time (e.g., "Customer", "Vehicle", "Loan Transaction"), it is a Class. If it denotes a simple data field (e.g., "name", "bar code", "price", "status"), it is an **Attribute** of the owning entity, not a Class.  
   *Reification check:* If a noun phrase represents a relationship that carries data (e.g., "Reservation", "Loan Transaction", "Payment", "Review"), it is a Class (and will be an AC).  
   *Critical exclusion:* Do **not** create classes for "Manufacturer", "Price Class", "Rental Price", "Organizer", "Domain", "Account", "Service Provider", "Venue", "Conference Room", "Keynote Address", "Trade Show Material", "Observer", "Staff", "Service Charges", "Payments Received", "Account Balances", "Contact Information", "Website", "Fee", "Size", "Price", "Evaluation", "Type", "Grace Period", "Means", "Void", "Opened", "Balance", "Charges", "Payment", "Slogan", "Theme", "Duration", "Location", "Evaluation", "Product", "Proposal", "Reviewer", "Review Committee", "Seminar", "Booth", "Invited Speaker", "Participant", "Exhibitor", "Domain", "Organizer" when they appear only as property holders or roles without independent relationships.  
   *Examples:* "Membership Card", "Loan Item", "Bar Code" (physical tag) are classes; "name", "address", "bar code" (as data field), "rental charge", "number of doors" are attributes.

2. **Pass 2 – Attributes & Values**  
   For each class from Pass 1, attach every property that is *intrinsic* to that class. Output one `A` row per attribute. If the text gives fixed literals for an attribute, output `V` rows.  
   *Ownership rule:* The `arg1` of every `A` row **must** be a Class from Pass 1. If the text says "Invoice has rental charge", `rental charge` is an attribute of `Invoice`.  
   *Attribute-like nouns:* Treat the following as attributes, not classes: manufacturer, make, model, price class, price, rental price, rental charge, depreciation, theme, slogan, duration, contact information, website, service charges, payments received, account balances, fee, size, evaluation, status, keynote address, type, grace period, means, void, opened, balance, charges, payment, conference room, subject, language, level, number of doors, transmission, body style, additional charge, id, bar code, title, author, number of subject sections, number of items, loan period, membership status, maximum loan items, loan items constraint.

3. **Pass 3 – Relationships**  
   Using only the classes from Pass 1, extract:
   - `AS` for pure relationships (no data carried). Use domain-specific verbs (borrow, issue, rent, reserve, manufacture, select, process, sign, pay, send, attend, register, invite, evaluate, review, exhibit, setup-with, submit, take from, return to, bill for, check out, open, cover, check, archive, promote, organize, run, contact, create, record, regard, belong to, add, remove, prepare, give, select, comprise, request, setup, receive, visit).  
   - `AC` for relationships that carry data (the text will mention attributes *of* the relationship). The AC element name is the reified class from Pass 1.  
   - `AG` for whole/part phrases ("library has sections", "section contains items", "committee comprises reviewers", "block reservation includes reservations"). `element` = literal `Part-of`. `arg1` = part class, `arg2` = whole class.  
   - `I` for explicit "is a" / "kind of" statements.

## Critical Rules (violations create FP/FN)

- **One row per element** – never combine multiple items in one row.  
- **No invention** – every `element`, `arg1`, `arg2` must be directly supported by the text.  
- **Canonical naming** – use the exact wording from the text (lower-cased, singular).  
  - Classes: "loan item", "membership card", "credit card company", "daily unlimited miles plan", "loan transaction", "rental plan", "daily unlimited miles plan", "weekend savings plan", "rental transaction", "payment", "pay by credit card", "credit card company", "registration", "review", "seminar", "booth", "trade show", "event", "customer", "account", "organizer", "participant", "exhibitor", "observer", "speaker", "proposal", "committee", "reviewer", "domain", "trade show material", "conference room".  
  - Attributes: "bar code", "number of doors", "rental charge", "time of reservation", "grace period", "means", "void", "opened", "charges", "payment", "balance", "fee", "size", "theme", "slogan", "location", "duration", "contact information", "website", "evaluation", "status", "keynote address", "type", "price class", "price", "manufacturer", "make", "model", "transmission", "body style", "additional charge", "depreciation", "id", "title", "author", "subject", "language", "level", "number of subject sections", "number of items", "loan period", "membership status", "maximum loan items", "loan items constraint".  
  - Verbs: "borrow", "issue", "rent", "reserve", "manufacture", "select", "process", "sign", "pay", "send", "attend", "register", "invite", "evaluate", "review", "exhibit", "setup-with", "submit", "take from", "return to", "bill for", "check out", "open", "cover", "check", "archive", "promote", "organize", "run", "contact", "create", "record", "regard", "belong to", "add", "remove", "prepare", "give", "comprise", "request", "setup", "receive", "visit".  
- **Attribute ownership** – an `A` row's `arg1` **must** be a class from Pass 1.  
- **Association vs Association Class** – default to `AS`. Upgrade to `AC` **only** when the relationship itself is described as having attributes (e.g., "Reservation has time-of-reservation and grace-period").  
- **Aggregation direction** – `arg1` = part, `arg2` = whole ("Part-of,section,library").  
- **Inheritance direction** – `arg1` = child, `arg2` = parent ("ISA,book,loan item").  
- **No duplicate rows** – identical quadruples are forbidden.  
- **No "has" / "has a" as AS verb** – generic possession ("Customer has Membership Card", "Vehicle has Price Class", "Event has Organizer", "Customer has Account") is modeled via attributes or aggregation, not AS. Use AS only for domain-specific verbs.  
- **AC implies Class** – if you emit an `AC` row, that `element` is a Class; do not emit a separate `C` row for it.  
- **Values bind to attributes** – a `V` row's `element` is the literal value, `arg1` is the attribute name (from an `A` row). Never use a class name as `arg1` of a `V` row.  
- **Attribute-only entities** – if a noun phrase appears only as a property holder with no independent relationships (e.g., "Manufacturer", "Price Class", "Rental Price", "Organizer", "Domain", "Account" in certain contexts), model it as an `A` row under its owner, not a `C` row.  
- **Output format** – raw CSV only, header + data rows, no markdown, no commentary, no code fences.