##Return Values##
#a function doesnt always have to display its output directly
#instead, it can process some data and then return a value or set of values
#the value the function returns is called a return value
#return statement takes a value from inside a function and sends it back to the 
#line that called the function
#return values allow you to move much of the programs grunt work into functions

def get_formatted_name(first_name,last_name):
    """return full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#we define the function get_formatted_name, with the parameters first_name, last_name
#we add docstring return full name
#we create a variable full name and add the two parameters combined to make full name
#we use return to get the full name

#useful when considering a large program that needs to store many first and last names

##making an argument optional##
#making an argument optional is useful so that people using it can choose to 
#provide extra information if they want to

#eg, if we want to expand get_formatted_name() to handle middle names this could
#be an answer

def get_formatted_name(first_name,last_name,middle_name=''):
    """return full name"""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker',middle_name='lee')
print(musician)

#john lee hooker is the guys actual name lol
#as middle name is optional its last in the parameters in defining the function
#python interprets non-empty strings as true
#so conditional test if middle_name evaluates to true if a middle name argument
#is in the function call

#returning a dictionary


