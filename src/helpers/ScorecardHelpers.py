def build_scorecard(trial: int, lib: dict, rental: dict, ntss: dict,
                    strategy: str | None = None) -> str:
    """
    Builds a markdown scorecard for a single trial showing precision, recall,
    F1 and TP/FP/FN per dataset, plus a summary row (metrics macro-averaged,
    counts summed across the three datasets). `strategy` is the resolved
    optimizer strategy label, shown at the bottom when provided.
    """
    datasets = [("library", lib), ("rental", rental), ("ntss", ntss)]

    def row(name, s):
        return (f"| {name} | {s.get('precision', 0):.3f} | {s.get('recall', 0):.3f} | "
                f"{s.get('f1', 0):.3f} | {s.get('TP', 0)} | {s.get('FP', 0)} | {s.get('FN', 0)} |")

    avg = {k: sum(s.get(k, 0) for _, s in datasets) / len(datasets)
           for k in ("precision", "recall", "f1")}
    total = {k: sum(s.get(k, 0) for _, s in datasets) for k in ("TP", "FP", "FN")}

    lines = [
        f"# Scorecard (trial {trial})",
        "",
        "| Dataset | Precision | Recall | F1 | TP | FP | FN |",
        "|---|---|---|---|---|---|---|",
        *[row(name, s) for name, s in datasets],
        row("**average**", {**avg, **total}),
        "",
        "Precision, recall and F1 are macro-averaged across the three datasets; "
        "TP/FP/FN are summed.",
    ]
    if strategy:
        lines += ["", f"*Optimizer strategy: {strategy}*"]
    return "\n".join(lines) + "\n"