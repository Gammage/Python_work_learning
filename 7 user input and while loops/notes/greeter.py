##Writing clear prompts##
#each time you use the input() function, you should include a clear, easy-to-use
#followup prompt that tells the user exactly what kind of information you are
#looking for

# name = input("please enter your name: ")
# print(f"\nHello, {name.title()}")

#we trust the user to follow the prompt
#notice spacing for easier readability in the code above

#sometimes you would want to write a prompt thats longer then one line.
    #eg, why you are asking for a certian input
    
# prompt = "if you share your name, we can personalize the messages you see."
# prompt += "\nwhat is your first name?"

# name = input(prompt)
# print(f"\nHello, {name.title()}")

#this example shows how to do a multiline string.
    #first line assignts the first part of the message to variable prompt
    #the second line, operator += takes the string that was assigned to prompt
    #and adds new string to the end
    
#when using input() function, python interprets everything the user enters as string
#consider the following interpreter session which asks for users age

# age = input("how old are you?")
# print(age)
# print(type(age))

#we know its string because the number is now enclosed in quotes. you can use
#type() to find out what the value of a variable is stored as

# age = input("how old are you?")
# age >= 18

#the above proves input stores as string, because you are comparing a string to 
#an integer with age variable (>= 18) we get an error

age = input("how old are you")
age = int(age)
age >= 18

#the above converts the string into an integer
#the operator can then compare the two integers


