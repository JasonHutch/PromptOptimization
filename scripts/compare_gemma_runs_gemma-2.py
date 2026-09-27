#!/usr/bin/env python3
"""Compare two completed Gemma experiment directories."""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import statistics


def read_rows(path: pathlib.Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def aggregate(rows: list[dict]) -> list[dict]:
    groups = {}
    for row in rows:
        key = tuple(row[k] for k in ("strategy", "activity", "domain"))
        groups.setdefault(key, []).append(row)
    result = []
    for key, values in sorted(groups.items()):
        f1 = [float(row["f1"]) * 100 for row in values]
        precision = [float(row["precision"]) * 100 for row in values]
        recall = [float(row["recall"]) * 100 for row in values]
        result.append({
            "strategy": key[0],
            "activity": key[1],
            "domain": key[2],
            "trials": len(values),
            "mean_precision": statistics.mean(precision),
            "mean_recall": statistics.mean(recall),
            "mean_f1": statistics.mean(f1),
            "stdev_f1": statistics.stdev(f1) if len(f1) > 1 else 0.0,
            "trial1_f1": f1[0],
            "trial10_f1": f1[-1],
        })
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("first_run")
    parser.add_argument("second_run")
    parser.add_argument("--output", default="temp_run2_output/comparison")
    args = parser.parse_args()

    first = aggregate(read_rows(pathlib.Path(args.first_run) / "trial_summary.csv"))
    second = aggregate(read_rows(pathlib.Path(args.second_run) / "trial_summary.csv"))
    first_by_key = {(r["strategy"], r["activity"], r["domain"]): r for r in first}
    second_by_key = {(r["strategy"], r["activity"], r["domain"]): r for r in second}
    comparison = []
    for key in sorted(first_by_key.keys() | second_by_key.keys()):
        a, b = first_by_key.get(key), second_by_key.get(key)
        row = {"strategy": key[0], "activity": key[1], "domain": key[2]}
        for label, source in (("run1", a), ("run2", b)):
            row[f"{label}_trials"] = source["trials"] if source else 0
            row[f"{label}_mean_precision"] = source["mean_precision"] if source else None
            row[f"{label}_mean_recall"] = source["mean_recall"] if source else None
            row[f"{label}_mean_f1"] = source["mean_f1"] if source else None
            row[f"{label}_stdev_f1"] = source["stdev_f1"] if source else None
            row[f"{label}_trial1_f1"] = source["trial1_f1"] if source else None
            row[f"{label}_trial10_f1"] = source["trial10_f1"] if source else None
        row["delta_mean_f1"] = (
            row["run2_mean_f1"] - row["run1_mean_f1"]
            if row["run1_mean_f1"] is not None and row["run2_mean_f1"] is not None
            else None
        )
        comparison.append(row)

    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "comparison.json").write_text(json.dumps(comparison, indent=2), encoding="utf-8")
    with (output / "comparison.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=comparison[0].keys())
        writer.writeheader()
        writer.writerows(comparison)
    print(f"wrote {len(comparison)} comparisons to {output}")


if __name__ == "__main__":
    main()
