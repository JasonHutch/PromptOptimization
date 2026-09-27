# Identification

**Task:** Identification
---

## 1. Identification Methodology

Lang Graph workflow broken down into the following states
* Initial prompt
* identification task conducted against ntss, library, and car rental domains
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
Read the business description below and extract every domain-specific phrase.

## Business Description
<DESCRIPTION>

## Extraction Rules
Categorize each phrase using the following rule numbers. Extract the core concept only.

1 = Nouns / Noun phrases (Primary entities, objects, or concepts. Include specific business roles, domain objects, and the name of the business/organization itself.)
2 = "X of Y" expressions (Phrases indicating composition, quantity, or attribute, e.g., "number of items", "types of cars", "duration of the event". Extract the full phrase.)
3 = Transitive verbs (Actions performed on an object. Use the base form/lemma. Include phrasal verbs like "keep track of" or "belong to".)
4 = Adjectives and list items (Qualifiers, statuses, categories, or methods of delivery, e.g., "available", "national", "by phone", "pending", "accepted". Include specific domain values like "French" or "daily".)
5 = Numbers and quantities (Specific counts, ranges, or quantifiers, e.g., "8", "several", "one or more", "each".)
6 = Possession (The relationship "has" or "contains" as a property of an entity. Extract the full relationship phrase, e.g., "has a title language".)
7 = Composition/Involvement ("consist of", "part of", "involves", "including")
8 = Containment expressions (Physical holding/containing)
9 = Identity/Categorization (The relationship markers only, e.g., "is a", "regarded as", "type of", "known as")

## Output Specifications
- Output raw CSV text.
- Header row: `rule,phrase`
- One row per phrase.
- Phrase Normalization: 
    - Use singular forms for nouns (e.g., "customers" -> "customer").
    - Use base forms for verbs (e.g., "processed" -> "process").
    - Remove leading/trailing articles (a, an, the).
    - Do not include full sentences.
    - For Rule 9, extract ONLY the relationship marker (e.g., "regarded as"), not the entities being linked.
    - For Rule 4, extract the specific qualifier or status (e.g., "available", "voided").
    - Do not include "implied" logic; extract only text present in the description.
- Precision Filter: 
    - Avoid extracting generic business jargon (e.g., "business model", "job market", "operating cost") unless they are central domain entities.
    - Do not extract "filler" nouns that are merely parts of other extracted phrases (e.g., if you extract "number of items" for Rule 2, do not also extract "number" as Rule 1).
    - Ensure Rule 4 is used for statuses and attributes (e.g., "available", "pending") rather than complex noun phrases.
    - Do not extract phrases that are purely descriptive of the business's general operation (e.g., "car rental company") if a more specific domain entity exists (e.g., "vehicle").
- Strict Rule Adherence:
    - Rule 3 (Verbs): Ensure you capture all action verbs, including those that appear as gerunds (e.g., "processing" -> "process") or past participles (e.g., "identified" -> "identify").
    - Rule 4 (Attributes): Capture specific domain values (e.g., "French", "daily") as Rule 4, not Rule 1.
    - Rule 9 (Identity): Extract only the marker (e.g., "is a", "type of"). Do not include the subject or object of the relationship.
    - Rule 1 vs Rule 4: If a word functions as a status, a category, or a state of an entity (e.g., "purchase", "repair", "maintenance", "opened", "disposal" when used as a status of a vehicle/record), assign it to Rule 4.
    - Rule 1 vs Rule 2: If a phrase follows the "X of Y" pattern, it MUST be Rule 2, even if the "Y" part is a domain entity.
    - Rule 5 (Quantities): Extract specific numeric constraints (e.g., "maximum of 8", "less than 8") as Rule 5.
    - Rule 6 (Possession): Extract only the relationship phrase (e.g., "has a title"). Do not include the full sentence or the subject of the possession.
