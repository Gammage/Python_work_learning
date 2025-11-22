##imported admin exercise##

#start with exercise 9-8
#store class user, privilegs and admin in one module
#create a seperate file, make an admin instance, and call show privileges()
#to show that everything is working correctly

# from admin_module import User
from admin_module import Admin
# from admin_module import Privileges

ben = Admin('ben','gammage',34,'england')
ben.privileges.show_privileges()
