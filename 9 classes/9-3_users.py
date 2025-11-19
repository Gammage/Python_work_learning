##users exercise##
#make a class called user
#create two attributes called first_name and last_name
#create several other attributes that are typically stored in a user profile
#make a method called describe_user() that prints a summary of the users information
#make another method called greet_user() that prints a personalised greeting to that
#user
#create several instances representing different users, and call  both methods for each user

class User:
    """summary of user and greets them"""
    
    def __init__(self,firstname,lastname,age,location):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.age = age
        self.location = location.title()
        
        self.fullname = f'{firstname} {lastname}'
            
    def greet_user(self):
        """greet user"""
        print(f"Hello {self.fullname} :)")
        
    def describe_user(self):
        """self description"""
        print(f"Your age is {self.age} and you live at {self.location}")
        
ben = User('benjamin','gammage',34,'leicester')
ben.greet_user()
ben.describe_user()

matt = User('matt','Goddard',33,'suffolk')
matt.greet_user()
matt.describe_user()

#when assigning new attributes (or variables) for an instance, you need to assign it
#to the self, assigning it therefore to the instance

#an instance is created from a class but it is a object. other things can also create
#objects.

