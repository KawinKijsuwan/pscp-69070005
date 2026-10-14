"""Pad Thai"""
best_ingredient = {"Pad Thai Sauce","Tofu",
                   "Pickle Turnip","Shrimp","Bean Sprouts",
                   "Noodle","Chives","Lime","Egg","Oil","Peanuts"}
best_taste = {"Sweet","Sour","Salty"}

ingredients = []
tastes_list = []

while True:
    item = input()
    if item == "Cook":
        break
    ingredients.append(item)

while True:
    tastes = input()
    if tastes == "End":
        break
    tastes_list.append(tastes)
ingredients_set = set(ingredients)
tastes_set = set(tastes_list)

if not ingredients_set.issubset(best_ingredient):
    print("This is not Pad Thai!!!")
elif ingredients_set != best_ingredient:
    print("This is bad!")
elif tastes_set != best_taste:
    print("Not Bad...")
else:
    print("Delicious!")
