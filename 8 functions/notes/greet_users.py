##Passing a list##
#You'll oftne find it useful to pass a list to a function
    #whether its a list of names, numbers, or more complex objects like dicts
#when you pass a list to a function, the function gets direct access to the
#contents of the list.

#a list of users and want to print a greeting to each
#following example sends a list to a function called greet_users()
#which greets each person in the list individually

def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
        
usernames = ['jack','bummy','ben']
greet_users(usernames)

#defined function greet_users with the rquired parameter names
#assigned doctstring in quotes
#creates for loop name in names
#created msg variable with name titalised
#pring the message for each name

#create a list, then assign the list to our new function

