#min and max digits, plus the sum of all the values in the list

digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

####################slicing a list###############################
    #how to work through all elements in a list
    
#how to slice a list
    #specify the index of the first and last element to work with
    #0 seems
print('\nslicing a list')
players=['charlies','george','martina','michael','florence','eli']
print(f'the full list {players}')
print(f'the list 1-3 {players[0:3]}')
print(f'the list 1-4 {players[1:4]}')
print(f'if you remove first index of a slice, python starts your slice at the beginning (prints 4, :4) {players[:4]}')
print(f'if you do something like 2:, you skip the first two items {players[2:]}')

#book example of slicing. when creating a game, adding a players final score to a list every time that player finishes playing. then you could sort the list in decreasing order
#then slice the first 3 scores

    
