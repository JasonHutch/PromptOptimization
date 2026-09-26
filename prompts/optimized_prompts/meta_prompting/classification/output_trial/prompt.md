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