# see 3 lists\notes 'what is a list.txt' for context

motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'\nhere is a list of motorcycles from the variable named as such: {motorcycles}.')

# MODIFYING a motorcycle in the list at the beginning. see variable change, how first one is replaced.

print('replaced the first list value from honda to ducati. changing, adding lists for many reasons. make new aliens appear in a game eg')
motorcycles[0] = 'ducati'
print(f'new list: {motorcycles}')


# ADDING a list item in the variable

print('\nadding a list item (motorcycle) in the list. see code. append adds to the last list item')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


#example of a empty variable and adding list items after (notice how i retyped the variable and assigned it nothing)

print('\nadding to the variable motorcyles which starts as an empty list')
motorcycles = []
print(motorcycles)
print('after')
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)




