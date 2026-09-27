# Role

You are performing AUM Step 3: classify the supplied domain-specific phrases into a domain model.

# Evidence and scope

Use only the business description and phrase table. Ignore background narrative and software infrastructure. Preserve lower-case source wording; do not invent synonyms. First identify classes, then attributes, then values and relationships. Do not classify a phrase as multiple incompatible elements.

# Decisions

- `C`: an independently existing domain object, role, document, place, or business occurrence.
- `A`: a scalar property, identifier, state, quantity, or characteristic owned by exactly one class.
- `V`: a literal closed-list value owned by an attribute. Create the attribute row when needed.
- `AS`: an application-domain verb relationship between two classes explicitly supported by the sentence.
- `AG`: an explicit object part/whole relationship.
- `I`: inheritance only when every instance of the child is the parent and the parent's relationships apply.
- `AC`: an association occurrence class only when the matching association is many-to-many AND information about that occurrence is maintained.

# Car-rental and narrative guard

Do not create classes or relationships for generic narrative concepts such as business, service, costs, job market, solution, operation, system, message, or information. Do not create classes from property words such as make, model, price class, status, transmission, or body style; make them attributes of vehicle/car when the description supports that ownership. Do not make unsupported relationships from generic verbs such as provide, want, need, allow, have, or display.

# Attribute and value guard

Properties such as price, status, available, rented out, manufacturer, model, transmission, body style, additional charge, depreciation, time of reservation, grace period, means, void, and opened are attributes when supported by the description. Values such as automatic/manual, sedan/hatchback, purchase/repair/maintenance/disposed, in person/by phone, and numeric bounds are `V` rows owned by the relevant attribute. Do not turn values into classes.

# Association-class audit

For every possible association, answer both questions privately: is it many-to-many, and is information about the relationship occurrence maintained? Only if both answers are yes, output the matching `AS`, one `AC`, and occurrence attributes. Never output an `AC` without its `AS` and at least one attribute. Never duplicate an `AC` as a plain `C`.

# Final graph audit

Remove unsupported narrative elements, merge aliases, ensure every `AS`, `AG`, and `I` endpoint is a `C` or `AC`, ensure every `A` has one owner, ensure every `V` has one attribute owner, and ensure each association class passes both tests.

# Output contract

Your entire response must be exactly one markdown table:

| label | element | arg1 | arg2 |
|---|---|---|---|

Allowed labels are only `C`, `A`, `V`, `AS`, `AC`, `AG`, and `I`. Do not write an introduction, reasoning, notes, or any additional table. Use blank cells when an argument does not apply.

# Business description

"""
{{DESCRIPTION}}
"""

# Domain-specific phrases

{{PHRASES}}
