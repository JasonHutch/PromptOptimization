# Task
Read the business description below and list every domain-specific phrase you can find in it.

## Business Description
<DESCRIPTION>

## Rule numbers
Categorize each phrase with the matching rule number. Follow these definitions and examples strictly:

1 = nouns / noun phrases. Extract the core entity. Avoid overly long descriptive phrases; focus on the business object.
   - Example: "The company provides vehicle rentals" -> 1,vehicle
   - Example: "The rental fleet consists of passenger cars" -> 1,passenger car
   - Example: "The company has a great business model" -> 1,business model
   - Few-Shot: "The library has records" -> 1,records
   - Few-Shot: "The company provides professional services" -> 1,services
   - Error Correction: If a phrase is a state or a process (e.g., "purchase", "repair", "maintenance"), it belongs in Rule 4, not Rule 1.
   - Note: Do not include adjectives or descriptors that belong in Rule 4. Do not extract generic business terms (e.g., "operating cost", "improvement proposals") unless they are the primary domain entity.
   - Critical: Extract the simplest form of the entity. "The rental locations are managed" -> 1,location.

2 = "X of Y" expressions.
   - Example: "The update of records is daily" -> 2,update of records
   - Example: "The number of subject sections" -> 2,number of subject sections
   - Example: "The size of the booth" -> 2,size of the booth
   - Few-Shot: "The types of participants" -> 2,types of participants
   - Error Correction: Extract the structural relationship. "Types of loan items" -> 2,types of loan items.
   - Note: If the phrase is "types of [Entity]", extract as Rule 2.

3 = transitive verbs. Extract the base verb or the passive phrase.
   - Example: "Items are scanned by staff" -> 3,scanned
   - Example: "The system processes the request" -> 3,process
   - Example: "The proposal is reviewed by experts" -> 3,reviewed by
   - Few-Shot: "The system keeps track of rentals" -> 3,keep track of
   - Error Correction: Extract the action, not the noun. "The system records the payment" -> 3,record.
   - Note: Focus on actions that change the state of an entity or move data. Extract the base form (e.g., "issued" -> 3,issue).
   - Critical: Do not categorize state-based adjectives (e.g., "borrowed", "reserved", "renewed") as Rule 3; these are Rule 4.

4 = adjectives and list items (status, types, qualities, and state-based nouns).
   - Example: "The car is available" -> 4,available
   - Example: "The proposal is pending review" -> 4,pending
   - Example: "The event is national or international" -> 4,national
   - Few-Shot: "The car is for repair" -> 4,repair
   - Few-Shot: "The event is held in person" -> 4,in person
   - Error Correction: Include nouns that describe a state or category of an object. "The car is for maintenance" -> 4,maintenance.
   - Note: Extract the state/quality only. If the text says "pending review", extract "pending".

5 = numbers and quantities.
   - Example: "There are several makes" -> 5,several
   - Example: "Maximum of 8" -> 5,maximum of 8
   - Example: "Two types of items" -> 5,two
   - Few-Shot: "One or more domains" -> 5,one or more
   - Few-Shot: "Four doors" -> 5,four
   - Note: Do not categorize numbers as Rule 4.

6 = possession ("has"). Extract ONLY the verb "has".
   - Example: "A member has a title" -> 6,has
   - Example: "The company has several models" -> 6,has
   - Note: Never include the object of the possession in this rule.

7 = "consist of" / "part of" expressions (e.g., "made up of", "involves", "including").
   - Example: "The process involves registration" -> 7,involves
   - Example: "The fleet is made up of cars" -> 7,made up of

8 = containment expressions ("contains", "holds").

9 = "is a" expressions. Extract the full relationship phrase.
   - Example: "A customer is known as a member" -> 9,customer is known as a member
   - Example: "Tapes and books are types of loan items" -> 9,tapes and books are types of loan items
   - Few-Shot: "A trade show can be regarded as an event" -> 9,can be regarded as
   - Note: Extract the relationship, not just the entities.

# Output
Output raw CSV text with exactly this header row, followed by one row per phrase.

rule,phrase

Output nothing except the CSV text. Do not include markdown formatting or code fences.