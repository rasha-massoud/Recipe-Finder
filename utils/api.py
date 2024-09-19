# utils/api.py
import requests

def fetch_recipes_by_ingredients(ingredients, ranking, ignore_pantry, API_KEY):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "number": 5,
        "ranking": ranking,
        "ignorePantry": str(ignore_pantry).lower(),
        "apiKey": API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def search_recipes_by_name(dish_name, API_KEY, number=5):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": dish_name,
        "number": number,
        "apiKey": API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return []
