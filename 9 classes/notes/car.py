##WORKING WITH CLASSES AND INSTANCES##

#you can use classes to represent many real-world situations.
#once you write a class, you'll spend your time working with instances created
#from that class

#one of the first tasks you'll want to do is modify the attributes associated
#with a particular instance

#this class will store information about the kind of car we're working with
#it will have a mehtod that summarises this information:

# class Car:
#     """a simple attempt to represent a car"""
    
#     def __init__(self, make, model, year):
#         """initialise attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_new_car = Car('audi','a4','2024')
# print(my_new_car.get_descriptive_name())

#just like dog class, we defined the init method with the self parameter first
#we give it three other parameters, make model and year
#we define a method called get_descriptive_name that puts a cars year, make and 
#model into one string neatly describing car.

#again, we use self to assign attribute values in this method.
#outside of the class, we make an instance from the car class and assign it to 
#the variable my_new_car. we call get_Descriptive_name() to show what car we have

##SETTING A DEFAULT VALUE FOR AN ATTRIBUTE## 

class Car:
    """a simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_omodeter(self):
        """print a statement showing the cars mileage"""
        print(f"this car has {self.odometer_reading} miles on it")
    
my_new_car = Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_omodeter()

#python here creates a new attribute called odometer_reading and sets its initial value to 0
#so we need a way to change the attribute

##MODIFYING ATTRIBUTE VALUES##
#you can change an attributes value in three ways: 
    #you can change the value directly through an instance
    #set the value through a method
    #increment the value through a method
    
#modifying an attributes value directly
#simplest way to modify the value of an attribute is to access the attribute directly
#through the instance 

my_new_car.odometer_reading = 23
my_new_car.read_omodeter()

#use dot notation to access the cards odometer reading attribute and set its value
#directly
#this line tells python to take the instance my_new_car find the attribute
#odometer_Reading associated with it, and set the value of the attribute to 23




    