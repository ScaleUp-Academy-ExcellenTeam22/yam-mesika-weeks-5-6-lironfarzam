# Cup of join
from functools import reduce


def join(*list_of_lists, separator='-'):
    """
    function receives an unlimited number of lists.
    The function must return one list consisting of all the lists received as parameters.
    If the sep parameter is provided, it should be threaded as an element between any two lists.
    If not provided, the character "-" should be threaded in place.

    :param list_of_lists: receives an unlimited number of lists, each list as a parameter
    :param separator: element between any two lists
    :return: return one list consisting of all the lists received as parameters
    """
    if len(list_of_lists) == 0:  # if no argument is provided
        return None
    new_list = [element for a_list in list_of_lists for element in a_list + [separator]]
    return new_list


# get_recipe_price
"""

An authority parameter called optionals that will get a list of components that we will ignore, that is - we will not buy from them at all.
If the parameter is not specified, all the transferred components must be considered.
For each component transferred in ingredients, an argument bearing the component name must be passed.
The value of the argument should be the quantity of the ingredient (in grams) from which we want to buy for the recipe.
The function will return the price we have to pay for buying all the groceries.
"""

def get_recipe_price(ingredients, optionals=[], **prices):
    """
    A function that receives a list of shopping prices and a list of products
    that are not mandatory to buy. Thinks how much to pay in total for the product
    list after missing the non-mandatory products

    :param ingredients: dict of ingredients which we want to buy by gram.
    :param optionals: list of ingredients which we don't need to buy.
    :param prices: dict of ingredients and prices.
    :return: total prices for all the ingredients we need to buy.
    """

    total = 0
    # for ingredient in ingredients:
    #     if ingredient not in optionals:
    #         total += (prices[ingredient] * ingredients[ingredient] / 100)

    # total = reduce(lambda ingredient, val: val + (prices[ingredient] * ingredients[ingredient] / 100 if ingredient not in optionals else 0), ingredients)

    total = sum((prices[ingredient] * ingredients[ingredient] / 100) for ingredient in ingredients if ingredient not in optionals)

    return total
