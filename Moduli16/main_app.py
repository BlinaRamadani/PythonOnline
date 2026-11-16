import streamlit as st

if st.button("Click Me"):
    st.write("Button Clicked!")

if st.checkbox("Check me to show some text"):
    st.write("You're seeing this text because you chacked the chackbox")

user_input = st.text_input("Enter text", "Sample text")

st.write("You entered:", user_input)

age = st.number_input("Enter your age", min_value=0, max_value=100)

at.write(f"Your age is: {age}")

message = st.text_area("Enter a message")

st.write(f"Your message: {message}")

choice = st.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])

st.write(f"You chose: {choice}")

if st.button("Success"):
    st.success("Operation was successful")

