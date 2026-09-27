# Classification — Optimized Prompt Submission

**Task:** Classification
---

## 1. Identification Methodology

Lang Graph workflow broken down into the following states
* Initial prompt
* classification task conducted against ntss, library, and car rental domains
* Each domain scored by calculating precision, recall, and F1
* Optimization node scans the prompt, and model performance against ground truths to make reccomendations on prompt improvements based on selected strategy
* Repeat

### Selection Criteria
- Primary metric: **average F1 across the three domains**
- Tie-breakers: `<e.g., highest recall on worst domain, fewest FP>`
---

## 2. Final Prompt

```text
# Task
Extract a software schema from the provided domain phrases. Map the phrases to a formal structure of classes, attributes, and relationships.

## Domain Phrases
<DOMAIN PHRASES>

## Labels and Mapping Rules
Use these labels. Follow the structural rules for each to ensure consistency:

- **C (Class)**: A primary entity, object, or conceptual category.
  - *Mapping*: `element` = class name, `arg1` = blank, `arg2` = blank.
- **A (Attribute)**: A property, characteristic, or a simple value associated with an entity.
  - *Mapping*: `element` = attribute name, `arg1` = the class it belongs to (if explicitly linked), `arg2` = blank.
  - *Note*: If a property is mentioned without a clear owner, or is a general characteristic of the domain, leave `arg1` blank.
- **V (Attribute Value)**: A specific value, state, or option of an attribute.
  - *Mapping*: `element` = the value, `arg1` = the attribute it belongs to, `arg2` = blank.
- **AS (Association)**: A relationship between two classes.
  - *Mapping*: `element` = the relationship verb/phrase, `arg1` = source class, `arg2` = target class.
- **AC (Association Class)**: A relationship that is itself a class (e.g., a transaction) with its own attributes.
  - *Mapping*: `element` = the association class name, `arg1` = source class, `arg2` = target class.
- **AG (Aggregation)**: A "part-of" or "whole-part" relationship.
  - *Mapping*: `element` = "Part-of", `arg1` = the whole, `arg2` = the part.
- **I (Inheritance)**: An "is-a" relationship.
  - *Mapping*: `element` = "ISA", `arg1` = the subclass, `arg2` = the superclass.

## Output Specification
Output raw CSV text. Do not use markdown code fences, bolding, or introductory text.

Header:
label,element,arg1,arg2

Constraints:
1. One row per extracted element.
2. Case Sensitivity: Use the casing found in the domain phrases.
3. Singular Form: Use singular nouns for all classes and attributes.
4. No Articles: Remove "a", "an", "the" from all fields.
5. No CamelCase: Use spaces between words instead of CamelCase.
6. Strict Slotting: 
   - For `I` (Inheritance), the `element` must be exactly "ISA".
   - For `AG` (Aggregation), the `element` must be exactly "Part-of".
   - For `V` (Value), `arg1` must be the attribute name.
7. Extraction Logic:
   - **Class vs Attribute**: If a noun represents a property (e.g., "price", "status", "name", "manufacturer"), label it as `A`. Do not create a Class `C` for things that are logically properties of another entity.
   - **Association vs Attribute**: Use `AS` only for active relationships between two distinct classes. If a relationship is described as a property of a transaction or a state, it may be an attribute `A`.
   - **Value Extraction**: Extract `V` rows only when the text explicitly lists specific options or states for an attribute. Do not create `V` rows for the attribute name itself.
   - **Implicit Attributes**: If a property is mentioned without a clear owner, extract it as `A` with a blank `arg1`.
   - **Avoid Over-Extraction**: Do not infer classes or associations that are not explicitly stated in the text. Do not create "helper" classes for simple attributes.
   - **State Mapping**: When a set of verbs or states describes the status of an entity (e.g., "purchase", "repair", "maintenance" for a vehicle), create one attribute `A` named "status" and map the specific states as `V` rows linked to that "status" attribute.
   - **Inheritance Precision**: For `I` (Inheritance), ensure the `element` is always "ISA". Do not put the class name in the `element` column.
8. Empty Fields: If a field is empty, leave it blank (e.g., `C,library,,`).
```

---

## 3. Responses & F1 Scores per Domain

# Scorecard

| Dataset | Precision | Recall | F1 | TP | FP | FN |
|---|---|---|---|---|---|---|
| library | 0.270 | 0.370 | 0.312 | 10 | 27 | 17 |
| rental | 0.317 | 0.288 | 0.302 | 19 | 41 | 47 |
| ntss | 0.221 | 0.283 | 0.248 | 15 | 53 | 38 |
| **average** | 0.269 | 0.314 | 0.287 | 44 | 121 | 102 |

Precision, recall and F1 are macro-averaged across the three datasets; TP/FP/FN are summed.

