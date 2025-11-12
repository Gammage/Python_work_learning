##how the input() function works##
#input() function pauses the program and waits for user to enter text
#once user submits input, input is stored in variable to be used with

message = input("tell me something, and i will repeat it back to you: ")
print(message)

#the input function takes one argument: the prompt we want to display to the user
#(so that they know what information to enter)
#in this example, when python runs the first line, the user sees the prompt 
#"tell me something, and i will repeat it back to you "
#program waits for the user to respond (pressing enter) the response is assigned
#to the variable message

#the print(message) prints the stored message to the user

#the input function allows any prompt the user sends, but we print a string in the
#input parenthesis to guide the user what input they should do

