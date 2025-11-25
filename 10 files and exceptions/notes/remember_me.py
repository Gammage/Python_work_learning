##SAVING AND READING USER-GENERATED DATA##

#saving data with json is useful when your working with user-generated data
#you will lose the information when program stops running
#eg

# from pathlib import Path
# import json

# username = input("what is your name?:")

# path = Path('./10 files and exceptions/notes/username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"we will remember you, {username}!")

#json.dumps converts the info into a json ready format (from python object to str)
#allowing us to write text to the path


#many helpful methods you can use with path objects
#the exists() mehtod returns true if a file or folder exists and false if it doesnt
#if it exists we load username and print welcome back username

##REFACTORING##
#sometimes code can be changed (even if it works) and improved by breaking it down
#into functions

from pathlib import Path
import json  
        
def get_stored_username(path):
    """get stored username if available"""
    
    if path.exists():
        contents= path.read_text()
        username= json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """prompt for a new username"""
    username = input("what is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """greet user by name"""
    path = Path('./10 files and exceptions/notes/username.json')
    username = get_stored_username(path)
    if username:
        print(f"welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"well remember you when your back, {username}!")

greet_user()










