##Passing an Arbitrary number of arguments##
#Sometimes you won't know ahead of time how many arguments a function needs to accept
#fortunately python allows a function to collect an arbitrary number of arguments from
#the calling statement

#eg, a function that builds pizza it needs to accept a number of toppings, but
#you cant know ahead of time how many toppings a person will want

#following example has one parameter, toppings, but this parameter collects as 
#many arguments as the calling line provides;

# def make_pizza(*toppings):
#     """make a pizza with requested toppings"""
#     print(toppings)
    
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

#the asterisk in the parameter name *toppings tells python to make a tuple
#containing all the values this function recieves

#the print() call in the function body produces output showing that python can
#handle a function call wit one value and a call with three values. it treats
#the different calls similiarly

#python packs the arguments into a tuple, even if the function recieves only one
#value

#now we can replace the print() call with a loop that runs through the list of 
#toppings and describes the pizza being ordered:

# def make_pizza(*toppings):
#     """summarize the pizza we are about to make"""
#     print(f"making a pizza with the following toppings")
#     for topping in toppings:
#         print(f"-{topping}")
        
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

#this syntax works no matter how many arguments the function receives

##Mixing positional and arbitrary arugments##
#if you want a function to accept several diff kind of arguments, the parameter
#that accepts an arbitrary number of arguments must be placed last in the function
#definition
#python matches positional and keyword arguments tfirst, then collects any remaining
#arrguments in the final parameter

#eg, if the function needs to take in a size of the pizza, that parameter must
#come before the parameter *toppings

# def make_pizza(size,*toppings):
#     """make a pizza using size and toppings"""
#     print(f"\nmaking a {size}-inch pizza with the following toppings")
#     for topping in toppings:
#         print(
#             f"-{topping}"
#         )
        
# make_pizza(16, 'pepperoni')
# make_pizza(21, 'mushrooms','greenpeppers')

#in the function definition, we call the first parameter the pizza size. as the
#second paramter has multiple potential values, its assigned last in function

#youl often see the generic parameter name *args, which collects arbitrary
#positional arguments like this

#STORYING YOUR  FUNCTIONS IN MODULES#
#one advantage of functions is the way they seperate blocks of code from your 
#main program. when you use descriptive names for functions, your programs
#become much easier to follow
#you can go a step further by storing your  functions in a seperate file called a module
#then importing that module into your main program
    #an import tells python make the code in a module available in the current
    #running program file
    
#allows the reuse of functions in many different programs
#knowing how to import functions also allows you to use libraries of functions
#that other programmers have written

#importing an en entire module

#in this function below, we move it to making_pizzas.py;

def make_pizza(size,*toppings):
    """summarise the pizza we are about to make"""
    print(f"making a {size}- inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")