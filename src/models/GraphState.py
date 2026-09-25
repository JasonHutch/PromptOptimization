from typing import TypedDict

class OptimizerState(TypedDict):
    current_prompt: str
    current_trial: int
    optimized_prompt: str
    rental_eval: dict[str,str]
    ntss_eval: dict[str,str]
    lib_eval: dict[str,str]


class IdentificationState(TypedDict):
    current_prompt: str
    current_trial: int
    optimized_prompt: str
    rental_eval: dict[str,str]
    ntss_eval: dict[str,str]
    lib_eval: dict[str,str]