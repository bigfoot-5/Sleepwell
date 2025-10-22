def compute_sleep_score(hours_slept, continuity_score, mood_rating):
    """
    Score = (Hours Slept / 8 * 40) + (Continuity Score * 40) + (Mood Rating * 20)
    """
    part1 = (hours_slept / 8.0) * 40
    part2 = continuity_score * 40
    part3 = mood_rating * 20
    return part1 + part2 + part3
def score_log_entry(log_entry: dict):
    # assume continuity_score etc exist
    score = compute_sleep_score(
        log_entry.get("sleep_time_hours", 0),
        log_entry.get("continuity_score", 0),
        log_entry.get("mood_rating", 0),
    )
    log_entry["sleep_score"] = score
    return score