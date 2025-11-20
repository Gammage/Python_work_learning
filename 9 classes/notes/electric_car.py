##INHERITANCE##
#You dont always need to start from scratch when writing a class
#if the class you're writing is a specialised version of another class you wrote,
#it takes on the attributes and methods of the first class
#the original class is called the parent class, and the new one is called the child
#class.
#child class can inherit any or all ofthe attributes and methods of its parent 
#class, but its also free to define new attributes and methods of its own

#THE __INIT__ METHOD FOR A CHILD CLASS
#when writing a new class based on an existing one, you'll often want to call the
#__init__ method from parent class. this will initialise the attributes that
#where defined in the parent __init__() method and make them available in the child class

#eg electric car.
    #electric car is a specific type of car, so we can use the electric car class
    #on the car class we used earlier
    #therefore we only need to write code specific for an electric car
    #start by making a simple version of the electriccar class, which does 
    #everything the car class does
    
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

class Battery:
    """a simple attempt to modela  battery for an electric car"""
    def __init__(self, battery_size=40):
        """initialise battery attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """print statement describing battery size"""
        print(f"this car has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        """describe the range the battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
            
        print(f"this car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    
    def __init__ (self, make, model, year):
        """initalise attributes of the parent class."""
        
        super().__init__(make,model,year)
        self.battery = Battery()
        
    def describe_battery(self):
        "print a statement about the battery size"
        print(f"this car has a {self.battery_size}-kwh battery")
        
my_new_car = Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

##electric cars##
           
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.battery.get_range()

#parent class must be part of the current file
#name of the parent class must be included in paranthesis in the definition of a child
#class
#the init method tkaes in the information required to make a car instance
#the super() function
    #a special function allows you to call a method from the parent class
    #this function allows all the attributes defined in that method
    #the name super comes from a convention of calling the parent class a superclass
    #and the child subclass
    
#we can test whether inheritance is working properly by trying to create an electric
#car with the same kind of information we'd provide when making a regular car
#aside from init there are no attributes or methods that are particular to electric
#car

##DEfINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS##

#you can add new attributes and methods necessary to differentiate the child class from
#parent one, see describe battery and battery size in the above

##OVERRIDING METHODS FROM THE PARENT CLASS##

#define a method in the child class with the same name as parent class to override
#in parent class.
#if the class car had a method filled_petrol_tank() this method is meaningless
#for an all electric vehicle, so you might want to override this method eg

# def fill_petrol_tank(self):
#     """electric cars dont have petrol tanks"""
#     print("this car doesnt have a petrol tank")

#just use same name and modify like above

##INSTANCES AS ATTRIBUTES##

#may find that your adding more and more detail to a class
#find that you have a growing list of attributes and methods
#in such situations, you might recognise that part of one class can be written
#as a seperate class
#this approach is called composition

#eg in the car situation, see the class battery and how its called in the electric
#car class

#we define battery that doesnt inherit from any other class
#this line tells python to create a new instance of Battery(with a default size of 
# 40)

##seems alot of extra work, given the attribute is singular. but it allows battery
#to have more given attributes without overloading the electric car class

#such as the battery types. the battery stores two types, which can indicate the range
#of the vehicle

##Modeling real-world objects
#as you begin to model complicated things like electric cars,
#you will wrestly with interesting questions:
    #is the range of an electric car a property of the battery or the car?
    #fine if one car, but what about an entire line of cars, we may want to move
    #get range() to the electriccarclass. the get_Range() method would still
    #check battery size before determining range, but it would report a range
    #specific to the kind of car its associated with
    #alternatively, we could maintain the association of the get_range() method
    #with the battery but pass it a parameter such as car model. the get_range()
    #would report a range based on the battery size and car model
    
    #when you wrestle with questions liek these, you're thinking at a higher logical
    #level than a syntax-focused level, not so much about python but how to represent
    #real world in code. takes practice fo find the most efficient representation
    
    
