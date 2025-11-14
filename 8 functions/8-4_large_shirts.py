##large shirts##
#modify the make_shirt() function so that shirts are large by default
    #with a message saying 'i love python'
    #make a large shirt and medium with the default message, and a shirt of any
    #size with a different message

def make_shirt(size_shirt='large',message_print='i love python'):
    """making a shirr"""
    print(f"shirt size {size_shirt} with print {message_print.title()}")
    
make_shirt()
make_shirt(size_shirt='medium')
make_shirt(message_print='i love coca cola')


