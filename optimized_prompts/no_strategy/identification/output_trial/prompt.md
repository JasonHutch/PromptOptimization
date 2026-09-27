# Task
Read the business description below and extract domain-specific phrases. You are identifying the core entities, attributes, and relationships of the business domain.

## Business Description
<DESCRIPTION>

## Extraction Rules
Categorize each phrase using the following rule numbers. Be precise: extract the shortest meaningful phrase that captures the concept.

1 = Nouns / Noun Phrases (Core entities, objects, or concepts. e.g., "vehicle", "customer", "registration")
2 = "X of Y" expressions (Possessive or descriptive relationships. e.g., "makes of cars", "duration of the event")
3 = Transitive Verbs (Actions performed on entities. Extract the base form. e.g., "process", "archive", "borrow")
4 = Adjectives and List Items (Qualities, statuses, categories, or descriptors. e.g., "available", "national", "pending", "automatic")
5 = Numbers and Quantities (Specific counts, limits, or quantifiers. e.g., "two", "maximum of 8", "several", "one or more")
6 = Possession ("has") (The specific relationship of having an attribute. Extract only the relationship trigger, e.g., "has", "has a")
7 = "consist of" / "part of" / "includes" / "involves" expressions (Compositional relationships. Extract only the relationship trigger. e.g., "made up of", "involves", "including")
8 = Containment expressions ("contains", "holds")
9 = "is a" / "regarded as" expressions (Equivalence or classification. Extract the full equivalence phrase. e.g., "customer is known as a member")

## Guidelines
- **Precision over Volume**: Focus on primary domain entities. Avoid generic business terms (e.g., "business model", "service") unless they are central to the domain.
- **Rule 1 (Nouns)**: Extract the base noun. Avoid adding unnecessary adjectives (e.g., use "vehicle" instead of "passenger cars" unless "passenger car" is a distinct domain category). Ensure you capture all distinct entities mentioned, including those that appear as part of a larger phrase.
- **Rule 3 (Verbs)**: Extract the verb in its base form (e.g., "borrow" instead of "borrowed"). Capture all domain-specific actions, including those that describe the movement or state change of an entity (e.g., "taken from", "returned to").
- **Rule 4 (Adjectives/Statuses)**: Explicitly capture statuses (e.g., "pending", "voided", "available") and categories (e.g., "national", "international"). Include descriptors that function as attributes of an entity (e.g., "automatic", "manual"). If a word like "purchase", "repair", "maintenance", or "disposal" is used as a status or category of a record/activity, use Rule 4.
- **Rule 5 (Quantities)**: Capture all quantifiers, including phrases like "one or more", "several", "a number of", "each", and specific numbers (e.g., "two", "four"). Do not categorize these as Rule 4.
- **Rule 6 & 7 (Relationships)**: Do not include the subject or object of the relationship. Extract only the relationship trigger (e.g., for "Event has an organizer", extract "has"; for "Trade show involves design", extract "involves").
- **Rule 9 (Equivalence)**: Extract the full phrase that establishes the equivalence (e.g., "X is known as Y").
- **Avoid Over-extraction**: Do not extract descriptive filler. If a phrase is a combination of a noun and an adjective that doesn't form a unique domain term, prioritize the noun.

# Output
Output raw CSV text with exactly this header row, followed by one row per phrase.

rule,phrase

Output nothing except the CSV text. No markdown formatting, no code fences.