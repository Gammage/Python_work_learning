##READING FROM A FILE##

#CodeRunner implicitly runs the Python executable from inside the folder
# of your workspace
#filepath 'root' is displayed on the terminal. so direct filepath from that

#reading the contents

# from pathlib import Path

# path = Path('10 files and exceptions/notes/pi_digits.txt')
# contents = path.read_text().rstrip()
# # contents = contents.rstrip()
# print(contents)

#path is exact location of a file or folder in system
#python provides module called pathlib to make is easier working with files and
#directories
    #modules that provide specific functionality like this often called a library, 
    #hence the pathlib name
    
#we start by importing the pathlibrary and class path.
#alot can be done with the path object;
    #check the file exists before working with it
    #read files contents
    #write data to the file
#we build a path object representing the file pi_digits.txt,
#which we assign to the variable path

#
#VS code looks for files in the folder that was most recently opened,
#you can see root on terminal eg, so write path from that
#
#

#we use read_text() method to read the entire contents of the file
#for instances when an extra blank line etc at the end of the output we can use
#rstrip() on the contents string;

#contents = path.read_text().rstrip()
#the above cleans the string when string is assigned to variable.
    #the act of chaining methods like this is method chaining, often used in
    #programming
    
##RELATIVE AND ABSOLUTE FILE PATHS##
#when you pass a simple filename python looks in the directory where that files
#currently being executed (that is, your program file) is stored

#sometimes the file you want to open, wont be in the directory of your program file
#for example, a file is in a different folder.

#two main ways to specifiy programming:

#RELATIVE FILE PATH
    #tells python to look for a given location relative to the directory where the
    #currently running program is stored
    #since file_reader is in notes folder, which is in 10 files and exceptions,
    #we build the path as above
    
#ABSOLUTE FILE PATH
    #you can also tell the program exactly where the files are
    #used when relative file path doesnt work, so you specify the path absolutely
    #so you would often go sys root folder eg:
    #D:/python_work_learning/10 files and exceptions/notes/pi_digits.txt
    
##**windows systems use a backslash (\) instead of a forward slash (/) when displaying
#file paths, but always use forward slashes (/)


##Accessing a files lines##

#examine each line 
    #might be looking at certian information about a file, or modify a text in the
    #file a certian way
        #eg read through a file of weather data and work with any line that
        #includes the word sunny in the description
    
#using the splitlines() method to turn a long string into a set of lines
    #and then use a for loop to examine each line from a file, one at a time
    
# from pathlib import Path

# path = Path('10 files and exceptions/notes/pi_digits.txt')
# contents = path.read_text().rstrip()

# lines = contents.splitlines()

# for line in lines:
#     print(line)
    
#since we havent modified any lines, the output remains the same anyways

##working with a files contents##
#after you've read the contents of a file into memory, you can do whatever you
#want with that data
#build a single string containing all the digits in the with no whitespace

# from pathlib import Path

# path = Path('10 files and exceptions/notes/pi_digits.txt')
# contents = path.read_text().rstrip()
# lines = contents.splitlines()
# print(contents)
# print(lines)
# pi_string  = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

#we split the llines of the contents and assign it to variable lines
#we create a new variable called pi_string
#create a for loop to add into the string the 3 list lines and strip whitspace
#lstrip()

#when python reads from a text file, inteprets all text in the file as as string
#if you read in a number and want to work with that value in a numerical context,
#you have to convert it to an integer int() function or a float using the 
#float() function

##LARGE FILES: ONE MILLION DIGITS##
#code examples reference larger numbers.
#pi to 1_000_000 decimal places, we can create a single string containing all these
#digits. we'll also print just the first 50 decimal places, so no million digits
#scroll in terminal

from pathlib import Path

path = Path('10 files and exceptions/notes/pi_millions_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()
# print(contents)
# print(lines)
pi_string  = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string[:52])
print(len(pi_string))

##birthday contained in pi##
#example of finding out if birthday is in number format mmddyy

birthday = input("enter your birthday, in the form of mmddyy:")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi")
else:
    print("does not appear in the first million digits of pi")
    










