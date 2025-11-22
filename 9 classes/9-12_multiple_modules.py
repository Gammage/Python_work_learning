##Multiple modules exercise##

#store user in one module, store privileges and admin classes in a seperate module
#in a seperate file, create an admin instance and call show_privileges()

from admin_multiple_module import Admin

ben = Admin('ben','gammage',34,'england')
ben.privileges.show_privileges()

#disgusting way of file naming, but
#we call admin_multiple module and import admin class
#for admin class to work inside this module, it requires the user class, which is 
#in module user_multiple_module. so, in admin_multiple_module,
#we have from user_multiple_module import User


