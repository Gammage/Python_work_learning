##how the input() function works##
#input() function pauses the program and waits for user to enter text
#once user submits input, input is stored in variable to be used with

# message = input("tell me something, and i will repeat it back to you: ")
# print(message)

#the input function takes one argument: the prompt we want to display to the user
#(so that they know what information to enter)
#in this example, when python runs the first line, the user sees the prompt 
#"tell me something, and i will repeat it back to you "
#program waits for the user to respond (pressing enter) the response is assigned
#to the variable message

#the print(message) prints the stored message to the user

#the input function allows any prompt the user sends, but we print a string in the
#input parenthesis to guide the user what input they should do


##USER CHOOSING WHEN TO QUIT##
    #we can make the parrot program run as long as the user wants by putting
    #most of the program inside a while loop. define a quit value and then 
    #keep the program running as long as the user has not entered the quit value
    
prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\n enter 'quit' to exit the program"

message = ""

# while message != "quit":
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

#we define what prompt is
#we then define the message as empty    
#while message is not equal to quit
#message variable is the prompt input from user in the while loop
#unless quit is anything other than quit to the message variable the while loop
#continues

#we make sure to give the message an initivial value. its just an empty string,
#it will make sense to python and allow it to perform the comparison

##Using a flag##
#there might be multiple reasons to end a while loop, for example in a game
#say a city you needed to protect was destroyed

#for a program that should run if many conditions are true, you can define one
#variable that determines whether or not the entire program is active

#flag acts as a signal to the program
#as a result, the overall while program only needs one condition: whether the
#flag is true

#flag in this instance is active

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
#we set the variable active to true so the program starts in an active state.
#doing so makes the while statement simpler because no comparison is made in the
#while statement itself. the logic is taken care of in other parts of the program

#in the if statement in the while loop, we check if message equals quit, if it 
#is then active because false and the while loop ends. else the message prints

#to simplify code it makes sense to have the active state handled outside the while
#loop

