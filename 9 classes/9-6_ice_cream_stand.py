##ICE CREAM EXERCISE 9-6##
#ice cream stand is a specific kind of restaurant
#write a class called icecream stand that inherits the restaurent calss wrote earlier
#add an attribute called falvours that store a list of icecream flavours
#write a method that displays these flavours
#create an instance of icecreamstand and call this method

class Restaurant:
    """define a restaurant name and cuisine type"""
    
    def __init__(self,name,cuisine):
        """declare restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
        
    def open_restaurant(self):
        """indicates restaurant is open"""
        print(f"the {self.name} is open")
        
    def set_number_Served(self,customer_served):
        """update how many customers"""
        self.number_served = customer_served
        
    def increment_number_served(self,increment_customers):
        """how many customers incremented"""
        self.number_served += increment_customers
        
        
    def customers(self):
        """how many customers served"""
        print(f"{self.name} has served {self.number_served} customers")
        
class IceCreamstand(Restaurant):
    "a specific type of restaurant with different ice creams :)"
    
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)       
        icecream_flavours = ['vanilla','chocolate','blueberry']
        self.flavours = icecream_flavours
        
    def show_icecream(self):
        print(f"here are {self.name.title()} {self.cuisine.title()} flavours! {self.flavours}")
        
peters_icecream = IceCreamstand('peters','icecream')
peters_icecream.show_icecream()

#we define class as restaurant, as before, 
#for this exercise focused on creating a subclass called icecreamstand
#we then assigned a list of icecreams to a  value and assigned it to the self.flavours
#attribute
#we then reference the parent class attributes in combination with the subclass flavours
#in a print string which is called by the show_icecream function