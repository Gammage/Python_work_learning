##STORING DATA##

#programs will ask users for data
#we will store info in lists and dictionaries
#when user close a program, will always want to store what they put

#simple way to do this is store data in a json module

#the json module allows you to convert simple python data structures into
#JSON-formatted strings, then load the data from that file next time program runs
#you can use json to share data between diff programs
#JSON data not specific to python so can share stored data between diff people 
#who may use diff programming languages
#useful, portable, simple to learn

#was originally for Javascript, however its a common format now :)

##Using json.dumps() and json.laods()

#a short program that stores a set of numbers and another program reads these numbers
#back into memory
#first program will use json.dumps() to store the set of numbers, second program
#will use json.loads()

from pathlib import Path
import json

numbers = [2,3,5,6,11,13]

path = Path('./10 files and exceptions/notes/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

#we import the json module
#we use the json.dumps() function to generate a string containing the JSON representation
#of the data where working with

#program has no output the data is stored in a format that looks just like python




