#!/usr/bin/env python3
"""
Score an LLM's domain-specific phrase identification against a ground-truth CSV.

    python score_identification.py ../ground_truths/identification/library.csv out.md
    python score_identification.py gold.csv out.md --any-category   # ignore the rule number
    python score_identification.py gold.csv out.md --strict         # no partial matches
    python score_identification.py gold.csv out.md --json           # machine-readable

Gold CSV columns: rule,phrase   (alternates in phrase separated by " / ")

The model output may be:
  a) a markdown table with a `rule` (or `category`) column and a `phrase` column
  b) lines like  `3 | borrow`  or  `- (3) borrow`

Rule numbers (AUM brainstorming list):
  1 noun / noun phrase      4 adjective, enumeration   7 consist of / part of
  2 "X of Y" expression     5 numeric, quantity        8 containment / containing
  3 transitive verb         6 possession (has/have)    9 "X is a Y" (generalization)

MATCHING
Both sides are normalised (lower case, punctuation and articles dropped) and each word is
reduced to a crude stem, so "issued" ~ "issues" ~ "issue" and "books" ~ "book".
A pair is EXACT when the stemmed phrases are equal to any gold alternate, PARTIAL when one
is a contiguous word sequence inside the other ("has a title language" ~
"language tape has a title language"). By default the rule number must also agree.
Rows are paired by maximum-weight bipartite matching within each rule, so one gold item
consumes exactly one prediction and duplicates count as false positives.
"""
import argparse, csv, json, re, sys

EXACT_W, PARTIAL_W = 1.0, 0.6
RULE_NAMES = {1: "noun", 2: "X of Y", 3: "verb", 4: "adj/enum", 5: "numeric",
              6: "possession", 7: "part-of", 8: "containment", 9: "X is a Y"}
WORD_RULES = {"noun": 1, "nouns": 1, "xofy": 2, "verb": 3, "verbs": 3, "transitive": 3,
              "adjective": 4, "adjectives": 4, "enumeration": 4, "numeric": 5,
              "quantity": 5, "possession": 6, "consist": 7, "partof": 7,
              "containment": 8, "containing": 8, "isa": 9, "generalization": 9}


# ---------- normalisation ----------

def stem(w):
    for suf in ("ies",):
        if w.endswith(suf) and len(w) > 4:
            w = w[:-3] + "y"
    if w.endswith("ing") and len(w) > 5:
        w = w[:-3]
    elif w.endswith("ed") and len(w) > 4:
        w = w[:-2]
    elif w.endswith("es") and len(w) > 4 and w[-3] in "sxz":
        w = w[:-2]
    elif w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        w = w[:-1]
    if len(w) > 3 and w[-1] == w[-2] and w[-1] not in "aeiouls":
        w = w[:-1]                                  # running -> runn -> run
    if len(w) > 3 and w.endswith("e"):
        w = w[:-1]                                  # issue/issued -> issu
    return w


def canon(s):
    s = (s or "").lower()
    s = re.sub(r"\*\*|__|`", "", s)
    s = s.replace("(s)", "")
    s = re.sub(r"[^a-z0-9% ]+", " ", s)
    toks = [t for t in s.split() if t not in ("the", "a", "an")]
    return tuple(stem(t) for t in toks)


def contains(big, small):
    n, m = len(big), len(small)
    return m > 0 and any(big[i:i + m] == small for i in range(n - m + 1))


def parse_rule(cell):
    c = (cell or "").strip().lower()
    m = re.search(r"\d", c)
    if m:
        return int(m.group(0))
    key = re.sub(r"[^a-z]", "", c)
    for k, v in WORD_RULES.items():
        if key.startswith(k):
            return v
    return None


# ---------- parsing ----------

def parse_gold(path):
    rows = []
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        alts = [canon(a) for a in r["phrase"].split(" / ")]
        rows.append((int(r["rule"]), r["phrase"], [a for a in alts if a]))
    return rows


LINE = re.compile(r"^\s*(?:[-*+]|\d+\.)?\s*\(?\s*([1-9])\s*\)?\s*(?:\||:|-|\))\s*(.+?)\s*\|?\s*$")


def parse_output(text):
    """Return [(rule, raw_phrase)]. Prefers a markdown table with rule+phrase headers."""
    rows, cols = [], None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.count("|") >= 3:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if re.fullmatch(r"[:\- ]+", "".join(cells)):
                continue
            low = [re.sub(r"[^a-z]", "", c.lower()) for c in cells]
            if any(h in ("rule", "category", "cat") for h in low) and "phrase" in low:
                ri = next(i for i, h in enumerate(low) if h in ("rule", "category", "cat"))
                cols = (ri, low.index("phrase"))
                continue
            if cols and max(cols) < len(cells):
                rule = parse_rule(cells[cols[0]])
                if rule and cells[cols[1]]:
                    rows.append((rule, cells[cols[1]]))
            continue
        cols = None if not s else cols
        m = LINE.match(s)
        if m and not s.startswith("|"):
            rows.append((int(m.group(1)), m.group(2)))
    return rows


