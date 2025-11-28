##employee 11-3 exercise##
#write a class name called employee
#the init method should take in a first name, last name, annual salary,
    #store each of these as attributes
    
#write a method called give_raise() that adds $5000 to the annual salary by default
#but also accepts a different raise amount

#write a test file for employee with two test functions
    #test_give_default_raise()
    #test_give_custom_raise()
    
#write your tests once without using a fixture, make sure they pass
#then write a fixture so you don't have to create a new employee instance in each test function
#run again, make sure both pass

class Employee:
    """class defining a employee"""
    
    def __init__(self,first_name,last_name,annual_salary):
        """initialising the employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self,raise_amount=5000):
        """give raise to employee"""
        self.annual_salary += raise_amount

            