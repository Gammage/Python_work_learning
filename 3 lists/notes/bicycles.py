# see what is a list.txt for context

bicycles = ['trek', 'cannondale','redline','specialised']
print('\nbelow is the list from the variable bicycle')
print('bicycles in the list are trek, cannondale, redline, specialised')
print(bicycles)

# for returning specificed list item, you reference the number in its order. with python, the list starts at 0
print('\nexample printing first item on list (0)')
print(bicycles[0])

# you can also format the specific list item, giving it a title eg;
print('\nexample of using title method on string item')
print(bicycles[0].title())

#further example of order of list items
print('\npicking out list item 0 and 3 from the 4 bikes (4 bikes = 0, 1, 2, 3)')
print(bicycles[1])
print(bicycles[3])

# to accessing last item in a list, you type index -1. python returns the last item on list (you might not know how long the list is)
# -1 would be the last list item, -2 second last, -3 3rd last. etc. it COUNTS from one but list starts 0
print('\nfor finding last indexed list item -1')
print(bicycles[-1])

#using individual values in a list
print('\nindividual values from a list, in this case a string')
print(f'my first bike was supposedly {bicycles[0].title()}')


