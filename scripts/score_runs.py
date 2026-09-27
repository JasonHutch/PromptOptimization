#!/usr/bin/env python3
"""
Score saved runs (JSON documents exported from the lab page's `runs` collection).

    python score_runs.py RUNS_DIR OUT_DIR

For each run with status "done" and no score yet, writes OUT_DIR/<run_id>.json containing
{"score": {...}} and prints a summary table. Also saves each raw response as
responses/<activity>/<version>/<domain>.md for the submission.

Identification -> score_identification.py (category must match).
Classification -> the team's score_markdown.py (substring mode, args used).
Chain of thought -> Step 1 table scored as identification, "Final domain model" table as
classification.
"""
import json, os, re, sys, tempfile, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import score_identification as SI   # noqa: E402
import score_markdown as SM         # noqa: E402

GT = ROOT / "ground_truths"


def score_id(text, domain):
    gold = SI.parse_gold(GT / "identification" / f"{domain}.csv")
    raw = SI.parse_output(text)
    r = SI.score(gold, raw)
    return {k: r[k] for k in ("precision", "recall", "f1", "tp", "fp", "fn", "missed", "spurious",
                              "per_rule", "n_gold", "n_pred")}


def score_cls(text, domain):
    gold = SM.parse_csv(GT / "classification" / f"{domain}.csv")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
        fh.write(text)
        path = fh.name
    pred = SM.parse_markdown(path)
    os.unlink(path)
    TP = FP = FN = 0
    missed, spurious, per = [], [], {}
    for lab in sorted({t[0] for t in gold + pred}):
        g = [t for t in gold if t[0] == lab]
        p = [t for t in pred if t[0] == lab]
        pairs = SM.match(g, p, True, True)
        tp = len(pairs); fp = len(p) - tp; fn = len(g) - tp
        TP, FP, FN = TP + tp, FP + fp, FN + fn
        per[lab] = {"tp": tp, "fp": fp, "fn": fn}
        gu = {i for i, _, _ in pairs}; pu = {j for _, j, _ in pairs}
        missed += [SM.fmt(t) for i, t in enumerate(g) if i not in gu]
        spurious += [SM.fmt(t) for j, t in enumerate(p) if j not in pu]
    P, R, F = SM.prf(TP, FP, FN)
    return {"precision": P, "recall": R, "f1": F, "tp": TP, "fp": FP, "fn": FN,
            "missed": missed, "spurious": spurious, "per_label": per,
            "n_gold": len(gold), "n_pred": len(pred)}


def split_cot(text):
    low = text.lower()
    s1 = low.find("step 1")
    s2 = low.find("step 2", s1 + 1) if s1 >= 0 else -1
    fin = low.rfind("final domain model")
    step1 = text[s1:s2] if s1 >= 0 and s2 > s1 else (text[:fin] if fin > 0 else text)
    final = text[fin:] if fin >= 0 else ""
    return step1, final


def main():
    runs_dir, out_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for f in sorted(runs_dir.glob("*.json")):
        run = json.load(open(f))
        doc = run.get("data", run)
        rid = run.get("id") or f.stem
        if doc.get("status") != "done" or not doc.get("response"):
            continue
        act, dom, text = doc["activity"], doc["domain"], doc["response"]
        resp = ROOT / "responses" / act / doc["version"] / f"{dom}_r{doc.get('n', 1)}.md"
        resp.parent.mkdir(parents=True, exist_ok=True)
        resp.write_text(text)
        if act == "identification":
            sc = score_id(text, dom)
        elif act == "classification":
            sc = score_cls(text, dom)
        else:
            step1, final = split_cot(text)
            sc = {"identification": score_id(step1, dom),
                  "classification": score_cls(final, dom) if final else None}
            if not final:
                sc["note"] = "No 'Final domain model' section found in the response."
        json.dump({"score": sc}, open(out_dir / f"{rid}.json", "w"))
        head = sc if act != "cot" else sc["classification"] or {"f1": 0, "precision": 0, "recall": 0}
        extra = f"  (step1 F1 {sc['identification']['f1']:.3f})" if act == "cot" else ""
        rows.append((act, doc["version"], dom, doc.get("n"), head["precision"], head["recall"], head["f1"], extra, rid))
    for r in sorted(rows):
        print(f"{r[0]:>15} {r[1]:>3} {r[2]:>11} r{r[3]}  P {r[4]:.3f}  R {r[5]:.3f}  F1 {r[6]:.3f}{r[7]}   [{r[8]}]")


if __name__ == "__main__":
    main()
