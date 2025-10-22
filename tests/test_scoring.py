# tests/test_scoring.py
import unittest
from sleepwell_cli.scoring import score_documents

class TestScoring(unittest.TestCase):
    def test_score_documents(self):
        documents = ["Sleep well tonight", "Good night sleep"]
        query = "sleep"
        scored_docs = score_documents(documents, query)
        self.assertEqual(scored_docs, ["Sleep well tonight", "Good night sleep"])

if __name__ == '__main__':
    unittest.main()