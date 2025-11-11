##use the code in favourite_languages.py
#make a list of people who should take the favorite languages poll.
    #include some names that are already in the dictionary and some that are not
    #loop through the list of people who should take the poll. if they already
    #have, print a message thanking them for responding. if they have not yet
    #taken the poll, print a emssage inviting them to take the poll
    
favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': 'rust',
    'phil': 'python',
}

should_take_poll = ['jen','bummy','rob','phil','ben']

for voters in should_take_poll:
    if voters in favourite_languages.keys():
        print(f'{voters}, you have already voted!')
    else:
        print(f'{voters}: Vote on your favourite language!')
        
    