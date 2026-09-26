# Task
Classify the provided domain phrases into a software system schema (classes, attributes, associations, etc.).

## Labels
- C = class
- A = attribute
- V = attribute value
- AS = association
- AC = association class
- AG = aggregation
- I = inheritance

## Extraction Rules & Examples
1. **Classes (C):** Identify core entities. Use singular nouns.
   - *Example:* "The system manages books" -> `C,book,,`
2. **Attributes (A):** Identify properties. 
   - **Mapping:** Map the attribute to its owner class in `arg1`. If the owner is not explicitly mentioned or is a global property, leave `arg1` blank.
   - **Avoid Over-extraction:** Do not create a new Class for a simple property.
   - *Example:* "A book has a title" -> `A,title,book,`
   - *Few-Shot (Global/Implicit):* "The vehicle has a manufacturer" -> `A,manufacturer,,`
   - *Few-Shot (Correct Mapping):* "The customer has a name and address" -> `A,name,customer,` \n `A,address,customer,`
3. **Attribute Values (V):** Identify specific allowed values for an attribute. Map the value to the attribute name in `arg1`.
   - *Example:* "The transmission can be automatic or manual" -> `V,automatic,transmission,`
   - *Few-Shot (Conceptual Attribute):* "The vehicle can be purchased, repaired, or maintained" -> `V,purchase,status,`
   - *Few-Shot (Categorical Value as Attribute):* "The vehicle can be a sedan or a hatchback" -> `A,body style,,` \n `V,sedan,body style,` \n `V,hatchback,body style,`
4. **Associations (AS):** Identify structural relationships between two classes. Use a verb for the element.
   - *Example:* "Customers borrow books" -> `AS,borrow,customer,book`
   - *Few-Shot (Avoid Over-extraction):* "The salesperson archives the reservation" -> (Ignore if it is a transient task; only extract if it defines a permanent system relationship).
   - *Few-Shot (Implicit Relationship):* "The customer has a membership card" -> `AS,has,customer,membership card`
5. **Inheritance (I):** Identify "is-a" relationships. Use "ISA" as the element, the subclass as `arg1`, and the superclass as `arg2`.
   - *Example:* "A book is a type of loan item" -> `I,ISA,book,loan item`
   - *Few-Shot (Direct Hierarchy):* "A sedan is a type of car" -> `I,ISA,sedan,car`
6. **Aggregation (AG):** Identify "part-of" relationships. Use "Part-of" as the element, the part as `arg1`, and the whole as `arg2`.
   - *Example:* "A library consists of sections" -> `AG,Part-of,section,library`
   - *Few-Shot (Correct Direction):* "A reviewer is part of a committee" -> `AG,Part-of,reviewer,committee`
7. **Association Class (AC):** Identify a relationship that is treated as an entity linking two others or has its own attributes.
   - *Example:* "A loan transaction links a customer and a book" -> `AC,loan transaction,customer,book`
   - *Few-Shot (Process as Entity):* "A reservation is a process between a customer and a vehicle" -> `AC,reservation,customer,vehicle`

## Domain Phrases
<DOMAIN PHRASES>

# Output
Output raw CSV text with exactly this header row, followed by one row per phrase.
label,element,arg1,arg2

Output nothing except the CSV text. No markdown formatting, no code fences.