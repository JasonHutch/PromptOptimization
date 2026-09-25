import pandas as pd
from src.helpers.ResponseParser import parse_llm_response

def score_response(response: str, ground_truth: pd.DataFrame) -> dict:
    """
    Scores the model response against a ground truth DataFrame using exact
    4-tuple (label, element, arg1, arg2) matching.
    Returns: {"precision", "recall", "f1", "TP", "FP", "FN"}
    """
    truth = _truth_to_set(ground_truth)
    pred = parse_llm_response(response)

    tp = len(pred & truth)
    fp = len(pred - truth)
    fn = len(truth - pred)

    c_matrix = {"TP": tp, "FP": fp, "FN": fn}

    precision = calc_precision(c_matrix) if (tp + fp) > 0 else 0.0
    recall = calc_recall(c_matrix) if (tp + fn) > 0 else 0.0
    f1 = calculate_f1(precision, recall) if (precision + recall) > 0 else 0.0

    return {"precision": precision, "recall": recall, "f1": f1, "TP": tp, "FP": fp, "FN": fn}

def generate_confusion_matrix(pred, targets):
    """Takes model predictions and ground truths and returns a confusion matrix as a dict"""
    return { "TP":0, "TN":0, "FP":0, "FN":0 }

def calc_precision(c_matrix):
    """Given confusion matrix, calculate how precise the models predictions are"""
    return c_matrix["TP"] / (c_matrix["TP"] + c_matrix["FP"])

def calc_recall(c_matrix):
    """Given confusion matrix, calculate the models ability to identify all positive cases in a dataset"""
    return c_matrix["TP"] / (c_matrix["TP"] + c_matrix["FN"])

def calculate_f1(precision, recall):
    """Calculates F1 score for classification task"""
    return 2 * ((precision * recall) / (precision + recall)) if (precision + recall) > 0 else 0.0

def _truth_to_set(ground_truth: pd.DataFrame) -> set[tuple[str, str, str, str]]:
    """Normalize a ground-truth DataFrame into a set of (label, element, arg1, arg2)."""
    df = ground_truth[["label", "element", "arg1", "arg2"]].fillna("").astype(str)
    df = df.apply(lambda col: col.str.strip().str.lower())
    return set(df.itertuples(index=False, name=None))
