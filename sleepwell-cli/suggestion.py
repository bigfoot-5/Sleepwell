from storage import get_log_for_user_date, upsert_log
from scoring import score_log_entry
from rules_engine import evaluate_rules_for_entry

import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # or /api/chat depending
MODEL_NAME = "qwen3:1.7b"

def query_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    resp = requests.post(OLLAMA_API_URL, json=payload)
    j = resp.json()
    # depending on Ollama API version, extract the generated message
    return j.get("response") or j.get("message", {}).get("content", "")

def generate_suggestions_for(user_id: str, date: str) -> str:
    """Compute suggestions (remedies) for a specific log entry, return text output."""
    log = get_log_for_user_date(user_id, date)
    if log is None:
        return "No log entry found for that date."

    # 1. compute score
    score = score_log_entry(log)

    # 2. evaluate rules
    remedies = evaluate_rules_for_entry(log)

    # 3. Build a prompt for LLM with context + remedies
    context = f"Log entry: {log}\nDerived remedies: {remedies}\n"
    prompt = (
        context +
        "Using the above log and remedies, generate a concise suggestion to improve sleep quality tonight."
    )
    llm_response = query_ollama(prompt)
    # optionally save suggestions back in log
    log["suggestions"] = remedies + [llm_response]
    upsert_log(log)

    return llm_response