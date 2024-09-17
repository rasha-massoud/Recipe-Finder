import streamlit as st
from utils.api import fetch_recipes_by_ingredients, search_recipes_by_name


# Sidebar with options to choose between searching by name or ingredients
search_option = st.sidebar.selectbox(
    "Search by",
    ["Name", "Ingredients"],
    index=0
)

if search_option == "Name":
    st.title("Recipe Finder 🍲")

    st.header("Search by Dish Name")
    dish_name = st.text_input("Enter the dish name:")
    
    if st.button("Search Recipes by Name"):
        if dish_name:
            with st.spinner("Searching recipes..."):
                recipes = search_recipes_by_name(dish_name)
                if recipes.get('results'):
                    st.write(f"Found {len(recipes['results'])} recipes:")
                    for recipe in recipes['results']:
                        st.subheader(recipe['title'])
                        st.image(recipe.get('image', ''), use_column_width=True)
                        st.write(f"Ready in {recipe.get('readyInMinutes', 'N/A')} minutes")
                        st.write(f"Servings: {recipe.get('servings', 'N/A')}")
                        st.markdown(f"[View Recipe](https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']})")
                else:
                    st.write("No recipes found.")
        else:
            st.warning("Please enter a dish name.")

elif search_option == "Ingredients":
    
    st.title("Recipe Finder 🍲")
    st.header("Search Recipes by Ingredients")
    st.write("Enter ingredients you have, and we'll find recipes for you!")

    ingredients = st.text_input("Enter ingredients separated by commas", "Apples, Flour, Sugar")
    
    # Ranking and ignore pantry options
    ranking = st.selectbox("How would you like to rank the recipes?", options=["Maximize used ingredients", "Minimize missing ingredients"])
    ranking_value = 1 if ranking == "Maximize used ingredients" else 2
    ignore_pantry = st.checkbox("Ignore common pantry items (like water, salt, etc.)", value=True)

    if st.button("Search Recipes"):
        with st.spinner("Fetching recipes..."):
            recipes = fetch_recipes_by_ingredients(ingredients, ranking_value, ignore_pantry)
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
