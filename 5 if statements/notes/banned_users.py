#checking whether a value is in a list
    #to check whether a list contains a certian value before taking an action
    
    #eg. might want to check whether a new username already exists in a list of 
    #current usernames before completing someones registration on a website.
    
    #in mapping, you might want to check whether a submitted location already
    #exists in a list of konwn locations.

###IN###

requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings
#true
'pepperoni' in requested_toppings
#false

#keyword in tells python to check for existance of mushrooms/pepperoni. 
#powerful, as it can test if value matches in list.

banned_users = ['andrew','rob','bummy']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()} you can post a response if you wish')
#user 'marie' list item not in list, so if statement true 
    
if user in banned_users:
    print('chicken')
#nothing works because user isnt in banned users.

###BOOLEAN EXPRESSIONS###
#another name for a conditional test. boolean value is either true or false
#boolean values often used to keep track of certian conditions, such as
#whether a game is running or whether a user can edit certian content

game_active = True
can_edit = False

#boolean values provide an efficient way to track state of a program
