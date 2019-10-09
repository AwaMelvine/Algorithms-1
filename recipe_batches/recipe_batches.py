#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    for i in recipe.keys():
        if i not in ingredients:
            return 0
        if i in ingredients and ingredients[i] >= recipe[i]:
            itemRecipeCount = int(ingredients[i]/recipe[i])
            batches.append(itemRecipeCount)
        if i in ingredients and ingredients[i] < recipe[i]:
          return 0

    min = batches[0]
    for i in range(len(batches)):
        if batches[i] < min:
            min = batches[i]
    return min


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
