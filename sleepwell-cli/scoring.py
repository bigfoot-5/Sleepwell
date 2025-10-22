# sleepwell-cli/scoring.py
def score_documents(documents, query):
    """Score documents based on relevance to the query."""
    return sorted(documents, key=lambda doc: doc.count(query), reverse=True)