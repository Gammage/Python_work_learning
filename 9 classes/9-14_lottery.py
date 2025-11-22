##lottery exercise##

#make a list or tuple containing a series of 10 numbers and 5 letters
#randomly select 4 numbers or letters from a list and print a message saying that
#any ticket matching these 4 numbers or letters win a prize

# from random import randint
from random import choice

my_lottery_ticket = ('c',3,'a',3,'b',5,'d',1,'a','a','c','b','d',5,'d')

lottery_list = list('abcde') + list(range(10))

winning_lottery = []

lottery_pick = 0
while lottery_pick < 4:
    winning_lottery.append(choice(lottery_list))
    lottery_pick += 1
    
print(f"any ticket matching this list {winning_lottery} wins!")


    

    
