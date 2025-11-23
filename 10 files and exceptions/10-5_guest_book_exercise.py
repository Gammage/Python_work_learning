##GUEST BOOK EXERCISE##
#write a while loop that prompts users for their name
#collect all the names that are entered, then write these names to a file called
#guest_book.txt
#make sure each enmtry appears on a new line in the file

from pathlib import Path

path = Path("./10 files and exceptions/guest_book.txt")
content = path

names = ''
while True:
    message = input("Please enter Name, or press f to quit:")
    if message == 'f':
        break

    names += message + " "
content.write_text(names)
