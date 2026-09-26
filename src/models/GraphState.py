from typing import TypedDict

from src.models.OptimizationStrategy import OptimizationStrategy

class OptimizerState(TypedDict):
    current_prompt: str
    current_trial: int
    optimized_prompt: str
    changelog: str
    optimization_strategy: OptimizationStrategy
    rental_eval: dict[str,str]
    ntss_eval: dict[str,str]
    lib_eval: dict[str,str]


class IdentificationState(TypedDict):
    current_prompt: str
    current_trial: int
    optimized_prompt: str
    changelog: str
    optimization_strategy: OptimizationStrategy
    rental_eval: dict[str,str]
    ntss_eval: dict[str,str]
    lib_eval: dict[str,str]