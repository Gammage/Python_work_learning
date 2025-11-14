##Deli 7-8 book exercise##
#make a list called sanwich_orders, fill with various sandwiches
#loop through list of sandwich orders print message for each order
#as each sandwich is made, move it to the list of finished sandwiches

#after all sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = ['peanut sandwich','jam sandwich',
                   'BLT','prawn mayo','bacon sarnie']
complete_orders = []

#while theres a list

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    
    print(f"completing order for {sandwich_order.title()}")
    complete_orders.append(sandwich_order)
    
    # for sandwich in complete_orders:
        # print(f"{sandwich.title()} is ready")
    
print("no more orders")
print(complete_orders)