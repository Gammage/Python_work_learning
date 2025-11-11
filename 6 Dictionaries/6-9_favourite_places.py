##Favourite_places##
    #make a dictionary called favourite_places
    #think of three names to use as keys in the dictionary
    #store one to three favourite places for each person

favourite_places = {
    'ben':['japan','america'],
    'bob':['germany'],
    'matt':['england','nigeria'],
}

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite countries are:")
    for place in places:
        print(f"{place}")

##DICTIONARY VALUES CAN BE LISTS, DICTIONARIES, EVEN FUNCTIONS
##values can be lists. treat it as a list, like so

my_list = [1,2,3,4,5]
print(my_list)
for number in my_list:
    print(number)
    
    