"w5e3"

#Parseltongue
"""
The course logo appears in the resources / logo.jpg file, and inside it are hidden some secret messages.
The messages are strings at least 5 letters long, written in small English letters only and ending with an exclamation mark.
Open the logo for reading in a binary configuration, and extract the secret messages from it.
Keep in mind that the file may be very large, and it is best not to read it all in one go.
Find help on the Internet regarding opening files in a binary form and a graded reading of the file.
Be careful not to use techniques we have not learned (or add them only in addition to such a solution).
"""

f = open('logo.jpg', 'rb')
file_content = f.read()

for i in file_content:
    print(i)
f.close()
