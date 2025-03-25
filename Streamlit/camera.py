import streamlit as st
import pandas as pd

# Tittle
st.title("My first app")

# Header
st.header("this is header")

# text
st.text("hello streamlit")

# st.camera_input(label="hello")
st.exception(ValueError("This is an exception of type ValueError"))

st.text("Iron Man")
st.warning("This is a warning")
st.error("This is an error")
st.success("This is a success")
st.info("This is a info")


st.checkbox("I agree")
st.radio("What is your favorite color", ["Red", "Blue", "Green"])
st.selectbox("Which is your favorite movie", ["Endgame", "Infinity War", "Thor Rangnarok"])
st.multiselect("Which is you favorite animal", ["Fox", "Dog", "Sandip"])
st.slider("What is your level", 0, 100)
st.text_input("What is your name")
st.number_input("What is your age")
st.text_area("What is your address")
st.date_input("What is your birthday")
st.pills("pick the language",["Python", "Java", "C++"])
st.button("Submit")
st.file_uploader("Upload a file")
st.color_picker("Pick a color")
st.write("This is a write")
st.write(pd.DataFrame({
    "Name": ["Sandip", "Sagar", "Sabin"],
    "Age": [23, 24, 25]
}))

st.map({
    'latitude': [27.7172], 
    'longitude': [ 85.3240]
})


#BMI Calculator
st.title("BMI Calculator")
weight = st.number_input("Enter your weight in kg")
height = st.radio("Select your height fromat", ["cms", "meters", "feet"])
height = st.number_input("Enter your height")
if st.button("Calculate BMI"):
    if height == "cms":
        bmi = weight / ((height/100)**2)
    elif height == "meters":
        bmi = weight / height**2
    else:
        bmi = weight / ((height/3.28)**2)
    st.write(f"Your BMI is {bmi}")
    if bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        st.success("Normal weight")
    elif bmi >= 25 and bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obesity")
        