from enum import Enum


class OptimizationStrategy(str, Enum):
    """
    Allowed focus strategies for the prompt-optimization step. The optimizer's
    `optimization_strategy` state value must be one of these members (or the
    equivalent string value); anything else is rejected with a ValueError.
    """
    META_PROMPTING = "meta_prompting"
    FEW_SHOT_PROMPTING = "few_shot_prompting"
    DECISION_RUBRIC = "decision_rubric"
    NONE = "none"