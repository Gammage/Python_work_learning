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

# class Car:
#     """a simple attempt to represent a car"""
    
#     def __init__(self, make, model, year):
#         """initialise attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
        
#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """print a statement showing the cars mileage"""
#         print(f"this car has {self.odometer_reading} miles on it")
        
#     def update_odometer(self,mileage):
#         """set the odometer reading to the given value"""
#         self.odometer_reading = mileage
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you cant roll back an odometer!")
    
# my_new_car = Car('audi','a4','2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

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

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#use dot notation to access the cards odometer reading attribute and set its value
#directly
#this line tells python to take the instance my_new_car find the attribute
#odometer_Reading associated with it, and set the value of the attribute to 23

##modifying an attributes value through a method

#helpful to use methods that update certian attributes for you.
#instead of accessing the attribute directly, you pass the new value to a method
#that handles the updates internally

# my_new_car.update_odometer(25)
# my_new_car.read_odometer()

#this method takes in a mileage value and asigns it self.omodeter_Reading.
#for this to work i created the method in car class

#we can extend this method to do additional work every time the odometer reading is
#modified (see the if statement in update_odometer(self, mileage)
    #it now checks the new reading to see if it is greater to or equal than the existing
    #mileage. if not, you get a warning
    
##INCREMENTING AN ATTRIBUTES VALUE THROUGH A METHOD##

#sometimes you will want to increment an attributes value by a certian amount,
#rather than set an entirely new value. 
    #say we buy a used car and put 100 miles on it between the time we buy it
    #and the time we register it. heres a method that allows us to pass the 
    #incremental amount and add that value to the odometer reading:

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
    
    def read_odometer(self):
        """print a statement showing the cars mileage"""
        print(f"this car has {self.odometer_reading} miles on it")
        
    def update_odometer(self,mileage):
        """set the odometer reading to the given value"""
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer!")
            
    def increment_odometer(self,miles):
        """add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_new_car = Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#the increment_odemeter() adds the value to the meter
#the update_odometer() SETS the value. because a odemeter cant record less,
#this is a seperate method

#you can use methods like this to control how users of your program updates values
#such as an odometer reading. anyone with access to the program can set the odometer
#reading to any value by accessing the attribute directly. effective security takes
#extreme attention to detail in addition to basic checks like those shown here

##IMPORTING CLASSES##
##as you add more functionality to your classes files can get long, even with
#inheritance and composition
#to help, python lets you store classes in modules and import the classes you need
#into your main program

#importing a single class#
#in this example, we include a module level docstring that briefly describes the 
#contents of this module
    