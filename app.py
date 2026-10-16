"""
DeveloperOS Media & Assets Suite - Interactive Application
"""

import streamlit as st
from core.base64_engine import encode_string_to_data_uri, decode_base64_string
from ui.components import render_suite_header, render_suite_footer, render_main_promotional_banner

st.set_page_config(
    page_title="DeveloperOS - Media Suite",
    page_icon="🎨",
    layout="wide",
)


def main():
    render_suite_header(
        title="Base64 & Data URI Media Encoder / Decoder",
        description="Encode text, SVG strings, and media assets into production CSS data URIs or decode raw Base64 bytes.",
    )

    tab_encode, tab_decode = st.tabs(["Encode to Data URI", "Decode Base64"])

    with tab_encode:
        sample_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#38bdf8"/></svg>'
        raw_input = st.text_area("Input Text or SVG Markup:", value=sample_svg, height=120)
        mime = st.selectbox("MIME Type", ["image/svg+xml", "text/plain", "application/json"])

        if raw_input:
            encoded = encode_string_to_data_uri(raw_input, mime_type=mime)
            st.subheader("Data URI Output")
            st.code(encoded["data_uri"], language="text")

            st.subheader("CSS Background Snippet")
            st.code(encoded["css_background"], language="css")

    with tab_decode:
        b64_in = st.text_area("Input Base64 String to Decode:", value="RGV2ZWxvcGVyT1MgVG9vbHM=", height=100)
        if b64_in:
            decoded = decode_base64_string(b64_in)
            if decoded["success"]:
                st.success("Successfully Decoded!")
                st.text_area("Decoded Text Output:", value=decoded["text"], height=100)
            else:
                st.error(decoded["error"])

    render_main_promotional_banner()
    render_suite_footer()


if __name__ == "__main__":
    main()
