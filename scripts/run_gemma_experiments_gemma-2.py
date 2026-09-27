#!/usr/bin/env python3
"""Run the complete local Gemma prompt experiment.

The experiment records every rendered prompt, response, model setting, and score
input. It runs 10 trials for each strategy, domain, and task, then writes a
machine-readable summary with trial-1 versus trial-10 comparisons.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from score_runs import score_cls, score_id  # noqa: E402

DOMAINS = ("car_rental", "library", "ntss")
STRATEGIES = ("baseline", "cot", "meta", "few_shot")
ACTIVITIES = ("identification", "classification")


def ollama(model: str, prompt: str, temperature: float) -> tuple[str, dict]:
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }).encode()
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    started = time.time()
    with urllib.request.urlopen(req, timeout=900) as response:
        data = json.load(response)
    text = data.get("response", "")
    if not text:
        raise RuntimeError(f"Ollama returned no response: {data}")
    return text, {
        "elapsed_seconds": round(time.time() - started, 3),
        "prompt_eval_count": data.get("prompt_eval_count"),
        "eval_count": data.get("eval_count"),
        "total_duration_ns": data.get("total_duration"),
    }


def load_prompt(activity: str, strategy: str) -> str:
    if strategy == "baseline":
        name = "P0.md"
    elif activity == "identification":
        name = "P6_gemma-2.md"
    else:
        name = "P5_gemma-2.md"
    return (ROOT / "prompts" / activity / name).read_text(encoding="utf-8")


def strategy_suffix(strategy: str, activity: str) -> str:
    if strategy == "cot":
        return (
            "\n\nExecution instruction: reason through the task in numbered steps "
            "privately, then return only the required output table. Never output reasoning.\n"
        )
    if strategy == "meta":
        return (
            "\n\nBefore finalizing, privately audit coverage, precision, duplicates, and "
            "format compliance. Correct your draft, then return only the required table.\n"
        )
    if strategy == "few_shot":
        if activity == "identification":
            return (
                "\n\nNeutral examples:\n"
                "- 'a clinic schedules appointments' -> rule 1: clinic; rule 1: appointments; "
                "rule 3: schedules\n"
                "- 'an appointment has a date' -> rule 1: appointment; rule 1: date; "
                "rule 6: has a date\n"
                "Do not copy these examples into the answer.\n"
            )
        return (
            "\n\nNeutral example: Customer places Order -> "
            "AS | places | customer | order; order has a total -> "
            "A | total | order. Do not copy this example into the answer.\n"
        )
    return ""


def render(template: str, description: str, phrases: str = "", strategy: str = "", activity: str = "") -> str:
    return (
        template.replace("{{DESCRIPTION}}", description)
        .replace("{{PHRASES}}", phrases)
        + strategy_suffix(strategy, activity)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gemma2:latest")
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--strategies", nargs="+", choices=STRATEGIES, default=list(STRATEGIES))
    parser.add_argument("--output", default="gemma-2_run1/runs")
    parser.add_argument("--response-root", default="gemma-2_run1/responses")
    args = parser.parse_args()

    out = ROOT / args.output
    response_root = ROOT / args.response_root
    out.mkdir(parents=True, exist_ok=True)
    (out / "logs").mkdir(exist_ok=True)
    manifest = {
        "model": args.model,
        "trials": args.trials,
        "temperature": args.temperature,
        "response_root": args.response_root,
        "strategies": args.strategies,
        "domains": DOMAINS,
        "activities": ACTIVITIES,
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    rows = []

    for strategy in args.strategies:
        for domain in DOMAINS:
            description = (ROOT / f"inputs/descriptions/{domain}.txt").read_text(encoding="utf-8")
            id_template = load_prompt("identification", strategy)
            for trial in range(1, args.trials + 1):
                id_prompt = render(id_template, description, strategy=strategy, activity="identification")
                id_text, usage = ollama(args.model, id_prompt, args.temperature)
                ident_path = response_root / strategy / "identification" / f"{domain}_trial{trial:02d}_gemma-2.md"
                ident_path.parent.mkdir(parents=True, exist_ok=True)
                ident_path.write_text(id_text, encoding="utf-8")
                ident_score = score_id(id_text, domain)
                log = {
                    "strategy": strategy, "activity": "identification", "domain": domain,
                    "trial": trial, "model": args.model, "temperature": args.temperature,
                    "prompt_sha256": hashlib.sha256(id_prompt.encode()).hexdigest(),
                    "prompt_path": str((ROOT / "prompts" / "identification" / ("P0.md" if strategy == "baseline" else "P6_gemma-2.md")).relative_to(ROOT)),
                    "response_path": str(ident_path.relative_to(ROOT)),
                    "score": ident_score, "usage": usage,
                }
                (out / "logs" / f"{strategy}_{domain}_trial{trial:02d}_identification.json").write_text(
                    json.dumps(log, indent=2), encoding="utf-8"
                )
                rows.append(log)

                cls_template = load_prompt("classification", strategy)
                cls_prompt = render(
                    cls_template, description, id_text, strategy=strategy, activity="classification"
                )
                cls_text, usage = ollama(args.model, cls_prompt, args.temperature)
                cls_path = response_root / strategy / "classification" / f"{domain}_trial{trial:02d}_gemma-2.md"
                cls_path.parent.mkdir(parents=True, exist_ok=True)
                cls_path.write_text(cls_text, encoding="utf-8")
                cls_score = score_cls(cls_text, domain)
                log = {
                    "strategy": strategy, "activity": "classification", "domain": domain,
                    "trial": trial, "model": args.model, "temperature": args.temperature,
                    "prompt_sha256": hashlib.sha256(cls_prompt.encode()).hexdigest(),
                    "prompt_path": str((ROOT / "prompts" / "classification" / ("P0.md" if strategy == "baseline" else "P5_gemma-2.md")).relative_to(ROOT)),
                    "response_path": str(cls_path.relative_to(ROOT)),
                    "score": cls_score, "usage": usage,
                }
                (out / "logs" / f"{strategy}_{domain}_trial{trial:02d}_classification.json").write_text(
                    json.dumps(log, indent=2), encoding="utf-8"
                )
                rows.append(log)
                print(f"{strategy} {domain} trial {trial}/{args.trials}")

    with (out / "all_runs.jsonl").open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row) + "\n")
    with (out / "trial_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["strategy", "activity", "domain", "trial", "precision", "recall", "f1", "tp", "fp", "fn"])
        for row in rows:
            s = row["score"]
            writer.writerow([row["strategy"], row["activity"], row["domain"], row["trial"],
                             s["precision"], s["recall"], s["f1"], s["tp"], s["fp"], s["fn"]])
    comparison = []
    for strategy in args.strategies:
        for activity in ACTIVITIES:
            for domain in DOMAINS:
                selected = [r for r in rows if r["strategy"] == strategy and r["activity"] == activity and r["domain"] == domain]
                for trial in (1, args.trials):
                    score = next(r["score"] for r in selected if r["trial"] == trial)
                    comparison.append({
                        "strategy": strategy, "activity": activity, "domain": domain,
                        "trial": trial, "precision": score["precision"],
                        "recall": score["recall"], "f1": score["f1"],
                    })
    (out / "trial_1_vs_trial_10.json").write_text(json.dumps(comparison, indent=2), encoding="utf-8")
    print(f"wrote {len(rows)} scored runs to {out}")


if __name__ == "__main__":
    main()
