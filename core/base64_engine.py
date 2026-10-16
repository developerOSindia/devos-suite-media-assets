"""
Pure business logic for Base64 and media data URI encoding/decoding.
Zero Streamlit or UI dependencies.
"""

import base64
import binascii
from typing import Dict, Any


def encode_string_to_data_uri(content: str, mime_type: str = "text/plain") -> Dict[str, Any]:
    """Encodes a string into standard Base64 and data URI representations."""
    raw_bytes = content.encode("utf-8")
    encoded_b64 = base64.b64encode(raw_bytes).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded_b64}"

    return {
        "raw_length": len(content),
        "byte_length": len(raw_bytes),
        "base64_string": encoded_b64,
        "data_uri": data_uri,
        "css_background": f"background-image: url('{data_uri}');",
    }


def decode_base64_string(b64_string: str) -> Dict[str, Any]:
    """Decodes a Base64 string safely."""
    clean = b64_string.strip()
    if clean.startswith("data:") and ";base64," in clean:
        clean = clean.split(";base64,")[1]

    try:
        decoded_bytes = base64.b64decode(clean, validate=True)
        decoded_text = decoded_bytes.decode("utf-8", errors="replace")
        return {
            "success": True,
            "text": decoded_text,
            "byte_count": len(decoded_bytes),
            "error": None,
        }
    except (binascii.Error, ValueError) as err:
        return {
            "success": False,
            "text": "",
            "byte_count": 0,
            "error": f"Invalid Base64 string: {str(err)}",
        }
