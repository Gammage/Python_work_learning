##READ DATA BACK INTO PROGRAM/MEMORY##

from pathlib import Path
import json

path = Path('./10 files and exceptions/notes/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)

#we make sure to read the same file we wrote to
#as the data in file is just a text file with specific formatting, we can read
#it with the read_text() method
#we pass the contents of file to json.loads()
#this function takes in a json-formatted string and returns a python object
    #(in this case a list) which we assign to numbers

