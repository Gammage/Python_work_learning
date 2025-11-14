##Using a while loop with lists and dictionaries##
#to track many users and piece of information we will need to use lists and
#dictionaries with our while loops

#a for loop is effective for looping through a list, but shouldn't modify a list
#inside a for loop as python will have trouble keeping track of the items in the
#list

#to modify a list as you work through it, use a while loop
#using while loops with lsits and dictionaries allows you to collect, store, and
#organise lots of input to examine and report on later

#moving items from one list to another
    #consider a list of newly registered but unverified users of a website
    #after we verify them, how can we move them to a seperate list of confirmed
    #users?
    
    #one way would be to use a while loop to pull users from the list of 
    #unconfirmed users as we verify them and then add them to a seperate list
    #of confirmed users. heres what that code looks like;
    
#start with users that need to be verified
#move each verified user into the list of confirmed users

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users
#move each verified user into the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
#display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
#pop takes from the top, so candace is printed first, (list order reversed)
#simulating confirming each user by printing a verification message
#as list of unconfirmed users shrinks, the list of confirmed users grows.
#when list of unconfirmed users is empty the loop stops. and list of confirmed
#users is printed


    