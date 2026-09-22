#!/usr/bin/env python3
"""
Score an LLM's markdown output against a ground-truth CSV.

    python score_markdown.py library.csv model_output.md
    python score_markdown.py ntss.csv out.md --strict        # exact match only
    python score_markdown.py ntss.csv out.md --no-args       # label+element only
    python score_markdown.py ntss.csv out.md --report m.csv  # dump every pairing

Gold CSV columns: label,element,arg1,arg2

The markdown may contain either form (both are parsed, mixed is fine):

  a) a table with label | element | arg1 | arg2 columns, in any column order
  b) bullets in the ground-truth notation:
       - (C) Vehicle
       - (AS) select (Customer, Vehicle)
       - (A) name (Customer)
       - (I) ISA (Passenger Car, Vehicle)

MATCHING
Default is substring matching, not equality: normalised strings match when
either contains the other ("price" ~ "rental price"). Because substring
matching is many-to-many, rows are paired by maximum-weight bipartite
matching within each label, so one gold row consumes exactly one predicted
row. Exact matches are weighted above substring matches so they win ties.

An empty arg on EITHER side is a wildcard. That is deliberate: the Word-derived
gold files mostly do not state attribute ownership, so a model that correctly
fills arg1 on an `A` row is not punished for it.

For AS and AG, both argument orders are tried (the source files disagree on
part/whole order).
"""
import sys, csv, re, argparse

SYMMETRIC = {"AS", "AG"}
EXACT_W, FUZZY_W = 1.0, 0.6      # exact pairings are preferred over substring ones


# ---------- normalisation ----------

def canon(s):
    s = re.sub(r"[\u201c\u201d\u2018\u2019]", "", (s or ""))
    s = re.sub(r"\*\*|__|`", "", s)                 # strip markdown emphasis
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\b(the|a|an)\b", "", s).strip()


def norm_label(s):
    s = re.sub(r"[^A-Za-z]", "", (s or "")).upper()
    return {"CLASS": "C", "ATTRIBUTE": "A", "ATTR": "A", "VALUE": "V",
            "ASSOCIATION": "AS", "ASSOCIATIONCLASS": "AC",
            "AGGREGATION": "AG", "ISA": "I", "INHERITANCE": "I",
            "GENERALIZATION": "I"}.get(s, s)


VALID = {"C", "A", "V", "AS", "AC", "AG", "I"}


# ---------- parsing ----------

def parse_csv(path):
    rows = []
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        lab = norm_label(r.get("label"))
        if lab in VALID:
            rows.append((lab, canon(r.get("element")),
                         canon(r.get("arg1")), canon(r.get("arg2"))))
    return rows


BULLET = re.compile(
    r"^\s*(?:[-*+]|\d+\.)?\s*\(?\s*(C|A|V|AS|AC|AG|I)\s*\)\s*"   # (C)
    r"([^()]*?)\s*"                                              # element
    r"(?:\(([^()]*)\))?\s*$", re.I)


def parse_markdown(path):
    text = open(path, encoding="utf-8-sig").read()
    text = re.sub(r"```.*?```", lambda m: m.group(0).strip("`"), text, flags=re.S)
    rows, in_table, cols = [], False, None

    for line in text.splitlines():
        s = line.strip()

        # --- markdown table ---
        if s.startswith("|") and s.count("|") >= 3:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if re.fullmatch(r"[:\- ]+", "".join(cells)):      # separator row
                continue
            low = [c.lower().strip("*` ") for c in cells]
            if "label" in low and "element" in low:           # header row
                cols, in_table = {n: i for i, n in enumerate(low)}, True
                continue
            if in_table and cols:
                def g(name):
                    i = cols.get(name)
                    return cells[i] if i is not None and i < len(cells) else ""
                lab = norm_label(g("label"))
                if lab in VALID:
                    rows.append((lab, canon(g("element")),
                                 canon(g("arg1")), canon(g("arg2"))))
                continue
        else:
            in_table = False

        # --- bullet notation ---
        m = BULLET.match(s)
        if m:
            lab = norm_label(m.group(1))
            if lab not in VALID:
                continue
            args = [canon(a) for a in (m.group(3) or "").split(",")] + ["", ""]
            rows.append((lab, canon(m.group(2)), args[0], args[1]))
    return rows


# ---------- matching ----------

def field_match(g, p):
    if not g or not p:                 # blank on either side = wildcard
        return True, True              # (matched, was_exact)
    if g == p:
        return True, True
    return (g in p or p in g), False


