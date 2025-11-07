#continue 5-8, add an if test to hello_admin.py to make sure the list of users
#is not empty.

usernames = []

        
if not usernames:
    print('we need users!')
else:
    for username in usernames:
        if username == 'admin':
            print(f'hi {username}, welcome')
        else:
            print(f'hello {username} welcome back')
            
 #a list empty is FALSE. therefore if not username to an empty list is 
 #TRUE and prints we need users. if false it runs the else, which has a for
 #loop inside.           
        