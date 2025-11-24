##EXCEPTIONS##

#python uses special objects called exceptions
    #to manage errors that occurs that makes python unsure what to do next
    #(it creates an exception object)
    
#if you write code that handles an exception, the program will continue running
#if you don't handle the exception, the program will halt and show a traceback,
#which includes a report of the exception that was raised

#exceptions are handled with try-except blocks
    #a try-except block asks python to do something, but it also tells python what 
    #to do if an exception was raised
    
#when you use try-except blocks, your porgrams will continue running even if things
#start to go wrong. instead of tracebacks, which can be confusing ofr users to read,
#users will see friendly error messages that you've written

#handling the zerodivisionerror exception#

#you cant divide a number by zero, eg
# (print(5/0))

#the error reported in the traceback, ZeroDivisionError is an exception object
#python creates this object in response to a situation where it cant do what we ask
#it to do

#when this happens, python stops the program and tells us the kind of exception that
#was raised

#we can use this formation to modify the program
#we'll tell python what to do when the kind of exception occurs: that way, if it
#happens again, we'll be prepared

##Using try-except blocks##

#when you think an error will occur, you can write a try-except block to handle
#the exception that might be raised

#tell python to run some code, and you tell it what to do if the code results in a 
#particular kind of exception

#heres what a try-except block for handling a ZeroDivisionError exception looks like

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you cant divide by zero!")
    
#we put expected error in the try block
#if the code in try block causes an error, python looks for an except block
#whos error matches that which was raised,
#and runs the code in that block.

#in this eg, code in the try block produces a ZeroDivisionError,
#so python looks for an except block telling it how to respond.

#python then runs the code in that block, and user sees a friendly erorr message
#instead of a traceback

#if more code followed the try-except block, program would continue running
#as we told python how to handle the error

#below is an example where catching an error can allow a program to continue running

##Using eceptions to Prevent crashes##

#handling errors correctly is especially important when the program has more 
#work to do after the error occurs.
#this happens often in programs that prompt users for input
#if the program responds to invalid input appropiately, it can prompt for more valid
#input instead of crashing

print("give me two numbers, and ill divie them")
print("enter 'q' to quit")

while True:
    first_number = input("\nfirst number: ")
    if first_number == 'q':
        break
    second_number = input("second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(answer)
        
#the only code that should go in a try block is code that might cause an exception
#to be raised. sometimes, additional code that should run only if the try block was successful;
#this code goes into the else block
#the except block tells python what to do in case of a certian exception arises
#when it tries to run the code in the try block

#by anticipating likely sources of errors, you can write robust programs that 
#continue to run even when they encounter invalid data and missing resources
#code will be resistant to innocent user mistakes and malicious attacks

        
