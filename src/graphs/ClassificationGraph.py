import os

from langgraph.graph import StateGraph, START, END
from src.models.GraphState import OptimizerState
from src.helpers.PromptHelpers import (extract_prompt, extract_changelog,
                                       build_eval_prompt, resolve_strategy)
from src.helpers.ScoringHelpers import score_response
from src.helpers.ScorecardHelpers import build_scorecard
from datetime import datetime

def build_classification_graph(model, phrases, truths,  max_trials):
    def _run_lib_classifier(state: dict):
        """Builds full lib prompt and asks model to classify domain phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DOMAIN PHRASES>", phrases["lib_phrases"])
        path = f"../prompts/auto_prompt_evo/classification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | lib: classifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | lib: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/lib.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "lib_eval": {
                "response": model_response
            }
        }

    def _run_rental_classifier(state: dict):
        """Builds full lib prompt and asks model to classify domain phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DOMAIN PHRASES>", phrases["rental_phrases"])
        path = f"../prompts/auto_prompt_evo/classification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | rental: classifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | rental: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/rental.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "rental_eval": {
                "response": model_response
            }
        }

    def _run_ntss_classifier(state: dict):
        """Builds full lib prompt and asks model to classify domain phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DOMAIN PHRASES>", phrases["ntss_phrases"])
        path = f"../prompts/auto_prompt_evo/classification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | ntss: classifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | ntss: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/ntss.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "ntss_eval": {
                "response": model_response
            }
        }

    def _score(state: dict):
        """Score evals for each dataset adding precision, recall, f1 and TP/FP/FN to state for each"""

        # Helper to extract text from potential AIMessage objects
        def get_text(data):
            resp = data.get("response", "")
            return resp.content if hasattr(resp, 'content') else resp

        lib_scores = score_response(get_text(state["lib_eval"]), truths["lib_truth"])
        rent_scores = score_response(get_text(state["rental_eval"]), truths["rent_truth"])
        ntss_scores = score_response(get_text(state["ntss_eval"]), truths["ntss_truth"])

        def fmt(name, s):
            return (f"{name}: p-{s['precision']:.2f} r-{s['recall']:.2f} f1-{s['f1']:.2f} "
                    f"(TP={s['TP']} FP={s['FP']} FN={s['FN']})")

        print(f"\n--- Evaluation Results (trial {state['current_trial']}) ---")
        print(fmt("Lib", lib_scores))
        print(fmt("Rent", rent_scores))
        print(fmt("Ntss", ntss_scores))

        strategy_name, _ = resolve_strategy(state.get("optimization_strategy"))
        scorecard = build_scorecard(state["current_trial"], lib_scores, rent_scores, ntss_scores,
                                    strategy=strategy_name)
        path = f"../prompts/auto_prompt_evo/classification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/scorecard.md", 'w', encoding='utf-8') as f:
            f.write(scorecard)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | score: wrote scorecard to {path}/scorecard.md")

        return {
            "lib_eval": {**state["lib_eval"], **lib_scores},
            "rental_eval": {**state["rental_eval"], **rent_scores},
            "ntss_eval": {**state["ntss_eval"], **ntss_scores},
        }

    def _optimize(state: dict):
        """Read eval data, prompt, and ground truths and optimize prompt"""
        eval_prompt = build_eval_prompt(state, truths, strategy=state.get("optimization_strategy"))
        strategy_name, _ = resolve_strategy(state.get("optimization_strategy"))
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | optimize: strategy '{strategy_name}'; asking model to improve the prompt...")
        improved_prompt = model.invoke(eval_prompt)
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | optimize: done")

        # Ensure we return the content string, not the AIMessage object
        content = improved_prompt.content if hasattr(improved_prompt, 'content') else improved_prompt
        return {
            "optimized_prompt": content
        }

    def _checkpoint(state: dict):
        """Write optimized prompt and change log to classification folder and advance to the new prompt"""
        path = f"../prompts/auto_prompt_evo/classification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)

        raw = state["optimized_prompt"]
        new_prompt = extract_prompt(raw)
        changelog = extract_changelog(raw)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | checkpoint: saving optimized prompt to {path}/prompt.md")

        if "<DOMAIN PHRASES>" not in new_prompt:
            print(f"WARNING: optimized prompt for trial {state['current_trial']} is missing the "
                  f"<DOMAIN PHRASES> placeholder; keeping the previous prompt.")
            new_prompt = state["current_prompt"]

        with open(f"{path}/prompt.md", 'w', encoding='utf-8') as f:
            f.write(new_prompt)

        if changelog:
            print(
                f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | checkpoint: saving change log to {path}/changelog.md")
            with open(f"{path}/changelog.md", 'w', encoding='utf-8') as f:
                f.write(f"# Change Log (trial {state['current_trial']})\n\n{changelog}\n")
        else:
            print(f"WARNING: no ```changelog block found in optimizer response for trial "
                  f"{state['current_trial']}; no change log written.")

        return {
            "current_trial": state["current_trial"] + 1,
            "current_prompt": new_prompt,
            "changelog": changelog,
        }

    def _should_continue(state: dict):
        """Determines if the optimizer should run again or stop"""
        if state["current_trial"] < max_trials:
            return "run_lib"
        return END

    workflow = StateGraph(OptimizerState)

    workflow.add_node("run_lib", _run_lib_classifier)
    workflow.add_node("run_rental", _run_rental_classifier)
    workflow.add_node("run_ntss", _run_ntss_classifier)
    workflow.add_node("score", _score)
    workflow.add_node("optimize", _optimize)
    workflow.add_node("checkpoint", _checkpoint)

    workflow.add_edge(START, "run_lib")
    workflow.add_edge("run_lib", "run_rental")
    workflow.add_edge("run_rental", "run_ntss")
    workflow.add_edge("run_ntss", "score")
    workflow.add_edge("score", "optimize")
    workflow.add_edge("optimize", "checkpoint")
    workflow.add_conditional_edges(
        "checkpoint",
        _should_continue,
        {
            "run_lib": "run_lib",
            END: END
        }
    )

    return workflow