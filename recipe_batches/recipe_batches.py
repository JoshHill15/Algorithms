#!/usr/bin/python

import math

# O(n^2)


# def recipe_batches(recipe, ingredients):
#     recipeKeys = len(recipe.keys())
#     if recipeKeys != len(ingredients.keys()):
#         return 0
#     count = [0] * recipeKeys
#     a = 0
#     for i in recipe:
#         recipe[i] = ingredients[i] // recipe[i]
#         if recipe[i] > 0:
#             while recipe[i] > 0:
#                 count[a] += 1
#                 recipe[i] -= 1
#         a += 1
#     count.sort()
#     return count[0]


# O(n)

def recipe_batches(recipe, ingredients):
    recipeKeys = recipe.keys()
    if len(recipeKeys) <= len(ingredients.keys()):
        return 0
    for i in recipe:
        recipe[i] = ingredients[i] // recipe[i]
    smallestKey = min(recipeKeys, key=lambda i: recipe[i])
    return recipe[smallestKey]


print(recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {
      'milk': 5, 'sugar': 120, 'butter': 500}))


# print(recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 138, 'butter': 48, 'flour': 51}
# )) # 0
# print(recipe_batches(
#       {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5},
#       {'milk': 1288, 'flour': 9, 'sugar': 95})) # 0

# 1
# if __name__ == '__main__':
# Change the entries of these dictionaries to test
# your implementation with different inputs
# recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
# ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
# print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
