##restuarant seating exercise 7-2##
#write a program that asks the user how many people are in their dinner group
#if answer > 8 print a message saying they'll have to wait for a table. otherwise
#report table is ready

dinner_group = input("how many people in your dinner group?")

dinner_group = int(dinner_group)
if dinner_group >8 :
    print(f"you will have to wait for a table")
else:
    print(f"table is ready")
    
#dinner_group variable stores the input()
#int() then converts variable string to int
#if/else statement if number greater then 8 you will have to wait for table
#else table is ready :)