# Change Log (trial 9)

- Added explicit instruction to Rule 6 to extract only the relationship phrase and exclude the subject, addressing FPs where the model extracted full sentences (e.g., "company has several different makes of cars").
- Reinforced Rule 9 constraints to ensure only the marker is extracted, addressing FPs where the model included the subject/object (e.g., "customer is known as a member").
- Clarified Rule 1 vs Rule 4 distinction to prevent noun-form statuses (e.g., "maintenance", "disposal") from being categorized as Rule 1, addressing FPs in the rental dataset.
- Strengthened the "X of Y" priority for Rule 2 to reduce FNs where domain entities were extracted as Rule 1 instead of the full phrase as Rule 2.
