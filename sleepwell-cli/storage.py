import json
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_PATH = os.path.join(DATA_DIR, "logs.json")
RULES_PATH = os.path.join(DATA_DIR, "rules.json")

def load_logs():
    if not os.path.exists(LOGS_PATH):
        return []
    with open(LOGS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_logs(logs):
    with open(LOGS_PATH, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

def get_log_for_user_date(user_id, date_str):
    logs = load_logs()
    for entry in logs:
        if entry.get("user_id") == user_id and entry.get("date") == date_str:
            return entry
    return None

def upsert_log(entry):
    """Add or update an entry in logs.json."""
    logs = load_logs()
    # find existing
    for i, e in enumerate(logs):
        if e.get("user_id") == entry.get("user_id") and e.get("date") == entry.get("date"):
            logs[i] = entry
            save_logs(logs)
            return
    # else append
    logs.append(entry)
    save_logs(logs)