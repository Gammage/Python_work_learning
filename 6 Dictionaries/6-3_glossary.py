###Calling glossary exercise###

#a python dictionary can be used to model an actual dictionary, but to avoid
#confusion this is called a glossary. apparently.

#think of five programming words from previous learnings.
#use words as keys and  values as descriptions

#print each word and its meaning in a nearly formatted output

glossary = {'function':'pull something from a variable/object, find a result',
            'method':'change a variable, do something to an object',
            'variable':'create something that can store a value or data',
            'object':'a thing that stores data and knows how to do stuff with it',
            'string':'a sequence of characters'}

for term in glossary:
    print(f"\nThe term {term.title()}: {glossary[term]}")
    

    
    