##Learning C exercise 10-2##
#you can use replace() method to replace any word in a string with a different
#word.

#read in each line from file just created replace the word 'python' with a name
#of another language. such as C. print each modified line to the screen

from pathlib import Path

path = Path('./10 files and exceptions/learning_python.txt')
contents = path.read_text()
print(f"{contents.title()}\n")
lines = contents.splitlines()

for line in lines:
    line = line.replace('python','C')
    print(line.title())





    




