##NESTING##
#a list of dictionaries. dictionaryception
    #sometimes you'll want to store multiple dictionaries in a list, or a list of
    #items as a value in a dictionary (nesting). 
    
#in the aliens example below, it has information to store one alien, but not
#multiple aliens. so you can arrange the aliens in a list

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'blue','points':10}
alien_2 = {'color':'yellow','points':15}

aliens = [alien_0, alien_1, alien_2,]

for alien in aliens:
    print(alien)

#list containing multiple dictionaries

#a more practical approach would involve more then 3 aliens with code that
#automatically generates each alien. in the following example, we use range()
#to create a fleet of 30 aliens;

#make an empty list of aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)

#show how many aliens created:
print(f'total amount of aliens {len(aliens)}')

#create a new list aliens
#create a loop of 30 for alien_number using range()
#for each number a new_alien with the dictionary keyvalue pair(S)
#for each alien created we add to the list new_alien

#for alien in aliens[:5] is first 5 as first number omitted in slice
#print the list

#using len to count total amount of aliens in print

#books saying imagine usecase of changing colours depending if alien is faster
#look at the key-value pairs combo insinuating. eg

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
#show the first five aliens
print("\nnew five aliens")
for alien in aliens[:5]:
    print(alien)
    
#we want to modify the first 3 aliens, we loop through a slice that includes them
#only. all of the aliens are green, but won't always be the case.
#you could expand the program with elif and else to add extra coloured aliens with
#different values (faster, more points)

#its common to store a number of dictionaries in a list when each dictionary
#contains many kinds of informatino about one object. eg, creating users on a 
#website as did in user.py

#all of the dictionaries in the list should have an identical structure, so you
#can loop through the list and work with each dictionary object in the same way

