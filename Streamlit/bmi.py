import streamlit as st

# Set page title
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Styling for dark mode
st.markdown("""
    <style>
        body {
            background-color: #0e0e0e;
            color: white;
        }
        .stNumberInput input {
            background-color: #1a1a1a;
            color: white;
        }
        .stRadio [role=radiogroup] label {
            color: white;
        }
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton button:hover {
            background-color: #cc0000;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💪 BMI Calculator")

# Input for weight
weight = st.number_input("Enter your weight in kg",format="%.2f")

# Height selection
height_format = st.radio("Select your height format", ["cms", "meters", "feet"], index=0)

# Input for height
height = st.number_input("Enter your height", format="%.2f")

# Convert height to meters correctly
if height_format == "cms":
    height_in_meters = height / 100  # Convert cm to meters
elif height_format == "meters":
    height_in_meters = height
elif height_format == "feet":
    height_in_meters = height * 0.3048  # Convert feet to meters
else:
    height_in_meters = 0  # Safety check

# Ensure correct calculation
if st.button("Calculate BMI"):
    if weight > 0 and height_in_meters > 0:
        bmi = round(weight / (height_in_meters ** 2), 1)  # Round to 1 decimal place for accuracy
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal weight" if bmi < 24.9 else
            "Overweight" if bmi < 29.9 else
            "Obese"
        )
        st.success(f"Your BMI is: {bmi}")
        st.info(f"Category: {category}")
    else:
        st.error("Please enter valid values for weight and height.")
