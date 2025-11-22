"""electric car and battery classes"""
from car_import import Car

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