##archived messages##
#start from your exercise at 8_10
#call the function send_messages() with a copy of list messages
#after calling the function, print both of your lists to show that the original
#list has retained its messages

text_list = ['hello','how are you','i like chicken','this is a txt message']

sent_messages = []

print(f"this is the text list before: {text_list}")

def send_messages(texts, sent_texts):
    """moving messages from one list to another"""
    new_list = texts[:]
    while new_list:
        message = new_list.pop()
        print(f"sending {message.title()}")
        sent_texts.append(message)
        
send_messages(text_list,sent_messages)

print(f"this is the text list after {text_list}")
print(f"this is the sent messages list {sent_messages}")