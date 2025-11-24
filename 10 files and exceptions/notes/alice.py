#HANDLING THE FileNotFoundError EXCEPTION#
#common issue when working with files is handling missing files
#the file you're looking for might be in adifferent location, filename misspelled,
#file might not exist
#you can handle these with try-except block

#eg file that doesnt exist

# from pathlib import Path

# path = Path('./10 files and exceptions/alice.txt')
# contents = path.read_text(encoding='utf-8')

#encoding argument is needed when your system's default encoding doesnt match
#the encoding of the file that being read
#most likely to happen when reading froma  file that wasn't created on your system

#often best to start at the very end of the traceback
#this last line is important as it tells us what kind of exception to use in the
#except block

#to handle the error thats being raised, the try block will begin with the line that
#was identified as problamtic in the tracebook. in our example, this is the line
#that contains read_text()

# from pathlib import Path

# path = Path('./10 files and exceptions/alice.txt')

# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"sorry the file {path} does not exist")

#in this example, the code in the try block produces FileNotFoundError
#we write an except block that matches the error. python then runs the code in that
#block when the file cant be found, result is a friendly error message instead of
#a traceback

#an example to see how exception handling can help when your're working with more than
#one file

#analyzing text#
#you can analyze text files containing entire books
#many classic works of literature are available as simple text files because
#they are in the public domain
#texts used in this sectio come from project gutenberg
#project gutenberg maintains a collection of literary works that are available
#in the public domain, and its a great resource if you're interested in working with
#literary texts in your programming projects

from pathlib import Path

path = Path('./10 files and exceptions/notes/alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"sorry the file {path} does not exist")
else:
    #count the words in a file
    words = contents.split()
    num_words = len(words)
    print(f"the file from path '{path}' has about {num_words} words")
    
##WORKING WITH MULTIPLE FILES##

