import streamlit as st

st.title("My Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("Hello, welcome to my app!") 

if st.button("Click me!"):
    st.write("Button clicked!")

if st.checkbox("Check me!"):
    st.write("Checkbox checked!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

slider_value = st.slider("Select a number:", 0, 100, 50)
if slider_value:
    st.write(f"You selected: {slider_value}")