- Output nothing except the CSV text. No markdown fences, no preamble.
```

---

## 3. Responses & F1 Scores per Domain

# Scorecard

| Dataset | Precision | Recall | F1 | TP | FP | FN |
|---|---|---|---|---|---|---|
| library | 0.773 | 0.618 | 0.687 | 34 | 10 | 21 |
| rental | 0.487 | 0.629 | 0.549 | 39 | 41 | 23 |
| ntss | 0.728 | 0.770 | 0.749 | 67 | 25 | 20 |
| **average** | 0.663 | 0.672 | 0.662 | 140 | 76 | 64 |

Precision, recall and F1 are macro-averaged across the three datasets; TP/FP/FN are summed.

*Optimizer strategy: meta_prompting*


### Per-Domain Responses
Model responses for each domain are included verbatim from the winning trial:

<details>
<summary>library.csv</summary>

```csv
rule,phrase
1,library
3,issue
1,loan item
1,customer
9,known as
1,member
1,membership card
1,member number
1,name
1,address
1,date of birth
1,subject section
2,number of subject sections
1,classification mark
3,identify
1,bar code
9,type of
1,language tape
1,book
6,has a title language
4,French
6,has a level
4,beginner
6,has a title
6,has a author
5,maximum of 8
3,borrow
3,reserve
3,renew
3,extend
1,loan
3,scan
1,bar code reader
3,enter
4,valid
5,less than 8
3,read
4,reserved
3,stamp
3,support
1,facility
3,search
2,update of records
4,daily
```
</details>

<details>
<summary>rental.csv</summary>

```csv
rule,phrase
1,rental location
1,vehicle
1,passenger car
1,reservation system
1,make
1,model
1,manufacturer
1,price class
1,rental plan
1,gear change
1,door
1,sedan
1,hatchback
1,option
1,customer
1,salesperson
1,reservation form
1,file cabinet
1,deposit
1,contract
1,block reservation
1,invoice
1,rental
1,credit card
1,credit card processing company
1,preventive maintenance
1,damage
1,tax
1,depreciation
2,number of rental locations
2,forms of vehicle rentals
2,number of price classes
2,models of car
2,period of time
3,take
3,return
3,branch out
3,select
3,display
3,suggest
3,reserve
3,process
3,archive
3,void
3,sign
3,honor
3,handle
3,check out
3,open
3,settle
3,keep track of
4,additional
4,available
4,rented out
4,daily
4,unlimited miles
4,weekend
4,10% discount
4,automatic
4,manual
4,two
4,four
4,in person
4,through the phone
4,manually
4,voided
4,purchase
4,repair
4,maintenance
4,disposal
5,several
5,one
5,different
5,small number
5,one or more
6,company has several different makes of cars
6,make may have several models
6,company has a number of different rental plans
7,grouped into
9,is a
```
</details>

<details>
<summary>ntss.csv</summary>

```csv
rule,phrase
1,National Trade Show Services
1,service provider
1,business customer
1,trade show
1,design
1,professional service
1,theme
1,slogan
1,location
1,duration
1,advertisement activity
1,speaker
1,participant
1,exhibitor
1,on site registration
1,booth
1,conference room
1,seminar
1,reception
1,trade show material
1,account
1,service charge
1,payment
1,account balance
1,event
1,organizer
1,person
1,organization
1,contact information
1,website
1,domain
1,event organization staff
1,observer
1,registration fee
1,NTSS staff
1,keynote address
1,proposal
1,committee
1,reviewer
1,expert
1,status
1,product
1,service
2,selection of a theme
2,selection of a slogan
2,duration of the event
2,types of participants
2,evaluation of their proposals
2,size of the booth
3,create
3,promote
3,organize
3,run
3,contact
3,invite
3,register
3,set up
3,distribute
3,record
3,maintain
3,belong to
3,change
3,add
3,remove
3,attend
3,charge
3,prepare
3,give
3,review
3,exhibit
3,pay
3,request
3,rent
3,visit
4,national
4,international
4,pending review
4,accepted
4,rejected
4,large
4,medium
4,small
5,one or more
5,each
6,has an organizer
6,has contact information
6,has a website
7,involve
7,include
9,regarded as
9,is a
9,type of
```
</details>