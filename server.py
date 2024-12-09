import requests
from flask import Flask, request, jsonify, render_template
import json
from rapidfuzz import process
import os

# Initialize Flask app
app = Flask(__name__)

# Public URL of the Google Cloud Storage file
INDEXED_RECIPES_URL = "https://storage.googleapis.com/recipe-storage/indexed_recipes.json"  # Replace <BUCKET_NAME> with your bucket name.

# Load the indexed recipes from Google Cloud Storage
try:
    response = requests.get(INDEXED_RECIPES_URL)
    response.raise_for_status()  # Raise an error for bad status codes
    indexed_recipes = response.json()  # Parse the JSON content
except Exception as e:
    indexed_recipes = {}
    print(f"Error loading indexed_recipes.json: {e}")

# Search recipe by title with fuzzy matching
def search_recipe_by_title(query):
    query = query.lower()
    closest_match = process.extractOne(query, indexed_recipes.keys(), score_cutoff=70)  # Adjust score_cutoff as needed
    if closest_match:
        return indexed_recipes[closest_match[0]]
    return None

# Search for a recipe via GET request (from the browser)
@app.route('/get_recipe', methods=['GET'])
def get_recipe_get():
    query = request.args.get('query')  # Accept query from URL
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Search for recipes based on query
    recipe = search_recipe_by_title(query)
    print(f"Recipe found: {recipe}")  # Debugging output to verify the data

    if recipe:
        # If a list is returned, pass the list; otherwise, pass the dictionary
        return render_template('recipe_result.html', recipe=recipe if isinstance(recipe, list) else [recipe])
    else:
        return render_template('recipe_result.html', recipe=None)  # If no recipe is found

# Home page with search bar
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
