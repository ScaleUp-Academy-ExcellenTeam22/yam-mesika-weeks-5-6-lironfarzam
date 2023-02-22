#Parseltongue
"""
The course logo appears in the resources / logo.jpg file, and inside it are hidden some secret messages.
The messages are strings at least 5 letters long, written in small English letters only and ending with an exclamation mark.
Open the logo for reading in a binary configuration, and extract the secret messages from it.
Keep in mind that the file may be very large, and it is best not to read it all in one go.
Find help on the Internet regarding opening files in a binary form and a graded reading of the file.
Be careful not to use techniques we have not learned (or add them only in addition to such a solution).
"""
# open file binary mood
file_logo = open('logo.jpg', 'rb')
content = file_logo.read()
str = ""
for i in range(len(content)):
    if content[i] == ord("!"):
        j = i - 1
        # A loop for reading all the letters (a-z only)
        while j > 0 and ord("z") >= content[j] >= ord("a"):

            str += chr(content[j])
            j = j-1
        # Just words longer then 2
        if len(str) > 2:
            # Reverse printing because we read the letters from end to beginning
            print(str[::-1])
        # Reset str
        str = ""

file_logo.close()


