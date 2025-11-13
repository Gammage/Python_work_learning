##the for loop takes a collection of items and executes a block of code
#once for each item in the collection

#in contrast, the while loop runs as long as or while, a certian condition is
#true

#you can use a while loop to count up through a series of numbers. for example,
#the following while loop counts from 1 to 5:

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#while current number is less than or equal to five
#print the number
#add to the number 1
#repeat until 5

#programs used everyday will most likely contain while loops
#an example of while loop, a game needs one to running as you want to keep playing
#so it can stop running as soon as you ask it to quit
#programs wouldn't be fun to use if they stopped running before we told them to
#or kept running even after wanted to quit, so while loops are quite useful

##USING CONTINUE IN A LOOP##

#Rather then breaking a loop entirely you can return to the beginning, based on
#the resulf of a conditional test.

#eg, a a loop counts from 1- 10 but prints only the odd numbers in that range

current_number = 0

while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0: 
        continue
    print(current_number)

#continue ends the loop where its situated then resets the loop

#current_number is set to 0
#while variable current_number is less than or equal to 10
#current number variable = current number + 1,
#we then have a if statement on no remainder when divided by 2
#if the number has no remainder, therefore it is even, we go back to begining
#and plus one, theres a remainder so print

#while loops needs a way to stop running otherwise it continues forever
#eg

x = 1
while x <= 5:
    x += 1
    print(x)
    
#if omit x += 1, loop will go on forever, as x will never be more then 5
#every programmer makes this mistake, especially with subtle exit conditions
#if a program gets stuck in an infinite loop. press ctrl-c/close terminal

#to avoid this, test every while loop :)

#to end program when user enters a certian input value, run program and enter
#that value.


    
