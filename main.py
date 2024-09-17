# app.py
import streamlit as st
from utils.api import fetch_recipes

st.title("Recipe Finder 🍲")
st.write("Enter ingredients you have, and we'll find recipes for you!")

ingredients = st.text_input("Enter ingredients separated by commas", "Apples, Flour, Sugar")

ranking = st.selectbox("How would you like to rank the recipes?", options=["Maximize used ingredients", "Minimize missing ingredients"])
ranking_value = 1 if ranking == "Maximize used ingredients" else 2
ignore_pantry = st.checkbox("Ignore common pantry items (like water, salt, etc.)", value=True)

if st.button("Search Recipes"):
    with st.spinner("Fetching recipes..."):
        recipes = fetch_recipes(ingredients, ranking_value, ignore_pantry)
        if recipes:
            st.write(f"Found {len(recipes)} recipes:")
            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'], use_column_width=True)
                st.write(f"Used ingredients: {', '.join([ing['name'] for ing in recipe['usedIngredients']])}")
                st.write(f"Missing ingredients: {', '.join([ing['name'] for ing in recipe['missedIngredients']])}")
                st.markdown(f"[View Recipe](https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']})")
        else:
            st.write("No recipes found.")

