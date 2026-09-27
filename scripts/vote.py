#!/usr/bin/env python3
"""Element-level self-consistency (atomic majority voting) for identification.

    python vote.py DOMAIN K run1.md run2.md ...      -> prints a | rule | phrase | table

A row (rule, stemmed phrase) is kept when at least K of the runs contain it.
Stemming/normalisation is the same as score_identification.canon, so "books" and "book" vote together.
"""
import sys, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import score_identification as SI

AUX = {"is", "are", "be", "been", "being", "was", "were", "can", "may", "must", "should", "will", "shall", "need", "has", "have"}

def _key(rule, phrase):
    """Exact-match vote key: scorer normalisation plus auxiliaries/modals dropped for verbs,
    so "issues", "is issued" and "issued" vote together but "bar code" and "book bar code" do not."""
    toks = SI.canon(phrase.split(" / ")[0])
    if rule == 3:
        toks = tuple(t for t in toks if t not in AUX) or toks
    return (rule, toks)

def vote(texts, k):
    counts, rep = collections.Counter(), {}
    for t in texts:
        seen = set()
        for rule, phrase in SI.parse_output(t):
            key = _key(rule, phrase)
            if not key[1] or key in seen:
                continue
            seen.add(key); counts[key] += 1; rep.setdefault(key, (rule, phrase))
    return [rep[key] for key, c in counts.items() if c >= k]

if __name__ == "__main__":
    k = int(sys.argv[2]); texts = [open(p).read() for p in sys.argv[3:]]
    print("| rule | phrase |\n|---|---|")
    for r, p in vote(texts, k): print(f"| {r} | {p} |")
