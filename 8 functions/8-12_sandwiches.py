##sandwiches exercise 8-12##
#write a function that accepts a list of items a person wants on a sandwich
#function should have one parameter that collects as many items as the function
#call provides, it should print a summary of the sanwich thats being ordered
#call the function three times, using a different number of arguments each time

def make_sandwich(*sandwich_items):
    """make a sandwich"""
    for item in sandwich_items:
        print(f"-added {item} to your sandwich")
        
make_sandwich('bacon','lettuce','tomatoe')
make_sandwich('MORE BACON')
make_sandwich('cheese')

#im creating a make sandwich function that accepts multiple arguments with one 
#parameter, defined by the asterisk as we don't know what items the function will
#require ahead of time