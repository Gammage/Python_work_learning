##DICTIONARYCEPTION##
#dictionary within a dictionary. code can get complicated quickly when you do so

#eg, a website, each with a unique username, you can use the usernames as the keys
#in the dictionary. then store info about each user by using a dictionary as the 
#value associated with their username.

users = {
    'ainestein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',     
        },
    }

for username, user_info in users.items():
    print(f'\nUsername:{username.title()}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"Full name:{full_name.title()}")
    print(f"Location:{location.title()}")

#created a for loop to get the key/value pair in dictionaries using items()
#printed the key referenced as username in the for loop
#created a variable called full name using a f string (formatted string literal)
#combining the first and last name in the value dictionary, which is a nested dictionary
#that nested dictionary is key first/last/location with respecting values.

