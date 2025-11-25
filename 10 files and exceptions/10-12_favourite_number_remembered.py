##Favourite number remembered 10-12##

#combine the two programs you wrote in exercise 10-11  into one file
#if number is already stored, report the favourite number to the user
#prompt 


from pathlib import Path
import json


#we want to ask the user for a number.
#we want to see if the number is already stored
    #if it isnt, we should store it!

def ask_number():
    """ask user their favourite number"""
    path = Path('./10 files and exceptions/favourite_numbers_exercise.json')
    number = is_number_stored(path)
    
    if number:
        print(f"your favourite number is {number}")
    else:
        storing_number(path)
    
def is_number_stored(path):
    """check if number is stored"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def storing_number(path):
    """save number to file"""
    message = input("what is your favourite number?")
    contents = json.dumps(message)
    path.write_text(contents)

ask_number()

# ##storing number
# message = input("what is your favourite number?")
# path = Path('./10 files and exceptions/favourite_numbers_exercise.json')
# contents = json.dumps(message)
# path.write_text(contents)


# ##retrieving number
# path = Path("./10 files and exceptions/favourite_numbers_exercise.json")
# contents = path.read_text()
# print(f"i know your favouriter number, its {contents}")


# def get_stored_username(path):
#     """get stored username if available"""
    
#     if path.exists():
#         contents= path.read_text()
#         username= json.loads(contents)
#         return username
#     else:
#         return None
    
# def get_new_username(path):
#     """prompt for a new username"""
#     username = input("what is your name?")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     return username

# def greet_user():
#     """greet user by name"""
#     path = Path('./10 files and exceptions/notes/username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"welcome back, {username}")
#     else:
#         username = get_new_username(path)
#         print(f"well remember you when your back, {username}!")

# greet_user()