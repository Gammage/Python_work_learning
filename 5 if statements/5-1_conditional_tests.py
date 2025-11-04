#write a series of conditoinal tests.

jungler = 'shaco'

if jungler == 'annie':
    print('true')

if jungler != 'annie':
    print('annie is not a jungler')
    
if jungler == 'shaco':
    print('shaco is a jungler')
    
food = ['chicken','eggs','bacon']

for food_item in food:
    if food_item == 'chicken':
        print('this is a food item')
              
banned_champions = ['mel','shaco','jarvan']

# champion = 'shaco'
# champion_two = 'elise'

# if champion not in banned_champions:
#     print('shaco champion is available')
    
# if champion in banned_champions:
#     print('shaco is banned lel')
    
# if champion_two not in banned_champions:
#     print('elise is available')
    
junglers = ['shaco','elise']

# if jungler in banned_champions:
#     print (f'{jungler} is banned')
# else:
#     print(f'{jungler}is available')
        
for jungler in junglers:
    if jungler in banned_champions:
        print (f'{jungler} is banned')
    else:
        print(f'{jungler} is available')
        
#i skipped ahead abit with this
     