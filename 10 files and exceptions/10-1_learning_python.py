##LEARNING PYTHON EXERCISE 10-1##
#open a blank file
#write a few lines summarising what you've learned so far
#save as learning_python.txt
#write a program that reads the file and prints what you wrote two times:
#print the contents once by reading in the entire file,
#once by storing the lines in a list then looping over each line

from pathlib import Path

path = Path('./10 files and exceptions/learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
the_string = ''
for line in lines:
    the_string += line

print(the_string)
    

# single represents the dir you are in
# double represents the parent of the dir