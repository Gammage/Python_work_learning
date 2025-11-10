##favourite numbers exercise

##use a dictionary to store peoples favourite numbers
#random

favourite_numbers = {'Bob':4,
                     'jeff':3,
                     'shaco':6,
                     'chey':8,
                     'alex':2,}


for name in favourite_numbers:
    print(f'{name} favourite number is {favourite_numbers[name]}')
 
 
 #as the for loop addresses referencing the key value, referencing it again in
 # favourite_numbers[name] goes a step furhter. thats how im understanding it
 #because we called the name already, it picks the value from the key name in 
 #the dictionary
 
 
 
 
    