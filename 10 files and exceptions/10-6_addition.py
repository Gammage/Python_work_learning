##ADDITION EXERCISE##
#one common problem when prompting for numerical input occers when people
#provide text instead of numbers. when you try to convert the input to an int,
#you'll get a valueerror.
#write a program that prompts for two numbers
#add them together and print the result

#catch the value error if either value is not a number,
#print a friendly erorr message: test program by entering 2 numbers
#and then entering text instead of number

print("give two numbers")
number_one = input("first number:")
number_two = input("second number:")

try:
    num_one = int(number_one)
    num_two = int(number_two)
except ValueError:
    print("friendly error message")
else:
    total = num_one + num_two
    print(total)
    

    
    