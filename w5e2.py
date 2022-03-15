#Cup of join
''' Write a function called join, which receives an unlimited number of lists, each list as a parameter.
 The function must be able to have another parameter called september.
 The function must return one list consisting of all the lists received as parameters.
 If the sep parameter is provided, it should be threaded as an element between any two lists. If not provided, the character "-" should be threaded in place.
'''
def join(*args, sep='-'):
    if len(args) == 0:  # if no argument is provided
        return None
    list =[]
    for arg in args:
        for i in arg:
            list.append(i)
        list.append(sep)
    list.pop() # remove the last element of the list
    return list  

#get_recipe_price
"""
Realize a function called get_recipe_price, which has:
A parameter called prices, which will get a dictionary of ingredients needed to make a particular recipe.
The key to the dictionary will be the name of the product, and the value of the dictionary will be its price per 100 grams.
Assume that the name of each element is one word, with no spaces and no special characters.
An authority parameter called optionals that will get a list of components that we will ignore, that is - we will not buy from them at all.
If the parameter is not specified, all the transferred components must be considered.
For each component transferred in ingredients, an argument bearing the component name must be passed.
The value of the argument should be the quantity of the ingredient (in grams) from which we want to buy for the recipe.
The function will return the price we have to pay for buying all the groceries.
"""
def get_recipe_price(ingredients, optionals=[], **prices):
    total = 0
    for ingredient in ingredients:
        if ingredient not in optionals:
            total += (prices[ingredient] * ingredients[ingredient] / 100)
            
    return total

