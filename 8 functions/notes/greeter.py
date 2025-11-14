##a simple function named greet_user() that prints a greeting:

# def greet_user():
#     """display a simple greeting"""
#     print("hello")
    
# greet_user()

#this examples shows a simple way to structure a function
#first line uses def to define a function
#this is the function definition, tells the name of the function and if applicable,
#what kind of information the function needs to do its job - the parenthesis hold
#this information
#in this case, the name of the functions is greet_user() and it needs no info to do
#its job so parenthesis are empty. finally the definition ends in a colon

#indented lines that follow def greet_user(): make up the body of the function
#the text on the second line is a comment called a docstring, which descibres
#what the function does
    #when python generates documentation for the functions in your programs, it looks
    #for a string immediately after the functions definition.
    #these strings are usually enclosed in triple quotes, which letrs you write
    #multiple lines
    
#the line print hello is the only line of actual code in the body of the function
#when you want to use this function you have to call it
#function call tells python to execute the code within it
    #to call the function you write the name of the function followed by its
    #necessary info in the parenthesis
        #as no info is needed, this can be called by simply entering greet_user()
        
#if we modify slightly, it can greet the user by name. for the function to do this,
#you enter username in the parenthesis of the functions definition at def greet_user()
#example of changing this function for a username:

# def greet_user(username):
#     """says hello to user"""
#     print(f"hello {username}")

# greet_user('alskdjhas89')

#by adding username here, allow the function to accept any value of username
#you specify. it expects a value for username each type you call it

#you can call greet user as much as you like and pass it any name

##Arguments and parameters##

#the variable username in the defintion of greet_user()is an example of a parameter

#people use arguments and parameters interchangeably

##Using a function with a while loop##
##you can use functions with all the python structures so far

def get_formatted_name(firstname,lastname):
    """return a full name, nearly formatted"""
    fullname = f"{firstname} {lastname}"
    return fullname.title()

while True:
    print(f"\nPlease tell me your name")
    print(f"(enter'q' at any time to quit)")
    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"hello, {formatted_name}")
    



