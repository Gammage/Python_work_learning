##GUEST EXERCISE 10-4##
#write a program that prompts user for their name.
#when they respond, write their name to a file called guest.txt

from pathlib import Path

path = Path('10 files and exceptions/guest_exercise.txt')

message = input("what is your name?")

content = path.write_text(message)



