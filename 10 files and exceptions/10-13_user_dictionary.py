##User dictionary exercise##
##the remember me example only stores one piece of information, the user
#expand this example by asking for two more pieces of information about the user,
#then store all the information you collect in a dictionary.
    #write the dictionary to a file using json.dumps() and read it back in using
    #json.loads(). print a summary showing exactly what your program remembers 
    #about the user
    
from pathlib import Path
import json

def get_stored_user(path):
    """get stored user if available"""
    
    if path.exists():
        contents= path.read_text()
        user= json.loads(contents)
        return user
    else:
        return None
    
def get_new_user(path):
    """prompt for a new user"""
    user = {'username':None,
            'name':None,
            'age':None,}
    
    for key in user.keys():
        user[key] = input(f"what is your {key.title()}?".title())
    
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """greet user by name"""
    path = Path('./10 files and exceptions/user_dictionary_exercise.json')
    user = get_stored_user(path)
    if user:
        print(f"welcome back, {user['name']}. Your username is {user['username']}" 
              f"and you are {user['age']} years old")
    else:
        user = get_new_user(path)
        print(f"well remember you when your back, {user['username']}!")

greet_user()
