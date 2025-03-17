import streamlit as st

# Title of the app
st.title("Streamlit Example: Age Calculator")

# User input: name and age
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)

# Button to trigger calculation
if st.button("Submit"):
    # Check if both name and age are provided
    if name and age:
        years_until_100 = 100 - age
        st.write(f"Hello, {name}!")
        st.write(f"You are {age} years old. You will turn 100 in {years_until_100} years.")
    else:
        st.warning("Please enter both your name and age.")

