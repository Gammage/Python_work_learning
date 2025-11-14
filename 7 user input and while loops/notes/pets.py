##removing all instances of specific values from a list'

#in chapter 3 (6 dictionaries, see pets.py) we used remove() to remove a specific
#value. it worked because said value we where interested in appeared only once
#in list

#if list has multiple items of one thing, say cats in a list of pets, you can
#use a while loop until cat no longer appears

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

#start with a list containing multiple instances of cat
#print the list
#while cats in pets
#remove the cats in list
#print the pets list

