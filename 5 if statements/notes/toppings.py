#to determine if two values are not equal, we can use the inequality operator
#(!=)

# requested_topping = 'mushroom'

# if requested_topping != 'anchioves':
#     print("hold the anchovies!")
    
#this code compares the value in requested_topping in an if statement to anchioves
#as it was not equal to mushroom the if statement continued to print
#hold the anchovies, because the statement is true: requested_topping mushroom
#is not equal to anchioves.

#most conditional expressions will test for equality, but sometimes checking
#for inequality is more applicable

###testing multiple conditions###

#pizza example - if somebody requests a two topping pizza, you will need
#to be sure to include both toppings on their pizza:

# requested_toppings = ['mushrooms','extra cheese','green peppers','extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("adding mushrooms")
# if 'pepperoni' in requested_toppings:
#     print("adding pepperoni")
# if 'extra cheese' in requested_toppings:
#     print("adding extra cheese")
    
# print(f"\nFinished making your pizza")
    
#because we use if statements, even tho first one is true, we check for the
#second and third. thats how extra cheese was printed even when pepperoni wasnt
#requested in the variable

#the below wouldnt work for checking everything;

# if 'mushrooms' in requested_toppings:
#     print("adding mushrooms")
# elif 'pepperoni' in requested_toppings:
#     print("adding pepperoni")
# elif 'extra cheese' in requested_toppings:
#     print("extra cheese")

# print(f"\nfinished making your pizza")

#the mushroom if statement passes, so none of the else if statements are
#checked. elif = else if. the name suggests as such

#TLDR: if you only want one block of code to run, use an if-elif-else.
#if you want more than one, use a series of if statements

# for requested_topping in requested_toppings:
#     print(f"adding {requested_topping}")

# print(f'\nFinished making your pizza!')

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("we are out of green peppers :(")
#     else:
#         print(f'adding {requested_topping}')
        
#we check each item before adding it to the pizza. 
#statement checks to see if green peppers are in the list
#inform no green peppers
#else block ensures all other toppings will be added

#weve assumed lists contain something so far. an example of using empty list

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
    
#in this example, instead of jumping into a for loop we do a quick if statement
#we check if theres at least one item in the list via this if statement
#as an empty list means the if statement is false, skips to else 

#Using multiple lists

available_toppings = ['mushrooms','olives','green peppers'
                      'pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'adding {requested_topping}')
    else:
        print(f"sorry, we don't have {requested_topping}")

#we define available toppings
    #this could be a tuple if toppings are a stable list and not changed!
#then we make a list of customer requested toppings

#then we create a for loop going through all requested topping in
#requested toppings list
#we then create a if statement for each requested topping in the available
#toppings list.
    #we print the result
#else, we print any requested toppings not in the available toppings
        