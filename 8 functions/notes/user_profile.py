##Using arbitrary keyword arguments##
#sometimes you will want to accept an arbitrary number of arguments, but you wont
#know ahead of time what kind of info will be passed to the function.
#in which case, you can write functions that accept as many key-value pairs as
#the calling statement provides.

#eg. building user profiles
    #you will get information about a user, but your not sure what kind of information
    #you will recieve
    
def build_profile(first,last,**user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

#definition of build_profile() expects a first and last name, and then allows
#user to pass in as many name-value pairs as they want. the double asterisk before
#the parameter **user_info causes python to create a dictionary called user_info
#containing all the extra name-value pairs the function recieves. 
#in the body of build_profile() we add the first and last names to the user_info dicitonary
#because we will always get that info from the user. they havent been placed in the
#dictionary yet

##theres many best usecase scenarios for each positional parameters in a function.

##you will often see the parameter name **kwargs used to collect nonspecific keyword
#arguments