# ---------- matching ----------

def pair_score(g, p, any_cat, strict):
    grule, _, galts = g
    prule, palts = p
    if not any_cat and grule != prule:
        return 0.0
    if not palts:
        return 0.0
    if any(pa == ga for pa in palts for ga in galts):
        return EXACT_W
    if strict:
        return 0.0
    if any(contains(ga, pa) or contains(pa, ga) for pa in palts for ga in galts):
        return PARTIAL_W
    return 0.0


def match(gold, pred, any_cat, strict):
    edges = [(i, j, pair_score(gold[i], pred[j], any_cat, strict))
             for i in range(len(gold)) for j in range(len(pred))]
    edges = [e for e in edges if e[2] > 0]
    if not edges:
        return []
    try:
        import numpy as np
        from scipy.optimize import linear_sum_assignment
        cost = np.zeros((len(gold), len(pred)))
        for i, j, s in edges:
            cost[i, j] = -s
        ri, cj = linear_sum_assignment(cost)
        return [(i, j, -cost[i, j]) for i, j in zip(ri, cj) if cost[i, j] < 0]
    except ImportError:
        out, gu, pu = [], set(), set()
        for i, j, s in sorted(edges, key=lambda e: -e[2]):
            if i not in gu and j not in pu:
                out.append((i, j, s)); gu.add(i); pu.add(j)
        return out


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)


def score(gold, raw_pred, any_cat=False, strict=False):
    pred = [(r, [a for a in (canon(x) for x in t.split(" / ")) if a]) for r, t in raw_pred]
    groups = [None] if any_cat else sorted({g[0] for g in gold} | {p[0] for p in pred})
    TP = FP = FN = 0
    per, matched, missed, spurious = {}, [], [], []
    for rule in groups:
        gi = [i for i, g in enumerate(gold) if rule is None or g[0] == rule]
        pj = [j for j, p in enumerate(pred) if rule is None or p[0] == rule]
        pairs = match([gold[i] for i in gi], [pred[j] for j in pj], any_cat, strict)
        tp = len(pairs); fp = len(pj) - tp; fn = len(gi) - tp
        TP, FP, FN = TP + tp, FP + fp, FN + fn
        if rule is not None:
            per[RULE_NAMES.get(rule, str(rule))] = dict(zip(("tp", "fp", "fn"), (tp, fp, fn)))
        gu = {gi[a] for a, _, _ in pairs}
        pu = {pj[b] for _, b, _ in pairs}
        for a, b, s in pairs:
            matched.append({"gold": f"{gold[gi[a]][0]}|{gold[gi[a]][1]}",
                            "pred": f"{raw_pred[pj[b]][0]}|{raw_pred[pj[b]][1]}",
                            "kind": "exact" if s == EXACT_W else "partial"})
        missed += [f"{gold[i][0]}|{gold[i][1]}" for i in gi if i not in gu]
        spurious += [f"{raw_pred[j][0]}|{raw_pred[j][1]}" for j in pj if j not in pu]
    P, R, F = prf(TP, FP, FN)
    return {"tp": TP, "fp": FP, "fn": FN, "precision": P, "recall": R, "f1": F,
            "per_rule": per, "matched": matched, "missed": missed, "spurious": spurious,
            "n_gold": len(gold), "n_pred": len(pred)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gold_csv")
    ap.add_argument("output")
    ap.add_argument("--any-category", action="store_true", help="ignore rule number")
    ap.add_argument("--strict", action="store_true", help="exact matches only")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    gold = parse_gold(a.gold_csv)
    raw = parse_output(open(a.output, encoding="utf-8-sig").read())
    if not raw:
        sys.exit("No rows parsed. Expected a | rule | phrase | table.")
    res = score(gold, raw, a.any_category, a.strict)
    if a.json:
        print(json.dumps(res, indent=2)); return
    print(f"gold: {res['n_gold']}  predicted: {res['n_pred']}  "
          f"mode: {'any category' if a.any_category else 'category must match'}"
          f"{', strict' if a.strict else ''}\n")
    if res["per_rule"]:
        print(f"{'rule':>12} {'TP':>4} {'FP':>4} {'FN':>4}")
        for k, v in res["per_rule"].items():
            print(f"{k:>12} {v['tp']:4d} {v['fp']:4d} {v['fn']:4d}")
    print(f"\nTP {res['tp']}  FP {res['fp']}  FN {res['fn']}   "
          f"P {res['precision']:.3f}  R {res['recall']:.3f}  F1 {res['f1']:.3f}")
    part = [m for m in res["matched"] if m["kind"] == "partial"]
    if part:
        print(f"\npartial matches ({len(part)}) - check these are fair:")
        for m in part:
            print(f"  ~ {m['gold']}   <-   {m['pred']}")
    print(f"\nmissed ({len(res['missed'])}):")
    for t in res["missed"]:
        print("  -", t)
    print(f"\nspurious ({len(res['spurious'])}):")
    for t in res["spurious"]:
        print("  +", t)


if __name__ == "__main__":
    main()
