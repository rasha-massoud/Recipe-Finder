import streamlit as st

st.title("Recipe Finder 🍲")
st.write("Enter ingredients you have, and we'll find recipes for you!")

ingredients = st.text_input("Enter ingredients separated by commas", "Apples, Flour, Sugar")