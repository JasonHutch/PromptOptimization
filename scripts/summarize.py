#!/usr/bin/env python3
"""Aggregate every scored run in scores/ into results.json (mean over runs per cell).

    python summarize.py            # reads ../scores, writes ../results.json
"""
import json, glob, os, collections, pathlib, statistics
ROOT = pathlib.Path(__file__).resolve().parent.parent
cells = collections.defaultdict(list)
for f in glob.glob(str(ROOT / "scores" / "*.json")):
    rid = os.path.basename(f)[:-5]
    pid, dom, n = rid.split("__")
    act, ver = pid.split("-")
    s = json.load(open(f))["score"]
    if act == "cot":
        if not s.get("classification"):
            continue
        rec = {"f1": s["classification"]["f1"], "p": s["classification"]["precision"],
               "r": s["classification"]["recall"], "step1_f1": s["identification"]["f1"]}
    else:
        rec = {"f1": s["f1"], "p": s["precision"], "r": s["recall"]}
    cells[(act, ver, dom)].append(rec)
out = {}
for (act, ver, dom), runs in sorted(cells.items()):
    m = lambda k: round(100 * statistics.mean(r[k] for r in runs), 1)
    d = {"f1": m("f1"), "p": m("p"), "r": m("r"), "n": len(runs),
         "f1_runs": [round(100 * r["f1"], 1) for r in runs]}
    if act == "cot":
        d["step1_f1"] = m("step1_f1")
    out.setdefault(act, {}).setdefault(ver, {})[dom] = d
json.dump(out, open(ROOT / "results.json", "w"), indent=1)
for act, vs in out.items():
    for ver, ds in vs.items():
        print(act, ver, {d: v["f1"] for d, v in ds.items()})
