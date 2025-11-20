##Number served exercise##
#start with program from exercise 9.1
#add attribute called number_Served with a default value 0
#create an instance called restaurant from this class
#print the number of customers the restaurant has served, then change this value
#and print again

#add a mehtod called set_number_served() that lets incremeent number of customers
#whove been served. call this method with any number you like that could represent
#how many customers where served in, say, a day of business

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
        
kfc = Restaurant('kfc','chicken')
kfc.open_restaurant()
kfc.set_number_Served(3)
kfc.customers()
kfc.set_number_Served(4)
kfc.customers()
kfc.increment_number_served(200)
kfc.customers()

maccies = Restaurant('mcdonalds','burger')
maccies.open_restaurant()

#adding customers to a restaurant is information we dont know when we load this instance
#so we cant use it as a parameter with the init method
#instead, we give it a default value 0, as a restaurant will always start with no customers
#we then create a method within the instance that we call to assign it the value of actual
#customers.
#the print method customers can print out the value change


