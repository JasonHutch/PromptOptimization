# Change Log (trial 9)

- Fixed Inheritance mapping: Added explicit instruction to use "ISA" as the element for `I` labels to prevent the model from putting the class name in the element column (addresses FP/FN in rental and ntss datasets).
- Refined Class vs Attribute logic: Strengthened the rule against creating "helper" classes for simple properties to reduce FP (addresses over-extraction of classes in library and ntss).
- Clarified Value Extraction: Explicitly forbade creating `V` rows for the attribute name itself to reduce FP.
- Reinforced Slotting: Added a specific constraint for `I` (Inheritance) to ensure the `element` column is strictly "ISA", matching ground truth patterns.
