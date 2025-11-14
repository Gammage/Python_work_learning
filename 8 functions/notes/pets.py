##Passing/positional arguments##
#you can have multiple parameters, which means you would need multiple arguments
#you can apss arguments to your functions in multiple ways

#positional arguments which need to be in the same order the parameters where written.
#keyword arguments, where each argument consists of a variable name and value; and
#lists and dictionaries of values.

##POSITIONAL ARGUMENTS##
#when you call a function, python must match each argument in the function with
#a parameter in the function definition
#simplest way is to do this based on the order of the arguments provided

#to see how this works, consider a function that displays information about pets
#function tels us what kind of animal each pet is and the pets name, eg;

# def describe_pet(animal_Type, pet_name):
#     """display info about a pet"""
#     print(f"\nI have a {animal_Type}")
#     print(f"\nmy {animal_Type}'s name is {pet_name}")
    
#defintion shows that this function needs a ttype of animal and animal name.
#when we call describe_pet() we will need the animal type and name in that order.
#eg

# describe_pet('dog','arthur')

##multiple function calls##
#you can call a function as many times as needed##
##describing asecond pet requires one more call to describe_pet()

# describe_pet('dog','merlin')
# describe_pet('cat','marshmallow')

#calling a function multiple times is a very effiecient way to work
#order matters in positional arguments
#if you reverse the order of arguments in the example above you would get eg.

# describe_pet('merlin','dog')

##KEYWORD ARGUMENTS##

#keyword argument is a name-value pair that you pass to a function
#you directly associate the name and the value within the argument
    #so when you pass the argument to the function, theres no confusion
#kkeyword arguments free you from having to worry about correctly ordering your 
#arguments in the function call, and they clarify the role of each value in the
#function call

#to rewrite pets.py using keyword arguments to call describe pet

# def describe_pet(animal_type, pet_name):
#     """display info about a pet"""
#     print(f"I have a {animal_type} called {pet_name}")

# describe_pet(animal_type='hamster',per_name='harry')

#the function hasnt changed, but when we call the function we explicity tell python
#which parameter each argument should be matched in
#when python reads the function call, it knows to aassign the argument 'hamster'
#and 'harry' to their respective parameters.
#here, the order doesnt amtter because we explicity define where the arguments go

##Default values##

#when writing a function you can define a default value for each parameter
#if an argument for a parameter is provided in the function call, python uses the
#argument value
#when you define a default value for a parameter, you can excluse the corresponding
#argument you'd usually write in the aargument you'd usually write in the function call

def descibe_pet(pet_name, animal_type='dog'):
    """display info about pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")
    
descibe_pet('willie')

#the parameters had to be changed. as the default value makes it unneccesary to 
#define the type of animal as an argument, only argument left is the pets name
#python interprets this as a positional argument
    #if the function is called with just a pets name, that argument will match
    #up with the first parameter listed in the functions definition. thats the reason
    #the parameter has to be pets name

#when you use default values, any parameter with a default needs to be listed
#after all the parameters that dont have default values. allows python to interprete
#positional arguments correctly

##EQUIVALENT FUNCTION CALLS##

#because positional arguments, keyword arguments, default  values can all be used
#together, you'll often have several equivalent ways to call a function. consider
#the following definition for describe_pet() with one default value provided

def describe_pet(pet_name,animal_type="dog"):
    """define an animal"""
    
#the above needs a argument for the first parameter pet_name, this value can be 
#provided by positional or keyword format

#if animal being described is not a dog, an argument for animal_type must be included
#in the call, and this argument can also be specified using positional or keyword format

#a dog named willie
descibe_pet('willie')
descibe_pet(pet_name='willie')

#a hamster named harry
descibe_pet('harry','hamster')
descibe_pet(pet_name='harry',animal_type='hamster')
descibe_pet(animal_type='hamster',pet_name='harry')

#doesnt matter what style to use, as long as the output is what i want
#just use style easiest to understand

##AVOIDING ARGUMENT ERORRS##

#unmatched arguments occer when you provide fewer or more arugments then a function
#needs to do its work

#eg
# descibe_pet()

