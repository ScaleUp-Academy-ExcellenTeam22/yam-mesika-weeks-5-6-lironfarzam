# "w5e4"

# connected vessels
'''
 Write a function called interleave that gets one or more iterable parameters, and returns a list of intertwined members.
'''

# function to interleave lists
def interleave(*iterable):
    longest = max(len(i) for i in iterable)
    result = []
    j = 0
    #Run like this on the loop because it is important that the first members of each list appear first
    while j < longest:
        for i in range(len(iterable)):
            if j < len(iterable[i]):
                result.append(iterable[i][j])
        j += 1

    return result

# print(interleave('abc', [1, 2, 3], ('!', '@', '#', '$')))

# function to interleave lists
def interleave_generator(*iterable):
    longest = max(len(i) for i in iterable)
    result = []
    j = 0
    while j < longest:
        for i in range(len(iterable)):
            if j < len(iterable[i]):
                yield (iterable[i][j])
        j += 1


# our_generator = interleave_generator('abc', [1, 2, 3], ('!', '@', '#', '$'))
# for i in our_generator:
#     print(i)


#Harry is rational but not terrible
"""
The librarian who was on his way to bring me the coveted copy of "Harry Potter and the Rational Method" stumbled.
The books flew by and the book chapters scattered everywhere.
The resources folder contains a compressed file with all the chapters of the story, but unfortunately the name of the files does not match their contents.
Rename each file so that its new name is a three-digit number that describes the chapter number, followed by the chapter name.
For example: For the first episode, the file name should be 001 A Day of Very Low Probability.
During the exercise you may need to combine work with some libraries, including those we have not studied.
"""
import os
import re
import codecs
from bs4 import BeautifulSoup

#function get num in string ang make it 3 digits long and return it as a string
def three_digits(num):
    if len(num) == 3:
        return num
    elif len(num) == 2:
        return '0' + num
    elif len(num) == 1:
        return '00' + num
    else:
        return '000'

# function get string cut the head and split to num and title
def getCapterNumAndTitel(str):
    head = "Chapter"
    temp = str[len(head):]
    ret1 =""
    ret2 = ""
    i = 0

    #Capter num
    while temp[i] != ":":
        ret1 += temp[i]
        i = i+1

    i = i+1
    #Capter title
    while i < len(temp) and temp[i] != "<":
        if temp[i] != "\n" and temp[i] != ":":
            ret2 += temp[i]
        i = i+1

    return three_digits(ret1.replace(" ", "")),ret2


def rename(path):

    str=""
    for filename in os.listdir(path):
        file = codecs.open(path + "/" + filename, "r", encoding="utf8")
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find(id="chapter-title")
        chapterNum, chapterTitel = getCapterNumAndTitel(div.get_text())
        file.close()
        new_name = chapterNum + chapterTitel
        os.rename(os.path.join(path + "/", filename), os.path.join(path + "/", new_name + '.html'))

rename("Harry")