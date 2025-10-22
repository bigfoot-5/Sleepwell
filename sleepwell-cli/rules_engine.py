import json
import os
from typing import List, Dict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_PATH = os.path.join(DATA_DIR, "logs.json")
RULES_PATH = os.path.join(DATA_DIR, "rules.json")

def load_rules():
    with open(RULES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate_rules_for_entry(log_entry: dict) -> List[str]:
    """
    Return list of remedy strings whose conditions are triggered.
    For simplicity, conditions will be checked via simple comparisons or keywords.
    """
    remedies = []
    rules = load_rules()
    # rules structure may be: { "Caffeine_intake": [ {cond, remedy}, ... ], ... }
    for attr, rules_for_attr in rules.items():
        if attr not in log_entry:
            continue
        val = log_entry[attr]
        for rule in rules_for_attr:
            cond = rule.get("condition")
            remedy = rule.get("remedy")
            # Here, condition is a string like "caffeine_intake_mg > 50"
            # We can `eval` it carefully with local context, or parse it
            try:
                # build a small environment where `val` is available as `value`
                env = {"value": val}
                # e.g. condition: "value > 50"
                if eval(cond, {}, env):
                    remedies.append(remedy)
            except Exception as e:
                # skip invalid
                pass
    return remedies