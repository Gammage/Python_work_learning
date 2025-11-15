##Modifying a list in a function
#when you pass a list to a function, the function can modify the list
#any changes made to the list inside the functions body are permenant
#allowing you to work efficiently even when dealing with large amounts of data

#eg. a company that creates 3D printed models of designs that users submit
#designs that need to be printed are stored in a list, and after being printed
#theyre moved to a seperate list. the following code does this without using 
#functions

#start with some designs that need to be printed
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

#simulate printing each design, until none are left
#move each design to completed_models after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nthe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
    
##by using functions we can structure the above carefully

def print_models(unprinted_designs, completed_models):
    """simulate printing design until none are left
    move each designt o completed models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """show all the models that are printed"""
    for completed_model in completed_models:
        print(completed_model)
        
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#we have two defined functions.
#print_models takes on the parameters 'unprinted_design, completed_models
    #while in the list of unprinted_designs
        #we create a variable unprinted_design and store an item from list to it
        #we print the current list item in question
        #we add the list item to the other list completed_models
#show_completed_models is our other defined function, that takes the
#completed_models list
#we create a for loop to go through the completed_models list and print each one

#we then call the functions
#this makes code simpler to read. see below

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#if you're writing a function and notice the function doing too many different
#tasks, try split the code into two functions.
#you can always call a function from another function

