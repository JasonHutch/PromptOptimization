# Task
Extract a software schema (classes, attributes, associations, etc.) from the provided domain phrases.

## Domain Phrases
<DOMAIN PHRASES>

## Schema Labels & Logic
Use these labels. Follow these strict mapping rules for the columns (label, element, arg1, arg2):

- **C (Class)**: A primary entity, object, or distinct category. 
  - Format: `C,ClassName,,`
- **A (Attribute)**: A property, characteristic, or data field. 
  - Format: `A,AttributeName,OwningClass,`
  - *Crucial*: If the attribute is a general property of the system, or if the owning class is not explicitly stated in the phrase, leave `arg1` empty.
- **V (Attribute Value)**: A specific allowed value for an attribute.
  - Format: `V,ValueName,AttributeName,`
- **AS (Association)**: A relationship between two classes. 
  - Format: `AS,RelationshipName,Class1,Class2`
- **AC (Association Class)**: A relationship that is itself an entity with attributes (e.g., a transaction, a registration, or a contract). 
  - Format: `AC,ClassName,Class1,Class2`
- **AG (Aggregation)**: A "part-of" or "whole-part" relationship. 
  - Format: `AG,Part-of,WholeClass,PartClass`
- **I (Inheritance)**: An "is-a" or specialization relationship. 
  - Format: `I,ISA,SubClass,SuperClass`

## Extraction Guidelines
1. **Naming Convention**: Use singular nouns. Use the capitalization found in the phrases. Use spaces instead of CamelCase.
2. **Attribute vs. Class (The "Property" Rule)**: 
   - Be extremely conservative with Class (C) creation. 
   - If a term describes a property, a characteristic, or a value (e.g., "manufacturer", "price", "status", "theme", "location", "fee", "balance"), it MUST be an Attribute (A).
   - **Implicit Ownership**: Do not guess the owning class. If the phrase does not explicitly link an attribute to a specific class, leave `arg1` blank.
3. **Association vs. Attribute**: 
   - Use **A** for simple properties.
   - Use **AS** for structural relationships between two distinct entities.
   - Use **AC** for complex events or transactions (e.g., "registration", "loan transaction", "payment", "contract") that link two classes.
4. **Inheritance (I)**: Always use "ISA" as the element. `arg1` is the specific (child), `arg2` is the general (parent).
5. **Aggregation (AG)**: Always use "Part-of" as the element. `arg1` is the whole, `arg2` is the part.
6. **Precision & Noise Reduction**: 
   - Do not invent entities or "helper" classes. Only extract what is explicitly mentioned.
   - Do not create classes for things that are clearly values (V) or attributes (A).
   - Avoid extracting generic "has" relationships unless they are the only way to describe a critical link.
7. **Consistency**: Any element used in `arg1` or `arg2` must be defined as a Class (C) or an Attribute (for V).

# Output
Output raw CSV text with exactly this header row, followed by one row per phrase.
label,element,arg1,arg2

Output nothing except the CSV text. No markdown, no code fences, no preamble.