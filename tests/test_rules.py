# tests/test_rules.py
import unittest
from sleepwell_cli.rules_engine import apply_rules

class TestRulesEngine(unittest.TestCase):
    def test_apply_rules(self):
        rules = [{"condition": "sleep", "replacement": "rest"}]
        text = "Good sleep is essential."
        result = apply_rules(text, rules)
        self.assertEqual(result, "Good rest is essential.")

if __name__ == '__main__':
    unittest.main()