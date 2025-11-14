##Tshirt exercise 8-3##
#Write a function called make_shirt() 
#function should summarise the size of the shirt and message print to it
#call the function once using positional argument
#call the function a second time using keyword argument

def make_shirt(size_shirt,message_print):
    """making a shirr"""
    print(f"shirt size {size_shirt} with print {message_print.title()}")

make_shirt('m','smiley face') #<<positional 
make_shirt(size_shirt='s',message_print='sad face') #<<keyword





