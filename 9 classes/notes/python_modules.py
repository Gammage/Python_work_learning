##few examples of python standard library modules##

#the python standard library comes with many useful modules one can use
#eg

###RANDINT###

from random import randint

number = randint(1,6)
print(number)

#randomnises a number between a specified range

##CHOICE

from random import choice

players = ['ben','jack','bummy','rob']
firstup = choice(players)

print(firstup)

#choice randomises list

#random module shouldn't be used when building security-related applications,
#works for fun and interesting projects

##you can also download modules from external sources. see examples of this in part 2,
#will need external modules to complete project

