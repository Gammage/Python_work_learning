##messages exercise##
#make a list containing a series of short text messages. pass the list to a function
#called show_messages(), which prints each text message

text_list = ['hello','how are you','i like chicken','this is a txt message']



def show_messages(texts):
    """prints txt messages in list"""
    for text in texts:
        print(text.title())
        

show_messages(text_list)

#because the function returns nothing, when you print the function after this
#it prints none. you aren't printing the list but the result of the function,
#which doesnt provide anything new?


    