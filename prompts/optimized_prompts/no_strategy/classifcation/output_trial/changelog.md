# Change Log (trial 9)

- Added "fee" and "balance" to the "Property Rule" examples to prevent the model from incorrectly classifying financial attributes as Classes (addresses high FP in ntss dataset).
- Reinforced the "Implicit Ownership" rule to discourage the model from guessing owning classes when not explicitly stated (addresses high FP in library and rental datasets).
- Clarified that "C (Class)" includes "distinct categories" to better capture inheritance hierarchies (addresses FN in rental and ntss datasets).
- Maintained strict output formatting to ensure exact-match scoring compatibility.
