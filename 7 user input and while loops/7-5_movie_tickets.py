##movie tickets exercise##
#a movie theater charges different ticket prices depending on persons age
#if a person is under age 3
    #ticket is free
#if between 3 - 12
    #ticket is $10
#is age over 12
    #ticket is $15 
#write a loop which you ask users their age, and then tell them the cost of 
#movie ticket

prompt = "ask as your age for ticket price"
prompt += "\nEnter age or quit: "

message = ""
inactive = True
    
while inactive:
    message = input(prompt)
    if message == "quit":
        inactive = False
    else:
        message = int(message)
        if message <= 3:
            print(f"{message}'s go free!")
        elif message >= 3 and message < 12:
            print(f"{message}'s pay $10")
        else:
            print(f"over 12s pay $15")
            
#needed to check message before it turned to an integer, to see if user entered
#quit as quit is a string :)