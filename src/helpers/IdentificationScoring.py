import re

import pandas as pd

from src.helpers.IdentificationParser import parse_identification_response, canon_rule


def _stem(word: str) -> str:
    """Crude stemmer so inflections match: issues/issued/issue, books/book."""
    w = word
    if w.endswith("ies") and len(w) > 4:
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
        w = w[:-1]
    if len(w) > 3 and w.endswith("e"):
        w = w[:-1]
    return w


def canon_phrase(phrase: str) -> tuple[str, ...]:
    """Lowercase, strip emphasis/punctuation, drop articles, stem each word."""
    s = (phrase or "").lower()
    s = re.sub(r"[*_`]", "", s)
    s = s.replace("(s)", "")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    tokens = [t for t in s.split() if t not in ("the", "a", "an")]
    return tuple(_stem(t) for t in tokens)


def _truth_rows(ground_truth: pd.DataFrame) -> list[tuple[str, list[tuple[str, ...]]]]:
    """Expands a ground-truth DataFrame into (rule, [alternate phrase tuples]) rows."""
    df = ground_truth[["rule", "phrase"]].fillna("").astype(str)
    rows, seen = [], set()
    for rule_cell, phrase_cell in df.itertuples(index=False, name=None):
        rule = canon_rule(rule_cell)
        alternates = {canon_phrase(a) for a in phrase_cell.split(" / ")}
        alternates = sorted(a for a in alternates if a)
        if not rule or not alternates:
            continue
        key = (rule, tuple(alternates))
        if key in seen:
            continue
        seen.add(key)
        rows.append((rule, alternates))
    return rows


def score_identification_response(response: str, ground_truth: pd.DataFrame) -> dict:
    """
    Scores an identification response against a ground-truth DataFrame.
    A prediction matches a truth row when the rule numbers agree and the phrase
    equals any alternate after normalization (stemming, punctuation-insensitive).
    Returns: {"precision", "recall", "f1", "TP", "FP", "FN"}
    """
    predictions = {(rule, canon_phrase(phrase))
                   for rule, phrase in parse_identification_response(response)}
    truth_rows = _truth_rows(ground_truth)

    tp = sum(1 for rule, alternates in truth_rows
             if any((rule, alt) in predictions for alt in alternates))
    fn = len(truth_rows) - tp
    fp = max(0, len(predictions) - tp)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {"precision": precision, "recall": recall, "f1": f1, "TP": tp, "FP": fp, "FN": fn}
