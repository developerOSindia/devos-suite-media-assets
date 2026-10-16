"""
Unit tests for suite-media-assets Base64 and media utilities.
"""

import sys
import unittest
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.base64_engine import encode_string_to_data_uri, decode_base64_string, validate_svg_asset


class TestBase64(unittest.TestCase):
    def test_encode_data_uri(self):
        res = encode_string_to_data_uri("DeveloperOS", mime_type="text/plain")
        self.assertEqual(res["base64_string"], "RGV2ZWxvcGVyT1M=")
        self.assertEqual(res["data_uri"], "data:text/plain;base64,RGV2ZWxvcGVyT1M=")
        self.assertIn("background-image", res["css_background"])

    def test_decode_base64(self):
        res = decode_base64_string("RGV2ZWxvcGVyT1M=")
        self.assertTrue(res["success"])
        self.assertEqual(res["text"], "DeveloperOS")

    def test_decode_with_data_uri_prefix(self):
        res = decode_base64_string("data:application/json;base64,eyJzdGF0dXMiOiAic3VjY2VzcyJ9")
        self.assertTrue(res["success"])
        self.assertIn('"status": "success"', res["text"])

    def test_decode_invalid_base64(self):
        res = decode_base64_string("not_valid_base64_%%%")
        self.assertFalse(res["success"])
        self.assertIn("Invalid Base64 string", res["error"])

    def test_unicode_encoding(self):
        text = "DeveloperOS 🇮🇳 ✨"
        res = encode_string_to_data_uri(text)
        dec = decode_base64_string(res["base64_string"])
        self.assertEqual(dec["text"], text)

    def test_validate_svg_clean(self):
        svg = '<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg>'
        val = validate_svg_asset(svg)
        self.assertTrue(val["is_valid"])
        self.assertEqual(val["viewbox"], "0 0 100 100")
        self.assertFalse(val["has_script"])

    def test_validate_svg_malicious_script(self):
        svg = '<svg><script>alert("xss")</script><circle cx="10" cy="10" r="5"/></svg>'
        val = validate_svg_asset(svg)
        self.assertFalse(val["is_valid"])
        self.assertTrue(val["has_script"])
        self.assertIn("Security warning", val["error"])


if __name__ == "__main__":
    unittest.main()
