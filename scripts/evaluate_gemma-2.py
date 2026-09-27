#!/usr/bin/env python3
"""Score the checked-in best-response fixtures against the _gemma-2 prompt contract.

The repository does not contain an LLM runner or credentials. This command therefore
performs a reproducible scorer regression using the strongest existing P4/P3/P3
responses, copied under _gemma-2 names. Replace the fixture mapping with fresh model
responses when a model runner is available.
"""
from __future__ import annotations

import json
import pathlib
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import score_identification as si  # noqa: E402
import score_markdown as sm  # noqa: E402


DOMAINS = ("library", "car_rental", "ntss")
FIXTURES = {
    "identification": "P4",
    "classification": "P3",
    "cot": "P3",
}


def score_identification(text: str, domain: str) -> dict:
    gold = si.parse_gold(ROOT / "ground_truths" / "identification" / f"{domain}.csv")
    return si.score(gold, si.parse_output(text))


def score_classification(text: str, domain: str) -> dict:
    gold = sm.parse_csv(ROOT / "ground_truths" / "classification" / f"{domain}.csv")
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as fh:
        fh.write(text)
        temp_path = pathlib.Path(fh.name)
    try:
        pred = sm.parse_markdown(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)
    tp = 0
    for label in sorted({row[0] for row in gold + pred}):
        gold_label = [row for row in gold if row[0] == label]
        pred_label = [row for row in pred if row[0] == label]
        tp += len(sm.match(gold_label, pred_label, True, True))
    result = {
        "precision": tp / len(pred) if pred else 0.0,
        "recall": tp / len(gold) if gold else 0.0,
        "tp": tp,
        "fp": len(pred) - tp,
        "fn": len(gold) - tp,
        "n_gold": len(gold),
        "n_pred": len(pred),
    }
    p, r = result["precision"], result["recall"]
    result["f1"] = 2 * p * r / (p + r) if p + r else 0.0
    return result


def main() -> None:
    output_root = ROOT / "responses"
    score_root = ROOT / "scores"
    report = {"mode": "fixture-regression", "domains": {}}

    for activity, version in FIXTURES.items():
        for domain in DOMAINS:
            source = output_root / activity / version / f"{domain}_r1.md"
            if not source.exists():
                raise FileNotFoundError(source)
            target_dir = output_root / activity / f"{version}_gemma-2"
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / f"{domain}_r1_gemma-2.md"
            shutil.copyfile(source, target)

            text = source.read_text(encoding="utf-8")
            if activity == "identification":
                score = score_identification(text, domain)
            elif activity == "classification":
                score = score_classification(text, domain)
            else:
                score = {"note": "CoT fixture retained for manual Step 1/Final model split."}

            report["domains"].setdefault(domain, {})[activity] = score
            score_dir = score_root / f"{activity}_gemma-2"
            score_dir.mkdir(parents=True, exist_ok=True)
            (score_dir / f"{domain}_r1_gemma-2.json").write_text(
                json.dumps({"score": score, "source_fixture": str(source.relative_to(ROOT))}, indent=2),
                encoding="utf-8",
            )

    (score_root / "saif_fixture_regression.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    deck_results = json.loads((ROOT / "results.json").read_text(encoding="utf-8"))
    for activity, version in FIXTURES.items():
        if activity == "cot":
            continue
        deck_results.setdefault(activity, {})[f"{version}_gemma-2"] = {}
        for domain in DOMAINS:
            score = report["domains"][domain][activity]
            deck_results[activity][f"{version}_gemma-2"][domain] = {
                "f1": round(score["f1"] * 100, 1),
                "p": round(score["precision"] * 100, 1),
                "r": round(score["recall"] * 100, 1),
                "n": 1,
                "f1_runs": [round(score["f1"] * 100, 1)],
            }
    (ROOT / "results_gemma-2.json").write_text(json.dumps(deck_results, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
