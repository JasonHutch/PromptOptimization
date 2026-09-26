# Change Log (trial 9)

- Clarified Rule 4 to explicitly include "purchase", "repair", "maintenance", and "disposal" as statuses/categories to reduce FP in the rental dataset where they were incorrectly tagged as Rule 1.
- Reinforced Rule 5 to prevent numbers (e.g., "two", "four") from being categorized as Rule 4 (Adjectives), addressing a specific error in the rental dataset.
- Emphasized the extraction of base forms for Rule 3 (Verbs) to improve recall and matching for stemmed ground-truth verbs (e.g., "borrowed" -> "borrow").
- Added explicit instruction to capture "taken from" and "returned to" as domain-specific actions under Rule 3 to address FN in the rental dataset.
- Maintained strict output formatting to ensure CSV compatibility and zero-shot precision.
