# Project Structure
----------
- ground_truths - used Claude to structure ground truth files into consitently structured CSV files to make it easier to run evals
- notebooks - sanbox for tinkering with langchain / langgraph
- prompts - Location to store prompt variations, organized by prompting strategy
- scripts - home for eval scripts. Used Claude to generate the first one. Still need to test and review

# Prompt Optimization Output
----------
Each optimizer trial `tN` (under `prompts/auto_prompt_evo/<task>/tN/`) produces:
- `lib.csv`, `rental.csv`, `ntss.csv` - the model's responses for the three domains
- `scorecard.md` - per-domain precision / recall / F1 (plus TP/FP/FN) with an average row
- `prompt.md` - the refined prompt produced by that trial
- `changelog.md` - a change log describing the enhancements made in that trial (what changed and which observed error/metric it addresses). Trials from t1 onward only; the optimizer is asked to emit this in a ` ```changelog ` fenced block, which is parsed and saved by the graph's checkpoint step.

# Optimization Strategy
----------
What the optimizer focuses on during the optimization step is controlled per run by the `optimization_strategy` state key (set `STRATEGY` in the notebook; it flows into the graph via `inputs`). Allowed values are defined by the `OptimizationStrategy` enum in `src/models/OptimizationStrategy.py`:
- `OptimizationStrategy.META_PROMPTING` (`'meta_prompting'`) - treat the prompt itself as the object of analysis: build an error taxonomy from the FP/FN rows, rewrite the offending definitions, and codify the ground truths' output conventions in the prompt
- `OptimizationStrategy.FEW_SHOT_PROMPTING` (`'few_shot_prompting'`) - embed canonical input/output examples drawn from the observed mismatches
- `OptimizationStrategy.DECISION_RUBRIC` (`'decision_rubric'`) - rewrite the labels as a mutually exclusive, ordered decision procedure with explicit tie-breakers for observed confusions
- `OptimizationStrategy.NONE` (`'none'`, also the default) - no focus; the optimizer improves the prompt generically

Enum members or their string values are both accepted; anything else raises a `ValueError` before any model call. The active strategy is printed by the `optimize` node each trial and recorded at the bottom of each trial's `scorecard.md`.
