##favourite fruit exercise

favourite_fruit = ['banana','orange','apricot']

for fruits in favourite_fruit:
    if fruits == 'banana':
        print(f'you really like {fruits}!')
    if fruits == 'orange':
        print(f'you really like {fruits}')
    if fruits == 'apricot':
        print(f'you really like {fruits}')
    if fruits == 'pineapple':
        print(f'nobody likes {fruits}')
    if fruits == 'blueberries':
        print(f'nobody likes {fruits}')
    
##apparently the above isnt the answer, they wanted independant if statements
#like below;

if 'banana' in favourite_fruit:
    print('banana')
if 'orange' in favourite_fruit:
    print('orange')
if 'apricot' in favourite_fruit:
    print('apricot')
    
#use case for each situation