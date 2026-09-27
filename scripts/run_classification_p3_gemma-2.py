#!/usr/bin/env python3
"""Run the repository P3 classification prompt with Gemma 2."""

from __future__ import annotations

import argparse
import json
import pathlib
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOMAINS = ("library", "car_rental", "ntss")

import sys
sys.path.insert(0, str(ROOT / "scripts"))
from score_runs import score_cls  # noqa: E402


def call(model: str, prompt: str, temperature: float) -> tuple[str, dict]:
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }).encode()
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    started = time.time()
    with urllib.request.urlopen(request, timeout=900) as response:
        result = json.load(response)
    if not result.get("response"):
        raise RuntimeError(f"Ollama returned no response: {result}")
    return result["response"], {
        "elapsed_seconds": round(time.time() - started, 3),
        "prompt_eval_count": result.get("prompt_eval_count"),
        "eval_count": result.get("eval_count"),
        "total_duration_ns": result.get("total_duration"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gemma2:latest")
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--output", default="gemma-2_run3/p3_classification")
    args = parser.parse_args()

    prompt_path = ROOT / "prompts/classification/P3.md"
    output = ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    rows = []

    for domain in DOMAINS:
        description = (ROOT / f"inputs/descriptions/{domain}.txt").read_text(encoding="utf-8")
        phrases = (ROOT / f"inputs/phrases/{domain}.md").read_text(encoding="utf-8")
        template = prompt_path.read_text(encoding="utf-8")
        prompt = template.replace("{{DESCRIPTION}}", description).replace("{{PHRASES}}", phrases)

        for trial in range(1, args.trials + 1):
            text, usage = call(args.model, prompt, args.temperature)
            response_path = output / f"{domain}_trial{trial:02d}_P3_gemma-2.md"
            response_path.write_text(text, encoding="utf-8")
            score = score_cls(text, domain)
            row = {
                "model": args.model,
                "prompt": "prompts/classification/P3.md",
                "domain": domain,
                "trial": trial,
                "temperature": args.temperature,
                "response": str(response_path.relative_to(ROOT)),
                "score": score,
                "usage": usage,
            }
            (output / f"{domain}_trial{trial:02d}_P3_gemma-2.json").write_text(
                json.dumps(row, indent=2), encoding="utf-8"
            )
            rows.append(row)
            print(f"P3 classification {domain} trial {trial}/{args.trials}", flush=True)

    (output / "summary.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
