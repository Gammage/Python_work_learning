#simplest kind of if statement has one test and one action
###if statement###

# if conditional_test:
    # do something
    
#you can put any conditional test in the first line and just about any action
#following in the indented block test

age = 19

if age >= 18:
    print("you are old enough to vote")
    print("have you registered to vote yet?")
    
#indentation plays the same role in if statements as it did for loops
#you can have any amount of lines after an if statement

###if-else statements###
age = 17

if age >= 18:
    print('you are old enough to vote!')
    print('have you registered to vote yet?')
else:
    print('you are too young to vote!')
    print('register to vote when you are 18')
    
#as age is less then 18, it is false, so goes to else
#the above is useful if want to execute one of two actions.

