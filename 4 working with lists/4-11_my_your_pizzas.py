#my pizzas, your pizas
    #from exercise 4-1, copy pizza list and make friend_pizzas
        #add a new pizza to original list
        #add a different pizza to friends list
        #prove two diff lists
        
pizzas = ['farmhouse','margheritta','meat feast']
friend_pizzas = pizzas[:]

for pizza in pizzas:
    print(f'I like {pizza.capitalize()} pizza toppings')
print('I like pizzas woo')

pizzas.append("pepperoni")
friend_pizzas.append("vegan")

print(pizzas)
print(friend_pizzas)

print(f'\nmy favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print(f'\nmy friends favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)

