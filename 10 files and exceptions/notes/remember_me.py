##SAVING AND READING USER-GENERATED DATA##

#saving data with json is useful when your working with user-generated data
#you will lose the information when program stops running
#eg

from pathlib import Path
import json

username = input("what is your name?:")

path = Path('./10 files and exceptions/notes/username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"we will remember you, {username}!")

#json.dumps converts the info into a json ready format (from python object to str)
#allowing us to write text to the path


