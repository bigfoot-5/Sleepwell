# tests/test_suggestions.py
import unittest
from sleepwell_cli.suggestion import generate_suggestion

class TestSuggestions(unittest.TestCase):
    def test_generate_suggestion(self):
        query = "How to improve sleep?"
        suggestion = generate_suggestion(query)
        self.assertIn("improve sleep", suggestion)

if __name__ == '__main__':
    unittest.main()