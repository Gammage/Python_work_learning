"""admin and privileges"""
from user_multiple_module import User

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