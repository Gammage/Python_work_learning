##Lottery analysis##

#you can use a loop to see how hard it might be to win the kind of lottery you just
#modeled
#make a tuple list called my_ticket
#write a loop that keeps pulling numbers until your ticket wins
#print a message reporting how many times the loop had to run to give you a winning ticket

from random import choice

my_lottery_ticket = ('c',8,'e','c',)

lottery_list = list('abcde') + list(range(10))

ticket_attempt = 0
while True:
    winning_lottery = ()
    lottery_pick = 0
    while lottery_pick <4:
        winning_lottery += (choice(lottery_list),)
        lottery_pick += 1

    if my_lottery_ticket != winning_lottery:
        ticket_attempt += 1
    else:
        print(f"after {ticket_attempt} attempts, you won!")
        break

    
    
    