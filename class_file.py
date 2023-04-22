import random as rdm


class Recipe:
    def __init__(self, name, ingredients, nutritional_facts):
        self.name = name
        self.ingredients = ingredients
        self.nutritional_facts = nutritional_facts

    def __str__(self):
        return f"\nRecipe: {self.name}\n"


class stored_recipe:
    def __init__(self, recipes):
        self.recipes = []
        for recipe in recipes:
            self.recipes.append(Recipe(recipe['Recipe'], recipe['Ingredients'], recipe['Nutritional facts']))

    def random_recipe(self):
        return rdm.choice(self.recipes)

'''To be continued...'''
recipes = [
    {
        "Recipe": "Grilled Chicken Salad",
        "Ingredients": [
            "4 oz. boneless, skinless chicken breast",
            "2 cups mixed greens",
            "1/2 cup cherry tomatoes",
            "1/4 cup sliced cucumber",
            "2 tbsp balsamic vinaigrette"
        ],
        "Nutritional facts": {
            "Calories : 250",
            "Protein : 20g",
            "Carbs : 10g",
            "Fat : 15g"
        }
    },
    {
        "Recipe": "Greek Yogurt Parfait",
        "Ingredients": [
            "1 cup non-fat Greek yogurt",
            "1/2 cup sliced strawberries",
            "1/2 cup blueberries",
            "2 tbsp honey",
            "1/4 cup granola"
        ],
        "Nutritional facts": {
            "Calories : 250",
            "Protein : 20g",
            "Carbs : 35g",
            "Fat : 5g"
        }
    },
    {
        "Recipe": "Roasted Salmon with Asparagus",
        "Ingredients": [
            "4 oz. salmon fillet",
            "1 cup asparagus",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories : 300",
            "Protein : 25g",
            "Carbs : 5g",
            "Fat : 20g"
        }
    },
    {
        "Recipe": "Turkey Chili",
        "Ingredients": [
            "1 lb. ground turkey",
            "1 can black beans",
            "1 can diced tomatoes",
            "1 onion, chopped",
            "1 green pepper, chopped",
            "2 cloves garlic, minced",
            "1 tbsp chili powder"
        ],
        "Nutritional facts": {
            "Calories : 300",
            "Protein : 25g",
            "Carbs : 25g",
            "Fat : 10g"
        }
    },
    {
        "Recipe": "Quinoa Salad with Vegetables",
        "Ingredients": [
            "1 cup cooked quinoa",
            "1/2 cup diced tomatoes",
            "1/2 cup diced cucumbers",
            "1/4 cup diced red onion",
            "1/4 cup feta cheese",
            "1 tbsp olive oil",
            "1 tbsp lemon juice"
        ],
        "Nutritional facts": {
            "Calories : 300",
            "Protein : 10g",
            "Carbs : 40g",
            "Fat : 10g"
        }
    },
    {
        "Recipe": "Grilled Tuna Steak",
        "Ingredients": [
            "4 oz. tuna steak",
            "1 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories : 200",
            "Protein : 25g",
            "Carbs : 0g",
            "Fat : 10g"
        }
    },
    {
        "Recipe": "Broiled Pork Chop",
        "Ingredients": [
            "4 oz. pork chop",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories : 300",
            "Protein : 25g",
            "Carbs : 0g",
            "Fat : 20g"
        }
    },

]
def border():
    print("\n", "*--*" * 20)

def suggested_recipe():
    recipe_list = stored_recipe(recipes)
    random_recipe = recipe_list.random_recipe()
    border()
    print(random_recipe)

    print("Ingredients:")
    for ingredient in random_recipe.ingredients:
        print("- " + ingredient)

    print("\nNutritional facts:")
    for fact in random_recipe.nutritional_facts:
        print("- " + fact)
    border()


#suggested_recipe()
