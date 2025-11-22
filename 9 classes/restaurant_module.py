"""the restaurant exercise module"""

class Restaurant:
    """define a restaurant name and cuisine type"""
    
    def __init__(self,name,cuisine):
        """declare restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine
        
    def open_restaurant(self):
        """indicates restaurant is open"""
        print(f"the {self.name} is open")