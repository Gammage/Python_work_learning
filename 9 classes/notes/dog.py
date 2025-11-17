##WHAT IS A CLASS##
#classes represent real world things and situations
#you create objects based on these classes
#when you write a class, you define the general behaviour that a whole
#category of objects have

#classes make life easier and for other programmers
#programs hopefully make sense to people you work with


##CREATING AND USING A CLASS##

#you can model most things using classes
#in this eg, we use a dog - any dog.
#we assign it generic definitions, all dogs can sit, roll over etc.

class Dog:
    """a simple attempt to model a dog"""
    
    def __init__(self, name, age):
        "initialise name and age attributes"
        self.name = name
        self.age = age
        
    def sit(self):
        "simulate a dog sitting in response to a command"
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name}rolled over!")

#classes are defined by capitalisation in python conventionally
#theres no paranthesis around the class definition because we are creating this class
#from scratch

#THE __INIT__() METHOD
#a function thats part of a class is a method
#this is a special method that python runs automatically whenever we create a new
#instance based on the dog class
#it looks like this to prevent conflicting with other method names
#it needs 2 underscores each side, a convention used

    #in dog, we have three parameters - self name and age
    #self is required in the method definition, and it must come first
    #must be included in definition, because when python calls this method later
    #(to create instance of dog) the method call will automatically pass the self
    #argument. 

    #every method call associated with an instance automatically passes
    #self which is a reference to the instance itself: gives the invidivual instance
    #access to the attributes and methods in the class.
    
    #the two variables defined in the body of __init__() each have the prefix
    #self any variable prefixed with self is available to every method in the class
    #name and age are passed as arguments,
    #the line self.name = name takes the value associated with the parameter name
    #and assigns it to the variable name, which is then attached to the instance
    #being created. the same process happens with age. 
    #variables that are accessible through instances like this are called attributes
    
    #n_sweep
        #attribute is to variable as method is to function
        #age = 10 is a variable, my_dog.age = 10 is an attribute
        #just like a method vs a function - a method IS just a function, but in a class
        #an attribute is a variable, but in a class



