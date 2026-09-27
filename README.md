# Project Structure
----------
- `ground_truths/` - ground truth files restructured into consistently structured CSVs (with Claude's help) to make evals easy to run, split by task (`classification/`, `identification/`)
- `inputs/` - the raw task inputs: text descriptions of the three domains (car rental, library, NTSS) that the prompts are run against
- `notebooks/` - sandbox for tinkering with langchain / langgraph; home of the classification and identification self-prompt-optimization notebooks
- `prompts/` - prompt variations organized by prompting strategy
- `optimized_prompts/` - the final optimized prompts, organized by strategy (`meta_prompting/`, `few_shot/`, `no_strategy`) and task
- `src/` - the reusable code behind the notebooks: langgraph `graphs/` (`ClassificationGraph`, `IdentificationGraph`), `helpers/` for parsing and scoring, and `models/` for the graph state and the `OptimizationStrategy` enum
- `submission/` - final deliverables for the assignment

# Branches
----------
- `main` - the workflow documented above
- `gemma_addition_on_oscars` - **contains an additional prompt optimization workflow** alongside the ones here

# Running the Notebooks
----------
1. **Install dependencies** with `uv sync` (Python 3.12+; installs langchain, langgraph, langchain-ollama, langchain-anthropic, pandas, ipykernel), then select the project's `.venv` as the notebook kernel.
2. **Set the optimization strategy** in the `STRATEGY` cell near the top of each notebook:
   ```python
   STRATEGY = OptimizationStrategy.META_PROMPTING
   ```
   Allowed values come from the `OptimizationStrategy` enum in `src/models/OptimizationStrategy.py`: `META_PROMPTING`, `FEW_SHOT_PROMPTING`, `DECISION_RUBRIC`, or `NONE` (the default). Enum members or their string values are both accepted; anything else raises a `ValueError` before any model call. The strategy flows into the graph via `inputs["optimization_strategy"]`, is printed by the `optimize` node each trial, and is recorded at the bottom of each trial's `scorecard.md`.
3. **Run the notebook cells top to bottom.** Both notebooks use relative paths and expect to be run from inside `notebooks/`:
   - `notebooks/classification_prompt_optimization.ipynb` (classification) - builds the `ClassificationGraph` with the domain phrases and `ground_truths/classification/` CSVs, seeded from `prompts/auto_prompt_evo/classification/t0/prompt.md`
   - `notebooks/identification_self_prompt_optimization.ipynb` (identification) - builds the `IdentificationGraph` with the domain descriptions from `inputs/descriptions/` and `ground_truths/identification/` CSVs, seeded from `prompts/auto_prompt_evo/identification/t0/prompt.md`

Both notebooks run `MAX_TRIALS = 10` trials on `gemma4:31b-cloud` via Ollama (temperature 0), so Ollama needs to be up and the model pulled. Outputs land in `prompts/auto_prompt_evo/` (see below).

# Notebook Outputs (prompts/auto_prompt_evo)
----------
**This is where the outputs of the classification and identification notebooks get written.** Each optimizer run saves a trial folder per task (`classification/t0/`, `identification/t1/`, ...). Each trial `tN` contains:
- `lib.csv`, `rental.csv`, `ntss.csv` - the model's responses for the three domains
- `scorecard.md` - per-domain precision / recall / F1 (plus TP/FP/FN) with an average row
- `prompt.md` - the refined prompt produced by that trial
- `changelog.md` - what changed in that trial and which observed error/metric it addresses (emitted by the optimizer in a ` ```changelog ` fenced block, parsed and saved by the graph's checkpoint step)