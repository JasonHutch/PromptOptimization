# Saif prompt-optimization evaluation

## Scope

The `_gemma-2` prompt set adds coverage audits, source-span fidelity checks, an evidence ledger, and a mandatory two-condition association-class gate:

- [P5_gemma-2.md](../prompts/identification/P5_gemma-2.md) identifies phrases.
- [P4_gemma-2.md](../prompts/classification/P4_gemma-2.md) classifies phrases.
- [P4_gemma-2.md](../prompts/cot/P4_gemma-2.md) combines both activities with auditable intermediate tables.

## Measured regression

The environment has no LLM runner or model credentials. `scripts/evaluate_gemma-2.py` therefore copies the repository's strongest existing P4/P3/P3 response fixtures under `_gemma-2` names and scores them with the existing evaluators. This is a reproducible scorer regression, not a claim that a fresh model call was made with the new prompts.

| Activity | Domain | F1 | Precision | Recall | Fixture |
|---|---|---:|---:|---:|---|
| Identification | library | 95.5% | 96.4% | 94.6% | P4 |
| Identification | car rental | 71.9% | 62.5% | 84.6% | P4 |
| Identification | NTSS | 89.6% | 84.5% | 95.3% | P4 |
| Classification | library | 69.1% | 67.9% | 70.4% | P3 |
| Classification | car rental | 50.4% | 52.5% | 48.5% | P3 |
| Classification | NTSS | 64.7% | 58.1% | 72.9% | P3 |

The detailed machine-readable report is [saif_fixture_regression.json](./scores/saif_fixture_regression.json). The report keeps the assignment's 97% goal visible; these fixture results do not meet it, so fresh LLM runs are still required before claiming completion.

## Actual local Ollama run

The prompts were then sent to the installed local Ollama models through [run_ollama_gemma-2.py](./scripts/run_ollama_gemma-2.py). The latest run used `gemma2:latest` with temperature 0. Raw outputs are under the `_gemma-2` response directories. Scores are in [ollama_gemma-2_report.json](./scores/ollama_gemma-2_report.json).

| Activity | Domain | Precision | Recall | F1 |
|---|---|---:|---:|---:|
| Identification | library | 81.8% | 64.3% | 72.0% |
| Identification | car rental | 27.7% | 50.8% | 35.9% |
| Identification | NTSS | 78.9% | 65.1% | 71.3% |
| Classification | library | 51.5% | 63.0% | 56.7% |
| Classification | car rental | 17.3% | 21.2% | 19.0% |
| Classification | NTSS | 26.2% | 27.1% | 26.7% |

The CoT outputs did not consistently follow the required Step 1 and final-table headings, so their scores are low and partly reflect output-format failure. This shows that the combined task is too demanding for this small model and should be split into stricter staged calls or run with a stronger local model.

## Reproduction

```bash
virtualenv .venv
.venv/bin/python scripts/run_ollama_gemma-2.py --model gemma2:latest
.venv/bin/python scripts/score_ollama_gemma-2.py --model gemma2:latest
```

This writes `_gemma-2` response copies under `responses/`, per-domain score files under `scores/`, and [results_gemma-2.json](./results_gemma-2.json) for the deck generator. The script intentionally labels the run `fixture-regression` so fixture scores cannot be mistaken for new model evaluations.

## Lessons carried into the prompts

1. Identification needs a second source-span pass because missed passive verbs, quantities, and list values lower recall.
2. Classification needs a concept ledger before relationship creation so aliases do not cascade into inconsistent class and attribute names.
3. Association classes require a separate many-to-many and maintained-occurrence check; a relationship noun alone is not sufficient.
4. Exact table contracts reduce parser failures and keep scorer output comparable across prompt versions.
