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

# this is a good example of lists, because often they are empty at first

# INSERTING a list item at a specific position
print('\ninserting a list item at a specific position. see code how i insert at index 0, pushing other items back one index')
motorcycles.insert(0, "ducati")
# 0 is insert at begin, ducati is the new item

# Deleting a list item at a specific postion
print('\nExample of deleting a list item at specific position')
print(motorcycles)
del motorcycles[0]
print(f'motorcycle first list item deleted {motorcycles}')
# you can use index to see which list item should be deleted. 0 is first, 1 is second etc. remember, -1 is last item, -2 is second last

# delete an item from a list, but use it after.
# pop refers to thinking of a list as a stack of items, popping one item off the top of the stack.
# in this analogy, it pops off the top
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'here are the current list of motorcycles:{motorcycles}, going to use pop()')
popped_motorcycle = motorcycles.pop()
print(f'created a variable popped_motorcycle and assigned the list variable with pop(). the result is {popped_motorcycle}')
print('the pop is last item. you can use negative index (-1, -2 etc)')

#POP WHEN USED EVEN WHEN STORED IN A VARIABLE THE LIST IS PERMENANTLY CHANGED, THE ORIGINAL LIST ITEM IS REMOVED PER POP. YOU CAN USE POP IN CONTEXT OF THE ORDER ON THE PAGE

#so remove deleted list item. pop takes it to be used in something else. sometimes you will need to loop over a list if something gets added back

