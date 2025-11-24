##ADDITION CALCULATOR exercise##
#wrap up code from exercise 10-6 in a while loop so user can continue entering 
#numbers, even if they make a mistake and enter text instead of a number

print("give two numbers. type f to quit")
while True:  
    number_one = input("first number:")
    if number_one == 'f':
        break
    number_two = input("second number:")
    if number_two == 'f':
        break
    
    try:
        num_one = int(number_one)
        num_two = int(number_two)

    except ValueError:
            print("friendly error message")
    else:
            total = num_one + num_two
            print(total)
    

    