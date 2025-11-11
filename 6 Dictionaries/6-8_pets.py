##PETS##
    #make several dictionaries
        #each dictionary represents a pet
            #each dictionary include the kind of animal and owners name
            #store in a list called pets
            #loop through your list, as you do print everything you know
            #about each pet
            
arthur = {
    'animal':'dog',
    'owners name':'Russ',
}

marshmallow = {
    'animal':'cat',
    'owners name':'jas',
}

Kaiser = {
    'animal':'dog',
    'owners name':'Katie',
}

pets = [arthur,marshmallow,Kaiser]

for index, pet in enumerate(pets):
    print(f"\nPet:{index + 1}")
    print(f"{pet['owners name']} has a {pet['animal']}")
    
#we have created 3 dictionaries under the variables the pets names
#we create a list called pets and store the variables in there (references them)
#we use a for loop and enumerate the pets to get the index and variable of each
#as each variable is a dictionary, we call upon the keys to get their respective values

