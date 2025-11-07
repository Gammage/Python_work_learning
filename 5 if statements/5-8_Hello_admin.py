#a list of five usernames, imagine writing code print a greeting to each user
#after they login to a website. loop through list, print a greeting to each
#user

#if user is admin, print a special greeting
#otherwise, print a generic greeting

usernames = ['ben','george','rob','bummy','jack','admin']

for username in usernames:
    if username == 'admin':
        print(f'hello {username}, would you like a report?')
    else:
        print(f'Hello {username}, welcome')
        
