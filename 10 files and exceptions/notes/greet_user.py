from pathlib import Path
import json

path = Path("./10 files and exceptions/notes/username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"welcome back, {username}")

#by creating a variable path and assigning the Path instance it loads the contents
#of its parenthesis 
#we create a variable contents and assign it the path variable whilst applying the method
#read text which returns a string
#we create a new variable username which loads the contents from the json format to python object
#we print welcome back and the username variable


