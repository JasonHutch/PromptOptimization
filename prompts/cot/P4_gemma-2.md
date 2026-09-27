# Role

Build an AUM domain model in four controlled stages. Keep reasoning concise and do not expose hidden chain-of-thought; provide only the requested audit tables and final model.

# Business description

"""
{{DESCRIPTION}}
"""

## Step 1: Domain-specific phrases

Apply the identification rules: preserve literal source wording, scan every sentence for nouns, `of` phrases, verbs in all grammatical positions, states/enumerations, quantities, possession, part/whole, containment, and generalization. Exclude generic software language and narrative. Output exactly:

| rule | phrase |
|---|---|

## Step 2: Classification ledger

For each Step 1 phrase, output one short audit row:

| phrase | label | element | arg1 | arg2 | evidence |
|---|---|---|---|---|---|

Use only `C`, `A`, `V`, `AS`, `AC`, `AG`, and `I`. The evidence must be a short source-based fragment, not invented information.

## Step 3: Model audits

Output exactly:

| audit | result |
|---|---|

Check source-span fidelity, duplicate aliases, class/attribute ownership, relationship endpoints, inheritance tests, and both association-class conditions. Record `pass` or a concise correction.

## Final domain model

After applying the audits, output exactly:

| label | element | arg1 | arg2 |
|---|---|---|---|

Rows must begin with only `C`, `A`, `V`, `AS`, `AC`, `AG`, or `I`. Do not use `AUM` as a label. No prose or code fences after the final table.
