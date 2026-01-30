import streamlit as st
import os
from render_svg import main

st.set_page_config(page_title="NVR Prototype", layout="centered")

st.title("🧠 NVR Prototype – Auto Generated Question")

# Run generator + renderer
main()

st.subheader("Question")
st.image("stem.svg")

st.subheader("Options")
cols = st.columns(4)

letters = ["a", "b", "c", "d"]
for i, col in enumerate(cols):
    with col:
        st.image(f"opt_{letters[i]}.svg")
        st.caption(letters[i].upper())
