# Scorecard (trial 9)

| Dataset | Precision | Recall | F1 | TP | FP | FN |
|---|---|---|---|---|---|---|
| library | 0.875 | 0.636 | 0.737 | 35 | 5 | 20 |
| rental | 0.507 | 0.581 | 0.541 | 36 | 35 | 26 |
| ntss | 0.792 | 0.655 | 0.717 | 57 | 15 | 30 |
| **average** | 0.725 | 0.624 | 0.665 | 128 | 55 | 76 |

Precision, recall and F1 are macro-averaged across the three datasets; TP/FP/FN are summed.

*Optimizer strategy: few_shot_prompting*
