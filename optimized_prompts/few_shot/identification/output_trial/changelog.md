# Change Log (trial 9)

- Added "Critical" note to Rule 3 to prevent state-based adjectives (e.g., "borrowed", "reserved") from being categorized as verbs, addressing the high FP rate in the library dataset.
- Updated Rule 2 Few-Shot from "types of" to "types of participants" to ensure the model extracts the full phrase rather than a fragment, improving recall for structural expressions.
- Reinforced Rule 4's definition of state-based nouns to ensure "repair" and "maintenance" are consistently captured as Rule 4 rather than Rule 1, addressing the rental dataset mismatches.
- Clarified Rule 1's "simplest form" instruction to reduce over-extraction of descriptive phrases (e.g., "business model", "labor cost") that were marked as FP in the rental dataset.
