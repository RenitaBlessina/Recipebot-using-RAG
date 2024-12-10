# Cooking With Love

---

## **Recipebot-using-RAG**  
**Cooking With Love**  
A recipe chatbot website that allows users to search for recipes and explore popular categories.

---

## **Table of Contents**

1. [Project Description](#project-description)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Getting Started](#getting-started)  
5. [Usage](#usage)  
6. [Folder Structure](#folder-structure)  
7. [Team Members](#team-members)  

---

## **Project Description**

Cooking With Love is a user-friendly platform where users can search for recipes by name and explore popular recipe categories. The website combines a beautiful, responsive design with a powerful recipe retrieval system powered by Flask and OpenAI's API.

---

## **Features**

- **Recipe Search**: Enter a recipe name and get detailed information.  
- **Popular Categories**: Browse categories like Pasta, Pizza, and more.  
- **Ingredient-based Search**: Find recipes by specifying ingredients.  
- **Dietary Restrictions**: Search for recipes suitable for specific diets (e.g., gluten-free, vegan).  

---

## **Technologies Used**

- **Backend**: Flask  
- **Frontend**: HTML, CSS  
- **Search Engine**: Fuzzy matching with RapidFuzz  
- **Data**: Indexed recipes in JSON  
- **API Integration**: OpenAI GPT for enhanced recipe descriptions  

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:  
- Python 3.x  
- pip (Python package manager)  
- Flask (`pip install flask`)  
- RapidFuzz (`pip install rapidfuzz`)  
- dotenv (`pip install python-dotenv`)
- openapi(`pip install openapi`)

### **Setup**
1. Clone this repository:  
   ```bash
   git@github.com:RenitaBlessina/Recipebot-using-RAG.git
   cd Recipebot-using-RAG
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Create and configure the `.env` file:
   - In the project root directory, create a file named `.env`.
   - Add your OpenAI API key in the following format:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```
     
4. Prepare the recipe data:
   - Ensure you have the `indexed_recipes.json` file in the project directory.
   - This file contains the recipe data in JSON format, which the application uses to provide search results.

5. Run the Flask application:
   ```bash
   python3 server.py
6. Access the application:
   - Open your web browser and navigate to `http://127.0.0.1:5000` to view the application.

---

## **Usage**

1. Open the homepage in your browser.
2. Use the search bar to look for a recipe by name.
3. Filter recipes based on dietary restrictions or specific ingredients.

---

## **Folder Structure**
   ```bash
   cooking-with-love/
   ├── indexed_recipes.json      # Recipe data file
   ├── server.py                 # Main application file
   ├── templates/                # HTML templates
   │   ├── index.html            # Homepage template
   │   ├── recipe_result.html    # Recipe result display template
   ├── static/                   # Static files (e.g., CSS, images)
   ├── .env                      # Environment variables (not included in repo)
   ├── requirements.txt          # Dependencies
   └── README.md                 # Project documentation
```
---

## **Team Members**

- **Blair Jones**  
- **Niharika Narasimhiah Govinda**  
- **Renita Blessina Sathiaraj** 
- **Subashree Dinesh**  
 







   
