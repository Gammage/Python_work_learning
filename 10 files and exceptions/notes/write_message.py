##WRITING TO A FILE##
#one of the simplest ways to save data is to write to a file
#when you write a text to a file, output will still be available after you close the
#terminal containing your files output

#you can examine output after a program finishes running, and share output files with 
#others as well
#you can also write programs that read the text back into memory and work with it 
#again later

##Writing a single line##

# from pathlib import Path

# path = Path('./10 files and exceptions/notes/programming.txt')
# path.write_text("I love programming")

#write text method takes a single argument - string you want to write to the file
#file behaves like any other file on your computer. you can open it, write new 
#text in it, copy, paste etc

#python can only write strings to a text file
    #if want to store numerical data, convert data to string format first using
    #the str() function
    
##Writing multiple lines##

#write_text() method does a few things:
    #if the file that path points to doesnt exist, it creates that file
    #after writing the string to the file, it makes sure file is closed properly
        #files that arent closed can lead to missing or corrupted data

#to write more then one line to a file, you need to build a string containing the
#entire contents of file. then call write_text() with that string. eg

from pathlib import Path

path = Path('./10 files and exceptions/notes/programming.txt')


contents = "I love programming .\n"
contents += 'I love creating new games.\n'
contents += "i also love working with data."

path.write_text(contents)

#be careful when writing write_text() on a path object. if file already exists,
#write_text() will erase the current contents of the file and write new contents to
#the file.



