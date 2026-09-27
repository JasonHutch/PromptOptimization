# Ground truths

Evaluation references only. Never paste these into a prompt.

## identification/
Built from the instructor's answer keys:
- library.csv    <- Library-domain-phrases.docx (56 items; matches instructor's updated count)
- ntss.csv       <- ntss-underlined.doc superscripts (rule number = category)
- car_rental.csv <- Brainstorming column of 4392-crclassified.doc

Columns: rule, phrase. Alternates separated by " / " (inflections, expert renamings).
Rule numbers: 1 noun/noun phrase, 2 "X of Y", 3 transitive verb, 4 adjective/enumeration,
5 numeric/quantity, 6 possession, 7 consist-of/part-of, 8 containment, 9 "X is a Y".
Enumerations the key underlines as one span (e.g. "large, medium, or small") are split into
one item per value, matching how the library key lists French / beginner separately.

## classification/
Copies of the top-level CSVs. ntss.csv is corrected against ntss-classified.doc, which the
original conversion dropped:
- A,type,Speaker  (Speaker has "(A) type (values: invited, selected)")
- V rows for the listed values of Speaker.type and Proposal.status
The originals in ground_truths/*.csv are left unchanged.
