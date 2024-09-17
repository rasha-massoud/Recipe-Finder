import streamlit as st

st.title("Recipe Finder 🍲")
st.write("Enter ingredients you have, and we'll find recipes for you!")

ingredients = st.text_input("Enter ingredients separated by commas", "Apples, Flour, Sugar")

ranking = st.selectbox("How would you like to rank the recipes?", options=["Maximize used ingredients", "Minimize missing ingredients"])
ranking_value = 1 if ranking == "Maximize used ingredients" else 2

ignore_pantry = st.checkbox("Ignore common pantry items (like water, salt, etc.)", value=True)