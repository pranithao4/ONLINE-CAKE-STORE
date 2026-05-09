import streamlit as st

# Read HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Display HTML
st.components.v1.html(html_data, height=800, scrolling=True)