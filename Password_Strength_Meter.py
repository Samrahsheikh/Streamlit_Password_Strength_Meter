import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = ""

    # Conditions for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Assigning strength score based on criteria
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Strength level
    if strength == 5:
        remarks = "💪 Very Strong (Excellent!)"
        color = "green"
    elif strength == 4:
        remarks = "✅ Strong (Good Choice!)"
        color = "blue"
    elif strength == 3:
        remarks = "⚠️ Moderate (Could be Stronger)"
        color = "orange"
    elif strength == 2:
        remarks = "❌ Weak (Try Adding More Characters)"
        color = "red"
    else:
        remarks = "❌ Very Weak (Not Safe!)"
        color = "darkred"

    return strength, remarks, color

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Custom CSS for dark theme
st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
        }
        .stApp {
            background-color: white;
        }
        .stTextInput, .stTextArea {
            background-color: #333;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🔐 Password Strength Meter")

# User input
password = st.text_input("Enter your password:", type="password")

# Checking password strength
if password:
    strength, remarks, color = check_password_strength(password)

    # Display result
    st.markdown(f"<h3 style='color: {color};'>{remarks}</h3>", unsafe_allow_html=True)

    # Strength bar
    st.progress(strength / 5)

    # Suggestions
    st.subheader("🔹 Tips for a Stronger Password:")
    st.markdown("""
    - Use at least **8 characters**.
    - Include **uppercase & lowercase** letters.
    - Add **numbers (0-9)**.
    - Use **special characters (@, #, $, etc.)**.
    """)

