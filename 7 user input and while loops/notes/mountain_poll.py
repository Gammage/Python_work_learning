##filling a dictionary with user input##

#you can prompt for as much input as you need in each pass through a while loop
#eg. a polling program in which each pass through the loop prompts for the 
#participants name and response. we'll store the data we gather in a dictionary
#because we want to connect each response with a particular user

responses = {}
#set a flag to indicate the polling is active
polling_active = True

while polling_active:
    #prompt for persons name and response
    name = input("what is your name?")
    response = input("which mountain would you like to climb someday?")
    
    #store the response in the dictionary
    responses[name] = response
    
    #find out if anyone else is going to take the poll
    repeat = input("would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
        
#polling is complete
print("poll results:")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
    
#we create an empty dictionary
#we set a flag called polling active to be true
#we create a while loop with the flag
#we have a name variable and response variable, each with inputs requesting respective
#values from user
#we store these in the responses dictionary. note the name is the key and response
#value
#we ask another prompt if user wishes to add mroe to the poll
#if they say no we end the while loop and print the poll results
#we use a for loop in dictionary using items() to print the results