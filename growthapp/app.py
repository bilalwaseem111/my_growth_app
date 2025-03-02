import streamlit as st  # type: ignore
import random
import os
from challenges import daily_challenges
from quotes import motivational_quotes

# Load CSS
def load_css():
    css_file = "style.css"
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ CSS file not found! Make sure 'style.css' is in the same folder as 'app.py'.")

# Select a random challenge & quote
daily_challenge = random.choice(daily_challenges) if daily_challenges else "No challenges available."
daily_quote = random.choice(motivational_quotes) if motivational_quotes else "No quotes available."

# Streamlit App UI
st.title("🚀 Growth Mind Challenge App")
load_css()

st.header("🌱 Your Challenge for Today:")
st.info(daily_challenge)

st.header("💡 Motivational Quote:")
st.success(f"*{daily_quote}*")

# User Progress Tracking
st.subheader("✅ Track Your Progress")
progress = st.slider("How much did you complete today's challenge?", 0, 100, 0)
if progress > 0:
    st.write(f"Great job! You're {progress}% closer to a growth mindset! 🎯")

# Footer
st.markdown("---")
st.markdown("💪 Keep pushing forward! Growth comes with consistency. 🚀")
