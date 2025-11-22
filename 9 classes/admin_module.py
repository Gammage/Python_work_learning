"""user, admin and privilages"""

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
        
class Admin(User):
    
    def __init__(self, firstname, lastname, age, location):
        super().__init__(firstname, lastname, age, location)
        self.privileges = Privileges()
          
    
class Privileges:
    
    def __init__(self):
        privileges = ['add post','delete post','edit post']
        self.privileges = privileges
        
    def show_privileges(self):
        """shows admin privileges"""
        for privilege in self.privileges:
            print(f"user can {privilege}")