"""
Unit tests for suite-media-assets business logic.
"""

import sys
import unittest
from pathlib import Path

# Ensure suite root is in sys.path
SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.base64_engine import encode_string_to_data_uri, decode_base64_string


class TestBase64Engine(unittest.TestCase):
    def test_encode_and_decode(self):
        original = "DeveloperOS Tools"
        encoded = encode_string_to_data_uri(original, "text/plain")
        self.assertIn("data:text/plain;base64,", encoded["data_uri"])

        decoded = decode_base64_string(encoded["base64_string"])
        self.assertTrue(decoded["success"])
        self.assertEqual(decoded["text"], original)

    def test_decode_invalid_string(self):
        res = decode_base64_string("!@#$%^&*")
        self.assertFalse(res["success"])
        self.assertIsNotNone(res["error"])


if __name__ == "__main__":
    unittest.main()
