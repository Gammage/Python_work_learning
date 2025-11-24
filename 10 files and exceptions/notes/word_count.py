##WORKING WITH MULTIPLE FILES##

#running an 'analysis' over multiple books by using the count_words()

# from pathlib import Path

# def count_words(path):
#     """count the approximate number of words in a file"""
    
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"sorry, the {path} does not exist")
#     else:
#         #count number of words in a file
#         words = contents.split()
#         num_words = len(words)
#         print(f"the file {path} has about {num_words} words")

# filenames = ['alice.txt','siddhartha.txt','moby dick.txt','little women.txt']
# for filename in filenames:
#     path = Path(f'./10 files and exceptions/notes/{filename}')
#     count_words(path)
    
#the try-except block in thise example provides two significant advantages
    #prevent our users from seeing a traceback, allowing to continue aanalysing the
    #texts is able to find
    #if we dont catch the filenotfounderror that siddhartha.txt raises, the user would
    #see a full traceback. program would stop running after trying to analyze siddhartha
    #it would never analyse the following texts moby dick and little women
    
#Failing silently#
#dont need to report every exception
#sometimes you want the program to fail silently
    #continue on as if nothing happened
#see code

from pathlib import Path

def count_words(path):
    """count the approximate number of words in a file"""
    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        #count number of words in a file
        words = contents.split()
        num_words = len(words)
        print(f"the file {path} has about {num_words} words")

filenames = ['alice.txt','siddhartha.txt','moby dick.txt','little women.txt']
for filename in filenames:
    path = Path(f'./10 files and exceptions/notes/{filename}')
    count_words(path)
    
#in this instance, the pass statement also acts as a placeholder, a reminder choosing
#to do nothing at a specific point in your programs execution & that you might
#want to do something there later, but it still goes through that block

##Deciding which errors to report##

#knowing when to report an error to users and when to report silently?
#giving user information they arent looking for can decrease usability of program
#pythons error handlinggives you fine grained control over how much to share with
#users when things go wrong

#but when a program depends on something external such as user input, existance of 
#a file, availability of a network connection, there is a possibility of an exception
#being raised. a little experience will help you know where to include an
#exception handling block in your program and how much to report to users about 
#errors that arise

