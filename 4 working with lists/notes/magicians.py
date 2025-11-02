# this is an example of looping over the list

magicians = ['alice','david', 'carolina']
for magician in magicians:
    print(magician)
    
# look at this closely. for magician is a new variable
# define a for loop (we called the 'a' magician in this loop), then in magicians = each list item gets put into magician, starting with first one.
# alot of people use a but it can be anything. naming convention makes sense to call magician, as its pulling from a list of magicians
# the print(magician) prints on the terminal each item in magician from magicians list, for each list item the for loop goes through.

# the books definition 'for every magician in the list of magicians, print the magicians name'
# the output is a simple printout of each name in the list

#the most common way computer automates repetitive tasks

#the list contains multiple values, always starts the first one

#after the first list item, it goes through the next magician in magicians, which is david. then printout happens again

#program ends when all list items have been printed out

#gpt summary;
# magician is a variable created for the loop

# The loop goes through each value in the list, one at a time

# Each value is assigned to magician in order

# print(magician) prints the current value

# The loop stops when all values are processed

# Meaningful variable names improve readability

# It automates repeating tasks

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    
#notice how the print personalises each message for each magician
#you can write as many lines of code as you like in the for loop, it counts for inside the loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f'I cant wait to see the next trick {magician.title()}!')
    
# doing something after a for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f'I cant wait to see the next trick {magician.title()}!')
    # print('thankyou for everyone for a magic show')
    
print('thank you everyone for a magic show')

#as the 3rd print function isnt in the for loop (not indented) its not repeated per magician.

# book states (paraphrased) when processing data for loop, find this is a good way to summarise an operation was performed on a data set. eg, use a for loop to
# initialise a game by running through a list of characters & displaying each character on a screen. might write some code after this loop displays a play now button
# after all chars have been drawn to the screen

#indentations determines how a line/lines related to rest of a program
#indentions are a perk of pythons readability. so it helps to identify errors

# it will prompt if not indented

#and sometimes theres a logical error. if you didnt indent in a for loop, print function or whatever is treated outside the loop, hence in previos example
# thank you everyone for a magic show prints after the for loop ends

#refer to the hellow_world.py for indent errors