"""user module"""

class User:
    """summary of user and greets them"""
    
    def __init__(self,firstname,lastname,age,location):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.age = age
        self.location = location.title()
        
        self.fullname = f'{firstname} {lastname}'