
####################copying a list###############################
    #copying a list
    #often want to start with an existing list and make an entirely new list based on the first one
    
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print('\nmy favourite foods are:')
print(my_foods)

print('my friends favourite foods are:')
print(friend_foods)

    #we make a copy using [:] (empty first and second index)
    #tells python to make a slice that starts at the first item and ends with the last item
    #producing a copy as the index is empty, so it assigns the entire list
    
my_foods.append('chocolate')
friend_foods.append('pineapple')

print(f'\nmy new fav food list {my_foods}')
print(f'my friends new fav food list {friend_foods}')

    #point is, we need to assign a slice so that we can copy the original list.
    #if we just did friend_foods = my_foods, then it tells python to associate the new variable with the same list.
    #that would mean any changes would apply to both variables/lists. see below.
    
print('\nAn example of incorrect list copying, see code')
bummys_foods = ['pitta bread','battered mars bar']
robs_foods = bummys_foods
robs_foods.append('bacon')
print(f'this would be bummys food {bummys_foods}')
print(f'this would be robs food {robs_foods}')

