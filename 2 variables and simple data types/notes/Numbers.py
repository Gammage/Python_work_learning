# add
print('\nADD')
print(f'2 + 3 = {2 + 3}')

#subtract
print('\nSubtract')
print(f'3 - 2 = {3 - 2}')

#multiply
print('\nMultiply')
print(f'2 * 3 = {2 * 3}')

#divide
print('\nDivide')
print(f'3 / 2 = {3 / 2}')
print(f'when dividing two numbers, you will always get a float eg. 4 / 2 = {4 / 2}')

print(f'\nNote: when mixing integer and float, answer will always be a float. eg, 1 + 2.0 = {1 + 2.0}\n')

#exponents uses two asterisks or multiply symbols
#exponent/index is the small number above and right of the base number. remmeber i would say in the below example 3 to the power of 2
#so below would be 9. 3 x 3. 
print('\nEXPONENTS/INDEX')
print(f'3 to the power of 2. so 3 x 3 = {3 ** 2}')

#3 to the power of 3 would be 3 x 3 x 3 so 27. i suck at simple math.
print(f'3 to the power of 3 example: {3 ** 3}')

#python supports the order of operations too (bodmas)
print('\nBODMAS example')
print(f'order of operations answer to 2 + 3 * 4 = {2 + 3 * 4}')

# any number with a decimal point is a float in python
(print('\nFLOATS'))
(print)(f'add with floats 0.1 + 0.1 = {0.1 + 0.1}')
(print)(f'issue with some float math is apparently it can get weird amount of decimal places like 0.2 + 0.1 = {0.2 + 0.1}')

# underscores in numbers. makes them readable, eg.
universe_age = 14_000_000_000
print(f'this number was underscored {universe_age} works for integers and floats')

#multiple assignments
# so adding multiple values to more then one variable in a single line
print('\nMultiple Assignments')
x, y, z = 1, 2, 3
print(f'adding values to muliple variables in one line \nX = {x}\nY = {y}\nZ = {z}')

# constants is a variable whos value stays the same throughout the life of a program
# a constant variable has a value that always stays the same, but python doesnt have a built in constant,
# so developers just uppercase variable so it should be treated as constant and never changed
print('\nConstants')
print('see the code notes')
MAX_HP = 100



