##verify user exercise##
##the final listing for remember_me assumes either the user already entered
#their username or that the program is running for the first time

#we shhould modify it in case the current user is not the person who last used the program
#before printing a welcome back message in greet_user() ask the user if this is the
#correct username. if its not, call get_new_username() to get the correct username

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
        confirmation = input(f"is your username {user['username']}? (y/n)")
        if confirmation.lower() not in ['y','yes']:
            user = get_new_user(path)
        else:
            print(f"welcome back, {user['name']}. Your username is {user['username']}" 
                f"and you are {user['age']} years old")
    else:
        user = get_new_user(path)
        print(f"well remember you when your back, {user['username']}!")

greet_user()