##Looping through a dictionary##

##a single python dictionary can contain a few key-value pairs  or millions
#as dictionarys a large python lets you loop through them

#several ways to loop through a dictionary
    #you can loop through each value within a dictionary: keys/values/pairs(both)

# user_0 = {'username':'efermi',
#           'first':'enrico',
#           'last':'fermi'}

# for key in user_0:
#     print(f'{key} is the key and {user_0[key]} is the value')
    
#in above, this is how you would reference the key and its value. see the value
#reference

###USING ITEMS()###

#items() allows to reference the key and value pair in a dictionary
# for key, value in user_0.items():
#     print(f'{key}: {value}')

# any name can be used in key and value eg.
for k, v in user_0.items()

# examples of this being affective can be seen in favourite_languages.py

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': 'rust',
    'phil': 'python',
}

for k, v in favourite_languages.items(): 
    print(f"\n{k}'s favourite language:")
    print(f"{v}")
    
#because the keys refer to a persons name of each person in the dictionary and
#their favourite language you get the same output as above for loop
#for code to be easily read they should be whats referenced in the for loop, like
#so

print("\nRevised syntax:")
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
 
   
##Looping through Keys()##
#for when you want to loop through keys in dictionary
#not always need the values (or both)

for key in favourite_languages.keys():
    print(f"{key.title()}")

#exact same behaviour if not using keys(), as above. it can make code easier to
#read (i will be using key() for simplicity)

#you can access the value associated with any key you care about inside the loop
#

friends = ['phil','sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\n{name.title()}, I see you love {language}")
        
if 'erin' not in favourite_languages.keys():
    print("erin, please take our poll")
        
#we have the dictionary
#we have the list
#we have a for loop going through the key in the dictionary (name in favourite_languages)
#we print the name of each
#we nest an if statement referencing the key (we call it name) of names.
#we create a variable language which holds the value of each key (their fav languages)
#we print the name(key) and the  value(language) of the dictionary items.

#Note: because we call on the keys first, they are always called out in order of
#dictionary.

#keys() method isnt just for looping. it returns a sequence of keys, and the
#if statement simply checks if 'erin' is in this sequence. because shes not, 
#message is printed in the poll
    

###LOOPING THROUGH A DICTIONARY IN A PARTICULAR ORDER###
#looping through a dictionary returns the items in the same order they where inserted
    #you may want to change the order!
    
#one way to do this, is to sort the keys as they're returned in the for loop

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

for name in sorted(favourite_languages.keys()):
    print(f"\n{name.title()}, thankyou for taking the poll")
    
#sorted arranges the dictionary items in alphabetical order.


##LOOPING THROUGH ALL VALUES IN A DICTIONARY##


