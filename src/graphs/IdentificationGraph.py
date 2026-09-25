import os

from langgraph.graph import StateGraph, START, END
from src.models.GraphState import IdentificationState
from src.helpers.PromptHelpers import extract_prompt, build_identification_eval_prompt
from src.helpers.IdentificationScoring import score_identification_response
from datetime import datetime

def build_identification_graph(model, descriptions, truths, max_trials):
    def _run_lib_identifier(state: dict):
        """Builds full lib prompt and asks model to identify domain-specific phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DESCRIPTION>", descriptions["lib_desc"])
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | lib: identifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | lib: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        path = f"../prompts/auto_prompt_evo/identification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/lib.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "lib_eval": {
                "response": model_response
            }
        }

    def _run_rental_identifier(state: dict):
        """Builds full rental prompt and asks model to identify domain-specific phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DESCRIPTION>", descriptions["rental_desc"])
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | rental: identifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | rental: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        path = f"../prompts/auto_prompt_evo/identification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/rental.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "rental_eval": {
                "response": model_response
            }
        }

    def _run_ntss_identifier(state: dict):
        """Builds full ntss prompt and asks model to identify domain-specific phrases"""

        prompt_template = state["current_prompt"]
        full_prompt = str(prompt_template).replace("<DESCRIPTION>", descriptions["ntss_desc"])
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | ntss: identifying domain phrases...")
        model_response = model.invoke(full_prompt)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | ntss: done ({len(str(model_response.content))} chars)")

        # Save response to trial folder
        path = f"../prompts/auto_prompt_evo/identification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)
        response_text = model_response.content if hasattr(model_response, 'content') else str(model_response)
        with open(f"{path}/ntss.csv", 'w', encoding='utf-8') as f:
            f.write(response_text)

        return {
            "ntss_eval": {
                "response": model_response
            }
        }

    def _score(state: dict):
        """Score identification evals for each dataset adding precision, recall, f1 and TP/FP/FN to state"""

        # Helper to extract text from potential AIMessage objects
        def get_text(data):
            resp = data.get("response", "")
            return resp.content if hasattr(resp, 'content') else resp

        lib_scores = score_identification_response(get_text(state["lib_eval"]), truths["lib_truth"])
        rent_scores = score_identification_response(get_text(state["rental_eval"]), truths["rent_truth"])
        ntss_scores = score_identification_response(get_text(state["ntss_eval"]), truths["ntss_truth"])

        def fmt(name, s):
            return (f"{name}: p-{s['precision']:.2f} r-{s['recall']:.2f} f1-{s['f1']:.2f} "
                    f"(TP={s['TP']} FP={s['FP']} FN={s['FN']})")

        print(f"\n--- Identification Evaluation Results (trial {state['current_trial']}) ---")
        print(fmt("Lib", lib_scores))
        print(fmt("Rent", rent_scores))
        print(fmt("Ntss", ntss_scores))

        return {
            "lib_eval": {**state["lib_eval"], **lib_scores},
            "rental_eval": {**state["rental_eval"], **rent_scores},
            "ntss_eval": {**state["ntss_eval"], **ntss_scores},
        }

    def _optimize(state: dict):
        """Read eval data, prompt, and ground truths and optimize prompt"""
        eval_prompt = build_identification_eval_prompt(state, truths)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | optimize: asking model to improve the prompt...")
        improved_prompt = model.invoke(eval_prompt)
        print(f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | optimize: done")

        # Ensure we return the content string, not the AIMessage object
        content = improved_prompt.content if hasattr(improved_prompt, 'content') else improved_prompt
        return {
            "optimized_prompt": content
        }

    def _checkpoint(state: dict):
        """Write optimized prompt to identification folder and advance to the new prompt"""
        path = f"../prompts/auto_prompt_evo/identification/t{state['current_trial']}"
        os.makedirs(path, exist_ok=True)

        raw = state["optimized_prompt"]
        new_prompt = extract_prompt(raw)
        print(
            f"[{datetime.now():%H:%M:%S}] Trial {state['current_trial']} | checkpoint: saving optimized prompt to {path}/prompt.md")

        if "<DESCRIPTION>" not in new_prompt:
            print(f"WARNING: optimized prompt for trial {state['current_trial']} is missing the "
                  f"<DESCRIPTION> placeholder; keeping the previous prompt.")
            new_prompt = state["current_prompt"]

        with open(f"{path}/prompt.md", 'w', encoding='utf-8') as f:
            f.write(new_prompt)

        return {
            "current_trial": state["current_trial"] + 1,
            "current_prompt": new_prompt,
        }

    def _should_continue(state: dict):
        """Determines if the optimizer should run again or stop"""
        if state["current_trial"] < max_trials:
            return "run_lib"
        return END

    workflow = StateGraph(IdentificationState)

    workflow.add_node("run_lib", _run_lib_identifier)
    workflow.add_node("run_rental", _run_rental_identifier)
    workflow.add_node("run_ntss", _run_ntss_identifier)
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
