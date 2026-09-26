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