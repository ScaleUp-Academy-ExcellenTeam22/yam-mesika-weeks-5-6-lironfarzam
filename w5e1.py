"w5e1" 
import random
import os

# pokemon s1e1 -> Ash late to professor Oak so can't choose pokemon...
from datetime import datetime, timedelta

MONDAYS = 1


def pokemon():
    pokemons = ['Bulbasaur', 'Squirtle', 'Charmander']
    starter_pokemon = random.choice(pokemons)
    print(starter_pokemon)


'''
 This Is The Way
 Write a function that gets a path to the folder,
 and returns the list of all files that begin with the
 "startsWith" letter sequence in that folder.
'''


def startsWith_files(folder, startsWith):
    list_files = os.listdir(folder)
    list_deep_files = []
    for file in list_files:
        if file.startswith(startsWith):
            list_deep_files.append(file)
    return list_deep_files


# -----------------------------------------------------------------------#
'''
I have no vinaigrette
Write software that receives as input from the user two dates in the configuration: YYYY-MM-DD.
The software will grill a new date that is between the two dates that the user entered as input.
For example, for inputs 1912-06-23 and 1954-06-07, a possible output is 1939-09-03.
Since I only go to the grocery store on Mondays and I am a heavy consumer of vinaigrette sauce,
 if the date falls on Monday, print: "I do not have vinaigrette!"
'''


def IHaveNoVinaigrette():
    date1 = input("Enter first date: ")
    while not is_valid_date(date1):
        date1 = input("Enter first valid date: (YYYY-MM-DD.)")

    date2 = input("Enter second date: ")
    while not is_valid_date(date2):
        date2 = input("Enter second valid date: (YYYY-MM-DD.)")

    date1, date2 = datetime.strptime(min(date1, date2), '%Y-%m-%d'), datetime.strptime(max(date1, date2), '%Y-%m-%d')
    dayInWeek = get_day_of_week(random_date(date1, date2))
    if dayInWeek == MONDAYS:
        print("I do not have vinaigrette!")
    else:
        print("Here is your sauce, it's 21.90 please")


# function get date yyyy-mm-dd and retern if it is a valid date
def is_valid_date(date):
    try:
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False


# function get start date and end date and return random date between them
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


# function get date and return day of the week
def get_day_of_week(date):
    return date.weekday()


# -----------------------------------------------------------------------#

IHaveNoVinaigrette()
