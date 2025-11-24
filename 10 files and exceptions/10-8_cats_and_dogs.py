##cats and dogs exercise##
#make two files cats and dogs.txt
#store at least three names of cats in the first file and three names of dogs in 
#the second 
#write a program that tries to read fhese files and print the contents of the file to 
#the screen
#wrap your code in a try-excpet block to catch the filrnotfound error
#print a friendly message if a file is missing
#move one of the files to a different location on your system, and make sure
#the code in the except block executes properly

from pathlib import Path

def readfile(path):
    """reads the file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"file path {path} is missing")
    else:
        print(contents)
        
filenames = ['cats.txt','dogs.txt','chicken.txt']
for filename in filenames:
    path = Path(f'./10 files and exceptions/{filename}')
    readfile(path)