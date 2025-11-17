##8-10 sending messages exercise##
#with a copy of exercise 8-9,
#write a function called send messages that prints each text message
#and it moves each message to a new list called sent_messages as its printed
#after calling the function, print both of your lists to make sure the messages
#were moved correctly




text_list = ['hello','how are you','i like chicken','this is a txt message']

sent_messages = []

print(f"this is the text list before: {text_list}")

def send_messages(texts, sent_texts):
    """moving messages from one list to another"""

    while texts:
        message = texts.pop()
        print(f"sending {message.title()}")
        sent_texts.append(message)
        
send_messages(text_list,sent_messages)

print(f"this is the text list after {text_list}")
print(f"this is the sent messages list {sent_messages}")


    
    