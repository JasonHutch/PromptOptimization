# Deck

Regenerate after new runs are scored:

    python scripts/score_runs.py <exported runs dir> scores_new/ && cp scores_new/*.json scores/
    python scripts/summarize.py            # scores/ -> results.json
    node deck/build_deck.js results.json Team4_Prompt_Optimization.pptx

Every number and every "within noise" / "met" statement is computed from results.json.
Slides that depend on P3 (Experiment 4) appear automatically once P3 has been scored on all domains.
Add team member names on slide 1 and your own contributions to the AI/HITL table (slide 12).
