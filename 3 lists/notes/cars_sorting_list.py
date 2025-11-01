# sort list
# sort list goes from a-z
cars = ['bmw', 'audi', 'toyota']
cars.sort()
print(cars)

# this is permenantly changing the list
# reverse true goes from z-a
#true or false needs to be capitalise
cars.sort(reverse=True)
print(f'\nreverse cars list with reverse=True {cars}')


cars = ['bmw', 'audi', 'toyota']
# temporarily sorting list. doesnt change actual list, displays it in a sorted order such as in a print function
print('\nbelow is sorted cars')
print(sorted(cars))
print(f'original still says {cars}')

#apparently sorting a list is more complicated when all values are not in lowercase

# reverse cars
cars = ['bmw', 'audi', 'toyota', 'tesla']
print(f'\nnew cars list:{cars}')
cars.reverse()
print(f'reverse cars list permenantly result:{cars}')
cars.reverse()
print(f'can use reverse again to permenantly reverse{cars}')

#finding the length of the list
len(cars)
print("\nfinding the length of a list using len()")
print(f'the length of the cars list {cars} is {len(cars)}')
#very useful. imagine when you need to count the result of a list, alien need to be shot down remaining in a game, registered users on a website. other shit.