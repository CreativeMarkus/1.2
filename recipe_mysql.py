from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Matches your setup from the screenshot
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} ({self.difficulty})>"

Base.metadata.create_all(engine)

def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients.split(", "))
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe():
    name = input("Recipe name: ")
    try:
        cooking_time = int(input("Cooking time (mins): "))
        ingredients = input("Ingredients (comma and space separated): ")
        difficulty = calculate_difficulty(cooking_time, ingredients)
        
        new_recipe = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time, difficulty=difficulty)
        session.add(new_recipe)
        session.commit()
        print("Recipe added!")
    except ValueError:
        print("Invalid input for time. Please enter a number.")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("Database is empty.")
        return
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for row in results:
        for ing in row[0].split(", "):
            if ing not in all_ingredients: all_ingredients.append(ing)
    
    for i, ing in enumerate(all_ingredients): print(f"{i+1}. {ing}")
    try:
        choice = int(input("Select ingredient number: "))
        search_ing = all_ingredients[choice - 1]
        found = session.query(Recipe).filter(Recipe.ingredients.like(f"%{search_ing}%")).all()
        for r in found: print(r)
    except:
        print("Invalid selection.")

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes to edit.")
        return
    
    recipes = session.query(Recipe).all()
    for r in recipes:
        print(f"ID: {r.id} | Name: {r.name}")

    try:
        id_to_edit = int(input("ID to edit: "))
        recipe = session.query(Recipe).get(id_to_edit)
        if not recipe:
            print("Recipe not found.")
            return

        print("1. Name\n2. Cooking Time\n3. Ingredients")
        pick = input("Pick attribute: ")
        
        if pick == "1":
            recipe.name = input("Enter new name: ")
        elif pick == "2":
            recipe.cooking_time = int(input("Enter new time: "))
        elif pick == "3":
            recipe.ingredients = input("Enter new ingredients: ")

        recipe.difficulty = calculate_difficulty(recipe.cooking_time, recipe.ingredients)
        session.commit()
        print("Updated!")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_recipe():
    try:
        recipes = session.query(Recipe).all()
        for r in recipes:
            print(f"ID: {r.id} | Name: {r.name}")
        
        id_del = int(input("ID to delete: "))
        recipe = session.query(Recipe).get(id_del)
        if recipe:
            session.delete(recipe)
            session.commit()
            print("Deleted!")
        else:
            print("ID not found.")
    except:
        print("Invalid input.")

def main_menu():
    while True:
        print("\n--- Recipe Manager ---")
        print("1. Create\n2. View All\n3. Search\n4. Edit\n5. Delete\n6. Exit")
        choice = input("Option: ")

        if choice == '1': create_recipe()
        elif choice == '2': view_all_recipes()
        elif choice == '3': search_by_ingredients()
        elif choice == '4': edit_recipe()
        elif choice == '5': delete_recipe()
        elif choice == '6':
            session.close()
            break

if __name__ == "__main__":
    main_menu()