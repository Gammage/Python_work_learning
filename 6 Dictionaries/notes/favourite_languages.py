###Dictionary of similiar objects###

#previous example (alien.py) involved storing different kinds of information
#about one object, an alien in a game.

#you can use a dictionary to store one kind of information about many objects

#an example in the book, is information from a poll (hypothetically) to ask
#them their favourite programming language

#a dictionary is useful for storying the results of a simple poll, eg;

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': 'rust',
    'phil': 'python',
}

#in python, press enter after the opening brace! this syntax format is useful
#for clean clear written code
    #most development environments will match the indents for the next key-pair
    #just bare in mind indents in python are important
    
#good practice to leave a comma at end of every key pair - even last one for 
#future changes

language = favourite_languages['sarah'].title()
print(f'Sarahs favourite language is {language}.')

#we ask for her favourite language when defining the language variable
#you can use this syntax with any individual represented in the dictionary

