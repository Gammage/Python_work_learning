##7-3 multiples of ten##
#ask the user for a number
#report whether the number is a multiple of 10 or not

user_number = int(input("please give me a number"))


if user_number % 10 == 0:
    print(f"{user_number} is a multiple of 10")
else:
    print(f"{user_number} is not a multiple of 10")
    
#we define user_number variable by using int function with a input function inside
#we prompt the user please give me a number
#we use that integer in a if statement using modulo of 10 to make sure we get the 
#multiplier of 10, if theres a remainer it will go to else and inform the user 
#that said number isnt a multiplier of 10 :) 

