import streamlit as st

st.title("Welcome to Streamlit!")
name = st.text_input("Enter Your Name")

if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.warning("Enter your Name")

