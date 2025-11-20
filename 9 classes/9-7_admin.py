##ADMIN EXERCISE 9-7##
#write a class called admin that inherits from the user class you wrote in 9-3
#add attribute, privilages, that stores a list of strings like 'can add post',
#can delete post,'can ban user'and so on
#write a method called show_privileges() that lists the admin set of privilesg
#create an instance of admin, call your method

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
        privileges = ['add post','delete post','edit post']
        self.privileges = privileges
        
    def show_privileges(self):
        """shows admin privileges"""
        for privilege in self.privileges:
            print(f"{self.fullname} can {privilege}")
        
ben = User('benjamin','gammage',34,'leicester')
ben.greet_user()
ben.describe_user()

matt = User('matt','Goddard',33,'suffolk')
matt.greet_user()
matt.describe_user()

katie = Admin('katie','smith',20,'england')
katie.show_privileges()