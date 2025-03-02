import streamlit as st # type: ignore
import random
from challenges import daily_challenges
from quotes import motivational_quotes

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Select a random challenge & quote
daily_challenge = random.choice(daily_challenges)
daily_quote = random.choice(motivational_quotes)

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
