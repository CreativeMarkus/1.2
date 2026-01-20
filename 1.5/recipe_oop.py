class Recipe:
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cooking_time(self, time):
        self.cooking_time = time

    def get_cooking_time(self):
        return self.cooking_time

    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        return (
            f"\nRecipe: {self.name}"
            f"\nCooking Time: {self.cooking_time} minutes"
            f"\nIngredients: {', '.join(self.ingredients)}"
            f"\nDifficulty: {self.get_difficulty()}"
        )


def recipe_search(data, search_term):
    print(f"\nSearching for recipes with: {search_term}")
    print("-" * 40)
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)



tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
print(cake)

smoothie = Recipe("Banana Smoothie")
smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
smoothie.set_cooking_time(5)
print(smoothie)

recipes_list = [tea, coffee, cake, smoothie]

recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")
