# sleepwell-cli/rules_engine.py
import json

def load_rules():
    """Load domain-specific rules from rules.json."""
    with open('data/rules.json', 'r') as f:
        return json.load(f)

def apply_rules(text, rules):
    """Apply rules to the given text."""
    for rule in rules:
        if rule['condition'] in text:
            text = text.replace(rule['condition'], rule['replacement'])
    return text