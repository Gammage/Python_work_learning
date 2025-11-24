##COMMON WORDS EXERCISE##
#find something on guternberg, copy pasta to a txt file
#use count() method to find out how many times a word of phrase appears in a string
#write a program that reads the files you found at project guternberg
#determine how many times the was used
#try counting 'the ', with a space in the string, see how much lower your count is

from pathlib import Path

text_files = ['little women.txt','moby dick.txt','alice.txt']

def count_the(path):
    """counting the in files"""
    
    try:
        contents = path.read_text(encoding='utf-8').lower().count('the ')
    except FileNotFoundError:
        print("IT AINT THERE")
    else:
        print(contents)

for file in text_files:
    path = Path(f"./10 files and exceptions/notes/{file}")
    count_the(path)
    
#we import the library pathlib and import class path
#we then create a list called text_files which is the list of text files we use later
#we then creat a function called count_the with a paramter path
#we use a try except else block where we 'try' to create a contents variable and
#assign the path parameter with a chain method(S) of read text and count.
    #read text changes the txts files into strings (Default bytecode i think?)
    #count counts the specified string in the paranthesis. note the space (so we
    # dont find 'thens' and 'theres)
    #we handle filenotfound exceptions with a print string
    #else we print the contents variable
#we then create a for loop for file in text files
#we finally create the path variable and assign the path class with a string ref
#the files in our list enabling the correct path directory for respective files
#we then call the function and pass it our new path variable for each file



    


    
    