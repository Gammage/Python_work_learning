##three exits exercise##
#write different versions of exercise 7-4,7-5 that do the following;
    #use a conditional test in the while statement to stop the loop
    #use an active variable to control how long the loop runs
    #use a break statement to exit the loop when the users enters a 'quit' value
    
prompt = "Enter your pizza topping to pizza"
prompt += "\nEnter here or type quit: "

message = ""
inactive = True
while inactive:
    message = input(prompt)
    if message != "quit":
        print(f"we will add {message.title()} to your pizza")
    else:
        inactive = False
        
while True:
    message = input(prompt)
    if message != "quit":
        print(f"we will add {message.title()} to your pizza")
    else:
        break
    
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(f"we will add {message.title()} to your pizza")
        
#3rd is a conditional test in the while statement