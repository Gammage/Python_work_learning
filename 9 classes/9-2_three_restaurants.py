##exercise 9-2 three restaurants##
#start with exercise 9-1
#create three instances and call describe_restaurant for each instance


class Restaurant:
    """define a restaurant name and cuisine type"""
    
    def __init__(self,name,cuisine):
        """declare restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine
        
    def open_restaurant(self):
        """indicates restaurant is open"""
        print(f"the {self.name} is open")
        
    def describe_restaurant(self):
        """describe restaurant"""
        print(f"{self.name} is known for {self.cuisine}")
        
kfc = Restaurant('kfc','chicken')
kfc.open_restaurant()
kfc.describe_restaurant()

maccies = Restaurant('mcdonalds','burger')
maccies.open_restaurant()
maccies.describe_restaurant()

pizza_hut = Restaurant('pizza hut','pizza')
pizza_hut.open_restaurant()
pizza_hut.describe_restaurant()

