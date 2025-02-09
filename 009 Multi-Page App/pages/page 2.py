import streamlit as st 

name = st.text_input("Enter your Name")

if name:
    st.write(f"Hello, {name}!")