##pizza toppings exercise 7-4##
#write a loop that promps the user to enter a series of pizza toppings until
#they enter a 'quit' value
#as they enter each topping, print a message saying you'll add that typping to 
#their pizza

prompt = "Enter your pizza topping to pizza"
prompt += "\nEnter here or type quit: "

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(f"we will add {message.title()} to your pizza")
        
