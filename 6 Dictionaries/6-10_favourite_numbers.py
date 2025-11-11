##favourite_numbers##
#modify exercise from 6-2
#each person can have more than one favorite number
#then print each persons name along with their favourite numbers

favourite_numbers = {'Bob':[4,6,7,8],
                     'jeff':[3,2,1,86],
                     'shaco':[6,3,7],
                     'chey':[8,45,34],
                     'alex':[2,45,78],
                    }

for name, numbers in favourite_numbers.items():
    numbers.sort()
    print(f"each {name.title()} favourite numbers:")
    for number in numbers:
        print(f"{number}") 

##number sort before each number, reduce work