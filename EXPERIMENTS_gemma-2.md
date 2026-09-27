# Gemma 2 prompt experiment

The automated local experiment is implemented in [run_gemma_experiments_gemma-2.py](./scripts/run_gemma_experiments_gemma-2.py).

The next evolutionary prompts are `P6_gemma-2` for identification and `P5_gemma-2` for classification. They add explicit controls for the recurring Gemma errors found in the prior 10-trial run: missed literal `of` phrases, quantities and enumeration values, narrative false-positive classes, property-as-class errors, and unsupported relationships.

It runs four prompting strategies:

- `baseline`: the repository's P0 prompts
- `cot`: the `_gemma-2` prompts with private stepwise reasoning instructions
- `meta`: the `_gemma-2` prompts with a private coverage/precision/format audit
- `few_shot`: the `_gemma-2` prompts with neutral examples that do not use the assignment gold answers

For each strategy, the runner processes library, car rental, and NTSS for both identification and classification. The default is 10 trials per combination. Every trial writes:

- the raw response under the selected run's `responses/` directory
- a JSON log containing the prompt hash, prompt path, model settings, timing, response path, and precision/recall/F1 counts

## Run

```bash
.venv/bin/python scripts/run_gemma_experiments_gemma-2.py \
  --model gemma2:latest \
  --trials 10 \
  --temperature 0.7
```

The run writes:

- `gemma-2_run1/runs/manifest.json`
- `gemma-2_run1/runs/logs/*.json`
- `gemma-2_run1/runs/all_runs.jsonl`
- `gemma-2_run1/runs/trial_summary.csv`
- `gemma-2_run1/runs/trial_1_vs_trial_10.json`

Precision, recall, and F1 use the existing repository scorers and the existing ground truths. The experiment does not overwrite the prior `_gemma-2` response or score files.

To run another permanent repeat and compare it with the first run:

```bash
.venv/bin/python scripts/run_gemma_experiments_gemma-2.py \
  --model gemma2:latest \
  --trials 10 \
  --temperature 0.7 \
  --output gemma-2_run2/runs \
  --response-root gemma-2_run2/responses

.venv/bin/python scripts/compare_gemma_runs_gemma-2.py \
  gemma-2_run1/runs \
  gemma-2_run2/runs \
  --output gemma-2_run2/comparison
```
