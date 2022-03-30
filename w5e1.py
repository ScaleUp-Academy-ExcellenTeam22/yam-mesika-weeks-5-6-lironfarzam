"w5e1" 
import random
import os
from datetime import datetime, timedelta

MONDAY = 1


def pokemon():
    """ Function  just to try "random" in python.
    from the tuple POKEMONS chose one random
    and print the chaise """

    POKEMONS = ('Bulbasaur', 'Squirtle', 'Charmander')
    starter_pokemon = random.choice(POKEMONS)
    print(starter_pokemon)


'''
 This Is The Way
 Write a function that gets a path to the folder,
 and returns the list of all files that begin with the
 "startsWith" letter sequence in that folder.
'''


def search_files_starts_with_in_folder(folder_path_to_search_in: str, starts_with: str) -> list:
    """
    :param folder_path_to_search_in: string. the full path for folder to search in it.
    :param starts_with: string. what is the start of file to search.
    :return:list. list of all file how start whit given parameter.(empty if nat enemy)
    """
    list_files = os.listdir(folder_path_to_search_in)
    list_deep_files = [file for file in list_files if file.startswith(starts_with)]
    return list_deep_files


'''
I have no vinaigrette
Write software that receives as input from the user two dates in the configuration: YYYY-MM-DD.
The software will grill a new date that is between the two dates that the user entered as input.
For example, for inputs 1912-06-23 and 1954-06-07, a possible output is 1939-09-03.
Since I only go to the grocery store on Mondays and I am a heavy consumer of vinaigrette sauce,
 if the date falls on Monday, print: "I do not have vinaigrette!"
'''


def i_Have_no_vinaigrette() -> str:
    """
    function get from user 2 date and random chose day between them.
    calculate if the chosen date is monday.
    if it's monday return : "I do not have vinaigrette!"
    else return           : "Here is your sauce, it's 21.90 please"
    :return:
    the answer of the shopkeeper depend the day in the week.
    """
    first_date = input("Enter first date: ")
    while not is_valid_date(first_date):
        first_date = input("Enter first valid date: (YYYY-MM-DD.)")

    second_date = input("Enter second date: ")
    while not is_valid_date(second_date):
        second_date = input("Enter second valid date: (YYYY-MM-DD.)")

    early_date = datetime.strptime(min(first_date, second_date), '%Y-%m-%d')
    late_date = datetime.strptime(max(first_date, second_date), '%Y-%m-%d')

    day_in_week = get_day_of_week(random_date(early_date, late_date))

    return "I do not have vinaigrette!" if day_in_week == MONDAY else "Here is your sauce, it's 21.90 please"


def is_valid_date(date):
    """
    function to find if given date is a really a date
    :param date:date yyyy-mm-dd
    :return:if it is a valid date
    """
    try:
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False


def random_date(start, end):
    """
    :param start: start date of limit
    :param end: end date of limit
    :return: random date between them
    """
    return start + timedelta(days=random.randint(0, (end - start).days))


def get_day_of_week(date):
    """
    :param date: date
    :return: day of the week
    """
    return date.weekday()
