#more conditional exercises, using inequality strings and using the lower
#method

first_number = 20
second_number = 30

if (first_number >= 23) and (second_number >= 23):
    print('true')

if (first_number <= 23) and (second_number >= 23):
    print('first if/and should work')

if (first_number >= 19) or (second_number >= 23):
    print('second if/or should work')
    
caps_on = 'AUDI'
caps_off = 'audi'
if caps_on.lower() == caps_off:
    print('this should print')
    
second_caps_off = 'balls'
second_caps_onn = 'BALLS'
if second_caps_off.upper() == second_caps_onn:
    print('this should also print')
    

