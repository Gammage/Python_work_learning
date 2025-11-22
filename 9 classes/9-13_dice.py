##dice exercise##

#make a class die with one attribute called sides
#which has a default value of six
#write a method called roll_die that prints a random number between 1-6
#make a six sided die and roll it 10 times
#make a 10 sided die and roll it ten times

from random import randint

class Die:
    """a dice"""
    
    def __init__(self,sides=6):
        """initialising the dice"""
        self.sides = sides
    
    def roll_die(self):
        """we roll the dice"""
        print(randint(1,self.sides))
          
               
dice = Die(20)
  
n = 0
while n < 10:
    dice.roll_die()
    n += 1