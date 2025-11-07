#create a program that simulates how websites ensure everyone has a unique
#username

current_users = ['ben','George','charles','BUMMY','rob']
current_users_lower = [user.lower() for user in current_users]

new_users = ['catherine','matt','heather','ROB','bummy']
new_users_lower = [user.lower() for user in new_users]

for user in new_users_lower:
    if user in current_users_lower:
        print(f'{user} already registered.')
    else:
        print(f'{user} not registered. ')
        
##the task was insensitive caps for the names. so i cleaned both current
#and new users before the for/if statement.


