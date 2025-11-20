##BATTERY UPGRADE EXERCISE##
#use final version of electric_car.py from this section.
#add a method to the battery class called upgrade_battery()
    #this method should check battery size and set the capacity to 65 if isnt already
    #make a electrict car with a default battery size, call get_range() once,
    #and then call get_range() a second time after upgrading the battery. you should
    #see an increase in the cars range
    
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
    
    def upgrade_battery(self):
        """upgrade battery"""
        
        if self.battery_size <= 65:
            self.battery_size = 65
        
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
        
# my_new_car = Car('audi','a4','2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# my_used_car = Car('subaru','outback',2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

##electric cars##
           
# my_leaf = ElectricCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

    #make a electrict car with a default battery size, call get_range() once,
    #and then call get_range() a second time after upgrading the battery. you should
    #see an increase in the cars range
    
my_electric_car = ElectricCar('vroom','tree',2025)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.describe_battery()
