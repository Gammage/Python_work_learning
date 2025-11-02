#storing a set of numbers. for example, keep track of positions of each character in game
#keeping track of players score

#data visualisations always works with sets of numbers. temperatures, distances, population sizes, latitude/longitude, values
#lists are ideal for numbers, which python provides tools to work efficiently with. even millions of numbers.

for value in range(1,5):
    print(value)
    
#notice how its 1,2,3,4. 
#range() causes python to start counting at first value you give it, and stops when it reaches the second you provide. never prints end value

#so for 1-5 you do below

print('\nvalue range 1-5')
for correct_Value in range(1,6):
    print(correct_Value)
    
print('\none argument')
for single_range in range(6):
    print(single_range)
#notice how this one starts on 0 but ends on 5. starts from 0 and includes it, per python range norm.

#using range to create a list;
numbers = list(range(1,6))
print(f'\nlist generated from the range method {numbers} and assigned to variable')

