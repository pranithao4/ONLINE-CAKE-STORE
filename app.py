import streamlit as st
from pathlib import Path

html_path = Path(__file__).parent / "login.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_data = f.read()

st.components.v1.html(html_data, height=1000, scrolling=True)
