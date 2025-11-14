##No pastrami exercise##
#using exercise from 7-8, make sure the sandwich pastrami appears in list 3 times
#then use a while loop to remove all occurances of pastrami from sandwich orders
#make sure they dont end up in finished_sandwiches

sandwich_orders = ['peanut sandwich','pastrami','jam sandwich',
                   'pastrami','BLT','prawn mayo','bacon sarnie',
                   'pastrami',]
complete_orders = []

#while theres a list

while 'pastrami' in sandwich_orders:
    print('we ran out of pastrami orders sry')
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"completing order for {sandwich_order.title()}")
    complete_orders.append(sandwich_order)
    
print("no more orders")
print(complete_orders)

##having a seperate while loop that removes items list seperately seems to be
#cleaner code.