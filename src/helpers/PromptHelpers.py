import re

from src.models.OptimizationStrategy import OptimizationStrategy

def extract_prompt(text: str) -> str:
    """
    Returns the contents of the first ```markdown (or plain ```) fenced block
    in an optimizer response. Falls back to the whole text if no fence is found.
    """
    m = re.search(r"```(?:markdown|md)?[ \t]*\n(.*?)\n```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return text.strip()

def extract_changelog(text: str) -> str:
    """
    Returns the contents of the first ```changelog fenced block in an optimizer
    response. Falls back to an empty string if no changelog fence is found.
    """
    m = re.search(r"```changelog[ \t]*\n(.*?)\n```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


# Focus instruction injected into the optimizer prompt for each strategy.
# NONE maps to no instruction: the optimizer improves the prompt generically.
OPTIMIZATION_STRATEGY_FOCUS = {
    OptimizationStrategy.META_PROMPTING:
        "Treat the current prompt itself as the object of analysis. First build a concise "
        "error taxonomy from the FP and FN rows (which label confusions and which "
        "output-convention mismatches dominate), then rewrite the offending definitions "
        "and instructions so the downstream model resolves them. Also mine the ground "
        "truths for output conventions (singular/lowercase elements, dropped articles, "
        "arg1/arg2 slot assignment) and codify them explicitly in the prompt's output "
        "spec. Do not add worked examples; improve the instructions themselves.",
    OptimizationStrategy.FEW_SHOT_PROMPTING:
        "Teach by example. Pick the most informative prediction/ground-truth mismatches "
        "and embed a small set of canonical few-shot examples in the prompt (input -> "
        "expected output_trial row), each illustrating a distinct observed error pattern. "
        "Keep the set minimal and place each example next to the rule it reinforces.",
    OptimizationStrategy.DECISION_RUBRIC:
        "Rewrite the label definitions as a mutually exclusive, ordered decision "
        "procedure. Replace flat per-label descriptions with a single checklist the "
        "downstream model applies in order (first matching test wins), with explicit "
        "tie-breakers for the confusions seen in the FP rows. Each predicted row must "
        "be assignable by exactly one first-matching test; remove any overlapping "
        "guidance that lets a phrase qualify under more than one label. Do not rely on "
        "worked examples; the decision procedure itself is the teaching device.",
}


def resolve_strategy(strategy) -> tuple[str, str | None]:
    """
    Coerces a strategy argument into (label, focus instruction). Accepts an
    OptimizationStrategy member, one of its string values, or None (= NONE).
    Raises ValueError for anything else. NONE yields no focus instruction.
    """
    if strategy is None:
        strategy = OptimizationStrategy.NONE
    if isinstance(strategy, OptimizationStrategy):
        s = strategy
    else:
        try:
            s = OptimizationStrategy(strategy)
        except ValueError:
            valid = ", ".join(f"'{m.value}'" for m in OptimizationStrategy)
            raise ValueError(
                f"Unknown optimization strategy: {strategy!r}. "
                f"Valid options: {valid} (or None)."
            ) from None
    return s.value, OPTIMIZATION_STRATEGY_FOCUS.get(s)

def build_eval_prompt(state: dict, truths, strategy=None) -> str:
    """
    Constructs a prompt for the optimizer to improve the current prompt
    by providing results and ground truths for error analysis.
    `strategy` is an OptimizationStrategy member, one of its string values,
    or None (= NONE, no focus section).
    """
    strategy_name, strategy_focus = resolve_strategy(strategy)
    focus_block = ""
    if strategy_focus:
        focus_block = (f"Optimization focus - apply the '{strategy_name}' strategy: "
                       f"{strategy_focus}\n\n")
    # These variables should be defined in your notebook's global scope (e.g., via pd.read_csv)
    ground_truths = {
        'library': truths["lib_truth"],
        'rental': truths["rent_truth"],
        'ntss': truths["ntss_truth"]
    }
    evals = {
        'library': state['lib_eval'],
        'rental': state['rental_eval'],
        'ntss': state['ntss_eval'],
    }

    def get_text(data):
        resp = data.get("response", "")
        return resp.content if hasattr(resp, 'content') else str(resp)

    sections = []
    for name in ('library', 'rental', 'ntss'):
        ev = evals[name]
        metrics = ", ".join(
            f"{k}={ev.get(k, 0):.3f}" if k in ('precision', 'recall', 'f1') else f"{k}={ev.get(k, 0)}"
            for k in ('precision', 'recall', 'f1', 'TP', 'FP', 'FN')
        )
        sections.append(
            f"### Dataset: {name}\n"
            f"Metrics: {metrics}\n\n"
            f"Model response (CSV):\n{get_text(ev)}\n\n"
            f"Ground truth (CSV):\n{ground_truths[name].to_csv(index=False)}"
        )

    return (
        "You are optimizing a prompt used to extract a software schema table "
        "(label, element, arg1, arg2) from domain phrases.\n\n"
        "## Current Prompt\n"
        "```markdown\n"
        f"{state['current_prompt']}\n"
        "```\n\n"
        "## Evaluation Results\n"
        "Scoring is exact-match on the full (label, element, arg1, arg2) row, case-insensitive. "
        "TP = predicted rows found in ground truth, FP = predicted rows not in ground truth, "
        "FN = ground-truth rows the model missed.\n\n"
        + "\n\n".join(sections) +
        "\n\n## Instructions\n"
        "Analyze where the predictions went wrong relative to the ground truths and write an "
        "improved version of the prompt to increase the F1 score.\n\n"
        + focus_block +
        "Output requirements (strict):\n"
        "- First, return the new prompt inside a single ```markdown fenced code block.\n"
        "- Immediately after it, return a change log inside a single ```changelog fenced "
        "code block describing the enhancements made relative to the current prompt. For "
        "each change, use one bullet point stating what was changed and which observed "
        "error or metric it addresses.\n"
        "- Do not include any analysis, commentary, or text outside these two fences.\n"
        "- The new prompt MUST preserve the literal placeholder `<DOMAIN PHRASES>` exactly, "
        "where the domain phrases will be substituted.\n"
        "- The new prompt must still instruct the model to output_trial raw CSV text with the "
        "header `label,element,arg1,arg2` and nothing else (no markdown, no code fences)."
    )


def build_identification_eval_prompt(state: dict, truths, strategy=None) -> str:
    """
    Constructs a prompt for the optimizer to improve the current identification
    prompt by providing results and ground truths for error analysis.
    `strategy` is an OptimizationStrategy member, one of its string values,
    or None (= NONE, no focus section).
    """
    strategy_name, strategy_focus = resolve_strategy(strategy)
    focus_block = ""
    if strategy_focus:
        focus_block = (f"Optimization focus - apply the '{strategy_name}' strategy: "
                       f"{strategy_focus}\n\n")
    ground_truths = {
        'library': truths["lib_truth"],
        'rental': truths["rent_truth"],
        'ntss': truths["ntss_truth"]
    }
    evals = {
        'library': state['lib_eval'],
        'rental': state['rental_eval'],
        'ntss': state['ntss_eval'],
    }

    def get_text(data):
        resp = data.get("response", "")
        return resp.content if hasattr(resp, 'content') else str(resp)

    sections = []
    for name in ('library', 'rental', 'ntss'):
        ev = evals[name]
        metrics = ", ".join(
            f"{k}={ev.get(k, 0):.3f}" if k in ('precision', 'recall', 'f1') else f"{k}={ev.get(k, 0)}"
            for k in ('precision', 'recall', 'f1', 'TP', 'FP', 'FN')
        )
        sections.append(
            f"### Dataset: {name}\n"
            f"Metrics: {metrics}\n\n"
            f"Model response (CSV):\n{get_text(ev)}\n\n"
            f"Ground truth (CSV):\n{ground_truths[name].to_csv(index=False)}"
        )

    return (
        "You are optimizing a prompt used to identify the domain-specific phrases "
        "(rule, phrase) in a business description.\n\n"
        "## Current Prompt\n"
        "```markdown\n"
        f"{state['current_prompt']}\n"
        "```\n\n"
        "## Evaluation Results\n"
        "Scoring matches a predicted (rule, phrase) row to a ground-truth row when the "
        "rule numbers agree and the phrases are equal after normalization (lowercase, "
        "punctuation and markdown ignored, articles dropped, singular/plural and verb "
        "inflections stemmed). A ground-truth phrase may list accepted alternates "
        "separated by ' / '; matching any alternate counts. TP = ground-truth rows "
        "matched, FP = predicted rows that matched nothing, FN = ground-truth rows "
        "missed.\n\n"
        + "\n\n".join(sections) +
        "\n\n## Instructions\n"
        "Analyze where the predictions went wrong relative to the ground truths and "
        "write an improved version of the prompt to increase the F1 score.\n\n"
        + focus_block +
        "Output requirements (strict):\n"
        "- First, return the new prompt inside a single ```markdown fenced code block.\n"
        "- Immediately after it, return a change log inside a single ```changelog fenced "
        "code block describing the enhancements made relative to the current prompt. For "
        "each change, use one bullet point stating what was changed and which observed "
        "error or metric it addresses.\n"
        "- Do not include any analysis, commentary, or text outside these two fences.\n"
        "- The new prompt MUST preserve the literal placeholder `<DESCRIPTION>` exactly, "
        "where the business description will be substituted.\n"
        "- The new prompt must still instruct the model to output_trial raw CSV text with the "
        "header `rule,phrase` and nothing else (no markdown, no code fences)."
    )