def pair_score(gold, pred, use_args, fuzzy):
    if gold[0] != pred[0]:
        return 0.0
    ok, exact = field_match(gold[1], pred[1])
    if not ok or (not exact and not fuzzy):
        return 0.0
    all_exact = exact
    if use_args:
        orders = [(pred[2], pred[3])]
        if gold[0] in SYMMETRIC:
            orders.append((pred[3], pred[2]))
        best = None
        for a1, a2 in orders:
            o1, e1 = field_match(gold[2], a1)
            o2, e2 = field_match(gold[3], a2)
            if not o1 or not o2:
                continue
            if not fuzzy and not (e1 and e2):
                continue
            cand = e1 and e2
            best = cand if best is None else (best or cand)
        if best is None:
            return 0.0
        all_exact = all_exact and best
    return EXACT_W if all_exact else FUZZY_W


def match(gold, pred, use_args, fuzzy):
    """Max-weight bipartite matching; returns list of (gold_i, pred_j, score)."""
    n, m = len(gold), len(pred)
    edges = [(i, j, pair_score(gold[i], pred[j], use_args, fuzzy))
             for i in range(n) for j in range(m)]
    edges = [e for e in edges if e[2] > 0]
    if not edges:
        return []
    try:
        import numpy as np
        from scipy.optimize import linear_sum_assignment
        cost = np.zeros((n, m))
        for i, j, s in edges:
            cost[i, j] = -s
        ri, cj = linear_sum_assignment(cost)
        return [(i, j, -cost[i, j]) for i, j in zip(ri, cj) if cost[i, j] < 0]
    except ImportError:                                   # greedy fallback
        out, gu, pu = [], set(), set()
        for i, j, s in sorted(edges, key=lambda e: -e[2]):
            if i not in gu and j not in pu:
                out.append((i, j, s)); gu.add(i); pu.add(j)
        return out


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)


def fmt(t):
    return "|".join(x for x in t if x)


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gold_csv")
    ap.add_argument("markdown")
    ap.add_argument("--strict", action="store_true", help="exact match only")
    ap.add_argument("--no-args", action="store_true", help="ignore arg1/arg2")
    ap.add_argument("--report", help="write every pairing to this CSV")
    a = ap.parse_args()

    gold, pred = parse_csv(a.gold_csv), parse_markdown(a.markdown)
    use_args, fuzzy = not a.no_args, not a.strict
    if not pred:
        sys.exit("No rows parsed from the markdown. Expected a "
                 "| label | element | arg1 | arg2 | table or (LABEL) bullets.")

    print(f"gold rows: {len(gold)}   parsed from markdown: {len(pred)}   "
          f"mode: {'exact' if a.strict else 'substring'}"
          f"{', args ignored' if a.no_args else ''}\n")

    print(f"{'label':>6} {'TP':>4} {'FP':>4} {'FN':>4} {'P':>7} {'R':>7} {'F1':>7}")
    TP = FP = FN = 0
    macro, audit, misses, spurious = [], [], [], []

    for lab in sorted({t[0] for t in gold + pred}):
        g = [t for t in gold if t[0] == lab]
        p = [t for t in pred if t[0] == lab]
        pairs = match(g, p, use_args, fuzzy)
        tp = len(pairs)
        fp, fn = len(p) - tp, len(g) - tp
        TP, FP, FN = TP + tp, FP + fp, FN + fn
        P, R, F = prf(tp, fp, fn)
        macro.append((P, R, F))
        print(f"{lab:>6} {tp:4d} {fp:4d} {fn:4d} {P:7.3f} {R:7.3f} {F:7.3f}")

        gu = {i for i, _, _ in pairs}
        pu = {j for _, j, _ in pairs}
        for i, j, s in pairs:
            audit.append(("exact" if s == EXACT_W else "substring",
                          fmt(g[i]), fmt(p[j])))
        misses += [fmt(t) for i, t in enumerate(g) if i not in gu]
        spurious += [fmt(t) for j, t in enumerate(p) if j not in pu]

    P, R, F = prf(TP, FP, FN)
    print(f"{'MICRO':>6} {TP:4d} {FP:4d} {FN:4d} {P:7.3f} {R:7.3f} {F:7.3f}")
    n = len(macro) or 1
    print(f"{'MACRO':>6} {'':14} {sum(x[0] for x in macro)/n:7.3f} "
          f"{sum(x[1] for x in macro)/n:7.3f} {sum(x[2] for x in macro)/n:7.3f}")

    loose = [x for x in audit if x[0] == "substring"]
    if loose:
        print(f"\nsubstring pairings ({len(loose)}) — check these are fair:")
        for _, gtxt, ptxt in loose:
            print(f"  ~ {gtxt}   <-   {ptxt}")
    print(f"\nmissed ({len(misses)}):")
    for t in misses:
        print("  -", t)
    print(f"\nspurious ({len(spurious)}):")
    for t in spurious:
        print("  +", t)

    if a.report:
        with open(a.report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["outcome", "gold", "prediction"])
            for kind, gtxt, ptxt in audit:
                w.writerow([f"TP ({kind})", gtxt, ptxt])
            for t in misses:
                w.writerow(["FN", t, ""])
            for t in spurious:
                w.writerow(["FP", "", t])
        print(f"\nwrote {a.report}")


if __name__ == "__main__":
    main()
