#simple If statement from the book

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#for each car in cars, if car equals to bmw its printed as upper case.
#else print the cars as titles (caps lock at beginning)

#conditional tests
    #heart of every if statement is an expression that can be evaluated as
    #true or false to decide whether the code in an if statment should be 
    #executed.
        #if true, python executes the code following the if statement
        #if false, python ignores the code following the if statement
        
#checking for equality
    #conditional tests compare the current value of a variable to a specific
    #value of interest.
        #simplest conditional test checks whether the value of the variable
        #is equal to the value of interest, see below;
        
car = 'bmw' #this line sets the value of car to 'bmw' using single = sign
car == 'bmw' #this line checks whether the value of car is bmw using == sign
#this then would be true

car = 'audi'
car == 'bmw'
#this would be false

#a single = sign is a statement: set the value of car equal to audi in this eg.
#two == sign is a question. is car equal to bmw?

#testing equality is case sensitive. eg

car = 'Audi'
car == 'audi'
#false. 

#if case doesnt matter (sometimes it can tho!)

car = 'Audi'
car.lower() == 'audi'
#true
    #by lowering the car value before equal to audi, it matches.
    #the lower() method has not changed the original value of the car variable

#this type of thing can be used to verify website usernames, as a username
#entry stored in lowercase, checked for other usernames in database.
#a username of 'John' would be rejected therefore if 'john' exists.

