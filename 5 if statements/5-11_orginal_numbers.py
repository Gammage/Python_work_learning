##orginal loops exercise.
##store 1-9 through a list
##loop through list
##use an if-elif-else chain inside the loop to label each number with the 
#appropiate ordinal

# range(1,10)

num_list = list(range(1,10))
#LIST tells you to create whatever is in the parenthesis into.. a list.

for num in num_list:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')