*Optimizer strategy: meta_prompting*

### Per-Domain Responses
Model responses for each domain are included verbatim from the winning trial:

<details>
<summary>library.csv</summary>

```csv
label,element,arg1,arg2
C,library,,
C,loan item,,
C,customer,,
C,member,,
C,membership card,,
C,subject section,,
C,language tape,,
C,book,,
C,bar code reader,,
C,record,,
A,member number,member,
A,name,member,
A,address,member,
A,date of birth,member,
A,classification mark,subject section,
A,bar code,loan item,
A,title language,loan item,
A,level,loan item,
A,title,loan item,
A,author,loan item,
A,status,loan item,
V,borrow,status,
V,reserved,status,
V,renewed,status,
V,extend,status,
V,French,title language,
V,beginner,level,
A,number of subject sections,library,
A,number of items,library,
I,ISA,member,customer
I,ISA,language tape,loan item
I,ISA,book,loan item
AS,has,member,membership card
AS,contains,library,subject section
AS,manages,library,record
AS,scans,bar code reader,loan item
AC,loan,member,loan item
```
</details>

<details>
<summary>rental.csv</summary>

```csv
label,element,arg1,arg2
C,vehicle,,
C,car,,
C,passenger car,,
C,customer,,
C,rental plan,,
C,reservation,,
C,salesperson,,
C,reservation form,,
C,contract,,
C,invoice,,
C,company,,
C,credit card processing company,,
A,manufacturer,vehicle,
A,price class,vehicle,
A,rental price,vehicle,
A,status,vehicle,
A,make,car,
A,model,car,
A,transmission,car,
A,door count,car,
A,body style,car,
A,option,car,
A,additional charge,option,
A,depreciation,vehicle,
A,location,vehicle,
A,time of reservation,reservation,
A,period of time,reservation,
A,reservation method,reservation,
A,rental charge,invoice,
A,credit card,invoice,
V,available,status,
V,not available,status,
V,rented out,status,
V,purchase,status,
V,repair,status,
V,maintenance,status,
V,disposal,status,
V,automatic,transmission,
V,manual,transmission,
V,two,door count,
V,four,door count,
V,sedan,body style,
V,hatchback,body style,
V,daily unlimited miles plan,rental plan,
V,weekend savings plan,rental plan,
V,voided,reservation,
I,car,vehicle,
I,passenger car,car,
AS,select,customer,rental plan,
AS,reserving,customer,reservation,
AS,process,salesperson,reservation,
AS,archive,salesperson,reservation form,
AS,sign,customer,contract,
AS,make,salesperson,invoice,
AS,cover,invoice,reservation,
AS,pay,customer,invoice,
AS,sent to,invoice,company,
AS,processed,invoice,credit card processing company,
AG,Part-of,reservation,reservation form,
AG,Part-of,vehicle,location,
```
</details>

<details>
<summary>ntss.csv</summary>

```csv
label,element,arg1,arg2
C,service provider,,
C,business customer,,
C,trade show,,
C,service,,
C,advertisement,,
C,speaker,,
C,participant,,
C,exhibitor,,
C,booth,,
C,conference room,,
C,seminar,,
C,reception,,
C,account,,
C,event,,
C,organizer,,
C,person,,
C,organization,,
C,domain,,
C,organization staff,,
C,observer,,
C,proposal,,
C,committee,,
C,reviewer,,
A,theme,trade show,
A,slogan,trade show,
A,location,trade show,
A,duration,trade show,
A,service charge,account,
A,payment received,account,
A,account balance,account,
A,contact information,organizer,
A,website,organizer,
A,fee,observer,
A,status,proposal,
A,booth size,booth,
V,pending,status,
V,review,status,
V,accepted,status,
V,rejected,status,
V,large,booth size,
V,medium,booth size,
V,small,booth size,
AS,create,service provider,trade show
AS,promote,service provider,trade show
AS,organize,service provider,trade show
AS,run,service provider,trade show
AS,create,service provider,account
AS,belong to,organizer,domain
AS,attended by,trade show,organization staff
AS,invited,trade show,observer
AS,selected,trade show,observer
AS,register,observer,trade show
AS,give keynote address,speaker,trade show
AS,prepares,reviewer,proposal
AS,runs,reviewer,proposal
AS,reviewed by,proposal,committee
AS,exhibit products,exhibitor,trade show
AS,pay,exhibitor,trade show
AS,request,exhibitor,booth
AS,rent,exhibitor,booth
AS,visit,participant,trade show
I,trade show,event,
I,organizer,person,
I,organizer,organization,
AG,Part-of,trade show,booth
AG,Part-of,trade show,conference room
AG,Part-of,trade show,seminar
AG,Part-of,trade show,reception
```
</details>