import streamlit as st
from render_svg import main
from generator import generate_sequence_question

st.set_page_config(page_title="NVR Prototype", layout="centered")

st.title("🧠 NVR Prototype – Auto Generated Question")

# Generate question
question = generate_sequence_question()

# Render images
main()

st.subheader("Question")
st.image("stem.svg")

st.subheader("Options")

letters = ["a", "b", "c", "d"]
cols = st.columns(4)

selected = None

for i, col in enumerate(cols):
    with col:
        st.image(f"opt_{letters[i]}.svg")
        if st.button(f"Option {letters[i].upper()}", key=letters[i]):
            selected = i

if selected is not None:
    if selected == question["correct_index"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Not quite. Try again.")
