# connected vessels

def interleave(*iterable):
    """
    gets one or more iterable parameters, and returns a list of intertwined members.
    function to interleave lists
    :param iterable:
    :return:
    """
    longest = max(len(index) for index in iterable)
    result = []
    counter = 0
    # Run like this on the loop because it is important
    # that the first members of each list appear first
    while counter < longest:
        for index in range(len(iterable)):
            if counter < len(iterable[index]):
                result.append(iterable[index][counter])
        counter += 1

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
                yield iterable[i][j]
        j += 1


# our_generator = interleave_generator('abc', [1, 2, 3], ('!', '@', '#', '$'))
# for i in our_generator:
#     print(i)


# Harry is rational but not terrible
"""
The librarian who was on his way to bring me the coveted copy of "Harry Potter and the Rational Method" stumbled.
The books flew by and the book chapters scattered everywhere.
The resources folder contains a compressed file with all the chapters of the story, but unfortunately the name of the files does not match their contents.
Rename each file so that its new name is a three-digit number that describes the chapter number, followed by the chapter name.
For example: For the first episode, the file name should be 001 A Day of Very Low Probability.
During the exercise you may need to combine work with some libraries, including those we have not studied.
"""
import os
import codecs
from bs4 import BeautifulSoup


def three_digits(num: str) -> str:
    """
    function get num in string ang make it 3 digits long and return it as a string
    :param num: num in string
    :return: 3 digits long
    """
    while len(num) != 3:
        num = '0' + num

    return num


def get_chapter_num_and_title(str):
    """
    function get string cut the head and split to num and title
    :param str: string
    :return: num of chapter and title
    """
    head = "Chapter"
    temp = str[len(head):]
    ret1 = ""
    ret2 = ""
    i = 0

    # Chapter num
    while temp[i] != ":":
        ret1 += temp[i]
        i = i + 1

    i = i + 1
    # Chapter title
    while i < len(temp) and temp[i] != "<":
        if temp[i] != "\n" and temp[i] != ":":
            ret2 += temp[i]
        i = i + 1

    return three_digits(ret1.replace(" ", "")), ret2


def rename(path):
    str = ""
    for file_name in os.listdir(path):
        file_to_change_name = codecs.open(path + "/" + file_name, "r", encoding="utf8")
        html = file_to_change_name.read()
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find(id="chapter-title")
        chapterNum, chapter_title = get_chapter_num_and_title(div.get_text())
        file_to_change_name.close()
        new_name = chapterNum + chapter_title
        os.rename(os.path.join(path + "/", file_name), os.path.join(path + "/", new_name + '.html'))


if __name__ == "__main__":
    print(three_digits("1"))
    print(three_digits("12"))
    print(three_digits("123"))
