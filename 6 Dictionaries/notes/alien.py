##alien example for simple dictionary
#dictionary item for an alien that can have a colour and point value;

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#notice
    #dictionary is created with curly brackets {}
    #when referencing a dictionary item you call the dictionary variable,
    #then the key that holds the value. key being color, green being the value
    
##as the book says, i think this will take practice

#Dictionary is a list of key value pairs
#a dictionary can store as many key value pairs as possible

print('example of using dictionary in print')
new_points = alien_0['points']
print(f"you have just earned {new_points} points!")

#pull value from key points (value of polints is defined in the dictionary)
#new_points is assigned this value. which we use in the print function

#dictionaries are dynamic


###ADDING TO A DICTIONARY###

print(f'before adding to the dict {alien_0}')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f'after adding to the dict {alien_0}')

#so the x_postiion and y_position was added to the alien_0 dictionary
#they retain the order in which they are defined


##STARTING WITH AN EMPTY DICTIONARY###
print('\nRESETTING DICTIONARY')
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
#define an empty dictionary
#add the key color and assign it value green
#add the key points and assign it value 5 points


###MODIFYING A DICTIONARY###
print('\nMODIFYING A DICTIONARY')
alien_0 = {'color':'green'}
print(f'this alien is {alien_0["color"]}')
alien_0 = {'color':'blue'}
print(f'this alien is {alien_0["color"]}') 

#say a game progresses and aliens change colours
#define a dictionary for alien_0 that conatiains only the aliens colour
#(i guess even if theres more key value pairs its not relevant as its aliens
#color only)
#then change the value of the key. you reference the dictionary in the print

#another example

print('\nmore complicated example of modifying list')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium',}
print(f'Original position: {alien_0["x_position"]}')

#move alien to the right
#determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    #fast alien
    x_increment = 3
    
# new position is old position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'new position {alien_0["x_position"]}')

#start by defining aliens position with dictionary key values x_position and
#y_position, as well as the speed as 'medium'
#if the speed of alien is slow, we add 1 to the variable x_increment
# if the speed is medium, 2 to x_increment. 3 for fast.
#we then add the x_increement variable to the x_position by adding them to 
#alien_0 x_position key

#i mean if nothing else other then slow or medium it would go fast


##Removing Key-value Pairs
#when you don't need a piece of info in a dictionary deleted
#note it removes permenantly
print(f'\nDeleting key value information')
alien_0 = {'color':'green','points':5}

del alien_0['points']

print(alien_0)

