#!/usr/bin/env python3
"""Offline evaluation of element-level voting on repeated identification runs -> research.json

    python research_eval.py runs_export/     (exported run JSON documents)
"""
import json, glob, sys, statistics, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import score_identification as SI, vote as V
ROOT = pathlib.Path(__file__).resolve().parent.parent
runs = {}
for f in glob.glob(str(pathlib.Path(sys.argv[1]) / "identification-*.json")):
    d = json.load(open(f))
    if d.get("status") == "done" and d.get("response") and "max" not in d["prompt_id"]:
        runs.setdefault((d["version"], d["domain"]), []).append(d["response"])
out = []
for (ver, dom), texts in sorted(runs.items()):
    if len(texts) < 2:
        continue
    gold = SI.parse_gold(ROOT / "ground_truths" / "identification" / f"{dom}.csv")
    single = statistics.mean(SI.score(gold, SI.parse_output(t))["f1"] for t in texts)
    votes = {k: SI.score(gold, V.vote(texts, k)) for k in range(1, len(texts) + 1)}
    bk = max(votes, key=lambda k: votes[k]["f1"])
    out.append({"version": ver, "domain": dom, "n": len(texts), "single_f1": round(100 * single, 1),
                "best_k": bk, "vote_f1": round(100 * votes[bk]["f1"], 1),
                "vote_p": round(100 * votes[bk]["precision"], 1), "vote_r": round(100 * votes[bk]["recall"], 1)})
json.dump({"voting": out}, open(ROOT / "research.json", "w"), indent=1)
for r in out: print(r)
