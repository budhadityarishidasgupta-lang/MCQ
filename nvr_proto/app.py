import streamlit as st
from render_svg import main
from generator import generate_sequence_question

st.set_page_config(page_title="NVR Prototype", layout="centered")
st.title("🧠 NVR Prototype – Auto Generated Question")

# --- SESSION STATE ---
if "question" not in st.session_state:
    st.session_state.question = generate_sequence_question()
    main()

question = st.session_state.question

# --- QUESTION ---
st.subheader("Question")
st.image("stem.svg")

# --- OPTIONS ---
st.subheader("Options")

letters = ["a", "b", "c", "d"]
cols = st.columns(4)

selected = None

for i, col in enumerate(cols):
    with col:
        st.image(f"opt_{letters[i]}.svg")
        if st.button(f"Option {letters[i].upper()}", key=f"opt_{i}"):
            selected = i

# --- FEEDBACK ---
if selected is not None:
    if selected == question["correct_index"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Not quite. Try again.")

# --- NEXT QUESTION ---
st.markdown("---")

if st.button("Next Question ▶️"):
    st.session_state.question = generate_sequence_question()
    main()
    st.experimental_rerun()
