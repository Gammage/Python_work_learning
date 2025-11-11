##glossary 2 exercise##
#clean up exercise 6-3
#replace series of print calls with a loop runs through the dictionarys keys and
#values
#then add five more python terms to the glossary

glossary = {'function':'pull something from a variable/object, find a result',
            'method':'change a variable, do something to an object',
            'variable':'create something that can store a value or data',
            'object':'a thing that stores data and knows how to do stuff with it',
            'string':'a sequence of characters'}

for term, definition in glossary.items():
    print(f"{term.title()} = {definition}")
    
glossary['syntax'] = 'a code language'
glossary['loop'] = 'repeats something multiple times'
glossary['condition'] = 'lets program make decisions'
glossary['class'] = 'a blueprint for making objects'
glossary['dictionary'] = 'a set of key value pairs, abit like a list'

print('\nupdated list:')
for term, definition in glossary.items():
    print(f"new list {term.title()} = {definition.capitalize()}")
    
