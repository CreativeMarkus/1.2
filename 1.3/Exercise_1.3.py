recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))

    ingredients = []
    num_ingredients = int(input("How many ingredients?: "))

    for i in range(num_ingredients):
        ingredient = input("Enter ingredient: ")
        ingredients.append(ingredient)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe


n = int(input("How many recipes would you like to enter?: "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)


for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print("\nRecipe:", recipe["name"])
    print("Cooking Time (min):", recipe["cooking_time"])
    print("Ingredients:")
    
    for ingredient in recipe["ingredients"]:
        print(ingredient)
        
    print("Difficulty level:", difficulty)


ingredients_list.sort()

print("\nAll Ingredients:")
for ingredient in ingredients_list:
    print(ingredient)