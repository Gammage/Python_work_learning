##login attempts exercise##
##add an attribute called login_attempts to your user class
#from exercise 9-3

#write a method called increment_login_Attempts() that increments the value of
#login attempts by 1.
#write another method called reset_login_attempts() that resets the value of login
#attempts to 0

#make an instance of the user class and call increment_login_Attempts several times
#print value of login_attempts to make sure it was incremented properly
#and then call reset_login_attempts()
#print login_attempts again to make sure it was reset to 0

class User:
    """summary of user and greets them"""
    
    def __init__(self,firstname,lastname,age,location):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0
        
        self.fullname = f'{firstname} {lastname}'
            
    def greet_user(self):
        """greet user"""
        print(f"Hello {self.fullname} :)")
        
    def describe_user(self):
        """self description"""
        print(f"Your age is {self.age} and you live at {self.location}")
        
    def increment_login_attempts(self):
        """login attempts"""
        self.login_attempts += 1
        print(self.login_attempts)
        
    def reset_login_attempts(self):
        """reset login attempts"""
        self.login_attempts = 0
        print(f"Login attempts returned to {self.login_attempts}")
        
ben = User('benjamin','gammage',34,'leicester')
ben.greet_user()
ben.describe_user()
ben.increment_login_attempts()
ben.increment_login_attempts()
ben.increment_login_attempts()
ben.reset_login_attempts()
ben.increment_login_attempts()
ben.increment_login_attempts()


matt = User('matt','Goddard',33,'suffolk')
matt.greet_user()
matt.describe_user()