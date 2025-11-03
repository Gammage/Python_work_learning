###Truple###
    #when something cant change in python its referred to as immutable, and in the case of a list, an immutable list is a truple.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#notice we use parenthesis over square brackets, and how we access the elements in the list.

#when trying to change the value
# dimensions[0] = 250
#that gets a typeerror

##first note of book;
    #tuples technically defined by the presence of a comma; parenthesis make them neater and more readable. example given;*
        # my_t = (3,)
    #this doesnt make sense to have a tuple with one element, but can happen when generated automatically
    
print('\nfor loop on a tuple')
for dimension in dimensions:
        print(dimension)
        
#you cant modify, but you can assign a new value to the variable that represents a tuple

dimensions = (200,50)
print("\noriginal dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,100)
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)
    
#reassigning a variable is valid.

#tuples pretty simple compared to lists. use them when a set of values shouldn't change
#*a different definition suggests paranthesis makes it a truple. contents are protected by the ()