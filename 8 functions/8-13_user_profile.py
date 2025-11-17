##User_profile exericse 8-13##
##start with a copy of user_profile.py from page 148
##build a profile of yourself by calling build_profile()
##using your first and last name and three other key-value pairs that describe you

def build_profile(first,last,**user_info):
    """build a profile"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info

me = build_profile('ben','gammage',age = 34,
                   location ='england',starsign = 'capricorn')

print(me)