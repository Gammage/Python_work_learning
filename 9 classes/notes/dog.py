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
        print(f"{self.name} rolled over!")

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
        #just like a method is a function - a method IS just a function, but in a class
        #an attribute is a variable, but in a class

##MAKING AN INSTANCE FROM A CLASS##
#think of a class as a set of instructions for how to make an instance.
#the dog class is a set of instructions that tells python how to make individual instances
#representing specific dogs

#to make an instance representing a dog;

# my_dog = Dog('willie',6)

# print(f"my dog's name is {my_dog.name}.")
# print(f"my dog is {my_dog.age} years old")

#here we tell python to create a dog whos name is willie and age is 6,
#when python reads this line, it calls the __init__() method when python reads
#in dog with the arguments willie and 6. the __init__() method creates an instance
#representing this dog. we assign that instance to the variable my_dog
#naming convention is useful here, we can usually assume that a capitalised name
#refers to a class, and a lowercase name like my_dog refers to a single instance
#created from a class

##ACCESSING ATTRIBUTES##
#to access attributes of an instance, we use dot notation. we access the value
#of my_dogs attribute name by writing:

# my_dog.name

#dot notation is used often in python. This syntax demonstrates how python finds
#an attributes value. Here, python looks at the instance my_dog and then finds
#the attribute name associated with my_dog. this is the same attribute referred
#to as self.name in the class dog
#same approach to age

##CALLING METHODS##
#we use dot notation to call any method defined in dog

# my_dog.sit()
# my_dog.roll_over()

#to call a method, give the name of instance (my_dog) and the method, seperated 
#by a dot. when python reads my_dog.sit(), it looks for the method sit in the
#class dog and runs that code. python interprets the line my_dog.roll_over in the
#same way

#syntax is quite useful, when attributes and methods have been given appriopiate
#descriptive names like name,age,sit() and roll_over(), we can easily infer what
#a block of code,even one we've never seen before, is supposed to do 

##CREATING MULTIPLE INSTANCES##

my_dog = Dog('willie',6)
your_dog = Dog('lucie',3)

print(f"My dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
my_dog.sit()

print(f"your dog's name is {your_dog.name}")
print(f"your dog is {your_dog.age} years old")
your_dog.sit()

#in this example we create a dog named willie and a dog named lucy
#each dog is a seperate instance with its own set of attributes, capable of the same
#set of actions

#even if we used the same name and age for the second dog, python would still
#create a seperate instance from the dog class. you can make as many instances
#from one class as you need, as long as you give each instance a unique variable
#name or it occupies a unique spot in a list or dictionary







