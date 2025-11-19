##9-1 restaurant exercise##
#make a class called restaurant
#the __init__() method for restaurant should store 2 attributes:
    #a restaurant name and cuisine type
#make a method called open_restaurant() that prints a message indicating that the
#restaurent is open
#make an instance called restaurant from your class. print the two attributes individually
#then call both methods

class Restaurant:
    """define a restaurant name and cuisine type"""
    
    def __init__(self,name,cuisine):
        """declare restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine
        
    def open_restaurant(self):
        """indicates restaurant is open"""
        print(f"the {self.name} is open")
        
kfc = Restaurant('kfc','chicken')
kfc.open_restaurant()

maccies = Restaurant('mcdonalds','burger')
maccies.open_restaurant()

#we create the class restaurant with a capital R 
#we describe it badly with the docstring
#the initialisation method calls self, name and cuisine of restaurant
#i then create the variable name with self.name = name, so name is essentially
#an attribute
#the same with cuisine
#i then create the method open restaurant which references the name parameter assigned
#to self 

#when calling these classes, i assign them to the variable which makes them an instance
#i do this by calling the class and pass the respective arguments
#to use the methods within the class, i simply assign them to the instance
#the method open_restaurant prints the name restaurant with a message it is open

#gpt vers
# You create the class Restaurant using capital R (good convention).

# The class has an __init__() method that defines attributes: name and cuisine type.

# self.name = name assigns the passed-in value to the instance.

# You create instances (kfc, maccies) by calling the class with arguments.

# Calling instance.open_restaurant() triggers the method inside the class.

# Each instance has its own name and cuisine type, stored independently.


