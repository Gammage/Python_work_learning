###If-elif-else chain###

#often, will need to test more then two possible situations
#python executes only one block in an if-elif-else chain
#runs each conditional in order
#when a test passes, code following that test is executed
    #python skips the rest of the tests
    
#example of real world scenario:
    #admission for anyone under 4 is free
    #admission for anyone between the ages of 4-18 is $24
    #admission for anyone age 18 or older is $40
    
age = 17

if age < 4:
    print('children under 4 come free!')
elif age < 18:
    print('the price of entry is $24 ')
else:
    print('the price of entry is $40')

#age is 17

#if age is less than seven print: children under 4 come free
#else if age is less then 18 print: price of entry is 24
#else print: price of entry is 40

#the elif line is really another if test.

#for the above to me more practical, the following is best.
age = 12

if age <4:
    price = 0
elif age < 18:
    price = 24
else:
    price = 40
    
# print(f'your price is ${price}')

#the code is narrower in above. the price value is set by this chain
#and the print out is outside the if statement.
#you would only need to change the print message once instead of 3 times

#you can also use multiple elif blocks.
#if the amusement park wanted to add discounts for seniors, you could add
#another conditional test. eg, 65 year old/older pays 20:

age = 64

if age <4:
    price = 0
elif age < 18:
    price = 24
elif age >= 65:
    price = 20
else:
    price = 40

print(f'your price is ${price}')

#!python does not need an else block!#
#sometimes, its better not to have one. other times it is.

#omitted example without else for above

if age <4:
    price = 0
elif age <18:
    price = 24
elif age <65:
    price = 40
elif age >= 65:
    price 20
    
#the if statement covers all age brackets, without needing an else block
#else block is a catch all statement. matches any conditions that wasn't
#specific to the if or elif. if you have a specific final condition, such as
#the above example, you can omit the else block.

#the if/elif/else chain is powerful when you need one thing to pass. it skips
#the rest if it does.

#sometimes you need to check all conditions of interest.
#in which case, a series of if statements with no elif or else blocks.
    #this is for examples when more then one if statement/condition is true - 
    #when you want to act on every condition that is true