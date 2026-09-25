import re

def extract_prompt(text: str) -> str:
    """
    Returns the contents of the first ```markdown (or plain ```) fenced block
    in an optimizer response. Falls back to the whole text if no fence is found.
    """
    m = re.search(r"```(?:markdown|md)?[ \t]*\n(.*?)\n```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return text.strip()

def build_eval_prompt(state: dict, truths) -> str:
    """
    Constructs a prompt for the optimizer to improve the current prompt
    by providing results and ground truths for error analysis.
    """
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
        "Output requirements (strict):\n"
        "- Return ONLY the new prompt, inside a single ```markdown fenced code block.\n"
        "- Do not include any analysis, commentary, or text outside the fence.\n"
        "- The new prompt MUST preserve the literal placeholder `<DOMAIN PHRASES>` exactly, "
        "where the domain phrases will be substituted.\n"
        "- The new prompt must still instruct the model to output raw CSV text with the "
        "header `label,element,arg1,arg2` and nothing else (no markdown, no code fences)."
    )


def build_identification_eval_prompt(state: dict, truths) -> str:
    """
    Constructs a prompt for the optimizer to improve the current identification
    prompt by providing results and ground truths for error analysis.
    """
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
        "Output requirements (strict):\n"
        "- Return ONLY the new prompt, inside a single ```markdown fenced code block.\n"
        "- Do not include any analysis, commentary, or text outside the fence.\n"
        "- The new prompt MUST preserve the literal placeholder `<DESCRIPTION>` exactly, "
        "where the business description will be substituted.\n"
        "- The new prompt must still instruct the model to output raw CSV text with the "
        "header `rule,phrase` and nothing else (no markdown, no code fences)."
    )