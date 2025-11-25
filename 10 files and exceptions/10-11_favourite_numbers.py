##FAVOURITE NUMBERS EXERCISE##

#write a program that prompts for the users favourite number.
#use json.dumps() to store that number in a file
#write a seperate progrma that reads in this value and prints the message
#i know your favourite number! its __

from pathlib import Path
import json

message = input("what is your favourite number?")

path = Path('./10 files and exceptions/favourite_numbers_exercise.json')
contents = json.dumps(message)
path.write_text(contents)

