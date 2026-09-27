#!/usr/bin/env python3
"""Run the _gemma-2 prompts against a local Ollama model and score the responses."""

from __future__ import annotations

import argparse
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOMAINS = ("library", "car_rental", "ntss")


def call_ollama(model: str, prompt: str) -> str:
    payload = json.dumps(
        {"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0}}
    ).encode()
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=900) as response:
        data = json.load(response)
    if not data.get("response"):
        raise RuntimeError(f"Ollama returned no response: {data}")
    return data["response"]


def render(path: pathlib.Path, description: str, phrases: str = "") -> str:
    text = path.read_text(encoding="utf-8")
    return text.replace("{{DESCRIPTION}}", description).replace("{{PHRASES}}", phrases)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="llama3:8b")
    args = parser.parse_args()

    id_prompt = ROOT / "prompts/identification/P6_gemma-2.md"
    cls_prompt = ROOT / "prompts/classification/P5_gemma-2.md"
    cot_prompt = ROOT / "prompts/cot/P4_gemma-2.md"
    for domain in DOMAINS:
        description = (ROOT / f"inputs/descriptions/{domain}.txt").read_text(encoding="utf-8")
        id_text = call_ollama(args.model, render(id_prompt, description))
        id_path = ROOT / f"responses/identification/P6_gemma-2/{domain}_r1_gemma-2.md"
        id_path.parent.mkdir(parents=True, exist_ok=True)
        id_path.write_text(id_text, encoding="utf-8")

        cls_text = call_ollama(args.model, render(cls_prompt, description, id_text))
        cls_path = ROOT / f"responses/classification/P5_gemma-2/{domain}_r1_gemma-2.md"
        cls_path.parent.mkdir(parents=True, exist_ok=True)
        cls_path.write_text(cls_text, encoding="utf-8")

        cot_text = call_ollama(args.model, render(cot_prompt, description))
        cot_path = ROOT / f"responses/cot/P4_gemma-2/{domain}_r1_gemma-2.md"
        cot_path.parent.mkdir(parents=True, exist_ok=True)
        cot_path.write_text(cot_text, encoding="utf-8")
        print(f"completed {domain}")


if __name__ == "__main__":
    main()
