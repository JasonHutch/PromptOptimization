# P4 to P5 Gemma 2 increment

## P4 execution

The original repository prompt [P4.md](../prompts/identification/P4.md) was sent to `gemma2:latest` with temperature `0.7` for 10 trials on each domain. The original P4 prompt was not modified.

| Domain | Mean precision | Mean recall | Mean F1 |
|---|---:|---:|---:|
| Library | 74.6% | 63.6% | 68.5% |
| Car rental | 29.8% | 65.8% | 41.0% |
| NTSS | 72.6% | 72.0% | 71.9% |

Raw responses and per-trial scores are in [p4_identification/](./p4_identification/).

## Error evidence used for P5

The P4 run repeatedly missed:

- literal `of` phrases such as `date of birth`, `types of loan items`, `update of records`, `models of car`, `time of reservation`, and `period of time`;
- quantities such as `two`, `one or more`, `less than 8`, and `four`;
- whole possession clauses such as `has a title language`, `has a title, and author(s)`, and the NTSS organizer/contact-information clauses;
- lifecycle values such as `purchase`, `repair`, `maintenance`, and `disposal`;
- rule 7 and rule 9 expressions.

It repeatedly added unsupported generic narrative words such as `business`, `information`, `costs`, `activities`, `different`, `several`, `given`, and `professional`, and misclassified some state or relationship wording.

## P5 increment

[P5_gemma-2.md](../prompts/identification/P5_gemma-2.md) is the original P4 prompt plus a targeted second-pass audit. It does not replace or alter P4. The additions explicitly address only the observed P4 misses and false positives.
