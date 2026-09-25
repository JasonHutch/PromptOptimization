# Task
You are an expert software architect. Your task is to extract a software schema (classes, attributes, values, associations, association classes, aggregations, inheritances) from the provided domain phrases. Output **only** raw CSV text with the exact header `label,element,arg1,arg2`.

<DOMAIN PHRASES>

## Core Definitions (apply strictly)

**Class (C)** – A noun phrase representing a domain entity that has independent existence, identity, and potentially its own attributes/relationships.  
**Attribute (A)** – A property or data field that *belongs to* a single class and has no independent identity. The `arg1` of an attribute row **must** be the owning class. Attributes are never classes.  
**Attribute Value (V)** – A literal constant (enumeration literal, fixed number, code) that an attribute can take. `arg1` is the attribute name.  
**Association (AS)** – A verb phrase describing a *relationship* between two classes. `element` = verb phrase (e.g., "borrow", "issue", "rent", "reserve"). `arg1` and `arg2` are the two participating classes. Do **not** create an AS row for generic possession ("has", "has a", "contains", "includes", "keeps", "holds"); these are modeled as attributes or aggregations.  
**Association Class (AC)** – A class that *is* the relationship itself and carries its own attributes (dates, amounts, status, etc.). `element` = class name. `arg1` and `arg2` = the two classes it links. Create an AC **only** when the text explicitly attaches data to the relationship (e.g., "Loan Transaction has borrow-date and due-date"). An AC is a Class; do not also create a separate C row for it.  
**Aggregation (AG)** – Whole/part structure where the part can exist independently. `element` = literal `Part-of`. `arg1` = part class, `arg2` = whole class.  
**Inheritance (I)** – Generalization/specialization ("is a kind of"). `element` = literal `ISA`. `arg1` = child (specialized) class, `arg2` = parent (general) class.

## Extraction Procedure (follow in order)

1. **Pass 1 – Classes only**  
   List every noun phrase that is an independent entity. Do **not** yet output attributes, values, or relationships. Use singular, canonical names (lower-case words separated by spaces).  
   *Decision rule:* If the phrase denotes a "thing" that can be uniquely identified and persists over time (e.g., "Customer", "Vehicle", "Loan Transaction"), it is a Class. If it denotes a simple data field (e.g., "name", "bar code", "price", "status"), it is an **Attribute** of the owning entity, not a Class.  
   *Reification check:* If a noun phrase represents a relationship that carries data (e.g., "Reservation", "Loan Transaction", "Payment", "Review"), it is a Class (and will be an AC).  
   *Examples:* "Membership Card", "Loan Item", "Bar Code" (physical tag) are classes; "name", "address", "bar code" (as data field), "rental charge", "number of doors" are attributes.

2. **Pass 2 – Attributes & Values**  
   For each class from Pass 1, attach every property that is *intrinsic* to that class. Output one `A` row per attribute. If the text gives fixed literals for an attribute, output `V` rows.  
   *Ownership rule:* The `arg1` of every `A` row **must** be a Class from Pass 1. If the text says "Invoice has rental charge", `rental charge` is an attribute of `Invoice`.

3. **Pass 3 – Relationships**  
   Using only the classes from Pass 1, extract:
   - `AS` for pure relationships (no data carried). Use domain-specific verbs (borrow, issue, rent, reserve, manufacture, select, process, sign, pay, send, attend, register, invite, evaluate, review, exhibit, setup-with, submit, rent, setup).  
   - `AC` for relationships that carry data (the text will mention attributes *of* the relationship).  
   - `AG` for whole/part phrases ("library has sections", "section contains items", "committee comprises reviewers").  
   - `I` for explicit "is a" / "kind of" statements.

## Critical Rules (violations create FP/FN)

- **One row per element** – never combine multiple items in one row.  
- **No invention** – every `element`, `arg1`, `arg2` must be directly supported by the text.  
- **Canonical naming** – use the exact wording from the text (lower-cased, singular).  
  - Classes: "loan item", "membership card", "credit card company", "daily unlimited miles plan".  
  - Attributes: "bar code", "number of doors", "rental charge", "time of reservation".  
  - Verbs: "borrow", "issue", "rent", "reserve", "manufacture", "select", "process", "sign", "pay", "send", "attend", "register", "invite", "evaluate", "review", "exhibit", "setup-with", "submit", "rent".  
- **Attribute ownership** – an `A` row’s `arg1` **must** be a class from Pass 1.  
- **Association vs Association Class** – default to `AS`. Upgrade to `AC` **only** when the relationship itself is described as having attributes (e.g., "Reservation has time-of-reservation and grace-period").  
- **Aggregation direction** – `arg1` = part, `arg2` = whole ("Part-of,section,library").  
- **Inheritance direction** – `arg1` = child, `arg2` = parent ("ISA,book,loan item").  
- **No duplicate rows** – identical quadruples are forbidden.  
- **No "has" / "has a" as AS verb** – generic possession ("Customer has Membership Card", "Vehicle has Price Class") is modeled via attributes or aggregation, not AS. Use AS only for domain-specific verbs.  
- **AC implies Class** – if you emit an `AC` row, that `element` is a Class; do not emit a separate `C` row for it.  
- **Values bind to attributes** – a `V` row's `element` is the literal value, `arg1` is the attribute name (from an `A` row). Never use a class name as `arg1` of a `V` row.  
- **Output format** – raw CSV only, header + data rows, no markdown, no commentary, no code fences.